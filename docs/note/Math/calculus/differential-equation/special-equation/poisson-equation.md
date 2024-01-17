---
title: ポアソン方程式
title-en: Poisson's equation
---
# 定義

空間座標 $\boldsymbol{r}=(x,y,z)$ を変数に持つ関数 $u(\boldsymbol{r})=u(x,y,z)$ に関する偏微分方程式

$$
\cfrac{\partial^2 u}{\partial x^2} +
\cfrac{\partial^2 u}{\partial y^2} +
\cfrac{\partial^2 u}{\partial z^2}
=
f(x, y, z)
\tag{1}
$$

を **ポアソン方程式** という。

ベクトル演算子 $\nabla$ を以下の式で定義すると、

$$
\nabla := \left( \cfrac{\partial}{\partial x}, \cfrac{\partial}{\partial y}, \cfrac{\partial}{\partial z} \right)
$$

$(1)$ は次のように表すこともできる。

$$
\nabla^2 u = f(x,y,z)
\tag{1'}
$$

ただし、

$$
\nabla^2 := \nabla \cdot \nabla
=
\cfrac{\partial^2}{\partial x^2} +
\cfrac{\partial^2}{\partial y^2} +
\cfrac{\partial^2}{\partial z^2}
$$


# 導出

前提
- $\rho(\boldsymbol{r})=\rho(x,y,z)$：何かしらの物理量の密度分布。**距離に反比例する大きさの位置エネルギーを与える（比例定数：$k$）**
- $u(\boldsymbol{r})=u(x,y,z)$：点 $\boldsymbol{r}=(x,y,z)$ における位置エネルギー

## 一般のポアソン方程式

点 $\boldsymbol{r'}=(x',y',z')$ における密度分布 $\rho(\boldsymbol{r'})$ が点 $\boldsymbol{r}=(x,y,z)$ に生じさせる位置エネルギー $\Delta u(\boldsymbol{r}, \boldsymbol{r'})$ は、

$$
\Delta u(\boldsymbol{r}, \boldsymbol{r'})
= \cfrac{k \rho(\boldsymbol{r'})}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert}
\tag{2}
$$

$u(\boldsymbol{r})$ はこれを全空間の $\boldsymbol{r'}$ に関して積分すれば得られるので、

$$
\begin{eqnarray}
    u(\boldsymbol{r}) &=& \int_V \Delta u(\boldsymbol{r}, \boldsymbol{r'}) d\boldsymbol{r'}
    \\ &=&
    k \int_V \cfrac{\rho(\boldsymbol{r'})}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert} d\boldsymbol{r'}
    \tag{3}
\end{eqnarray}
$$

ここで、$\int_V$ は空間全体の積分を表す：

$$
\int_V f(\boldsymbol{r'}) d\boldsymbol{r'} =
\int_{-\infty}^\infty \int_{-\infty}^\infty \int_{-\infty}^\infty 
f(\boldsymbol{r'})
dx' dy' dz'
$$

$(3)$ を $x$ で偏微分すると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x}
    &=&
    k \int_V \rho(\boldsymbol{r'}) \cfrac{\partial}{\partial x} \left( \cfrac{1}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert} \right) d\boldsymbol{r'}
    \\ &=&
    k \int_V \rho(\boldsymbol{r'}) \cfrac{\partial}{\partial x} \left( \cfrac{1}{\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}} \right) d\boldsymbol{r'}
    \\ &=&
    k \int_V \rho(\boldsymbol{r'}) \cfrac{x-x'}{\left(\sqrt{(x-x')^2+(y-y')^2+(z-z')^2}\right)^3} d\boldsymbol{r'}
    \\ &=&
    k \int_V \rho(\boldsymbol{r'}) \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3} d\boldsymbol{r'}
    \tag{4}
\end{eqnarray}
$$

$y,z$ についても同様に計算できるので、

$$
\nabla u
=
\left(
    \cfrac{\partial u}{\partial x},
    \cfrac{\partial u}{\partial y},
    \cfrac{\partial u}{\partial z}
\right)
=
k \int_V
    \rho(\boldsymbol{r'}) \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
d\boldsymbol{r'}
\tag{5}
$$

よって

$$
\nabla^2 u =
\nabla \cdot \nabla u
=
k \int_V
    \rho(\boldsymbol{r'}) \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
d\boldsymbol{r'}
\tag{6}
$$

ここで、中心が $\boldsymbol{r}$ で微小な半径 $\varepsilon$ を持つ球面 $S': \vert \boldsymbol{r'}-\boldsymbol{r} \vert = \varepsilon$ を考え、この球面の内部 $V_\mathrm{in}: \vert \boldsymbol{r'}-\boldsymbol{r} \vert \lt \varepsilon$ と 外部 $V_\mathrm{out}: \vert \boldsymbol{r'}-\boldsymbol{r} \vert \ge \varepsilon$ とで積分範囲を分ける。  
半径 $\varepsilon$ は微小であり、球の内部 $V_\mathrm{in}$ においては $\rho(\boldsymbol{r'})$ はほぼ均一とみなせる（$\rho(\boldsymbol{r'}) \simeq \rho(\boldsymbol{r})$）ので、

$$
\begin{eqnarray}
    \nabla^2 u &=&
    k \int_{V_\mathrm{in}}
        \rho(\boldsymbol{r'}) \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    +
    k \int_{V_\mathrm{out}}
        \rho(\boldsymbol{r'}) \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    \\ &=&
    k \rho(\boldsymbol{r}) \int_{V_\mathrm{in}}
        \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    +
    k \int_{V_\mathrm{out}}
        \rho(\boldsymbol{r'}) \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    \tag{7}
\end{eqnarray}
$$

球面の外部 $V_\mathrm{out}$ では $\vert \boldsymbol{r'}-\boldsymbol{r} \vert \ne 0$ であるから、非積分関数の分母はゼロにならない。  
$(4)$ をもう一度 $x$ で偏微分すると、

$$
\begin{eqnarray}
    \cfrac{\partial^2 u}{\partial x^2}
    &=&
    k \int_V
        \rho(\boldsymbol{r'})
        \cfrac{\partial}{\partial x} \left( \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3} \right)
    d\boldsymbol{r'}
    \\ &=&
    k \int_V
        \rho(\boldsymbol{r'})
        \cfrac{
            1 \cdot \vert \boldsymbol{r}-\boldsymbol{r'} \vert^3 -
            (x-x') \cdot 3(x-x')\vert \boldsymbol{r}-\boldsymbol{r'} \vert
        }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^6}
    d\boldsymbol{r'}
    \\ &=&
    k \int_V
        \rho(\boldsymbol{r'})
        \cfrac{
            \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2 -
            3(x-x')^2
        }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^5}
    d\boldsymbol{r'}
    \tag{8}
\end{eqnarray}
$$

であり、$y,z$ についても同様なので、

$$
\begin{eqnarray}
    \int_{V_\mathrm{out}}
        \rho(\boldsymbol{r'}) \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    &=&
    \int_{V_\mathrm{out}}
        \rho(\boldsymbol{r'})
        \cfrac{
            3 \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2 -
            3 \left\{ (x-x')^2 + (y-y')^2 + (z-z')^2 \right\}
        }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^5}
    d\boldsymbol{r'}
    \\ &=&
    \int_{V_\mathrm{out}}
        \rho(\boldsymbol{r'})
        \cfrac{
            3 \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2 -
            3 \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2
        }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^5}
    d\boldsymbol{r'}
    \\ &=&
    0
    \tag{9}
\end{eqnarray}
$$

これを $(7)$ に代入して、

$$
\nabla^2 u =
k \rho(\boldsymbol{r}) \int_{V_\mathrm{in}}
    \nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
d\boldsymbol{r'}
\tag{10}
$$

ここで、**ガウスの発散定理** を適用するため、偏微分の置き換えを行う。$(8)$ の途中計算と同様の計算により、

$$
\begin{eqnarray}
    \cfrac{\partial}{\partial x} \left(
        \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    \right)
    &=&
    \cfrac{
        \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2 - 3(x-x')^2
    }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^5}
    \\
    \cfrac{\partial}{\partial x'} \left(
        \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    \right)
    &=&
    - \cfrac{
        \vert \boldsymbol{r}-\boldsymbol{r'} \vert^2 - 3(x-x')^2
    }{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^5}
\end{eqnarray}
$$

であるから、

$$
\cfrac{\partial}{\partial x} \left(
    \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
\right)
=
- \cfrac{\partial}{\partial x'} \left(
    \cfrac{x-x'}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
\right)

$$

$y',z'$ の偏微分についても同様なので、

$$
\nabla \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
=
- \nabla' \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
\qquad
\left(
    \nabla' := \left(
        \cfrac{\partial}{\partial x'},
        \cfrac{\partial}{\partial y'},
        \cfrac{\partial}{\partial z'}
    \right)
\right)
\tag{11}
$$

これを $(10)$ に代入して、

$$
\nabla^2 u =
- k \rho(\boldsymbol{r}) \int_{V_\mathrm{in}}
    \nabla' \cdot \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
d\boldsymbol{r'}
\tag{12}
$$

ガウスの発散定理より、任意のベクトル関数 $\boldsymbol{f}(\boldsymbol{r})$ の発散 $\nabla \cdot \boldsymbol{f}(\boldsymbol{r})$ のなめらかな閉曲面内の空間積分 $\int_V$ は、その閉曲面上の面積分 $\int_S$ に書き換えることができる：

$$
\int_V \nabla \cdot \boldsymbol{f}(\boldsymbol{r}) d\boldsymbol{r}
=
\int_S \boldsymbol{f}(\boldsymbol{r}) \cdot \boldsymbol{n}(\boldsymbol{r}) dS
\tag{13}
$$

- $dS$：閉曲面上の微小面積
- $\boldsymbol{n}(\boldsymbol{r})$：閉曲面上の点 $\boldsymbol{r}$ における外向き法線単位ベクトル

これを $(12)$ に適用する。球面 $S'$ 上の点 $\boldsymbol{r'}$ における外向き法線単位ベクトルは

$$
\boldsymbol{n}(\boldsymbol{r'})
=
\cfrac{\boldsymbol{r'}-\boldsymbol{r}}{\vert \boldsymbol{r'}-\boldsymbol{r} \vert}
$$

なので、

$$
\begin{eqnarray}
    \nabla^2 u
    &=&
    -k \rho(\boldsymbol{r})
    \int_{V_\mathrm{in}}
        \nabla' \cdot
        \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
    d\boldsymbol{r'}
    \\ &=&
    -k \rho(\boldsymbol{r})
    \int_{S'}
        \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
        \cdot
        \boldsymbol{n}(\boldsymbol{r'})
    dS'
    \\ &=&
    -k \rho(\boldsymbol{r})
    \int_{S'}
        \cfrac{\boldsymbol{r}-\boldsymbol{r'}}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^3}
        \cdot
        \cfrac{\boldsymbol{r'}-\boldsymbol{r}}{\vert \boldsymbol{r'}-\boldsymbol{r} \vert}
    dS'
    \\ &=&
    k \rho(\boldsymbol{r})
    \int_{S'}
        \cfrac{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^2}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^4}
    dS'
    \\ &=&
    k \rho(\boldsymbol{r})
    \int_{S'}
        \cfrac{1}{\vert \boldsymbol{r}-\boldsymbol{r'} \vert^2}
    dS'
    \\ &=&
    \cfrac{k \rho(\boldsymbol{r})}{\varepsilon^2}
    \int_{S'} dS'
    \qquad \left( \because \vert \boldsymbol{r}-\boldsymbol{r'} \vert = \varepsilon \right)
\end{eqnarray}
$$

最後の式の積分は閉曲面 $S'$ すなわち半径 $\varepsilon$ の球面の面積であるから、値は $4\pi \varepsilon^2$。  
したがって、

$$
\nabla^2 u
= \cfrac{k \rho(\boldsymbol{r})}{\varepsilon^2} \cdot 4\pi \varepsilon^2
= 4 \pi k \rho(\boldsymbol{r})
$$

$f(\boldsymbol{r}) := 4 \pi k \rho(\boldsymbol{r})$ と置けば、ポアソン方程式 $(1')$ を得る。


## 密度分布が球対称である場合のポアソン方程式

点 $\boldsymbol{r}_0 = (x_0,y_0,z_0)$ を中心に球対称な密度分布の場合を考える。  

$$
\boldsymbol{r'} := \boldsymbol{r} - \boldsymbol{r}_0
, \quad
r' := \vert \boldsymbol{r'} \vert = \vert\boldsymbol{r}-\boldsymbol{r}_0\vert
$$

とおくと、空間の対称性から、$f,u$ はともに $r'$ のみに依存する関数：

$$
f(\boldsymbol{r}), u(\boldsymbol{r}) \longrightarrow f(r'), u(r')
$$

$u(r')$ の $x$ 微分を考えると、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial x}
    &=&
    \cfrac{\partial u}{\partial r'} \cfrac{\partial r'}{\partial x}
    \\ &=&
    \cfrac{d u}{d r'} \cfrac{\partial}{\partial x} \sqrt{(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}
    \\ &=&
    \cfrac{d u}{d r'} \cfrac{x-x_0}{\sqrt{(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}}
    \\ &=&
    \cfrac{d u}{d r'} \cfrac{x-x_0}{r'}
\end{eqnarray}
$$

もう一度 $x$ で微分すると、

$$
\begin{eqnarray}
    \cfrac{\partial^2 u}{\partial x^2}
    &=&
    \cfrac{\partial}{\partial x} \left( \cfrac{d u}{d r'} \cfrac{x-x_0}{r'} \right)
    \\ &=&
    \cfrac{\partial}{\partial x} \left( \cfrac{d u}{d r'} \right) \cfrac{x-x_0}{r'} +
    \cfrac{d u}{d r'} \cfrac{\partial}{\partial x} \left( \cfrac{x-x_0}{r'} \right)
    \\ &=&
    \cfrac{\partial}{\partial r'} \left( \cfrac{d u}{d r'} \right)
    \cfrac{\partial r'}{\partial x} \cfrac{x-x_0}{r'} +
    \cfrac{d u}{d r'}
    \left( \cfrac{1}{r'} - \cfrac{(x-x_0)^2}{r'^3} \right)
    \\ &=&
    \cfrac{d^2 u}{d r'^2} \cfrac{(x-x_0)^2}{r'^2} +
    \cfrac{d u}{d r'}
    \left( \cfrac{1}{r'} - \cfrac{(x-x_0)^2}{r'^3} \right)
\end{eqnarray}
$$

$y,z$ についての微分も同様であるから、

$$
\begin{eqnarray}
    \nabla^2 u
    &=&
    \cfrac{\partial^2 u}{\partial x^2} +
    \cfrac{\partial^2 u}{\partial y^2} +
    \cfrac{\partial^2 u}{\partial z^2}
    \\ &=&
    \cfrac{d^2 u}{d r'^2} \cfrac{(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}{r'^2} +
    \cfrac{d u}{d r'}
    \left( \cfrac{3}{r'} - \cfrac{(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}{r'^3} \right)
    \\ &=&
    \cfrac{d^2 u}{d r'^2} \cfrac{r'^2}{r'^2} +
    \cfrac{d u}{d r'}
    \left( \cfrac{3}{r'} - \cfrac{r'^2}{r'^3} \right)
    \\ &=&
    \cfrac{d^2 u}{d r'^2} +
    \cfrac{2}{r'} \cfrac{d u}{d r'}
    \\ &=&
    \cfrac{1}{r'} \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
\end{eqnarray}
$$

したがって、点 $\boldsymbol{r}_0 = (x_0,y_0,z_0)$ を中心に球対称な密度分布のけるポアソン方程式は

$$
\cfrac{1}{r'} \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
=
f(r')
\tag{14}
$$



# 一般解

$f(x,y,z)$ の形や境界条件によって異なるため、一般解を求めることは難しい。


# 境界条件と特殊解

## 特殊解の例

### 球内に一様分布している場合

> 点 $\boldsymbol{r}_0 = (x_0,y_0,z_0)$ を中心とする半径 $a$ の球面内部で一様な密度分布：
> 
> $$
f(\boldsymbol{r}) = \begin{cases}
    f_0 & \qquad \mathrm{if} \ & r' = \vert \boldsymbol{r}-\boldsymbol{r}_0 \vert \le a
    \\
    0 & \qquad \mathrm{if} \ & r' = \vert \boldsymbol{r}-\boldsymbol{r}_0 \vert \gt a
\end{cases}
$$
> 
> 境界条件：
> 
> $$
\begin{cases}
    \displaystyle \lim_{r'\to \infty} u(r') &=& 0
    \\ \\
    \displaystyle \lim_{r'\to 0} u(r') &\ne& \pm \infty
    \\ \\
    \displaystyle \lim_{r'\to a+0} u(r')
    &=&
    \displaystyle \lim_{r'\to a-0} u(r')
    \\ \\
    \displaystyle \lim_{r'\to a+0} \cfrac{d u(r')}{d r'}
    &=&
    \displaystyle \lim_{r'\to a-0} \cfrac{d u(r')}{d r'}
\end{cases}
$$
> 
> - 第1式：無限遠で $u(r')$ がゼロ
> - 第2式：点 $\boldsymbol{r}_0$ で $u(r')$ が発散しない
> - 第3式：境界となる球面において $u(r')$ が滑らかに連続（値が一致）
> - 第4式：境界となる球面において $u(r')$ が滑らかに連続（勾配が一致）

ポアソン方程式 $(14)$ を立てて解くと、

$$
\begin{eqnarray}
    &\begin{cases}
        \cfrac{1}{r'} \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
        &=& f_0
        & \qquad \mathrm{if} \ & r' \le a
        \\
        \cfrac{1}{r'} \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
        &=& 0
        & \qquad \mathrm{if} \ & r' \gt a
    \end{cases}
    \\
    \Longleftrightarrow \ 
    &\begin{cases}
        \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
        &=& f_0 r'
        & \qquad \mathrm{if} \ & r' \le a
        \\
        \cfrac{d^2}{d r'^2} \left( r'u(r') \right)
        &=& 0
        & \qquad \mathrm{if} \ & r' \gt a
    \end{cases}
    \\
    \Longleftrightarrow \ 
    &\begin{cases}
        r'u(r')
        &=& \cfrac{f_0}{6} r'^3 + C_1 r' + C_2
        & \qquad \mathrm{if} \ & r' \le a
        \\
        r'u(r')
        &=& D_1 r' + D_2
        & \qquad \mathrm{if} \ & r' \gt a
    \end{cases}
    \\
    \Longleftrightarrow \ 
    &\begin{cases}
        u(r')
        &=& \cfrac{f_0}{6} r'^2 + C_1 + \cfrac{C_2}{r'}
        & \qquad \mathrm{if} \ & r' \le a
        \\
        u(r')
        &=& D_1 + \cfrac{D_2}{r'}
        & \qquad \mathrm{if} \ & r' \gt a
    \end{cases}
\end{eqnarray}
$$

ここで、$C_1, C_2, D_1, D_2$ は積分定数。

境界条件を全て適用すると、

$$
\begin{cases}
    \displaystyle \lim_{r'\to \infty} \left( D_1 + \cfrac{D_2}{r'} \right) &=& 0
    \\ \\
    \displaystyle \lim_{r'\to 0} \left( \cfrac{f_0}{6} r'^2 + C_1 + \cfrac{C_2}{r'} \right) &\ne& \pm \infty
    \\ \\
    \displaystyle \lim_{r'\to a+0} \left( D_1 + \cfrac{D_2}{r'} \right)
    &=&
    \displaystyle \lim_{r'\to a-0} \left( \cfrac{f_0}{6} r'^2 + C_1 + \cfrac{C_2}{r'} \right)
    \\ \\
    \displaystyle \lim_{r'\to a+0} \left( -\cfrac{D_2}{r'^2} \right)
    &=&
    \displaystyle \lim_{r'\to a-0} \left( \cfrac{f_0}{3} r' - \cfrac{C_2}{r'^2} \right)
\end{cases}
$$

第1式より $D_1=0$、第2式より $C_2 = 0$ なので、これらを第3,4式に代入して、

$$
\begin{eqnarray}
    & \begin{cases}
        \displaystyle \lim_{r'\to a+0} \cfrac{D_2}{r'}
        &=&
        \displaystyle \lim_{r'\to a-0} \left( \cfrac{f_0}{6} r'^2 + C_1 \right)
        \\ \\
        \displaystyle \lim_{r'\to a+0} \left( -\cfrac{D_2}{r'^2} \right)
        &=&
        \displaystyle \lim_{r'\to a-0} \cfrac{f_0}{3} r'
    \end{cases}
    \\ \\ \Longleftrightarrow \quad
    & \begin{cases}
        \cfrac{D_2}{a}
        &=&
        \cfrac{f_0}{6} a^2 + C_1
        \\ \\
        -\cfrac{D_2}{a^2}
        &=&
        \cfrac{f_0}{3} a
    \end{cases}
\end{eqnarray}
$$

これを解くと、

$$
D_2 = - \cfrac{f_0 a^3}{3}
,\quad
C_1 = - \cfrac{f_0 a^2}{2}
$$

以上により、

$$
\begin{cases}
    u(r')
    &=& \cfrac{f_0 r'^2}{6} - \cfrac{f_0 a^2}{2}
    & \qquad \mathrm{if} \ & r' \le a
    \\
    u(r')
    &=& - \cfrac{f_0 a^3}{3r'}
    & \qquad \mathrm{if} \ & r' \gt a
    \end{cases}
$$

$\boldsymbol{r}$ の表式で書くと、

$$
\begin{cases}
    u(\boldsymbol{r})
    &=& \cfrac{f_0 \vert \boldsymbol{r}-\boldsymbol{r}_0 \vert^2}{6} - \cfrac{f_0 a^2}{2}
    & \qquad \mathrm{if} \ & \vert \boldsymbol{r}-\boldsymbol{r}_0 \vert \le a
    \\
    u(\boldsymbol{r})
    &=& - \cfrac{f_0 a^3}{3\vert \boldsymbol{r}-\boldsymbol{r}_0 \vert}
    & \qquad \mathrm{if} \ & \vert \boldsymbol{r}-\boldsymbol{r}_0 \vert \gt a
    \end{cases}
$$

$f_0=1, a=10$ の場合の $u(r')$ を描画：

![poisson](https://gist.github.com/assets/13412823/4f748cbc-cc1c-4be5-8200-fb027c61be3f)

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/4cb052a95ff294e143b09aee4b55bd95#file-poisson-eq-spherical-symmetry-py)
