---
title: 統計学の公式
title-en: Formula for Statistics
---

# 定義

記号の定義：
- $n$：標本数
- $x_1, \cdots, x_n$：確率変数 $X$ について母集団から抽出された標本

## 標本平均

$$
\bar{x} := \cfrac{1}{n} \sum_{k=1}^{n} x_k
$$

## 標本分散

$$
s_x^2 := \cfrac{1}{n} \sum_{k=1}^{n} (x_k - \bar{x})^2
$$

## 共分散

$$
s_{xy} := \cfrac{1}{n} \sum_{k=1}^{n} (x_k - \bar{x}) (y_k - \bar{y})
$$

## 相関係数

$$
r_{xy} := \cfrac{s_{xy}}{s_x s_y}
=
\cfrac{
	\displaystyle
	\sum_{k=1}^{n} (x_k - \bar{x}) (y_k - \bar{y})
}{
	\displaystyle
	\sqrt{ \sum_{k=1}^{n} (x_k - \bar{x})^2 }
	\sqrt{ \sum_{k=1}^{n} (y_k - \bar{y})^2 }
}
$$


# 定理

記号の定義：
- $E(X)$：確率変数 $X$ の母集団の期待値（母平均）
- $V(X)$：確率変数 $X$ の母分散
- $\mathrm{Cov}(X,Y)$：確率変数 $X,Y$ の共分散
- $P(X=x) = P(x)$：確率変数 $X$ が値 $x$ を取る確率（確率密度）
- $P(X=x,Y=y) = P(x,y)$：確率変数 $X,Y$ が値 $x,y$ を取る同時確率（同時確率密度）

## 分散公式

> **【公式】**
> 
> $$
\begin{eqnarray}
	s_x^2 &=& \cfrac{1}{n} \sum_{k=1}^n x_k^2 - \bar{x}^2
	\\
	V(X) &=& E(X^2) - E(X)^2
\end{eqnarray}
\tag{1}
$$

**【証明】**

$$
\begin{eqnarray}
	s_x^2 &=& \cfrac{1}{n} \sum_{k=1}^{n} (x_k - \bar{x})^2
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k^2 +
	\cfrac{\bar{x}^2}{n} \sum_{k=1}^{n} 1 -
	\cfrac{2\bar{x}}{n} \sum_{k=1}^{n} x_k
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k^2 +
	\bar{x}^2 - 2\bar{x}^2
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k^2 - \bar{x}^2
	\\
	\\
	V(X) &=& E \left( (X-E(X))^2 \right)
	\\ &=&
	\sum_x (x-E(X))^2 P(x)
	\\ &=&
	\sum_x x^2 P(x) + E(X)^2 \sum_x P(x) - 2 E(X) \sum_x x P(x)
	\\ &=&
	\sum_x x^2 P(x) + E(X)^2 \cdot 1 - 2 E(X) \cdot E(X)
	\\ &=&
	E(X^2) - E(X)^2
\end{eqnarray}
$$

> **【公式】**
> 
> $$
\begin{eqnarray}
	s_{xy} &=& \cfrac{1}{n} \sum_{k=1}^n x_k y_k - \bar{x} \cdot \bar{y}
	\\
	\mathrm{Cov}(X, Y) &=& E(XY) - E(X)E(Y)
\end{eqnarray}
\tag{2}
$$

**【証明】**

$$
\begin{eqnarray}
	s_{xy} &=& \cfrac{1}{n} \sum_{k=1}^{n} (x_k - \bar{x}) (y_k - \bar{y})
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k y_k +
	\cfrac{\bar{x} \bar{y}}{n} \sum_{k=1}^{n} 1 -
	\cfrac{\bar{x}}{n} \sum_{k=1}^{n} y_k -
	\cfrac{\bar{y}}{n} \sum_{k=1}^{n} x_k
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k y_k +
	\bar{x} \bar{y} - \bar{x} \bar{y} - \bar{x} \bar{y}
	\\ &=&
	\cfrac{1}{n} \sum_{k=1}^{n} x_k y_k - \bar{x} \bar{y}
	\\
	\\
	\mathrm{Cov}(X,Y) &=& E \left( (X-E(X))(Y-E(Y)) \right)
	\\ &=&
	\sum_{x,y} (x - E(X))(y-E(Y)) P(x,y)
	\\ &=&
	\sum_{x,y} xy P(x,y) +
	E(X) E(Y) \sum_{x,y} P(x,y) -
	E(X) \sum_{x,y} y P(x,y) -
	E(Y) \sum_{x,y} x P(x,y)
	\\ &=&
	E(XY) + E(X)E(Y) \cdot 1 - E(X) E(Y) - E(Y) E(X)
	\\ &=&
	E(XY) - E(X)E(Y)
\end{eqnarray}
$$


## 確率変数の定数倍の期待値・分散

> **【公式】**
> 
> $a$ を定数として、
> 
> $$
E(aX) = aE(X)
\tag{3}
$$

**【証明】**

$$
E(aX) = \sum_x ax P(x) = a \sum_x x P(x) = a E(X)
$$

> **【公式】**
> 
> $a$ を定数として、
> 
> $$
V(aX) = a^2 V(X)
\tag{4}
$$

**【証明】**

$(3)$ を用いて、

$$
\begin{eqnarray}
	V(aX) &=& E \left( (aX - E(aX))^2 \right)
	\\ &=&
	E \left( (aX - aE(X))^2 \right)
	\\ &=&
	E \left( a^2(X - E(X))^2 \right)
	\\ &=&
	a^2 E \left( (X - E(X))^2 \right)
	\\ &=&
	a^2 V(X)
\end{eqnarray}
$$



## 確率変数の和の期待値・分散

> **【公式】**
> 
> $$
E(X+Y) = E(X) + E(Y)
\tag{5}
$$

**【証明】**

$$
\begin{eqnarray}
	E(X+Y) &=& \sum_{x,y} (x+y) P(x,y)
	\\ &=&
	\sum_{x,y} x P(x,y) +
	\sum_{x,y} y P(x,y)
	\\ &=&
	E(X) + E(Y)
\end{eqnarray}
$$


> **【公式】**
> 
> $$
V(X+Y) = V(X) + V(Y) + 2 \mathrm{Cov}(X,Y)
\tag{6}
$$

**【証明】**

$(1)(3)(5)$ を用いて、

$$
\begin{eqnarray}
	V(X+Y) &=& E \left( (X+Y)^2 \right) - E(X+Y)^2
	\\ &=&
	E(X^2 + Y^2 + 2XY) - ( E(X) + E(Y) )^2
	\\ &=&
	E(X^2) + E(Y^2) + 2E(XY) - E(X)^2 - E(Y)^2 - 2E(X)E(Y)
	\\ &=&
	\left( E(X^2)-E(X)^2 \right) +
	\left( E(Y^2)-E(Y)^2 \right) +
	2 \left( E(XY)-E(X)E(Y) \right)
	\\ &=&
	V(X) + V(Y) + 2\mathrm{Cov}(X,Y)
\end{eqnarray}
$$

> **【公式】**
> 
> $$
V(X+Y+Z) = V(X) + V(Y) + V(Z) +
2 \mathrm{Cov}(X,Y) + 2 \mathrm{Cov}(Y,Z) + 2 \mathrm{Cov}(Z,X)
\tag{7}
$$

**【証明】**

(TODO)

$$
V(X+Y+Z) = V(X+Y) + V(Z) + 2 \mathrm{Cov}(X+Y,Z) \cdots
$$


## 「独立な」確率変数の積の期待値・分散

> **【公式】**
> 
> 確率変数 $X, Y$ が独立であるとき、
> 
> $$
E(XY) = E(X)E(Y)
\tag{8}
$$

**【証明】**

$X, Y$ が独立である時、$x,y$ の同時確率 $P(x,y) = P(x)P(y)$ であるから、

$$
\begin{eqnarray}
	E(XY) &=&
	\sum_{x} \sum_{y} xy P(x,y)
	\\ &=&
	\sum_{x} \sum_{y} xy P(x)P(y)
	\\ &=&
	\left( \sum_{x} x P(x) \right) \left( \sum_{y} y P(y) \right)
	\\ &=&
	E(X) E(Y)
\end{eqnarray}
$$


> **【公式】**
> 
> 確率変数 $X, Y$ が独立であるとき、
> 
> $$
V(XY) = V(X)V(Y) + E(X)^2 V(Y) + E(Y)^2 V(X)
\tag{9}
$$

**【証明】**

$(1)$ より

$$
\begin{eqnarray}
	V(XY) &=& E((XY)^2) - E(XY)^2
	\\ &=&
	E(X^2Y^2) - E(XY)^2
\end{eqnarray}
$$

ここで、$X,Y$ 独立より $X^2, Y^2$ も独立であるから、$(8)$ より

$$
\begin{eqnarray}
	E(XY) &=& E(X)E(Y) \\
	E(X^2Y^2) &=& E(X^2)E(Y^2)
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
	V(XY) &=& E(X^2)E(Y^2) - \left( E(X) E(Y) \right)^2
	\\ &=&
	(V(X) + E(X)^2)(V(Y) + E(Y)^2) - E(X)^2 E(Y)^2
	\\ &=&
	V(X)V(Y) + E(X)^2 V(Y) + E(Y)^2 V(X)
\end{eqnarray}
$$

