---
title: ポアソン分布
title-en: Poisson Distribution
---

# ポアソン分布とは

単位時間あたりに平均 $\lambda$ 回起こる事象が、ある単位時間に $k$ 回起こる確率 $P(k)$ の分布。

$$
P_\lambda(k) = \cfrac{\lambda^k}{k!} e^{-\lambda}
$$

# 確率密度関数の導出

単位時間を $n$ 等分する。  
$n$ を十分に大きく取れば、$n$ 等分された各区間において、事象が2回以上起こる可能性はゼロと考えて良い。  
そのため、各分割区間を「事象が起こったか起こらなかったか」の試行と捉えることができる。  
$n$ 個の分割区間のうち平均 $\lambda$ 個の区間で事象が発生するから、各区間で事象が発生する確率は $\cfrac{\lambda}{n}$

したがって、$n$ 個の分割区間においてこの事象が $k$ 回起こる確率は、事象発生確率 $\cfrac{\lambda}{n}$ の試行を $n$ 回行って事象が $k$ 回発生する確率であるから、二項分布

$$
P(k) = {}_n \mathrm{C}_k \left( \cfrac{\lambda}{n} \right)^k \left( 1-\cfrac{\lambda}{n} \right)^{n-k}
$$

に従う。分割区間の大きさを無限に小さく（分割数を無限に大きく）すれば、

$$
\begin{eqnarray}
	\lim_{n \to \infty} P(k)
	&=&
	\lim_{n \to \infty}
	{}_n \mathrm{C}_k
	\left( \cfrac{\lambda}{n} \right)^k
	\left( 1-\cfrac{\lambda}{n} \right)^{n-k}
	\\ &=&
	\lim_{n \to \infty}
	\cfrac{n(n-1)(n-2) \cdots (n-k+1)}{k!} \cfrac{\lambda^k}{n^k}
	\left( 1-\cfrac{\lambda}{n} \right)^n
	\left( 1-\cfrac{\lambda}{n} \right)^{-k}
	\\ &=&
	\cfrac{\lambda^k}{k!}
	\lim_{n \to \infty}
	\cfrac{n(n-1)(n-2) \cdots (n-k+1)}{n^k}
	\left( 1-\cfrac{\lambda}{n} \right)^n
	\left( 1-\cfrac{\lambda}{n} \right)^{-k}
	\\ &=&
	\cfrac{\lambda^k}{k!}
	\lim_{n \to \infty}
	\left(
		\displaystyle \prod_{i=0}^{k-1} \left( 1 - \cfrac{i}{n} \right)
	\right)
	\left( 1-\cfrac{\lambda}{n} \right)^n
	\left( 1-\cfrac{\lambda}{n} \right)^{-k}
	\\ &=&
	\cfrac{\lambda^k}{k!}
	\left(
		\displaystyle \prod_{i=0}^{k-1} \left( 1 - 0 \right)
	\right)
	e^{-\lambda}
	\left( 1-0 \right)^{-k}
	\\ &=&
	\cfrac{\lambda^k}{k!} e^{-\lambda}
\end{eqnarray}
$$

となり、ポアソン分布の確率密度関数を得る。

# ポアソン分布の期待値・分散

## 期待値

$$
\begin{eqnarray}
	E(k) &=& \displaystyle \sum_{k=0}^{\infty} k P_\lambda(k) =
	\displaystyle \sum_{k=1}^{\infty} k P_\lambda(k)
	\\ &=&
	\displaystyle \sum_{k=1}^{\infty}
	\cfrac{\lambda^k}{(k-1)!} e^{-\lambda}
	\\ &=&
	\lambda \displaystyle \sum_{k'=0}^{\infty}
	\cfrac{\lambda^{k'}}{k'!} e^{-\lambda}
	\\ &=&
	\lambda \displaystyle \sum_{k'=0}^{\infty}
	P_\lambda(k')
\end{eqnarray}
$$

途中の変形で、$k - 1 = k'$ による置き換えを行った。
この式の和を取る部分は、ポワソン分布の確率密度関数の総和であるから1になる。
したがって、

$$
E(k) = \lambda
$$

## 分散

$$
\begin{eqnarray}
	E(k^2) &=& \displaystyle \sum_{k=0}^{\infty} k^2 P_\lambda(k) =
	\displaystyle \sum_{k=1}^{\infty} k^2 P_\lambda(k)
	\\ &=&
	\displaystyle \sum_{k=1}^{\infty} (k(k-1) + k) P_\lambda(k)
	\\ &=&
	\displaystyle \sum_{k=1}^{\infty} k(k-1) P_\lambda(k) +
	\displaystyle \sum_{k=1}^{\infty} k P_\lambda(k)
	\\ &=&
	\displaystyle \sum_{k=2}^{\infty} k(k-1) P_\lambda(k) +
	\displaystyle \sum_{k=1}^{\infty} k P_\lambda(k)
	\\ &=&
	\displaystyle \sum_{k=2}^{\infty} \cfrac{\lambda^k}{(k-2)!} e^{-\lambda} +
	\displaystyle \sum_{k=1}^{\infty} \cfrac{\lambda^k}{(k-1)!} e^{-\lambda}
	\\ &=&
	\lambda^2 \displaystyle \sum_{k'=0}^{\infty} \cfrac{\lambda^{k'}}{k'!} e^{-\lambda} +
	\lambda \displaystyle \sum_{k''=0}^{\infty} \cfrac{\lambda^{k''}}{k''!} e^{-\lambda}
	\\ &=&
	\lambda^2 \displaystyle \sum_{k'=0}^{\infty} P_\lambda(k') +
	\lambda \displaystyle \sum_{k''=0}^{\infty} P_\lambda(k'')
	\\ &=&
	\lambda^2 + \lambda
\end{eqnarray}
$$

したがって、

$$
\begin{eqnarray}
	V(k) &=& E(k^2) - E(k)^2
	\\ &=&
	(\lambda^2 + \lambda) - \lambda^2
	\\ &=&
	\lambda
\end{eqnarray}
$$

## モーメント母関数

$$
\begin{eqnarray}
	M_X(t) &=& E(e^{tX})
	\\ &=&
	\displaystyle \sum_{X=0}^{\infty}
	e^{tX} P_\lambda(X)
	\\ &=&
	\displaystyle \sum_{X=0}^{\infty}
	e^{tX} \cfrac{\lambda^X}{X!} e^{-\lambda}
	\\ &=&
	e^{-\lambda} \displaystyle \sum_{X=0}^{\infty}
	\cfrac{(\lambda e^t)^X}{X!}
\end{eqnarray}
$$

指数関数のマクローリン展開の式

$$
e^x = \displaystyle \sum_{k=0}^{\infty} \cfrac{x^k}{k!}
$$

より、

$$
\begin{eqnarray}
	M_X(t) &=&
	e^{-\lambda} e^{\lambda e^t}
	\\ &=&
	e^{\lambda (e^t - 1)}
\end{eqnarray}
$$


# ポアソン分布の特徴

![Figure_1](https://user-images.githubusercontent.com/13412823/212444395-f678b225-1caf-467a-b001-09b5884f93d1.png)
$\lambda$ が大きいほど、分布は平均値付近に集中する：
![Figure_2](https://user-images.githubusercontent.com/13412823/212444401-814855e9-f922-44bd-ba08-6aeebc413729.png)

（描画に使った Python コード）
```python
import numpy as np
import math
from matplotlib import pyplot as plt

def plot_poisson(k_max, lamb, legend=False):
	k = np.array(range(k_max+1))
	# 階乗の計算
	ln_factorial = [0]
	for i in range(1, k_max+1):
		ln_factorial.append(ln_factorial[-1] + np.log(i))
	ln_factorial = np.array(ln_factorial)
	# kのlamb乗の計算
	ln_k_pow = k * np.log(lamb)
	# 確率密度の計算
	poisson = np.exp(ln_k_pow - ln_factorial - lamb)
	# グラフ描画
	plt.plot(k, poisson, marker='.', label=r'$\lambda = {}$'.format(lamb))
	plt.grid()
	plt.legend()


for lamb in [1, 2, 3, 5, 10, 20]:
	plot_poisson(k_max=30, lamb=lamb)

plt.xlabel('$k$')
plt.ylabel(r'$P_\lambda(k)$')
plt.grid()
plt.show()


plt.figure(figsize=(12, 3))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
cnt_plot = 1
for lamb in [4, 16, 64]:
	plt.subplot(1, 3, cnt_plot)
	plot_poisson(k_max=lamb*2, lamb=lamb)
	cnt_plot += 1

plt.show()
```

# 利用例

## 交通事故が1日平均2回起こる地域で、2日間にちょうど6回の事故が起こる確率

単位時間を2日に設定する。  
2日で事故が起こる回数の平均値は4なので、$\lambda=4$ のポアソン分布で $k=6$ である確率を求めれば良い。

$$
P_{\lambda=4}(k=6) = \cfrac{4^6}{6!} e^{-4} = 0.1042
$$

求める確率は 10.42%

## 交通事故が1日平均2回起こる地域で、2日間に6回以上事故が起こる確率

0〜5回事故が起こる確率を求めて余事象の確率を取れば良い。

$$
\begin{eqnarray}
	1 - \sum_{k=0}^{5}
	P_{\lambda=4}(k)
	&=&
	1 - e^{-4} \left( \cfrac{4^0}{0!} + \cfrac{4^1}{1!} + \cfrac{4^2}{2!} + \cfrac{4^3}{3!} + \cfrac{4^4}{4!} + \cfrac{4^5}{5!}\right)
	\\ &=&
	1 - 0.7851 = 0.2149
\end{eqnarray}
$$

求める確率は 21.49%

## 1%の割合で不良品ができる工場で、10個の製品を抽出したとき不良品が2個以上混ざる確率

10個の製品を抽出する場合の不良品個数の期待値は $0.01 \times 10 = 0.1$ 個なので、$\lambda=0.1$ のポアソン分布で不良品が2個以上（$k \ge 2$）である確率を求めれば良い。  
これは $k=0,1$ の余事象であるから、

$$
\begin{eqnarray}
	1 - \sum_{k=0}^{1} P_{\lambda=0.1}(k)
	&=&
	1 - e^{-0.1} \left( \cfrac{0.1^0}{0!} + \cfrac{0.1^1}{1!} \right)
	\\ &=&
	1 - 0.9953 = 0.0047
\end{eqnarray}
$$

よって求める確率は 0.47%

→ これは非常に起こりにくい確率なので、「不良品率が1%」という前提が間違っていた可能性が高い（「不良品率1%以下」を帰無仮説とする仮説検定）。
