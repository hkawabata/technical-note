---
title: ベータ分布
title-en: Beta Distribution
---

# ベータ分布とは

連続確率分布の一つ。
ある試行を何度か行った時、成功数 $\alpha$ と失敗数 $\beta$（ただし、$\alpha, \beta \gt 0$）が分かっている現象の成功率 $p$ の分布を表す。

確率密度関数は以下の式で表される。

$$
\begin{eqnarray}
  f_{\alpha, \beta} (p) &=& \cfrac{1}{B(\alpha, \beta)} p^{\alpha-1} (1-p)^{\beta-1}
  \\
  B(\alpha, \beta) &=& \int_{0}^{1} x^{\alpha-1} (1-x)^{\beta-1} dx
\end{eqnarray}
$$

$B(\alpha, \beta)$ は規格化のための定数。


# 確率密度関数の導出

略

# ベータ分布の期待値・分散

## 準備

一般に、$m, n$ を自然数とすると、部分積分を用いて

$$
\begin{eqnarray}
  \int_{0}^{1} x^m (1-x)^n dx
  &=&
  \left[ \cfrac{1}{m+1} x^{m+1} (1-x)^n \right]_0^1
  - \left( - \cfrac{n}{m+1} \int_{0}^{1} x^{m+1} (1-x)^{n-1} dx \right)
  \\ &=&
  \cfrac{n}{m+1}
  \int_{0}^{1} x^{m+1} (1-x)^{n-1} dx
  \\ &=&
  \cfrac{n}{m+1} \left(
    \left[ \cfrac{1}{m+2} x^{m+2} (1-x)^{n-1} \right]_0^1
    - \left( - \cfrac{n-1}{m+2} \int_{0}^{1} x^{m+2} (1-x)^{n-2} dx \right)
  \right)
  \\ &=&
  \cfrac{n}{m+1} \cfrac{n-1}{m+2} 
  \int_{0}^{1} x^{m+2} (1-x)^{n-2} dx
  \\ &=&
  \cdots
  \\ &=&
  \cfrac{n}{m+1} \cfrac{n-1}{m+2} \cdots \cfrac{1}{m+n}
  \int_{0}^{1} x^{m+n} (1-x)^{0} dx
  \\ &=&
  \cfrac{m!n!}{(m+n)!}
  \left[ \cfrac{1}{m+n+1} x^{m+n+1} \right]_0^1
  \\ &=&
  \cfrac{m!n!}{(m+n+1)!}
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
  B(\alpha, \beta)
  &=&
  \int_{0}^{1} x^{\alpha-1} (1-x)^{\beta-1} dx
  \\ &=&
  \cfrac{(\alpha-1)!(\beta-1)!}{((\alpha-1)+(\beta-1)+1)!}
  \\ &=&
  \cfrac{(\alpha-1)!(\beta-1)!}{(\alpha+\beta-1)!}
\end{eqnarray}
$$

## 期待値

$$
\begin{eqnarray}
  E(p) &=& \int_{0}^{1} p \cfrac{1}{B(\alpha, \beta)} p^{\alpha-1} (1-p)^{\beta-1} dp
  \\ &=&
  \cfrac{1}{B(\alpha, \beta)}
  \int_{0}^{1} p^{\alpha} (1-p)^{\beta-1} dp
  \\ &=&
  \cfrac{(\alpha+\beta-1)!}{(\alpha-1)!(\beta-1)!}
  \cfrac{\alpha ! (\beta-1)!}{(\alpha+(\beta-1)+1)!}
  \\ &=&
  \cfrac{\alpha}{\alpha + \beta}
\end{eqnarray}
$$

## 分散

$$
\begin{eqnarray}
  E(p^2) &=& \int_{0}^{1} p^2 \cfrac{1}{B(\alpha, \beta)} p^{\alpha-1} (1-p)^{\beta-1} dp
  \\ &=&
  \cfrac{1}{B(\alpha, \beta)}
  \int_{0}^{1} p^{\alpha+1} (1-p)^{\beta-1} dp
  \\ &=&
  \cfrac{(\alpha+\beta-1)!}{(\alpha-1)!(\beta-1)!}
  \cfrac{(\alpha+1) ! (\beta-1)!}{((\alpha+1)+(\beta-1)+1)!}
  \\ &=&
  \cfrac{(\alpha+1)\alpha}{(\alpha+\beta+1)(\alpha+\beta)}
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
  V(p) &=& E(p^2) - E(p)^2
  \\ &=&
  \cfrac{(\alpha+1)\alpha}{(\alpha+\beta+1)(\alpha+\beta)}
  - \cfrac{\alpha^2}{(\alpha + \beta)^2}
  \\ &=&
  \cfrac{\alpha \beta}{(\alpha+\beta+1)(\alpha+\beta)^2}
\end{eqnarray}
$$


# ベータ分布の特徴

- 「成功数：失敗数」の比が同じであっても、全試行回数が大きくなるほど、狭い範囲に集中して分布
	- → 試行回数が多いほど、確率の見積もり精度が高まる
![Figure_1](https://user-images.githubusercontent.com/13412823/211961160-cd458953-fabc-466e-a782-e023dee885cc.png)

```python
import numpy as np
import math
from matplotlib import pyplot as plt

def ln_factorial(n):
	"""階乗の log を計算するための補助関数"""
	ret = 0
	for i in range(1, n+1):
		ret += np.log(i)
	return ret

def calc_beta(p, a, b):
	"""
	ベータ分布関数の計算
	計算中のオーバーフローを防ぐため、先に対数を取って計算してから指数を取る
	"""
	ret = np.zeros(p.shape)
	for i in range(len(p)):
		if 0 < p[i] < 1:
			log_beta = (a-1) * np.log(p[i]) + (b-1) * np.log(1-p[i]) + ln_factorial(a+b-1) - ln_factorial(a-1) - ln_factorial(b-1)
			ret[i] = np.exp(log_beta)
	return ret

def plot_beta(a, b):
	plt.title(r'$\alpha = {}, \beta = {}$'.format(a, b))
	# ベータ関数の描画
	p = np.linspace(0, 1, 1000)
	#beta = p**(a-1) * (1-p)**(b-1) / B
	beta = calc_beta(p, a, b)
	plt.plot(p, beta)

plt.figure(figsize=(10, 6))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
cnt_fig = 1
for a_seed, b_seed in [(3, 1), (2, 2), (1, 3)]:
	for i in range(4):
		plt.subplot(3, 4, cnt_fig)
		plot_beta(a_seed * 5**i, b_seed * 5**i)
		cnt_fig += 1

plt.show()
```