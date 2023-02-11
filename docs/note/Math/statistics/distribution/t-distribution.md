---
title: t 分布
title-en: Student's t-distribution
---

# t 分布とは

平均 $\mu$、不偏分散 $s^2$ の正規分布に従う母集団から $n$ 件の標本を抽出した際に、以下の式で定義される統計量 $t$ が従う分布を、**自由度 $n-1$ の t 分布**という。

$$
t \equiv \cfrac{\bar{x} - \mu}{s/\sqrt{n}}
$$

ただし、$\bar{x}$ は標本平均。

# 確率密度関数

## 式

自由度 $n-1 \equiv \nu$ として、

$$
f_\nu(t) = \cfrac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi} \Gamma(\nu/2)}
\left( 1 + \cfrac{t^2}{\nu} \right)^{-(\nu+1)/2}
$$

ここで $\Gamma$ はガンマ関数で、以下の式で定義される。

$$
\Gamma(z) = \int_{0}^{\infty} t^{z-1} e^{-t} dt
$$

## 特徴

t 分布の確率密度関数は、自由度 $\nu$ に応じて以下の形になる。  
図の通り、$n \to \infty$ のとき t 分布は標準正規分布 $N(0, 1)$ に近づく。

![Figure_1](https://user-images.githubusercontent.com/13412823/216806950-9b7bfe18-2913-4de2-af81-4d88e4043d1d.png)

（描画に使った Python コード）

```python
import numpy as np
import math
from matplotlib import pyplot as plt

t = np.linspace(-5, 5, 100)
y_norm = np.exp(-t**2 * 0.5) / math.sqrt(2 * math.pi)

for nu in [1, 2, 3, 5, 10, 100]:
	y = (1 + t**2 / nu) ** (-(nu+1)*0.5)
	y *= math.gamma((nu+1)*0.5) / math.gamma(nu*0.5) / math.sqrt(nu * math.pi)
	plt.plot(t, y, label=r'$\nu = {}$'.format(nu))

plt.plot(t, y_norm, linestyle='dotted', color='black', label='$N(0, 1)$')
plt.title('t-distribution')
plt.xlabel('$t$')
plt.legend()
plt.grid()
plt.show()
```

## 導出

（ToDo）

# t 分布の利用

- 正規分布する母集団の母平均 $\mu$、母分散 $\sigma^2$ が未知、かつ標本サイズ $n$ が小さい場合に母平均 $\mu$ を推定
- 2つの平均値の有意差を検討（t 検定）


# t 分布の期待値・分散

## 期待値

式より、$t$ の確率密度関数 $f_\nu (t)$ は $t$ の偶関数なので、

$$
f_\nu (-t) = f_\nu(t)
$$

よって

$$
\begin{eqnarray}
	E(t)
	&=&
	\int_{-\infty}^\infty t f_\nu (t) dt
	\\ &=&
	\int_\infty^{-\infty} (-s) f_\nu (-s) (-ds) \qquad (s = -t)
	\\ &=&
	- \int_{-\infty}^\infty s f_\nu (s) ds
	\\ &=&
	- E(t)
\end{eqnarray}
$$

よって

$$
E(t) = 0
$$

## 分散

$\nu \gt 2$ のとき、

$$
V(t) = \cfrac{\nu}{\nu-2}
$$

（ToDo：証明）
