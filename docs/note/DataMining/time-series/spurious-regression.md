---
title: 見せかけの回帰
title-en: Spurious Regression
---

# 概要

実際には無関係な2つの時系列データに関して回帰分析を行うとき、これらの時系列が [単位根過程](unit-root-process.md) だった場合、有意な相関が表れてしまう問題を **見せかけの回帰** という。

# 原因

互いに独立な[単位根過程](unit-root-process.md) $r_t, s_t$ を考える。

$$
\begin{eqnarray}
	r_t &=& a + r_{t-1} + \varepsilon_t
	\\
	s_t &=& b + s_{t-1} + \zeta_t
\end{eqnarray}
$$

ここで $a,b$ は定数、$\varepsilon_t, \zeta_t$ は[ホワイトノイズ](white-noise.md)。

この漸化式を過去にさかのぼっていくと、
$$
\begin{eqnarray}
	r_t &=& ta + r_0 + \sum_{k=1}^t \varepsilon_k
	\\
	s_t &=& tb + s_0 + \sum_{k=1}^t \zeta_k
\end{eqnarray}
$$

これら2式より、ホワイトノイズ部分以外の $t$ を消去すると、

$$
a \left( s_t - s_0 - \sum_{k=1}^t \zeta_k \right)
=
b \left( r_t - r_0 - \sum_{k=1}^t \varepsilon_k \right)
$$

両辺の期待値を取れば、

$$
a( E(s_t) - s_0 ) = b( E(r_t) - r_0 )
$$

よって、$E(s_t)$ は $E(r_t)$ の1次関数で表される。

以上により、2つの時系列 $r_t, s_t$ が独立であっても、単位根過程であれば相関関係を示す。

# 回避方法

差分を取って

$$
\begin{eqnarray}
	\Delta r_t &:=& r_t - r_{t-1} &=& a + \varepsilon_t
	\\
	\Delta s_t &:=& s_t - s_{t-1} &=& b + \zeta_t
\end{eqnarray}
$$

で分析すれば良い。


# 実験

独立な単位根過程

$$
\begin{eqnarray}
	r_t &=& 0.3 + r_{t-1} + \mathrm{W.N.}(\sigma^2 = 1.3^2)
	\\
	s_t &=& 0.3 + s_{t-1} + \mathrm{W.N.}(\sigma^2 = 1.1^2)
\end{eqnarray}
$$

の相関を見る。

| 独立な単位根過程 $r_t, s_t$ | $r_t, s_t$ の相関 |
| :--: | :--: |
| ![Figure_1](https://user-images.githubusercontent.com/13412823/246292492-2baf0d47-5744-4336-adba-0107a04aeaa4.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/246293866-06131dcd-952b-487b-bb02-a0ccdd6f6609.png) |

→ 独立な単位根過程であるにも関わらず、高い相関（相関係数 0.91）を示している。

次に差分を取った

$$
\begin{eqnarray}
	\Delta r_t &:=& r_t - r_{t-1} &=& 0.3 + \mathrm{W.N.}(\sigma^2 = 1.3^2)
	\\
	\Delta s_t &:=& s_t - s_{t-1} &=& 0.3 + \mathrm{W.N.}(\sigma^2 = 1.1^2)
\end{eqnarray}
$$

について相関を見る。

| $\Delta r_t, \Delta s_t$ | $\Delta r_t, \Delta s_t$ の相関 |
| :--: | :--: |
| ![Figure_3](https://user-images.githubusercontent.com/13412823/246304493-e9f1631d-75f6-4eb6-96dd-ed5e1fdbb592.png) | ![Figure_4](https://user-images.githubusercontent.com/13412823/246304508-2b475ada-a3ff-48d9-a0df-cd2fb2592234.png) |

→ 見せかけの回帰が観測されなくなった

```python
import numpy as np
from matplotlib import pyplot as plt

def generate(phi0, sigma, n):
	rand = np.random.normal(0, sigma, n)
	tmp = 0
	r = []
	for i in range(n):
		tmp += phi0 + rand[i]
		r.append(tmp)
	return np.array(r)

def plot_graph(x, y, xlabel, ylabel):
	plt.xlabel('Time step', fontsize=14)
	plt.ylabel('Value', fontsize=14)
	plt.plot(range(len(x)), x, label=xlabel)
	plt.plot(range(len(y)), y, label=ylabel)
	plt.legend()
	plt.show()
	plt.title('correlation coefficient = {}'.format(np.corrcoef(x, y)[0,1]))
	plt.xlabel(xlabel, fontsize=14)
	plt.ylabel(ylabel, fontsize=14)
	plt.scatter(x, y)
	plt.show()

# 独立な単位根過程 r, s
r = generate(0.3, 1.3, 100)
s = generate(0.3, 1.1, 100)
plot_graph(r, s, '$r_t$', '$s_t$')

# r, s の差分
dr = r[:-1] - r[1:]
ds = s[:-1] - s[1:]
plot_graph(dr, ds, r'$\Delta r_t$', r'$\Delta s_t$')
```
