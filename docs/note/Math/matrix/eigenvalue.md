---
title: 固有値
---

# 定義：固有値と固有ベクトル

$n$ 次正方行列 $A$ に対して、零ベクトルでない列ベクトル $\boldsymbol{x}$ と定数 $\lambda$ が存在し、

$$
A \boldsymbol{x} = \lambda \boldsymbol{x}
$$

が成立する時、

- $\lambda$：行列 $A$ の **固有値**
- $\boldsymbol{x}$：行列 $A$ の固有値 $\lambda$ に属する **固有ベクトル**

と呼ぶ。

# 性質


# 意義

- ベクトルに行列を掛ける = 線形写像を取る操作 $A \boldsymbol{x}$ 
- ベクトルを定数倍する操作 $\lambda \boldsymbol{x}$

が一致するということは、**固有ベクトル $\boldsymbol{x}$ に対して行列 $A$ による線形変換を行っても、長さが定数倍になるだけで、ベクトルの向きが変わらない**と解釈できる（真逆になることはある）。


# 計算方法

## 固有値を求める

$I$ を単位行列とすると、

$$
\begin{eqnarray}
&&A \boldsymbol{x} = \lambda \boldsymbol{x} \\
& \Longleftrightarrow &\left( A - \lambda I \right) \boldsymbol{x} = \boldsymbol{0}
\end{eqnarray}
$$

これが $\boldsymbol{x} = \boldsymbol{0}$ 以外の解を持つためには、行列 $\left( A - \lambda I \right)$ は逆行列を持ってはならない。
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


## 固有ベクトルを求める

固有値 $\lambda$ に対応する固有ベクトルを求めるには、固有値・固有ベクトルの定義式

$$
A \boldsymbol{x} = \lambda \boldsymbol{x}
$$

に $\lambda$ を代入し、$\boldsymbol{x} = \left(x_1, x_2, \cdots, x_n \right)^T$ の各成分の連立方程式として解けば良い。


# 計算の例

## 例題1：固有値の重複度が全て1

$$
A =
\begin{pmatrix}
0  & -1 & -3 \\
2  & 3  & 3  \\
-2 & 1  & 1
\end{pmatrix}
$$

### 固有値

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

### 固有ベクトル

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

#### 固有値 4 に属する固有ベクトル

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
\boldsymbol{x} =
k \begin{pmatrix}
  1  \\
  -1 \\
  -1
\end{pmatrix}
$$


#### 固有値 2 に属する固有ベクトル

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
\boldsymbol{x} =
k \begin{pmatrix}
  1 \\
  1 \\
  -1
\end{pmatrix}
$$


#### 固有値 -2 に属する固有ベクトル

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
\boldsymbol{x} =
k \begin{pmatrix}
  1 \\
  -1 \\
  1
\end{pmatrix}
$$


## 例題2：固有値の重複度が2以上

$$
A =
\begin{pmatrix}
0  & 6 & 3 \\
-2 & 7 & 2  \\
0  & 0 & 3
\end{pmatrix}
$$

### 固有値

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


### 固有ベクトル

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


#### 固有値 4 に属する固有ベクトル

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
\boldsymbol{x} =
k \begin{pmatrix}
  3 \\
  2 \\
  0
\end{pmatrix}
$$


#### 固有値 3 に属する固有ベクトル

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
\boldsymbol{x}
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
