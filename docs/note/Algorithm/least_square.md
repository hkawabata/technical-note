---
title: 最小二乗法
---

# 概要

与えられたデータ点 $N$ 個の集合 $(x_1, y_1), \cdots, (x_N, y_N)$ を通る関数 $y = f(x)$ を近似して求める手法。  
$f(x)$ の形（二次関数、三次関数、対数関数、...）を仮定した上で、実際のデータ点と近似曲線の値との誤差の平方和

$$
S := \sum_{i=1}^N \left( y_i - f(x_i) \right)^2
\tag{1}
$$

が最小となるように関数のパラメータを決定する。

# 誤差平方和を最小化する方法

求める関数 $f(x)$ の未知のパラメータを $a_1, a_2, \cdots, a_m$ とし、$f(x) = f(x;a_1, a_2, \cdots, a_m)$ とも書くことにする。

$f(x;a_1, a_2, \cdots, a_m)$ を任意のパラメータ $a_k$ の関数として見た時、$f$ が $a_k$ で微分可能であるとすれば、誤差平方和 $S$ が最小となるとき、

$$
\cfrac{\partial S}{\partial a_k}
=
-2 \sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_k} \left( y_i - f(x_i) \right)
= 0
\tag{2}
$$

すなわち、

$$
\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_k} y_i
=
\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_k} f(x_i)
\tag{3}
$$

が成り立つ。したがって、各パラメータで $S$ を偏微分してゼロと置いた $m$ 元連立方程式

$$
\begin{cases}
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_1} y_i
    =
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_1} f(x_i) 
    \\
    \\
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_2} y_i
    =
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_2} f(x_i)
    \\
    \\
    \cdots \\
    \\
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_m} y_i
    =
    \displaystyle\sum_{i=1}^N \cfrac{\partial f(x_i)}{\partial a_m} f(x_i)
\end{cases}
\tag{4}
$$

を解けば $a_1, a_2, \cdots, a_m$ が求まる。

特に、

$$
\begin{eqnarray}
    f(x) &=& a_1 x^2 + a_2 x + a_3 \\
    f(x) &=& a_1 \sin x + a_2 \sin x
\end{eqnarray}
$$

のように $f(x)$ が $a_1, a_2, \cdots, a_m$ それぞれについて線形（一次関数）であるとき、上の連立方程式は $m$ 元1次の連立方程式となり、行列を用いて簡単に解ける。

$$
f(x;a_1, a_2, \cdots, a_m) = a_1 g_1(x) + a_2 g_2(x) + \cdots + a_m g_m(x)
\tag{5}
$$

と置けば

$$
\cfrac{\partial f(x)}{\partial a_k} = g_k(x)
$$

であるから、解くべき方程式 $(3)$ は

$$
\begin{eqnarray}
    &\sum_{i=1}^N g_k(x_i) y_i
    &=&
    \sum_{i=1}^N g_k(x_i) (a_1 g_1(x_i) + a_2 g_2(x_i) + \cdots + a_m g_m(x_i))
    \\
    \Longleftrightarrow \quad &
    \sum_{i=1}^N g_k(x_i) y_i
    &=&
    a_1 \sum_{i=1}^N g_k(x_i) g_1(x_i) +
    \cdots +
    a_m \sum_{i=1}^N g_k(x_i) g_m(x_i)
    \tag{3'}
\end{eqnarray}
$$

となる。  
各 $a_k$ についての $(3')$ 式を連立させて行列形式で書くと、

$$
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N g_1(x_i) y_i \\
    \displaystyle \sum_{i=1}^N g_2(x_i) y_i \\
    \vdots \\
    \displaystyle \sum_{i=1}^N g_m(x_i) y_i
\end{pmatrix}
=
\begin{pmatrix}
    \displaystyle\sum_{i=1}^N g_1(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_1(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_1(x_i) g_m(x_i) \\
    \displaystyle\sum_{i=1}^N g_2(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_2(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_2(x_i) g_m(x_i) \\
    \vdots & \vdots & \ddots & \vdots \\
    \displaystyle\sum_{i=1}^N g_m(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_m(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_m(x_i) g_m(x_i)
\end{pmatrix}
\begin{pmatrix}
    a_1 \\ a_2 \\ \vdots \\ a_m
\end{pmatrix}
\tag{4'}
$$

よって

$$
\begin{pmatrix}
    a_1 \\ a_2 \\ \vdots \\ a_m
\end{pmatrix}
=
\begin{pmatrix}
    \displaystyle\sum_{i=1}^N g_1(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_1(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_1(x_i) g_m(x_i) \\
    \displaystyle\sum_{i=1}^N g_2(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_2(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_2(x_i) g_m(x_i) \\
    \vdots & \vdots & \ddots & \vdots \\
    \displaystyle\sum_{i=1}^N g_m(x_i) g_1(x_i) & \displaystyle\sum_{i=1}^N g_m(x_i) g_2(x_i) & \cdots & \displaystyle\sum_{i=1}^N g_m(x_i) g_m(x_i)
\end{pmatrix}^{-1}
\begin{pmatrix}
    \displaystyle \sum_{i=1}^N g_1(x_i) y_i \\
    \displaystyle \sum_{i=1}^N g_2(x_i) y_i \\
    \vdots \\
    \displaystyle \sum_{i=1}^N g_m(x_i) y_i
\end{pmatrix}
\tag{6}
$$

によりパラメータが求まる。

係数行列は対称行列になるので、計算量は多少節約できる。

> **【NOTE】**
> 
> $$
\begin{eqnarray}
f(x) &=& a\log bx + c \tag{7} \\
f(x) &=& a\sin cx + b \cos cx \tag{8}
\end{eqnarray}
$$
> 
> のような回帰関数を考える場合、これらはパラメータ $a,b,c$ についての一次関数にはなっていない。しかし、$(7)$ は
> 
> $$
f(x) = a(\log b + \log x) + c = a\log x + d \qquad (d := a\log b+c)
$$
> 
> と変形して、パラメータ $a,d$ の一次関数で表せる。したがって上述の方法による fitting が可能。  
> $(8)$ はパラメータの一次関数に変形することは（たぶん）できないので、別の方法で最適化が必要。


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

