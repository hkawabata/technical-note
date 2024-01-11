---
title: ディリクレ境界条件
title-en: Dirichlet boundary condition
---
# 概要

微分方程式の解を決定するための境界条件の形状の1つ。  
境界条件上の点の値を直接与えるもの。

微分方程式の解となる関数を $f(x)$、考える領域の境界点を $x=x_0$ として、

$$
f(x_0) = \alpha \qquad (\alpha = \mathrm{const.})
$$

の形で与えられる。


# 具体例

> 微分方程式
> 
> $$
\cfrac{df(x)}{dx} = 3f(x)
$$
> 
> ディリクレ境界条件
> 
> $$
f(x_0) = 1
$$

与えられた微分方程式の一般解は

$$
f(x) = a e^{3x} \qquad (a = \mathrm{const.})
$$

であり、積分定数 $a$ の分だけ自由度が残る。  
ここに境界条件を代入すると

$$
1 = a e^{3x_0} \quad \Longleftrightarrow \quad a = e^{-3x_0}
$$

であるから、微分方程式の解は

$$
f(x) = e^{3(x-x_0)}
$$

と一意に定まる。