---
title: 正規分布
title-en: Normal Distribution
---

# 正規分布とは

期待値を $\mu$、分散を $\sigma^2$ として、確率密度関数が以下の式で与えられる分布。  
$N(\mu, \sigma^2)$ で表す。

$$
f(x) = \cfrac{1}{\sqrt{2\pi}\sigma} \exp{\left( - \cfrac{(x-\mu)^2}{2\sigma^2} \right)}
$$

工業製品の規格誤差や人間の体重など、自然に生じる誤差や個体差は、正規分布になることが多い。


# 標準正規分布

期待値を $\mu$、分散を $\sigma^2$ の正規分布に従う確率変数 $x$ について、$x$ を標準化した

$$
z := \cfrac{x-\mu}{\sigma}
$$

は、**標準正規分布** $N(0, 1)$：期待値 $0$、分散 $1$ の正規分布にしたがう。  
これは後述の「和の再生成」「積の再生成」の性質から証明できる。


# 正規分布の性質

## 中心極限定理

推定や検定で利用する、統計学上非常に重要な定理。  
[中心極限定理](../central-limit-theorem.md)を参照。

## 和の再生性

> **【定理】** 互いに独立な確率変数 $X, Y$ について
> 
> $$
\begin{eqnarray}
	X &\sim& N(\mu_x, \sigma_x^2) \\
	Y &\sim& N(\mu_y, \sigma_y^2)
\end{eqnarray}
$$
> 
> が成り立つとき、$Z := X+Y$ について
> 
> $$
Z \sim N(\mu_x + \mu_y, \sigma_x^2 + \sigma_y^2)
$$
> 
> が成り立つ。

**【証明】**

独立な確率変数の和の確率密度関数は、それぞれの変数の密度関数の畳込みで与えられる（[参考](../sum-of-independent-random-variable.md)）ので、$X, Y, Z$ の確率密度関数をそれぞれ $f_X, f_Y, f_Z$ とすると、

$$
\begin{eqnarray}
	f_Z (z) &=& \int_{-\infty}^\infty f_X (t) f_Y (z-t) dt
	\\ &=&
	\int_{-\infty}^\infty
		\cfrac{1}{\sqrt{2\pi}\sigma_x}
		\exp{\left( -\cfrac{(t-\mu_x)^2}{2\sigma_x^2} \right)}
		\cfrac{1}{\sqrt{2\pi}\sigma_y}
		\exp{\left( -\cfrac{(z-t-\mu_y)^2}{2\sigma_y^2} \right)}
	dt
	\\ &=&
	\cfrac{1}{2 \pi \sigma_x \sigma_y}
	\int_{-\infty}^\infty
		\exp{\left(
			-\cfrac{(t-\mu_x)^2}{2\sigma_x^2}
			-\cfrac{(z-t-\mu_y)^2}{2\sigma_y^2}
		\right)}
	dt
	\\ &=&
	\cfrac{1}{2 \pi \sigma_x \sigma_y}
	\int_{-\infty}^\infty
		\exp{\left(
			-\cfrac{\sigma_x^2 + \sigma_y^2}{2\sigma_x^2 \sigma_y^2}(t+C)^2
			- \cfrac{(z-(\mu_x + \mu_y))^2}{2(\sigma_x^2 + \sigma_y^2)}
		\right)}
	dt
	\qquad \left( C = \cfrac{-z\sigma_x^2+\mu_y \sigma_x^2-\mu_x \sigma_y^2}{\sigma_x^2+\sigma_y^2} \right)
	\\ &=&
	\cfrac{1}{2 \pi \sigma_x \sigma_y}
	\exp{\left(
		- \cfrac{(z-(\mu_x + \mu_y))^2}{2(\sigma_x^2 + \sigma_y^2)}
	\right)}
	\int_{-\infty}^\infty
		\exp{\left(
			-\cfrac{\sigma_x^2 + \sigma_y^2}{2\sigma_x^2 \sigma_y^2}(t+C)^2
		\right)}
	dt
	\\ &=&
	\cfrac{1}{2 \pi \sigma_x \sigma_y}
	\exp{\left(
		- \cfrac{(z-(\mu_x + \mu_y))^2}{2(\sigma_x^2 + \sigma_y^2)}
	\right)}
	\sqrt{\cfrac{2 \pi \sigma_x^2 \sigma_y^2}{\sigma_x^2 + \sigma_y^2}}
	\\ &=&
	\cfrac{1}{\sqrt{2 \pi (\sigma_x^2 + \sigma_y^2)}}
	\exp{\left(
		- \cfrac{(z-(\mu_x + \mu_y))^2}{2(\sigma_x^2 + \sigma_y^2)}
	\right)}
\end{eqnarray}
$$

これは平均 $\mu_x + \mu_y$、分散 $\sigma_x^2 + \sigma_y^2$ の正規分布の確率密度関数。

※ 途中、ガウス積分の公式

$$
\int_{-\infty}^\infty e^{-a(x+C)^2} dx = \sqrt{\cfrac{\pi}{a}}
$$

を用いた。


## 積の再生性

> **【定理】** 確率変数 $X$ について
> 
> $$
X \sim N(\mu, \sigma^2)
$$
> 
> が成り立つとき、$Z := aX$ について
> 
> $$
Z \sim N(a\mu, a^2 \sigma^2)
$$
> 
> が成り立つ。

**【証明】**

$$
\begin{eqnarray}
	f_X (x) dx &=& \cfrac{1}{\sqrt{2\pi}\sigma}
		\exp{\left( -\cfrac{(x-\mu)^2}{2\sigma^2} \right)}
	dx
	\\ &=&
	\cfrac{1}{\sqrt{2\pi}\sigma}
		\exp{\left( -\cfrac{(z/a-\mu)^2}{2\sigma^2} \right)}
	\left( \cfrac{1}{a} dz \right)
	\qquad (z = ax)
	\\ &=&
	\cfrac{1}{\sqrt{2\pi} a \sigma}
		\exp{\left( -\cfrac{(z-a\mu)^2}{2a^2\sigma^2} \right)}
	dz
\end{eqnarray}
$$

よって、$Z$ の確率密度関数 $f_Z$ は

$$
f_Z(z) =
\cfrac{1}{\sqrt{2\pi} a \sigma}
\exp{\left( -\cfrac{(z-a\mu)^2}{2a^2\sigma^2} \right)}
$$

これは平均 $a\mu$ 分散 $a^2\sigma^2$ の正規分布であるから、

$$
Z \sim N(a\mu, a^2 \sigma^2)
$$