---
title: 最小二乗法
---

# 概要

与えられたデータ点 N 個の集合 $$(x_1, y_1), ..., (x_N, y_N)$$ を通る M 次関数

$$f(x) = a_0 + a_1 x + a_2 x^2 + ... + a_M x^M = \displaystyle \sum_{j=0}^M a_j x^j$$

を近似して求める手法。

実際のデータ点と近似曲線との値の差分の平方和が最小となるように係数 $$a_j$$ を決定する。

# 手法

最小化すべき平方和 $$S$$ は

$$S = \displaystyle \sum_{i=1}^N \left\{ y_i - f(x_i) \right\}^2 = \sum_{i=1}^N \left( y_i - \sum_{j=0}^M a_j x_i^j \right)^2$$

$$S$$ は任意の $$a_k$$ に関して下に凸の二次関数であるから、

$$\cfrac{\partial S}{\partial a_k} = 0$$

となる $$a_k$$ を求めれば良い。

$$\cfrac{\partial S}{\partial a_k} = \displaystyle -2 \sum_{i=1}^N x_i^k \left(y_i - \sum_{j=0}^M a_j x_i^j \right) = -2 \left\{ \sum_{i=1}^N x_i^k y_i - \sum_{j=0}^M \left( a_j \sum_{i=1}^N x_i^{j+k} \right) \right\}$$

なので、M+1 元一次連立方程式

$$\sum_{i=1}^N x_i^k y_i = \sum_{j=0}^M \left\{ a_j \sum_{i=1}^N x_i^{j+k} \right\}$$

$$
\Longleftrightarrow
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
\end{pmatrix}
$$

$$\left( s_k = \displaystyle \sum_{i=1}^N x_i^k, t_k = \displaystyle \sum_{i=1}^N x_i^k y_i \right)$$

を解くことに等しい。
