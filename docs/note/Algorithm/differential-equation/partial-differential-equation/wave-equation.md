---
title: 波動方程式
title-en: wave equation
---
# 問題設定

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ の波動方程式

$$
\cfrac{\partial^2 u}{\partial t^2} = c \cfrac{\partial^2 u}{\partial x^2}
\qquad (c = \mathrm{const.} \gt 0)
\tag{1}
$$

を数値的に解きたい。


# 理論

## 1次元空間の波動方程式

### 漸化式

- 座標空間に微小な間隔 $\Delta x$ で格子点 $x_0, \cdots, x_M$ を取る
    - $x_{m+1} = x_m + \Delta x$
- 時間ステップを微小な間隔 $\Delta t$ 単位で進める
    - $t_{n+1} = t_n + \Delta t$

#### 漸化式の導出

$u(x, t+\Delta t), u(x, t-\Delta t)$ をテイラー展開すると

$$
\begin{eqnarray}
    u(x, t+\Delta t) &=&
    u(x,t) + \cfrac{\partial u}{\partial t} \Delta t
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial t^2} (\Delta t)^2
    + \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial t^3} (\Delta t)^3
    + \cdots
    \\
    u(x, t-\Delta t) &=& u(x,t) - \cfrac{\partial u}{\partial t} \Delta t
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial t^2} (\Delta t)^2
    - \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial t^3} (\Delta t)^3
    + \cdots
\end{eqnarray}
$$

2式の和を取って整理すると

$$
\cfrac{\partial^2 u}{\partial t^2} = \cfrac{u(x, t+\Delta t) - 2u(x,t) + u(x, t-\Delta t)}{(\Delta t)^2}
\tag{2}
$$

同様に $x$ についても微分を考えれば

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
- u(x, t-\Delta t) +
\alpha u(x+\Delta x, t) +
(2-2\alpha) u(x, t) +
\alpha u(x-\Delta x, t)
\qquad \left( \alpha := \cfrac{c (\Delta t)^2}{(\Delta x)^2} \right)
\tag{4}
$$

ここで $x=x_m,\,t=t_n$ とおけば、$u(x_m, t_n)$ の漸化式は以下の式で表せる。

$$
u(x_m, t_{n+1})
\simeq
-u(x_m, t_{n-1}) +
\alpha u(x_{m+1},t_n) +
(2-2\alpha) u(x_m,t_n) +
\alpha u(x_{m-1},t_n)
\tag{5}
$$

時刻 $t_n$ における座標 $x_m$ の $u$ の値 $u(x_m, t_n)$ を $U_n^m$ と簡略化して表すと、

$$
U_{n+1}^m
\simeq
- U_{n-1}^m +
\alpha U_n^{m+1} +
(2-2\alpha)U_n^m +
\alpha U_n^{m-1}
\tag{6}
$$


# 実装

{% gist a38013791e705b0b314af9b946bdc35f ~PartialDifferentialEquationSolver.py %}

{% gist a38013791e705b0b314af9b946bdc35f ~wave-fixed.py %}

![partial-differential-eq](https://gist.github.com/assets/13412823/fbcdcf63-223b-489f-b7e3-7b93f98ae547)

{% gist a38013791e705b0b314af9b946bdc35f ~wave-free.py %}

![partial-differential-eq](https://gist.github.com/assets/13412823/6bac4e92-b17c-4a88-872d-bb23185a54d6)

