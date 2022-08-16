---
title: 行列式
---

# 行列式の定義

$n$ 次正方行列

$$
A =
\begin{pmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} &        & a_{2n} \\
  \vdots &        & \ddots & \vdots \\
  a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{pmatrix}
$$

に対して、**行列式（determinant）** $\det A$ を下式で定義する。

$$
\det A \equiv \displaystyle \sum_{\sigma \in S_n} {\rm sgn}\left( \sigma \right) \prod_{i=1}^n a_{i \sigma(i)}
$$

ここで、
- $S_n$：$1〜n$ の整数の並び替えの集合（全 $n!$ 通り）
	- 例）$n = 3$ の場合、$S_3 = \{(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)\}$
- $\sigma (i)$：並び順 $\sigma$ の $i$ 番目の要素
	- 例）$n = 4, \ \sigma = (4,2,3,1)$ の場合、$\sigma (1) = 4, \ \sigma (2) = 2, \ \sigma (3) = 3, \ \sigma (4) = 1$
- ${\rm sgn}(\sigma)$：符号を表す関数で、$\sigma$ が偶置換なら1、奇置換なら-1
	- 「2つを選んで置換する」という操作を、元の並び（$n=3$ なら $(1,2,3)$）に何度か適用して $\sigma$ を作る時、置換の回数が偶数なら偶置換、奇数なら奇置換
	- 例）$n = 3$ の場合、
		- $\sigma = (1,3,2)$：元の並び $(1,2,3)$ から1回の置換で作れるので奇置換
		- $\sigma = (2,3,1)$：元の並び $(1,2,3)$ から2回の置換で作れるので偶置換
		- $\sigma = (1,2,3)$：元の並び $(1,2,3)$ から0回の置換で作れるので偶置換

$$
\begin{eqnarray}
  \det
  \begin{pmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22}
  \end{pmatrix}
  &=& a_{11} a_{22} - a_{12} a_{21}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  \det
  \begin{pmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33}
  \end{pmatrix}
  &=& a_{11} a_{22} a_{33} - a_{11} a_{23} a_{32} +
  \\
  &&  a_{12} a_{23} a_{31} - a_{12} a_{21} a_{33} +
  \\
  &&  a_{13} a_{21} a_{32} - a_{13} a_{22} a_{31}
\end{eqnarray}
$$



# 性質

## 基本変形と行列式

### （1）行・列に定数（$\ne 0$）をかける

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{red} a_{21}} & {\color{red} a_{22}} & {\color{red} a_{23}} & {\color{red} a_{24}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  a_{41} & a_{42} & a_{43} & a_{44}
\end{pmatrix}
=
{\color{red}{\cfrac{1}{c}}}
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{red}{c a_{21}}} & {\color{red}{c a_{22}}} & \color{red}{c a_{23}} & \color{red}{c a_{24}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  a_{41} & a_{42} & a_{43} & a_{44}
\end{pmatrix}
$$

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{red}{a_{13}}} & a_{14} \\
  a_{21} & a_{22} & {\color{red}{a_{23}}} & a_{24} \\
  a_{31} & a_{32} & {\color{red}{a_{33}}} & a_{34} \\
  a_{41} & a_{42} & {\color{red}{a_{43}}} & a_{44}
\end{pmatrix}
=
{\color{red}{\cfrac{1}{c}}}
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{red}{c a_{13}}} & a_{14} \\
  a_{21} & a_{22} & {\color{red}{c a_{23}}} & a_{24} \\
  a_{31} & a_{32} & {\color{red}{c a_{33}}} & a_{34} \\
  a_{41} & a_{42} & {\color{red}{c a_{43}}} & a_{44}
\end{pmatrix}
$$

### （2）行・列を入れ替える

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{red} a_{21}} & {\color{red} a_{22}} & {\color{red} a_{23}} & {\color{red} a_{24}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  {\color{blue} a_{41}} & {\color{blue} a_{42}} & {\color{blue} a_{43}} & {\color{blue} a_{44}}
\end{pmatrix}
=
{\color{red} -1}
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{blue} a_{41}} & {\color{blue} a_{42}} & {\color{blue} a_{43}} & {\color{blue} a_{44}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  {\color{red} a_{21}} & {\color{red} a_{22}} & {\color{red} a_{23}} & {\color{red} a_{24}}
\end{pmatrix}
$$

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{red} a_{13}} & {\color{blue} a_{14}} \\
  a_{21} & a_{22} & {\color{red} a_{23}} & {\color{blue} a_{24}} \\
  a_{31} & a_{32} & {\color{red} a_{33}} & {\color{blue} a_{34}} \\
  a_{41} & a_{42} & {\color{red} a_{43}} & {\color{blue} a_{44}}
\end{pmatrix}
=
{\color{red} -1}
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{blue} a_{14}} & {\color{red} a_{13}} \\
  a_{21} & a_{22} & {\color{blue} a_{24}} & {\color{red} a_{23}} \\
  a_{31} & a_{32} & {\color{blue} a_{34}} & {\color{red} a_{33}} \\
  a_{41} & a_{42} & {\color{blue} a_{44}} & {\color{red} a_{43}}
\end{pmatrix}
$$

### （3）ある行・列に他の行・列を定数倍して加える

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{red} a_{21}} & {\color{red} a_{22}} & {\color{red} a_{23}} & {\color{red} a_{24}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  {\color{blue} a_{41}} & {\color{blue} a_{42}} & {\color{blue} a_{43}} & {\color{blue} a_{44}}
\end{pmatrix}
=
\det
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  {\color{red} a_{21}+ca_{41}} & {\color{red} a_{22}+ca_{42}} & {\color{red} a_{23}+ca_{43}} & {\color{red} a_{24}+ca_{44}} \\
  a_{31} & a_{32} & a_{33} & a_{34} \\
  a_{41} & a_{42} & a_{43} & a_{44}
\end{pmatrix}
$$

$$
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{red} a_{13}} & {\color{blue} a_{14}} \\
  a_{21} & a_{22} & {\color{red} a_{23}} & {\color{blue} a_{24}} \\
  a_{31} & a_{32} & {\color{red} a_{33}} & {\color{blue} a_{34}} \\
  a_{41} & a_{42} & {\color{red} a_{43}} & {\color{blue} a_{44}}
\end{pmatrix}
=
\det
\begin{pmatrix}
  a_{11} & a_{12} & {\color{red} a_{13}+ca_{14}} & a_{14} \\
  a_{21} & a_{22} & {\color{red} a_{23}+ca_{24}} & a_{24} \\
  a_{31} & a_{32} & {\color{red} a_{33}+ca_{34}} & a_{34} \\
  a_{41} & a_{42} & {\color{red} a_{43}+ca_{44}} & a_{44}
\end{pmatrix}
$$


## 三角行列の行列式
上三角行列

$$
A =
\begin{pmatrix}
  a_{11} & a_{12} & a_{13} & \cdots & a_{1\ n-1} & a_{1n} \\
  0      & a_{22} & a_{23} & \cdots & a_{2\ n-1} & a_{2n} \\
  0      & 0      & a_{33} & \cdots & a_{3\ n-1} & a_{3n} \\
  \vdots & \vdots & \vdots & \ddots & \vdots       & \vdots \\
  0      & 0      & 0      & \cdots & a_{n-1\ n-1} & a_{n-1\ n} \\
  0      & 0      & 0      & \cdots & 0            & a_{nn}
\end{pmatrix}
$$

および下三角行列

$$
A =
\begin{pmatrix}
  a_{11}     & 0          & 0      & \cdots & 0 & 0 \\
  a_{21}     & a_{22}     & 0      & \cdots & 0 & 0 \\
  a_{31}     & a_{32}     & a_{33} & \cdots & 0 & 0 \\
  \vdots     & \vdots     & \vdots & \ddots & \vdots & \vdots \\
  a_{n-1\ 1} & a_{n-1\ 2} & a_{n-1\ 3} & \cdots & a_{n-1\ n-1} & 0 \\
  a_{n1}     & a_{n2}     & a_{n3} & \cdots & a_{n\ n-1}   & a_{nn}
\end{pmatrix}
$$

において行列式の値を計算すると、並び順 $\sigma = (1,2,3,\cdots,n)$ の項以外は積にゼロが含まれて消えるため、計算結果は対策成分の積になる：

$$
\det A = \displaystyle \prod_{i=1}^n a_{ii} = a_{11}a_{22} \cdots a_{nn}
$$


## その他の公式

$$
\det A = \det A^T
$$

$$
\det (A B) = \det A \det B
$$

$$
\det (A^{-1}) = (\det A)^{-1}
$$


