---
title: 決定木
---

# 決定木とは

分類問題や回帰問題を解くアルゴリズムの1つ。

# 用語

## 不純度（Impurity）

対象とする集団に、異なるクラスラベルのサンプルがどの程度の割合で混ざっているかを表す指標。  
純粋（最も純粋 = サンプル全てが同じクラスラベル）であるほど低くなる。

不純度として具体的に以下のような指標が用いられる。

| 指標 | 定義 | 備考 |
| :-- | :-- | :-- |
| ジニ不純度 | $$I_G \equiv 1 - \displaystyle \sum_c p(c)^2$$ |  |
| 情報エントロピー | $$I_H \equiv - \displaystyle \sum_c p(c) \log_{n_c} p(c)$$ | エントロピーの対数の底は実は何でも良いが、$$n_c$$ を底に取ると最大値が1になるので扱いやすい |
| 分類誤差 | $$I_E \equiv 1 - \max p(c)$$ | 一番多いラベルが正しいと仮定したときの誤分類率 |

- $c$: 集団に **実際に1件以上含まれる** クラスのラベル
  - $n_c$: その種類数
- $p(c)$: 集団内のクラスラベル $c$ の割合


## 情報利得（Information Gain）

ある集団を複数に分割した時の、分割前後の不純度の差。  
つまり、**ある分割による情報利得が大きい = その分割を行うと不純度を大きく下げることができる**。

$$
IG(D_p) \equiv I(D_p) - \displaystyle \sum_{j=1}^m \cfrac{N_j}{N_p} I(D_j)
$$

- $I$: 不純度
- $D_p$: 分割前の集団
- $D_j$: 分割後の $j$ 番目の集団
- $m$: 集団を分割する個数
- $N_p$: $D_p$ に属するサンプル数
- $N_j$: $D_j$ に属するサンプル数


# 決定木による分類

## 問題設定

入力値（特徴量） $x_1, \cdots, x_m$ に対し、分類ラベル $y$ を出力するモデルを作る。

## 学習規則

学習サンプル全体に対応するルートノードから始めて決定木を育てていく。  

1. 集団を、情報利得が最大となるように分割
    - 特徴量の1つ $$f$$ を選択し、$$f$$ の値が閾値以上か否かで集団を分ける
        - 分割の閾値は、集団内の $$f$$ の値をソートし、隣同士の中間の値を取ると良い
        - $$n$$ 分割の場合は $$n-1$$ 個の閾値を選ぶ必要がある
    - 全ての特徴量・閾値の中で一番情報利得が大きくなるものを見つけ、その特徴量と閾値を今いるノードに記録
    - 分割された各集団を今いるノードの子ノードとする
2. 分割後の各子ノードについても、再帰的に1を繰り返す
3. どのように分割しても情報利得がゼロになる（= 分割しても不純度が下がらない）状態になったら終了、その時の集団内で多数決により代表ラベルを決定、ノードに記録する（ここが決定木の「葉」となる）

> **【NOTE】**
>
> 決定木が深くなるほど決定境界が複雑になり、容易に過学習に陥る。  
> これを防ぐため、以下のような対策を講じることが多い。
> - 決定木の深さ（= 分割回数）に上限を設ける
> - 葉の最小サイズ（サンプル数）を設定し、それより少ないサンプル数には分割できないようにする

## ラベル判定

学習済みの決定木を使い、未知の入力データのラベル判定を行う手順を示す。

1. ルートノードへ移動
2. 今いるノードに記録された、分割に使う特徴量 $$f$$ と閾値を確認
3. 入力データの $$f$$ の値と閾値とを比べ、対応する子ノードへ移動
4. 葉に到達するまで 2, 3 を繰り返す
5. 葉に記録された代表ラベルを返す


## 実装

### コード

{% gist f48fc2b0f1adb9adc10ad8badecf1254 decision-tree.py %}


### 動作確認

{% gist f48fc2b0f1adb9adc10ad8badecf1254 fit1.py %}

![過学習](https://user-images.githubusercontent.com/13412823/79865383-0a967180-8416-11ea-9329-bf1107272cb7.png)

→ 外れ値に対して過学習の傾向が見られる

![過学習回避](https://user-images.githubusercontent.com/13412823/79865392-0d916200-8416-11ea-97a3-9171a5c84e3f.png)

→ 葉が持つべきサンプル数の最小値設定により、過学習が抑えられる

![決定木](https://user-images.githubusercontent.com/13412823/79865497-39ace300-8416-11ea-9bbe-0fdaeaddee73.png)


{% gist f48fc2b0f1adb9adc10ad8badecf1254 fit2.py %}

![過学習回避・同心円](https://user-images.githubusercontent.com/13412823/79865396-0e29f880-8416-11ea-85a2-88c18628face.png)

![決定木・同心円](https://user-images.githubusercontent.com/13412823/79865503-3c0f3d00-8416-11ea-97f6-8e252d56cd25.png)


# ランダムフォレストによる分類

アンサンブル学習の手法、**バギング** の一種。  
複数の決定木で多数決を取ることにより、汎化性能を高める。

## 学習規則

1. 全データサンプル $$N$$ 個のうち $$n(<N)$$ 個をランダムに抽出
2. 特徴量 $$M$$ 個のうち $$m(<M)$$ 個をランダムに抽出
3. 抽出した $$n$$ 個のデータサンプルを学習データとして、$$m$$ 個の特徴量だけを使って決定木を構築
4. 1-3 を繰り返し、複数の決定木を作る

## ラベル判定

入力データに対して各決定木でラベル判定を行い、その多数決で最終的なラベルを決定する。

## 実装

### コード

{% gist f48fc2b0f1adb9adc10ad8badecf1254 random-forest.py %}

### 動作確認

{% gist f48fc2b0f1adb9adc10ad8badecf1254 fit-rf.py %}

![Unknown](https://user-images.githubusercontent.com/13412823/80094585-79540600-85a1-11ea-927f-963d7b2b5aef.png)

![Unknown-1](https://user-images.githubusercontent.com/13412823/80094582-78bb6f80-85a1-11ea-90d4-38cd91bf6862.png)

![Unknown-2](https://user-images.githubusercontent.com/13412823/80094579-778a4280-85a1-11ea-9831-a751edb7d307.png)

# 決定木・ランダムフォレストによる回帰

## 問題設定

変数 $$x_1, \cdots, x_m$$ から目的変数 $$y$$ の値を予測するモデルを作る。

## 学習規則

基本的に分類問題と同様。
- 不純度の代わりに、教師データと予測値との誤差平方和 $$\displaystyle \sum_i (y^{(i)} - \hat{y}^{(i)})^2$$ が最小となるようにノードを分割する
- 代表ラベルの代わりに、ノードに属する集団の平均値を代表値としてノードに記録する

## 実装

### コード

決定木による回帰：

{% gist 20087921f74025506ad5c68505ff792a decision-tree-regression.py %}

ランダムフォレストによる回帰：

{% gist 20087921f74025506ad5c68505ff792a random-forest-regression.py %}

### 動作確認

{% gist 20087921f74025506ad5c68505ff792a ~fit.py %}

![Decision Tree Regression](https://user-images.githubusercontent.com/13412823/81375706-0b7d1200-913d-11ea-8bcd-226d78ed2ab9.png)
