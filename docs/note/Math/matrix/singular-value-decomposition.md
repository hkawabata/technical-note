---
title: 特異値分解
---

# 特異値分解とは

$n \times m$ 行列 $A$ を、
- $U$：$n$ 次直行行列
- $V$：$m$ 次直行行列
- $\Sigma$：左側 or 上側の対角成分以外がゼロの $n \times m$ 行列

を用いて

$$
\begin{eqnarray}
A
&=&
  U \Sigma V^T \\
&=&
  \begin{cases}
    \left( \boldsymbol{u}_1, \cdots, \boldsymbol{u}_n \right)
    \begin{pmatrix}
      \lambda_1 &        & 0         & 0      & \cdots & 0      \\
                & \ddots &           & \vdots &        & \vdots \\
      0         &        & \lambda_n & 0      & \cdots & 0
    \end{pmatrix}
    \left( \boldsymbol{v}_1, \cdots, \boldsymbol{v}_m \right)^T
    \qquad {\rm if} \quad n \lt m
    \\
    \left( \boldsymbol{u}_1, \cdots, \boldsymbol{u}_n \right)
    \begin{pmatrix}
      \lambda_1 &        & 0         \\
                & \ddots &           \\
      0         &        & \lambda_m \\
      0         & \cdots & 0         \\
      \vdots    &        & \vdots    \\
      0         & \cdots & 0
    \end{pmatrix}
    \left( \boldsymbol{v}_1, \cdots, \boldsymbol{v}_m \right)^T
    \qquad {\rm if} \quad n \ge m
  \end{cases}
\end{eqnarray}
$$

の形に分解する操作。
簡単のため、これ以降は $n \lt m$ で考えていく。

- **特異値**：$\lambda_1, \cdots, \lambda_n$
- **左特異ベクトル**：$\boldsymbol{u}_1, \cdots, \boldsymbol{u}_n$
- **右特異ベクトル**：$\boldsymbol{v}_1, \cdots, \boldsymbol{v}_m$


# 特異値分解の意義

(ToDo)

# 手順

## 下準備

### $U, V, \Sigma$ の性質

$U, V$ は直交行列なので、$I$ を単位行列とすると

$$
U^T = U^{-1}, \quad U U^T = U^T U = I
$$

$$
V^T = V^{-1}, \quad V V^T = V^T V = I
$$

また、$\Sigma$ は左側の対角成分以外がゼロの行列なので、

$$
\Sigma \Sigma^T =
\begin{pmatrix}
      \lambda_1^2 &        & 0         \\
                & \ddots &           \\
      0         &        & \lambda_n^2
  \end{pmatrix}
$$

$$
\Sigma^T \Sigma =
  \begin{pmatrix}
      \lambda_1^2 &        & 0           &  &   & \\
                  & \ddots &             &  & O & \\
      0           &        & \lambda_n^2 &  &   & \\
                  &        &             &  &   & \\
                  & O      &             &  & O & \\
                  &        &             &  &   & \\
  \end{pmatrix}
$$


### 特異ベクトルの変換

特異値分解の定義式

$$
A = U \Sigma V^T
$$

に対して、
1. 右から $V$ をかける操作
2. 転置した後、右から $U$ をかける操作

をそれぞれ行うと、以下の2式を得る

$$
\begin{eqnarray}
  &&
  \begin{cases}
    A V = U \Sigma
    \\
    A^T U = V \Sigma^T
  \end{cases}
  \\
  &
  \Longleftrightarrow
  &
  \begin{cases}
    A \left( \boldsymbol{v}_1, \cdots, \boldsymbol{v}_m \right) =
    \left( \boldsymbol{u}_1, \cdots, \boldsymbol{u}_n \right)
    \begin{pmatrix}
      \lambda_1 &        & 0         & 0      & \cdots & 0      \\
                & \ddots &           & \vdots &        & \vdots \\
      0         &        & \lambda_n & 0      & \cdots & 0
    \end{pmatrix}
    \\
    A^T \left( \boldsymbol{u}_1, \cdots, \boldsymbol{u}_n \right) =
    \left( \boldsymbol{v}_1, \cdots, \boldsymbol{v}_m \right)
    \begin{pmatrix}
      \lambda_1 &        & 0         \\
                & \ddots &           \\
      0         &        & \lambda_n \\
      0         & \cdots & 0         \\
      \vdots    &        & \vdots    \\
      0         & \cdots & 0
    \end{pmatrix}
  \end{cases}
  \\
  &
  \Longleftrightarrow
  &
  \begin{cases}
    \left( A \boldsymbol{v}_1, \cdots, A \boldsymbol{v}_m \right)
    =
    \left( \lambda_1 \boldsymbol{u}_1, \cdots, \lambda_n \boldsymbol{u}_n, 0, \cdots, 0 \right)
    \\
    \left( A^T \boldsymbol{u}_1, \cdots, A^T \boldsymbol{u}_n \right)
    =
    \left( \lambda_1 \boldsymbol{v}_1, \cdots, \lambda_n \boldsymbol{v}_n \right)
  \end{cases}
\end{eqnarray}
$$

両辺の $k$ 列目 ($k \le \min{(m, n)}$) だけを取り出して比較すると、

$$
\begin{cases}
  A \boldsymbol{v}_k = \lambda_k \boldsymbol{u}_k
  \\
  A^T \boldsymbol{u}_k = \lambda_k \boldsymbol{v}_k
\end{cases}
$$

となり、同じ特異値 $\lambda_k$ に対応する左右の特異ベクトル間の変換式

$$
\begin{cases}
  \boldsymbol{u}_k = \cfrac{1}{\lambda_k} A \boldsymbol{v}_k
  \\
  \boldsymbol{v}_k = \cfrac{1}{\lambda_k} A^T \boldsymbol{u}_k
\end{cases}
$$

を得る。


## 特異行列と特異値の計算

まず $AA^T$ を考える。

$$
\begin{eqnarray}
  A A^T
  &=& U \Sigma V^T
  \left( U \Sigma V^T \right)^T
  \\
  &=& U \Sigma V^T V \Sigma^T U^T
  \\
  &=& U \Sigma \Sigma^T U^T
  \\
  &=&
  U
  \begin{pmatrix}
    \lambda_1^2 &        & 0           \\
                & \ddots &             \\
    0           &        & \lambda_n^2
  \end{pmatrix}
  U^T
\end{eqnarray}
$$

$U^T = U^{-1}$ なので、この式は行列 $A A^T$ を $U$ で対角化する式。
つまり
- $U, U^{-1}$ は $A A^T$ の固有ベクトルを並べた行列
- $\lambda_1^2, \cdots, \lambda_n^2$ は $A A^T$ の固有値

よって、$A A^T$ の固有値問題を解けば左特異行列 $U$ と特異値 $\lambda_1, \cdots, \lambda_n$ が求まる。

同様に $A^T A$ を考えると、

$$
\begin{eqnarray}
  A^T A
  &=& \left( U \Sigma V^T \right)^T
  U \Sigma V^T
  \\
  &=& V \Sigma^T U^T U \Sigma V^T
  \\
  &=& V \Sigma^T \Sigma V^T
  \\
  &=&
  V
  \begin{pmatrix}
    \lambda_1^2 &        & 0           &  &   & \\
                & \ddots &             &  & O & \\
    0           &        & \lambda_n^2 &  &   & \\
                &        &             &  &   & \\
                & O      &             &  & O & \\
                &        &             &  &   & \\
  \end{pmatrix}
  V^T
\end{eqnarray}
$$

なので、

$A^T A$ の固有値問題を解けば右特異行列 $V$ も求まる。

実際には、以下の手順で解くのが楽。
1. $A^T A, A A^T$ の固有値問題のうち解きやすい方（次数が小さい方）を解いて特異ベクトルと特異値を求める
2. それを使って、$\boldsymbol{u}, \boldsymbol{v}$ の変換公式からもう一方の特異ベクトルを求める
3. 変換公式だけでは求まらない特異ベクトルについては直交条件（$\boldsymbol{u}_i \cdot \boldsymbol{u}_j = 0 \quad {\rm if} \quad i \ne j$）から求める


# 例題

$$
A =
\begin{pmatrix}
  1  & −1 & 0 \\
  −1 & 0  & 1
\end{pmatrix}
$$

を特異値分解する。

## 特異値の計算

$$
A A^T
=
\begin{pmatrix}
  1  & −1 & 0 \\
  −1 & 0  & 1
\end{pmatrix}
\begin{pmatrix}
  1  & -1 \\
  -1 & 0  \\
  0  & 1
\end{pmatrix}
=
\begin{pmatrix}
  2  & −1 \\
  −1 & 2
\end{pmatrix}
$$

$$
A^T A =
\begin{pmatrix}
  1  & -1 \\
  -1 & 0  \\
  0  & 1
\end{pmatrix}
\begin{pmatrix}
  1  & −1 & 0 \\
  −1 & 0  & 1
\end{pmatrix}
=
\begin{pmatrix}
  2  & −1 & -1 \\
  −1 & 1  & 0  \\
  -1 & 0  & 1
\end{pmatrix}
$$

$A A^T$ の方が $A^T A$ より次数が低く、固有方程式の計算が楽なのでこちらを計算する。

固有値を $\lambda^2$ とする特性方程式
$$
\det\left( A A^T - \lambda^2 I \right) = 0
$$

を解く。

$$
A A^T - \lambda^2 I
=
\begin{pmatrix}
  2 - \lambda^2 & -1 \\
  -1 & 2 - \lambda^2
\end{pmatrix}
$$

なので、

$$
\begin{eqnarray}
  det\left( A A^T - \lambda^2 I \right) = 0
  \\
  (2-\lambda^2)^2 - 1 = 0
  \\
  2-\lambda^2 = \pm 1
  \\
  \lambda^2 = 3, 1
\end{eqnarray}
$$

よって特異値 $\lambda = \sqrt 3, 1$ となり、

$$
\Sigma =
\begin{pmatrix}
  \sqrt 3 & 0 & 0 \\
  0 & 1 & 0
\end{pmatrix}
$$

## 左特異ベクトルの計算

前節の固有値について、固有値 $\lambda^2 = 3$ に対する固有ベクトル $\boldsymbol{u}_1 = \begin{pmatrix} u_x \\ u_y \end{pmatrix}$ は、

$$
\begin{eqnarray}
  \begin{pmatrix}
    2  & -1 \\
    -1 & 2
  \end{pmatrix}
  \begin{pmatrix}
    u_x \\
    u_y
  \end{pmatrix}
  &=&
  3 \begin{pmatrix}
    u_x \\
    u_y
  \end{pmatrix}
  \\
  2 u_x - u_y &=& 3 u_x
  \\
  u_x &=& - u_y
\end{eqnarray}
$$

より、$\boldsymbol{u}_1 = \cfrac{1}{\sqrt 2} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

固有値 $\lambda^2 = 1$ に対する固有ベクトル $\boldsymbol{u}_2 = \begin{pmatrix} u_x \\ u_y \end{pmatrix}$ は

$$
\begin{eqnarray}
  \begin{pmatrix}
    2  & -1 \\
    -1 & 2
  \end{pmatrix}
  \begin{pmatrix}
    u_x \\
    u_y
  \end{pmatrix}
  &=&
  1 \begin{pmatrix}
    u_x \\
    u_y
  \end{pmatrix}
  \\
  2 u_x - u_y &=& u_x
  \\
  u_x &=& u_y
\end{eqnarray}
$$

より、$\boldsymbol{u}_2 = \cfrac{1}{\sqrt 2} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

以上により左特異ベクトルは、特異値が大きい順に並べて

$$
U =
\cfrac{1}{\sqrt 2}
\begin{pmatrix}
  1  & 1\\
  -1 & 1
\end{pmatrix}
$$

> **【NOTE】固有ベクトルの符号**
> 
> 固有ベクトルはノルム（長さ）が1になるように正規化しているが、符号の正負に自由度がある。
> たとえば、上の $\lambda^2 = 3$ に対する固有ベクトルを
> $$
 \begin{pmatrix} u_x \\ u_y \end{pmatrix} = \cfrac{1}{\sqrt 2} \begin{pmatrix} 1 \\ -1 \end{pmatrix}
 $$
>
 > としても良いし、
 > 
>$$
 \begin{pmatrix} u_x \\ u_y \end{pmatrix} = \cfrac{1}{\sqrt 2} \begin{pmatrix} -1 \\ 1 \end{pmatrix}
 $$
 > 
 > としても良い。
 > 
 > 後述のように、右特異ベクトルを左特異ベクトルから計算する際に、符号の自由度は吸収される。
 
 

## 右特異ベクトルの計算

右特異ベクトル・左特異ベクトルの変換の式

$$
\boldsymbol{v}_k = \cfrac{1}{\lambda_k} A^T \boldsymbol{u}_k
$$
より、$\lambda = \sqrt 3$ に対応する右特異ベクトルは

$$
\boldsymbol{v}_1
=
\cfrac{1}{\sqrt 3}
\begin{pmatrix}
  1  & -1 \\
  -1 & 0  \\
  0  & 1
\end{pmatrix}
\cfrac{1}{\sqrt 2}
\begin{pmatrix} 1 \\ -1 \end{pmatrix}
=
\cfrac{1}{\sqrt 6}
\begin{pmatrix}
  2  \\
  -1 \\
  -1
\end{pmatrix}
$$


$\lambda = 1$ に対応する右特異ベクトルは

$$
\boldsymbol{v}_2
=
\cfrac{1}{1}
\begin{pmatrix}
  1  & -1 \\
  -1 & 0  \\
  0  & 1
\end{pmatrix}
\cfrac{1}{\sqrt 2}
\begin{pmatrix} 1 \\ 1 \end{pmatrix}
=
\cfrac{1}{\sqrt 2}
\begin{pmatrix}
  0  \\
  -1 \\
  1
\end{pmatrix}
$$

$V$ は3次正方行列なので、もう一つの右特異ベクトル $\boldsymbol{v}_3$ が存在。
$\boldsymbol{v}_1, \boldsymbol{v}_2$ との直行条件から、

$$
\begin{eqnarray}
&&
  \begin{cases}
    \boldsymbol{v}_3 \cdot \boldsymbol{v}_1 = 0 \\
    \boldsymbol{v}_3 \cdot \boldsymbol{v}_2 = 0
  \end{cases}
  \\
  & \Longleftrightarrow &
  \begin{cases}
    2v_x - v_y - v_z = 0 \\
    -v_y + v_z = 0
  \end{cases}
  \\
  & \Longleftrightarrow &
  v_x = v_y = v_z
\end{eqnarray}
$$

よって

$$
\boldsymbol{v}_3
=
\cfrac{1}{\sqrt 3}
\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
$$

以上により右特異ベクトルは、特異値が大きい順に並べて

$$
V =
\begin{pmatrix}
  \cfrac{2}{\sqrt 6} & 0                  & \cfrac{1}{\sqrt 3} \\
  -\cfrac{1}{\sqrt 6} & -\cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 3} \\
  -\cfrac{1}{\sqrt 6} & \cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 3}
\end{pmatrix}
$$


## 最終結果

以上の結果をまとめて、$A$ の特異値分解は

$$
\underbrace{
  \begin{pmatrix}
    1  & −1 & 0 \\
    −1 & 0  & 1
  \end{pmatrix}
}_{A}
=
\underbrace{
  \begin{pmatrix}
    \cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 2} \\
    -\cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 2}
  \end{pmatrix}
}_{U}
\underbrace{
  \begin{pmatrix}
    \sqrt 3 & 0 & 0 \\
    0 & 1 & 0
  \end{pmatrix}
}_{\Sigma}
\underbrace{
  \begin{pmatrix}
    \cfrac{2}{\sqrt 6} & 0                  & \cfrac{1}{\sqrt 3} \\
    -\cfrac{1}{\sqrt 6} & -\cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 3} \\
    -\cfrac{1}{\sqrt 6} & \cfrac{1}{\sqrt 2} & \cfrac{1}{\sqrt 3}
  \end{pmatrix}^T
}_{V}
$$

