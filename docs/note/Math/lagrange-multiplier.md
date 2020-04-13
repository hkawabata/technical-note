---
title: ラグランジュの未定乗数法
---

# ラグランジュの未定乗数法とは

束縛条件下で関数の極値を求めるための手法。


## ラグランジュの未定乗数法：等式制約

制約が等式 $$g(\boldsymbol{x}) = 0$$ で表現されるときの関数 $$f(\boldsymbol{x})$$ の極値を求めたい。

![Unknown](https://user-images.githubusercontent.com/13412823/78958628-98738200-7b23-11ea-838d-ab20bcb8ccd7.png)

![Unknown-1](https://user-images.githubusercontent.com/13412823/78958625-96112800-7b23-11ea-978d-f469dd43a3dc.png)


### 定理

$$n$$ 変数 $$\boldsymbol{x} = (x_1, \cdots, x_n)$$ の関数 $$f(\boldsymbol{x})$$ に関して、束縛条件 $$g(\boldsymbol{x}) = 0$$ が課されているとする。  
**ラグランジュ関数** $$L(\boldsymbol{x}, \lambda)$$ を

$$L(\boldsymbol{x}, \lambda) \equiv f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$

で定義する。  
条件 $$g(\boldsymbol{x}) = 0$$ 下での $$f(\boldsymbol{x})$$ の極値は $$\boldsymbol{x}, \lambda$$ に関する連立方程式

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L(\boldsymbol{x}, \lambda) &= 0 \\
g(\boldsymbol{x}) &= 0
\end{cases}
$$

を解くことで得られる（$$\nabla_{\boldsymbol{x}} = \frac{\partial}{\partial \boldsymbol{x}} = (\frac{\partial}{\partial x_1}, \cdots, \frac{\partial}{\partial x_n})$$）。  
最後の式は $$ \frac{\partial L}{\partial \lambda}(\boldsymbol{x}, \lambda) = 0 $$ と書くこともできる。

$$m$$ 個の束縛条件 $$g_i(\boldsymbol{x}) = 0$$（$$i = 1, \cdots, m$$）が存在する場合にも拡張でき、未定定数 $$\boldsymbol{\lambda} = (\lambda_1, \cdots, \lambda_m)$$ を用いて

$$
L(\boldsymbol{x}, \boldsymbol{\lambda}) \equiv f(\boldsymbol{x}) - \displaystyle \sum_{i=1}^m \lambda_i g_i(\boldsymbol{x})
$$

と置き、

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L(\boldsymbol{x}, \lambda) &= 0 \\
g_i(\boldsymbol{x}) &= 0 \ \ (i = 1, \cdots, m)
\end{cases}
$$

を解けば良い。


### 直感的な理解

方程式 $$f(\boldsymbol{x}) = C$$（$$C$$ は定数）は、$$f(\boldsymbol{x})$$ の等高線を表す。  
簡単のため2次元空間を想定し、$$f(\boldsymbol{x}) = f(x, y)$$ は上に凸であるとして最大値を求める（下に凸な場合でも考え方は同じ）。

下図のように、様々な $$C$$ の値に対して等高線を描いてみる。

![Unknown-2](https://user-images.githubusercontent.com/13412823/78782841-9a332d80-79dd-11ea-9bb4-a72dbb65cb15.png)

- 等高線 $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点を持つ場合、その等高線よりも $$C$$ が大きい領域（内側）に、$$g(x, y) = 0$$ と交わるあるいは接する別の等高線が存在する
- 等高線 $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点も接点も持たない場合、制約条件を満たす $$x$$, $$y$$ が等高線上に存在しないため不適

以上により、$$f(x, y)$$ が極大値をとり得るのは $$f(x, y) = C$$ と $$g(x, y) = 0$$ が接点を持つ場合であり、極大値を与えるのはその時の接点。

曲線 $$f(x, y) = C$$, $$g(x, y) = 0$$ の接点では、2曲線の接線が平行。したがって曲線の法線（勾配）も平行。  
それぞれの勾配 $$\left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$, $$\left( \frac{\partial g}{\partial x}, \frac{\partial g}{\partial y} \right)$$ が定数倍の関係にあれば良いから、

$$
\left( \cfrac{\partial f}{\partial x}, \cfrac{\partial f}{\partial y} \right) = \lambda \left( \cfrac{\partial g}{\partial x}, \cfrac{\partial g}{\partial y} \right)
$$

したがって、

$$
\nabla_{\boldsymbol{x}} \left( f - \lambda g \right) = 0
$$

これと元の制約条件 $$g(x, y) = 0$$ を合わせれば、上述の定理の連立方程式を得る。


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

制約が不等式 $$g(\boldsymbol{x}) \le 0$$ で表現されるときの関数 $$f(\boldsymbol{x})$$ の極値を求めたい。

### 定理：Karush-Kuhn-Tucker 条件（KKT 条件）

$$n$$ 変数 $$\boldsymbol{x} = (x_1, \cdots, x_n)$$ の関数 $$f(\boldsymbol{x})$$ に関して、束縛条件 $$g(\boldsymbol{x}) \le 0$$ が課されているとする。  
**ラグランジュ関数** $$L(\boldsymbol{x}, \lambda)$$ を

$$L(\boldsymbol{x}, \lambda) \equiv f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$

で定義する。  
条件 $$g(\boldsymbol{x}) \le 0$$ 下で $$f(\boldsymbol{x})$$ の極小値が存在するならば、極小値を与える $$\boldsymbol{x}$$ に対して以下を満たす $$\lambda$$ が存在する。

$$
\begin{cases}
\nabla_{\boldsymbol{x}} L &= 0 \\
\lambda g(\boldsymbol{x}) &= 0 \\
g(\boldsymbol{x}) &\le 0 \\
\lambda &\le 0
\end{cases}
$$

極大値の場合、最後の不等号が逆転する。


### 直感的な理解

等式制約では取りうる $$\boldsymbol{x}$$ が境界線上に限定されていたのが、境界で囲まれた領域内に広がった。

簡単のため2次元空間を想定し、$$f(\boldsymbol{x}) = f(x, y)$$ は下に凸であるとして最小値を考える（上に凸で最大値を求める場合も考え方は同じ）。

#### 1. 制約がないときの極値が実行可能領域の内側に存在する時

領域の境界は関係がなく、制約条件なしの問題に等しい（$$\lambda = 0$$）。

![Unknown-1](https://user-images.githubusercontent.com/13412823/78921807-73095880-7ad0-11ea-8d60-d8ce016ec5fb.png)

![Unknown-3](https://user-images.githubusercontent.com/13412823/78921812-73a1ef00-7ad0-11ea-9ad7-6c988daae932.png)


#### 2. 制約がないときの極値が実行可能領域の外側に存在する時

等式制約のときと同じく、極値は領域境界線上に存在し、$$f(x, y)$$ の等高線との接点で与えられる。  
領域の境界では $$g(x, y) = 0$$ が成り立つ。

![Unknown](https://user-images.githubusercontent.com/13412823/78921800-70a6fe80-7ad0-11ea-87e0-8cb8d659c8a3.png)

![Unknown-2](https://user-images.githubusercontent.com/13412823/78948862-ba114100-7b04-11ea-9d9c-5608725c2c28.png)

また、上図を見れば分かる通り、
- 境界の内側で $$g(x, y) \lt 0$$、領域境界で $$g(x, y) = 0$$ なので、$$g(x, y)$$ は境界近傍では内側に向かって凹んでいる
  - よって接点における $$g(x, y)$$ の勾配ベクトルは、領域から出ていく向き
- 仮定より、$$f(x, y)$$ は下に凸であり、制約なしの極小値は領域の外側に存在
  - よって接点における $$f(x, y)$$ の勾配ベクトルは、領域へ入っていく向き

以上により、**$$f(x, y)$$ と $$g(x, y)$$ の勾配は逆向き**：

$$
\left( \cfrac{\partial f}{\partial x}, \cfrac{\partial f}{\partial y} \right) = \lambda \left( \cfrac{\partial g}{\partial x}, \cfrac{\partial g}{\partial y} \right)
$$

$$\lambda \lt 0$$

> **【NOTE】**
>
> $$f(x, y)$$ が上に凸であるときの最大値を求める場合、接点における $$f(x, y)$$ の勾配ベクトルは領域から出ていく向きになる。  
> したがって、**$$f(x, y)$$ と $$g(x, y)$$ の勾配は同じ向き** なので、条件は $$\lambda \gt 0$$ となる。
>
> ![Unknown-3](https://user-images.githubusercontent.com/13412823/78948874-bed5f500-7b04-11ea-8635-8326300ef695.png)


#### まとめ

1, 2は以下の2条件にまとめられる。

- $$\lambda$$ または $$g(x, y)$$ がゼロ：$$\lambda g(x, y) = 0$$
- $$\lambda$$ はゼロまたは負：$$\lambda \le 0$$

これと元の制約 $$g(x, y) \le 0$$ を合わせて、上述の定理を得る。


### 双対問題

条件 $$g(\boldsymbol{x}) \le 0$$ の下で $$f(\boldsymbol{x})$$ 最小化問題を考える（最大化問題でも考え方は同じ）。

#### 目的関数の下限値

ラグランジュ関数 $$L(\boldsymbol{x}, \lambda) = f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$ を KKT 条件 $$\lambda \le 0$$ に関して最大化してみる。

- 実行可能領域（$$g(\boldsymbol{x}) \le 0$$）においては $$- \lambda g(\boldsymbol{x}) \le 0$$ なので、$$\lambda g(\boldsymbol{x}) = 0$$ で $$L(\boldsymbol{x}, \lambda)$$ 最大
- 実行可能領域外（$$g(\boldsymbol{x}) > 0$$）においては $$- \lambda g(\boldsymbol{x}) \ge 0$$ でありいくらでも大きくできる

よって

$$
\underset{\lambda \le 0}{\max} L(\boldsymbol{x}, \lambda) = \begin{cases}
f(\boldsymbol{x}) & {\rm if} \ g(\boldsymbol{x}) \le 0 \\
\infty & {\rm if} \ g(\boldsymbol{x}) > 0
\end{cases}
$$

となるから、両辺で $$\boldsymbol{x}$$ に関する最小値を取ると

$$
\underset{\boldsymbol{x}}{\min} \left( \underset{\lambda \le 0}{\max} L(\boldsymbol{x}, \lambda) \right) = \underset{\boldsymbol{x}}{\min} f(\boldsymbol{x})
$$

よって、

$$
\underset{\boldsymbol{x}}{\min} f(\boldsymbol{x})
= \underset{\boldsymbol{x}}{\min} \left( \underset{\lambda \le 0}{\max} L(\boldsymbol{x}, \lambda) \right)
\ge \underset{\lambda \le 0}{\max} \left( \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda) \right)
$$

したがって最後の式 $$\underset{\lambda \le 0}{\max} \left( \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda) \right)$$ は、目的関数 $$f(\boldsymbol{x})$$ の最小値の下限値を与えることが分かる。

> **【NOTE】「最大値の最小値」と「最小値の最大値」の関係**
>
> $$L(\boldsymbol{x}, \lambda) \ge \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda)$$
>
> は明らかなので、両辺で $$\lambda \le 0$$ における最大を取って、
>
> $$\underset{\lambda \le 0}{\max} L(\boldsymbol{x}, \lambda) \ge \underset{\lambda \le 0}{\max} \left( \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda) \right)$$
>
> 更に両辺で $$\boldsymbol{x}$$ に関する最小を取ると、右辺は既に $$\boldsymbol{x}$$ を含まない式であるから変わらず、
>
> $$\underset{\boldsymbol{x}}{\min} \left( \underset{\lambda \le 0}{\max} L(\boldsymbol{x}, \lambda) \right) \ge \underset{\lambda \le 0}{\max} \left( \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda) \right)$$
>
> を得る。


#### 双対関数と双対問題

前節最後の不等式に関して、多くの最適化問題においては統合が成立する（**強双対性**）。

$$
\underset{\boldsymbol{x}}{\min} f(\boldsymbol{x})
= \underset{\lambda \le 0}{\max} l(\lambda)
$$

$$\underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda)$$ の最大化問題を **ラグランジュ双対問題** と呼び、

$$
l(\lambda) \equiv \underset{\boldsymbol{x}}{\min} L(\boldsymbol{x}, \lambda)
$$

を **ラグランジュ双対関数** と呼ぶ。

最適化問題が強双対性を持つ場合、下の問題よりも双対問題を解く方が簡単な場合がある。

> **【NOTE】強双対性が成り立つ条件**
>
> 以下を満たせば強双対性が成り立つ（十分条件）。
>
> - 等式制約 $$h_i(\boldsymbol{x}) = 0$$ の左辺が全て線形関数
> - 不等式制約 $$g_i(\boldsymbol{x}) \le 0$$ の左辺が全て凸関数
> - 実行可能領域の内部に（$$g_i(\boldsymbol{x}) < 0$$）に、等式制約 $$h_i(\boldsymbol{x}) = 0$$ 満たす点 $$\boldsymbol{x}$$ が存在する（**スレーターの条件**）
