---
title: k-means
---

# k-means とは

プロトタイプベースのクラスタリング手法の1つ。

## 問題設定

与えられたデータセットを $$k$$ 個のクラスタに分割する。


## 処理の流れ

1. 与えられたデータセット $$\boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)}$$ のうち $$k$$ 個を **セントロイド** としてランダムに選択
    - 以後、セントロイドは $$\boldsymbol{\mu}^{(1)}, \cdots, \boldsymbol{\mu}^{(k)}$$ で表す
    - セントロイド $$\boldsymbol{\mu}^{(j)}$$ は $$j$$ 番目のクラスタ $$C^{(j)}$$ に対応する
2. 各データサンプル $$\boldsymbol{x}^{(i)}$$ に対して、各セントロイド $$\boldsymbol{\mu}^{(j)}$$ からのユークリッド距離 $$d\left(\boldsymbol{x}^{(i)}, \boldsymbol{\mu}^{(j)}\right)$$ を計算
    - $$d\left(\boldsymbol{x}^{(i)}, \boldsymbol{\mu}^{(j)}\right)^2 = \left\| \boldsymbol{x^{(i)}} - \boldsymbol{\mu}^{(j)} \right\|^2$$
3. 各データサンプルを、距離が一番近いセントロイド（に対応するクラスタ）に所属させる
4. 各クラスタに所属する全データの重心（平均）を取り、それを新しいセントロイドとする
    - $$\boldsymbol{\mu}^{(j)} \longleftarrow \cfrac{1}{|C^{(j)}|} \displaystyle \sum_{\boldsymbol{x}^{(i)} \in C^{(j)}} \boldsymbol{x}^{(i)}$$
5. 条件を満たすまで2〜4を繰り返す
    - セントロイドが変化しなくなる or 変化量がユーザ定義の許容値を下回る
    - ユーザ定義のイテレーション回数を超える


## 注意

- ユークリッド距離を用いるため、変数のスケールを事前に揃えておく必要がある
- はじめにハイパーパラメータ $$k$$ を指定する必要があり、適切な $$k$$ を選ばないと性能が悪くなる


## 実装

### コード

{% gist 205917c3a344ee1aaeb82ef37847bc97 k-means.py %}

### 動作確認

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~fit-k-means1.py %}

![KMeans-Circle](https://user-images.githubusercontent.com/13412823/81466743-da6d1200-920e-11ea-857d-b2ce48cf3117.png)

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~fit-k-means2.py %}

![KMeans-Square](https://user-images.githubusercontent.com/13412823/81466745-dc36d580-920e-11ea-9240-cbc8ffc8db5f.png)
