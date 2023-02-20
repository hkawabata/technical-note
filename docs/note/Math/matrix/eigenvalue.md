---
title: 固有値と固有ベクトル
---

# 定義

$n$ 次正方行列 $A$ に対して、零ベクトルでない列ベクトル $\boldsymbol{u}$ と定数 $\lambda$ が存在し、

$$A \boldsymbol{u} = \lambda \boldsymbol{u}$$

が成立する時、

- $\lambda$：行列 $A$ の **固有値**
- $\boldsymbol{u}$：行列 $A$ の固有値 $\lambda$ に属する **固有ベクトル**

と呼ぶ。

# 図形的な意味

$A \boldsymbol{u} = \lambda \boldsymbol{u}$ の式から、**固有ベクトルを行列 $A$ により線形変換しても、定数倍されるだけで向きは変わらない。この「定数倍」の拡大倍率が固有値**。

具体例として

$$
A = \begin{pmatrix}
	4 & 1 \\
	-2 & 1
\end{pmatrix}
$$

を考えると、$A$ の固有値は $\lambda_1 = 2,\ \lambda_2 = 3$、対応する固有ベクトルは $\boldsymbol{u}_1=\begin{pmatrix} 1 \\ -2 \end{pmatrix},\ \boldsymbol{u}_2=\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ 

固有ベクトルやその他のベクトルの $A$ による変換を図に示す。

![Figure_1](https://user-images.githubusercontent.com/13412823/219907053-7bcda206-2409-4632-ae29-e0bfc5e211f9.png)

図より、
- 固有ベクトルを $A$ で変換すると長さが固有値倍されるだけで向きは変わらない
- 固有ベクトル以外を $A$ で変換すると向きが変わる

ことが分かる。

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/533b3f374d8f938316a63ad502a07914#file-20230219_linear-transform-eigenvector-py)

# 性質

## 固有値の存在保証

> **【定理】**
> 
> 任意の正方行列 $A$ には固有値 $\lambda$ と固有ベクトル $\boldsymbol{x}$ が存在する

**【証明】**

固有方程式

$$
\det (A - \lambda I) = 0
$$

は $\lambda$ の $n$ 次方程式であるから、$\lambda \in \mathbb{C}$ であるような解を持つ。

（ToDo：続き）

## 固有ベクトルは一意に定まらない

行列 $A$ の固有値の1つを $\lambda$、それに対応する固有ベクトルを $\boldsymbol{u}$ とする：

$$A \boldsymbol{u} = \lambda \boldsymbol{u}$$

ここで、$\boldsymbol{u}$ を定数倍したベクトル

$$\boldsymbol{v} := c \boldsymbol{u} \qquad (c = \mathrm{const.} \ne 0)$$

と考えると、

$$
A \boldsymbol{v} = A (c \boldsymbol{u}) = c(A \boldsymbol{u}) = c\lambda \boldsymbol{u} = \lambda \boldsymbol{v}
$$

なので、$\boldsymbol{v}$ も $\lambda$ に対する $A$ の固有ベクトルになっている。  
したがって、固有ベクトルには定数倍の自由度があり一意に定まらない。


## 固有ベクトルの線形独立性

> **【定理】**
> 
> 固有値の異なる固有ベクトルは、 互いに線形独立である

**【証明】**

（ToDo）


## 固有値の積と行列式

> **【定理】**
> 
> 行列式の値は固有値を全て掛けた値に等しい

**【証明】**

（ToDo）


# 計算方法

## 理論

### 固有値を求める

$I$ を単位行列とすると、

$$
\begin{eqnarray}
&&A \boldsymbol{u} = \lambda \boldsymbol{u} \\
& \Longleftrightarrow &\left( A - \lambda I \right) \boldsymbol{u} = \boldsymbol{0}
\end{eqnarray}
$$

これが $\boldsymbol{u} = \boldsymbol{0}$ 以外の解を持つためには、行列 $\left( A - \lambda I \right)$ は逆行列を持ってはならない。
つまり行列式の値がゼロ：

$$
\det \left( A - \lambda I \right) = 0
$$

この $n$ 次方程式（**固有方程式**）を解くことで、固有値 $\lambda$ が得られる。

$A$ の相異なる固有値を $\lambda_1, \cdots, \lambda_d$ とすると、固有方程式の左辺は

$$
(\lambda - \lambda_1)^{r_1} (\lambda - \lambda_2)^{r_2} \cdots (\lambda - \lambda_d)^{r_d} = 0
$$

と因数分解される。このとき、$r_k$ を固有値 $\lambda_k$ の **重複度** という。

> **【定理】**
> 
> 固有値 $\lambda$ の重複度が $r$ であるとき、$\lambda$ に属する固有ベクトルが持つ自由度のパラメータの個数は $r$ に一致する


### 固有ベクトルを求める

固有値 $\lambda$ に対応する固有ベクトルを求めるには、固有値・固有ベクトルの定義式

$$
A \boldsymbol{u} = \lambda \boldsymbol{u}
$$

に $\lambda$ を代入し、$\boldsymbol{u} = \left(u_1, u_2, \cdots, u_n \right)^T$ の各成分の連立方程式として解けば良い。

ただし、固有ベクトルには定数倍の自由度があるため一意には定まらず、定数 $k, l$ などを用いて

$$
\boldsymbol{u} = k \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}
$$

あるいは

$$
\boldsymbol{u} =
k \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} +
l \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}
$$

のような形で求まる。

※ 式に現れる定数の個数は固有値の重複度以下


## 具体例

### 例題1：固有値の重複度が全て1

$$
A =
\begin{pmatrix}
0  & -1 & -3 \\
2  & 3  & 3  \\
-2 & 1  & 1
\end{pmatrix}
$$

#### 固有値

固有方程式は、

$$
\det
\begin{pmatrix}
-\lambda  & -1 & -3 \\
2  & 3-\lambda & 3  \\
-2 & 1  & 1-\lambda
\end{pmatrix}
= 0
$$

よって

$$
\begin{eqnarray}
  &
  -\lambda \{(3-\lambda)(1-\lambda) - 3 \cdot 1 \}
  -1 \{3 \cdot (-2) - 2 (1-\lambda)\}
  -3 \{ 2 \cdot 1 - (3-\lambda) \cdot (-2) \}
  =
  0
  \\
  &
  \lambda^3 - 4 \lambda^2 - 4 \lambda + 16 = 0
  \\
  &
  (\lambda - 4)(\lambda - 2)(\lambda + 2) = 0
\end{eqnarray}
$$

したがって、$A$ の固有値は

$$
\lambda = 4, 2, -2
$$

重複度はゼロ。

#### 固有ベクトル

$$
\begin{eqnarray}
  &
  \begin{pmatrix}
    -\lambda  & -1 & -3 \\
    2  & 3-\lambda & 3  \\
    -2 & 1  & 1-\lambda
  \end{pmatrix}
  \begin{pmatrix}
    x \\
    y \\
    z
  \end{pmatrix}
  =
  \begin{pmatrix}
    0 \\
    0 \\
    0
  \end{pmatrix}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    -\lambda x - y - 3z = 0 \\
    2x + (3-\lambda)y + 3z = 0 \\
    -2x + y + (1-\lambda)z = 0 \\
  \end{cases}
\end{eqnarray}
$$
に求めた固有値を代入する。

**【固有値 4 に属する固有ベクトル】**

$$
\begin{eqnarray}
  &
  \begin{cases}
    -4x - y - 3z = 0 \\
    2x - y + 3z = 0 \\
    -2x + y - 3z = 0 \\
  \end{cases}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    y = -x\\
    z = -x
  \end{cases}
\end{eqnarray}
$$
より、$x = k$ とおけば

$$
\boldsymbol{u} =
k \begin{pmatrix}
  1  \\
  -1 \\
  -1
\end{pmatrix}
$$


**【固有値 2 に属する固有ベクトル】**

$$
\begin{eqnarray}
  &
  \begin{cases}
    -2x - y - 3z = 0 \\
    2x + y + 3z = 0 \\
    -2x + y - z = 0 \\
  \end{cases}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    y = x \\
    z = -x
  \end{cases}
\end{eqnarray}
$$

より、$x = k$ とおけば

$$
\boldsymbol{u} =
k \begin{pmatrix}
  1 \\
  1 \\
  -1
\end{pmatrix}
$$


**【固有値 -2 に属する固有ベクトル】**

$$
\begin{eqnarray}
  &
  \begin{cases}
    2x - y - 3z = 0 \\
    2x + 5y + 3z = 0 \\
    -2x + y + 3z = 0 \\
  \end{cases}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    y = -x \\
    z = x
  \end{cases}
\end{eqnarray}
$$

より、$x = k$ とおけば

$$
\boldsymbol{u} =
k \begin{pmatrix}
  1 \\
  -1 \\
  1
\end{pmatrix}
$$


### 例題2：固有値の重複度が2以上

$$
A =
\begin{pmatrix}
0  & 6 & 3 \\
-2 & 7 & 2  \\
0  & 0 & 3
\end{pmatrix}
$$

#### 固有値

固有方程式は、

$$
\det
\begin{pmatrix}
-\lambda  & 6 & 3 \\
-2  & 7-\lambda & 2  \\
0 & 0  & 3-\lambda
\end{pmatrix}
= 0
$$

よって

$$
\begin{eqnarray}
  &
  -\lambda \{(7-\lambda)(3-\lambda) - 2 \cdot 0 \}
  +6 \{2 \cdot 0 - (-2) (3-\lambda)\}
  +3 \{ (-2) \cdot 0 - (7-\lambda) \cdot 0 \}
  =
  0
  \\
  &
  - \lambda^3 + 10 \lambda^2 - 33 \lambda + 36 = 0
  \\
  &
  (\lambda - 3)^2(\lambda - 4) = 0
\end{eqnarray}
$$

したがって、$A$ の固有値は

$$
\lambda = 4, 3
$$
固有値4は重複度1、固有値3は重複度2。


#### 固有ベクトル

$$
\begin{eqnarray}
  &
  \begin{pmatrix}
    -\lambda  & 6 & 3 \\
    -2  & 7-\lambda & 2  \\
    0 & 0  & 3-\lambda
  \end{pmatrix}
  \begin{pmatrix}
    x \\
    y \\
    z
  \end{pmatrix}
  =
  \begin{pmatrix}
    0 \\
    0 \\
    0
  \end{pmatrix}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    -\lambda x + 6y + 3z = 0 \\
    -2x + (7-\lambda)y + 2z = 0 \\
    (3-\lambda) z = 0 \\
  \end{cases}
\end{eqnarray}
$$
に求めた固有値を代入する。


**【固有値 4 に属する固有ベクトル】**

$$
\begin{eqnarray}
  &
  \begin{cases}
    -4x + 6y + 3z = 0 \\
    -2x + 3y + 2z = 0 \\
    -z = 0 \\
  \end{cases}
  \\
  \Longleftrightarrow
  &
  \begin{cases}
    y = \cfrac{2}{3} x \\
    z = 0
  \end{cases}
\end{eqnarray}
$$

より、$x = 3k$ とおけば

$$
\boldsymbol{u} =
k \begin{pmatrix}
  3 \\
  2 \\
  0
\end{pmatrix}
$$


**【固有値 3 に属する固有ベクトル】**

$$
\begin{eqnarray}
  &
  \begin{cases}
    -3x + 6y + 3z = 0 \\
    -2x + 4y + 2z = 0 \\
    0 = 0 \\
  \end{cases}
  \\
  \Longleftrightarrow
  &
  x - 2y - z = 0
\end{eqnarray}
$$

より、$x = k,\ y = l$ とおけば

$$
\boldsymbol{u}
=
\begin{pmatrix}
  k \\
  l \\
  k - 2l
\end{pmatrix}
=
k \begin{pmatrix}
  1 \\
  0 \\
  1
\end{pmatrix}
+
l \begin{pmatrix}
  0 \\
  1 \\
  -2
\end{pmatrix}
$$


# 固有空間

## 固有空間の定義

> **【定義】固有空間**
> 
> 行列 $A$ の固有値 $\lambda$（重複度 $r$）に対応する固有ベクトルを $\boldsymbol{u}_1, \cdots, \boldsymbol{u}_r$ とするとき、$\boldsymbol{u}_1, \cdots, \boldsymbol{u}_r$ の線形結合で表せる $\mathbb{C}^r$ 空間を、**行列 $A$ の固有値 $\lambda$ に属する固有空間** と言う。

## 具体例

例として、前述の「計算方法」例題2で扱った3次正方行列を考える。

$$
A =
\begin{pmatrix}
	0  & -1 & -3 \\
	2  & 3  & 3  \\
	-2 & 1  & 1
\end{pmatrix}
$$

$A$ の固有値・固有ベクトルは

- $\lambda_1 = 4$（重複度1）、対応する固有ベクトル $\boldsymbol{u}_1 = (3,2,0)^T$
- $\lambda_2 = 3$（重複度2）、対応する固有ベクトル $\boldsymbol{u}_2 = (1,0,1)^T,\ \boldsymbol{u}_3 = (0, 1, -2)^T$

それぞれの固有値について、固有空間のベクトル $\boldsymbol{x} = (x, y, z)^T$ が満たす方程式を考える。

**【$\lambda_1$ に属する固有空間】**

$$
\boldsymbol{x} = k \boldsymbol{u}_1 \quad (k=\mathrm{const.})
$$

成分で表記すると、

$$
\begin{cases}
	x &=& 3k \\
	y &=& 2k \\
	z &=& 0
\end{cases}
$$

$k$ を消去して、

$$
2x - 3y = 0,\quad z = 0
$$

したがって、$\lambda_1$ に属する固有空間は直線 $2x - 3y = 0,\ z=0$


**【$\lambda_2$ に属する固有空間】**

$$
\boldsymbol{x} =
k \boldsymbol{u}_2 +
l \boldsymbol{u}_3
\quad (k, l=\mathrm{const.})
$$

成分で表記すると、

$$
\begin{cases}
	x &=& k \\
	y &=& l \\
	z &=& k-2l
\end{cases}
$$

$k, l$ を消去して、

$$
x -2y -z = 0
$$

したがって、$\lambda_2$ に属する固有空間は平面 $x -2y -z = 0$

求めた固有空間を可視化すると下図のようになる。

![Figure_1](https://user-images.githubusercontent.com/13412823/219932521-ff1ed64a-c0eb-418e-a113-172b17d4f757.png)

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/533b3f374d8f938316a63ad502a07914#file-20230219_draw_eigenspace-py)
