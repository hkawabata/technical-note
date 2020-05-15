---
title: k-means
---

# k-means とは

プロトタイプベースのクラスタリング手法の1つ。  
通常の k-means は、各データサンプルに対して1つだけ所属クラスタを割り当てる **ハードクラスタリング**。

## 問題設定

与えられたデータセットを $$k$$ 個のクラスタに分割する。


## 処理の流れ

1. 与えられたデータセット $$\boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)}$$ のうち $$k$$ 個をランダムに選択して **セントロイド** $$\boldsymbol{\mu}^{(1)}, \cdots, \boldsymbol{\mu}^{(k)}$$ の初期値とする
    - セントロイド $$\boldsymbol{\mu}^{(j)}$$ は $$j$$ 番目のクラスタ $$C^{(j)}$$ に対応する
2. 各データサンプル $$\boldsymbol{x}^{(i)}$$ に対して、各セントロイド $$\boldsymbol{\mu}^{(j)}$$ からのユークリッド距離 $$d\left(\boldsymbol{x}^{(i)}, \boldsymbol{\mu}^{(j)}\right)$$ を計算
    - $$d\left(\boldsymbol{x}^{(i)}, \boldsymbol{\mu}^{(j)}\right)^2 = \left\| \boldsymbol{x^{(i)}} - \boldsymbol{\mu}^{(j)} \right\|^2$$
3. 各データサンプルを、距離が一番近いセントロイド（に対応するクラスタ）に所属させる
4. 各クラスタに所属する全データの重心（平均）を求め、その座標を新しいセントロイドとする
    - $$\boldsymbol{\mu}^{(j)} \longleftarrow \cfrac{1}{|C^{(j)}|} \displaystyle \sum_{\boldsymbol{x}^{(i)} \in C^{(j)}} \boldsymbol{x}^{(i)}$$
5. 条件を満たすまで2〜4を繰り返す
    - セントロイドが変化しなくなる or 変化量がユーザ定義の許容値を下回る
    - ユーザ定義のイテレーション回数を超える


## 注意

- ユークリッド距離を用いるため、変数のスケールを事前に揃えておく必要がある
- はじめにハイパーパラメータ $$k$$ を指定する必要があり、適切な $$k$$ を選ばないと性能が悪くなる
- 下図のように、乱数による初期化が不適切だとクラスタリングがうまくいかない場合がある
  - 初期化方法を改善した k-means++ という手法がある

![bad k-means](https://user-images.githubusercontent.com/13412823/81996885-3ad5d680-9689-11ea-834b-06be4d843a45.png)


## 実装

### コード

{% gist 205917c3a344ee1aaeb82ef37847bc97 k-means.py %}

### 動作確認

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~plot-k-means.py %}

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~fit-k-means1.py %}

![KMeans-Square](https://user-images.githubusercontent.com/13412823/81466745-dc36d580-920e-11ea-9240-cbc8ffc8db5f.png)

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~fit-k-means2.py %}

![KMeans-Circle](https://user-images.githubusercontent.com/13412823/81466743-da6d1200-920e-11ea-857d-b2ce48cf3117.png)


# Fuzzy C-means (FCM)

各データサンプルを複数のクラスタに割り当てる **ソフトクラスタリング** 手法で、k-means の改善版。  
**Soft k-means** または **Fuzzy k-means** とも呼ばれる。

## 問題設定

与えられたデータセットを $$k$$ 個のクラスタに分割する。  
各データセットが属するクラスタを1つ決めるのではなく、各クラスタに属する確率を求める。

## 処理の流れ

1. 各データサンプルの各クラスタへの帰属度（所属確率のようなもの）を乱数で初期化し、**セントロイド** $$\boldsymbol{\mu}^{(1)}, \cdots, \boldsymbol{\mu}^{(k)}$$ の初期値を計算
2. 各データサンプル $$\boldsymbol{x}^{(i)}$$ に対して、各セントロイド $$\boldsymbol{\mu}^{(j)}$$ への帰属度を計算
3. 各セントロイドへの帰属度を重みとして重み付き重心（平均）を求め、次のセントロイドを計算
4. 条件を満たすまで2〜3を繰り返す
    - セントロイドが変化しなくなる or 変化量がユーザ定義の許容値を下回る
    - ユーザ定義のイテレーション回数を超える

新たなハイパーパラメータとして、クラスタの **ファジー係数** $$m\ (\gt 1)$$ を導入する。  
$$m$$ が大きいほど、各クラスタへの帰属度が広く分散してクラスタの境界が曖昧（ファジー）になる。

データサンプル $$\boldsymbol{x}^{(i)}$$ が $$\boldsymbol{\mu}^{(j)}$$ に所属する帰属度 $$w^{(i,j)}$$ は、

$$
w^{(i,j)} = \left\{ \displaystyle \sum_{c=1}^k \left( \frac{\left\| \boldsymbol{x^{(i)}} - \boldsymbol{\mu}^{(j)} \right\|^2}{\left\| \boldsymbol{x^{(i)}} - \boldsymbol{\mu}^{(c)} \right\|^2} \right)^{\frac{1}{m-1}} \right\}^{-1}
$$

セントロイド更新の式は、

$$
\boldsymbol{\mu}^{(j)} \longleftarrow \displaystyle \cfrac{\sum_{i=1}^n \left(w^{(i,j)}\right)^m \boldsymbol{x}^{(i)}}{\sum_{i=1}^n \left(w^{(i,j)}\right)^m}
$$

> **【NOTE】**
>
> - k-means の1ステップ目：データサンプルから最初のセントロイドをランダムに選ぶ
> - FCM の1ステップ目：各データサンプルの各クラスタへの所属確率をランダムに決める
>
> FCM で実際のデータ点からセントロイドを選んでしまうと、その点とセントロイドの距離がゼロになり、$$w^{(i,j)}$$ の計算時にゼロ除算が発生してしまって困るから...？


## 実装

### コード

{% gist 205917c3a344ee1aaeb82ef37847bc97 fcm.py %}

### 動作確認

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~fit-fcm.py %}

![FCM](https://user-images.githubusercontent.com/13412823/82025160-e7d14300-96cb-11ea-9d7c-999f27824701.png)

→ $$m$$ が大きいほど確率が分散していることが確認できる
