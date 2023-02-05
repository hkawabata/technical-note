---
title: ガンマ関数
title-en: Gamma Function
---

# ガンマ関数とは

実部が正であるような複素数 $z$ に対して、以下の式で定義される関数。

$$
\Gamma(z) \equiv \int_0^\infty t^{z-1} e^{-t} dt
$$

後述の性質から、「階乗の一般化（整数以外への階乗の拡張）」と言える。

![Figure_1](https://user-images.githubusercontent.com/13412823/216817551-0d233bd5-24a7-4ee8-abd8-e08de74f1d63.png)


（描画に使った Python コード）

```python
import numpy as np
import math
from matplotlib import pyplot as plt

np_gamma = np.frompyfunc(math.gamma, 1, 1)
x = np.linspace(1e-4, 5, 1000)
y = np_gamma(x)
plt.ylim([0, 10])
plt.xlabel(r'$z$', fontsize=18)
plt.ylabel(r'$\Gamma(z)$', fontsize=18)
plt.plot(x, y)
plt.grid()
plt.show()
```

# ガンマ関数の性質

## 漸化式

> **【定理】**
> 
> $$
\Gamma(z+1) = z \Gamma(z)
$$

**【証明】**

$$
\begin{eqnarray}
	\Gamma(z+1)
	&=&
	\int_0^\infty t^z e^{-t} dt
	\\ &=&
	\left[ -t^z e^{-t} \right]_0^\infty -
	\int_0^\infty (-z t^{z-1} e^{-t}) dt
	\\ &=&
	z \int_0^\infty t^{z-1} e^{-t} dt
	\\ &=&
	z \Gamma(z)
\end{eqnarray}
$$

途中、$\mathrm{Re}\ z \gt 0$ より

$$
\begin{eqnarray}
	\left[ -t^z e^{-t} \right]_0^\infty
	&=&
	\lim_{t \to \infty} (-t^z e^{-t}) - 0 \cdot 1
	\\ &=&
	0
\end{eqnarray}
$$

となることを用いた。

## 特別な引数のときのガンマ関数の値

> **【定理】**
> 
> $$
\begin{eqnarray}
	\Gamma(1) &=& 1 \\
	\Gamma(1/2) &=& \sqrt{\pi}
\end{eqnarray}
$$

**【証明】**

$$
\begin{eqnarray}
	\Gamma(1)
	&=&
	\int_0^\infty t^{1-1} e^{-t} dt
	\\ &=&
	\int_0^\infty e^{-t} dt
	\\ &=&
	\left[ -e^{-t} \right]_0^\infty
	\\ &=&
	(-0) - (-1)
	\\ &=&
	1
	\\
	\Gamma(1/2)
	&=&
	\int_0^\infty t^{1/2-1} e^{-t} dt
	\\ &=&
	\int_0^\infty \cfrac{e^{-t}}{\sqrt{t}} dt
	\\ &=&
	\int_0^\infty \cfrac{e^{-s^2}}{s} 2s\ ds
	\qquad (s = \sqrt{t} \to dt = 2s \cdot ds)
	\\ &=&
	2 \int_0^\infty e^{-s^2} ds
	\\ &=&
	2 \cdot \cfrac{1}{2} \int_{-\infty}^\infty e^{-s^2} ds
	\\ &=&
	\sqrt{\pi} \qquad (\mathrm{Gaussian}\ \mathrm{integral})
\end{eqnarray}
$$

## 階乗の一般化

> **【定理】**
>
> $n$ が整数のとき、
> 
> $$
\Gamma(n) = (n-1)!
$$

**【証明】**

ここまでに示した定理から、

$$
\begin{eqnarray}
	\Gamma(n) &=& (n-1) \Gamma(n-1)
	\\ &=&
	(n-1) (n-2) \Gamma(n-2)
	\\ &=&
	\cdots
	\\ &=&
	(n-1)! \Gamma(1)
	\\ &=&
	(n-1)!
\end{eqnarray}
$$
