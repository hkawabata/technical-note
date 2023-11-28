---
title: コーシー・リーマンの方程式
title-en: Cauchy–Riemann Equations
---
# コーシー・リーマンの方程式とは

複素関数 $f(z)$ が[正則関数](regular-analytic-function.md)であるための必要十分条件を示す方程式。  
$z = x+iy\ (x,y \in \mathbb{R})$ として、$f(z)$ がある実数関数 $u(x,y),\ v(x,y)$ を用いて

$$
f(z) = u(x,y) + iv(x,y)
$$

と書ける時、コーシー・リーマンの方程式は

$$
\begin{cases}
    \cfrac{\partial u(x,y)}{\partial x} = \cfrac{\partial v(x,y)}{\partial y}
    \\
    \cfrac{\partial u(x,y)}{\partial y} = - \cfrac{\partial v(x,y)}{\partial x}
\end{cases}
$$

- 点 $z=z_0$ においてこの方程式が成り立てば、$f(z)$ は $z=z_0$ で **微分可能**
- 点 $z=z_0$ とその近傍においてこの方程式が成り立てば、$f(z)$ は $z=z_0$ で **正則**


# 例

## 例1：任意の点で正則

> $f(z) = az^2+bz+c$

$z=x+iy$ を代入して、

$$
\begin{eqnarray}
    f(z) &=& a(x+iy)^2 + b(x+iy) + c
    \\ &=&
    (ax^2-ay^2 + bx + c) + i(2axy + by)
\end{eqnarray}
$$

よって

$$
\begin{cases}
    u(x,y) &=& ax^2-ay^2 + bx + c
    \\
    v(x,y) &=& 2axy + by
\end{cases}
$$

偏微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x} &=& 2ax + b
    \\
    \cfrac{\partial u}{\partial y} &=& -2ay
    \\
    \cfrac{\partial v}{\partial x} &=& 2ay
    \\
    \cfrac{\partial v}{\partial y} &=& 2ax + b
\end{eqnarray}
$$

任意の $z$ に関してコーシー・リーマンの方程式が成り立つので、$f(z)$ は複素空間全体で正則。


## 例2：特異点が存在


> $f(z) = \cfrac{1}{z}$

$z=x+iy$ を代入して、

$$
\begin{eqnarray}
    f(z) &=& \cfrac{1}{x+iy}
    \\ &=&
    \cfrac{x-iy}{x^2+y^2}
    \\ &=&
    \cfrac{x}{x^2+y^2} + i\cfrac{-y}{x^2+y^2}
\end{eqnarray}
$$

よって

$$
\begin{cases}
    u(x,y) &=& \cfrac{x}{x^2+y^2}
    \\
    v(x,y) &=& \cfrac{-y}{x^2+y^2}
\end{cases}
$$

偏微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x} &=& \cfrac{1\cdot(x^2+y^2)-x\cdot2x}{(x^2+y^2)^2} = \cfrac{y^2-x^2}{(x^2+y^2)^2}
    \\
    \cfrac{\partial u}{\partial y} &=& \cfrac{-2y \cdot x}{(x^2+y^2)^2} = \cfrac{-2xy}{(x^2+y^2)^2}
    \\
    \cfrac{\partial v}{\partial x} &=& \cfrac{-2x \cdot (-y)}{(x^2+y^2)^2} = \cfrac{2xy}{(x^2+y^2)^2}
    \\
    \cfrac{\partial v}{\partial y} &=& \cfrac{-1\cdot(x^2+y^2)-(-y)\cdot 2y}{(x^2+y^2)^2} = \cfrac{y^2-x^2}{(x^2+y^2)^2}
\end{eqnarray}
$$

$x=y=0$ すなわち $z=0$ においては偏微分が発散するが、それ以外の点では偏微分を計算でき、コーシー・リーマンの方程式も成り立つ。  
したがって、[特異点](singularity.md) $z=0$ を除く任意の領域で $f(z)$ は正則。


## 例3：特定の点でのみコーシー・リーマンの方程式が成り立つ


> $f(z) = \vert z \vert^2$

$z=x+iy$ を代入して、

$$
\begin{eqnarray}
    f(z) &=& x^2 + y^2
\end{eqnarray}
$$

よって

$$
\begin{cases}
    u(x,y) &=& x^2+y^2
    \\
    v(x,y) &=& 0
\end{cases}
$$

偏微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x} &=& 2x
    \\
    \cfrac{\partial u}{\partial y} &=& 2y
    \\
    \cfrac{\partial v}{\partial x} &=& 0
    \\
    \cfrac{\partial v}{\partial y} &=& 0
\end{eqnarray}
$$

よって、$x=y=0$ すなわち $z=0$ でのみコーシー・リーマンの方程式が成り立つ。  
すなわち、$f(z)$ は $z=0$ でのみ微分可能であるが、この点のどんな近傍でも微分できないため、正則ではない。


## 例4：コーシー・リーマンの方程式が成り立たない

> $f(z) = z - \bar{z}$
> 
> ただし、$\bar{z}$ は $z$ の共役複素数

$z=x+iy$ を代入して、

$$
f(z) = (x+iy) - (x-iy) = 2iy
$$

よって

$$
\begin{cases}
    u(x,y) &=& 0
    \\
    v(x,y) &=& 2y
\end{cases}
$$

偏微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x} &=& 0
    \\
    \cfrac{\partial u}{\partial y} &=& 0
    \\
    \cfrac{\partial v}{\partial x} &=& 0
    \\
    \cfrac{\partial v}{\partial y} &=& 2
\end{eqnarray}
$$

よってどの点でもコーシー・リーマンの方程式を満たさないため、$f(z)$ はどんな領域でも正則ではない。
