---
title: 拡散方程式
title-en: diffusion equation
---
# 定義

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ に関する偏微分方程式

$$
\cfrac{\partial u}{\partial t} = \kappa \cfrac{\partial^2 u}{\partial x^2}
\qquad (\kappa = \mathrm{const.})
\tag{1}
$$

を **拡散方程式** という。


# 導出

前提
- 微小距離 $\Delta x$ ごとに空間を区切り、区切られた微小領域間の物理量の受け渡しを考える
- 微小時間 $\Delta t$ の間に隣の領域に渡される物理量は、その空間の物質濃度 $u(x,t)$ に比例：比例定数 $c$

微小時間 $\Delta t$ の間の物質の移動を考えると、

- 座標 $x$ の微小領域から両隣の微小領域 $x+\Delta x,\ x-\Delta x$ へ出ていく物質の量：それぞれ $cu(x, t)$
- 両隣の微小領域 $x+\Delta x,\ x-\Delta x$ から座標 $x$ の微小領域へ入ってくる物質の量：それぞれ $cu(x+\Delta x,t),\ cu(x-\Delta x,t)$

以上により、座標 $x$ における物質の変化量の式を立てると、

$$
u(x, t + \Delta t) - u(x,t) =
- 2c u(x, t) + cu(x+\Delta x,t) + cu(x-\Delta x,t)
$$

左辺・右辺をそれぞれ変形して、

$$
\begin{eqnarray}
    u(x, t + \Delta t) - u(x,t)
    &=&
    \cfrac{u(x, t + \Delta t) - u(x,t)}{\Delta t} \Delta t
    \\ &\simeq&
    \cfrac{\partial u}{\partial t} \Delta t
    \\
    \\
    - 2c u(x, t) + cu(x+\Delta x,t) + cu(x-\Delta x,t)
    &=&
    c \Delta x \left\{
        \cfrac{u(x+\Delta x,t) - u(x,t)}{\Delta x} -
        \cfrac{u(x,t)-u(x-\Delta x,t)}{\Delta x}
    \right\}
    \\ &\simeq&
    c \Delta x \left\{
        \cfrac{\partial u}{\partial x}(x,t) -
        \cfrac{\partial u}{\partial x}(x-\Delta x,t)
    \right\}
    \\ &=&
    c (\Delta x)^2
    \cfrac{
        \cfrac{\partial u}{\partial x}(x,t) -
        \cfrac{\partial u}{\partial x}(x-\Delta x,t)
    }{\Delta x}
    \\ &\simeq&
    c (\Delta x)^2
    \cfrac{\partial^2 u}{\partial x^2}
\end{eqnarray}
$$

以上より、

$$
\cfrac{\partial u}{\partial t} \Delta t
=
c (\Delta x)^2
\cfrac{\partial^2 u}{\partial x^2}
$$

$\kappa := \cfrac{c (\Delta x)^2}{\Delta t}$ とおけば、拡散方程式 $(1)$ を得る。


# 一般解

変数分離法で解く。

$$
u(x, t) = f(x)g(t)
$$

と置いて $(1)$ に代入すると、

$$
f(x) \cfrac{d g(t)}{d t} = \kappa \cfrac{d^2 f(x)}{d x^2} g(t)
$$

よって

$$
\cfrac{1}{g(t)} \cfrac{d g(t)}{d t} = \kappa \cfrac{1}{f(x)} \cfrac{d^2 f(x)}{d x^2}
$$

左辺は $t$ だけの式、右辺は $x$ だけの式であるから、これが任意の $x, t$ で成り立つ場合、この式の値は定数。  
この定数を $a$ と置くと、

$$
\begin{eqnarray}
    \cfrac{1}{g(t)} \cfrac{d g(t)}{d t} &=& a
    \\
    \kappa \cfrac{1}{f(x)} \cfrac{d^2 f(x)}{d x^2} &=& a
\end{eqnarray}
$$

それぞれを解く。$A_1, A_2, B$ を積分定数として、

$(i)\ a=0$ のとき

$$
\begin{eqnarray}
    f(t) &=& A_1 t + A_2
    \\
    g(t) &=& B
\end{eqnarray}
$$

$(ii)\ a \gt 0$ のとき

$$
\begin{eqnarray}
    f(x) &=& A_1 e^{\sqrt{a/\kappa}x} + A_2 e^{-\sqrt{a/\kappa}x}
    \\
    g(t) &=& B e^{at}
\end{eqnarray}
$$


$(iii)\ a \lt 0$ のとき、$a = -\omega\ (\omega \gt 0)$ とおけば

$$
\begin{eqnarray}
    f(x) &=& A_1 \sin \sqrt{\cfrac{\omega}{\kappa}}x + A_2 \cos \sqrt{\cfrac{\omega}{\kappa}}x
    \\
    g(t) &=& B e^{-\omega t}
\end{eqnarray}
$$

$a=0, a\gt 0$ の解は時間とともに発散するため、実際の物理現象を記述するには不適。  
したがって微分方程式 $(1)$ の解は

$$
u_\omega (x, t)
=
B e^{-\omega t} \left(
    A_1 \sin \sqrt{\cfrac{\omega}{\kappa}}x +
    A_2 \cos \sqrt{\cfrac{\omega}{\kappa}}x
\right)
$$

$BA_1, BA_2 \to S, C$ と置き換えれば、

$$
u_\omega (x, t)
=
e^{-\omega t} \left(
    S \sin \sqrt{\cfrac{\omega}{\kappa}}x +
    C \cos \sqrt{\cfrac{\omega}{\kappa}}x
\right)
$$

ここで、任意の $\omega \gt 0$ に対して $(1)$ は成り立つ。また実際に計算してみれば明らかなように、任意の異なる $\omega = \omega_1, \omega_2$ に対してそれらの重ね合わせ（和）である $u_{\omega_1}(x,t)+u_{\omega_2}(x,t)$ も $(1)$ を満たす。  
したがって、$(1)$ の一般解は

$$
u(x,t) = \sum_{\omega \gt 0}
e^{-\omega t} \left(
    S_{\omega} \sin \sqrt{\cfrac{\omega}{\kappa}}x +
    C_{\omega} \cos \sqrt{\cfrac{\omega}{\kappa}}x
\right)
\tag{2}
$$

積分定数 $S_\omega,C_\omega$ は境界条件や初期条件を課すことで定まる。

# 境界条件と特殊解

## 境界条件

### 外部の環境が一定である場合の境界条件

境界において物理量 $u(x,t)$ （濃度など）を一定とすれば良いので、境界の座標を $x_0$ とすると境界条件は

$$
u(x_0, t) = \alpha = \mathrm{const.}
$$

これは[ディリクレ条件](../boundary-condition/dirichlet-boundary-condition.md)に相当する。

### 外部とのやりとりがない場合の境界条件

境界において物理量 $u(x,t)$ が座標によって変化しなければ良いので、

$$
\cfrac{\partial u}{\partial x}(x_0, t) = 0
$$

これは[ノイマン条件](../boundary-condition/neumann-boundary-condition.md)に相当する。

## 特殊解の例

### 外部の環境が一定

定義域を $0 \le x \le L,\ 0 \le t$ として、

- 境界条件：
    - $u(0,t) = 0$
    - $u(L, t) = 0$
- 初期条件：
    - 初期濃度：$u(x, 0) = U_0 \sin \cfrac{2\pi x}{L}$

$(2)$ 式に境界条件・初期条件を適用して、

$$
\begin{cases}
    \sum_{\omega}
    e^{-\omega t} C_\omega = 0
    \\ \\
    \sum_{\omega}
    e^{-\omega t} \left(
        S_\omega \sin \sqrt{\cfrac{\omega}{\kappa}}L +
        C_\omega \cos \sqrt{\cfrac{\omega}{\kappa}}L
    \right)
    = 0
    \\ \\
    \sum_{\omega}
    \left(
        S_\omega \sin \sqrt{\cfrac{\omega}{\kappa}}x +
        C_\omega \cos \sqrt{\cfrac{\omega}{\kappa}}x
    \right)
    =
    U_0 \sin \cfrac{2\pi x}{L}
\end{cases}
$$

第1式が任意の時刻 $t$ で成り立つためには、

$$
C_\omega = 0
$$

第2式に代入して、

$$
\sum_{\omega}
e^{-\omega t} S_\omega \sin \sqrt{\cfrac{\omega}{\kappa}}L = 0
$$

これが任意の時刻 $t$ で成り立ち、かつ、$C_\omega=S_\omega=0$ のような無意味な解にならないためには、

$$
\begin{eqnarray}
    &\sqrt{\cfrac{\omega}{\kappa}}L = n\pi \quad (n = 1, 2, \cdots)
    \\ \Longleftrightarrow \quad &
    \omega = \kappa \left( \cfrac{n\pi}{L} \right)^2
\end{eqnarray}
$$

以上を第3式に代入し、以後 $n$ を用いて議論するために $S_\omega \to S(n)$ と書き換えると、

$$
\sum_{n=1}^\infty
S(n) \sin \cfrac{n\pi x}{L}
=
U_0 \sin \cfrac{2\pi x}{L}
$$

これらが任意の $x$ について成り立つため、

$$
\begin{cases}
    S(n)  = U_0
    \qquad &(\mathrm{if}\quad n=2)
    \\ \\
    S(n)  = 0
    \qquad &(\mathrm{if}\quad n \ne 2)
\end{cases}
$$

以上により、

$$
u(x,t) = U_0 \exp{\left\{ -\kappa \left( \cfrac{2\pi}{L} \right)^2 t \right\}} \sin \cfrac{2\pi x}{L}
$$

![diffusion-eq-const](https://gist.github.com/assets/13412823/b8d05985-a043-4f2d-bd6f-319f9019945d)

（cf. [描画に使った python コード](https://gist.github.com/hkawabata/4cb052a95ff294e143b09aee4b55bd95#file-u-x-t-animation-py)）


### 外部とのやりとりがない

定義域を $0 \le x \le L,\ 0 \le t$ として、

- 境界条件：
    - $\cfrac{\partial u}{\partial x}(0,t) = 0$
    - $\cfrac{\partial u}{\partial x}(L, t) = 0$
- 初期条件：
    - 初期濃度：$u(x, 0) = U_0 \cos \cfrac{2\pi x}{L}$

$(2)$ 式に境界条件・初期条件を適用して、

$$
\begin{cases}
    \sum_{\omega}
    e^{-\omega t} \sqrt{\cfrac{\omega}{\kappa}} S_\omega
    = 0
    \\ \\
    \sum_{\omega}
    e^{-\omega t} \sqrt{\cfrac{\omega}{\kappa}} \left(
        S_\omega \cos \sqrt{\cfrac{\omega}{\kappa}} L -
    C_\omega \sin \sqrt{\cfrac{\omega}{\kappa}} L
    \right)
    = 0
    \\ \\
    \sum_{\omega}
    \left(
        S_\omega \sin \sqrt{\cfrac{\omega}{\kappa}}x +
        C_\omega \cos \sqrt{\cfrac{\omega}{\kappa}}x
    \right)
    =
    U_0 \cos \cfrac{2\pi x}{L}
\end{cases}
$$

第1式が任意の時刻 $t$ で成り立つためには、

$$
S_\omega = 0
$$

第2式に代入して、

$$
- \sum_{\omega}
e^{-\omega t} \sqrt{\cfrac{\omega}{\kappa}} C_\omega \sin \sqrt{\cfrac{\omega}{\kappa}}L = 0
$$

これが任意の時刻 $t$ で成り立ち、かつ、$S_\omega=C_\omega=0$ のような無意味な解にならないためには、

$$
\begin{eqnarray}
    &\sqrt{\cfrac{\omega}{\kappa}}L = n\pi \quad (n = 1, 2, \cdots)
    \\ \Longleftrightarrow \quad &
    \omega = \kappa \left( \cfrac{n\pi}{L} \right)^2
\end{eqnarray}
$$

以上を第3式に代入し、以後 $n$ を用いて議論するために $C_\omega \to C(n)$ と書き換えると、

$$
\sum_{n=1}^\infty
C(n) \cos \cfrac{n\pi x}{L}
=
U_0 \cos \cfrac{2\pi x}{L}
$$

これらが任意の $x$ について成り立つため、

$$
\begin{cases}
    C(n)  = U_0
    \qquad &(\mathrm{if}\quad n=2)
    \\ \\
    C(n) = 0
    \qquad &(\mathrm{if}\quad n \ne 2)
\end{cases}
$$

以上により、

$$
u(x,t) = U_0 \exp{\left\{ -\kappa \left( \cfrac{2\pi}{L} \right)^2 t \right\}} \cos \cfrac{2\pi x}{L}
$$

![diffusion-eq-dannetsu](https://gist.github.com/assets/13412823/611c2afb-d75c-4902-bc09-991012c8e832)

（cf. [描画に使った python コード](https://gist.github.com/hkawabata/4cb052a95ff294e143b09aee4b55bd95#file-u-x-t-animation-py)）
