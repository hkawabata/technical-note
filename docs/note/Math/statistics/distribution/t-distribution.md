---
title: t 分布
title-en: Student's t-distribution
---

# t 分布とは

## 定義

母平均 $\mu$、母分散 $\sigma^2$ の正規分布に従う母集団から $n$ 件の標本を抽出するときを考える。

- $\bar{X}$：標本平均
- $s^2$：標本不偏分散

として、以下の式で定義される統計量 $t$ が従う分布を、**自由度 $n-1$ の t 分布**という。

$$
t := \cfrac{\bar{X} - \mu}{s/\sqrt{n}}
$$

## t 分布の重要性

平均 $\mu$、分散 $\sigma^2$（いずれも未知）の正規分布に従うと仮定できる確率変数 $X$ があるとき、$X$ から抽出した $n$ 個の標本 $X_1, \cdots, X_n$ から、母集団の平均 $\mu$ に関する推定や検定を行いたい。

$X \sim N(\mu, \sigma^2)$ であるから、標本平均

$$
\bar{X} := \cfrac{1}{n} \sum_{i=1}^n X_i = \cfrac{X_1}{n} + \cdots + \cfrac{X_n}{n} \sim N(\mu, \sigma^2/n)
$$

これを標準化すると、

$$
Z := \cfrac{\bar{X}-\mu}{\sigma/\sqrt{n}} \sim N(0, 1)
$$

標本数 $n$ と標本平均 $\bar{X}$ は既知なので、母分散 $\sigma^2$ が既知であれば、この $Z$ により、標準正規分布を用いて母平均 $\mu$ に関する推定や検定ができる。  
しかし多くの場合に母分散は未知。代わりに標本不偏分散

$$
s^2 := \cfrac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

であれば既知なので、母分散 $\sigma^2$ を標本不偏分散 $s^2$ で置き換えた

$$
t := \cfrac{\bar{X}-\mu}{s/\sqrt{n}}
$$

が従う分布を調べ、それを使って母平均 $\mu$ に関する推定・検定がしたい。

## 定義の拡張

カイ二乗分布についての定理（[参考](chi-square-distribution.md)）から、

$$
\chi^2 := \cfrac{(n-1)s^2}{\sigma^2} \sim \chi^2 (n-1)
$$

また、

$$
Z := \cfrac{\bar{X}-\mu}{\sigma/\sqrt{n}} \sim N(0, 1)
$$

これらを用いて、

$$
t := \cfrac{\bar{X}-\mu}{s/\sqrt{n}}
= \cfrac{\bar{X}-\mu}{\sigma/\sqrt{n}} \cfrac{\sigma}{s}
= Z \sqrt{\cfrac{n-1}{\chi^2}}
= \cfrac{Z}{\sqrt{\chi^2/(n-1)}}
$$

と書ける。すなわち、$t$ は

- 標準正規分布に従う確率変数 $Z$
- カイ二乗分布に従う確率変数 $\chi^2$ とその自由度

の式で表現できる。

このことを用いて、$t$ 分布の定義を以下のように拡張する。

> **【定義】**
>
> - 標準正規分布に従う確率変数 $Z$
> - 自由度 $k$ のカイ二乗分布に従う確率変数 $\chi_k^2$
>
> があるとき、
> 
> $$
t := \cfrac{Z}{\sqrt{\chi_k^2/k}}
$$
>
> が従う確率分布を **自由度 $k$ の t 分布** と呼び、$t(k)$ で表す。

## t 分布の利用

- 正規分布する母集団の母平均 $\mu$、母分散 $\sigma^2$ が未知、かつ標本サイズ $n$ が小さい場合に母平均 $\mu$ を推定・検定
	- cf. [区間推定](../estimation/interval-estimation.md)、[母平均の検定](../hypothesis-testing/testing-for-the-mean.md)
- 2つの平均値の有意差を検討
	- cf. [2標本 t 検定](../hypothesis-testing/two-sample-t-test.md)


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

（略）


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

（ToDo：導出）
