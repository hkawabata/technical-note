---
title: 波動方程式
title-en: wave equation
---
# 定義

時刻 $t$、空間座標 $x$ を変数に持つ関数 $u(x,t)$ に関する偏微分方程式

$$
\cfrac{\partial^2 u}{\partial t^2} = c^2 \cfrac{\partial^2 u}{\partial x^2}
\qquad (c = \mathrm{const.} \gt 0)
\tag{1}
$$

を **波動方程式** という。


# 導出

前提
- $x$ 方向に張られた弦の振動を考える
- $y$ 方向の弦の変位 $u(x,t)$ は十分小さい
- 重力の影響は考えない

弦の密度を $\rho$ とすると、微小な長さ $\Delta x$ あたりの弦の質量は $\rho \Delta x$ となる。  
この微小質量片の運動方程式を立てる。  

![wave-eq](https://gist.github.com/assets/13412823/477a48ec-aced-4c27-b1dd-e6791960cf97)

（cf. [描画に使った python コード](https://gist.github.com/hkawabata/4cb052a95ff294e143b09aee4b55bd95#file-wave-eq-introduction-py)）

弦の張力を $S$ とすれば、図より、質量片にかかる $y$ 方向の力は

$$
F_y = S \sin \theta_{+} - S \sin \theta_{-}
$$

ここで、弦の変位が小さいことから、

$$
\begin{eqnarray}
    \sin \theta_+ &\simeq& \tan \theta_+ &=& \cfrac{u(x+\Delta x)-u(x)}{\Delta x} &\simeq \cfrac{\partial u(x, t)}{\partial x} \\
    \sin \theta_- &\simeq& \tan \theta_- &=& \cfrac{u(x)-u(x-\Delta x)}{\Delta x} &\simeq \cfrac{\partial u(x-\Delta x, t)}{\partial x}
\end{eqnarray}
$$

したがって、

$$
\begin{eqnarray}
    F_y &\simeq& S\left( \cfrac{\partial u(x, t)}{\partial x} - \cfrac{\partial u(x-\Delta x, t)}{\partial x} \right)
    \\ &=&
    S \cfrac{\partial u(x, t)/\partial x - \partial u(x-\Delta x, t)/\partial x}{\Delta x} \Delta x
    \\ &\simeq&
    S \cfrac{\partial^2 u(x, t)}{\partial x^2} \Delta x
\end{eqnarray}
$$

運動方程式を立てると、

$$
\cfrac{\partial^2 u(x, t)}{\partial t^2} \rho \Delta x
=
S \cfrac{\partial^2 u(x, t)}{\partial x^2} \Delta x
$$

したがって

$$
\cfrac{\partial^2 u}{\partial t^2} = \cfrac{S}{\rho} \cfrac{\partial^2 u}{\partial x^2}
$$

$c := \sqrt{S/\rho}$ とすれば、波動方程式 $(1)$ を得る。


# 一般解

変数分離法で解く。

$$
u(x, t) = f(x)g(t)
$$

と置いて $(1)$ に代入すると、


$$
f(x) \cfrac{d^2 g(t)}{d t^2} = c^2 \cfrac{d^2 f(x)}{d x^2} g(t)
$$

よって

$$
\cfrac{1}{g(t)} \cfrac{d^2 g(t)}{d t^2} = c^2 \cfrac{1}{f(x)} \cfrac{d^2 f(x)}{d x^2}
$$

左辺は $t$ だけの式、右辺は $x$ だけの式であるから、これが任意の $x, t$ で成り立つ場合、この式の値は定数。  
この定数を $k$ と置くと、

$$
\begin{eqnarray}
    \cfrac{1}{g(t)} \cfrac{d^2 g(t)}{d t^2} &=& k
    \\
    c^2 \cfrac{1}{f(x)} \cfrac{d^2 f(x)}{d x^2} &=& k
\end{eqnarray}
$$

それぞれを解く。$A_1, A_2, B_1, B_2$ を積分定数として、

$(i)\ k=0$ のとき

$$
\begin{eqnarray}
    f(x) &=& A_1 x + A_2
    \\
    g(t) &=& B_1 t + B_2
\end{eqnarray}
$$

$(ii)\ k \gt 0$ のとき

$$
\begin{eqnarray}
    f(x) &=& A_1 e^{\sqrt{k}x/c} + A_2 e^{-\sqrt{k}x/c}
    \\
    g(t) &=& B_1 e^{\sqrt{k}t} + B_2 e^{-\sqrt{k}t}
\end{eqnarray}
$$


$(iii)\ k \lt 0$ のとき、$k = -\alpha^2$ とおけば

$$
\begin{eqnarray}
    f(x) &=& A_1 \sin \cfrac{\alpha x}{c} + A_2 \cos \cfrac{\alpha x}{c}
    \\
    g(t) &=& B_1 \sin \alpha t + B_2 \cos \alpha t
\end{eqnarray}
$$

$k=0, k\gt 0$ の解は時間とともに発散するため、実際の物理現象を記述するには不適。  
したがって微分方程式 $(1)$ の解は

$$
u_\alpha(x, t) =
\left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
\left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right)
$$

と書ける。  
ここで、任意の $\alpha \in \mathbb{R}$ に対して $(1)$ は成り立つ。また実際に計算してみれば明らかなように、異なる $\alpha = \alpha_1, \alpha_2$ に対してそれらの重ね合わせ（和）である $u_{\alpha_1}(x,t)+u_{\alpha_2}(x,t)$ も $(1)$ を満たす。  
したがって、$(1)$ の一般解は

$$
u(x, t)
=
\sum_{\alpha \in \mathbb{R}}
\left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
\left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right)
\tag{2}
$$

定数 $A_{1\alpha}, A_{2\alpha}, B_{1\alpha}, B_{2\alpha}$ は境界条件や初期条件を課すことで定まる。


# 境界条件と特殊解

## 境界条件

### 固定端の境界条件

固定端では媒質の変位がゼロなので、固定端の座標を $x_0$ とすると境界条件は

$$
u(x_0, t) = 0
$$

これは[ディリクレ条件](../boundary-condition/dirichlet-boundary-condition.md)に相当する。

### 自由端の境界条件

自由端では、隣接する微小質量片と変位を比べた時に差がない。すなわち、

$$
\cfrac{\partial u}{\partial x}(x_0, t) = 0
$$

これは[ノイマン条件](../boundary-condition/neumann-boundary-condition.md)に相当する。


## 特殊解の例

### 固定端

定義域を $0 \le x \le L,\ 0 \le t$ として、

- 境界条件：
    - $u(0,t) = 0$
    - $u(L, t) = 0$
- 初期条件：
    - 初期変位：$u(x, 0) = U_0 \sin \cfrac{2\pi x}{L}$
    - 初速度：$\cfrac{\partial u}{\partial t}(x,0) = V_0 \sin \cfrac{2\pi x}{L}$

$(2)$ 式に境界条件・初期条件を適用して、

$$
\begin{cases}
    \sum_\alpha A_{2\alpha} (B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t) = 0
    \\ \\
    \sum_\alpha \left (A_{1\alpha} \sin \cfrac{\alpha L}{c} + A_{2\alpha} \cos \cfrac{\alpha L}{c} \right)
    \left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right) = 0
    \\ \\
    \sum_\alpha \left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
    B_{2\alpha} = U_0 \sin \cfrac{2\pi x}{L}
    \\ \\
    \sum_\alpha \left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
    \alpha B_{1\alpha} = V_0 \sin \cfrac{2\pi x}{L}
\end{cases}
$$

第1式が任意の時刻 $t$ で成り立ち、かつ $B_1=B_2=0$ という無意味な解にならないためには、

$$
A_{2\alpha} = 0
$$

第2式に代入して、

$$
\sum_\alpha A_{1\alpha} \sin \cfrac{\alpha L}{c}
\left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right) = 0
$$

これが任意の時刻 $t$ で成り立ち、かつ、$B_1=B_2=0$ や $A_1=A_2=0$ のような無意味な解にならないためには、

$$
\begin{eqnarray}
    &\cfrac{\alpha L}{c} = n\pi \quad (n = 0, \pm 1, \pm2, \cdots)
    \\ \Longleftrightarrow \quad &
    \alpha = \cfrac{n\pi c}{L}
\end{eqnarray}
$$

以上を第3〜4式に代入し、式の見やすさのため $A_{1\alpha},B_{1\alpha},B_{2\alpha}\to A_{1n},B_{1n},B_{2n}$ と書きかえれば、

$$
\begin{cases}
    \sum_n A_{1n} B_{2n} \sin \cfrac{n\pi x}{L}
    = U_0 \sin \cfrac{2\pi x}{L}
    \\ \\
    \sum_n \cfrac{n\pi c}{L} A_{1n} B_{1n} \sin \cfrac{n\pi x}{L}
    = V_0 \sin \cfrac{2\pi x}{L}
\end{cases}
$$

これらが任意の $x$ について成り立つため、

$$
\begin{cases}
    A_{1n} B_{2n} = U_0, \quad A_{1n} B_{1n} = \cfrac{LV_0}{2\pi c}
    \qquad &(\mathrm{if}\quad n=2)
    \\ \\
    A_{1n} B_{2n} = 0, \quad A_{1n} B_{1n} = 0
    \qquad &(\mathrm{if}\quad n \ne 2)
\end{cases}
$$

以上により、

$$
u(x, t) = \sin \cfrac{2\pi x}{L}
\left(
    \cfrac{LV_0}{2\pi c} \sin \cfrac{2\pi c t}{L} +
    U_0 \cos \cfrac{2\pi c t}{L}
\right)
$$

![wave-eq-fixed](https://gist.github.com/assets/13412823/d46bec70-aeac-474d-b5b1-44f74c14f8bd)

（cf. [描画に使った python コード](https://gist.github.com/hkawabata/4cb052a95ff294e143b09aee4b55bd95#file-u-x-t-animation-py)）

### 自由端

定義域を $0 \le x \le L,\ 0 \le t$ として、

- 境界条件：
    - $\cfrac{\partial u}{\partial x}(0,t) = 0$
    - $\cfrac{\partial u}{\partial x}(L,t) = 0$
- 初期条件：
    - 初期変位：$u(x, 0) = U_0 \cos \cfrac{2\pi x}{L}$
    - 初速度：$\cfrac{\partial u}{\partial t}(x,0) = V_0 \cos \cfrac{2\pi x}{L}$

$(2)$ 式に境界条件・初期条件を適用して、

$$
\begin{cases}
    \sum_\alpha \cfrac{\alpha}{c} A_{1\alpha} (B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t) = 0
    \\ \\
    \sum_\alpha \cfrac{\alpha}{c} \left (A_{1\alpha} \cos \cfrac{\alpha L}{c} - A_{2\alpha} \sin \cfrac{\alpha L}{c} \right)
    \left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right) = 0
    \\ \\
    \sum_\alpha \left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
    B_{2\alpha} = U_0 \cos \cfrac{2\pi x}{L}
    \\ \\
    \sum_\alpha \left (A_{1\alpha} \sin \cfrac{\alpha x}{c} + A_{2\alpha} \cos \cfrac{\alpha x}{c} \right)
    \alpha B_{1\alpha} = V_0 \cos \cfrac{2\pi x}{L}
\end{cases}
$$

第1式が任意の時刻 $t$ で成り立ち、かつ $B_1=B_2=0$ という無意味な解にならないためには、

$$
A_{1\alpha} = 0
$$

第2式に代入して、

$$
\sum_\alpha \cfrac{\alpha}{c} A_{2\alpha} \sin \cfrac{\alpha L}{c}
\left( B_{1\alpha} \sin \alpha t + B_{2\alpha} \cos \alpha t \right) = 0
$$

これが任意の時刻 $t$ で成り立ち、かつ、$B_1=B_2=0$ や $A_1=A_2=0$ のような無意味な解にならないためには、

$$
\begin{eqnarray}
    &\cfrac{\alpha L}{c} = n\pi \quad (n = 0, \pm 1, \pm2, \cdots)
    \\ \Longleftrightarrow \quad &
    \alpha = \cfrac{n\pi c}{L}
\end{eqnarray}
$$

以上を第3〜4式に代入し、式の見やすさのため $A_{2\alpha},B_{1\alpha},B_{2\alpha}\to A_{2n},B_{1n},B_{2n}$ と書きかえれば、

$$
\begin{cases}
    A_{2n} B_{2n} \cos \cfrac{n\pi x}{L}
    = U_0 \cos \cfrac{2\pi x}{L}
    \\ \\
    \cfrac{n\pi c}{L} A_{2n} B_{1n} \cos \cfrac{n\pi x}{L}
    = V_0 \cos \cfrac{2\pi x}{L}
\end{cases}
$$

これらが任意の $x$ について成り立つため、

$$
\begin{cases}
    A_{2n} B_{2n} = U_0, \quad A_{2n} B_{1n} = \cfrac{LV_0}{2\pi c}
    \qquad &(\mathrm{if}\quad n=2)
    \\ \\
    A_{2n} B_{2n} = 0, \quad A_{2n} B_{1n} = 0
    \qquad &(\mathrm{if}\quad n \ne 2)
\end{cases}
$$

以上により、

$$
u(x, t) = \cos \cfrac{2\pi x}{L}
\left(
    \cfrac{LV_0}{2\pi c} \sin \cfrac{2\pi c t}{L} +
    U_0 \cos \cfrac{2\pi c t}{L}
\right)
$$

![wave-eq-free](https://gist.github.com/assets/13412823/70e4021b-2ffc-44cb-856a-379f6872631d)


