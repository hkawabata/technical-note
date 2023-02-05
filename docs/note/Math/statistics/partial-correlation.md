---
title: 偏相関
title-en: Partial Correlation
---

# 偏相関・擬似相関

**偏相関**：注目する2つの変数 $x, y$ の相関を考える時、単純に相関を調べるのではなく、別の変数 $z$ による影響を除外して考えたもの。

たとえば、「運動量が多いほど高血圧になりにくい」という仮説を検証したいとする。  
このとき、運動量 $x$ と血圧 $y$ の間に相関があったとしても、

- 年齢 $z$ が高いほど疲れやすいので運動しなくなる（運動量 $x$ が小さい）
- 年齢 $z$ が高いほど高血圧になりやすい（血圧 $y$ が高い）

という事情がある場合、運動量と高血圧の間に相関があっても、直接的な因果関係が存在するとは限らない（= **疑似相関**）。  
そのため、年齢 $z$ の影響を取り除いた運動量 $x$ と血圧 $y$ の相関を調べる必要がある。

この例のように、注目する2つの因子 $x, y$ 両方に対して影響を与える第三の因子 $z$ を **交絡因子** と呼ぶ。


# 偏相関係数

## 計算式

$z$ の影響を除いた $x, y$ の偏相関係数 $r_{xy,z}$ は、$r_{xy}$ を $x,y$ の相関係数（$r_{xz}, r_{yz}$ も同様）として、以下の式で計算できる。

$$
r_{xy,z} = \cfrac{r_{xy} - r_{xz} r_{yz}}{\displaystyle \sqrt{1-r_{xz}^2} \sqrt{1-r_{yz}^2}}
$$

## 計算式の導出

### 準備1：分散・共分散の公式

変数 $x$ の期待値・分散を $E(x)$・$V(x)$、変数 $x,y$ の共分散を $\mathrm{Cov}(x,y)$ で表すと、以下の公式が成り立つ。

$$
\begin{eqnarray}
	V(x) &=& E(x^2) - E(x)^2 \\
	\mathrm{Cov}(x, y) &=& E(xy) - E(x)E(y)
\end{eqnarray}
$$

### 準備2：回帰直線の係数

確率変数 $x, y$ の間の最小二乗法による回帰直線

$$
y = a x + b
$$

の係数は、

$$
\begin{eqnarray}
	a &=& \cfrac{\mathrm{Cov}(x, y)}{V(x)} \\
	b &=& E(y) - a E(x)
\end{eqnarray}
$$


### 偏相関係数の導出

相関係数は確率変数間の「線形な」関係性を調べるものであるから、偏相関についても線形な関係を前提として考える。  
$x$ と $z$、$y$ と $z$ の間に相関がある = 線形な関係があると仮定する。  
これらの関係性を示す回帰直線は、定数 $a, b, c, d$ を用いて以下の式で表現できる。

$$
\begin{eqnarray}
	x &=& az + b \\
	y &=& cz + d
\end{eqnarray}
$$

$x$ と $z$、$y$ と $z$ が完全に線形な関係にあれば、全てのサンプルデータに対してこの等式が成り立つ。  
よって、$z$ が与える影響を $x, y$ から除外した変数として、

$$
\begin{eqnarray}
	x' &\equiv& x - (az + b) \\
	y' &\equiv& y - (cz + d)
\end{eqnarray}
$$

を定義できる。

回帰直線の係数の式から、

$$
\begin{eqnarray}
	x' &=& x - (az + b)
	\\ &=&
	x - az - (E(x) - a E(z))
	\\ &=&
	(x-E(x)) - a(z-E(z))
	\\
	y' &=& y - (cz + d)
	\\ &=&
	y - cz - (E(y) - c E(z))
	\\ &=&
	(y-E(y)) - c(z-E(z))
\end{eqnarray}
$$

求める偏相関係数 $r_{xy,z}$ を $x', y'$ の相関係数 $r_{x'y'}$ で定義すると、相関係数の定義と分散・共分散の公式より

$$
\begin{eqnarray}
	r_{xy,z} \equiv r_{x'y'} &=& \cfrac{\mathrm{Cov}(x', y')}{\sqrt{V(x')}\sqrt{V(y')}}
	\\ &=&
	\cfrac{E(x'y') - E(x')E(y')}
	{\sqrt{E(x'^2)-E(x')^2}\sqrt{E(y'^2)-E(y')^2}}
\end{eqnarray}
$$

回帰直線の係数の式を用いて、$E(x'), E(y'), E(x'^2), E(y'^2), E(x'y')$ をそれぞれ計算する。

$$
\begin{eqnarray}
	E(x') &=& E( (x-E(x)) - a(z-E(z)) )
	\\ &=&
	E(x) - E(x) - a E(z) + a E(z)
	\\ &=&
	0
	\\
	\\
	E(y') &=& \cdots
	\\ &=&
	0
	\\
	\\
	E(x'^2) &=&
	E( (x-E(x))^2 - 2a (x-E(x)) (z-E(z)) + a^2 (z-E(z))^2 )
	\\ &=&
	E( (x-E(x))^2 ) - 2a E( (x-E(x)) (z-E(z)) ) + a^2 E( (z-E(z))^2 )
	\\ &=&
	V(x) - 2a \mathrm{Cov}(x, z) + a^2 V(z)
	\\ &=&
	V(x) -
	\cfrac{2 \mathrm{Cov}(x, z)^2}{V(z)} +
	\cfrac{\mathrm{Cov}(x, z)^2}{V(z)}
	\\ &=&
	V(x) -
	\cfrac{\mathrm{Cov}(x, z)^2}{V(z)}
	\\ &=&
	V(x) \left( 1 -
	\cfrac{\mathrm{Cov}(x, z)^2}{V(x) V(z)}
	\right)
	\\ &=&
	V(x) (1 - r_{xz}^2)
	\\
	\\
	E(y'^2) &=& \cdots
	\\ &=&
	V(y) (1 - r_{yz}^2)
	\\
	\\
	E(x'y') &=&
	E(
		( (x-E(x)) - a(z-E(z)) )
		( (y-E(y)) - c(z-E(z)) )
	)
	\\ &=&
	ac E \left( (z-E(z))^2 \right) -
	a E \left( (y-E(y)) (z-E(z)) \right) -
	c E \left( (x-E(x)) (z-E(z)) \right) +
	E \left( (x-E(x)) (y-E(y)) \right)
	\\ &=&
	ac V(z) -
	a \mathrm{Cov}(y, z) -
	c \mathrm{Cov}(x, z) +
	\mathrm{Cov}(x, y)
	\\ &=&
	\cfrac{\mathrm{Cov}(x, z) \mathrm{Cov}(y, z)}{V(z)^2} V(z) -
	\cfrac{\mathrm{Cov}(x, z)}{V(z)} \mathrm{Cov}(y, z) -
	\cfrac{\mathrm{Cov}(y, z)}{V(z)} \mathrm{Cov}(x, z) +
	\mathrm{Cov}(x, y)
	\\ &=&
	\mathrm{Cov}(x, y) -
	\cfrac{\mathrm{Cov}(x, z) \mathrm{Cov}(y, z)}{V(z)}
	\\ &=&
	\sqrt{V(x)}\sqrt{V(y)}
	\left(
		\cfrac{\mathrm{Cov}(x, y)}{\sqrt{V(x)}\sqrt{V(y)}} -
		\cfrac{\mathrm{Cov}(x, z)}{\sqrt{V(x)}\sqrt{V(z)}}
		\cfrac{\mathrm{Cov}(y, z)}{\sqrt{V(y)}\sqrt{V(z)}}
	\right)
	\\ &=&
	\sqrt{V(x)}\sqrt{V(y)} ( r_{xy} - r_{xz} r_{yz} )
\end{eqnarray}
$$

以上を相関係数の式に代入して、

$$
\begin{eqnarray}
	r_{xy,z}　&=&
	\cfrac{E(x'y') - E(x')E(y')}
	{\sqrt{E(x'^2)-E(x')^2}\sqrt{E(y'^2)-E(y')^2}}
	\\　&=&
	\cfrac{
		\sqrt{V(x)}\sqrt{V(y)} ( r_{xy} - r_{xz} r_{yz} ) -
		0 \cdot 0
	}{
		\displaystyle
		\sqrt{V(x) (1 - r_{xz}^2) - 0^2}
		\sqrt{V(y) (1 - r_{yz}^2) - 0^2}
	}
	\\ &=&
	\cfrac{r_{xy} - r_{xz} r_{yz}}{\displaystyle \sqrt{1-r_{xz}^2} \sqrt{1-r_{yz}^2}}
\end{eqnarray}
$$

## 例

Python で相関係数を計算 & 散布図を描画する関数

{% gist 795e3635009c4fdfbf40a148b3eca4c8 partial-correlation.py %}

### 手作りデータ

3変数 $x, y, z$ を、
- $x, y$ が $z$ と相関を持つ（線形の関係）
- $x, y$ は直接的な相関を持たない（$z$ を交絡因子とする疑似相関）

という条件で生成する。

{% gist 795e3635009c4fdfbf40a148b3eca4c8 ~handmade.py %}

![Figure_1](https://user-images.githubusercontent.com/13412823/215377569-b51f0572-b593-404c-83ef-fba3909733bd.png)

- 相関係数 $r_{xy}, r_{yz}, r_{zx}$ を見ると $x, y, z$ は相互に相関がある
- 注目していない変数の影響を除いた偏相関係数 $r_{xy,z}, r_{yz,x}, r_{zx,y}$ を見ると、$x$ と $z$、$y$ と $z$ の間には相関が見られるが、$x$ と $y$ の間には相関がなさそう

→ 期待通り、$x$ と $y$ の間に直接的な関係性がなさそうなことが示されている

### 実データ：ニューヨークの大気の状態

[rdatasets](https://vincentarelbundock.github.io/Rdatasets/articles/data.html) より、ニューヨークの大気状態のデータを利用。

{% gist 795e3635009c4fdfbf40a148b3eca4c8 ~newyork-airquality.py %}

![Figure_1](https://user-images.githubusercontent.com/13412823/215378527-662a7f27-9660-4451-a892-1a12467f65fa.png)

- 気温の影響を除外した場合も、オゾンと風の間には相関がありそう
- 風の影響を除外した場合も、オゾンと気温の間には相関がありそう
- オゾンの影響を除外すると、気温と風の間には直接的な相関はなさそう