---
title: 行列分解
title-en: Matrix Factorization
---
# 概要

**Matrix Factorization（MF, 行列分解）** は、レコメンデーションタスクにおける、協調フィルタリングのための次元圧縮手法。

## 問題設定

ユーザ数 $m$、アイテム数 $n$ のデータにおいて、ユーザ $i$ がアイテム $j$ につけた評価値 $r_{i,j}$ を並べた $m \times n$ 評価値行列（rating 行列）

$$
R := \begin{pmatrix}
    r_{1,1} & r_{1,2} & & \cdots & & r_{1,n-1} & r_{1,n} \\
    r_{2,1} & & & & & & r_{2,n} \\
    \\
    \vdots & & & \ddots & & & \vdots \\
    \\
    r_{m-1,1} & & & & & & r_{m-1,n} \\
    r_{m,1} & r_{m,2} & & \cdots & & r_{m,n-1} & r_{m,n}
\end{pmatrix}
\tag{1}
$$

を考える。この例では行がユーザ、列がアイテムに対応。

レコメンドシステムを採用する目的は「ユーザがまだ評価していない、知らないものを推薦する」ことであるから、「全てのユーザが全てのアイテムを評価済み」という状況は起こらないと思って良い。  
さらに言えば、ユーザ数もアイテム数も非常に大きいことが多く、一般にはユーザが触れたことのないアイテム、すなわち未評価であることの方が多い。  
つまり、評価値行列 $R$ のほとんどの要素 $r_{i,j}$ は値を持たない（null）。

ユーザ $i$ が未評価のアイテム $j$ をどう評価するか（= $r_{i,j}$ の推定値）を求めて、それが高いものをユーザに推薦したい。


## Matrix Factorization のアプローチ

評価値行列 $R$ の各要素 $r_{i,j}$ を直接推定しようとすると、およそ $m \times n$ 個の要素を求める必要がある。  
前述の通り、一般に $R$ の要素のほとんどが未知なので、非常に少ない既知の値から、非常に多数の未知のパラメータを求めることになり、推定精度の面で懸念が大きい。

そこで Matrix Factorization では、評価値行列 $R$ の要素 $r_{i,j}$ を直接推定するのではなく、ユーザ $i$、アイテム $j$ それぞれの $k$ 次元ベクトル表現 $\boldsymbol{u}_i, \boldsymbol{v}_j$ を求め、その内積で $r_{i,j}$ の推定値 $\hat{r}_{i,j}$ を表現することで次元圧縮を図る：

$$
\hat{r}_{i,j} =
\boldsymbol{u}_i^T \boldsymbol{v}_j
$$

ここで

- ユーザベクトルの全パラメータ数はユーザ数 $m$ とベクトル次元 $k$ の積 $= km$
- アイテムベクトルの全パラメータ数はアイテム数 $n$ とベクトル次元 $k$ の積 $= kn$

なので、$k \ll m,n$ となるように $k$ を設定することで、求める全パラメータ数 $k(m+n)$ は直接 $r_{i,j}$ を求める場合の $m \times n$ に比べて大幅に小さくできる。


## ユーザ・アイテムの行列表現

計算の都合上、実際に数値計算で求めるのは、ユーザ列ベクトルを人数分並べた行列

$$
U =
(\boldsymbol{u}_1, \cdots, \boldsymbol{u}_m)
=
\begin{pmatrix}
    u_{1,1} & u_{1,2} & & \cdots & & u_{1,m-1} & u_{1,m} \\
    \vdots & & & \ddots & & & \vdots \\
    u_{k,1} & u_{k,2} & & \cdots & & u_{k,m-1} & u_{k,m}
\end{pmatrix}
\tag{2}
$$

と、同じくアイテム列ベクトルをアイテムの個数分並べた行列

$$
V =
(\boldsymbol{v}_1, \cdots, \boldsymbol{v}_n)
=
\begin{pmatrix}
    v_{1,1} & v_{1,2} & & \cdots & & v_{1,n-1} & v_{1,n} \\
    \vdots & & & \ddots & & & \vdots \\
    v_{k,1} & v_{k,2} & & \cdots & & v_{k,n-1} & v_{k,n}
\end{pmatrix}
\tag{3}
$$

となる。これらの行列を用いて、評価値行列 $R$ の推定値の行列 $\hat{R}$ は以下の形で表現できる：

$$
R \simeq \hat{R} = U^T V
=
\begin{pmatrix}
    u_{1,1} & \cdots & u_{k,1} \\
    u_{1,2} & & u_{k,2} \\
    \vdots & \ddots & \vdots \\
    u_{1,m-1} & & u_{k,m-1} \\
    u_{1,m} & \cdots & u_{k,m}
\end{pmatrix}
\begin{pmatrix}
    v_{1,1} & v_{1,2} & & \cdots & & v_{1,n-1} & v_{1,n} \\
    \vdots & & & \ddots & & & \vdots \\
    v_{k,1} & v_{k,2} & & \cdots & & v_{k,n-1} & v_{k,n}
\end{pmatrix}
\tag{4}
$$

$$
r_{i,j} \simeq \hat{r}_{i,j} =
\boldsymbol{u}_i^T \boldsymbol{v}_j
= \sum_{l=1}^k u_{l,i} v_{l,j}
\tag{5}
$$

最適な $U, V$ を求めることで、
- 推定評価値行列 $\hat{R}$ を計算し、$r_{i,j} = null$ な $i,j$（つまりそのユーザが未評価アイテム）について推定評価値 $\hat{r}_{i,j} \ne null$ が高い順にレコメンドができる
- ユーザやアイテムの低次元なベクトル表現も得られるので、これを利用してユーザベース、アイテムベースのレコメンドにも利用できる


# 理論

## 学習の方法

損失関数 $L$ を下式で定義する：

$$
\begin{eqnarray}
    L &:=&
    \cfrac{1}{2}
    \sum_{(i,j) \in \{r_{i,j} \ne null\}} \left( \hat{r}_{i,j} - r_{i,j} \right)^2 +
    \cfrac{\lambda}{2} \left( \sum_{i=1}^m \vert \boldsymbol{u}_i \vert^2 + \sum_{j=1}^n \vert \boldsymbol{v}_j \vert^2 \right)
    \\ &=&
    \cfrac{1}{2}
    \sum_{(i,j) \in \{r_{i,j} \ne null\}} \left( \sum_{l=1}^k u_{l,i} v_{l,j} - r_{i,j} \right)^2 +
    \cfrac{\lambda}{2} \left( \sum_{i=1}^m \sum_{l=1}^k u_{l,i}^2 + \sum_{j=1}^n \sum_{l=1}^k v_{l,j}^2 \right)
    \tag{6}
\end{eqnarray}
$$

- 第1項：正解（実際にユーザがアイテムを評価した評価値）と推定値の誤差二乗和
- 第2項：過学習を防ぐための正則化項。パラメータ $\lambda \gt 0$ で強さを調整

係数の $1/2$ は以下の勾配の計算結果を単純にするため付与している。

この損失関数を最小化するような $U, V$ を求めたい。
$L$ を $u_{x,y},v_{x,y}$ で偏微分すると、

$$
\begin{eqnarray}
    \cfrac{\partial L}{\partial u_{x,y}}
    &=&
    \sum_{j \in \{r_{y,j} \ne null\}} v_{x,j} \left( \sum_{l=1}^k u_{l,y} v_{l,j} - r_{y,j} \right) +
    \lambda u_{x,y}
    \\ &=&
    \sum_{j \in \{r_{y,j} \ne null\}} v_{x,j} \left( \boldsymbol{u}_{y}^T \boldsymbol{v}_{j} - r_{y,j} \right) +
    \lambda u_{x,y}
    \\ &=&
    \sum_{j \in \{r_{y,j} \ne null\}} V_{x,j} \left( \hat{R} - R \right)_{y,j} +
    \lambda U_{x,y}
    \\ &=&
    \sum_{j=1}^n V_{x,j} \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)_{y,j} +
    \lambda U_{x,y}
    \\ &=&
    \left\{ V \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)^T \right\}_{x,y} +
    \lambda U_{x,y}
    \\ &=&
    \left\{ V \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)^T + \lambda U \right\}_{x,y}
    \tag{7}
    \\
    \\
    \cfrac{\partial L}{\partial v_{x,y}}
    &=&
    \sum_{i \in \{r_{i,y} \ne null\}} u_{x,i} \left( \sum_{l=1}^k u_{l,i} v_{l,y} - r_{i,y} \right) +
    \lambda v_{x,y}
    \\ &=&
    \sum_{j \in \{r_{i,y} \ne null\}} u_{x,i} \left( \boldsymbol{u}_{i}^T \boldsymbol{v}_{y} - r_{i,y} \right) +
    \lambda v_{x,y}
    \\ &=&
    \sum_{j \in \{r_{i,y} \ne null\}} U_{x,i} \left( \hat{R} - R \right)_{i,y} +
    \lambda V_{x,y}
    \\ &=&
    \sum_{j=1}^n U_{x,i} \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)_{i,y} +
    \lambda V_{x,y}
    \\ &=&
    \left\{ U \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right) \right\}_{x,y} +
    \lambda V_{x,y}
    \\ &=&
    \left\{ U \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right) + \lambda V \right\}_{x,y}
    \tag{8}
\end{eqnarray}
$$

途中で導入した演算 $\mathrm{putZero}(\hat{R}-R; r_{i,j} = null)$ は、行列 $\hat{R}-R$ の成分のうち $r_{i,j}=null$ であるような $i,j$ 成分をゼロに置き換える操作を表す。  
これにより、$j \in \{ r_{y,j} \ne null \}$ のような扱いにくい条件下の和を全ての $j$ の和に置き換えている。

ランダムな値で初期化した $U, V$ を勾配降下法などを用いて最適化すれば、$(4)$ 式により、null 値が推定値で埋まった評価値行列 $\hat{R}$ が得られる。


## 特異値分解 (SVD) との比較

行列の次元圧縮の手法として特異値分解 (Singular Value Decomposition, SVD) も有名だが、レコメンドシステムに特異値分解を利用しても性能は良化しない（むしろ悪くなることもある）。

レコメンドにおいて次元削減の対象となるのは評価値行列だが、評価値行列には null 値が含まれる。これに特異値分解を適用する場合、null を0など適当な値で補完する必要があるが、この場合の0は一般には「評価値が0（低評価）」ではなく「まだ評価していない」ことを表す。  
したがって、この0という情報をそのまま数値通りに使って（つまり、低評価をつけたという解釈をして）次元削減を行うと、実態とは異なる最適化が行われてしまう。  
一方、Matrix Factorization は実際の評価値のみを使って最適化していくので、レコメンドにはこちらの方が有効。


## 過学習の防止

以下のようにすれば過学習を検知できそう。

- 実際の評価値のうち一定割合をテストデータに選ぶ
- テストデータをマスクして null に変換した評価値行列で学習
- 学習の結果得られた予測評価値行列に関して、学習データとテストデータ両方の損失関数をモニターして学習曲線を描く


# 実装

{% gist d987349fcbef6b652d5c66acbc1f405f matrix-factorization.py %}

## 全てを学習データに利用

{% gist d987349fcbef6b652d5c66acbc1f405f ~test1.py %}

![mf1](https://gist.github.com/assets/13412823/5e95352f-bb90-44ef-8ea3-371348c1914b)



## 一部を評価用テストデータに利用

{% gist d987349fcbef6b652d5c66acbc1f405f ~test2.py %}

![mf2](https://gist.github.com/assets/13412823/11e2ae5f-a89d-4412-9df5-506b239e1638)


テストデータも学習データも損失関数が減少しているので、うまく過学習が抑えられていそう。


## MovieLens データセットで検証

https://grouplens.org/datasets/movielens/ の ml-latest-small.zip (size: 1 MB) を使って検証。

{% gist 71dcf4b2f891c3c2a36bdf234b677d4e dataset-movielenz-small.py %}

```python
mm = MovieLenzManager('ml-latest-small', th_user=30, th_item=30)
R = mm.get_eval_matrix()
X_fm, y_fm = mm.get_Xy_fm()

model_mf = MatrixFactorization(R)
model_mf.fit(k=16, lamb=0.2, eta=1.0, T=100000, eps=1e-5, r_test=0.1)
model_mf.draw_loss()
```

![mf-movielenz](https://gist.github.com/assets/13412823/e5d3d96f-c477-4426-90a4-e067c9be5144)


baseline = 学習データの予測値を全て、既知の評価値の平均値で埋めた時の結果。  
学習曲線がこれよりも下にあるので、平均値で埋めるよりはマシなレコメンド、と言えそう。