---
title: 独立な確率変数の和
---

# 独立な確率変数の和が従う分布

独立な確率変数 $P, Q$ がそれぞれ確率分布 $f_P(x), f_Q(x)$ に従うとき、確率変数 $P + Q$ が従う確率密度関数は以下の式で表される。

$$
f_{P+Q}(x) = \int_{-\infty}^{\infty} f_P (t) f_Q (x-t) dt
$$

# 式の導出

## 累積確率分布関数の導出

まず $P+Q$ の累積確率分布関数 $F_{P+Q}(x)$ を計算する。  
$P, Q$ は独立なので、$P,Q$ の同時確率密度はそれぞれの確率密度関数の積

$$
f_P(p) f_Q(q)
$$

になる。

$F_{P+Q}(x)$ は $P+Q \le x$ となる確率であるから、$PQ$ 空間の直線

$$
P + Q = x = \mathrm{const.}
$$

より下側の空間（$P+Q \le x$）で $f_P(p)f_Q(q)$ を積分すれば良い。

![Figure_1](https://user-images.githubusercontent.com/13412823/216754095-ab4eaf0c-397c-4135-ac38-897a1ba6cd28.png)

よって

$$
\begin{eqnarray}
	F_{P+Q}(x) &=& \int_{-\infty}^{\infty} \int_{-\infty}^{x-q} f_P(p) f_Q(q) dp dq
	\\ &=&
	\int_{-\infty}^{\infty} f_Q(q) \left( \int_{-\infty}^{x-q} f_P(p) dp \right) dq
\end{eqnarray}
$$

$u = p + q$ とおくと、

$$
\begin{eqnarray}
	F_{P+Q}(x) &=&
	\int_{-\infty}^{\infty} f_Q(q) \left( \int_{-\infty}^x f_P(u - q) du \right) dq
	\\ &=&
	\int_{-\infty}^x \left( \int_{-\infty}^{\infty} f_P(u-q) f_Q(q) dq \right) du
\end{eqnarray}
$$

$P + Q$ の確率密度は累積確率分布の微分で計算できるから、

$$
\begin{eqnarray}
	f_{P+Q}(x) &=&
	\cfrac{d}{dx} F_{P+Q}(x)
	\\ &=&
	\int_{-\infty}^{\infty} f_P(x-q) f_Q(q) dq
\end{eqnarray}
$$

これは証明したかった式と等価（$t=x-q$ とおけば同じ式を得る）。
