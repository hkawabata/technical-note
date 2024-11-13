---
title: フーリエ変換
title-en: Fourier transform
---
# フーリエ級数展開

## フーリエ級数とは

実関数 $f(x)$ を周期 $T$ の周期関数とする：

$$
f(x+T) = f(x)
\tag{1}
$$

このとき、$f(x)$ は以下ように三角関数の無限級数に展開できる：

$$
f(x)
=
\cfrac{a_0}{2} + \sum_{n=1}^\infty
\left(
    a_n \cos \cfrac{2n\pi x}{T} + b_n \sin \cfrac{2n\pi x}{T}
\right)
\tag{2}
$$

これを $f(x)$ の **フーリエ級数** という。係数 $a_n, b_n$ は

$$
\begin{eqnarray}
    a_n &=& \cfrac{2}{T} \int_0^T f(x) \cos \cfrac{2n\pi x}{T} dx
    \tag{3}
    \\
    b_n &=& \cfrac{2}{T} \int_0^T f(x) \sin \cfrac{2n\pi x}{T} dx
    \tag{4}
\end{eqnarray}
$$

この式は $a_0$ についても成り立つ。


## 係数の導出

フーリエ級数展開の係数 $a_n, b_n$ を導出する。

$(2)$ の両辺に $\cos \cfrac{2k\pi x}{T}\ (k = 1,2,3,\cdots)$ をかけて $0\le x \le T$ の区間で積分すると、

$$
\int_0^T f(x) \cos \cfrac{2k\pi x}{T} dx
=
\cfrac{a_0}{2} \int_0^T \cos \cfrac{2k\pi x}{T} dx +
\sum_{n=1}^\infty \left(
    a_n \int_0^T \cos \cfrac{2k\pi x}{T} \cos \cfrac{2n\pi x}{T} dx +
    b_n \int_0^T \cos \cfrac{2k\pi x}{T} \sin \cfrac{2n\pi x}{T} dx
\right)
$$

ここで右辺について、第一項は $\cos$ を1周期分の区間で積分しているのでゼロ。無限級数部分は、三角関数の積に関する積分公式

$$
\begin{eqnarray}
    \int_0^T \cos \cfrac{2k\pi x}{T} \cos \cfrac{2n\pi x}{T} dx
    &=&
    \int_0^T \sin \cfrac{2k\pi x}{T} \sin \cfrac{2n\pi x}{T} dx
    =
    \begin{cases}
        \cfrac{T}{2} \qquad &(k = n) \\
        0 \qquad &(k \ne n)
    \end{cases}
    \\
    \int_0^T \cos \cfrac{2k\pi x}{T} \sin \cfrac{2n\pi x}{T} dx &=& 0
\end{eqnarray}
$$

を適用すれば、$\cos$ どうしの積の $n=k$ の項のみが残るので、

$$
\int_0^T f(x) \cos \cfrac{2k\pi x}{T} dx = \cfrac{a_k T}{2}
$$

したがって

$$
a_k = \cfrac{2}{T} \int_0^T f(x) \cos \cfrac{2k\pi x}{T} dx
\tag{3}
$$

次に $(2)$ の両辺に $\sin \cfrac{2k\pi x}{T}\ (k = 1,2,3,\cdots)$ をかけて $0\le x \le T$ の区間で積分すると、同様に計算して

$$
b_k = \cfrac{2}{T} \int_0^T f(x) \sin \cfrac{2k\pi x}{T} dx
\tag{4}
$$

最後に $(2)$ の両辺を $0\le x \le T$ の区間で積分すると、

$$
\int_0^T f(x) dx = \cfrac{a_0 T}{2}
$$

となるので、

$$
a_0 = \cfrac{2}{T} \int_0^T f(x) dx
$$

この式は $(3)$ に $k=0$ を代入したものと一致するので、$(3)$ は $k=0$ の場合にも拡張できる。


## 計算例

> 【例1】$n$ を任意の整数として、
> 
> $$
f(x) = \begin{cases}
    1\qquad &(2n \lt x \le 2n+1) \\
    -1\qquad &(2n-1 \lt x \le 2n)
\end{cases}
$$

周期 $T=2$ の周期関数であるから、$n\ne 0$ について

$$
\begin{eqnarray}
    a_n &=& \int_0^2 f(x) \cos n\pi x \ dx
    \\ &=&
    \int_0^1 1 \cdot \cos n\pi x \ dx + \int_1^2 (-1) \cdot \cos n\pi x \ dx
    \\ &=&
    \cfrac{1}{n\pi} \left[ \sin n\pi x \right]_0^1 -
    \cfrac{1}{n\pi} \left[ \sin n\pi x \right]_1^2
    \\ &=&
    \cfrac{1}{n\pi} (0-0) - \cfrac{1}{n\pi} (0-0) = 0
    \\
    b_n &=& \int_0^2 f(x) \sin n\pi x \ dx
    \\ &=&
    \int_0^1 1 \cdot \sin n\pi x \ dx + \int_1^2 (-1) \cdot \sin n\pi x \ dx
    \\ &=&
    -\cfrac{1}{n\pi} \left[ \cos n\pi x \right]_0^1 +
    \cfrac{1}{n\pi} \left[ \cos n\pi x \right]_1^2
    \\ &=&
    - \cfrac{1}{n\pi} (\cos n\pi-1) + \cfrac{1}{n\pi} (1-\cos n\pi)
    \\ &=&
    \cfrac{2}{n\pi} (1 - \cos n\pi)
    = \cfrac{2}{n\pi} \left(1 - (-1)^n\right)
    = \cfrac{2}{n\pi} \left(1 + (-1)^{n+1}\right)
\end{eqnarray}
$$

$n=0$ については

$$
a_0 = \int_0^2 f(x) dx = \int_0^1 1dx + \int_1^2(-1)dx = 1 + (-1) = 0
$$

以上により

$$
\begin{eqnarray}
    f(x) &=& \sum_{n=1}^\infty \cfrac{2}{n\pi} \left(1 + (-1)^{n+1}\right)
    \sin n\pi x
    \\ &=&
    \cfrac{4}{\pi} \sum_{k=1}^\infty \cfrac{1}{2k-1} \sin (2k-1)\pi x
    \\ &=&
    \cfrac{4}{\pi} \left(
        \sin \pi x + \cfrac{1}{3} \sin 3\pi x + \cfrac{1}{5} \sin 5\pi x + \cdots
    \right)
\end{eqnarray}
$$

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y = np.where(x//1 % 2, -1, 1)
y2 = np.zeros(x.shape)
plt.plot(x, y, color='black', label='$f(x)$')
for n in range(1, 12+1):
    if n % 2 == 1:
        y2 += 4 * np.sin(n*np.pi*x) / n / np.pi
    if n % 3 == 0:
        plt.plot(x, y2, linewidth=1, label=r'sum($n \leq {}$)'.format(n))

plt.xlabel('$x$', fontsize=15)
plt.ylabel('$f(x)$', fontsize=15)
plt.legend()
plt.grid()
plt.show()
```



# フーリエ変換

## フーリエ変換とは

フーリエ級数展開を周期関数ではなく任意の関数に拡張したもの。

関数 $f(x)$ が絶対積分可能、すなわち

$$
\int_{-\infty}^\infty \vert f(x) \vert dx \lt \infty
$$

であるとき、

$$
F(\omega) = \int_{-\infty}^\infty f(x) e^{-i\omega x}\ dx
\tag{5}
$$

を $f(x)$ の **フーリエ変換** という。また、

$$
f(x) = \cfrac{1}{2\pi} \int_{-\infty}^\infty F(\omega) e^{i\omega x}\ d\omega
\tag{6}
$$

により $F(\omega)$ から $f(x)$ を求めることもでき、これを **逆フーリエ変換** という。


## パワースペクトルと位相

一般にフーリエ変換 $F(\omega)$ は複素数の値を取る：

$$
F(\omega) = \mathrm{Re}\ F(\omega) + i\ \mathrm{Im}\ F(\omega)
$$

この複素数の絶対値の二乗

$$
\vert F(\omega) \vert^2 = (\mathrm{Re}\ F(\omega))^2 + (\mathrm{Im}\ F(\omega))^2
\tag{7}
$$

を **パワースペクトル** と呼ぶ。

また、複素数 $F(\omega)$ の **位相** を $\theta(\omega)$ とすると、

$$
F(\omega) = \vert F(\omega) \vert e^{i\theta(\omega)}
$$

すなわち

$$
\begin{cases}
    \mathrm{Re}\ F(\omega) &=& \vert F(\omega) \vert \cos\theta(\omega) \\
    \mathrm{Im}\ F(\omega) &=& \vert F(\omega) \vert \sin\theta(\omega)
\end{cases}
\tag{8}
$$

が成り立つ（複素数の一般的な性質）。


## 式の導出

任意の関数 $f(x)$ は、周期 $T=\infty$ の周期関数と解釈できる。

$f(x),\ \cos \cfrac{2n\pi x}{T},\ \sin \cfrac{2n\pi x}{T}$ がそれぞれ周期 $T$ の周期関数であるとき、積分区間 $\int_0^T$ を $\int_{-T/2}^{T/2}$ としても（1周期分の区間の積分なので）値は変わらず、$T=2L$ とおけば、$(2),(3),(4)$ は以下のように書き換えられる：

$$
\begin{eqnarray}
    f(x) &=& \cfrac{a_0}{2} + \sum_{n=1}^\infty
    \left(
        a_n \cos \cfrac{n\pi x}{L} + b_n \sin \cfrac{n\pi x}{L}
    \right)
    \tag{2'}
    \\
    a_n &=& \cfrac{1}{L} \int_{-L}^L f(x) \cos \cfrac{n\pi x}{L} dx
    \tag{3'}
    \\
    b_n &=& \cfrac{1}{L} \int_{-L}^L f(x) \sin \cfrac{n\pi x}{L} dx
    \tag{4'}
\end{eqnarray}
$$

ここで

$$
\omega_n := n\pi/L,\quad \Delta \omega := \omega_{n+1}-\omega_n = \pi/L
$$

とおけば、$1/L = \Delta\omega/\pi$ なので、

$$
f(x) = \cfrac{\Delta\omega}{2\pi} \int_{-L}^L f(u) du
+ \cfrac{1}{\pi} \sum_{n=1}^\infty
    \left(
        \cos \omega_n x \int_{-L}^L f(u) \cos \omega_n u du +
        \sin \omega_n x \int_{-L}^L f(u) \sin \omega_n u du
    \right) \Delta\omega
$$

$f(x)$ を周期関数とみなすため $L \to \infty$ の極限を取ると $\Delta\omega \to 0$ であり、$\omega_n$ は等間隔であることから連続変数 $\omega$ とみなせるので、和を積分に置き換えられる：

$$
f(x) = \lim_{\Delta\omega\to 0} \cfrac{\Delta\omega}{2\pi} \int_{-\infty}^\infty f(u) du
+ \cfrac{1}{\pi} \int_0^\infty
    \left(
        \cos \omega x \int_{-\infty}^\infty f(u) \cos \omega u\ du +
        \sin \omega x \int_{-\infty}^\infty f(u) \sin \omega u\ du
    \right) d\omega
$$

$f(x)$ が絶対積分可能なので、右辺第一項の積分部分は発散しない。よって右辺第一項はゼロに収束するから、

$$
\begin{eqnarray}
    f(x) &=& \cfrac{1}{\pi} \int_0^\infty
    f(u) \left(
        \cos \omega x \int_{-\infty}^\infty f(u) \cos \omega u\ du +
        \sin \omega x \int_{-\infty}^\infty f(u) \sin \omega u\ du
    \right) d\omega
    \\ &=&
    \cfrac{1}{\pi} \int_0^\infty d\omega \int_{-\infty}^\infty du\ 
    f(u) \left( \cos\omega x \cos\omega u + \sin\omega x \sin\omega u \right)
    \\ &=&
    \cfrac{1}{\pi} \int_0^\infty d\omega \int_{-\infty}^\infty du\ 
    f(u) \cos \omega(x-u)
    \\ &=&
    \cfrac{1}{\pi} \int_0^\infty d\omega \int_{-\infty}^\infty du\ 
    f(u) \cfrac{e^{i\omega(x-u)}-e^{-i\omega(x-u)}}{2}
\end{eqnarray}
$$

ここで $e^{-i\omega(x-u)}$ の $\omega$ 積分に関して、$\omega' = -\omega$ と置換すれば

$$
\int_0^\infty e^{-i\omega(x-u)} d\omega =
\int_0^{-\infty} e^{i\omega'(x-u)} d(-\omega') =
\int_{-\infty}^0 e^{i\omega'(x-u)} d\omega'
$$

よって

$$
\begin{eqnarray}
    f(x) &=& \cfrac{1}{\pi} \int_0^\infty d\omega \int_{-\infty}^\infty du\ 
    f(u) \cfrac{e^{i\omega(x-u)}-e^{-i\omega(x-u)}}{2}
    \\ &=&
    \cfrac{1}{\pi} \left( \int_0^\infty d\omega + \int_{-\infty}^0 d\omega \right)
    \int_{-\infty}^\infty du\ 
    f(u) \cfrac{e^{i\omega(x-u)}}{2}
    \\ &=&
    \cfrac{1}{2\pi} \int_{-\infty}^\infty \int_{-\infty}^\infty
    f(u) e^{i\omega(x-u)}\ du d\omega
    \\ &=&
    \cfrac{1}{2\pi} \int_{-\infty}^\infty
    \left(
        \int_{-\infty}^\infty f(u) e^{-i\omega u}\ du
    \right) e^{i\omega x} d\omega
\end{eqnarray}
$$

最後の式のカッコの中身は $\omega$ にのみ依存する関数であり、これを

$$
F(\omega) := \int_{-\infty}^\infty f(x) e^{-i\omega x}\ dx
\tag{5}
$$

と置けば（※ ここでは積分変数を $u \to x$ と書き換えている）

$$
f(x) = \cfrac{1}{2\pi} \int_{-\infty}^\infty F(\omega) e^{i\omega x}\ d\omega
\tag{6}
$$

となり、フーリエ変換、逆フーリエ変換の式を得る。


## 計算例

> 【例1】
> 
> $$
f(x) = \begin{cases}
    1\qquad &(0 \lt x \le 1) \\
    -1\qquad &(1 \lt x \le 2)
\end{cases}
$$

$$
\begin{eqnarray}
    F(\omega) &=& \int_{-\infty}^\infty f(x) e^{-i\omega x}\ dx
    \\ &=&
    \int_0^1 1 \cdot e^{-i\omega x}\ dx +
    \int_1^2 (-1) \cdot e^{-i\omega x}\ dx
    \\ &=&
    \int_0^1 ( \cos \omega x - i \sin \omega x )\ dx -
    \int_1^2 ( \cos \omega x - i \sin \omega x )\ dx
    \\ &=&
    \left[\cfrac{1}{\omega} \sin \omega x + i \cfrac{1}{\omega} \cos \omega x \right]_0^1 -
    \left[ \cfrac{1}{\omega} \sin \omega x + i \cfrac{1}{\omega} \cos \omega x \right]_1^2
    \\ &=&
    \cfrac{1}{\omega}(\sin \omega + i \cos \omega)
    - \cfrac{1}{\omega}(0 + i)
    - \cfrac{1}{\omega}(\sin 2\omega + i \cos 2\omega)
    + \cfrac{1}{\omega}(\sin \omega + i \cos \omega)
    \\ &=&
    \cfrac{1}{\omega}(2\sin \omega - \sin 2\omega) +
    i \cfrac{1}{\omega}(2\cos \omega - \cos 2\omega -1)
\end{eqnarray}
$$

パワースペクトルは

$$
\begin{eqnarray}
    \vert F(\omega) \vert^2
    &=&
    \cfrac{1}{\omega^2} \left\{
        (2\sin \omega - \sin 2\omega)^2 +
        (2\cos \omega - \cos 2\omega -1)^2
    \right\}
    \\ &=&
    \cfrac{1}{\omega^2} \left\{
        (2\sin \omega - 2\sin \omega \cos \omega)^2 +
        (2\cos \omega - (2\cos^2\omega-1) -1)^2
    \right\}
    \\ &=&
    \cfrac{4}{\omega^2} \left\{
        \sin^2 \omega (1 - \cos \omega)^2 +
        \cos^2 \omega (1 - \cos \omega)^2
    \right\}
    \\ &=&
    \cfrac{4}{\omega^2}
    (\sin^2 \omega + \cos^2 \omega) (1 - \cos \omega)^2
    \\ &=&
    \cfrac{4}{\omega^2} (1 - \cos \omega)^2
\end{eqnarray}
$$

位相 $\theta(\omega)$ は

$$
\begin{eqnarray}
    \cos\theta(\omega) &=& \cfrac{\mathrm{Re}\ F(\omega)}{\vert F(\omega) \vert}
    = \cfrac{2\sin \omega - \sin 2\omega}{2(1-\cos\omega)} \\
    \sin\theta(\omega) &=& \cfrac{\mathrm{Im}\ F(\omega)}{\vert F(\omega) \vert} = \cfrac{2\cos \omega - \cos 2\omega -1}{2(1-\cos\omega)}
\end{eqnarray}
$$

| $f(x)$                                                                                             | $F(\omega)$                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| ![Figure_f1](https://gist.github.com/user-attachments/assets/ebfdba5a-3e0d-454f-98a3-19152ff88c42) | ![Figure_g1](https://gist.github.com/user-attachments/assets/65478171-d1ef-4796-9120-02b2b59bbed6) |

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = np.zeros(x.shape)
for i in range(len(x)):
    if 0 <= x[i] < 1:
        y[i] = 1
    elif 1 <= x[i] < 2:
        y[i] = -1

d_omega = np.pi * 0.01
omega = np.linspace(d_omega, d_omega*800, 1000)
re = (2*np.sin(omega)-np.sin(2*omega)) / omega
im = (2*np.cos(omega)-np.cos(2*omega)-1) / omega
ps = 4 * (1-np.cos(omega))**2 / omega**2
theta = np.where(re != 0, np.atan(im / re), np.asin(im))

plt.xlabel('$x$', fontsize=15)
plt.ylabel('$f(x)$', fontsize=15)
plt.plot(x, y)
plt.grid()
plt.show()

plt.xlabel(r'$\omega$', fontsize=15)
plt.plot(omega, re, label=r'Re $F(\omega)$')
plt.plot(omega, im, label=r'Im $F(\omega)$')
plt.plot(omega, ps, label=r'Power Spectrum $|F(\omega)|^2$')
plt.plot(omega, theta, label=r'$\theta(\omega)$')
plt.grid()
plt.legend()
plt.show()
```


> 【例1.1】（例1を平行移動したもの）
> 
> $$
f(x) = \begin{cases}
    1\qquad &(-1 \lt x \le 0) \\
    -1\qquad &(0 \lt x \le 1)
\end{cases}
$$

$$
\begin{eqnarray}
    F(\omega) &=& \int_{-\infty}^\infty f(x) e^{-i\omega x}\ dx
    \\ &=&
    \int_{-1}^0 1 \cdot e^{-i\omega x}\ dx +
    \int_0^1 (-1) \cdot e^{-i\omega x}\ dx
    \\ &=&
    \int_{-1}^0 ( \cos \omega x - i \sin \omega x )\ dx -
    \int_0^1 ( \cos \omega x - i \sin \omega x )\ dx
    \\ &=&
    \left[\cfrac{1}{\omega} \sin \omega x + i \cfrac{1}{\omega} \cos \omega x \right]_{-1}^0 -
    \left[ \cfrac{1}{\omega} \sin \omega x + i \cfrac{1}{\omega} \cos \omega x \right]_0^1
    \\ &=&
    \cfrac{1}{\omega}(0 + i)
    - \cfrac{1}{\omega}(-\sin \omega + i \cos \omega)
    - \cfrac{1}{\omega}(\sin \omega + i \cos \omega)
    + \cfrac{1}{\omega}(0 + i)
    \\ &=&
    i \cfrac{2}{\omega}(1 - \cos \omega)
\end{eqnarray}
$$

パワースペクトルは以下のようになり、例1の値と一致する。

$$
\vert F(\omega) \vert^2 = \cfrac{4}{\omega^2} (1 - \cos \omega)^2
$$

位相 $\theta(\omega)$ は

$$
\begin{eqnarray}
    \cos\theta(\omega) &=& \cfrac{\mathrm{Re}\ F(\omega)}{\vert F(\omega) \vert} = 0 \\
    \sin\theta(\omega) &=& \cfrac{\mathrm{Im}\ F(\omega)}{\vert F(\omega) \vert} = 1
\end{eqnarray}
$$

より $\theta(\omega) = \pi/2$

| $f(x)$ | $F(\omega)$ |
| -- | -- |
| ![Figure_f1-1](https://gist.github.com/user-attachments/assets/4fba3304-a059-4e4e-aa8e-fa6b9b6a8bc8) | ![Figure_g1-1](https://gist.github.com/user-attachments/assets/dc57c8b9-f797-4a36-b820-7e1fa573ee11) |

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = np.zeros(x.shape)
for i in range(len(x)):
    if -1 <= x[i] < 0:
        y[i] = 1
    elif 0 <= x[i] < 1:
        y[i] = -1

d_omega = np.pi * 0.01
omega = np.linspace(d_omega, d_omega*800, 1000)
re = np.zeros(omega.shape)
im = 2*(1-np.cos(omega)) / omega
ps = 4 * (1-np.cos(omega))**2 / omega**2
theta = np.full(omega.shape, np.pi/2)

plt.xlabel('$x$', fontsize=15)
plt.ylabel('$f(x)$', fontsize=15)
plt.plot(x, y)
plt.grid()
plt.show()

plt.xlabel(r'$\omega$', fontsize=15)
plt.plot(omega, re, label=r'Re $F(\omega)$')
plt.plot(omega, im, label=r'Im $F(\omega)$')
plt.plot(omega, ps, label=r'Power Spectrum $|F(\omega)|^2$')
plt.plot(omega, theta, label=r'$\theta(\omega)$')
plt.grid()
plt.legend()
plt.show()
```



> 【例2】ガウス関数
> 
> $$
f(x) = e^{-x^2}
$$

$$
\begin{eqnarray}
    F(\omega) &=& \int_{-\infty}^\infty f(x) e^{-i\omega x}\ dx
    \\ &=&
    \int_{-\infty}^\infty e^{-x^2} e^{-i\omega x}\ dx
\end{eqnarray}
$$

両辺を $\omega$ で微分して右辺を部分積分すると、

$$
\begin{eqnarray}
    \cfrac{dF(\omega)}{d\omega} &=&
    -i \int_{-\infty}^\infty x e^{-x^2} e^{-i\omega x}\ dx
    \\ &=&
    -i \int_{-\infty}^\infty \cfrac{d(-e^{-x^2})}{dx} e^{-i\omega x}\ dx
    \\ &=&
    -i \left\{
        \left[ -e^{-x^2} e^{-i\omega x} \right]_{-\infty}^\infty -
        \int_{-\infty}^\infty (-e^{-x^2}) \cfrac{d(e^{-i\omega x})}{dx}\ dx
    \right\}
    \\ &=&
    -i \left\{
        (0-0) - i\omega
        \int_{-\infty}^\infty e^{-x^2} e^{-i\omega x}\ dx
    \right\}
    \\ &=&
    -\omega F(\omega)
\end{eqnarray}
$$

これは $F(\omega)$ に関する微分方程式になっており、解は

$$
F(\omega) = F(0) e^{-\omega^2/2} = e^{-\omega^2/2} \int_{-\infty}^\infty e^{-x^2}\ dx
$$

この式の積分の部分はガウス関数の積分であるから、積分公式

$$
\int_{-\infty}^\infty e^{-x^2/2\sigma^2} dx = \sqrt{2\pi} \sigma
$$

に $\sigma = 1/\sqrt{2}$ を代入して、

$$
F(\omega) = e^{-\omega^2/2} \cdot \sqrt{2\pi} \cdot \cfrac{1}{\sqrt{2}} = \sqrt{\pi} e^{-\omega^2/2}
$$

→ **ガウス関数のフーリエ変換もガウス関数になる。**

パワースペクトルは

$$
\vert F(\omega) \vert^2 = \pi e^{-\omega^2}
$$

位相 $\theta(\omega)$ は

$$
\begin{eqnarray}
    \cos\theta(\omega) &=& \cfrac{\mathrm{Re}\ F(\omega)}{\vert F(\omega) \vert} = 1 \\
    \sin\theta(\omega) &=& \cfrac{\mathrm{Im}\ F(\omega)}{\vert F(\omega) \vert} = 0
\end{eqnarray}
$$

より $\theta(\omega) = 0$

| $f(x)$ | $F(\omega)$ |
| -- | -- |
| ![Figure_f2](https://gist.github.com/user-attachments/assets/4ff8901e-867d-4703-8807-c9ccd14cc5d6) | ![Figure_g2](https://gist.github.com/user-attachments/assets/91263af4-e20d-4707-b6dc-767b9743479a) |

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = np.exp(-x*x)

d_omega = np.pi * 0.01
omega = np.linspace(d_omega, d_omega*800, 1000)
re = np.sqrt(np.pi) * np.exp(-omega*omega/2)
im = np.zeros(omega.shape)
ps = np.pi * np.exp(-omega*omega)
theta = np.full(omega.shape, np.pi/2)

plt.xlabel('$x$', fontsize=15)
plt.ylabel('$f(x)$', fontsize=15)
plt.plot(x, y)
plt.grid()
plt.show()

plt.xlabel(r'$\omega$', fontsize=15)
plt.plot(omega, re, label=r'Re $F(\omega)$')
plt.plot(omega, im, label=r'Im $F(\omega)$')
plt.plot(omega, ps, label=r'Power Spectrum $|F(\omega)|^2$')
plt.plot(omega, theta, label=r'$\theta(\omega)$')
plt.grid()
plt.legend()
plt.show()
```