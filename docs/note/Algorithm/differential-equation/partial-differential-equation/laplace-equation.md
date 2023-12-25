---
title: ラプラス方程式
title-en: Laplace's equation
---
# 問題設定

空間座標 $x,y$ を変数に持つ関数 $u(x,y)$ のラプラス方程式

$$
\cfrac{\partial^2 u}{\partial x^2} + \cfrac{\partial^2 u}{\partial y^2} = 0
\tag{1}
$$

を数値的に解きたい。


# 理論

## 2次元空間のラプラス方程式

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
    &u(x, y) = \alpha (u(x+\Delta x, y) + u(x-\Delta x, y)) + \beta (u(x, y+\Delta y) + u(x, y-\Delta y))
    \\ \\
    &(\alpha, \beta) := \left(
        \cfrac{(\Delta y)^2}{2((\Delta x)^2+(\Delta y)^2)},\,
        \cfrac{(\Delta x)^2}{2((\Delta x)^2+(\Delta y)^2)}
    \right)
\end{eqnarray}
\tag{4}
$$

ここで $x=x_m,\,y=y_l$ とおけば、

$$
u(x_m, y_l) = \alpha (u(x_{m+1},y_l)+u(x_{m-1},y_l)) + \beta (u(x_m,y_{l+1})+u(x_m,y_{l-1}))
\tag{5}
$$

座標 $(x_m, y_l)$ の $u$ の値 $u(x_m, y_l)$ を $U_m^l$ と簡略化して表すと、

$$
U_m^l = \alpha (U_{m+1}^l + U_{m-1}^l) + \beta (U_m^{l+1} + U_m^{l-1})
\tag{6}
$$

右辺の係数の和 $\alpha + \alpha + \beta + \beta = 1$ であるから、この式は「**格子点の物理量が、それに隣接する格子点の物理量の重みつき平均で表される**」ことを示す。

$\Delta x = \Delta y$ となるように格子点間隔を取ることにすれば、$\alpha = \beta = 1/4$ であるから、

$$
U_m^l = \cfrac{U_{m+1}^l + U_{m-1}^l + U_m^{l+1} + U_m^{l-1}}{4}
\tag{7}
$$

となり、単純平均の式が得られる。  
微分方程式を解くには、全ての格子点に関して $(7)$ 式を立てて、連立方程式として解けば良い。

式より明らかに、全ての格子点 $N_x N_y$ 個について $(7)$ を立てるためには、それぞれの格子点の **隣接4点全ての値** が必要。  
したがって下図の通り、考える領域内の格子点（図の青色）の1つ外側に仮想的な格子点（図のオレンジ色）を取り、これらの値を **境界条件** として与えることで、連立方程式が一意に定まる。

![laplace-eq-grid](https://gist.github.com/assets/13412823/43716ec3-41c1-42a5-84d4-bdf12b9944a5)


```python
n_x, n_y = 4, 6
xx, yy = np.meshgrid(range(n_x+2), range(n_y+2))
x_inner, y_inner = xx[1:-1,1:-1].flatten(), yy[1:-1,1:-1].flatten()
x_boundary = np.concatenate([xx[0,1:-1], xx[1:-1,[0,-1]].flatten(), xx[-1,1:-1]])
y_boundary = np.concatenate([yy[0,1:-1], yy[1:-1,[0,-1]].flatten(), yy[-1,1:-1]])

plt.title(r'$N_x = {}, N_y = {}$'.format(n_x, n_y))
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.xlim([-2, n_x+3])
plt.ylim([-2, n_y+3])
plt.xticks(np.arange(-2, n_x+3))
plt.yticks(np.arange(-2, n_y+3))
plt.scatter(x_inner, y_inner, label='inner')
plt.scatter(x_boundary, y_boundary, label='boundary')
plt.grid()
plt.legend()
plt.show()
```

# 具体例

前節の図の例を考えてみる。
- $N_x = 4, N_y = 6$
- $\Delta x = \Delta y = 1$

ここに境界条件

$$
\begin{cases}
    u(0, y) &=& 1 \\
    u(5, y) &=& 2 \\
    u(x, 0) &=& 3 \\
    u(x, 7) &=& 4
\end{cases}
$$

を課す。  
$(x,y)=(1,1),(1,2),\cdots,(2,5),\cdots,(4,6)$  における $U_i^j$ に関して $(7)$ 式を立てると、

$$
\begin{cases}
    U_1^1 &=& \cfrac{U_2^1+U_0^1+U_1^2+U_1^0}{4} &=& \cfrac{U_2^1+1+U_1^2+3}{4} \\
    U_1^2 &=& \cfrac{U_2^2+U_0^2+U_1^3+U_1^1}{4} &=& \cfrac{U_2^2+1+U_1^3+U_1^1}{4} \\
    && \vdots && \\
    U_2^5 &=& \cfrac{U_3^5+U_1^5+U_2^6+U_2^4}{4} \\
    && \vdots && \\
    U_4^6 &=& \cfrac{U_5^6+U_3^6+U_4^7+U_4^5}{4} &=& \cfrac{2+U_3^6+4+U_4^5}{4} \\
\end{cases}
$$

これは $N_x \times N_y = 24$ 個の未知変数 $U_i^j$ に関する連立1次方程式となっている。  
未知の変数を左辺、定数を右辺にまとめて、

$$
\begin{cases}
    4U_1^1 - U_2^1 - U_1^2 &=& 4 \\
    4U_1^2 - U_2^2 - U_1^3 - U_1^1 &=& 1 \\
    &\vdots & \\
    4U_2^5 - U_3^5 - U_1^5 - U_2^6 - U_2^4 &=& 0 \\
    & \vdots & \\
    4U_4^6 - U_3^6 - U_4^5 &=& 6 \\
\end{cases}
$$

これを解くことで全ての格子点の $U_i^j$ が計算できる。


# 実装

> ラプラス方程式：
> 
> $$
\cfrac{\partial^2 u}{\partial x^2} + \cfrac{\partial^2 u}{\partial y^2} = 0
$$
> 
> 境界条件：
> 
> $$
\begin{cases}
    u(x_\mathrm{min}, y) &=& 0 \\
    u(x_\mathrm{max}, y) &=& 0 \\
    u(x, y_\mathrm{min}) &=& 0 \\
    u(x, y_\mathrm{max}) &=& 100
\end{cases}
$$

{% gist a38013791e705b0b314af9b946bdc35f ~LaplaceEquationSolver.py %}

| ヒートマップ | 3D |
| :-- | :-- |
| ![laplace-eq-heatmap](https://gist.github.com/assets/13412823/4a97c01d-4781-4e44-bc57-6cda278a1144) | ![laplace-eq-3d](https://gist.github.com/assets/13412823/a49d72e9-0b22-4a33-b963-481770ed596b) |



