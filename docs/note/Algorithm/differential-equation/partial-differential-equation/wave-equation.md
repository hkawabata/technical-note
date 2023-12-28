---
title: 波動方程式
title-en: wave equation
---
# 問題設定

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ の波動方程式

$$
\cfrac{\partial^2 u}{\partial t^2} = c^2 \cfrac{\partial^2 u}{\partial x^2}
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
\cfrac{\partial^2 u}{\partial t^2} \simeq \cfrac{u(x, t+\Delta t) - 2u(x,t) + u(x, t-\Delta t)}{(\Delta t)^2}
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
\qquad \left( \alpha := \cfrac{c^2 (\Delta t)^2}{(\Delta x)^2} \right)
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


### 計算の安定性条件の導出

漸化式 $(5)(6)$ による繰り返し計算が発散せず安定するための条件を調べる。

座標 $x$ に対して波数 $k$ を導入し、$u(x, t)$ にフーリエ変換を適用すると、

$$
\begin{eqnarray}
    u(x,t) &=& \int_{-\infty}^\infty A(k,t) e^{ikx} dk
    \tag{7}
    \\
    A(k,t) &=& \cfrac{1}{2\pi} \int_{-\infty}^\infty u(x,t) e^{-ikx} dx
\end{eqnarray}
$$

計算が安定するには、全ての波数 $k$ に関して、時間 $t$ とともに振幅 $A(k,t)$ が発散しなければ良い。すなわち、任意の $k$ に対して以下が成り立つ必要がある。

$$
\left\vert \cfrac{A(k,t+\Delta t)}{A(k,t)} \right\vert \le 1
\qquad \Longleftrightarrow \qquad
-1 \le \cfrac{A(k,t+\Delta t)}{A(k,t)} \le 1
\tag{8}
$$

$(7)$ を $(2),(3)$ 式に代入すると、

$$
\begin{eqnarray}
    \cfrac{\partial^2 u}{\partial t^2}
    &\simeq&
    \cfrac{u(x, t+\Delta t) - 2u(x,t) + u(x, t-\Delta t)}{(\Delta t)^2}
    \\ &=&
    \cfrac{1}{(\Delta t)^2}
    \int_{-\infty}^\infty (A(k,t+\Delta t) - 2A(k,t) + A(k,t-\Delta t)) e^{ikx} dk
    \\
    \\
    \cfrac{\partial^2 u}{\partial x^2}
    &\simeq&
    \cfrac{u(x+\Delta x, t) - 2u(x,t) + u(x-\Delta x, t)}{(\Delta x)^2}
    \\ &=&
    \cfrac{1}{(\Delta x)^2}
    \int_{-\infty}^\infty A(k,t)\left(
        e^{ik(x+\Delta x)} - 2 e^{ikx} + e^{ik(x-\Delta x)}
    \right) dk
    \\ &=&
    \cfrac{1}{(\Delta x)^2}
    \int_{-\infty}^\infty A(k,t) e^{ikx} \left(
        e^{ik\Delta x} - 2 + e^{-ik\Delta x}
    \right) dk
    \\ &=&
    \cfrac{2}{(\Delta x)^2}
    \int_{-\infty}^\infty A(k,t) e^{ikx} \left(
        \cos k\Delta x - 1
    \right) dk
    \\ &=&
    \cfrac{-4}{(\Delta x)^2}
    \int_{-\infty}^\infty A(k,t) e^{ikx} \sin^2 \cfrac{k\Delta x}{2} dk
\end{eqnarray}
$$

これらを元の拡散方程式 $(1)$ に代入すると、

$$
\int_{-\infty}^\infty (A(k,t+\Delta t) - 2A(k,t) + A(k,t-\Delta t)) e^{ikx} dk
\simeq
- \int_{-\infty}^\infty A(k,t) e^{ikx} \cfrac{4 c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2} dk
$$

任意の波数 $k$ でこの式が成り立つためには、

$$
(A(k,t+\Delta t) - 2A(k,t) + A(k,t-\Delta t)) e^{ikx}
\simeq
- A(k,t) e^{ikx} \cfrac{4 c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2}
$$

よって

$$
\cfrac{A(k,t+\Delta t)}{A(k,t)} - 2 + \cfrac{A(k,t-\Delta t)}{A(k,t)}
\simeq
- \cfrac{4 c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2}
$$

十分小さい $\Delta t$ に関して $\mu := \cfrac{A(k,t+\Delta t)}{A(k,t)} \simeq \cfrac{A(k,t)}{A(k,t-\Delta t)}$ が成り立つとすれば、

$$
\mu - 2 + \cfrac{1}{\mu}
\simeq
- \cfrac{4 c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2}
$$

ここで

$$
r := \cfrac{c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2}
$$

とおけば

$$
\mu^2 - 2(1-2r)\mu + 1 = 0
$$

これを $\mu$ について解けば、

$$
\begin{eqnarray}
    \mu &\simeq& 1-2r
    \pm
    \sqrt{
        (1-2r)^2- 1
    }
    \\ &=&
    1-2r \pm 2 \sqrt{r^2-r}
\end{eqnarray}
$$

$(i)$ $1 \lt r$ の場合、ルートの中身は正となり、$\mu$ は実数。このとき、

$$
\vert \mu \vert^2 = 1 \mp (2r-1) \sqrt{r^2-r}
$$

$1\lt r$ よりプラス符号の $\vert \mu \vert^2$ は常に1より大きくなってしまい、$(8)$ を満たさないので不安定。

$(ii)$ $r \le 1$ の場合、ルートの中身はゼロまたは負となるので、

$$
\mu = (1-2r) \pm 2i \sqrt{r-r^2}
$$

このとき

$$
\vert \mu \vert^2 = (1-2r)^2 + 4(r-r^2) = 1
$$

となるので、どんな $r$ の値であっても常に $(8)$ を満たす。

以上 $(i)(ii)$ より、計算が安定するために満たすべき式は

$$
r = \cfrac{c^2 (\Delta t)^2}{(\Delta x)^2} \sin^2 \cfrac{k\Delta x}{2} \le 1
$$

と書き換えられる。  
任意の $k$ について考えているから、$0 \le \sin^2 (k\Delta x/2) \le 1$ の取りうる値全てついてこの不等式が成り立つ必要がある。したがって、

$$
\cfrac{c^2 (\Delta t)^2}{(\Delta x)^2} \le 1
$$

$c, \Delta x, \Delta t$ は全て正であるから、

$$
\cfrac{c \Delta t}{\Delta x} \le 1
\tag{9}
$$

これが求める安定性条件となる。


# 実装

## 境界が固定端

{% gist a38013791e705b0b314af9b946bdc35f ~PartialDifferentialEquationSolver.py %}

{% gist a38013791e705b0b314af9b946bdc35f ~WaveEquationSolverFixedEnd.py %}

```python
solver = WaveEquationSolverFixedEnd(c=0.3)
solver.solve(x_min=0, x_max=10.0, dx=0.1, dt=0.01, n_steps=10000)
solver.draw_result_animation(plot_interval=100, ani_interval=100)
solver.draw_result_image(interval=1000)
```

![partial-differential-eq](https://gist.github.com/assets/13412823/fbcdcf63-223b-489f-b7e3-7b93f98ae547)

## 境界が自由端

{% gist a38013791e705b0b314af9b946bdc35f ~WaveEquationSolverFreeEnd.py %}

```python
solver = WaveEquationSolverFreeEnd(c=0.3)
solver.solve(x_min=0, x_max=10.0, dx=0.1, dt=0.01, n_steps=10000)
solver.draw_result_animation(plot_interval=100, ani_interval=100)
solver.draw_result_image(interval=1000)
```

![partial-differential-eq](https://gist.github.com/assets/13412823/6bac4e92-b17c-4a88-872d-bb23185a54d6)

