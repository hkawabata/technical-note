---
title: 波動方程式
title-en: wave equation
---
# 問題設定

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ の偏微分方程式

$$
\cfrac{\partial^2 u}{\partial t^2} = c \cfrac{\partial^2 u}{\partial x^2}
\qquad (c = \mathrm{const.} \gt 0)
\tag{1}
$$

を数値的に解きたい。


# 理論

## 1次元空間の波動方程式

### 漸化式

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


{% gist a38013791e705b0b314af9b946bdc35f ~PartialDifferentialEquationSolver.py %}

```python
class WaveEquationSolver(PartialDifferentialEquationSolver):
    def __init__(self, c):
        """
        波動方程式 d^2 u/dt^2 = c * d^2 u / dx^2
        c : 波動方程式の右辺の係数
        """
        self.c = c
    
    def u0(self):
        """座標 x から u(x,t) の初期値 u(x,0) を計算"""
        mu = 3.0
        sigma = 1.0
        res = np.exp(-(self.x-mu)**2/sigma**2)
        res[0], res[-1] = 0, 0  # 境界の値はゼロで固定（ディリクレ境界条件）
        return res
    
    def update_U(self, i):
        """i ステップ目の u(x,t) を計算"""
        if i == 1:
            self.U[i] = self.U[i-1]
        else:
            alpha = self.c * self.dt**2 / self.dx**2
            u_in = alpha * (self.U[i-1][:-2] + self.U[i-1][2:])
            u_out = 2 * alpha * self.U[i-1][1:-1]
            self.U[i][1:-1] = 2*self.U[i-1][1:-1] - self.U[i-2][1:-1] + u_in - u_out
            # 両端 U[i][0], U[i][-1] は初期値ゼロのまま更新しない（ディリクレ境界条件）

solver = WaveEquationSolver(c=0.1)
solver.solve(x_min=0, x_max=10.0, dx=0.1, dt=0.01, n_steps=10000)
solver.draw_result_animation(plot_interval=100, ani_interval=100)
solver.draw_result_image(interval=1000)
```

![partial-differential-eq](https://gist.github.com/assets/13412823/fbcdcf63-223b-489f-b7e3-7b93f98ae547)
