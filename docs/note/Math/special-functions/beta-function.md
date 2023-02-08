---
title: ベータ関数
title-en: Beta Function
---

# ベータ関数とは

実部が正であるような複素数 $x, y$ に対して、以下の式で定義される関数。

$$
B(x, y) := \int_0^1 t^{x-1} (1-t)^{y-1} dt
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/216883259-d2c36397-d290-4958-a192-b103d28e4bfc.png)

（描画に使った Python コード）

```python
import numpy as np
from scipy import special
from matplotlib import pyplot as plt

x = np.arange(start=0.05, stop = 3.0, step=0.01)
y = np.arange(start=0.05, stop = 3.0, step=0.01)
x_grid, y_grid = np.meshgrid(x, y)
z = special.beta(x_grid, y_grid)

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(projection='3d') # 3D用の設定
ax.plot_surface(x_grid, y_grid, z, cmap='jet', alpha=0.6) # 曲面図
ax.contour(x_grid, y_grid, z, cmap='jet', offset=z.min()) # 等高線図
ax.set_xlabel('$y$') # x軸ラベル
ax.set_ylabel('$x$') # y軸ラベル
ax.set_zlabel('$B(x, y)$') # z軸ラベル
plt.show() # 描画
```

# ベータ関数の性質

## 特別な引数のときのベータ関数の値

> **【定理】**
> 
> $$
\begin{eqnarray}
	& B(1, 1) & = 1 \\
	& B\left( \cfrac{1}{2}, \cfrac{1}{2} \right) & = \pi
\end{eqnarray}
$$

**【証明】**

$$
\begin{eqnarray}
	B(1, 1)
	&=&
	\int_0^1 t^0 (1-t)^0 dt
	\\ &=&
	\int_0^1 1 dt
	\\ &=&
	[t]_{0}^{1}
	\\ &=&
	1
	\\
	B\left( \cfrac{1}{2}, \cfrac{1}{2} \right)
	&=&
	\int_0^1 t^{-1/2} (1-t)^{-1/2} dt
	\\ &=&
	\int_0^1 \cfrac{1}{\sqrt{ t(1-t) }} dt
	\\ &=&
	\int_0^1 \cfrac{1}{\sqrt{ \frac{1}{4} - (t-\frac{1}{2})^2 }} dt
	\\ &=&
	\int_{-\pi/2}^{\pi/2} \cfrac{1}{\sqrt{ \frac{1}{4} - \frac{1}{4} \sin^2 \theta }} \left( \cfrac{1}{2} \cos \theta d\theta \right)
	\qquad \left(
		t - \cfrac{1}{2} = \cfrac{1}{2} \sin \theta,
		\cfrac{dt}{d\theta} = \cfrac{1}{2} \cos \theta
	\right)
	\\ &=&
	\int_{-\pi/2}^{\pi/2} \cfrac{\cos \theta}{\sqrt{ 1 - \sin^2 \theta }} d\theta
	\\ &=&
	\int_{-\pi/2}^{\pi/2} 1 d\theta
	\\ &=&
	[\theta]_{-\pi/2}^{\pi/2}
	\\ &=&
	\cfrac{\pi}{2} - \left( - \cfrac{\pi}{2} \right)
	\\ &=&
	\pi
\end{eqnarray}
$$

## 対称性

> **【定理】**
> 
> $$
B(x, y) = B(y, x) \qquad (1)
$$

**【証明】**

$$
\begin{eqnarray}
	B(x, y) &=& \int_0^1 t^{x-1} (1-t)^{y-1} dt
	\\ &=&
	\int_1^0 (1-s)^{x-1} s^{y-1} (-ds) \qquad (s = 1 - t)
	\\ &=&
	\int_0^1 s^{y-1} (1-s)^{x-1} ds
	\\ &=&
	B(y, x)
\end{eqnarray}
$$

## +1だけ異なる場合のベータ関数

> **【定理】**
> 
> $$
\begin{eqnarray}
	B(x, y+1) &=& \cfrac{y}{x} B(x+1, y) & \qquad & (2) \\
	B(x, y+1) &=& \cfrac{y}{x+y} B(x, y) & \qquad & (3) \\
	B(x+1, y) &=& \cfrac{x}{x+y} B(x, y) & \qquad & (4)
\end{eqnarray}
$$

**【証明】**

まず $(2)$ を示す。

$$
\begin{eqnarray}
	B(x, y+1) &=& \int_0^1 t^{x-1} (1-t)^y dt
	\\ &=&
	\left[ \cfrac{1}{x} t^x (1-t)^y \right]_0^1 -
	\int_0^1 \cfrac{-y}{x} t^x (1-t)^{y-1} dt
	\\ &=&
	(0 - 0) + \cfrac{y}{x} \int_0^1 t^x (1-t)^{y-1} dt
	\\ &=&
	\cfrac{y}{x} B(x+1, y)
\end{eqnarray}
$$

次に $(3)$ を示す。

$$
\begin{eqnarray}
	B(x, y+1) &=&
	\int_0^1 t^{x-1} (1-t)^y dt
	\\ &=&
	\int_0^1 t^{x-1} (1-t)^{y-1} (1-t) dt
	\\ &=&
	\int_0^1 \left(
		t^{x-1} (1-t)^{y-1} \cdot 1 -
		t^{x-1} (1-t)^{y-1} \cdot t
	\right) dt
	\\ &=&
	\int_0^1 t^{x-1} (1-t)^{y-1} dt -
	\int_0^1 t^x (1-t)^{y-1} dt
	\\ &=&
	B(x, y) - B(x+1, y)
	\\ &=&
	B(x, y) - \cfrac{x}{y} B(x, y+1) \qquad (\mathrm{by}\ \ (2))
\end{eqnarray}
$$

最後の式の第二項を移行すれば、

$$
\cfrac{x + y}{y} B(x, y+1) = B(x, y)
$$

したがって

$$
B(x, y+1) = \cfrac{y}{x + y} B(x, y)
$$

最後に $(4)$ を示す。

$$
\begin{eqnarray}
	B(x+1, y) &=& \cfrac{x}{y} B(x, y+1) & \qquad & (\mathrm{by}\ \ (2))
	\\ &=&
	\cfrac{x}{y} \cfrac{y}{x+y} B(x, y) & \qquad & (\mathrm{by}\ \ (3))
	\\ &=&
	\cfrac{x}{x + y} B(x, y)
\end{eqnarray}
$$

## ガンマ関数との関係

> **【定理】** [ガンマ関数](gamma-function.md) $\Gamma(z)$ を用いて、ベータ関数を以下のように表せる。
> 
> $$
B(x, y) = \cfrac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)} \qquad (5)
$$

**【証明】**

（複雑なので省略）

## 三角関数の積分としての表現

> **【定理】** ベータ関数は三角関数の積分を使って以下の形式で表せる。
> 
> $$
B(x, y) = 2 \int_0^{\pi/2} \sin^{2x-1} \theta \cos^{2y-1} \theta d \theta
\qquad (6)
$$

**【証明】**

ベータ関数の積分範囲は $0 \le t \le 1$ なので、$t = \sin^2 \theta$ と置ける。  

- $t: 0 \to 1$ のとき $\theta : 0 \to \pi / 2$
- $1 - t = 1 - \sin^2 \theta = \cos^2 \theta$
- $dt/d\theta = 2 \sin \theta \cos \theta$

であるから、

$$
\begin{eqnarray}
	B(x, y) &=&
	\int_0^1 t^{x-1} (1-t)^{y-1} dt
	\\ &=&
	\int_0^{\pi/2} (\sin^2 \theta)^{x-1} (\cos^2 \theta)^{y-1}
	(2 \sin \theta \cos \theta d \theta)
	\\ &=&
	2 \int_0^{\pi/2} \sin^{2x-1} \theta \cos^{2y-1} \theta d \theta
\end{eqnarray}
$$

**【例】**

$$
\begin{eqnarray}
	\int_0^{\pi/2} \sin^3 \theta \cos \theta d \theta
	&=&
	\int_0^{\pi/2} \sin^{2 \cdot 2 - 1} \theta \cos^{2 \cdot 1 - 1} \theta d \theta
	\\ &=&
	\cfrac{1}{2} B (2, 1)
	\\ &=&
	\cfrac{1}{2} \cfrac{1}{1+1} B (1, 1)
	\\ &=&
	\cfrac{1}{2} \cdot \cfrac{1}{2} \cdot 1
	\\ &=&
	\cfrac{1}{4}
	\\
	\int_0^{\pi/2} \sin^2 \theta \cos^2 \theta d \theta
	&=&
	\int_0^{\pi/2} \sin^{2 \cdot \frac{3}{2} - 1} \theta \cos^{2 \cdot \frac{3}{2} - 1} \theta d \theta
	\\ &=&
	\cfrac{1}{2} B \left( \cfrac{3}{2}, \cfrac{3}{2} \right)
	\\ &=&
	\cfrac{1}{2}
	\cfrac{\frac{1}{2}}{\frac{3}{2} + \frac{1}{2}}
	B \left( \cfrac{3}{2}, \cfrac{1}{2} \right)
	\\ &=&
	\cfrac{1}{2}
	\cfrac{\frac{1}{2}}{\frac{3}{2} + \frac{1}{2}}
	\cfrac{\frac{1}{2}}{\frac{1}{2} + \frac{1}{2}}
	B \left( \cfrac{1}{2}, \cfrac{1}{2} \right)
	\\ &=&
	\cfrac{1}{2} \cdot \cfrac{1}{4} \cdot \cfrac{1}{2} \cdot \pi
	\\ &=&
	\cfrac{\pi}{16}
\end{eqnarray}
$$

