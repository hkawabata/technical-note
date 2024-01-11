---
title: ポアソン方程式の数値的解法
title-en: numerical solution for Poisson's equation
---
# 問題設定

$\rho(x,y)$ を既知の関数として、空間座標 $x,y$ を変数に持つ関数 $u(x,y)$ に関するポアソン方程式

$$
\cfrac{\partial^2 u}{\partial x^2} + \cfrac{\partial^2 u}{\partial y^2} = \rho(x, y)
\tag{1}
$$

を数値的に解きたい。


# 理論

## 2次元空間のポアソン方程式

### 連立方程式の導出

- 座標空間に微小な間隔 $\Delta x, \Delta y$ で格子点 $x_1, \cdots, x_{N_x}$ および $y_1, \cdots, y_{N_y}$ を取る
    - $x_{m+1} = x_m + \Delta x$
    - $y_{l+1} = y_l + \Delta y$

$u(x+\Delta x, y), u(x-\Delta x, y)$ をテイラー展開すると

$$
\begin{eqnarray}
    u(x+\Delta x, y) &=&
    u(x,y) + \cfrac{\partial u}{\partial x} \Delta x
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial x^2} (\Delta x)^2
    + \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial x^3} (\Delta x)^3
    + \cdots
    \\
    u(x-\Delta x, y) &=&
    u(x,y) - \cfrac{\partial u}{\partial x} \Delta x
    + \cfrac{1}{2!}\cfrac{\partial^2 u}{\partial x^2} (\Delta x)^2
    - \cfrac{1}{3!}\cfrac{\partial^3 u}{\partial x^3} (\Delta x)^3
    + \cdots
\end{eqnarray}
$$

2式の和を取って整理すると

$$
\cfrac{\partial^2 u}{\partial x^2} = \cfrac{u(x+\Delta x, y) - 2u(x,y) + u(x-\Delta x, y)}{(\Delta x)^2}
\tag{2}
$$

同様に $y$ についても微分を考えれば

$$
\cfrac{\partial^2 u}{\partial y^2} = \cfrac{u(x, y+\Delta y) - 2u(x,y) + u(x, y-\Delta y)}{(\Delta y)^2}
\tag{3}
$$

$(2),(3)$ を $(1)$ に代入して整理すると、

$$
\begin{eqnarray}
    &u(x, y) = \alpha (u(x+\Delta x, y) + u(x-\Delta x, y)) + \beta (u(x, y+\Delta y) + u(x, y-\Delta y)) + \gamma \rho(x, y)
    \\ \\
    &(\alpha, \beta, \gamma) := \left(
        \cfrac{(\Delta y)^2}{2((\Delta x)^2+(\Delta y)^2)},\,
        \cfrac{(\Delta x)^2}{2((\Delta x)^2+(\Delta y)^2)},\,
        \cfrac{(\Delta x)^2 (\Delta y)^2}{2((\Delta x)^2+(\Delta y)^2)}
    \right)
\end{eqnarray}
\tag{4}
$$

ここで $x=x_m,\,y=y_l$ とおけば、

$$
u(x_m, y_l) = \alpha (u(x_{m+1},y_l)+u(x_{m-1},y_l))
+ \beta (u(x_m,y_{l+1})+u(x_m,y_{l-1}))
+ \gamma \rho(x_m, y_l)
\tag{5}
$$

座標 $(x_m, y_l)$ の $u,\rho$ の値 $u(x_m, y_l), \rho(x_m, y_l)$ を $U_m^l, \rho_m^l$ と簡略化して表すと、

$$
U_m^l = \alpha (U_{m+1}^l + U_{m-1}^l) + \beta (U_m^{l+1} + U_m^{l-1}) + \gamma \rho_m^l
\tag{6}
$$

右辺の $\rho$ を除く項を見ると、係数の和 $\alpha + \alpha + \beta + \beta = 1$ であるから、この値は「**隣接する格子点の物理量の重みつき平均**」となっている。  
$\Delta x = \Delta y = h$ となるように格子点間隔を取ることにすれば、$\alpha = \beta = 1/4,\,\gamma=h^2/4$ であるから、

$$
U_m^l = \cfrac{U_{m+1}^l + U_{m-1}^l + U_m^{l+1} + U_m^{l-1}}{4} + \cfrac{h^2 \rho_m^l}{4}
\tag{7}
$$

右辺は隣接格子点4つの単純平均 + $\rho$ の項となる。  
少し変形して、

$$
-4U_m^l + U_{m+1}^l + U_{m-1}^l + U_m^{l+1} + U_m^{l-1} = -h^2 \rho_m^l
\tag{8}
$$

微分方程式を解くには、全ての格子点に関して $(7)$ 式を立てて、連立方程式として解けば良い。


### 境界条件の設定

式より明らかに、全ての格子点 $N_x N_y$ 個について $(7)$ を立てるためには、それぞれの格子点の **隣接する4点** が必要。  
しかし、考える領域の境界線上の格子点には、隣接格子点は2つまたは3つしか存在しない。  
そこで、下図の通り、考える領域内の格子点（図の青色）の1つ外側に仮想的な格子点（図のオレンジ色）を取り、これらの値を **境界条件** として与えることで、連立方程式が一意に定まる。

$$
\begin{cases}
    U_0^l = \mathrm{const.} \\ \\
    U_{Nx+1}^l = \mathrm{const.} \\ \\
    U_m^0 = \mathrm{const.} \\ \\
    U_m^{Ny+1} = \mathrm{const.}
\end{cases}
\tag{9}
$$

![poisson-eq-grid](https://gist.github.com/assets/13412823/43716ec3-41c1-42a5-84d4-bdf12b9944a5)


### 連立方程式の行列形式

未知変数 $U_m^l$ は合わせて $N_x N_y$ 個あるので、連立方程式 $(8)$ を行列形式

$$
A \boldsymbol{u} = \boldsymbol{v}
$$

$$
\boldsymbol{u} := \left( U_1^1, U_1^2, \cdots, U_{Nx}^{Ny} \right)^T,
\quad
\boldsymbol{v} := \left(v_1^1, v_1^2, \cdots, v_{Nx}^{Ny} \right)^T (v_m^l = \mathrm{const.})
$$

で書くと、係数行列 $A$ は $N_xN_y \times N_xN_y$ 正方行列。  
各格子点の方程式に出てくる変数はせいぜい5個（自身と上下左右の隣接格子点）なので、$A$ はほとんどの値がゼロの非常に疎な行列になる。

$(8)$ に関して、

- 境界条件を課しているので、$U_0^j, U_i^0, U_{Nx+1}^j, U_i^{Ny+1} = \mathrm{const.}$
- $U_m^l$ の係数は $-4$
- 境界条件による定数の場合を除き、$U_{m+1}^l,U_{m-1}^l,U_m^{l+1},U_m^{l-1}$ の係数は $1$

であるから、

$$
(8) \Longleftrightarrow \begin{cases}
    U_{m-1}^l & +U_m^{l-1} & -4U_m^l & +U_m^{l+1} & +U_{m+1}^l
    &=& -h^2 \rho_m^l &  &
    &\qquad (\mathrm{if}\quad 1 \lt m \lt N_x,\,1 \lt l \lt N_y)
    \\
    & +U_1^{l-1} & -4U_1^l & +U_1^{l+1} & +U_2^l
    &=& -h^2 \rho_1^l & -U_0^l &
    &\qquad (\mathrm{if}\quad m=1,\,1 \lt l \lt N_y)
    \\
    U_{Nx-1}^l & +U_{Nx}^{l-1} & -4U_{Nx}^l & +U_{Nx}^{l+1} &
    &=& -h^2 \rho_{Nx}^l & -U_{Nx+1}^l &
    &\qquad (\mathrm{if}\quad m=N_x,\,1 \lt l \lt N_y)
    \\
    U_{m-1}^1 &  & -4U_m^1 & +U_m^2 & +U_{m+1}^1
    &=& -h^2 \rho_m^1 & -U_m^0 &
    &\qquad (\mathrm{if}\quad 1 \lt m \lt N_x,\,l=1)
    \\
    U_{m-1}^{Ny} & +U_m^{Ny-1} & -4U_m^{Ny} &  & +U_{m+1}^{Ny}
    &=& -h^2 \rho_m^{Ny} & -U_m^{Ny+1} &
    &\qquad (\mathrm{if}\quad 1 \lt m \lt N_x,\,l=N_y)
    \\
    &  & -4U_1^1 & +U_1^2 & +U_2^1
    &=& -h^2 \rho_1^1 & -U_0^1 & -U_1^0
    &\qquad (\mathrm{if}\quad m=1,\,l=1)
    \\
    U_{Nx-1}^1 &  & -4U_{Nx}^1 & +U_{Nx}^2 & 
    &=& -h^2 \rho_{Nx}^1 & -U_{Nx}^0 & -U_{Nx+1}^1
    &\qquad (\mathrm{if}\quad m=N_x,\,l=1)
    \\
     & +U_1^{Ny-1} & -4U_1^{Ny} &  & +U_2^{Ny}
    &=& -h^2 \rho_1^{Ny} & -U_1^{Ny+1} & -U_0^{Ny}
    &\qquad (\mathrm{if}\quad m=1,\,l=N_y)
    \\
    U_{Nx-1}^{Ny} & +U_{Nx}^{Ny-1} & -4U_{Nx}^{Ny} &  &
    &=& -h^2 \rho_{Nx}^{Ny} & -U_{Nx+1}^{Ny} & -U_{Nx}^{Ny+1}
    &\qquad (\mathrm{if}\quad m=N_x,\,l=N_y)
    \\
\end{cases}
$$

行列形式で書くと、

$$
\left(\begin{array}{cccc|cccc|cccc|cccc}
    -4&1     &0     &0    &   1&0     &0     &0   &   & &&   &   & && \\
    1 &\ddots&\ddots&0    &   0&\ddots&\ddots&0   &   & &&   &   & && \\
    0 &\ddots&\ddots&1    &   0&\ddots&\ddots&0   &   &O&&   &   &O&& \\
    0 &0     &1     &-4   &   0&0     &0     &1   &   & &&   &   & && \\
    \hline
    1&0     &0     &0   &   -4&1     &0     &0    &&      &&   &   & && \\
    0&\ddots&\ddots&0   &   1 &\ddots&\ddots&0    &&\ddots&&   &   & && \\
    0&\ddots&\ddots&0   &   0 &\ddots&\ddots&1    &&      &&   &   &O&& \\
    0&0     &0     &1   &   0 &0     &1     &-4   &&      &&   &   & && \\
    \hline
    && &   &   &      &&   &   &      &&   &   1&0     &0     &0 \\
    &&O&   &   &\ddots&&   &   &\ddots&&   &   0&\ddots&\ddots&0 \\
    && &   &   &      &&   &   &      &&   &   0&\ddots&\ddots&0 \\
    && &   &   &      &&   &   &      &&   &   0&0     &0     &1\\
    \hline
    && &   &   && &   &   1&0     &0     &0   &   -4&1     &0     &0 \\
    &&O&   &   &&O&   &   0&\ddots&\ddots&0   &   1 &\ddots&\ddots&0 \\
    && &   &   && &   &   0&\ddots&\ddots&0   &   0 &\ddots&\ddots&1 \\
    && &   &   && &   &   0&0     &0     &1   &   0 &0     &1     &-4
\end{array}\right)
\begin{pmatrix}
    U_1^1 \\ U_1^2 \\ \vdots \\ U_1^{Ny-1} \\ U_1^{Ny} \\
    \hline
    U_2^1 \\ U_2^2 \\ \vdots \\ U_2^{Ny-1} \\ U_2^{Ny} \\
    \hline
    \\ \\ \vdots \\ \\ \\
    \hline
    U_{Nx}^1 \\ U_{Nx}^2 \\ \vdots \\ U_{Nx}^{Ny-1} \\ U_{Nx}^{Ny}
\end{pmatrix}
=
\begin{pmatrix}
    -h^2 \rho_1^1 & -U_0^1 & -U_1^0 \\
    -h^2 \rho_1^2 & -U_0^2 \\
    &\vdots \\
    -h^2 \rho_1^{Ny-1} & -U_0^{Ny-1} \\
    -h^2 \rho_1^{Ny} & -U_0^{Ny} & -U_1^{Ny+1} \\
    \hline
    -h^2 \rho_2^1 & -U_2^0 \\
    -h^2 \rho_2^2 \\
    &\vdots \\
    -h^2 \rho_2^{Ny-1} \\
    -h^2 \rho_2^{Ny} & -U_2^{Ny} \\
    \hline
    \\ \\ &\vdots \\ \\ \\
    \hline
    -h^2 \rho_{Nx}^1 & -U_{Nx+1}^1 & -U_{Nx}^0 \\
    -h^2 \rho_{Nx}^2 & -U_{Nx+1}^2 \\
    &\vdots \\
    -h^2 \rho_{Nx}^{Ny-1} & -U_{Nx+1}^{Ny-1} \\
    -h^2 \rho_{Nx}^{Ny} & -U_{Nx+1}^{Ny} & -U_{Nx}^{Ny+1}
\end{pmatrix}
$$

よって、係数行列 $A$ は
- 体格成分がす全て $0$ で、体格成分の隣接成分が全て $1$ の $N_y$ 次正方行列 $C_{Ny}$
- $Ny$ 次単位行列 $I_{Ny}$

$$
C_{Ny} = \begin{pmatrix}
    0 & 1      &  & O \\
    1  & 0     &  \ddots \\
       & \ddots & \ddots & 1 \\
    O  &        & 1 & 0
\end{pmatrix},
\qquad
I_{Ny} = \begin{pmatrix}
    1 &       &  & O \\
      & 1     &  \\
       &  & \ddots &  \\
    O  &        &  & 1
\end{pmatrix}
$$

を用いて

$$
A = \begin{pmatrix}
    C_{Ny}-4I_{Ny} & I_{Ny} &        & O      \\
    I_{Ny} & \ddots & \ddots &        \\
           & \ddots & \ddots & I_{Ny} \\
    O      &        & I_{Ny} & C_{Ny}-4I_{Ny}
\end{pmatrix}
$$

と表せる。


# 実装

{% gist a38013791e705b0b314af9b946bdc35f ~PoissonEquationSolver.py %}

```python
solver = PoissonEquationSolver()
solver.solve(x1_range=(2,4), x2_range=(0,1), dx=0.02)
solver.draw_result_heatmap()
solver.draw_result_3d()
```

| ヒートマップ | 3D |
| :-- | :-- |
| ![poisson-eq-heatmap](https://gist.github.com/assets/13412823/fd5e9383-eb18-4b8e-ac74-821044752dda) | ![poisson-eq-3d](https://gist.github.com/assets/13412823/6ec72c3f-dd59-43fa-a9de-24a33163d5ae) |
