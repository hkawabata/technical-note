---
title: 歪正規分布
title-en: Skew Normal Distribution
---

# 歪正規分布とは


# 確率密度関数

与えられたパラメータ $\lambda \gt 0$ に対し、

$$
f_\lambda (x) = 2 \phi(x) \Phi (\lambda x)
$$

ただし、$\phi(x)$ は標準正規分布の確率密度関数

$$
\phi(x) := \cfrac{1}{\sqrt{2\pi}} \exp \left( - \cfrac{x^2}{2} \right)
$$

$\Phi(x)$ はその累積密度関数

$$
\Phi(x) = \int_{-\infty}^x \phi(t) dt = \cfrac{1}{2} \left( 1 + \mathrm{erf} \left( \cfrac{x}{\sqrt{2}} \right) \right)
$$

$\mathrm{erf}$ は[誤差関数](../../special-functions/error-function.md)。

![Figure_1](https://user-images.githubusercontent.com/13412823/250331486-d027f032-c13b-4cc6-be9f-327215990fb6.png)

```python
import numpy
from scipy.special import erf
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 501)

def skew_norm(x, lamb):
	return 2 * np.exp(-x*x/2.0)/np.sqrt(2*np.pi) * (1+erf(lamb*x/np.sqrt(2)))/2.0

for lamb in [-4, -2, 0, 2, 4]:
	y = skew_norm(x, lamb)
	plt.plot(x, y, label=r'$\lambda={}$'.format(lamb))

plt.legend()
plt.grid()
plt.show()
```
