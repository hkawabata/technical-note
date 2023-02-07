---
title: 中心極限定理
title-en: Central Limit Theorem
---

# 定理

$n$ 個の確率変数 $X_1, \cdots, X_n$ が

- **互いに独立している**
- **平均 $\mu$、分散 $\sigma^2$ の同一の確率分布（正規分布でなくて良い）に従う**

とき、これらの平均

$$
\bar{X} = X_1 + \cdots + X_n = \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} X_n
$$

を新しい確率変数とみなすと、$n$ を無限大に発散させたとき、$\bar{X}$ の確率分布は平均 $\mu$、分散 $\cfrac{\sigma^2}{n}$ の正規分布に収束する。

言い換えると、**標本数 $n$ が十分に大きい場合、母集団の分布がどんな形であっても、標本平均 $\bar{X}$ の分布は正規分布へと近づいていく**。


# 証明

## 平均・分散の証明

$\bar{X}$ の平均 $E(\bar{X}) = \mu$、分散 $V(\bar{X}) = \cfrac{\sigma^2}{n}$ であることは、一般的な期待値と分散の性質

$$E(aX) = aE(X)$$

$$E(X+Y) = E(X) + E(Y)$$

$$V(aX) = a^2 V(X)$$

$$V(X+Y) = V(X) + V(Y) + 2 \mathrm{Cov}(X, Y)$$

（ここで $\mathrm{Cov}$ は共分散であり、$X,Y$ が互いに独立ならゼロ）

を用いて、以下のように計算して示せる。

$$
\begin{eqnarray}
  E(\bar{X}) &=& E \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} E(X_i) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} \mu \\
  &=& \cfrac{1}{n} n\mu = \mu
\end{eqnarray}
$$

$$
\begin{eqnarray}
  V(\bar{X}) &=& V \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} V(X_i) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} \sigma^2 \\
  &=& \cfrac{1}{n^2} n \sigma^2 = \cfrac{\sigma^2}{n}
\end{eqnarray}
$$

## 正規分布に従うことの証明

$\bar{X}$ が正規分布に従う $\Longleftrightarrow$ $\bar{X}$ を標準化した確率変数 $Z$ が標準正規分布に従う

なので、$n \rightarrow \infty$ のときに $Z$ が標準正規分布に従うことを証明すれば良い。  
それには、[モーメント母関数](moment-generating-function.md)（積率母関数）が標準正規分布のものに収束することを示せば十分。

前節で計算した平均値と分散の値を用いて $\bar{X}$ を標準化すると、

$$
\begin{eqnarray}
  Z &\equiv& \cfrac{\bar{X}-\mu}{\sigma / \sqrt{n}}
  \\ &=&
  \cfrac{\sqrt{n}}{\sigma} \left(
    \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} X_i - \mu
  \right)
  \\ &=&
  \cfrac{1}{\sigma \sqrt{n}} \left(
    \displaystyle \sum_{i=1}^{n} X_i - n \mu
  \right)
  \\ &=&
  \cfrac{1}{\sigma \sqrt{n}} \left(
    \displaystyle \sum_{i=1}^{n} (X_i - \mu)
  \right)
\end{eqnarray}
$$

ここで $X_i$ を標準化した確率変数

$$
Z_i \equiv \cfrac{X_i-\mu}{\sigma}
$$

を導入すれば、

$$
Z = \cfrac{1}{\sqrt{n}} \displaystyle \sum_{i=1}^{n}Z_i
$$

$Z$ のモーメント母関数は

$$
\begin{eqnarray}
  M_Z(t) &=& E \left( \exp{(tZ)} \right)
  \\ &=&
  E \left(
    \exp{ \left(
      \cfrac{t}{\sqrt{n}} \displaystyle \sum_{i=1}^{n}Z_i
    \right) }
  \right)
  \\ &=&
  E \left(
    \displaystyle \prod_{i=1}^{n} \exp{ \left( \cfrac{t}{\sqrt{n}} Z_i \right) }
  \right)
  \\ &=&
  \displaystyle \prod_{i=1}^{n} E \left(
    \exp{ \left( \cfrac{t}{\sqrt{n}} Z_i \right) }
  \right)
  \\ &=&
  \displaystyle \prod_{i=1}^{n} M_{Z_i} \left (\cfrac{t}{\sqrt{n}} \right)
\end{eqnarray}
$$

よって、$Z$ のモーメント母関数は各変数 $Z_1, \cdots, Z_n$ のモーメント母関数の積で表現できる。

$Z_1, \cdots, Z_n$ は全て同じ確率分布に従うから、モーメント母関数も等しく、

$$
M_Z(t) = \left( M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right) \right)^n
$$

となる（$k$ は 1〜$n$ のどれでも良い）。

$M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)$ をマクローリン展開すると、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
M_{X_k}(0) +
\cfrac{M'_{Z_k}(0)}{1!}\left(\cfrac{t}{\sqrt{n}}\right) +
\cfrac{M''_{Z_k}(0)}{2!}\left(\cfrac{t}{\sqrt{n}}\right)^2 +
\cfrac{M'''_{Z_k}(0)}{3!}\left(\cfrac{t}{\sqrt{n}}\right)^3 + \cdots
$$

ここで、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
\int_{-\infty}^{\infty} \exp{\left(\cfrac{tZ_k}{\sqrt{n}}\right)} f(Z_k) dZ_k
$$

であるから、

$$
M_{Z_k}(0) = \int_{-\infty}^{\infty} f(Z_k) dZ_k = 1
$$

（任意の確率密度関数の全区間積分は1）

また、$Z_k$ は標準化されており、モーメント母関数の性質と分散・期待値の公式から、

$$
M'_{Z_k}(0) = E(Z_k) = 0
$$

$$
M''_{Z_k}(0) = E(Z^2_k) = V(Z_k) - E(Z_k)^2 = 1-0^2=1
$$

これらをマクローリン展開の式に代入し、$\cfrac{t}{\sqrt{n}}$ の3次以上の式を $O((t/\sqrt{n})^3)$ でまとめて表すと、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
1 + \cfrac{t^2}{2n} + O ((t/\sqrt{n})^3)
$$

これを $M_\bar{X}(t)$ の式に代入すれば、

$$
\begin{eqnarray}
  M_Z(t) &=& \left( M_{Z_k} \left( \cfrac{t}{\sqrt{n}} \right) \right)^n
  \\ &=&
  \left(
    1 + \cfrac{t^2}{2n} + O ((t/\sqrt{n})^3)
  \right)^n
  \\ &\longrightarrow&
  \exp{\left( \cfrac{t^2}{2} \right)} \qquad (n \rightarrow \infty)
\end{eqnarray}
$$

最後の式は標準正規分布のモーメント母関数に一致する（証明終了）。


# 実験

1. 色々な確率分布から標本を繰り返し抽出して、標本平均の度数分布表を描く。
2. 標本数 $n$ を大きくしていき、中心極限定理が成り立つ（= 標本数 $n$ が大きいほど標本平均の分布が正規分布に近づく）ことを確認する。

## 一様分布

![UniformDist](https://user-images.githubusercontent.com/13412823/217136511-31c44e33-40d6-4810-870b-0e0309687f8e.png)

## ベータ分布

$\alpha = 9, \beta = 3$ の場合：

![BetaDist-1](https://user-images.githubusercontent.com/13412823/217136508-12073e04-247e-4ad9-96d5-9f6180e222a8.png)


$\alpha = 2, \beta = 2$ の場合：

![BetaDist-2](https://user-images.githubusercontent.com/13412823/217136503-6053bcfc-4554-4a0e-b74a-0b16455a7df3.png)


## カイ二乗分布

自由度 $k = 2$ の場合：

![ChiSquaredDist-1](https://user-images.githubusercontent.com/13412823/217136500-46baac95-22d0-4beb-b578-3f3073452a94.png)

自由度 $k = 5$ の場合：

![ChiSquaredDist-2](https://user-images.githubusercontent.com/13412823/217136495-42b11187-8fcb-46a5-ac64-8b1c1356742f.png)


## 一次関数に従う分布

![LinearDist](https://user-images.githubusercontent.com/13412823/217136488-4d19c0bb-fb9e-4b91-8333-f716013d83cc.png)

ここでは、$0 \le x \le a$ の範囲で一次関数型の分布に従う母集団を考え、$a=1$ を代入した。

確率密度関数 $f(x)$ の全区間積分（直角三角形の面積）は1になる必要があるので、三角形の高さ（$x=a$ における $f(x)$ の値）は $\cfrac{2}{a}$

したがって、この確率密度関数（直角三角形の斜辺）の傾きは $\cfrac{2}{a^2}$ となるから、

$$
f(x) = \begin{cases}
	\cfrac{2}{a^2} x & \qquad & (0 \le x \le a) \\
	0 & \qquad & (x \lt 0, a \lt x)
\end{cases}
$$

母集団の期待値 $\mu$ は

$$
\begin{eqnarray}
	\mu &=& E(x) = \int_0^a x f(x) dx
	\\ &=&
	\cfrac{2}{a^2} \int_0^a x^2 dx
	=
	\cfrac{2}{a^2} \left[ \cfrac{x^3}{3} \right]_0^a
	\\ &=&
	\cfrac{2}{3} a
\end{eqnarray}
$$

同様に

$$
\begin{eqnarray}
	E(x^2) &=& \int_0^a x^2 f(x) dx
	\\ &=&
	\cfrac{2}{a^2} \int_0^a x^3 dx
	=
	\cfrac{2}{a^2} \left[ \cfrac{x^4}{4} \right]_0^a
	\\ &=&
	\cfrac{1}{2} a^2
\end{eqnarray}
$$

であるから、母集団の分散 $\sigma^2$ は

$$
\begin{eqnarray}
	\sigma^2 &=& V(x) = E(x^2) - E(x)^2
	\\ &=&
	\cfrac{1}{2} a^2 - \cfrac{4}{9} a^2
	\\ &=&
	\cfrac{1}{18} a^2
\end{eqnarray}
$$

## Appendix: 実験に使った Python コード

{% gist b932ca156b5f7e31158b9dce341856ec central-limit-theorem.py %}
