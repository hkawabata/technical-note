---
title: 二項分布
title-en: Binomial Distribution
---

# 二項分布とは

成功確率 $p$ が分かっている試行を $n$ 回行ったときの「成功回数」の分布。

確率密度関数は以下の式で表される。

$$
\begin{eqnarray}
	f_{p,n}(x)
	&=& {}_n \mathrm{C}_x p^x (1-p)^{n-x}
	\\ &=& \cfrac{n!}{(n-x)!x!} p^x (1-p)^{n-x}
\end{eqnarray}
$$

# 二項分布の期待値・分散

## 期待値

$$
\begin{eqnarray}
  E(x) &=& \displaystyle \sum_{k=0}^{n} k f_{p,n}(k) = \displaystyle \sum_{k=1}^{n} k f_{p,n}(k)
  \\ &=&
  \displaystyle \sum_{k=1}^{n} k \cfrac{n!}{(n-k)!k!} p^k (1-p)^{n-k}
  \\ &=&
  n \displaystyle \sum_{k=1}^{n} \cfrac{(n-1)!}{((n-1)-(k-1))!(k-1)!} p^k (1-p)^{n-k}
  \\ &=&
  np \displaystyle \sum_{k=1}^{n} {}_{n-1} \mathrm{C}_{k-1} p^{k-1} (1-p)^{n-k}
  \\ &=&
  np \displaystyle \sum_{k=0}^{n-1} {}_{n-1} \mathrm{C}_{k} p^{k} (1-p)^{(n-1)-k}
  \\ &=&
  np (p + (1-p))^{n-1}
  \\ &=&
  np
\end{eqnarray}
$$

## 分散

まず $E(x^2)$ を求める。

$$
\begin{eqnarray}
  E(x^2) &=& \displaystyle \sum_{k=0}^{n} k^2 f_{p,n}(k) = \displaystyle \sum_{k=1}^{n} k^2 f_{p,n}(k)
  \\ &=&
  \displaystyle \sum_{k=1}^{n} (k(k-1)+k) \cfrac{n!}{(n-k)!k!} p^k (1-p)^{n-k}
  \\ &=&
  \displaystyle \sum_{k=1}^{n} \cfrac{k(k-1)n!}{(n-k)!k!} p^k (1-p)^{n-k} +
  \displaystyle \sum_{k=1}^{n} \cfrac{n!}{(n-k)!(k-1)!} p^k (1-p)^{n-k}
\end{eqnarray}
$$

$k=1$ のとき $k(k-1)=0$ であるから、第一項は $k=2$ から和を取り始めても良いので、

$$
\begin{eqnarray}
  E(x^2) &=&
  \displaystyle \sum_{k=2}^{n} \cfrac{k(k-1)n!}{(n-k)!k!} p^k (1-p)^{n-k} +
  \displaystyle \sum_{k=1}^{n} \cfrac{n!}{(n-k)!(k-1)!} p^k (1-p)^{n-k}
  \\ &=&
  \displaystyle \sum_{k=2}^{n} \cfrac{n!}{(n-k)!(k-2)!} p^k (1-p)^{n-k} +
  \displaystyle \sum_{k=1}^{n} \cfrac{n!}{(n-k)!(k-1)!} p^k (1-p)^{n-k}
  \\ &=&
  n(n-1)p^2 \displaystyle \sum_{k=0}^{n-2} \cfrac{(n-2)!}{((n-2)-k)!k!} p^k (1-p)^{(n-2)-k} +
  np \displaystyle \sum_{k=0}^{n-1} \cfrac{(n-1)!}{((n-1)-k)!k!} p^k (1-p)^{(n-1)-k}
  \\ &=&
  n(n-1)p^2 (p+(1-p))^{n-2} +
  np (p+(1-p))^{n-1}
  \\ &=&
  n(n-1)p^2 + np
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
  V(x) &=& E(x^2) - E(x)^2
  \\ &=&
  n(n-1)p^2 + np - (np)^2
  \\ &=&
  np(1-p)
\end{eqnarray}
$$

## モーメント母関数

$$
\begin{eqnarray}
	M_X(t) &=& \displaystyle \sum_{k=0}^{n} e^{kt} f_{p,n}(k)
	\\ &=&
	\displaystyle \sum_{k=0}^{n} e^{kt}
	\cfrac{n!}{(n-k)!k!} p^k (1-p)^{n-k}
	\\ &=&
	\displaystyle \sum_{k=0}^{n}
	\cfrac{n!}{(n-k)!k!} (e^t p)^k (1-p)^{n-k}
	\\ &=&
	\displaystyle \sum_{k=0}^{n}
	{}_n \mathrm{C}_k (e^t p)^k (1-p)^{n-k}
	\\ &=&
	(e^t p + 1 - p)^n
\end{eqnarray}
$$


# 二項分布の特徴

![Figure_1](https://user-images.githubusercontent.com/13412823/212012103-71c759ed-4bbd-423b-9260-6011ae86591d.png)

（描画に使った Python コード）
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

def binomial(k, p, n):
	log_binomial = ln_factorial(n) - ln_factorial(n-k) - ln_factorial(k) + k * np.log(p) + (n-k) * np.log(1-p)
	return np.exp(log_binomial)

plt.figure(figsize=(8, 9))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
cnt_fig = 1
for p in [0.01, 0.1, 0.5, 0.9, 0.99]:
	for n in [10, 100, 1000]:
		plt.subplot(5, 3, cnt_fig)
		k = np.array(range(n+1))
		bi = np.zeros(k.shape)
		for i in range(n+1):
			bi[i] = binomial(k[i], p, n)
		plt.title('$p={}, n={}$'.format(p, n))
		plt.plot(k, bi)
		cnt_fig += 1

plt.show()
```