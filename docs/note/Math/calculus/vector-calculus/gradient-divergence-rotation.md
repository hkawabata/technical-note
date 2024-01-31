---
title: 勾配・発散・回転
title-en: gradient / divergence / rotation
---
# 勾配

## 定義

スカラー関数 $f(x,y,z)$ の **勾配** $\mathrm{grad}\,f$ は下式で定義される。

$$
\mathrm{grad}\,f := \nabla f = \left(
    \cfrac{\partial f}{\partial x},
    \cfrac{\partial f}{\partial y},
    \cfrac{\partial f}{\partial z}
\right)
$$

## 数学的な意味

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


# 発散

## 定義

ベクトル関数 $\boldsymbol{v}(x,y,z)$ の **発散** $\mathrm{div}\,\boldsymbol{v}$ は下式で定義される。

$$
\mathrm{div}\,\boldsymbol{v} := \nabla \cdot \boldsymbol{v} =
\cfrac{\partial v_x}{\partial x} +
\cfrac{\partial v_y}{\partial y} +
\cfrac{\partial v_z}{\partial z}
$$

## 数学的な意味

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

（cf. [描画に用いた Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-picture-of-divergence-py)）

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


## 具体例

図示しやすいように、$xy$ 平面に平行な向きのベクトル場だけを考える。

cf.
- [ベクトル場の図示に使った Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-draw-vector-field-py)
- [発散の図示に使った Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-draw_divergence-py)


### 発散なし

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (x, -y)
    \\ \\
    \nabla \cdot \boldsymbol{v} &=& 1 + (-1) = 0
\end{eqnarray}
$$

![no-div-1](https://gist.github.com/assets/13412823/0a8ad4d2-b44e-4e1d-9820-25c841461b24)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (-y, x)
    \\ \\
    \nabla \cdot \boldsymbol{v} &=& 0 + 0 = 0
\end{eqnarray}
$$

![no-div-2](https://gist.github.com/assets/13412823/800837af-3c44-4ce5-b807-2d9a9876895b)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (\sin 2\pi y, \sin 2\pi x)
    \\ \\
    \nabla \cdot \boldsymbol{v} &=& 0 + 0 = 0
\end{eqnarray}
$$

![no-div-3](https://gist.github.com/assets/13412823/b69d95dd-de3e-4199-bbdd-aa0ad26d0d66)




### 発散あり

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (x, y)
    \\ \\
    \nabla \cdot \boldsymbol{v} &=& 1+1 = 2
\end{eqnarray}
$$

![with-div-1](https://gist.github.com/assets/13412823/fa714858-065d-4b27-a2ef-c5441510bfe5)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& \left(\cfrac{x}{\sqrt{x^2+y^2+0.1}}, \cfrac{y}{\sqrt{x^2+y^2+0.1}}\right)
    \\ \\
    \nabla \cdot \boldsymbol{v}
    &=&
    \cfrac{1\cdot \sqrt{x^2+y^2+0.1} - x \cdot x/\sqrt{x^2+y^2+0.1}}{x^2+y^2+0.1} +
    \cfrac{1\cdot \sqrt{x^2+y^2+0.1} - y \cdot y/\sqrt{x^2+y^2+0.1}}{x^2+y^2+0.1}
    \\ &=&
    \cfrac{x^2+y^2+0.2}{(\sqrt{x^2+y^2+0.1})^3}
\end{eqnarray}
$$

![with-div-2](https://gist.github.com/assets/13412823/59dc1d38-7016-47fa-ac2e-fa5b27c3a289)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (\sin 2\pi x, \sin 2\pi y)
    \\ \\
    \nabla \cdot \boldsymbol{v} &=& 2\pi (\cos 2\pi x + \cos 2\pi y)
\end{eqnarray}
$$

![with-div-3](https://gist.github.com/assets/13412823/008ac402-20ff-40ab-8ecb-d7ad18b83208)



# 回転

## 定義

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


## 数学的な意味

> **【回転の数学的意味】** 
> 
> ベクトル場 $\boldsymbol{v}(x,y,z)$ の回転 $\nabla \times \boldsymbol{v}$ は、各点のまわりの（単位面積あたりの）物理的な回転の度合いを表す。

**【解説】**

下図のように、点 $\boldsymbol{x} = (x,y,z)$ を中心とし、$xy$ 平面に並行な1辺 $\Delta$ の正方形を考える（$\Delta$ は微小な値とする）。

![rotation](https://gist.github.com/assets/13412823/6a08bdce-2029-43df-86b2-97791c8e6233)

（cf. [描画に用いた Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-picture-of-rotation-py)）

この正方形上でベクトル場 $\boldsymbol{v}(x,y,z)$ を左回りに線積分した値を $R_z$ とすると、$R_z$ は **「点 $\boldsymbol{x}$ のまわりにある、$z$ 軸方向の軸を中心とする流れ1周分を足し合わせた値」** と言える。  
よってこれがゼロでない場合、**「点 $\boldsymbol{x}$ のまわりには $z$ 軸方向の軸を中心として回転する流れ（渦）がある」**  と解釈できる。

簡単のため、正方形の各辺上では $\boldsymbol{v}$ が一定（辺の中心の値）であるとして $R_z$ を計算すると、

$$
\begin{eqnarray}
    R_z &\simeq&
    v_y\left(x+\frac{\Delta}{2}, y, z\right) \cdot \Delta +
    v_y\left(x, y+\frac{\Delta}{2}, z\right) \cdot (-\Delta) +
    v_y\left(x-\frac{\Delta}{2}, y, z\right) \cdot (-\Delta) +
    v_y\left(x, y-\frac{\Delta}{2}, z\right) \cdot \Delta
    \\ &=&
    \left\{
        v_y\left(x+\frac{\Delta}{2}, y, z\right) -
        v_y\left(x, y+\frac{\Delta}{2}, z\right) -
        v_y\left(x-\frac{\Delta}{2}, y, z\right) +
        v_y\left(x, y-\frac{\Delta}{2}, z\right)
    \right\} \cdot \Delta
\end{eqnarray}
$$

$\Delta$ は微小なので、テイラー展開により

$$
\begin{cases}
    v_x(x, y-\frac{\Delta}{2}, z) &\simeq&
    v_x(x,y,z) - \cfrac{\partial v_x}{\partial y}(x,y,z) \frac{\Delta}{2}
    \\
    v_x(x, y+\frac{\Delta}{2}, z) &\simeq&
    v_x(x,y,z) + \cfrac{\partial v_x}{\partial y}(x,y,z) \frac{\Delta}{2}
    \\
    v_y(x+\frac{\Delta}{2}, y, z) &\simeq&
    v_y(x,y,z) + \cfrac{\partial v_y}{\partial x}(x,y,z) \frac{\Delta}{2}
    \\
    v_y(x-\frac{\Delta}{2}, y, z) &\simeq&
    v_y(x,y,z) - \cfrac{\partial v_y}{\partial x}(x,y,z) \frac{\Delta}{2}
\end{cases}
$$

であるから、

$$
\begin{eqnarray}
    R_z &=&
    \left\{
    \left(- \cfrac{\partial v_x}{\partial y}(x,y,z) \cfrac{\Delta}{2} \right)
    - \cfrac{\partial v_x}{\partial y}(x,y,z) \cfrac{\Delta}{2}
    + \cfrac{\partial v_y}{\partial x}(x,y,z) \cfrac{\Delta}{2}
    - \left(- \cfrac{\partial v_y}{\partial x}(x,y,z) \cfrac{\Delta}{2} \right)
    \right\} \cdot \Delta
    \\ &=&
    \left(
        \cfrac{\partial v_y}{\partial x}(x,y,z) -
        \cfrac{\partial v_x}{\partial y}(x,y,z)
    \right) \Delta^2
\end{eqnarray}
$$

同様に $x$ 軸・$y$ 軸方向の回転軸周りの流れ $R_x, R_y$ も計算できて、

$$
\begin{eqnarray}
    R_x &=& \Delta^2 \left(
        \cfrac{\partial v_z}{\partial y}(x,y,z) -
        \cfrac{\partial v_y}{\partial z}(x,y,z)
    \right)
    \\
    R_y &=& \Delta^2 \left(
        \cfrac{\partial v_x}{\partial z}(x,y,z) -
        \cfrac{\partial v_z}{\partial x}(x,y,z)
    \right)
\end{eqnarray}
$$

以上により、$x$ 軸・$y$ 軸・$z$ 軸方向それぞれの回転軸周りの流れを並べてベクトルにすると

$$
(R_x, R_y, R_z)
\ = \ 
\left(
    {\frac {\partial v_{z}}{\partial y}} -
    {\frac {\partial v_{y}}{\partial z}},\ \ 
    {\frac {\partial v_{x}}{\partial z}} -
    {\frac {\partial v_{z}}{\partial x}},\ \ 
    {\frac {\partial v_{y}}{\partial x}} -
    {\frac {\partial v_{x}}{\partial y}}
\right) \Delta^2
= (\nabla \times \boldsymbol{v}) \Delta^2
$$

これを正方形の面積 $\Delta^2$ で割れば、$\Delta$ の大きさに依存しない $\nabla \times \boldsymbol{v}$ の表式が得られる。  
したがって、回転 $\nabla \times \boldsymbol{v}$ はベクトル場 $\boldsymbol{v}$ の各点 $\boldsymbol{x}$ 周りの回転度合いを表す。


## 具体例

図示しやすいように、$xy$ 平面に平行な向きのベクトル場だけを考える。

cf.
- [ベクトル場の図示に使った Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-draw-vector-field-py)
- [回転の図示に使った Python コード](https://gist.github.com/hkawabata/606cdb1a5d9ee14a7bb32de60813d7fa#file-draw-rotation-py)


### 回転なし

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (2x, y)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& 0 - 0 = 0
\end{eqnarray}
$$

![no-rot-1](https://gist.github.com/assets/13412823/79f50266-b3b4-49ea-a1c0-f7984e377822)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (\sin x, \cos y)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& 0 - 0 = 0
\end{eqnarray}
$$

![no-rot-2](https://gist.github.com/assets/13412823/d102e78b-67cf-4822-9cbb-dadca479dee2)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (y, x)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& 1 - 1 = 0
\end{eqnarray}
$$

![no-rot-3](https://gist.github.com/assets/13412823/64848b3c-0266-467f-bc98-7f3ebee62f53)


### 回転あり

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (-y, x)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& 1 - (-1) = 2
\end{eqnarray}
$$

![with-rot-1](https://gist.github.com/assets/13412823/d338c41d-3e83-469e-a7b1-481eea1cd6ec)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (\sin \pi y, \cos \pi x)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& -\pi (\sin \pi x + \cos \pi y)
\end{eqnarray}
$$

![with-rot-2](https://gist.github.com/assets/13412823/d0c84079-4584-46ba-a88b-b03a3873a2d7)

> $$
\begin{eqnarray}
    (v_x, v_y) &=& (0, x^2)
    \\ \\
    (\nabla \times \boldsymbol{v})_z &=& 2x-0 = 2x
\end{eqnarray}
$$

![with-rot-3](https://gist.github.com/assets/13412823/314fa568-30f2-4833-9f6e-cb8ab164d4d7)


