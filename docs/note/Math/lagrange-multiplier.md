---
title: ラグランジュの未定乗数法
---

# ラグランジュの未定乗数法とは

束縛条件下で関数の極値を求めるための手法。

## ラグランジュの未定乗数法：等式制約

### 定理

$$n$$ 変数 $$\boldsymbol{x} = (x_1, \cdots, x_n)$$ の関数 $$f(\boldsymbol{x})$$ に関して、条件 $$g(\boldsymbol{x}) = 0$$ が課されているとする。  
**ラグランジアン** $$L(\boldsymbol{x}, \lambda)$$ を

$$L(\boldsymbol{x}, \lambda) \equiv f(\boldsymbol{x}) - \lambda g(\boldsymbol{x})$$

で定義すると、条件 $$g(\boldsymbol{x}) = 0$$ 下での $$f(\boldsymbol{x})$$ の極値は（存在するならば）$$\boldsymbol{x}, \lambda$$ に関する連立方程式

$$
\begin{cases}
\nabla L &= 0 \\
\cfrac{\partial L}{\partial \lambda} &= 0
\end{cases}
$$

を解くことで得られる。


### 直感的な理解

方程式 $$f(\boldsymbol{x}) = C$$（$$C$$ は定数）は、$$f(\boldsymbol{x})$$ の等高線を表す。  
説明のため2次元空間を想定し、$$f(\boldsymbol{x}) = f(x, y)$$ は極大値を持つとする。

下図のように、様々な $$C$$ の値に対して等高線を描いてみる。

![Unknown-2](https://user-images.githubusercontent.com/13412823/78782841-9a332d80-79dd-11ea-9bb4-a72dbb65cb15.png)

- $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点を持つ場合、それよりも $$C$$ が大きい領域（図では楕円の内側）に、$$g(x, y) = 0$$ と交わるあるいは接する別の等高線が存在する。
- $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点も接点も持たない場合、制約条件を満たす $$x$$, $$y$$ が等高線上に存在しない

以上により、$$f(x, y)$$ が極大値をとり得るのは $$f(x, y) = C$$ と $$g(x, y) = 0$$ が交点を持たず接点を持つ場合であり、極大値を与えるのはその時の接点。

曲線 $$f(x, y) = C$$, $$g(x, y) = 0$$ の接点では2曲線の接線が平行（傾きが等しい）。  
それぞれの接線ベクトル $$\left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$, $$\left( \frac{\partial g}{\partial x}, \frac{\partial g}{\partial y} \right)$$ が定数倍の関係にあれば良いから、

$$
\left( \cfrac{\partial f}{\partial x}, \cfrac{\partial f}{\partial y} \right) = \lambda \left( \cfrac{\partial g}{\partial x}, \cfrac{\partial g}{\partial y} \right)
$$

したがって、

$$
\nabla \left( f - \lambda g \right) = 0
$$

これと元の制約条件 $$g(x, y) = 0$$ を合わせれば、定理の連立方程式を得る。


> **【NOTE】「接点 = 極値」ではない**
>
> $$f(\boldsymbol{x}) = C$$ と $$g(\boldsymbol{x}) = 0$$ の接点全てが極値を与えるわけではない。  
>
> 下図は $$f(x, y) = (x-1)^2 + (y-2)^2$$, $$g(x, y) = x^2 - y$$ の例。  
> ラグランジュの未定乗数法による連立方程式の解として3つの接点  
> $$(x, y) = (-1, 1), (\frac{1+\sqrt{3}}{2}, \frac{2+\sqrt{3}}{2}), (\frac{1-\sqrt{3}}{2}, \frac{2-\sqrt{3}}{2})$$  
> が得られるが、$$f(x, y)$$ の極大値を与えるのは2番目の接点のみ。
>
> ![Unknown-3](https://user-images.githubusercontent.com/13412823/78782838-98696a00-79dd-11ea-8186-4feb9527e242.png)



## ラグランジュの未定乗数法：不等式制約
