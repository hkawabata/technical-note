---
title: ローラン展開
title-en: Laurent Series Expansion
---
# ローラン展開とは

$x=x_0$ 近傍において無限回微分可能な関数 $f(x)$ の[テイラー展開](taylor-expantion.md)

$$
\begin{eqnarray}
    f(x)
    &=&
    \sum_{n=0}^{\infty} a_n (x-x_0)^n
    \\
    a_n &=& \cfrac{f^{(n)}(x_0)}{n!}
\end{eqnarray}
$$

は、複素数 $z$ の関数 $f(z)$ にも適用できる。  
テイラー展開の拡張として、$f(z)$ が $z=z_0$ 近傍で特異である（解析的でない）場合であっても、負のべき項

$$
\sum_{n=1}^{\infty} \cfrac{b_n}{(z-z_0)^n}
=
\cfrac{b_1}{z-z_0} + \cfrac{b_2}{(z-z_0)^2} + \cfrac{b_3}{(z-z_0)^3} + \cdots
$$

を考慮すれば、$f(z)$ をべき級数に展開できる：

$$
f(z)
=
\sum_{n=0}^{\infty} a_n (z-z_0)^n
+
\sum_{n=1}^{\infty} \cfrac{b_n}{(z-z_0)^n}
$$

この展開操作を、$f(z)$ の $z=z_0$ まわりの **ローラン展開** といい、得られるべき級数を **ローラン級数** という。

また、この式の2つ目の和の部分（負のべき項全体）をまとめて **特異部** という。


# ローラン級数の係数と留数

ローラン展開の係数 $a_n, b_n$ は、複素平面上で $z_0$ の周りを一周する閉曲線経路 $C$ 上の線積分

$$
\begin{eqnarray}
    a_n &=& \cfrac{1}{2\pi i} \oint_C \cfrac{f(z)}{(z-z_0)^{n+1}} dz
    \\
    b_n &=& \cfrac{1}{2\pi i} \oint_C (z-z_0)^{n-1} f(z) dz
\end{eqnarray}
$$

で計算できる。  
ただし、$C$ は以下の条件を満たす必要があり、条件を満たせばどんな形でも良い（一般に、計算しやすい円形経路が用いられる）。
- 単純閉曲線である（自分自身と交わらず一周する）
- 反時計回りの経路である
- 以下の条件を満たす領域 $D$ 内の経路である
    - $z=z_0$ を中心とする2つの同心円で挟まれる
    - 領域 $D$ 内では $f(z)$ は無限回微分可能

![laurent-series-expansion](https://user-images.githubusercontent.com/13412823/285735036-ea17a4a9-d73c-40dc-9f63-8a8c274a86aa.png)


※ 実際の計算では積分ではなくテイラー展開を利用して係数を求めることが多い（後述の計算例を参照）

特に $-1$ 次の係数 $b_1$ は、$f(z)$ の $z=z_0$ における[留数](residue-theorem.md) $\mathrm{Res}(f,z_0)$ になっている。

# ローラン展開の性質

## ローラン展開と部分分数分解

> **【定理】**
> 
> $z=z_0$ で正則な複素関数 $g(z)$ を用いて、複素関数 $f(z)$ を
> 
> $$
\begin{eqnarray}
    f(z) &=& g(z) + \cfrac{b_1}{z-z_0} + \cfrac{b_2}{(z-z_0)^2} + \cfrac{b_3}{(z-z_0)^3} + \cdots
    \\ &=&
    g(z) + \sum_{n=1}^\infty \cfrac{b_n}{(z-z_0)^n}
\end{eqnarray}
$$
> という形式で表せる時、右辺の $g(z)$ 以外の和の部分は、$f(z)$ の $z=z_0$ まわりのローラン展開の特異部となる。

**【証明】**

$g(z)$ は $z=z_0$ で正則なので、このまわりでテイラー展開できる：

$$
g(z) = \sum_{n=0}^\infty a_n (z-z_0)^n
$$

よって、

$$
\begin{eqnarray}
    f(z) &=& g(z) + \sum_{n=1}^\infty \cfrac{b_n}{(z-z_0)^n}
    \\ &=&
    \sum_{n=0}^\infty a_n (z-z_0)^n + \sum_{n=1}^\infty \cfrac{b_n}{(z-z_0)^n}
\end{eqnarray}
$$

これはまさにローラン展開そのものであり、2つ目の和は負のべき項の部分（特異部）。

> **【NOTE】**
> 
> この性質は、部分分数分解を利用して複素関数の[留数](residue-theorem.md)を求める時に便利。
> たとえば $f(z) = \cfrac{1}{z(z-1)^2}$ を部分分数分解すると
> 
> $$
f(z) = \cfrac{-1}{z-1} + \cfrac{1}{(z-1)^2} + \cfrac{1}{z}
$$
> 
> であり、上の定理から、$z=1$ まわりのローラン展開の特異部が $\cfrac{-1}{z-1} + \cfrac{1}{(z-1)^2}$、$z=0$ まわりのローラン展開の特異部が $\cfrac{1}{z}$ であることが分かる。留数はローラン展開の $-1$ 次の項の係数であるから、
> 
> $$
\begin{eqnarray}
    \mathrm{Res}(f, 1) &=& -1
    \\
    \mathrm{Res}(f, 0) &=& 1
\end{eqnarray}
$$

# ローラン展開の計算例

> $f(z) = \cfrac{1}{z(z+2)}$ の $z=0$ まわりのローラン展開を求める

$\cfrac{1}{z+2}$ は $z=0$ のまわりでテイラー展開可能なので、

$$
\begin{eqnarray}
    f(z)
    &=&
    \cfrac{1}{z(z+2)}
    \\ &=&
    \cfrac{1}{z} \left( \cfrac{1}{0!(0+2)}
        - \cfrac{1}{1!(0+2)^2} z
        + \cfrac{1 \cdot 2}{2!(0+2)^3} z^2
        - \cfrac{1 \cdot 2 \cdot 3}{3!(0+2)^4} z^3
        + \cfrac{1 \cdot 2 \cdot 3 \cdot 4}{4!(0+2)^5} z^4
        - \cdots
    \right)
    \\ &=&
    \cfrac{1}{2z} - \cfrac{1}{2^2} + \cfrac{1}{2^3} z
    - \cfrac{1}{2^4} z + \cfrac{1}{2^5} z - \cdots
    \\ &=&
    \cfrac{1}{2z} + \sum_{n=0}^\infty \cfrac{(-1)^{n+1}}{2^{n+2}} z^n
\end{eqnarray}
$$


> $f(z) = \cfrac{e^{3z}}{(z-1)^2}$ の $z=1$ まわりのローラン展開を求める

$e^z$ は $z=1$ のまわりでテイラー展開可能なので、

$$
\begin{eqnarray}
    f(z)
    &=&
    \cfrac{e^{3z}}{(z-1)^2}
    \\ &=&
    \cfrac{1}{(z-1)^2} \left( \cfrac{e^0}{0!} (z-1)^0 + \cfrac{3e^0}{1!} (z-1)^1 + \cfrac{3^2e^0}{2!} (z-1)^2 + \cfrac{3^3e^0}{3!} (z-1)^3 + \cdots \right)
    \\ &=&
    \cfrac{1}{(z-1)^2} \left( 1 + \cfrac{3}{1!} (z-1) + \cfrac{3^2}{2!} (z-1)^2 + \cfrac{3^3}{3!} (z-1)^3 + \cdots \right)
    \\ &=&
    \cfrac{1}{(z-1)^2} + \cfrac{3}{(z-1)} + \cfrac{3^2}{2!} + \cfrac{3^3}{3!} (z-1) + \cfrac{3^4}{4!} (z-1)^2 + \cdots
    \\ &=&
    \cfrac{1}{(z-1)^2} + \cfrac{3}{(z-1)} +
    \sum_{n=0}^\infty \cfrac{3^{n+2}}{(n+2)!}(z-1)^n
\end{eqnarray}
$$

> $f(z) = \cfrac{1}{\sin z}$ の $z=0$ まわりのローラン展開の **3次以下の項** を求める

分母の $\sin z$ をテイラー展開して、

$$
\begin{eqnarray}
    f(z)
    &=&
    \cfrac{1}{\sin z}
    \\ &=&
    \cfrac{1}{z - \cfrac{1}{3!}z^3 + \cfrac{1}{5!}z^5 - \cfrac{1}{7!}z^7 + \cdots}
    \\ &=&
    \cfrac{1}{z} \cdot
    \cfrac{1}{1 - \cfrac{1}{3!}z^2 + \cfrac{1}{5!}z^4 - \cfrac{1}{7!}z^6 + \cdots}
    \\ &=&
    \cfrac{1}{z} \cdot
    \cfrac{1}{1 - \left( \cfrac{1}{3!}z^2 - \cfrac{1}{5!}z^4 + \cfrac{1}{7!}z^6 - \cdots \right)}
\end{eqnarray}
$$

ここで、分母の括弧内をまとめて $w$ と置いて $\cfrac{1}{1-w}$ をローラン展開すれば、

$$
\begin{eqnarray}
    \cfrac{1}{1-w}
    &=&
    \cfrac{1}{1-0} + \cfrac{1}{1!(1-0)^2}w
    + \cfrac{1\cdot 2}{2!(1-0)^3}w^2
    + \cfrac{1 \cdot 2 \cdot 3}{3!(1+0)^4}w^3
    \cdots
    \\ &=&
    1 + w + w^2 + w^3 + \cdots
    \\ &=&
    \sum_{n=0}^\infty w^n
\end{eqnarray}
$$

したがって、

$$
\begin{eqnarray}
    f(z)
    &=&
    \cfrac{1}{z} \sum_{n=0}^\infty w^n
    \\ &=&
    \cfrac{1}{z} \sum_{n=0}^\infty \left(
        \cfrac{1}{3!}z^2 - \cfrac{1}{5!}z^4 + \cfrac{1}{7!}z^6 - \cdots
    \right)^n
\end{eqnarray}
$$


和をとっている部分の各項の次数について考える。  
括弧の中身 ($w$) は $z$ の2次以上の偶数乗の項だけを持つ多項式であるから、
- 和の最低次数の項は、$n=0$ にだけ現れる $z^0$ の項：$1$
- 次に低い次数の項は、$n=1$ にだけ現れる $z^2$ の項：$\cfrac{1}{3!}z^2 = \cfrac{1}{6}z^2$
- 次に低い次数の項は、$n=1,2$ にだけ現れる $z^4$ の項：$-\cfrac{1}{5!}z^4 + \left( \cfrac{1}{3!}z^2 \right)^2 = \cfrac{7}{360}z^4$

以上により、$f(z)$ の $z=0$ まわりのローラン展開を3次の項まで書き出すと、

$$
\begin{eqnarray}
    f(z)
    &=&
    \cfrac{1}{z} \left( 1 + \cfrac{1}{6} z^2 + \cfrac{7}{360} z^4 + \cdots \right)
    \\ &=&
    \cfrac{1}{z} + \cfrac{1}{6} z + \cfrac{7}{360} z^3 + \cdots
\end{eqnarray}
$$
