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

# 勾配・発散・回転

## 勾配

### 定義

スカラー関数 $f(x,y,z)$ の **勾配** $\mathrm{grad}\,f$ は下式で定義される。

$$
\mathrm{grad}\,f := \nabla f = \left(
    \cfrac{\partial f}{\partial x},
    \cfrac{\partial f}{\partial y},
    \cfrac{\partial f}{\partial z}
\right)
$$

### 数学的な意味

> **【勾配の数学的意味】**
> 
> 関数 $f(x,y,z)$ の勾配 $\nabla f$ は、点 $\boldsymbol{x}=(x,y,z)$ から微小変位 $d\boldsymbol{x}=(dx,dy,dz)$ だけ移動するとき、$f(x,y,z)$ の増加が最も大きい方向を示す。

**【解説】**

点 $\boldsymbol{x}=(x,y,z)$ からの微小変位 $d\boldsymbol{x}=(dx,dy,dz)$ を考える。  

$$
f(x+dx,y+dy,z+dz)
=
f(x,y,z)
+ \cfrac{\partial f}{\partial x}dx
+ \cfrac{\partial f}{\partial y}dy
+ \cfrac{\partial f}{\partial z}dz
$$

であるから、この変位による $f(x,y,z)$ の値の変化 $df$ は、

$$
\begin{eqnarray}
    df &=& f(x+dx,y+dy,z+dz) - f(x,y,z)
    \\ &=&
    \cfrac{\partial f}{\partial x}dx
    + \cfrac{\partial f}{\partial y}dy
    + \cfrac{\partial f}{\partial z}dz
\end{eqnarray}
$$

最後の式は、$f$ の勾配 $\nabla f$ と微小変位 $d\boldsymbol{x}=(dx,dy,dz)$ の内積に等しい：

$$
df = \nabla f \cdot d\boldsymbol{x}
$$

微小変位 $d\boldsymbol{x}$ の大きさを固定するとき、$f$ の微小増加 $df$ を最大化するには、右辺の内積を最大化すればよい。  
すなわち、$d\boldsymbol{x}$ が $\nabla f$ と同じ向きであれば良い。

したがって、スカラー関数 $f(x,y,z)$ の勾配 $\nabla f$ は、微小変位 $d\boldsymbol{x}$ を与えるとき、$f(x,y,z)$ の増加量を最大化する方向を示す。


## 発散

### 定義

ベクトル関数 $\boldsymbol{v}(x,y,z)$ の **発散** $\mathrm{div}\,\boldsymbol{v}$ は下式で定義される。

$$
\mathrm{div}\,\boldsymbol{v} := \nabla \cdot \boldsymbol{v} =
\cfrac{\partial v_x}{\partial x} +
\cfrac{\partial v_y}{\partial y} +
\cfrac{\partial v_z}{\partial z}
$$

### 数学的な意味

> **【発散の数学的意味】** 
> 
> ベクトル場 $\boldsymbol{v}(x,y,z)$ の発散 $\nabla \cdot \boldsymbol{v}$ は、各点における流入・流出（湧き出し・吸い込み）の評価を符号付きスカラーで与える。

**【解説】**

簡単のため、二次元空間で考える：

$$
\nabla = \left(
    \cfrac{\partial}{\partial x},
    \cfrac{\partial}{\partial y}
\right)
$$

下図の通り、点 $\boldsymbol{x}$ から見て $xy$ 方向の上下左右にだけ離れた4点を取る。  

![divergence](https://gist.github.com/assets/13412823/62160cf8-3438-4210-a823-d5abe7a52262)

```python
import numpy as np
from matplotlib import pyplot as plt

plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)
plt.scatter(0, 0, label=r'$(x,y)$', color='black')
c = 'red'
plt.scatter(0.5, 0, color=c)
plt.arrow(0.5-0.3,0,0.6,0, label=r'$v_x(x+\Delta,y)$', width=0.01, color=c, ec=c)
c = 'blue'
plt.scatter(-0.5, 0, color=c)
plt.arrow(-0.5-0.3,0,0.6,0, label=r'$v_x(x-\Delta,y)$', width=0.01, color=c, ec=c)
c = 'orange'
plt.scatter(0, 0.5, color=c)
plt.arrow(0,0.5-0.3,0,0.6, label=r'$v_y(x,y+\Delta)$', width=0.01, color=c, ec=c)
c = 'green'
plt.scatter(0, -0.5, color=c)
plt.arrow(0,-0.5-0.3,0,0.6, label=r'$v_y(x,y-\Delta)$', width=0.01, color=c, ec=c)
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
plt.legend()
plt.grid()
plt.show()
```

点 $\boldsymbol{x}$ からこの4点に向かって流出するベクトルの大きさの和 $d$ を計算すると、

$$
d =
v_x(x+\Delta, y) -
v_x(x-\Delta, y) +
v_y(x, y+\Delta) -
v_y(x, y-\Delta)
$$

ここで、正負の符号は「点 $\boldsymbol{x}$ から流出する向き」を正として付けている。

$\Delta$ は微小なので、テイラー展開により

$$
\begin{cases}
    v_x(x+\Delta, y) &\simeq&
    v_x(x,y) + \cfrac{\partial v_x}{\partial x}(x,y) \Delta
    \\
    v_x(x-\Delta, y) &\simeq&
    v_x(x,y) - \cfrac{\partial v_x}{\partial x}(x,y) \Delta
    \\
    v_y(x, y+\Delta) &\simeq&
    v_y(x,y) + \cfrac{\partial v_y}{\partial y}(x,y) \Delta
    \\
    v_y(x, y-\Delta) &\simeq&
    v_y(x,y) - \cfrac{\partial v_y}{\partial y}(x,y) \Delta
\end{cases}
$$

であるから、

$$
\begin{eqnarray}
    d &=&
    \cfrac{\partial v_x}{\partial x}(x,y) \Delta -
    \left( - \cfrac{\partial v_x}{\partial x}(x,y) \Delta \right) +
    \cfrac{\partial v_y}{\partial y}(x,y) \Delta -
    \left( - \cfrac{\partial v_y}{\partial y}(x,y) \Delta \right)
    \\ &=&
    2 \Delta \left(
        \cfrac{\partial v_x}{\partial x}(x,y) +
        \cfrac{\partial v_y}{\partial y}(x,y)
    \right)
\end{eqnarray}
$$

よって、

$$
d
\ \propto \ 
\cfrac{\partial v_x}{\partial x} +
\cfrac{\partial v_y}{\partial y}
=
\nabla \cdot \boldsymbol{v}
$$

したがって、発散 $\nabla \cdot \boldsymbol{v}$ はベクトル場 $\boldsymbol{v}$ の各点における流入・流出（湧き出し・吸い込み）の評価を符号付きスカラーで与える。


## 回転

### 定義

ベクトル関数 $\boldsymbol{v}(x,y,z)$ の **回転** $\mathrm{rot}\,\boldsymbol{v}$ （$\mathrm{curl}\,\boldsymbol{v}$ とも書く）は下式で定義される。

$$
\mathrm{rot}\,\boldsymbol{v} := \nabla \times \boldsymbol{v}
=
\left(
    {\frac {\partial v_{z}}{\partial y}} -
    {\frac {\partial v_{y}}{\partial z}},\ \ 
    {\frac {\partial v_{x}}{\partial z}} -
    {\frac {\partial v_{z}}{\partial x}},\ \ 
    {\frac {\partial v_{y}}{\partial x}} -
    {\frac {\partial v_{x}}{\partial y}}
\right)
$$


### 数学的な意味

> **【回転の数学的意味】** 
> 
> ベクトル場 $\boldsymbol{v}(x,y,z)$ の回転 $\nabla \times \boldsymbol{v}$ は、各点のまわりの（単位面積あたりの）物理的な回転の度合いを表す。

**【解説】**

点 $\boldsymbol{x} = (x,y,z)$ の周りのベクトル場について、$\boldsymbol{x}$ を通って $z$ 軸に平行な回転軸周りのトルク $t_z$ を考える。

下図の通り、点 $\boldsymbol{x}$ から見て $xy$ 方向の上下左右に微小距離 $\Delta$ だけ離れた4点について、回転方向（左回りを正とする）のベクトルのトルクの和を取る。

※ 点 $\boldsymbol{x}$ まわりの点 $\boldsymbol{x'}$ のベクトル場 $\boldsymbol{v}(\boldsymbol{x'})$ の **トルク** は、「点 $\boldsymbol{x}$ から見た $\boldsymbol{x'}$ の位置ベクトル $\boldsymbol{x'}-\boldsymbol{x}$」と「ベクトル場 $\boldsymbol{v}(\boldsymbol{x'})$」の外積 $(\boldsymbol{x'}-\boldsymbol{x}) \times \boldsymbol{v}(\boldsymbol{x'})$ で定義される。

![rotation](https://gist.github.com/assets/13412823/b9537088-eebf-4db7-a0f4-91db3747d9e1)

```python
import numpy as np
from matplotlib import pyplot as plt

plt.xlabel(r'$x$', fontsize=12)
plt.ylabel(r'$y$', fontsize=12)
plt.scatter(0, 0, label=r'$(x,y,z)$', color='black')
c = 'red'
plt.scatter(1, 0, color=c)
plt.arrow(1,-0.2,0,0.4, label=r'$v_y(x+\Delta,y,z)$', width=0.01, color=c, ec=c)
c = 'blue'
plt.scatter(-1, 0, color=c)
plt.arrow(-1,-0.2,0,0.4, label=r'$v_y(x-\Delta,y,z)$', width=0.01, color=c, ec=c)
c = 'orange'
plt.scatter(0, 1, color=c)
plt.arrow(-0.2,1,0.4,0, label=r'$v_x(x,y+\Delta,z)$', width=0.01, color=c, ec=c)
c = 'green'
plt.scatter(0, -1, color=c)
plt.arrow(-0.2,-1,0.4,0, label=r'$v_x(x,y-\Delta,z)$', width=0.01, color=c, ec=c)
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
plt.legend()
plt.grid()
plt.show()
```

図よりベクトル場の $\boldsymbol{x}$ 周りのトルク $t_z$ は（左回りを正とすれば）

$$
t_z =
\Delta \cdot v_x(x, y-\Delta, z) -
\Delta \cdot v_x(x, y+\Delta, z) +
\Delta \cdot v_y(x+\Delta, y, z) -
\Delta \cdot v_y(x-\Delta, y, z)
$$

$\Delta$ は微小なので、テイラー展開により

$$
\begin{cases}
    v_x(x, y-\Delta, z) &\simeq&
    v_x(x,y,z) - \cfrac{\partial v_x}{\partial y}(x,y,z) \Delta
    \\
    v_x(x, y+\Delta, z) &\simeq&
    v_x(x,y,z) + \cfrac{\partial v_x}{\partial y}(x,y,z) \Delta
    \\
    v_y(x+\Delta, y, z) &\simeq&
    v_y(x,y,z) + \cfrac{\partial v_y}{\partial x}(x,y,z) \Delta
    \\
    v_y(x-\Delta, y, z) &\simeq&
    v_y(x,y,z) - \cfrac{\partial v_y}{\partial x}(x,y,z) \Delta
\end{cases}
$$

であるから、

$$
\begin{eqnarray}
    t_z &=&
    \left(- \cfrac{\partial v_x}{\partial y}(x,y,z) \Delta^2 \right)
    - \cfrac{\partial v_x}{\partial y}(x,y,z) \Delta^2
    + \cfrac{\partial v_y}{\partial x}(x,y,z) \Delta^2
    - \left(- \cfrac{\partial v_y}{\partial x}(x,y,z) \Delta^2 \right)
    \\ &=&
    2 \Delta^2 \left(
        \cfrac{\partial v_y}{\partial x}(x,y,z) -
        \cfrac{\partial v_x}{\partial y}(x,y,z)
    \right)
\end{eqnarray}
$$

同様に

- $t_x$：点 $\boldsymbol{x}$ を通り $x$ 軸に平行な回転軸周りの回転度合い
- $t_y$：点 $\boldsymbol{x}$ を通り $y$ 軸に平行な回転軸周りの回転度合い

についても計算できて、

$$
\begin{eqnarray}
    t_x &=& 2 \Delta^2 \left(
        \cfrac{\partial v_z}{\partial y}(x,y,z) -
        \cfrac{\partial v_y}{\partial z}(x,y,z)
    \right)
    \\
    t_y &=& 2 \Delta^2 \left(
        \cfrac{\partial v_x}{\partial z}(x,y,z) -
        \cfrac{\partial v_z}{\partial x}(x,y,z)
    \right)
\end{eqnarray}
$$

以上により、

$$
(t_x, t_y, t_z)
\ \propto \ 
\left(
    {\frac {\partial v_{z}}{\partial y}} -
    {\frac {\partial v_{y}}{\partial z}},\ \ 
    {\frac {\partial v_{x}}{\partial z}} -
    {\frac {\partial v_{z}}{\partial x}},\ \ 
    {\frac {\partial v_{y}}{\partial x}} -
    {\frac {\partial v_{x}}{\partial y}}
\right) = \nabla \times \boldsymbol{v}
$$

したがって、回転 $\nabla \times \boldsymbol{v}$ はベクトル場 $\boldsymbol{v}$ の各点 $\boldsymbol{x}$ 周りの回転度合いを表す。