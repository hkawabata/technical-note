---
title: ラグランジュの未定乗数法
---

# ラグランジュの未定乗数法とは

束縛条件下で関数の極値を求めるための手法。

## ラグランジュの未定乗数法：等式制約

### 定理

$$n$$ 変数 $$\boldsymbol{x} = (x_1, \cdots, x_n)$$ の関数 $$f(\boldsymbol{x})$$ に関して、束縛条件 $$g(\boldsymbol{x}) = 0$$ が課されているとする。  
**ラグランジアン** $$L(\boldsymbol{x}, \lambda)$$ を

$$L(\boldsymbol{x}, \lambda) \equiv f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$

で定義する。  
条件 $$g(\boldsymbol{x}) = 0$$ 下での $$f(\boldsymbol{x})$$ の極値は $$\boldsymbol{x}, \lambda$$ に関する連立方程式

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L &= 0 \\
\cfrac{\partial L}{\partial \lambda} &= 0
\end{cases}
$$

を解くことで得られる（$$\nabla_{\boldsymbol{x}} = \frac{\partial}{\partial \boldsymbol{x}} = (\frac{\partial}{\partial x_1}, \cdots, \frac{\partial}{\partial x_n})$$）。  
最後の式は束縛条件 $$g(\boldsymbol{x}) = 0$$ と同値。

$$m$$ 個の束縛条件 $$g_i(\boldsymbol{x}) = 0$$（$$i = 1, \cdots, m$$）が存在する場合にも拡張でき、未定定数 $$\boldsymbol{\lambda} = (\lambda_1, \cdots, \lambda_m)$$ を用いて

$$
L(\boldsymbol{x}, \boldsymbol{\lambda}) \equiv f(\boldsymbol{x}) - \displaystyle \sum_{i=1}^m \lambda_i g_i(\boldsymbol{x})
$$

と置き、

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L &= 0 \\
\nabla_{\boldsymbol{\lambda}} L &= 0
\end{cases}
$$

を解けば良い（$$\nabla_{\boldsymbol{\lambda}} = \frac{\partial}{\partial \boldsymbol{\lambda}} = (\frac{\partial}{\partial \lambda_1}, \cdots, \frac{\partial}{\partial \lambda_m})$$）。


### 直感的な理解

方程式 $$f(\boldsymbol{x}) = C$$（$$C$$ は定数）は、$$f(\boldsymbol{x})$$ の等高線を表す。  
説明のため2次元空間を想定し、$$f(\boldsymbol{x}) = f(x, y)$$ は極大値を持つとする。

下図のように、様々な $$C$$ の値に対して等高線を描いてみる。

![Unknown-2](https://user-images.githubusercontent.com/13412823/78782841-9a332d80-79dd-11ea-9bb4-a72dbb65cb15.png)

- $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点を持つ場合、それよりも $$C$$ が大きい領域（図では楕円の内側）に、$$g(x, y) = 0$$ と交わるあるいは接する別の等高線が存在する。
- $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点も接点も持たない場合、制約条件を満たす $$x$$, $$y$$ が等高線上に存在しない

以上により、$$f(x, y)$$ が極大値をとり得るのは $$f(x, y) = C$$ と $$g(x, y) = 0$$ が接点を持つ場合であり、極大値を与えるのはその時の接点。

曲線 $$f(x, y) = C$$, $$g(x, y) = 0$$ の接点では2曲線の接線が平行（傾きが等しい）。  
それぞれの接線ベクトル $$\left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$, $$\left( \frac{\partial g}{\partial x}, \frac{\partial g}{\partial y} \right)$$ が定数倍の関係にあれば良いから、

$$
\left( \cfrac{\partial f}{\partial x}, \cfrac{\partial f}{\partial y} \right) = \lambda \left( \cfrac{\partial g}{\partial x}, \cfrac{\partial g}{\partial y} \right)
$$

したがって、

$$
\nabla_{\boldsymbol{x}} \left( f - \lambda g \right) = 0
$$

これと元の制約条件 $$g(x, y) = 0$$ を合わせれば、定理の連立方程式を得る。


> **【NOTE】「接点 = 最大値 / 最小値」ではない**
>
> $$f(\boldsymbol{x}) = C$$ と $$g(\boldsymbol{x}) = 0$$ の接点全てが最大値 / 最小値を与えるわけではない。
>
> 下図は $$f(x, y) = (x-1)^2 + (y-2)^2$$, $$g(x, y) = x^2 - y$$ の例。  
> ラグランジュの未定乗数法による連立方程式の解として3つの接点  
> $$(x, y) = (-1, 1), (\frac{1-\sqrt{3}}{2}, \frac{2-\sqrt{3}}{2}), (\frac{1+\sqrt{3}}{2}, \frac{2+\sqrt{3}}{2})$$  
> が得られるが、$$f(x, y)$$ の最小値を与えるのは3番目の接点。
>
> ![Unknown-4](https://user-images.githubusercontent.com/13412823/78902403-b524a100-7ab4-11ea-8d6f-b5b3d87f6300.png)
>
> ![Unknown-5](https://user-images.githubusercontent.com/13412823/78902450-c1a8f980-7ab4-11ea-96fa-81fba33f28d0.png)



## ラグランジュの未定乗数法：不等式制約

### 定理：Karush-Kuhn-Tucker 条件（KKT 条件）

$$n$$ 変数 $$\boldsymbol{x} = (x_1, \cdots, x_n)$$ の関数 $$f(\boldsymbol{x})$$ に関して、束縛条件 $$g(\boldsymbol{x}) \le 0$$ が課されているとする。  
**ラグランジアン** $$L(\boldsymbol{x}, \lambda)$$ を

$$L(\boldsymbol{x}, \lambda) \equiv f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$

で定義する。  
条件 $$g(\boldsymbol{x}) \le 0$$ 下で $$f(\boldsymbol{x})$$ の極小値が存在するならば、極小値を取る $$\boldsymbol{x}$$ に対して以下を満たす $$\lambda$$ が存在する。

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L &= 0 \\
\lambda g(\boldsymbol{x}) &= 0 \\
g(\boldsymbol{x}) &\le 0 \\
\lambda &\ge 0
\end{cases}
$$

極大値の場合、最後の不等式が逆転する。

### 直感的な理解

等式制約では取りうる $$\boldsymbol{x}$$ が境界線上に限定されていたのが、境界で囲まれた領域内に広がった。

- 領域内に極値が存在するとき：領域の境界は関係がない。つまり、制約条件なしの問題に等しい（$$\lambda = 0$$）
- 領域内に極値が存在しないとき：極値は境界線上に存在する。解き方は（$$\lambda \neq 0$$）
