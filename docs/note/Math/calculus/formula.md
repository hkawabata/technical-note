---
title: 微分積分の公式
---

# 微分の公式

## n 次関数

$$
\left( x^a \right)' = a x^{a-1} \qquad (a \ne 0)
$$

## 指数関数

$$
\left( a^x \right)' = a^x \log a \qquad (a \ne 0)
$$

$$
\left( e^x \right)' = e^x
$$

## 対数関数

$$
\left( \log x \right)' = \cfrac{1}{x}
$$

## 関数の積

$$
\left( f(x) g(x) \right)' = f'(x) g(x) + f(x) g'(x)
$$

## 関数の商

$$
\left( \cfrac{f(x)}{g(x)} \right)' = \cfrac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}
$$

## 三角関数

$$
\left( \sin x \right)' = \cos x
$$

$$
\left( \cos x \right)' = - \sin x
$$

$$
\left( \tan x \right)' = \cfrac{1}{\cos^2 x}
$$

## 合成関数

$$
\left( f(g(x)) \right)' = g'(x) f'(g(x))
$$


# 積分の公式

## ガウス積分

> **【公式】**
>
> $a \gt 0$ として、
>
> $$
\int_{-\infty}^{\infty} e^{-ax^2} dx = \sqrt{\cfrac{\pi}{a}}
$$

**【証明】**

求める積分を $I = \int_{-\infty}^{\infty} e^{-ax^2} dx$ と置くと、

$$
\begin{eqnarray}
    I^2 &=& \int_{-\infty}^\infty e^{-ax^2} dx \int_{-\infty}^\infty e^{-ay^2} dy
    \\ &=&
    \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-a(x^2+y^2)} dx dy
\end{eqnarray}
$$

ここで $x = r\cos\theta,\ y=r\sin\theta$ と置換すれば、

$$
\begin{eqnarray}
    dxdy &=&
    \begin{vmatrix}
        \cfrac{\partial x}{\partial r} & \cfrac{\partial y}{\partial r} \\
        \cfrac{\partial x}{\partial \theta} & \cfrac{\partial y}{\partial \theta}
    \end{vmatrix}
    drd\theta
    =
    \begin{vmatrix}
        \cos\theta & \sin\theta \\
        -r\sin\theta & r\cos\theta
    \end{vmatrix}
    drd\theta
    \\ &=&
    (r\cos^2\theta + r\sin^2\theta)drd\theta = r\ drd\theta
\end{eqnarray}
$$

であるから、

$$
\begin{eqnarray}
    I^2 &=&
    \int_0^{2\pi} \int_0^\infty e^{-ar^2} r\ dr d\theta
    \\ &=&
    2\pi \int_0^\infty e^{-ar^2} r\ dr
    \\ &=&
    2\pi \left[ -\cfrac{1}{2a} e^{-ar^2} \right]_0^\infty
    \\ &=&
    \cfrac{\pi}{a}
\end{eqnarray}
$$

$I$ の被積分関数 $e^{-ax^2}$ は常に正のため $I\gt 0$ が成り立つ。したがって

$$
I = \sqrt{\cfrac{\pi}{a}}
$$


## 三角関数の直交性

> **【公式】三角関数の直交性**
> 
> **異なる三角関数の積を共通の周期で積分するとゼロになる**。
> 
> $n, m$ を異なる自然数とすれば、
>
> $$
\begin{eqnarray}
    \int_0^{2\pi} \sin mx \sin nx\ dx &=& 0 \tag{1}
    \\
    \int_0^{2\pi} \cos mx \cos nx\ dx &=& 0 \tag{2}
    \\
    \int_0^{2\pi} \sin mx \cos nx\ dx &=& 0 \tag{3}
    \\
    \int_0^{2\pi} \sin mx \cos mx\ dx &=& 0 \tag{4}
\end{eqnarray}
$$

**【証明】**

三角関数の角の和の公式

$$
\begin{eqnarray}
    \cos(\alpha+\beta) &=& \cos\alpha \cos\beta - \sin\alpha \sin\beta \\
    \sin(\alpha+\beta) &=& \sin\alpha \cos\beta + \cos\alpha \sin\beta \\
    \sin 2\alpha &=& 2\sin\alpha \cos\alpha \\
\end{eqnarray}
$$

を使うと

$$
\begin{eqnarray}
    \sin mx \sin nx &=& \cfrac{\cos(mx-nx) - \cos(mx+nx)}{2}
    \\ &=&
    \cfrac{\cos(m-n)x - \cos(m+n)x}{2}
    \\
    \cos mx \cos nx &=& \cfrac{\cos(mx-nx) + \cos(mx+nx)}{2}
    \\ &=&
    \cfrac{\cos(m-n)x + \cos(m+n)x}{2}
    \\
    \sin mx \cos nx &=& \cfrac{\sin(mx+nx) + \sin(mx-nx)}{2}
    \\ &=&
    \cfrac{\sin(m+n)x + \sin(m-n)x}{2}
    \\
    \sin mx \cos mx &=& \cfrac{\sin2mx}{2}
\end{eqnarray}
$$

であるから、それぞれ $0\le x \le 2\pi$ の範囲で積分して、

$$
\begin{eqnarray}
    \int_0^{2\pi} \sin mx \sin nx\ dx &=&
    \cfrac{1}{2} \left[
        \cfrac{\sin(m-n)x}{m-n} - \cfrac{\sin(m+n)x}{m+n}
    \right]_0^{2\pi}
    \\　&=&
    \cfrac{\sin 2(m-n)\pi-\sin 0}{2(m-n)} -
    \cfrac{\sin 2(m+n)\pi-\sin 0}{2(m+n)}
    \\ &=& 0-0 = 0
    \\
    \int_0^{2\pi} \cos mx \cos nx\ dx &=&
    \cfrac{1}{2} \left[
        \cfrac{\sin(m-n)x}{m-n} + \cfrac{\sin(m+n)x}{m+n}
    \right]_0^{2\pi}
    \\　&=&
    \cfrac{\sin 2(m-n)\pi-\sin 0}{2(m-n)} +
    \cfrac{\sin 2(m+n)\pi-\sin 0}{2(m+n)}
    \\ &=& 0+0 = 0
    \\
    \int_0^{2\pi} \sin mx \cos nx\ dx &=&
    \cfrac{1}{2} \left[
        -\cfrac{\cos(m+n)x}{m+n} - \cfrac{\cos(m-n)x}{m-n}
    \right]_0^{2\pi}
    \\　&=&
    -\cfrac{\cos 2(m+n)\pi-\cos 0}{2(m+n)}
    -\cfrac{\cos 2(m-n)\pi-\cos 0}{2(m-n)}
    \\ &=& -0-0 = 0
    \\
    \int_0^{2\pi} \sin mx \cos mx\ dx &=&
    \cfrac{1}{2} \left[
        - \cfrac{\cos 2mx}{2m}
    \right]_0^{2\pi}
    \\ &=&
    - \cfrac{\cos 4m\pi - \cos 0}{2m}
    \\ &=& 0
\end{eqnarray}
$$

それぞれの最後の計算では、$m,n$ が自然数であるため

$$
\begin{eqnarray}
    \sin 2(m+n)\pi &=& \sin 2(m-n)\pi &=& \sin 0
    \\
    \cos 2(m+n)\pi &=& \cos 2(m-n)\pi &=& \cos 0
    \\
    \cos 4m\pi &=& \cos 0
\end{eqnarray}
$$

となることを用いた。


> **【公式】三角関数の直交性その2**
> 
> $n, m$ を異なる自然数とすれば、
>
> $$
\begin{eqnarray}
    \int_0^T \sin\cfrac{2m\pi x}{T} \sin\cfrac{2n\pi x}{T}\ dx &=& 0 \tag{1'}
    \\
    \int_0^T \cos\cfrac{2m\pi x}{T} \cos\cfrac{2n\pi x}{T}\ dx &=& 0 \tag{2'}
    \\
    \int_0^T \sin\cfrac{2m\pi x}{T} \cos \cfrac{2n\pi x}{T}\ dx &=& 0 \tag{3'}
    \\
    \int_0^T \sin\cfrac{2m\pi x}{T} \cos\cfrac{2m\pi x}{T}\ dx &=& 0 \tag{4'}
\end{eqnarray}
$$

**【証明】**

$u = \cfrac{2\pi x}{T}$ と置換すれば、$(1)(2)(3)(4)$ と同じ積分になって同様に証明できる。