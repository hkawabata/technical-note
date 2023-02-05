---
title: 畳み込み積分
title-en: Convolution
---

# 畳み込み積分とは

2つの関数 $f(x), g(x)$ から以下のようにして**合成積** $h(x)$ を作る操作。

$$
h(x) = \int_{-\infty}^{\infty} f(t) g(x-t) dt
$$

$h(x)$ は $f*g (x)$ などのようにも書かれる。

**引数の和が一定（$x$）となるような全ての組み合わせを掛けて足し合わせている。**

# 畳み込み積分の意味

- $f(t)$：時刻 $t$ に発生した信号（音声など）の強度
- $g(t)$：信号が発生してから時間 $t$ が経過してから観測されるときの、信号の減衰率

のように捉えると、過去の時刻 $t$ に発生した信号が現在時刻 $x$ に観測されたときの強度は $f(t)g(x-t)$ で表される。  
これを時間 $t$ で積分した

$$
h(x) = \int_{-\infty}^\infty f(t)g(x-t) dt
$$

は「あらゆる時刻に発生した信号の重ね合わせが現在時刻 $x$ でどう観測されるか」を表している。

> 【NOTE】
> この例の場合、未来に発生した信号は現在時刻では観測されないので、$x \lt t$ のとき
>
> $$g(x-t) = 0$$
>
> よって
> 
> $$h(x) = \int_{-\infty}^x f(t)g(x-t) dt$$


# 畳み込み積分の特徴

## 交換

$$
f * g = g * f
$$

証明：

$$
\begin{eqnarray}
	f * g (x) &=&
	\int_{-\infty}^{\infty} f(t) g(x-t) dt
	\\ &=&
	\int_{\infty}^{-\infty} f(x-u) g(u) (-du) \qquad (x-t=u)
	\\ &=&
	\int_{-\infty}^{\infty} f(x-u) g(u) du
	\\ &=&
	g * f (x)
\end{eqnarray}
$$

## フーリエ変換

関数 $f$ のフーリエ変換を $F[f]$ で表すと、$C$ をフーリエ変換の定数（流儀によって値は異なる）として

$$
F[f * g] = \cfrac{1}{C} F[f] F[g]
$$

証明：

$$
\begin{eqnarray}
	F[f*g] &=&
	C \int_{-\infty}^{\infty} \left(
		\int_{-\infty}^{\infty} f(t) g(x-t) dt
	\right) e^{-ikx} dx
	\\ &=&
	\int_{-\infty}^{\infty} f(t) e^{-ikt} \left(
		C \int_{-\infty}^{\infty} g(x-t) e^{-ik(x-t)} dx
	\right) dt
	\\ &=&
	\int_{-\infty}^{\infty} f(t) e^{-ikt} \left(
		C \int_{-\infty}^{\infty} g(u) e^{-iku} du
	\right) dt
	\qquad (x-t = u)
	\\ &=&
	\cfrac{1}{C}
	\left( C \int_{-\infty}^{\infty} f(t) e^{-ikt} dt \right)
	\left( C \int_{-\infty}^{\infty} g(u) e^{-iku} du \right)
	\\ &=&
	\cfrac{1}{C} F[f] F[g]
\end{eqnarray}
$$