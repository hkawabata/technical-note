---
title: 幾何分布
title-en: Geometric Distribution
---

# 幾何分布とは

離散確率分布の1種。  
成功確率 $p$ の試行を連続で行う時、初めて成功するまでの試行回数 $k$ の分布。  
確率密度関数は以下の式で表される。

$$
f_p(k) = (1-p)^{k-1} p
$$

# 幾何分布の期待値・分散

## 準備

$\cfrac{1}{1-x}$ の $n$ 階微分は

$$
\cfrac{d^n}{dx^n} \left( \cfrac{1}{1-x} \right) = (-1)^n \times (-1)(-2)\cdots(-n) \cfrac{1}{(1-x)^{n+1}}
= \cfrac{n!}{(1-x)^{n+1}}
$$

であるから、$\cfrac{1}{1-x}$ をマクローリン展開すると、

$$
\cfrac{1}{1-x} = 1 + x + x^2 + \cdots = \sum_{k=0}^{\infty} x^k
$$

両辺の1階微分・2階微分は

$$
\begin{eqnarray}
	\cfrac{1}{(1-x)^2} &=& \sum_{k=1}^{\infty} k x^{k-1} & (1)
	\\
	\cfrac{2}{(1-x)^3} &=& \sum_{k=2}^{\infty} k(k-1) x^{k-2} & \qquad (2)
\end{eqnarray}
$$

## 期待値

$$
\begin{eqnarray}
	E(k) &=& \sum_{k=1}^{\infty} k (1-p)^{k-1} p
	\\ &=&
	p \sum_{k=1}^{\infty} k (1-p)^{k-1}
\end{eqnarray}
$$

式 $(1)$ に $x = 1-p$ を代入して用いれば、

$$
\begin{eqnarray}
	E(k) &=&
	p \cfrac{1}{(1-(1-p))^2}
	\\ &=&
	\cfrac{1}{p}
\end{eqnarray}
$$

## 分散

$$
\begin{eqnarray}
	E(k^2) &=& \sum_{k=1}^{\infty} k^2 (1-p)^{k-1} p
	\\ &=&
	p \sum_{k=1}^{\infty} (k(k-1)+k) (1-p)^{k-1}
	\\ &=&
	p \left(
		\sum_{k=1}^{\infty} k(k-1) (1-p)^{k-1} +
		\sum_{k=1}^{\infty} k (1-p)^{k-1}
	\right)
	\\ &=&
	p \left(
		(1-p) \sum_{k=2}^{\infty} k(k-1) (1-p)^{k-2} +
		\sum_{k=1}^{\infty} k (1-p)^{k-1}
	\right)
\end{eqnarray}
$$

式 $(1), (2)$ に $x = 1-p$ を代入して用いれば、

$$
\begin{eqnarray}
	E(k^2) &=&
	p \left(
		(1-p) \cfrac{2}{(1-(1-p))^3} +
		\cfrac{1}{(1-(1-p))^2}
	\right)
	\\ &=&
	\cfrac{1-p}{p^2} + \cfrac{1}{p}
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
	V(k) &=& E(k^2) - E(k)^2
	\\ &=&
	\cfrac{1-p}{p^2} + \cfrac{1}{p} - \cfrac{1}{p}
	\\ &=&
	\cfrac{1-p}{p^2}
\end{eqnarray}
$$


## モーメント母関数

$$
\begin{eqnarray}
	M_X(t) &=& E(tX)
	\\ &=&
	\sum_{X=1}^{\infty} e^{tX} (1-p)^{X-1} p
	\\ &=&
	p e^t \sum_{X=1}^{\infty} \left(e^t (1-p) \right)^{X-1}
	\\ &=&
	\cfrac{p e^t}{1 - e^t(1-p)}
\end{eqnarray}
$$

ただし、最後の変形ではモーメント母関数を利用する $t=0$ 近傍、特に

$$
e^t (1-p) \lt 1 \Longleftrightarrow t \lt - \log{(1-p)}
$$

が成り立つ範囲を仮定している。