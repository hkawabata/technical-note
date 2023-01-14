---
title: カイ二乗分布
title-en: Chi-Square Distribution
---

# カイ二乗分布とは

標準正規分布に従う互いに独立な $k$ 個の確率変数 $Z_1, \cdots, Z_k$ に対して、

$$
\chi^2 = Z_1^2 + \cdots + Z_k^2
$$

が従う分布を **自由度 $k$ のカイ二乗分布** という。

確率密度関数は以下の式で表される。

$$
f_k(x) = \begin{cases}
	\cfrac{1}{2^{k/2} \Gamma(k/2)} e^{-x/2}x^{k/2-1} & & 0 \le x \\
	0 & & x \lt 0
\end{cases}
$$

ここで $\Gamma$ はガンマ関数で、以下の式で定義される。

$$
\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t} dt
$$

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


# カイ二乗分布の特徴

![Figure_1](https://user-images.githubusercontent.com/13412823/212242584-fcb0e3f3-8015-453c-ac7c-04b9e69a34e1.png)


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