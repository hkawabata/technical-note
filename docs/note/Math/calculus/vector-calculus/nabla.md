---
title: ナブラ演算子
title-en: nabla
---
# ナブラ演算子とは

**ナブラ演算子**：ベクトル解析における微分演算子。$\nabla$ で表す。  
たとえば3次元空間におけるナブラ演算子は下式で表される。

$$
\nabla = \left(
    \cfrac{\partial}{\partial x},
    \cfrac{\partial}{\partial y},
    \cfrac{\partial}{\partial z}
\right)
$$


# ベクトル三重積・スカラー三重積


# ラプラシアン

## 定義

**ラプラシアン**：ナブラ演算子同士の内積 $\nabla \cdot \nabla$ で定義される演算子。$\nabla^2$ または $\Delta$ で表す（大文字デルタと同じ記号）。

$$
\Delta = \nabla^2 := \nabla \cdot \nabla =
\cfrac{\partial^2}{\partial x^2} +
\cfrac{\partial^2}{\partial y^2} +
\cfrac{\partial^2}{\partial z^2}
$$

## 極座標形式

極座標 $(r,\theta,\phi)$ を用いてラプラシアンを表すと、

$$
\Delta f =
\cfrac{1}{r^2} \cfrac{\partial}{\partial r}
\left( r^2 \cfrac{\partial f}{\partial r} \right) +
\cfrac{1}{r^2 \sin\theta} \cfrac{\partial}{\partial \theta}
\left( \sin\theta \cfrac{\partial f}{\partial \theta} \right) +
\cfrac{1}{r^2\sin^2\theta} \cfrac{\partial^2 f}{\partial \phi^2}
$$

### 導出

極座標 $(r,\theta,\phi)$ と直交座標 $(x,y,z)$ の関係は以下の通り。

$$
\begin{cases}
    x = r\sin\theta \cos\phi
    \\
    y = r \sin\theta \sin\phi
    \\
    z = r \cos\theta
\end{cases}
$$

$$
\begin{cases}
    r = \sqrt{x^2+y^2+z^2}
    \\
    \theta = \arctan \cfrac{\sqrt{x^2+y^2}}{z}
    \\
    \phi = \arctan \cfrac{y}{x}
\end{cases}
$$

ここで、後の計算で使うために必要な偏微分を計算しておく。

$$
\begin{eqnarray}
    \cfrac{\partial r}{\partial x}
    &=& \cfrac{x}{\sqrt{x^2+y^2+z^2}} = \cfrac{x}{r}
    = \sin\theta\cos\phi
    \\
    \cfrac{\partial r}{\partial y}
    &=& \cfrac{y}{\sqrt{x^2+y^2+z^2}} = \cfrac{y}{r}
    = \sin\theta\sin\phi
    \\
    \cfrac{\partial r}{\partial z}
    &=& \cfrac{z}{\sqrt{x^2+y^2+z^2}} = \cfrac{z}{r}
    = \cos\theta
    \\
    \cfrac{\partial \theta}{\partial x}
    &=& 2x \cdot \cfrac{1}{2z\sqrt{x^2+y^2}} \cdot \cfrac{1}{1+(x^2+y^2)/z^2}
    = \cfrac{xz}{(x^2+y^2+z^2)\sqrt{x^2+y^2}}
    \\ &=&
    \cfrac{r\sin\theta \cos\phi \cdot r\cos\theta}{r^2 \cdot r \sin \theta}
    = \cfrac{1}{r} \cos\theta \cos\phi
    \\
    \cfrac{\partial \theta}{\partial y}
    &=& 2y \cdot \cfrac{1}{2z\sqrt{x^2+y^2}} \cdot \cfrac{1}{1+(x^2+y^2)/z^2}
    = \cfrac{yz}{(x^2+y^2+z^2)^2\sqrt{x^2+y^2}}
    \\ &=&
    \cfrac{r\sin\theta \sin\phi \cdot r\cos\theta}{r^2 \cdot r \sin \theta}
    = \cfrac{1}{r} \cos\theta \sin\phi
    \\
    \cfrac{\partial \theta}{\partial z}
    &=& - \cfrac{\sqrt{x^2+y^2}}{z^2} \cdot \cfrac{1}{1+(x^2+y^2)/z^2}
    = - \cfrac{\sqrt{x^2+y^2}}{x^2+y^2+z^2}
    \\ &=&
    - \cfrac{r\sin\theta}{r^2}
    = - \cfrac{1}{r} \sin\theta
    \\
    \cfrac{\partial \phi}{\partial x}
    &=& - \cfrac{y}{x^2} \cdot \cfrac{1}{1+y^2/x^2}
    = -\cfrac{y}{x^2+y^2}
    \\ &=&
    - \cfrac{r\sin\theta \sin\phi}{r^2 \sin^2\theta}
    = -\cfrac{\sin\phi}{r\sin\theta}
    \\
    \cfrac{\partial \phi}{\partial y}
    &=& \cfrac{1}{x} \cdot \cfrac{1}{1+y^2/x^2}
    = \cfrac{x}{x^2+y^2}
    \\ &=&
    \cfrac{r\sin\theta \cos\phi}{r^2 \sin^2\theta}
    = \cfrac{\cos\phi}{r\sin\theta}
    \\
    \cfrac{\partial \phi}{\partial z}
    &=& 0
\end{eqnarray}
$$

途中、逆三角関数の微分公式

$$
\cfrac{d}{du} \arctan u = \cfrac{1}{1+u^2}
$$

と、極座標では $0 \le \theta \le \pi$ より $\sin \theta \ge 0$ であることを用いた。

以上を用いて、極座標の関数 $f(r, \theta, \phi)$ に関して、$x,y,z$ による偏微分を行う。  
まず $x$ について、

$$
\begin{eqnarray}
    \cfrac{\partial f}{\partial x}
    &=&
    \cfrac{\partial r}{\partial x} \cfrac{\partial f}{\partial r} +
    \cfrac{\partial \theta}{\partial x} \cfrac{\partial f}{\partial \theta} +
    \cfrac{\partial \phi}{\partial x} \cfrac{\partial f}{\partial \phi}
    \\ &=&
    \sin\theta\cos\phi \cfrac{\partial f}{\partial r} +
    \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial f}{\partial \theta} -
    \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial f}{\partial \phi}
    \\
    \\
    \cfrac{\partial^2 f}{\partial x^2}
    &=&
    \sin\theta\cos\phi \cfrac{\partial}{\partial r}
    \left(\cfrac{\partial f}{\partial x}\right) +
    \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial}{\partial \theta}
    \left(\cfrac{\partial f}{\partial x}\right) -
    \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial}{\partial \phi}
    \left(\cfrac{\partial f}{\partial x}\right)
    \\ &=&
    \sin\theta\cos\phi \left(
        \sin\theta\cos\phi \cfrac{\partial^2 f}{\partial r^2} -
        \cfrac{1}{r^2} \cos\theta \cos\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial^2 f}{\partial \theta \partial r} +
        \cfrac{\sin\phi}{r^2\sin\theta} \cfrac{\partial f}{\partial \phi} -
        \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi \partial r}
    \right)
    \\ && +
    \cfrac{1}{r} \cos\theta \cos\phi \left(
        \cos\theta\cos\phi \cfrac{\partial f}{\partial r} +
        \sin\theta\cos\phi \cfrac{\partial^2 f}{\partial r \partial \theta} -
        \cfrac{1}{r} \sin\theta \cos\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial^2 f}{\partial \theta^2} +
        \cfrac{\cos\theta\sin\phi}{r\sin^2\theta} \cfrac{\partial f}{\partial \phi} -
        \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi \partial \theta}
    \right)
    \\ && -
    \cfrac{\sin\phi}{r\sin\theta} \left(
        -\sin\theta\sin\phi \cfrac{\partial f}{\partial r} +
        \sin\theta\cos\phi \cfrac{\partial^2 f}{\partial r \partial \phi} -
        \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial^2 f}{\partial \theta \partial \phi} -
        \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial f}{\partial \phi} -
        \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi^2}
    \right)
    \\ &=&
    \sin^2\theta\cos^2\phi \cfrac{\partial^2 f}{\partial r^2} +
    \cfrac{\cos^2\theta \cos^2\phi}{r^2} \cfrac{\partial^2 f}{\partial \theta^2} +
    \cfrac{\sin^2\phi}{r^2\sin^2\theta} \cfrac{\partial^2 f}{\partial \phi^2}
    \\ &&+
    \cfrac{2\sin\theta\cos\theta\cos^2\phi}{r} \cfrac{\partial^2 f}{\partial r \partial \theta} -
    \cfrac{2\cos\theta\sin\phi\cos\phi}{r^2\sin\theta} \cfrac{\partial^2 f}{\partial \theta \partial \phi} -
    \cfrac{2\sin\phi\cos\phi}{r} \cfrac{\partial^2 f}{\partial \phi \partial r}
    \\ &&+
    \cfrac{\cos^2\theta\cos^2\phi+\sin^2\phi}{r} \cfrac{\partial f}{\partial r} +
    \cfrac{\cos\theta\sin^2\phi-2\sin^2\theta\cos\theta\cos^2\phi}{r^2\sin\theta} \cfrac{\partial f}{\partial \theta} +
    \cfrac{2\sin\phi\cos\phi}{r^2\sin^2\theta} \cfrac{\partial f}{\partial \phi}
\end{eqnarray}
$$

次に $y$ について、

$$
\begin{eqnarray}
    \cfrac{\partial f}{\partial y}
    &=&
    \cfrac{\partial r}{\partial y} \cfrac{\partial f}{\partial r} +
    \cfrac{\partial \theta}{\partial y} \cfrac{\partial f}{\partial \theta} +
    \cfrac{\partial \phi}{\partial y} \cfrac{\partial f}{\partial \phi}
    \\ &=&
    \sin\theta\sin\phi \cfrac{\partial f}{\partial r} +
    \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial f}{\partial \theta} +
    \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial f}{\partial \phi}
    \\
    \\
    \cfrac{\partial^2 f}{\partial y^2}
    &=&
    \sin\theta\sin\phi \cfrac{\partial}{\partial r}
    \left(\cfrac{\partial f}{\partial y}\right) +
    \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial}{\partial \theta}
    \left(\cfrac{\partial f}{\partial y}\right) +
    \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial}{\partial \phi}
    \left(\cfrac{\partial f}{\partial z}\right)
    \\ &=&
    \sin\theta\sin\phi \left(
        \sin\theta\sin\phi \cfrac{\partial^2 f}{\partial r^2} -
        \cfrac{1}{r^2} \cos\theta \sin\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial^2 f}{\partial \theta \partial r} -
        \cfrac{\cos\phi}{r^2\sin\theta} \cfrac{\partial f}{\partial \phi} +
        \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi \partial r}
    \right) +
    \\ && +
    \cfrac{1}{r} \cos\theta \sin\phi \left(
        \cos\theta\sin\phi \cfrac{\partial f}{\partial r} +
        \sin\theta\sin\phi \cfrac{\partial^2 f}{\partial r \partial \theta} -
        \cfrac{1}{r} \sin\theta \sin\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial^2 f}{\partial \theta^2} -
        \cfrac{\cos\theta\cos\phi}{r\sin^2\theta} \cfrac{\partial f}{\partial \phi} +
        \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi \partial \theta}
    \right) +
    \\ && +
    \cfrac{\cos\phi}{r\sin\theta} \left(
        \sin\theta\cos\phi \cfrac{\partial f}{\partial r} +
        \sin\theta\sin\phi \cfrac{\partial^2 f}{\partial r \partial \phi} +
        \cfrac{1}{r} \cos\theta \cos\phi \cfrac{\partial f}{\partial \theta} +
        \cfrac{1}{r} \cos\theta \sin\phi \cfrac{\partial^2 f}{\partial \theta \partial \phi} -
        \cfrac{\sin\phi}{r\sin\theta} \cfrac{\partial f}{\partial \phi} +
        \cfrac{\cos\phi}{r\sin\theta} \cfrac{\partial^2 f}{\partial \phi^2}
    \right)
    \\ &=&
    \sin^2\theta\sin^2\phi \cfrac{\partial^2 f}{\partial r^2} +
    \cfrac{\cos^2\theta \sin^2\phi}{r^2} \cfrac{\partial^2 f}{\partial \theta^2} +
    \cfrac{\cos^2\phi}{r^2\sin^2\theta} \cfrac{\partial^2 f}{\partial \phi^2}
    \\ &&+
    \cfrac{2\sin\theta\cos\theta \sin^2\phi}{r} \cfrac{\partial^2 f}{\partial r \partial \theta} +
    \cfrac{2\cos\theta \sin\phi\cos\phi}{r^2\sin\theta} \cfrac{\partial^2 f}{\partial \theta \partial \phi} +
    \cfrac{2\sin\phi\cos\phi}{r} \cfrac{\partial^2 f}{\partial \phi \partial r}
    \\ &&+
    \cfrac{\cos^2\theta\sin^2\phi+\cos^2\phi}{r} \cfrac{\partial f}{\partial r} +
    \cfrac{\cos\theta\cos^2\phi-2\sin^2\theta\cos\theta\sin^2\phi}{r^2\sin\theta} \cfrac{\partial f}{\partial \theta} -
    \cfrac{2\sin\phi\cos\phi}{r^2\sin^2\theta} \cfrac{\partial f}{\partial \phi}
\end{eqnarray}
$$

最後に $z$ について、

$$
\begin{eqnarray}
    \cfrac{\partial f}{\partial z}
    &=&
    \cfrac{\partial r}{\partial z} \cfrac{\partial f}{\partial r} +
    \cfrac{\partial \theta}{\partial z} \cfrac{\partial f}{\partial \theta} +
    \cfrac{\partial \phi}{\partial z} \cfrac{\partial f}{\partial \phi}
    \\ &=&
    \cos\theta \cfrac{\partial f}{\partial r} -
    \cfrac{\sin\theta}{r} \cfrac{\partial f}{\partial \theta}
    \\
    \\
    \cfrac{\partial^2 f}{\partial z^2}
    &=&
    \cos\theta \cfrac{\partial}{\partial r}
    \left(\cfrac{\partial f}{\partial z}\right) -
    \cfrac{\sin\theta}{r} \cfrac{\partial}{\partial \theta}
    \left(\cfrac{\partial f}{\partial z}\right)
    \\ &=&
    \cos\theta
    \left(
        \cos\theta \cfrac{\partial^2 f}{\partial r^2} +
        \cfrac{\sin\theta}{r^2} \cfrac{\partial f}{\partial \theta} -
        \cfrac{\sin\theta}{r} \cfrac{\partial f}{\partial \theta \partial r}
    \right) -
    \cfrac{\sin\theta}{r}
    \left(
        -\sin\theta \cfrac{\partial f}{\partial r} +
        \cos\theta \cfrac{\partial^2 f}{\partial r \partial \theta} -
        \cfrac{\cos\theta}{r} \cfrac{\partial f}{\partial \theta} -
        \cfrac{\sin\theta}{r} \cfrac{\partial^2 f}{\partial \theta^2}
    \right)
    \\ &=&
    \cos^2\theta \cfrac{\partial^2 f}{\partial r^2} +
    \cfrac{\sin^2\theta}{r^2} \cfrac{\partial^2 f}{\partial \theta^2} -
    \cfrac{2\sin\theta\cos\theta}{r} \cfrac{\partial f}{\partial r \partial \theta} +
    \cfrac{\sin^2\theta}{r} \cfrac{\partial f}{\partial r} +
    \cfrac{2\sin\theta\cos\theta}{r^2} \cfrac{\partial f}{\partial \theta}
\end{eqnarray}
$$

以上により、

$$
\begin{eqnarray}
    \Delta f
    &=&
    \cfrac{\partial^2 f}{\partial x^2} +
    \cfrac{\partial^2 f}{\partial y^2} +
    \cfrac{\partial^2 f}{\partial z^2}
    \\ &=&
    \cfrac{\partial^2 f}{\partial r^2} +
    \cfrac{1}{r^2} \cfrac{\partial^2 f}{\partial \theta^2} +
    \cfrac{1}{r^2\sin^2\theta} \cfrac{\partial^2 f}{\partial \phi^2} +
    \cfrac{2}{r} \cfrac{\partial f}{\partial r} +
    \cfrac{\cos\theta}{r^2\sin\theta} \cfrac{\partial f}{\partial \theta}
    \\ &=&
    \cfrac{1}{r^2} \cfrac{\partial}{\partial r}
    \left( r^2 \cfrac{\partial f}{\partial r} \right) +
    \cfrac{1}{r^2 \sin\theta} \cfrac{\partial}{\partial \theta}
    \left( \sin\theta \cfrac{\partial f}{\partial \theta} \right) +
    \cfrac{1}{r^2\sin^2\theta} \cfrac{\partial^2 f}{\partial \phi^2}
\end{eqnarray}
$$


# 勾配・発散・回転

[勾配・発散・回転](gradient-divergence-rotation.md)を参照。
