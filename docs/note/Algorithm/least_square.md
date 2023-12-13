---
title: 最小二乗法
---

# 概要

与えられたデータ点 $N$ 個の集合 $(x_1, y_1), \cdots, (x_N, y_N)$ を通る関数 $y = f(x)$ を近似して求める手法。  
$f(x)$ の形（二次関数、三次関数、対数関数、...）を仮定した上で、実際のデータ点と近似曲線との値の差分の平方和

$$
S := \sum_{i=1}^N \left( y_i - f(x_i) \right)^2
$$

が最小となるように関数のパラメータを決定する。

# 具体例

##  M 次関数

求める $M$ 次関数を

$$f(x) = a_0 + a_1 x + a_2 x^2 + ... + a_M x^M = \displaystyle \sum_{j=0}^M a_j x^j$$

と置く。

最小化すべき平方和 $S$ は

$$S = \displaystyle \sum_{i=1}^N \left\{ y_i - f(x_i) \right\}^2 = \sum_{i=1}^N \left( y_i - \sum_{j=0}^M a_j x_i^j \right)^2$$

$S$ は任意の $a_k$ に関して下に凸の二次関数であるから、$S$ が最小となる時、

$$\cfrac{\partial S}{\partial a_k} = 0$$

が成り立つ。

$$\cfrac{\partial S}{\partial a_k} = \displaystyle -2 \sum_{i=1}^N x_i^k \left(y_i - \sum_{j=0}^M a_j x_i^j \right) = -2 \left\{ \sum_{i=1}^N x_i^k y_i - \sum_{j=0}^M \left( a_j \sum_{i=1}^N x_i^{j+k} \right) \right\}$$

なので、$M+1$ 元一次連立方程式

$$
\begin{eqnarray}
	& \sum_{i=1}^N x_i^k y_i = \sum_{j=0}^M \left( a_j \sum_{i=1}^N x_i^{j+k} \right)
	\\
	\Longleftrightarrow &
	\begin{pmatrix}
		t_0    \\
		\vdots \\
		t_M
	\end{pmatrix}
	=
	\begin{pmatrix}
		s_0    & \cdots & s_M    \\
		\vdots & \ddots & \vdots \\
		s_M    & \cdots & s_{2M}
	\end{pmatrix}
	\begin{pmatrix}
		a_0    \\
		\vdots \\
		a_M
	\end{pmatrix} \\
	& \mathrm{where}\ \ \ 
	s_k = \sum_{i=1}^N x_i^k,\ \ 
	t_k = \sum_{i=1}^N x_i^k y_i
\end{eqnarray}
$$

を解けば良い：

$$
\begin{pmatrix}
    a_0    \\
    \vdots \\
    a_M
\end{pmatrix}
=
\begin{pmatrix}
    s_0    & \cdots & s_M    \\
    \vdots & \ddots & \vdots \\
    s_M    & \cdots & s_{2M}
\end{pmatrix}^{-1}
\begin{pmatrix}
    t_0    \\
    \vdots \\
    t_M
\end{pmatrix}
$$

係数行列は対角行列であり、共通の要素も多いので、計算量は節約できる。

## 対数関数

求める対数関数を

$$
f(x) = a \log x + b
$$

と置く。

最小化すべき平方和 $S$ は

$$
S = \sum_{i=1}^N \left\{ y_i - f(x_i) \right\}^2 = \sum_{i=1}^N ( y_i - a \log x_i - b )^2
$$

$S$ は $a, b$ に関して下に凸の二次関数であるから、$S$ が最小となる時、

$$\cfrac{\partial S}{\partial a} = 0,\quad\cfrac{\partial S}{\partial b} = 0$$

が成り立つ。

$$
\begin{eqnarray}
    \cfrac{\partial S}{\partial a}
    &=&
    - 2 \sum_{i=1}^N \log x_i (y_i - a \log x_i - b)
    \\ &=&
    - 2 \left(
        \sum_{i=1}^N y_i \log x_i
        - a \sum_{i=1}^N (\log x_i)^2
        - b \sum_{i=1}^N \log x_i
    \right)
    \\
    \\
    \cfrac{\partial S}{\partial b}
    &=&
    - 2 \sum_{i=1}^N (y_i - a \log x_i - b)
    \\ &=&
    - 2 \left(
        \sum_{i=1}^N y_i
        - a \sum_{i=1}^N \log x_i
        - Nb
    \right)
\end{eqnarray}
$$

をゼロと置いた連立方程式を行列形式で書くと、

$$
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N y_i \log x_i \\
    \displaystyle \sum_{i=1}^N y_i
\end{pmatrix}
=
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N (\log x_i)^2 & \displaystyle \sum_{i=1}^N \log x_i \\
    \displaystyle \sum_{i=1}^N \log x_i & \displaystyle N
\end{pmatrix}
\begin{pmatrix}
    a \\
    b
\end{pmatrix}
$$

これを解いて

$$
\begin{pmatrix}
    a \\
    b
\end{pmatrix}
=
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N (\log x_i)^2 & \displaystyle \sum_{i=1}^N \log x_i \\
    \displaystyle \sum_{i=1}^N \log x_i & \displaystyle N
\end{pmatrix}^{-1}
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N y_i \log x_i \\
    \displaystyle \sum_{i=1}^N y_i
\end{pmatrix}
$$

により係数 $a, b$ が求まる。

# 実装

## コード

{% gist fbb64ace37a9d5a68810439062166abf least-square.py %}

## 動作確認

{% gist fbb64ace37a9d5a68810439062166abf ~fit.py %}

![LeastSquare](https://user-images.githubusercontent.com/13412823/81069197-87e4da80-8f1c-11ea-928b-73bb50c19ff6.png)

