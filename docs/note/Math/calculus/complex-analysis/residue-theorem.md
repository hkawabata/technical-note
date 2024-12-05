---
title: 留数定理
title-en: Residue Theorem
---
# 留数

## 定義

複素関数 $f(z)$ がある領域 $D$ 内で点 $z=z_0$ を除いて[正則](regular-analytic-function.md)である時、$D$ 内部に $z_0$ を囲む単純閉曲線 $C$ を取る。

![laurent-series-expansion](https://user-images.githubusercontent.com/13412823/285735036-ea17a4a9-d73c-40dc-9f63-8a8c274a86aa.png)

$C$ を反時計回りに1周する経路で $f(z)$ を線積分した値

$$
\oint_C f(z) dz
$$

は、経路 $C$ の取り方によらず一定の値になる。  
これを $2\pi i$ で割った値を、$f(z)$ の $z=z_0$ における **留数** と呼び、$\mathrm{Res}(f, z_0)$ のように表す：

$$
\mathrm{Res}(f,z_0) = \cfrac{1}{2\pi i} \oint_C f(z) dz
$$

## 性質

> **【定理】**
> 
> $f(z)$ を[ローラン展開](laurent-series-expansion.md)した式
>
> $$
f(z)
=
\sum_{n=0}^{\infty} a_n (z-z_0)^n
+
\sum_{n=1}^{\infty} \cfrac{b_n}{(z-z_0)^n}
$$
>
> において、$-1$ 次の項の係数 $b_1$ は $f(z)$ の $z=z_0$ における留数 $\mathrm{Res}(f,z_0)$ に一致する。


# 留数定理

## 定理

> **【定理】留数定理**
> 
> 複素関数 $f(z)$ が単純閉曲線 $C$ 内に有限個の特異点 $z=z_1,z_2,\cdots,z_n$ を持ち、$C$ で囲まれた領域内ではこれらの特異点以外で正則な関数であるとする。  
> このとき、$C$ を反時計回りに1周する経路における $f(z)$ の線積分は、各特異点での留数に $2\pi i$ をかけたものの和で計算できる：
> 
> $$
\oint_C f(z) dz = 2\pi i \left\{\mathrm{Res}(f, z_1) + \mathrm{Res}(f, z_2) + \cdots + \mathrm{Res}(f, z_n) \right\}
$$

## 計算例

> - $f(z) = \cfrac{2}{z-1}$
> - $C$：$f(z)$ の特異点 $z=1$ を中心とする半径1の円周

$f(z)$ は $z=1$ 以外の特異点を持たないので、$C$ 内の特異点は $z=1$ のみ。  
留数定理より、

$$
\oint_C f(z) dz = 2\pi i \cdot \mathrm{Res}(f, 1)
$$

次に、留数がローラン展開の $-1$ 次の項の係数と一致することを用いる。

$$
f(z) = \cfrac{2}{z-1}
$$

はすでにローラン展開済みの形式であり、$-1$ 次の項の係数は2。  
したがって、

$$
\oint_C f(z) dz = 2\pi i \cdot \mathrm{Res}(f, 1) = 4\pi i
$$

> - $f(z) = \cfrac{1}{(2z-1)(z-i)}$
> - $C$：$z=0$ を中心とする半径2の円周

$C$ 内部には特異点 $z=1/2,i$ 両方が含まれるので、

$$
\oint_C f(z) dz = 2\pi i (\mathrm{Res}(f,1/2) + \mathrm{Res}(f,i))
$$

$f(z)$ を部分分数分解すると、

$$
\begin{eqnarray}
    f(z) &=& \cfrac{1}{1-2i} \left( \cfrac{2}{2z-1} + \cfrac{-1}{z-i} \right)
    \\ &=&
    \cfrac{1+2i}{5} \left( \cfrac{2}{2z-1} + \cfrac{-1}{z-i} \right)
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
    \mathrm{Res}(f, 1/2) &=& \cfrac{2+4i}{5}
    \\
    \mathrm{Res}(f, i) &=& -\cfrac{1+2i}{5}
\end{eqnarray}
$$

（※ 部分分数分解と留数の関係については[ローラン展開](laurent-series-expansion.md)の「ローラン展開と部分分数分解」を参照）

したがって、

$$
\begin{eqnarray}
    \oint_C f(z) dz &=& 2\pi i (\mathrm{Res}(f,1/2) + \mathrm{Res}(f,i))
    \\ &=&
    2\pi i \left( \cfrac{2+4i}{5} - \cfrac{1+2i}{5} \right)
    \\ &=&
    2\pi i \cfrac{1+2i}{5}
    \\ &=&
    \cfrac{-4+2i}{5} \pi
\end{eqnarray}
$$



## 実関数積分への応用

### 例題1

> $$
S = \int_{-\infty}^\infty \cfrac{1}{x^4 + 1} dx
$$

まず被積分関数を複素関数 $f(z)$ に置き換えて、特異点を求める。  
分母をゼロと置き、$z = re^{i\theta}\,(0 \le r, 0\le \theta \lt 2\pi)$ とすれば、

$$
\begin{eqnarray}
    & z^4 + 1 = 0
    \\
    \Longleftrightarrow\ & r^4 e^{4i\theta} + 1 = 0
    \\
    \Longleftrightarrow\ & r^4 e^{4i\theta} = -1
\end{eqnarray}
$$

両辺で絶対値を取れば $r^4=1$ であり、$r$ 実数かつ $0\le r$ より $r = 1$ となる。  
オイラーの公式より

$$
\cos 4\theta + i \sin 4\theta = -1
$$

よって $n$ を任意の整数として

$$
4\theta = (2n+1)\pi \Longleftrightarrow \theta = \cfrac{2n+1}{4} \pi
$$

$0\le \theta \lt 2\pi$ であるから、

$$
\theta = \cfrac{\pi}{4},\ \cfrac{3\pi}{4},\ \cfrac{5\pi}{4},\ \cfrac{7\pi}{4}
$$

以上により $z^4+1=0$ の解は

$$
\begin{cases}
    z_1 &:=& e^{\pi i/4}  &=& \cfrac{\sqrt{2}}{2}(1+i) \\
    z_2 &:=& e^{3\pi i/4} &=& \cfrac{\sqrt{2}}{2}(-1+i) \\
    z_3 &:=& e^{5\pi i/4} &=& \cfrac{\sqrt{2}}{2}(-1-i) \\
    z_4 &:=& e^{7\pi i/4} &=& \cfrac{\sqrt{2}}{2}(1-i) \\
\end{cases}
$$

の4つであり、これらが $f(z)$ の特異点となる。

次に、以下の2つの曲線からなる反時計回りの積分経路 $C$ を考える。
- $C_1$：十分に大きな正の実数を $R$ として、$z=-R$ と $z=R$ を結ぶ線分
- $C_2$：中心が $z=0$ で半径 $R$ の上半分の半円周 $C_2$

求める積分は、$C_1$ での線積分で $R \to \infty$ の極限を取ったものに等しい：

$$
S = \lim_{R\to\infty} \int_{C_1} f(z) dz
$$

![residue](https://user-images.githubusercontent.com/13412823/285921639-bd1b1ba6-6752-4aee-bc01-4cf6891b7cd9.png)

```python
from matplotlib import pyplot as plt
import numpy as np

th_sing = np.array([1,3,5,7])*np.pi/4.0
x_sing, y_sing = np.cos(th_sing), np.sin(th_sing)
r = 1.8
x = np.arange(-r, r+0.01, 0.001)
y1 = np.zeros(len(x))
y2 = np.sqrt(r**2-x**2)
plt.text(r-0.05,-0.15,'$R$',size=15)
plt.text(-r-0.1,-0.15,'$-R$',size=15)
plt.plot(x, y1, label='$C_1$')
plt.plot(x, y2, label='$C_2$')
plt.fill_between(x, y1, y2, color='red', alpha=0.2)
plt.scatter(x_sing, y_sing, label='Singularity', color='black', marker='x')
plt.grid()
plt.legend()
plt.show()
```

単純閉曲線 $C$ で囲まれる領域には、先に求めた特異点のうち $z_1, z_2=e^{\pi i/4},\ e^{3\pi i/4}$ の2つが含まれる。  
それぞれにおける $f(z)$ の留数は、

$$
\begin{eqnarray}
    \mathrm{Res}(f, z_1)
    &=&
    \lim_{z\to z_1} (z-z_1) f(z)
    =
    \lim_{z\to z_1} \cfrac{z-z_1}{z^4+1}
    \\ &=&
    \lim_{z\to z_1} \cfrac{(z-z_1)'}{(z^4+1)'}
    =
    \lim_{z\to z_1} \cfrac{1}{4z^3}
    \\ &=&
    \cfrac{1}{4z_1^3}
    =
    \cfrac{1}{4} e^{-3\pi i/4}
    \\ &=&
    \cfrac{1}{4} \left( -\cfrac{\sqrt{2}}{2}-\cfrac{\sqrt{2}}{2}i \right)
    \\ &=&
    \cfrac{\sqrt{2}}{8} (-1-i)
    \\
    \\
    \mathrm{Res}(f, z_2)
    &=&
    \lim_{z\to z_2} (z-z_2) f(z)
    =
    \lim_{z\to z_2} \cfrac{z-z_2}{z^4+1}
    \\ &=&
    \lim_{z\to z_2} \cfrac{(z-z_2)'}{(z^4+1)'}
    =
    \lim_{z\to z_2} \cfrac{1}{4z^3}
    \\ &=&
    \cfrac{1}{4z_2^3}
    =
    \cfrac{1}{4} e^{-9\pi i/4}
    \\ &=&
    \cfrac{1}{4} \left( \cfrac{\sqrt{2}}{2}-\cfrac{\sqrt{2}}{2}i \right)
    \\ &=&
    \cfrac{\sqrt{2}}{8} (1-i)
\end{eqnarray}
$$

計算途中、[ロピタルの定理](../lhopital-theorem.md)を用いた。

留数定理より、

$$
\begin{eqnarray}
    \oint_C f(z) dz
    &=&
    2\pi i (\mathrm{Res}(f, z_1) + \mathrm{Res}(f, z_2))
    \\ &=&
    2\pi i \left(
        \cfrac{\sqrt{2}(-1-i)}{8} + \cfrac{\sqrt{2}(1-i)}{8}
    \right)
    \\ &=&
    \cfrac{\sqrt{2}}{2} \pi
\end{eqnarray}
$$

次に、半円周 $C_2$ 上での線積分について考える。  
$C_2$ 上では $\vert z \vert = R$ であるから、$z=Re^{i\theta}\,(0\le\theta\le\pi)$ とおくことができて、

$$
\begin{eqnarray}
    \left\vert \int_{C_2} f(z) dz \right\vert
    &=&
    \left\vert \int_0^\pi \cfrac{iRe^{i\theta}}{R^4 e^{4\pi i} + 1} d\theta \right\vert
    \\ &\le&
    \int_0^\pi \left\vert \cfrac{iRe^{i\theta}}{R^4 e^{4\pi i} + 1} \right\vert d\theta
    \\ &=&
    \int_0^\pi \cfrac{R}{|R^4 e^{4\pi i} + 1|} d\theta
    \\ &\le&
    \int_0^\pi \cfrac{R}{|R^4 e^{4\pi i}| - |1|} d\theta
    \\ &=&
    \int_0^\pi \cfrac{R}{R^4-1} d\theta
    \\ &=&
    \cfrac{R\pi}{R^4-1} \longrightarrow 0 \qquad (R \longrightarrow \infty)
\end{eqnarray}
$$

途中、三角不等式 $\vert a + b \vert \ge \vert a \vert - \vert b \vert$ を用いた。

以上により、


$$
\begin{eqnarray}
    S &=& \int_{-\infty}^\infty \cfrac{1}{x^4 + 1} dx
    \\ &=&
    \lim_{R\to\infty} \int_{C_1} f(z) dz
    \\ &=&
    \lim_{R\to\infty} \left(
        \oint_C f(z) dz - \int_{C_2} f(z) dz
    \right)
    \\ &=&
    \cfrac{\sqrt{2}}{2} \pi - \lim_{R\to\infty} \int_{C_2} f(z) dz
    \\ &=&
    \cfrac{\sqrt{2}}{2} \pi
\end{eqnarray}
$$


### 例題2

> $$
S = \int_0^{2\pi} \cfrac{1}{3+\cos\theta} d\theta
$$

$z = e^{i\theta}$ とおくと、積分区間は複素空間上の半径1の円周を一周する経路。

$$
\begin{eqnarray}
    z &=& e^{i\theta} &=& \cos\theta+i\sin\theta \\
    z^{-1} &=& e^{-i\theta} &=& \cos\theta-i\sin\theta
\end{eqnarray}
$$

なので、

$$
\begin{eqnarray}
    dz &=& ie^{i\theta}d\theta = iz \cdot d\theta
    \\
    \cos\theta &=& \cfrac{z+z^{-1}}{2}
\end{eqnarray}
$$

これを用いて積分を変形すると、

$$
\begin{eqnarray}
    S &=& \oint_{|z|=1} \cfrac{1}{3+(z+z^{-1})/2} \cfrac{dz}{iz}
    \\ &=&
    \cfrac {2}{i} \oint_{|z|=1} \cfrac{1}{z^2 + 6z + 1} dz
    \\ &=&
    \cfrac {2}{i} \oint_{|z|=1}
    \cfrac{1}{(z+3-2\sqrt{2})(z+3+2\sqrt{2})}
    dz
\end{eqnarray}
$$

$f(z) = \cfrac{1}{z^2 + 6z + 1}$ とおけば、複素空間上の円周 $\vert z \vert=1$ の内側にある $f(z)$ の特異点は $z=-3+2\sqrt{2}$ のみ。

したがって、留数定理より

$$
\begin{eqnarray}
    S &=& \cfrac{2}{i} \oint_{|z|=1} f(z) dz
    \\ &=&
    \cfrac{2}{i} \cdot 2\pi i \cdot \mathrm{Res}(f, -3+2\sqrt{2})
    \\ &=&
    4\pi \lim_{z\to -3+2\sqrt{2}} (z+3-2\sqrt{2}) f(z)
    \\ &=&
    4\pi \lim_{z\to -3+2\sqrt{2}} \cfrac{1}{z+3+2\sqrt{2}}
    \\ &=&
    4\pi \cfrac{1}{-3+2\sqrt{2}+3+2\sqrt{2}}
    \\ &=&
    \cfrac{\pi}{\sqrt{2}}
\end{eqnarray}
$$

Python プログラムで検算：

```python
import numpy as np

dtheta = 0.0001
theta = np.arange(0, 2*np.pi, dtheta)
S1 = (1/(3+np.cos(theta))*dtheta).sum()  # 数値的に計算
S2 = np.pi/np.sqrt(2)                    # 解析的に計算
print(S1)
# 2.221445142284287
print(S2)
# 2.221441469079183
```


