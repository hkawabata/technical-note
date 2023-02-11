---
title: カイ二乗分布
title-en: Chi-Square Distribution
---

# カイ二乗分布とは

標準正規分布に従う互いに独立な $k$ 個の確率変数 $Z_1, \cdots, Z_k$ に対して、

$$
\chi^2 = Z_1^2 + \cdots + Z_k^2
$$

が従う分布を **自由度 $k$ のカイ二乗分布** といい、$\chi^2(k)$ で表す。

# 確率密度関数

## 式

確率密度関数は以下の式で表される。

$$
f_k(x) = \begin{cases}
	\cfrac{1}{2^{k/2} \Gamma(k/2)} e^{-x/2}x^{k/2-1} & & 0 \le x \\
	0 & & x \lt 0
\end{cases}
$$

ここで $\Gamma$ は[ガンマ関数](../../special-functions/gamma-function.md)であり、以下の式で定義される。

$$
\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t} dt
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/212242584-fcb0e3f3-8015-453c-ac7c-04b9e69a34e1.png)

（描画に使った Python コード）
```python
import numpy as np
import math
from matplotlib import pyplot as plt

def chi_square(x, k):
	return np.exp(-x*0.5) / (2**(k*0.5)) / math.gamma(k*0.5) * np.power(x, k*0.5-1)

x = np.linspace(0, 40.0, 1000)
for k in range(1, 30+1):
	y = chi_square(x, k)
	if k in {1, 2, 3, 5, 10, 20, 30}:
		plt.plot(x, y, lw=2.0, label='$k = {}$'.format(k))
	else:
		plt.plot(x, y, lw=0.5, color='black')

plt.xlabel('$x$')
plt.ylabel('$f_k(x)$')
plt.xlim([0, 40.0])
plt.ylim([0, 0.6])
plt.legend()
plt.show()
```

## 確率密度関数の導出

数学的帰納法で証明できる。

### $k=1$ のとき

$$
\chi^2 = Z_1^2
$$

$Z_1$ は標準正規分布に従うので、$Z_1$ の確率密度関数は

$$
\phi(Z_1) = \cfrac{1}{\sqrt{2\pi}} \exp{\left( -\cfrac{Z_1^2}{2} \right)}
$$

新しい確率変数 $Y \equiv Z_1^2 (= \chi^2)$ を定義し、$Y$ の累積分布関数 $F(y)$ を計算すると、

$$
\begin{eqnarray}
	F(y) &=& P(Y \le y)
	\\ &=&
	P(Z_1^2 \le y)
	\\ &=&
	P(- \sqrt{y} \le Z_1 \le \sqrt{y})
	\\ &=&
	\int_{-\sqrt{y}}^{\sqrt{y}} \phi(Z_1) dZ_1
	\\ &=&
	\Phi(\sqrt{y}) - \Phi(-\sqrt{y})
\end{eqnarray}
$$

ここで、$\Phi(Z_1)$ は $\phi(Z_1)$ の不定積分とする。

$Y$ の確率密度関数 $f(y)$ は累積分布関数を $y$ で微分すれば得られるので、

$$
\begin{eqnarray}
	f(y) &=& \cfrac{d}{dy} F(y)
	\\ &=&
	\cfrac{d}{dy} (\Phi(\sqrt{y})) - \cfrac{d}{dy} (\Phi(-\sqrt{y}))
	\\ &=&
	\phi(\sqrt{y}) \cfrac{d}{dy} (\sqrt{y}) -
	\phi(-\sqrt{y}) \cfrac{d}{dy} (-\sqrt{y})
	\\ &=&
	\cfrac{1}{\sqrt{2\pi}} \exp{\left( -\cfrac{y}{2} \right)} \cfrac{1}{2\sqrt{y}} +
	\cfrac{1}{\sqrt{2\pi}} \exp{\left( -\cfrac{y}{2} \right)} \cfrac{1}{2\sqrt{y}}
	\\ &=&
	\cfrac{1}{\sqrt{2\pi}} \exp{\left( -\cfrac{y}{2} \right)} \cfrac{1}{\sqrt{y}}
	\\ &=&
	\cfrac{1}{2^{1/2} \Gamma(1/2)} e^{-y/2}y^{1/2-1}
\end{eqnarray}
$$

これは $k=1$ のときのカイ二乗分布の式に一致。

### $k=n (\ge 2)$ のとき

$$\chi_{n-1}^2 \equiv Z_1^2 + \cdots + Z_{n-1}^2$$

が自由度 $n-1$ のカイ二乗分布の式に従うと仮定する。

このとき、$k = n$ の場合のカイ二乗値、すなわち

$$
\chi_n^2 \equiv Z_1^2 + \cdots + Z_n^2 = \chi_{n-1}^2 + Z_n^2
$$

の確率密度関数を考える。

$Z_1, \cdots, Z_n$ はそれぞれ互いに独立であるから、$\chi_{n-1}^2, Z_n^2$ も互いに独立。  

新しい確率変数

$$
\begin{eqnarray}
	X &\equiv& \chi_{n-1}^2 \\
	Y &\equiv& Z_n^2
\end{eqnarray}
$$

を導入すると、

- $X$ は仮定より自由度 $n-1$ のカイ二乗分布 $f_{n-1}(x)$ に従う
- $Y$ は前述の「$k=1$ のとき」より自由度1のカイ二乗分布 $f_1(y)$ に従う
- $X, Y$ は互いに独立

独立な確率変数の和を考える時、その確率密度関数は畳み込みで与えられる（[参考](../sum-of-independent-random-variable.md)）ので、$Z \equiv \chi_n^2 = X + Y$ の確率密度関数 $f(z)$ は、

$$
\begin{eqnarray}
	f(z) &=&
	\int_{0}^{z} f_{n-1}(y) f_1(z-y) dy
	\\ &=&
	\cdots
	\\ &=&
	\cfrac{1}{2^{n/2} \Gamma(n/2)} e^{-z/2}z^{n/2-1}
\end{eqnarray}
$$

（ToDo：途中計算）


# カイ二乗分布の利用

（ToDo）

# カイ二乗分布の期待値・分散

## 期待値

$$
\begin{eqnarray}
	E(x) &=&
	\int_{0}^{\infty} x \cfrac{1}{2^{k/2} \Gamma(k/2)} e^{-x/2}x^{k/2-1} dx
	\\ &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)}
	\int_{0}^{\infty} e^{-x/2}x^{k/2} dx
\end{eqnarray}
$$

$\cfrac{x}{2} = t$ とおけば、

$$
\begin{eqnarray}
	E(x) &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)}
	\int_{0}^{\infty} e^{-t}(2t)^{k/2} 2dt
	\\ &=&
	\cfrac{2}{\Gamma(k/2)}
	\int_{0}^{\infty} e^{-t}t^{k/2} dt
	\\ &=&
	\cfrac{2}{\Gamma(k/2)}
	\left(
		\left[ - e^{-t}t^{k/2} \right]_{0}^{\infty}
		+ \cfrac{k}{2} \int_{0}^{\infty} e^{-t}t^{k/2-1} dt
	\right)
	\\ &=&
	\cfrac{2}{\Gamma(k/2)}
	\left(
		0 + \cfrac{k}{2} \Gamma(k/2)
	\right)
	\\ &=&
	k
\end{eqnarray}
$$

## 分散

$$
\begin{eqnarray}
	E(x^2) &=&
	\int_{0}^{\infty} x^2 \cfrac{1}{2^{k/2} \Gamma(k/2)} e^{-x/2}x^{k/2-1} dx
	\\ &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)}
	\int_{0}^{\infty} e^{-x/2}x^{k/2+1} dx
\end{eqnarray}
$$

$\cfrac{x}{2} = t$ とおけば、

$$
\begin{eqnarray}
	E(x^2) &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)}
	\int_{0}^{\infty} e^{-t}(2t)^{k/2+1} 2dt
	\\ &=&
	\cfrac{4}{\Gamma(k/2)}
	\int_{0}^{\infty} e^{-t}t^{k/2+1} dt
	\\ &=&
	\cfrac{4}{\Gamma(k/2)}
	\left(
		\left[ - e^{-t}t^{k/2+1} \right]_{0}^{\infty}
		+ \cfrac{k+2}{2} \int_{0}^{\infty} e^{-t}t^{k/2} dt
	\right)
	\\ &=&
	\cfrac{2(k+2)}{\Gamma(k/2)}
	\int_{0}^{\infty} e^{-t}t^{k/2} dt
	\\ &=&
	\cfrac{2(k+2)}{\Gamma(k/2)}
	\left(
		\left[ - e^{-t}t^{k/2} \right]_{0}^{\infty}
		+ \cfrac{k}{2} \int_{0}^{\infty} e^{-t}t^{k/2-1} dt
	\right)
	\\ &=&
	\cfrac{2(k+2)}{\Gamma(k/2)} \cfrac{k}{2} \Gamma(k/2)
	\\ &=&
	k(k+2)
\end{eqnarray}
$$

したがって、

$$
\begin{eqnarray}
	V(x) &=& E(x^2) - E(x)^2
	\\ &=&
	k(k+2) - k^2
	\\ &=&
	2k
\end{eqnarray}
$$

## モーメント母関数

$$
\begin{eqnarray}
	M_X(t) &=& E(e^{tX})
	\\ &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)} \int_{0}^{\infty} e^{tX} e^{-X/2} X^{k/2-1} dX
	\\ &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)} \int_{0}^{\infty} e^{-(1-2t)X/2} X^{k/2-1} dX
\end{eqnarray}
$$

$\cfrac{1-2t}{2}X = s$ とおけば、 $dX = \cfrac{2}{1-2t} ds$

モーメント母関数を利用する $t=0$ 近傍について考えると、$x \to \infty$ のとき $s \to \infty$ であるから、

$$
\begin{eqnarray}
	M_X(t) &=&
	\cfrac{1}{2^{k/2} \Gamma(k/2)} \int_{0}^{\infty} e^{-s} \left( \cfrac{2}{1-2t} s \right)^{k/2-1} \cfrac{2}{1-2t} ds
	\\ &=&
	\cfrac{1}{(1-2t)^{k/2} \Gamma(k/2)}
	\int_{0}^{\infty} e^{-s} s^{k/2-1} ds
	\\ &=&
	\cfrac{1}{(1-2t)^{k/2} \Gamma(k/2)}
	\Gamma(k/2)
	\\ &=&
	(1-2t)^{-k/2}
\end{eqnarray}
$$


# カイ二乗分布の性質

## カイ二乗分布の和の再生性

> **【定理】**
> 
> 独立な確率変数 $X, Y$ がそれぞれ自由度 $n_A, n_B$ のカイ二乗分布に従う、すなわち
> 
> $$
\begin{eqnarray}
X \sim \chi^2 (n_X) \\
Y \sim \chi^2 (n_Y)
\end{eqnarray}
$$
> 
> を満たすとき、
> 
> $$
Z := X + Y \sim \chi^2(n_X + n_Y)
$$

**【証明】**

独立な確率変数の和の確率密度関数は、それぞれの変数の密度関数の畳込みで与えられる（[参考](../sum-of-independent-random-variable.md)）ので、$X, Y, Z$ の確率密度関数をそれぞれ $f_X, f_Y, f_Z$ とすると、

$$
\begin{eqnarray}
	f_Z(z) &=& \int_{-\infty}^\infty f_X (t) f_Y (z-t) dt
	\\ &=&
	\int_0^z
		\cfrac{1}{2^{n_X/2} \Gamma(n_X/2)} e^{-t/2}t^{n_X/2-1}
		\cfrac{1}{2^{n_Y/2} \Gamma(n_Y/2)} e^{-(z-t)/2}(z-t)^{n_Y/2-1}
	dt
	\\ &=&
	\cfrac{1}{2^{(n_X+n_Y)/2} \Gamma(n_X/2) \Gamma(n_Y/2)} e^{-z/2}
	\int_0^z t^{n_X/2-1} (z-t)^{n_Y/2-1} dt
\end{eqnarray}
$$

※ 途中、積分範囲が $0 \le t \le z$ に変わっているのは、この範囲の外ではカイ二乗分布の密度関数 $f_x(t), f_Y(z-t)$ いずれかの値がゼロとなるため。

ここで、最後の式の積分を変形すると

$$
\begin{eqnarray}
	\int_0^z t^{n_X/2-1} (z-t)^{n_Y/2-1} dt
	&=&
	\int_0^1 (zu)^{n_X/2-1} (z-zu)^{n_Y/2-1} (z du) \qquad (t = zu)
	\\ &=&
	z^{(n_X+n_Y)/2-1}
	\int_0^1 u^{n_X/2-1} (1-u)^{n_Y/2-1} du
	\\ &=&
	z^{(n_X+n_Y)/2-1} B \left( \cfrac{n_X}{2}, \cfrac{n_Y}{2} \right)
	\\ &=&
	z^{(n_X+n_Y)/2-1}
	\cfrac{\Gamma(n_X/2) \Gamma(n_Y/2)}{\Gamma((n_X+n_Y)/2)}
\end{eqnarray}
$$

※ $B(x, y)$ は[ベータ関数](../../special-functions/beta-function.md)であり、式変形の途中、[ガンマ関数](../../special-functions/gamma-function.md)との間の関係式を利用している。

以上により、

$$
\begin{eqnarray}
	f_Z(z)
	&=&
	\cfrac{1}{2^{(n_X+n_Y)/2} \Gamma(n_X/2) \Gamma(n_Y/2)} e^{-z/2}
	\cdot
	z^{(n_X+n_Y)/2-1}
	\cfrac{\Gamma(n_X/2) \Gamma(n_Y/2)}{\Gamma((n_X+n_Y)/2)}
	\\ &=&
	\cfrac{1}{2^{(n_X+n_Y)/2} \Gamma((n_X+n_Y)/2)}
	e^{-z/2} z^{(n_X+n_Y)/2-1}
\end{eqnarray}
$$

これは自由度 $n_X+n_Y$ のカイ二乗分布の確率密度関数であるから、

$$
Z \sim \chi^2 (n_X+n_Y)
$$


## 不偏分散とカイ二乗分布

> **【定理】** 平均 $\mu$、分散 $\sigma^2$ の正規分布に従う独立な $n$ 個の確率変数 $X_1, \cdots, X_n$ の平均を $\bar{X}$、不偏分散を $s^2$ とする。
> 
> $$
\begin{eqnarray}
	\bar{X} &=& \cfrac{1}{n} \sum_{i=1}^n X_i \\
	s^2 &=& \cfrac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
\end{eqnarray}
$$
> 
> このとき、
> 
> $$
\cfrac{(n-1)s^2}{\sigma^2} =
\cfrac{1}{\sigma^2} \sum_{i=1}^n (X_i - \bar{X})^2
$$
> 
> は自由度 $n-1$ のカイ二乗分布 $\chi^2(n-1)$ に従う。

> **【NOTE】** この定理は、母平均が未知の正規分布に従う母集団について、**母分散の区間推定や検定を行う際に利用される** ため非常に重要。

**【証明】**

$X_1, \cdots, X_n$ は正規分布 $N(\mu, \sigma^2)$ に従うので、それぞれを標準化した変数

$$
Z_i := \cfrac{X_i-\mu}{\sigma}
$$

を考えると、$\boldsymbol{z} = (Z_1, \cdots, Z_n)$ はそれぞれ独立に標準正規分布 $N(0, 1)$ に従う。  
よって、$\boldsymbol{z}$ の同時確率密度関数はそれぞれの確率密度関数の積となり、

$$
\begin{eqnarray}
	f(\boldsymbol{z})
	&=&
	\prod_{i=1}^n
	\cfrac{1}{\sqrt{2\pi}}
	\exp{\left( \cfrac{Z_i^2}{2} \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \sum_{i=1}^n Z_i^2 \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \boldsymbol{z}^T \boldsymbol{z} \right)}
\end{eqnarray}
$$

ただし、最後の式では $\boldsymbol{z}$ を列ベクトルとして扱っている。

ここで、一行目の成分が全て $1/\sqrt{n}$ であるような[直交行列](../../matrix/orthogonal-matrix.md)の1つ

$$
A = \begin{pmatrix}
	\frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \cdots & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}}\\
	a_{21} & a_{22} & \cdots & a_{2(n-1)} & a_{2n} \\
	& & \vdots & & \\
	& & \vdots & & \\
	a_{n1} & a_{n2} & \cdots & a_{n(n-1)} & a_{nn}
\end{pmatrix}
$$

を導入し（**補題：任意の $n$ に対してこのような直交行列が存在することの証明**）、

$$
\begin{pmatrix} Y_1 \\ \vdots \\ Y_n \end{pmatrix}
=
A \begin{pmatrix} Z_1 \\ \vdots \\ Z_n \end{pmatrix}
$$

により $\boldsymbol{z} = (Z_1, \cdots, Z_n)$ を $\boldsymbol{y} = (Y_1, \cdots, Y_n)$ に変換する。

多変数の確率変数を変換した際の同時確率密度の変換公式（cf. [同時確率分布](../joint-probability-distribution.md)）により、

$$
\begin{eqnarray}
	f(\boldsymbol{y}) &=& f(\boldsymbol{z}(\boldsymbol{y})) \det J
	\\
	\\
	J &:=& \begin{pmatrix}
		\frac{\partial Z_1}{\partial Y_1} & \frac{\partial Z_1}{\partial Y_2} & \cdots & \frac{\partial Z_1}{\partial Y_n} \\
		\frac{\partial Z_2}{\partial Y_1} & \frac{\partial Z_2}{\partial Y_2} & \cdots & \frac{\partial Z_2}{\partial Y_n} \\
		\vdots & \vdots & \ddots & \vdots \\
		\frac{\partial Z_n}{\partial Y_1} & \frac{\partial Z_n}{\partial Y_2} & \cdots & \frac{\partial Z_n}{\partial Y_n} \\
	\end{pmatrix}
\end{eqnarray}
$$

$\boldsymbol{y} = A \boldsymbol{z}$ より $\boldsymbol{z} = A^{-1} \boldsymbol{y} = A^T \boldsymbol{y}$ なので、 $J$ を計算すると、

$$
J = \begin{pmatrix}
	\frac{1}{\sqrt{n}} & a_{21} & \cdots & a_{n1} \\
	\frac{1}{\sqrt{n}} & a_{22} & \cdots & a_{n2} \\
	\vdots & \vdots & \ddots & \vdots \\
	\frac{1}{\sqrt{n}} & a_{2n} & \cdots & a_{nn} \\
\end{pmatrix}
=
A^T
$$

直交行列の行列式は1なので、

$$
\det J = \det A^T = \det A = 1
$$

よって

$$
\begin{eqnarray}
	f(\boldsymbol{y}) &=& f(\boldsymbol{z}(\boldsymbol{y}))
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \boldsymbol{z}(\boldsymbol{y})^T \boldsymbol{z}(\boldsymbol{y}) \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} (A^T \boldsymbol{y})^T (A^T \boldsymbol{y}) \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \boldsymbol{y}^T A A^T \boldsymbol{y} \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \boldsymbol{y}^T \boldsymbol{y} \right)}
	\\ &=&
	\cfrac{1}{(2\pi)^{n/2}}
	\exp{\left( \cfrac{1}{2} \sum_{i=1}^n Y_i^2 \right)}
	\\ &=&
	\prod_{i=1}^n
	\cfrac{1}{\sqrt{2\pi}}
	\exp{\left( \cfrac{Y_i^2}{2} \right)}
\end{eqnarray}
$$

したがって、$\boldsymbol{y} = (Y_1, \cdots, Y_n)$ の同時確率密度が $Y_1, \cdots, Y_n$ それぞれの標準正規分布の密度関数の積で表されるので、$Y_1, \cdots, Y_n$ はそれぞれ独立に標準正規分布に従う：

$$
Y_i \sim N(0, 1)
$$

行列 $A$ の1行目は全て $1/\sqrt{n}$ であるから、

$$
Y_1 = \cfrac{1}{\sqrt{n}} \sum_{i=1}^n Z_i = \sqrt{n} \bar{Z}
$$

ここで $\bar{Z} := \sum_{i=1}^n Z_i$ と置いた。

また、

$$
\begin{eqnarray}
	\sum_{i=1}^n (Z_i - \bar{Z})^2
	&=&
	\sum_{i=1}^n Z_i^2 -
	2 \bar{Z} \sum_{i=1}^n Z_i +
	n\bar{Z}^2
	\\ &=&
	\sum_{i=1}^n Z_i^2 -
	2 \bar{Z} \cdot n\bar{Z} +
	n\bar{Z}^2
	\\ &=&
	\sum_{i=1}^n Z_i^2 - n \bar{Z}^2
	\\ &=&
	\sum_{i=1}^n Z_i^2 - Y_1^2
\end{eqnarray}
$$

ここで $\boldsymbol{z} = A^T \boldsymbol{y}$ かつ $A$ は直交行列なので、

$$
\begin{eqnarray}
	\sum_{i=1}^n Z_i^2 &=& \boldsymbol{z}^T \boldsymbol{z}
	\\ &=&
	(A^T \boldsymbol{y})^T (A^T \boldsymbol{y})
	\\ &=&
	\boldsymbol{y}^T A A^T \boldsymbol{y}
	\\ &=&
	\boldsymbol{y}^T \boldsymbol{y}
	\\ &=&
	\sum_{i=1}^n Y_i^2
\end{eqnarray}
$$

以上により、

$$
\begin{eqnarray}
	\sum_{i=1}^n (Z_i - \bar{Z})^2
	&=&
	\sum_{i=1}^n Z_i^2 - Y_1^2
	\\ &=&
	\sum_{i=1}^n Y_i^2 - Y_1^2
	\\ &=&
	\sum_{i=2}^n Y_i^2
\end{eqnarray}
$$

したがって、$\sum_{i=1}^n (Z_i - \bar{Z})^2$ はそれぞれ独立で標準正規分布に従う $n-1$ 個の確率変数 $Y_2, \cdots, Y_n$ の平方和であるから、

$$
\sum_{i=1}^n (Z_i - \bar{Z})^2 \sim \chi^2 (n-1)
$$

また、

$$
\begin{eqnarray}
	Z_i - \bar{Z}
	&=&
	\cfrac{X_i-\mu}{\sigma} -
	\cfrac{1}{n} \sum_{k=1}^n \cfrac{X_k-\mu}{\sigma}
	\\ &=&
	\cfrac{X_i-\mu}{\sigma} -
	\cfrac{1}{\sigma} \cfrac{1}{n} \sum_{k=1}^n X_k +
	\cfrac{\mu}{\sigma}
	\\ &=&
	\cfrac{X_i}{\sigma} - \cfrac{\bar{X}}{\sigma}
	\\ &=&
	\cfrac{X_i - \bar{X}}{\sigma}
\end{eqnarray}
$$

であるから、

$$
\begin{eqnarray}
	\sum_{i=1}^n (Z_i - \bar{Z})^2
	&=&
	\sum_{i=1}^n \cfrac{(X_i - \bar{X})^2}{\sigma^2}
	\\ &=&
	\cfrac{n-1}{\sigma^2}
	\cfrac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
	\\ &=&
	\cfrac{(n-1) s^2}{\sigma^2}
\end{eqnarray}
$$

以上により、

$$
\cfrac{(n-1)s^2}{\sigma^2} =
\sum_{i=1}^n (Z_i - \bar{Z})^2
\sim \chi^2(n-1)
$$


> **【補題】** 任意の整数 $n \ge 2$ に対して、1行目成分が全て $1/\sqrt{n}$ であるような $n \times n$ 直交行列 $A$ が存在する

**【証明】**

$$
A = \begin{pmatrix}
	\frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \cdots & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}}\\
	a_{21} & a_{22} & \cdots & a_{2(n-1)} & a_{2n} \\
	& & \vdots & & \\
	& & \vdots & & \\
	a_{n1} & a_{n2} & \cdots & a_{n(n-1)} & a_{nn}
\end{pmatrix}
=
(\boldsymbol{a}_1, \boldsymbol{a}_2, \cdots, \boldsymbol{a}_n)
$$

と置く。ここで、 $\boldsymbol{a}_i$ はベクトル $\left( \frac{1}{\sqrt{n}}, a_{2i}, a_{3i}, \cdots, a_{ni} \right)$ を列ベクトルとしたもの。

$A$ が直交行列となるための必要十分条件は、任意の $i\ne j$ に対して $\boldsymbol{a}_i \cdot \boldsymbol{a}_j = 0$ となること。  

- この制約は $i, j$ の組み合わせの選び方の数だけあるから、$n(n+1)/2$ 通り
- これらの制約の式に登場する変数 $a_{kl}$ の数は、$2 \le k \le n, 1\le l \le n$ より $n(n-1)$ 通り

変数 $a_{kl}$ を決める自由度 $n(n-1)$ が、制約となる方程式 $\boldsymbol{a}_i \cdot \boldsymbol{a}_j = 0$ の数 $n(n+1)/2$ 以上であれば、制約を満たす $A$ が存在すると言える。

$$
n(n-1) - \cfrac{n(n+1)}{2} = \cfrac{n(n-3)}{2}
$$

よって $n \ge 3$ のとき、直交行列 $A$ は存在する。

また、$n=2$ のとき、

$$
A = \begin{pmatrix}
	\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
	a & b
\end{pmatrix}
$$

とおくと、

$$
A A^T = \begin{pmatrix}
	1 & \frac{1}{\sqrt{2}} (a+b) \\
	\frac{1}{\sqrt{2}} (a+b) & a^2 + b^2
\end{pmatrix}
$$

であるから、$(a,b) = \left( \frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}} \right)$ とすれば $A A^T = I$ が成り立つ。  
このとき $A^T = A$ なので、 $A^T A = I$ も成り立つ。

以上により、任意の整数 $n \ge 2$ に対して、1行目成分が全て $1/\sqrt{n}$ であるような $n \times n$ 直交行列 $A$ が存在する。