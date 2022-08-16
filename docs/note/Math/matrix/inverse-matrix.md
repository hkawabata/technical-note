---
title: 逆行列
---

# 逆行列の定義

$n$ 次正方行列 $A$ に対して、

$$
A A^{-1} = A^{-1} A = I
=
\begin{pmatrix}
  1 & & & & \\
   & 1 & & O & \\
   & & \ddots & & \\
   & O & & 1 & \\
   & & & & 1 \\
\end{pmatrix}
$$

（$I$ は $n$ 次単位行列）を満たすような $A^{-1}$ が存在する時、$A^{-1}$ を $A$ の **逆行列** と呼ぶ。

また、逆行列が存在するような行列 $A$ を **正則行列** と呼ぶ。

# 逆行列の意義

列ベクトル $\boldsymbol{x}$ に線形変換 $A$ を施した結果を $\boldsymbol{y}$ とする。

$$
\boldsymbol{y} = A \boldsymbol{x}
$$

$\boldsymbol{y}$ は、原因 $\boldsymbol{x}$ に対する操作 $A$ の結果、と捉えることができる（= **原因から結果を導く**）。

逆行列を $\boldsymbol{y}$ に作用させると

$$
A^{-1} \boldsymbol{y} = A^{-1} A \boldsymbol{x} = I \boldsymbol{x} = \boldsymbol{x}
$$

よって

$$
\boldsymbol{x} = A^{-1} \boldsymbol{y}
$$

これは先程とは逆に、結果 $\boldsymbol{y}$ から推定される原因、と捉えることができる（= **結果から原因を推定する**）。


# 逆行列の性質

行列 $A$ に逆行列が存在する条件は、

$$
\det A = 0
$$

行列 $A, B$ に逆行列が存在するとき、

$$
(AB)^{-1} = B^{-1}A^{-1}
$$


# 計算方法

逆行列を求めたい行列 $A$ と単位行列 $I$ を横に並べる：

$$
(A | E) =
\left(
  \begin{array}{ccc|ccc}
    a_{11} & \cdots & a_{1n} & 1 &        & O \\
    \vdots & \ddots & \vdots &   & \ddots &   \\
    a_{n1} & \cdots & a_{nn} & O &        & 1 \\
  \end{array}
\right)
$$
この $n \times 2n$ 行列に対して、
- 1つの行を定数倍する
- 2つの行を入れ替える
- ある行の定数倍を別の行に加える

の行基本変形を必要なだけ適用して、左側部分を単位行列にする：

$$
(E | A^{-1}) =
\left(
  \begin{array}{ccc|ccc}
     1 &  & O & b_{11} & \cdots & b_{1n} \\
       & \ddots & & \vdots & \ddots & \vdots \\
     O &  & 1 & b_{n1} & \cdots & b_{nn} \\
  \end{array}
\right)
$$

右側の $n \times n$ 行列が $A$ の逆行列 $A^{-1}$ になっている。


# 計算の例

## $2 \times 2$ 行列

$$
A =
\begin{pmatrix}
  3 & 5 \\
  4 & 7
\end{pmatrix}
$$

$$
(A | I) =
\left(
  \begin{array}{cc|cc}
     3 & 5 & 1 & 0 \\
     4 & 7 & 0 & 1
  \end{array}
\right)
$$
1行目を $-\cfrac{4}{3}$ 倍して2行目に足す：

$$
\left(
  \begin{array}{cc|cc}
     3 & 5 & 1 & 0 \\
     0 & \cfrac{1}{3} & -\cfrac{4}{3} & 1
  \end{array}
\right)
$$
2行目を $-15$ 倍して1行目に足す：

$$
\left(
  \begin{array}{cc|cc}
     3 & 0 & 21 & -15 \\
     0 & \cfrac{1}{3} & -\cfrac{4}{3} & 1
  \end{array}
\right)
$$

1行目に $\cfrac{1}{3}$、2行目に3をかける：

$$
\left(
  \begin{array}{cc|cc}
     1 & 0 & 7 & -5 \\
     0 & 1 & -4 & 3
  \end{array}
\right)
$$

したがって、

$$
A^{-1} =
\begin{pmatrix}
  7  & -5 \\
  -4 & 3
\end{pmatrix}
$$

## $2 \times 2$ 行列（逆行列なし）

$$
A =
\begin{pmatrix}
  4 & 3 \\
  8 & 6
\end{pmatrix}
$$

$$
(A | I) =
\left(
  \begin{array}{cc|cc}
     4 & 3 & 1 & 0 \\
     8 & 6 & 0 & 1
  \end{array}
\right)
$$

1行目を $-2$ 倍して2行目に足す：

$$
\left(
  \begin{array}{cc|cc}
     4 & 3 & 1  & 0 \\
     0 & 0 & -2 & 1
  \end{array}
\right)
$$

これ以上、どのような基本変形を行っても左側を単位行列にすることができない。

→ $A$ の逆行列は存在しない


## $3 \times 3$ 行列

$$
A =
\begin{pmatrix}
  1  & 3 & 2 \\
  -1 & 0 & 1 \\
  2  & 3 & 0
\end{pmatrix}
$$

$$
(A | I) =
\left(
  \begin{array}{ccc|ccc}
     1  & 3 & 2 & 1 & 0 & 0 \\
     -1 & 0 & 1 & 0 & 1 & 0 \\
     2  & 3 & 0 & 0 & 0 & 1 
  \end{array}
\right)
$$

1行目を2行目に足し、$-2$ 倍して3行目に足す：

$$
\left(
  \begin{array}{ccc|ccc}
     1 & 3  & 2  & 1  & 0 & 0 \\
     0 & 3  & 3  & 1  & 1 & 0 \\
     0 & -3 & -4 & -2 & 0 & 1 
  \end{array}
\right)
$$

2行目を $-1$ 倍して1行目に足し、3行目に足す：

$$
\left(
  \begin{array}{ccc|ccc}
     1 & 0 & -1 & 0  & -1 & 0 \\
     0 & 3 & 3  & 1  & 1  & 0 \\
     0 & 0 & -1 & -1 & 1 & 1 
  \end{array}
\right)
$$

3行目を $-1$ 倍して1行目に足し、3倍して2行目に足す：

$$
\left(
  \begin{array}{ccc|ccc}
     1 & 0 & 0  & 1  & -2 & -1 \\
     0 & 3 & 0  & -2 & 4  & 3 \\
     0 & 0 & -1 & -1 & 1  & 1
  \end{array}
\right)
$$

2行目に $\cfrac{1}{3}$、3行目に $-1$ をかける：

$$
\left(
  \begin{array}{ccc|ccc}
     1 & 0 & 0 & 1  & -2 & -1 \\
     0 & 1 & 0 & -\cfrac{2}{3} & \cfrac{4}{3} & 1 \\
     0 & 0 & 1 & 1  & -1  & -1
  \end{array}
\right)
$$

したがって、

$$
A^{-1} =
\begin{pmatrix}
  1  & -2 & -1 \\
  -\cfrac{2}{3} & \cfrac{4}{3} & 1 \\
  1  & -1  & -1
\end{pmatrix}
$$
