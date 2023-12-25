---
title: 拡散方程式
title-en: diffusion equation
---
# 問題設定

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ の拡散方程式

$$
\cfrac{\partial u}{\partial t} = \kappa \cfrac{\partial^2 u}{\partial x^2}
\qquad (\kappa = \mathrm{const.})
\tag{1}
$$

を数値的に解きたい。


# 理論

## 1次元空間の拡散方程式

### 漸化式

#### 漸化式の導出

$(1)$ は時間 $t$ に関する1階微分、空間 $x$ に関する2階微分を含む。  
したがって、解を一意に決定するためには、
- 時間に関する条件1つ（初期条件）
- 空間に関する条件2つ（境界条件）

が必要。

- 座標空間に微小な間隔 $\Delta x$ で格子点 $x_0, \cdots, x_M$ を取る
    - $x_{m+1} = x_m + \Delta x$
- 時間ステップを微小な間隔 $\Delta t$ 単位で進める
    - $t_{n+1} = t_n + \Delta t$

という前提のもと、差分法により漸化式を求める。

まず $t$ による微分を考える。$u(x, t+\Delta t)$ をテイラー展開すると

$$
\begin{eqnarray}
    u(x, t+\Delta t)
    &=&
    u(x,t) + \cfrac{\partial u}{\partial t} \Delta t
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial t^2} (\Delta t)^2
    + \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial t^3} (\Delta t)^3
    + \cdots
    \\ &=&
    u(x,t) + \cfrac{\partial u}{\partial t} \Delta t + O\left( (\Delta t)^2 \right)
\end{eqnarray}
$$

よって

$$
\cfrac{\partial u}{\partial t} \simeq \cfrac{u(x, t+\Delta t) - u(x, t)}{\Delta t}
\tag{2}
$$


次に $x$ による微分を考える。$u(x+\Delta x, t), u(x-\Delta x, t)$ をテイラー展開すると

$$
\begin{eqnarray}
    u(x+\Delta x, t) &=&
    u(x,t) + \cfrac{\partial u}{\partial x} \Delta x
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial x^2} (\Delta x)^2
    + \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial x^3} (\Delta x)^3
    + \cdots
    \\
    u(x-\Delta x, t) &=& u(x,t) - \cfrac{\partial u}{\partial x} \Delta x
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial x^2} (\Delta x)^2
    - \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial x^3} (\Delta x)^3
    + \cdots
\end{eqnarray}
$$

2式の和を取れば、

$$
u(x+\Delta x, t) + u(x-\Delta x, t)
=
2u(x,t) + \cfrac{\partial^2 u}{\partial x^2} (\Delta x)^2
+ O\left( (\Delta x)^4 \right)
$$

よって

$$
\cfrac{\partial^2 u}{\partial x^2}
\simeq
\cfrac{u(x+\Delta x, t) - 2u(x,t) + u(x-\Delta x, t)}{(\Delta x)^2}
\tag{3}
$$

$(2),(3)$ を $(1)$ に代入して整理すると、

$$
u(x, t+\Delta t)
\simeq
(1-2\alpha)u(x, t) +
\alpha u(x+\Delta x, t) +
\alpha u(x-\Delta x, t)
\qquad \left( \alpha := \cfrac{\kappa \Delta t}{(\Delta x)^2} \right)
\tag{4}
$$

ここで $x=x_m,\,t=t_n$ とおけば、$u(x_m, t_n)$ の漸化式は以下の式で表せる。

$$
u(x_m, t_{n+1})
\simeq
(1-2\alpha) u(x_m,t_n) +
\alpha (u(x_{m+1},t_n) + u(x_{m-1},t_n))
\tag{5}
$$

時刻 $t_n$ における座標 $x_m$ の $u$ の値 $u(x_m, t_n)$ を $U_n^m$ と簡略化して表すと、

$$
U_{n+1}^m
\simeq
(1-2\alpha)U_n^m +
\alpha (U_n^{m+1} + U_n^{m-1})
\tag{6}
$$

この式は、「次の時刻 $t_{n+1}$ における位置 $x_m$ での $u(x,t)$ の値を知るためには、現在時刻 $t_n$ の同じ位置の $u(x,t)$ の値、および両隣 $x_{m+1},x_{m-1}$ の $u(x,t)$ の値が分かれば良い」ことを示している。  
→ ある位置の $u(x,t)$ を計算するために両隣の情報を使うので、解きたい領域の境界である $x_0,x_M$ ではこの漸化式は適用できない（片方しか隣が存在しないため）。  
→ 両端 $x_0, x_M$ おける境界条件が必要。


#### 漸化式の物理的な解釈

漸化式 $(5)$ の右辺の解釈は以下の通り。

- 第1項 $(1-2\alpha) u(x_m,t_n)$
    - 元々格子点 $x_m$ に存在した物理量 $u(x_m, t_n)$ から、両隣の格子点 $x_{m-1},x_{m+1}$ それぞれへ流れ出す流出量 $\alpha u(x_m, t_n)$ を引いたもの
- 第2項 $\alpha (u(x_{m+1},t_n) + u(x_{m-1},t_n))$
    - 隣接する格子点 $x_{m+1}, x_{m-1}$ から $x_m$ へ流れ込んでくる流入量

よって、拡散方程式の漸化式の物理的な意味は以下のように解釈できる。
- 各格子点が今現在持っている物理量 $u$ が、時間と共に周囲へ流れ出す
- 流出する量は、現在の物理量 $u$ の値に比例する

また上の解釈から、$\alpha = \kappa \Delta t / (\Delta x)^2$ は1ステップあたりの流入量・流出量の大きさを表すパラメータであり、

- $\Delta t$ を大きくすると $\alpha$ も大きくなる：1ステップで長い時間が経つので流量も大きくなる
- $\Delta x$ を大きくすると $\alpha$ は小さくなる：格子点間の距離が長くなるので時間をかけないと隣の格子点まで流れない


### 境界条件の設定

領域の両端 $x_0, x_M$ における境界条件を設定する。

#### ディリクレ境界条件

境界における $u(x,t)$ の値が一定である場合に適用する。

$$
u(x_0) = \alpha = \mathrm{const.}, \quad u(x_M) = \beta = \mathrm{const.}
$$

例：
- 熱伝導において外気温が一定である場合
    - 気温 $u(x, t)$
    - $u(x_0,t) = u(x_M,t) = T = \mathrm{const.}$

（詳細は[ディリクレ境界条件](../../../Math/calculus/differential-equation/boundary-condition/dirichlet-boundary-condition.md)を参照）

#### ノイマン境界条件

境界における勾配 $\cfrac{\partial u}{\partial x}$ の値が一定である場合に適用する。

$$
\cfrac{\partial u}{\partial x} (x_0, t) = \alpha = \mathrm{const.}, \quad
\cfrac{\partial u}{\partial x} (x_M, t) = \beta = \mathrm{const.}
$$

例：
- 領域外と物理量のやりとりがない場合
    - $\cfrac{\partial u}{\partial x} (x_0, t) = \cfrac{\partial u}{\partial x} (x_M, t) = 0$

（詳細は[ノイマン境界条件](../../../Math/calculus/differential-equation/boundary-condition/neumann-boundary-condition.md)を参照）


## 2次元以上の空間の拡散方程式

2次元空間の場合を考える。

$$
\cfrac{\partial u}{\partial t} = \kappa \left(
    \cfrac{\partial^2 u}{\partial x^2} +
    \cfrac{\partial^2 u}{\partial y^2}
\right)
\qquad (\kappa = \mathrm{const.})
$$
1次元のときと同様に計算して、

$$
\begin{eqnarray}
    \cfrac{\partial u}{\partial t} &\simeq& \cfrac{u(x, y, t+\Delta t) - u(x, y, t)}{\Delta t}
    \\
    \cfrac{\partial^2 u}{\partial x^2} &\simeq&
    \cfrac{u(x+\Delta x, y, t) - 2u(x,y,t) + u(x-\Delta x, y, t)}{(\Delta x)^2}
    \\
    \cfrac{\partial^2 u}{\partial y^2} &\simeq&
    \cfrac{u(x, y+\Delta y, t) - 2u(x,y,t) + u(x, y-\Delta y, t)}{(\Delta y)^2}
\end{eqnarray}
$$

これらを元の拡散方程式に代入して整理すると、

$$
\begin{eqnarray}
    u(x, y, t+\Delta t)
    &\simeq&
    (1-2\alpha-2\beta) u(x, y, z, t) +
    \\ && + \alpha (u(x+\Delta x, y, t) + u(x-\Delta x, y, t))
    \\ && + \beta (u(x, y+\Delta y, t) + u(x, y-\Delta y, t))
    \\ \\
    (\alpha, \beta) &:=& \left( \cfrac{\kappa \Delta t}{(\Delta x)^2},\,\cfrac{\kappa \Delta t}{(\Delta y)^2} \right)
\end{eqnarray}
$$

漸化式で書けば、

$$
\begin{eqnarray}
    u(x_m, y_l, t_{n+1}) &=& (1-2\alpha-2\beta) u(x_m, y_l, t_n)
    \\ && + \alpha (u(x_{m+1}, y_l, t_n) + u(x_{m-1}, y_l, t_n))
    \\ && + \beta (u(x_m, y_{l+1}, t_n) + u(x_m, y_{l-1}, t_n))
\end{eqnarray}
$$

3次元空間の拡散方程式

$$
\cfrac{\partial u}{\partial t} = \kappa \left(
    \cfrac{\partial^2 u}{\partial x^2} +
    \cfrac{\partial^2 u}{\partial y^2} +
    \cfrac{\partial^2 u}{\partial z^2}
\right)
\qquad (\kappa = \mathrm{const.})
$$

も同様に、

$$
\begin{eqnarray}
    u(x_m, y_l, z_k, t_{n+1}) &=&
    (1-2\alpha-2\beta-2\gamma) u(x_m, y_l, t_n)
    \\ && + \alpha (u(x_{m+1}, y_l, z_k, t_n) + u(x_{m-1}, y_l, z_k, t_n))
    \\ && + \beta (u(x_m, y_{l+1}, z_k,  t_n) + u(x_m, y_{l-1}, z_k, t_n))
    \\ && + \gamma (u(x_m, y_l, z_{k+1}, t_n) + u(x_m, y_l, z_{k-1}, t_n))
    \\ \\
    (\alpha, \beta, \gamma) &:=& \left(
        \cfrac{\kappa \Delta t}{(\Delta x)^2},\,
        \cfrac{\kappa \Delta t}{(\Delta y)^2},\,
        \cfrac{\kappa \Delta t}{(\Delta z)^2}
    \right)
\end{eqnarray}
$$


# 実装

## ディリクレ境界条件の例

> $$
\cfrac{\partial u}{\partial t} = \kappa \cfrac{\partial^2 u}{\partial x^2}
\qquad (\kappa = 0.1)
$$
> 
> 定義域：
> 
> $$
x_\mathrm{min} \le x \le x_\mathrm{max}
$$
> 
> 初期条件：
> 
> $$
u(x,0) = e^{-(x-3)^2}
$$
> 
> 境界条件（ディリクレ条件）：
> 
> $$
u(x_\mathrm{min}, t) = 0,\quad u(_\mathrm{max}, t) = 0
$$

{% gist a38013791e705b0b314af9b946bdc35f ~PartialDifferentialEquationSolver.py %}

{% gist a38013791e705b0b314af9b946bdc35f ~diffusion-flux.py %}

![partial-differential-eq](https://gist.github.com/assets/13412823/a544c22c-1b9c-492b-b238-851703747501)

![diffusion-equation-flux](https://gist.github.com/assets/13412823/1576cd67-d3e1-4461-8e5d-6f72f76ea5f1)


## ノイマン境界条件の例

> $$
\cfrac{\partial u}{\partial t} = \kappa \cfrac{\partial^2 u}{\partial x^2}
\qquad (\kappa = 0.1)
$$
> 
> 定義域：
> 
> $$
x_\mathrm{min} \le x \le x_\mathrm{max}
$$
> 
> 初期条件：
> 
> $$
u(x,0) = e^{-(x-3)^2}
$$
> 
> 境界条件（ノイマン条件）：
> 
> $$
\cfrac{\partial u}{\partial x}(x_\mathrm{min}, t) = 0,\quad \cfrac{\partial u}{\partial x}(x_\mathrm{max}, t) = 0
$$

{% gist a38013791e705b0b314af9b946bdc35f ~diffusion-noflux.py %}

![partial-differential-eq](https://gist.github.com/assets/13412823/9896e3f2-7f45-457a-9bb6-5515566b24bf)

![diffusion-equation-noflux](https://gist.github.com/assets/13412823/472ffcfa-5d10-4511-9bcb-ce7ed0218efa)
