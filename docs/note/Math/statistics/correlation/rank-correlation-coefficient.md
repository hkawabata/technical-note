---
title: 順位相関係数
title-en: Rank Correlation Coefficient
---

# 順位相関係数とは

$n$ 個のデータ $d_1, d_2, \cdots, d_n$ を2つの基準 $S, S'$ によって順位付けする場合を考える。  
このとき、この順位付け基準 $S, S'$ に相関があるかどうかを **順位相関係数** によって評価できる。


# 定式化

- $i$ 番目のデータ $d_i$ を基準 $S, S'$ によって順位付けした値をそれぞれ $R_i, R'_i$ とする
- $R_i, R'_i$ の平均値をそれぞれ $\bar{R}, \bar{R'}$ とする

## スピアマンの順位相関係数

### 定義

2つの変数 $R_i, R'_i$ に対して、一般的な相関係数の式を適用した

$$
\begin{eqnarray}
	r_S &:=& \cfrac{
		\displaystyle \sum_{i=1}^n (R_i - \bar{R}) (R'_i - \bar{R'})
	}{
		\displaystyle
		\sqrt{ \sum_{i=1}^n (R_i - \bar{R})^2 }
		\sqrt{ \sum_{i=1}^n (R'_i - \bar{R'})^2 }
	}
	\\ &=&
	1 - \cfrac{6}{n^3-n} \sum_{i=1}^n (R_i - R'_i)^2
	\tag{1}
\end{eqnarray}
$$

を **スピアマンの順位相関係数** という。

### 導出

$R_i$ は $n$ 個の観測対象につけられる順位であるから、$R_1, \cdots, R_n$ は $1, 2, \cdots, n$ の値のいずれかを重複なく取る。

したがって、

$$
\begin{eqnarray}
	\sum_{i=1}^n R_i &=& 1 + 2 + \cdots + n = \sum_{k=1}^n k = \cfrac{n(n+1)}{2}
	\tag{2}
	\\
	\\
	\sum_{i=1}^n R_i^2
	&=&
	1^2 + 2^2 + \cdots + n^2
	=
	\sum_{k=1}^n k^2
	=
	\cfrac{n(n+1)(2n+1)}{6}
	\tag{3}
	\\
	\\
	\bar{R} &=& \cfrac{1}{n} \sum_{i=1}^n R_i = \cfrac{n+1}{2}
	\tag{4}
	\\
	\\
	\sum_{i=1}^n (R_i-\bar{R})^2
	&=&
	\sum_{i=1}^n R_i^2 -
	2 \bar{R} \sum_{i=1}^n R_i +
	\bar{R}^2 \sum_{i=1}^n 1
	\\ &=&
	\cfrac{n(n+1)(2n+1)}{6} -
	2 \cdot \cfrac{n+1}{2} \cdot \cfrac{n(n+1)}{2} +
	\left( \cfrac{n+1}{2} \right)^2 \cdot n
	\\ &=&
	\cfrac{n(n+1)(n-1)}{12}
	= \cfrac{n^3-n}{12}
	\tag{5}
\end{eqnarray}
$$

$R'_i, \bar{R'}$ についても同様に計算できる。  

$(2),(4)$ 式を用いて、

$$
\begin{eqnarray}
	\sum_{i=1}^n (R_i - \bar{R}) (R'_i - \bar{R'})
	&=&
	\sum_{i=1}^n R_i R'_i +
	\bar{R} \bar{R'} \sum_{i=1}^n 1 -
	\bar{R} \sum_{i=1}^n R'_i -
	\bar{R'} \sum_{i=1}^n R_i
	\\ &=&
	\sum_{i=1}^n R_i R'_i +
	\cfrac{n+1}{2} \cdot \cfrac{n+1}{2} \cdot n -
	\cfrac{n+1}{2} \cdot \cfrac{n(n+1)}{2} \times 2
	\\ &=&
	\sum_{i=1}^n R_i R'_i -
	\cfrac{n(n+1)^2}{4}
	\tag{6}
\end{eqnarray}
$$

ここで、

$$
\begin{eqnarray}
	\sum_{i=1}^n (R_i - R'_i)^2
	&=&
	\sum_{i=1}^n R_i^2 +
	\sum_{i=1}^n {R'_i}^2 -
	2 \sum_{i=1}^n R_i R'_i
	\\ &=&
	\cfrac{n(n+1)(2n+1)}{6} \times 2 -
	2 \sum_{i=1}^n R_i R'_i
\end{eqnarray}
$$

であるから、これを $\displaystyle \sum_{i=1}^n R_i R'_i$ について解いて $(6)$ に代入すると、

$$
\begin{eqnarray}
	\sum_{i=1}^n (R_i - \bar{R}) (R'_i - \bar{R'})
	&=&
	- \cfrac{1}{2} \sum_{i=1}^n (R_i - R'_i)^2 +
	\cfrac{n(n+1)(2n+1)}{6} -
	\cfrac{n(n+1)^2}{4}
	\\ &=&
	\cfrac{n^3-n}{12} -
	\cfrac{1}{2} \sum_{i=1}^n (R_i - R'_i)^2
	\tag{7}
\end{eqnarray}
$$

$(5),(7)$ を $r_S$ の定義式に代入すると、

$$
r_S
=
\cfrac{
	\displaystyle 
	\cfrac{n^3-n}{12} -
	\cfrac{1}{2} \sum_{i=1}^n (R_i - R'_i)^2
}{
	\displaystyle
	\sqrt{ \cfrac{n^3-n}{12} }
	\sqrt{ \cfrac{n^3-n}{12} }
}
=
1 - \cfrac{6}{n^3-n} \sum_{i=1}^n (R_i - R'_i)^2
$$

以上により、$(1)$ が示された。


### 性質

> **【定理】**
> 
> 2つの順位が完全に一致するとき、$r_S = 1$

**【証明】**

順位が完全に一致するので、

$$
R'_i = R_i
$$

よって、

$$
r_S = 1 - \cfrac{6}{n^3-n} \sum_{i=1}^n 0^2 = 1
$$

> **【定理】**
> 
> 2つの順位が完全に逆順であるとき、$r_S = -1$

**【証明】**

2つの順位が完全に逆順のとき、$(R_i, R'_i)$ が取り得る組み合わせは

$$
(R_i, R'_i) = (1, n), (2, n-1), (3, n-2), \cdots, (n, 1)
$$

よって

$$
\begin{eqnarray}
	& R_i + R'_i = n + 1
	\\ \Longrightarrow \ & R'_i = n + 1 - R_i
\end{eqnarray}
$$

これを $(1)$ に代入すると、

$$
\begin{eqnarray}
	r_S
	&=&
	1 - \cfrac{6}{n^3-n} \sum_{i=1}^n (2R_i - (n + 1))^2
	\\ &=&
	1 - \cfrac{6}{n^3-n}
	\left(
		4 \sum_{i=1}^n R_i^2 +
		(n+1)^2 \sum_{i=1}^n 1 -
		4(n+1) \sum_{i=1}^n R_i
	\right)
	\\ &=&
	1 - \cfrac{6}{n^3-n}
	\left(
		4 \cdot \cfrac{n(n+1)(2n+1)}{6} +
		(n+1)^2 \cdot n -
		4(n+1) \cdot \cfrac{n(n+1)}{2}
	\right)
	\\ &=&
	1 - \cfrac{6}{n^3-n} \cdot \cfrac{n^3-n}{3}
	\\ &=&
	-1
\end{eqnarray}
$$

式変形の途中、$(2),(3)$ を用いた。


## ケンドールの順位相関係数

### 定義

2つのデータ $d_i, d_j$ の全ての組み合わせ（$i \ne j$、$_n \mathrm{C}_2$ 通り）について、

- **正順**：「$R_i \lt R_j$ かつ $R'_i \lt R'_j$」または「$R_i \gt R_j$ かつ $R'_i \gt R'_j$」
	- すなわち、2つの基準 $S, S'$ による順位の大小関係が同じ
- **逆順**：「$R_i \lt R_j$ かつ $R'_i \gt R'_j$」または「$R_i \lt R_j$ かつ $R'_i \gt R'_j$」
	- すなわち、2つの基準 $S, S'$ による順位の大小関係が逆

を調べる。

正順となる組の個数を $G$、逆順となる組の個数を $H$ として、

$$
r_K := \cfrac{G-H}{_n \mathrm{C}_2} = \cfrac{G-H}{n(n-1)/2}
$$

を **ケンドールの順位相関係数** という。


### 性質

> **【定理】**
> 
> - 2つの順位が完全に一致するとき、$r_K = 1$
> - 2つの順位が完全に逆順であるとき、$r_K = -1$

**【証明】**

- 完全に一致するときは全ての $(i, j)$ の組（$i \ne j$）が正順となるから、$G = {_n}\mathrm{C}_2, H = 0$
- 完全に逆順であるとき全ての $(i, j)$ の組（$i \ne j$）が逆順となるから、$G = 0, H = {_n}\mathrm{C}_2$

よって明らか。