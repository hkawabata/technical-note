---
title: F 分布
title-en: F-distribution
---

# F 分布とは

## 定義

自由度 $k_1, k_2$ のカイ二乗分布に従う確率変数 $\chi_1^2, \chi_2^2$ が独立である時、以下の式で定義されつ統計量 $F$ が従う確率分布を **F 分布** といい、$F(k_1, k_2)$ で表す。

$$
F := \cfrac{\chi_1^2/k_1}{\chi_2^2/k_2}
\tag{1}
$$

## F 分布の利用

- **F 検定**：[等分散性の検定](../hypothesis-testing/testing-for-the-variance.md)


# 確率密度関数

$$
f_F(x:k_1,k_2) = \cfrac{
	\Gamma \left( \cfrac{k_1+k_2}{2} \right)
}{
	\Gamma \left( \cfrac{k_1}{2} \right)
	\Gamma \left( \cfrac{k_2}{2} \right)
}
\left(
	\cfrac{k_1 x}{k_1 x + k_2}
\right)^{k_1/2}
\left(
	1 - \cfrac{k_1 x}{k_1 x + k_2}
\right)^{k_2/2}
\cfrac{1}{x}
\tag{2}
$$

ここで、$\Gamma$ は[ガンマ関数](../../special-functions/gamma-function.md)

![Figure_1](https://user-images.githubusercontent.com/13412823/221330832-6aa5b07b-4332-496b-b7f8-d625b7b8d004.png)


```python
import numpy as np
from matplotlib import pyplot as plt
import math

def f(x, k1, k2):
	"""F 分布の確率密度関数"""
	g = math.gamma((k1+k2)/2.0) / math.gamma(k1/2.0) / math.gamma(k2/2.0)
	k1x = k1 * x
	tmp = k1x / (k1x+k2)
	return g * tmp**(k1/2) * (1-tmp)**(k2/2) / x

x = np.linspace(1e-10,5,1000)

for k1, k2 in [(1, 3), (3, 1), (2, 3), (3, 3), (5, 3), (20, 3), (3, 10), (10, 10)]:
	y = f(x, k1, k2)
	plt.plot(x, y, label='$k_1 = {}, k_2 = {}$'.format(k1, k2))

plt.ylim([-0.1, 1.1])
plt.legend()
plt.grid()
plt.show()
```


# F 分布の期待値・分散

## 期待値

$$
\begin{eqnarray}
	E(x) &=& \int_0^\infty x f_F(x:k_1,k_2) dx
	\\ &=&
	C \int_0^\infty
	\left(
		\cfrac{k_1 x}{k_1 x + k_2}
	\right)^{k_1/2}
	\left(
		1 - \cfrac{k_1 x}{k_1 x + k_2}
	\right)^{k_2/2}
	dx
	\qquad
	\left(
	C = \cfrac{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
		\Gamma \left( \cfrac{k_2}{2} \right)
	}\right)
	\\ &=&
	C \int_0^1
	t^{k_1/2} (1 - t)^{k_2/2}
	\left( \cfrac{k_2}{k_1} \cfrac{dt}{(1-t)^2} \right)
	\qquad \left( t = \cfrac{k_1 x}{k_1 x + k_2} \right)
	\\ &=&
	C \cfrac{k_2}{k_1}
	\int_0^1
		t^{k_1/2} (1 - t)^{k_2/2-2}
	dt
	\\ &=&
	C \cfrac{k_2}{k_1} B \left( \cfrac{k_1}{2}+1, \cfrac{k_2}{2}-1 \right)
	\\ &=&
	C \cfrac{k_2}{k_1}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+1 \right)
		\Gamma \left( \cfrac{k_2}{2}-1 \right)
	}{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}
	\\ &=&
	\cfrac{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
		\Gamma \left( \cfrac{k_2}{2} \right)
	}
	\cfrac{k_2}{k_1}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+1 \right)
		\Gamma \left( \cfrac{k_2}{2}-1 \right)
	}{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}
	\\ &=&
	\cfrac{k_2}{k_1}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+1 \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
	}
	\cfrac{
		\Gamma \left( \cfrac{k_2}{2}-1 \right)
	}{
		\Gamma \left( \cfrac{k_2}{2} \right)
	}
	\\ &=&
	\cfrac{k_2}{k_1}
	\cfrac{k_1/2}{1}
	\cfrac{1}{k_2/2-1}
	\\ &=&
	\cfrac{k_2}{k_2-2}
\end{eqnarray}
$$

$B$ は[ベータ関数](../../special-functions/beta-function.md)であり、式変形の途中、ベータ関数とガンマ関数の関係式を用いた。


## 分散

$$
\begin{eqnarray}
	E(x^2) &=& \int_0^\infty x^2 f_F(x:k_1,k_2) dx
	\\ &=&
	C \int_0^\infty
	x \left(
		\cfrac{k_1 x}{k_1 x + k_2}
	\right)^{k_1/2}
	\left(
		1 - \cfrac{k_1 x}{k_1 x + k_2}
	\right)^{k_2/2}
	dx
	\qquad
	\left(
	C = \cfrac{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
		\Gamma \left( \cfrac{k_2}{2} \right)
	}\right)
	\\ &=&
	C \int_0^1
	\left( \cfrac{k_2}{k_1} \cfrac{t}{1-t} \right)
	t^{k_1/2} (1 - t)^{k_2/2}
	\left( \cfrac{k_2}{k_1} \cfrac{dt}{(1-t)^2} \right)
	\qquad \left( t = \cfrac{k_1 x}{k_1 x + k_2} \right)
	\\ &=&
	C \cfrac{k_2^2}{k_1^2}
	\int_0^1
		t^{k_1/2+1} (1 - t)^{k_2/2-3}
	dt
	\\ &=&
	C \cfrac{k_2^2}{k_1^2} B \left( \cfrac{k_1}{2}+2, \cfrac{k_2}{2}-2 \right)
	\\ &=&
	C \cfrac{k_2^2}{k_1^2}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+2 \right)
		\Gamma \left( \cfrac{k_2}{2}-2 \right)
	}{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}
	\\ &=&
	\cfrac{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
		\Gamma \left( \cfrac{k_2}{2} \right)
	}
	\cfrac{k_2^2}{k_1^2}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+2 \right)
		\Gamma \left( \cfrac{k_2}{2}-2 \right)
	}{
		\Gamma \left( \cfrac{k_1+k_2}{2} \right)
	}
	\\ &=&
	\cfrac{k_2^2}{k_1^2}
	\cfrac{
		\Gamma \left( \cfrac{k_1}{2}+2 \right)
	}{
		\Gamma \left( \cfrac{k_1}{2} \right)
	}
	\cfrac{
		\Gamma \left( \cfrac{k_2}{2}-2 \right)
	}{
		\Gamma \left( \cfrac{k_2}{2} \right)
	}
	\\ &=&
	\cfrac{k_2^2}{k_1^2}
	\cfrac{
		\left(\cfrac{k_1}{2} + 1\right)
		\cfrac{k_1}{2}
	}{1}
	\cfrac{1}{
		\left(\cfrac{k_2}{2} - 1\right)
		\left(\cfrac{k_2}{2} - 2\right)
	}
	\\ &=&
	\cfrac{k_2^2(k_1+2)}{k_1(k_2-2)(k_2-4)}
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
	V(x) &=& E(x^2) - E(x)^2
	\\ &=&
	\cfrac{k_2^2(k_1+2)}{k_1(k_2-2)(k_2-4)}
	-
	\left( \cfrac{k_2}{k_2-2} \right)^2
	\\ &=&
	\cfrac{2k_2^2(k_1+k_2-2)}{k_1(k_2-2)^2(k_2-4)}
\end{eqnarray}
$$


# F 分布の性質

## t 分布との関係

> **【定理】**
> 
> 確率変数 $t$ が自由度 $n$ の t 分布 $t(n)$ に従う時、
> 
> $$
t^2 \sim F(1, n)
$$

**【証明】**

$t(n)$ に従う確率変数 $t$ は

- 標準正規分布 $N(0, 1)$ に従う確率変数 $Z$
- 自由度 $n$ のカイ二乗分布 $\chi^2(n)$ に従う確率変数 $\chi^2$

を用いて

$$
t = \cfrac{Z}{\sqrt{\chi^2/n}}
$$

と表せるので、

$$
t^2 = \cfrac{Z^2}{\chi^2/n}
$$

$Z \sim N(0, 1)$ より $Z^2 \sim \chi^2(1)$、仮定より $\chi^2 \sim \chi^2(n)$ であるから、

$$
t^2 = \cfrac{Z^2/1}{\chi^2/n} \sim F(1, n)
$$



## 逆数の F 分布

> **【定理】**
> 
> 確率変数 $F$ について、
> 
> $$
F \sim F(k_1, k_2)\ \Longleftrightarrow\ \cfrac{1}{F} \sim F(k_2, k_1)
$$

**【証明】**

（ToDo）

