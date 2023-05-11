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

2つの変数 $R_i, R'_i$ に対して、一般的な相関係数の式を適用する。

$$
r_s := \cfrac{
  \displaystyle \sum_{i=1}^n (R_i - \bar{R}) (R'_i - \bar{R'})
}{
  \displaystyle
  \sqrt{ \sum_{i=1}^n (R_i - \bar{R})^2 }
  \sqrt{ \sum_{i=1}^n (R'_i - \bar{R'})^2 }
}
=
1 - \cfrac{6}{n^3-n} \sum_{i=1}^n (R_i - R'_i)^2
\tag{1}
$$

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

$(5),(7)$ を用いて $r_s$ の定義式を計算すると、

$$
r_s
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
> 2つの順位が完全に一致するとき、$r_s = 1$

**【証明】**

順位が完全に一致するので、

$$
R'_i = R_i
$$

よって、

$$
r_s = 1 - \cfrac{6}{n^3-n} \sum_{i=1}^n 0^2 = 1
$$

> **【定理】**
> 
> 2つの順位が完全に逆順であるとき、$r_s = -1$

**【証明】**

2つの順位が完全に逆順なので、

$$
R'_i = n + 1 - R_i
$$

よって、

$$
\begin{eqnarray}
	r_s
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



### 性質

