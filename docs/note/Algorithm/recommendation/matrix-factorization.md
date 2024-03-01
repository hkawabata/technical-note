---
title: 行列分解
title-en: Matrix Factorization
---
# 概要

**Matrix Factorization（MF, 行列分解）** は、レコメンデーションタスクにおける、協調フィルタリングのための次元圧縮手法。

ユーザ数 $m$、アイテム数 $n$ のデータにおいて、ユーザ $i$ がアイテム $j$ につけた評価値 $r_{i,j}$ を並べた $m \times n$ 評価値行列

$$
R = \begin{pmatrix}
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

レコメンドシステムを採用したいサービスにおいては、「全てのユーザが全てのアイテムを評価済み」ということはない（ユーザがまだ評価していない、知らないものを推薦するのがモチベーション）ので、$r_{i,j}$ には null 値が含まれる。

ユーザ要素を $k$ 次元（$0 \lt k \lt n,m$）の列ベクトルで表して人数分並べた行列

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

と、$U$ 同様にアイテム要素を $k$ 次元の列ベクトルで表してアイテムの個数分並べた行列

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

を用いて、$R$ を

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

の形に分解する。$\hat{R}, \hat{r}_{i,j}$ のハット記号は推定値であることを表す。

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
    \left( V \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)^T \right)_{x,y} +
    \lambda U_{x,y}
    \\ &=&
    \left( V \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right)^T + \lambda U \right)_{x,y}
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
    \left( U \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right) \right)_{x,y} +
    \lambda V_{x,y}
    \\ &=&
    \left( U \left( \mathrm{putZero}(\hat{R} - R; r_{i,j} = null) \right) + \lambda V \right)_{x,y}
    \tag{8}
\end{eqnarray}
$$

途中で導入した演算 $\mathrm{putZero}(\hat{R}-R; r_{i,j} = null)$ は、行列 $\hat{R}-R$ の成分のうち $r_{i,j}=null$ であるような $i,j$ 成分をゼロに置き換える操作を表す。  
これにより、$j \in \{ r_{y,j} \ne null \}$ のような扱いにくい条件下の和を全ての $j$ の和に置き換えている。

ランダムな値で初期化した $U, V$ を勾配降下法などを用いて最適化すれば、$(4)$ 式により、null 値が推定値で埋まった評価値行列 $\hat{R}$ が得られる。


> **【NOTE】特異値分解 (Singular Value Decomposition, SVD) との比較**
> 
> レコメンドシステムにおける次元圧縮に特異値分解を利用しても性能は良化しない（むしろ悪くなることもある）。
> レコメンドにおいて次元削減の対象となるのは評価値行列だが、評価値行列には null 値が含まれる。null を0で補完することもできるが、この場合の0は一般には「評価値が0」ではなく「まだ評価していない」ことを表す。
> したがって、この0という情報をそのまま数値通りに使って（つまり、低評価をつけたという解釈をして）次元削減を行うと、実態とは異なる最適化が行われてしまう。
> 一方で、Matrix Factorization は値があるところのみで最適化していくので、レコメンドにはこちらの方が有効。


## 過学習の防止

以下のようにすれば過学習を検知できそう。

- 実際の評価値のうち一定割合をテストデータに選ぶ
- テストデータをマスクして null に変換した評価値行列で学習
- 学習の結果得られた予測評価値行列に関して、学習データとテストデータ両方の損失関数をモニターして学習曲線を描く


# 実装

{% gist d987349fcbef6b652d5c66acbc1f405f matrix-factorization.py %}

## 全てを学習データに利用

{% gist d987349fcbef6b652d5c66acbc1f405f ~test1.py %}

![mf](https://gist.github.com/assets/13412823/6053d6de-1bc3-4eff-ba8f-03e9f130f7c2)


## 一部を評価用テストデータに利用

{% gist d987349fcbef6b652d5c66acbc1f405f ~test2.py %}

![mf](https://gist.github.com/assets/13412823/61f01f91-3b9d-4ed9-881e-43bdbab912bf)
