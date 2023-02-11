---
title: 同時確率分布
title-en: Joint Probability Distribution
---

# 同時確率分布とは

複数の確率変数の組が同時に実現する確率の分布。

それぞれの確率変数が離散型確率変数であれば **同時確率質量関数**、連続であれば **同時確率密度関数** で表される。

# 同時確率分布の性質

## 同時確率密度の変数変換

> **【定理】**
> 
>  $n$ 個の確率変数 $\boldsymbol{X} = (X_1, \cdots, X_n)$ の同時確率密度関数を $f_{X}(x_1, \cdots, x_n)$ とする。  
>  確率変数 $\boldsymbol{X}$ を逆変換可能・微分可能な実数値関数によって別の確率変数 $\boldsymbol{Y} = (Y_1(\boldsymbol{X}), \cdots, Y_n(\boldsymbol{X}))$ に変換するとき、$\boldsymbol{Y}$ の同時確率密度関数 $f_Y(y_1, \cdots, y_n)$ は以下の式で表される。
>  
>  $$
f_Y(y_1, \cdots, y_n) = f_X(x_1, \cdots, x_n) \det J
$$
>
> ただし、$\det J$ は行列 $J$ の行列式であり、$J$ はヤコビ行列
> 
> $$
J = \begin{pmatrix}
	\cfrac{\partial x_1}{\partial y_1} & \cfrac{\partial x_1}{\partial y_2} & \cdots & \cfrac{\partial x_1}{\partial y_n} \\
	\cfrac{\partial x_2}{\partial y_1} & \cfrac{\partial x_2}{\partial y_2} & \cdots & \cfrac{\partial x_2}{\partial y_n} \\
	\vdots & \vdots & \ddots & \vdots \\
	\cfrac{\partial x_n}{\partial y_1} & \cfrac{\partial x_n}{\partial y_2} & \cdots & \cfrac{\partial x_n}{\partial y_n}
\end{pmatrix}
$$

**【証明】**

確率変数 $\boldsymbol{Y}$ の累積分布関数 $F_Y(y_1, \cdots, y_n)$ は、

$$
\begin{eqnarray}
	F_Y(y_1, \cdots, y_n)
	&=&
	P(Y_1 \le y1, \cdots, Y_n \le y_n)
	\\ &=&
	\int_{Y_1(\boldsymbol{x}) \le y_1, \cdots, Y_n(\boldsymbol{x}) \le y_n}
	f_X(x_1, \cdots, x_n) dx_1 \cdots dx_n
	\\ &=&
	\int_{-\infty}^{y_n} \cdots \int_{-\infty}^{y_1}
	f_X(x_1(\boldsymbol{y}), \cdots, x_n(\boldsymbol{y})) |J|
	dy_1 \cdots dy_n
\end{eqnarray}
$$

最後の変換では、重積分の変数変換の公式を用いた。

確率密度関数を求めるには、累積分布関数を微分すれば良いので、

$$
\begin{eqnarray}
	f_Y(y_1, \cdots, y_n)
	&=&
	\cfrac{\partial^n}{\partial y_1 \cdots \partial y_n} F_Y(y_1, \cdots, y_n)
	\\ &=&
	f_X(x_1(\boldsymbol{y}), \cdots, x_n(\boldsymbol{y})) |J|
\end{eqnarray}
$$
