---
title: 複素積分
---
# 複素積分とは

複素平面上の滑らかな曲線 $C: z = z(t)\,(a\le t \le b)$ と、$C$ に沿って連続な複素関数 $f(z)$ があるとする。
曲線 $C$ に沿って $f(z)$ の積分を取ったものを「$f(z)$ の $C$ に沿った **複素積分**」と呼び、

$$
\int_C f(z) dz
$$

と表す。$z = z(t)$ であるから、

$$
\int_C f(z) dz = \int_a^b f(z(t)) \cfrac{dz}{dt} dt
$$

と書き換えて積分を計算できる。

# 計算例

始点と終点が同じ2つの曲線

$$
\begin{eqnarray}
    &C_1:&\,z(t) = t + ti &\qquad (0 \le t \le 1)
    \\
    &C_2:&\,z(t) = t + t^2i &\qquad (0 \le t \le 1)
\end{eqnarray}
$$

に沿って、複素関数

$$
f(z) = z^2
$$

を始点 $(0,0)$ から終点 $(1,1)$ まで積分する。

![complex-integral](https://user-images.githubusercontent.com/13412823/284139586-14c9594c-af27-4bc1-9a15-6a3bdc00c529.png)

```python
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 1.01, 0.01)
y1 = x
y2 = x**2
plt.xlabel('Re')
plt.ylabel('Im')
plt.plot(x, y1, label='$C_1$')
plt.plot(x, y2, label='$C_2$')
plt.grid()
plt.legend()
plt.show()
```

$$
\begin{eqnarray}
    \int_{C_1} f(z) dz &=& \int_0^1 (t + ti)^2 (1 + i) dt
    \\ &=&
    \int_0^1 2t^2 i (1+i) dt
    \\ &=&
    2(-1+i) \int_0^1 t^2 dt
    \\ &=&
    2(-1+i) \left[ \cfrac{1}{3} t^3 \right]_0^1
    \\ &=&
    \cfrac{2}{3}(-1+i)
    \\
    \int_{C_2} f(z) dz &=& \int_0^1 (t + t^2i)^2 (1 + 2ti) dt
    \\ &=&
    \int_0^1 (t^2 + 2t^3i - t^4) (1+2ti) dt
    \\ &=&
    \int_0^1 (t^2 -5t^4) dt +
    i \int_0^1 (4t^3 -2t^5) dt
    \\ &=&
    \left[ \cfrac{1}{3} t^3 - t^5 \right]_0^1 +
    i \left[ t^4 - \cfrac{1}{3} t^6 \right]_0^1
    \\ &=&
    \cfrac{2}{3} (-1+i)
\end{eqnarray}
$$

経路が異なる $C_1, C_2$ の積分結果が一致しているが、このことは次節の定理から一般的に示せる。

# コーシーの積分定理

> **【定理】コーシーの積分定理**
> 
> 有界な単連結領域 $D$ で $f(z)$ が解析的なら、$D$ 内のすべての単純閉曲線 $C$ に対して、$C$ を一周する経路積分はゼロになる：
> 
> $$
\oint_C f(z) dz = 0
$$
>
> 数学的に厳密ではない注釈：
> - 単連結領域：複素関数に関しては「ドーナツ型のような穴あり領域でない」と思っておけば OK
> - $f(z)$ が解析的：領域内で微分可能（厳密には例外があるかも）
> - 単純閉曲線：自分自身と交わらない閉じた直線

前節の例に適用すると、
- $C_1$ と $C_2$（の逆向きの経路）を足すと単純閉曲線になる（この曲線を $C$ とする）
- $C$ で囲まれる領域において関数 $f(z) = z^2$ は明らかに解析的（微分可能）
- $C$ は明らかに単連結領域（穴なし）

なのでコーシーの積分定理が成り立ち、

$$
\oint_C f(z) dz = 0
$$

$C$ を一周する積分は $C_1$ の順方向と $C_2$ の逆方向の積分の和であるから、

$$
\oint_C f(z) dz = \int_{C_1} f(z) dz + \left( - \int_{C_2} f(z) dz \right)
$$

以上により、

$$
\int_{C_1} f(z) dz = \int_{C_2} f(z) dz
$$


# 計算例：解析的でない点を囲む経路

経路 $C_1$ と $C_2$ で囲まれる領域内に、$f(z)$ を微分できない特異点がある場合を考える。

```python
import numpy as np
from matplotlib import pyplot as plt

dt = 0.01
t1 = np.arange(0, 1+dt, dt)
x1 = t1
y1 = t1
t2 = np.arange(-np.pi, np.pi/2+dt, dt)
x2 = 1 + np.cos(t2)
y2 = np.sin(t2)
plt.axis('equal')
plt.xlabel('Re')
plt.ylabel('Im')
plt.scatter(1,0,color='red', label='indifferentiable')
plt.plot(x1, y1, label='$C_1$')
plt.plot(x2, y2, label='$C_2$')
plt.grid()
plt.legend(loc='lower right')
plt.show()
```

始点 $z=0$ と終点 $z=1+i$ が同じである2つの曲線

$$
\begin{eqnarray}
    &C_1:&\,z(t) = t + it &\qquad (0 \le t \le 1)
    \\
    &C_2:&\,z(t) = e^{it}+1 &\qquad (-\pi \le t \le \pi/2)
\end{eqnarray}
$$

に沿って、複素関数

$$
f(z) = \cfrac{1}{z-1}
$$

を積分する。

![complex-integral2](https://user-images.githubusercontent.com/13412823/284899302-d1439c3f-12bf-4c0c-86df-7056a014621e.png)


$$
\begin{eqnarray}
    \int_{C_1} f(z) dz &=& \int_0^1 \cfrac{1}{t+it-1} (1+i) dt
    \\ &=&
    \int_0^1 \cfrac{((t-1)-it)(1+i)}{(t-1)^2+t^2} dt
    \\ &=&
    \int_0^1 \cfrac{2t-1}{2t^2-2t+1} dt
    - i \int_0^1 \cfrac{1}{2t^2-2t+1} dt
    \\ &=&
    \cfrac{1}{2} \int_0^1 \cfrac{(2t^2-2t+1)'}{2t^2-2t+1} dt
    - i \int_0^1 \cfrac{1}{2\left(t-\frac{1}{2}\right)^2+\frac{1}{2}} dt
    \\ &=&
    \cfrac{1}{2} \left[ \log (2t^2-2t+1) \right]_0^1
    - i \int_0^1 \cfrac{2}{(2t-1)^2+1} dt
    \\ &=&
    \cfrac{1}{2}(0-0) - i \int_{-\pi/4}^{\pi/4} \cfrac{2}{\tan^2 \theta + 1} \cdot \cfrac{d\theta}{2\cos^2 \theta}
    &\qquad& (2t-1 := \tan \theta )
    \\ &=&
    - i \int_{-\pi/4}^{\pi/4} d \theta
    &\qquad& \left(\because \ 1+\tan^2 \theta = \cfrac{1}{\cos^2\theta} \right)
    \\ &=&
    - i \left( \cfrac{\pi}{4} - \left( -\cfrac{\pi}{4} \right) \right)
    \\ &=&
    - \cfrac{\pi i}{2}
    \\
    \\
    \int_{C_2} f(z) dz
    &=&
    \int_{-\pi}^{\pi/2} \cfrac{1}{e^{it}+1-1} \cdot ie^{it} dt
    \\ &=&
    i \int_{-\pi}^{\pi/2} dt
    \\ &=&
    i\left( \cfrac{\pi}{2} - (-\pi) \right)
    \\ &=&
    \cfrac{3\pi i}{2}
\end{eqnarray}
$$

したがって、この例では始点と終点が同じでも積分の結果が異なる：

$$
\int_{C_1} f(z) dz \ne \int_{C_2} f(z) dz
$$

また、$C_1$ の逆方向と $C_2$ の順方向を組み合わせた単純閉曲線 $C$ での積分を計算すると、

$$
\begin{eqnarray}
    \oint_C f(z) dz &=& - \int_{C_1} f(z) dz + \int_{C_2} f(z) dz
    \\ &=&
    \cfrac{\pi i}{2} + \cfrac{3\pi i}{2}
    \\ &=&
    2\pi i
\end{eqnarray}
$$

このような、内部に特異点を含む単純閉曲線 $C$ を1周する経路積分は、直接計算せずとも、[留数定理](residue-theorem.md)を用いて計算できる。
