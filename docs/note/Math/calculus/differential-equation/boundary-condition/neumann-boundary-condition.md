---
title: ノイマン境界条件
title-en: Neumann boundary condition
---
# 概要

微分方程式の解を決定するための境界条件の形状の1つ。  
境界条件上の点の値を直接与えるもの。

微分方程式の解となる関数を $f(x)$、考える区間の境界点を $x=x_0$ として、

$$
\cfrac{df}{dx}(x_0) = \alpha \qquad (\alpha = \mathrm{const.})
$$

の形で与えられる。


# 具体例

> 微分方程式
> 
> $$
\cfrac{d^2f(x)}{dx^2} = f(x)
$$
> 
> ノイマン境界条件
> 
> $$
\cfrac{df}{dx}(0) = 0
$$

与えられた微分方程式の一般解は

$$
f(x) = ae^x + be^{-x}
$$

であり、積分定数 $a,b$ の分だけ自由度が残る。  
両辺を微分して境界条件を代入すると

$$
0 = a - b \quad \Longleftrightarrow \quad a = b
$$

であるから、微分方程式の解は

$$
f(x) = a(e^x - e^{-x})
$$

となる。