---
title: 順序統計量
title-en: order statistics
---

# 定義

ある分布の母集団から $n$ 件のランダムサンプリングを行い、小さい順に並べたものを

$$
X_1 \le X_2 \le \cdots \le X_n
\tag{1}
$$

とする。$X_k$ を $k$ 番目の **順序統計量** という。


# 順序統計量の分布

母集団から抽出した $n$ 件のサンプルを $x_{(1)}, \cdots, x_{(n)}$ とする。  
※ これらのサンプルについては、大小関係による並べ替えは考えていないことに注意

また、母集団の確率密度関数を $f(x)$、累積分布関数を $F(x)$ とする。


## 最大値の分布

順序統計量の最大値 $X_n$ の分布を考える。  
$X_n$ の累積分布関数 $F_n (x)$ は $X_n$ が $x$ 以下となる確率であり、言い換えれば任意の $i$ について $x_{(i)} \le x$ が成り立つ確率であるから、

$$
\begin{eqnarray}
	F_n(x) &=& P(x_{(1)} \le x \mathrm{\quad and \quad} x_{(2)} \le x \mathrm{\quad and \quad} \cdots \mathrm{\quad and \quad} x_{(n)} \le x)
	\\ &=&
	P(x_{(1)} \le x) P(x_{(2)} \le x) \cdots P(x_{(n)} \le x)
\end{eqnarray}
$$

累積分布関数は確率変数の値が $x$ 以下となる確率であるから、

$$
F(x) = P(x_{(i)} \le x)
$$

よって、

$$
F_n(x) = F(x)^n
\tag{2}
$$

したがって順序統計量の最大値 $X_n$ の確率密度関数 $f_n(x)$ は、$F_n(x)$ を微分して

$$
f_n(x) = \cfrac{d F_n(x)}{d x} = n F(x)^{n-1} f(x)
\tag{3}
$$

## 最小値の分布

順序統計量の最小値 $X_1$ の分布を考える。  
$X_1$ の累積分布関数 $F_1(x)$ は $X_1$ が $x$ 以下となる確率であり、言い換えれば1つ以上の $i$ について $x_{(i)} \le x$ が成り立つ確率であるから、

$$
\begin{eqnarray}
	F_1(x) &=& P(x_{(1)} \le x \mathrm{\quad or \quad} \cdots \mathrm{\quad or \quad} x_{(n)} \le x)
	\\ &=&
	1 - P(x_{(1)} \gt x \mathrm{\quad and \quad} \cdots \mathrm{\quad and \quad} x_{(n)} \gt x)
	\\ &=&
	1 - P(x_{(1)} \gt x) \cdots P(x_{(n)} \gt x)
	\\ &=&
	1 - \left(1 - P(x_{(1)} \le x)\right) \cdots \left(1 - P(x_{(n)} \le x)\right)
	\\ &=&
	1 - (1 - F(x))^n
	\tag{4}
\end{eqnarray}
$$

最大値同様に、最小値 $X_1$ の確率密度関数 $f_1(x)$ は、

$$
f_1(x) = \cfrac{d F_1(x)}{d x} = n (1 - F(x))^{n-1} f(x)
\tag{5}
$$


## k 番目の順序統計量の分布

最小値・最大値と同様に、順序統計量の $k$ 番目に小さい値 $X_k$ の分布を考える。  
$X_k$ の累積分布関数 $F_k(x)$ は $X_k$ が $x$ 以下となる確率であり、言い換えれば $n$ 個のサンプルのうち、$k$ 個以上が $x$ 以下となる確率である。

$n$ 個のうちちょうど $j$ 個のサンプルが $x$ 以下となる確率は

$$
{}_nC_j F(x)^j (1-F(x))^{n-j}
$$

であるから、$j$ を $k$ から $n$ まで変えて足し合わせれば $F_k(x)$ が計算できる：

$$
F_k(x) = \sum_{j=k}^n {}_nC_j F(x)^j (1-F(x))^{n-j}
\tag{6}
$$

よって $X_k$ の確率密度関数 $f_k(x)$ は

$$
\begin{eqnarray}
	f_k(x) &=& \cfrac{d F_k(x)}{d x}
	\\ &=&
	\sum_{j=k}^n {}_nC_j
	\left\{
		j F(x)^{j-1} (1-F(x))^{n-j} -
		(n-j) F(x)^j (1-F(x))^{n-j-1}
	\right\} f(x)
	\\ &=&
	\sum_{j=k}^n {}_nC_j j F(x)^{j-1} (1-F(x))^{n-j} f(x)
	- \sum_{j=k}^{n-1} {}_nC_j (n-j) F(x)^j (1-F(x))^{n-j-1} f(x)
	\\ &=&
	{}_nC_k k F(x)^{k-1} (1-F(x))^{n-k} f(x)
	\\ &&
	+ \sum_{j=k+1}^n {}_nC_j j F(x)^{j-1} (1-F(x))^{n-j} f(x)
	\\ &&
	- \sum_{j=k}^{n-1} {}_nC_j (n-j) F(x)^j (1-F(x))^{n-j-1} f(x)
	\\ &=&
	{}_nC_k k F(x)^{k-1} (1-F(x))^{n-k} f(x)
	\\ &&
	+ \sum_{j=k}^{n-1} {}_nC_{j+1} (j+1) F(x)^j (1-F(x))^{n-j-1} f(x)
	\\ &&
	- \sum_{j=k}^{n-1} {}_nC_j (n-j) F(x)^j (1-F(x))^{n-j-1} f(x)
\end{eqnarray}
$$

3行目の変形では、$(n-j) F(x)^j (1-F(x))^{n-j-1}$ の和を取る際 $j=n$ のときはゼロとなるから $n-1$ までの和だけを取れば良いことを用いた。

ここで、

$$
\begin{eqnarray}
	{}_nC_{j+1} (j+1)
	&=& \cfrac{n!}{(n-j-1)!(j+1)!} (j+1)
	\\ &=& \cfrac{n!}{(n-j-1)!j!}
	\\ &=& \cfrac{n!}{(n-j)!j!} (n-j)
	\\ &=& {}_nC_j (n-j)
\end{eqnarray}
$$

であるから、$f_k(x)$ の計算の最後の2項は符号以外が等しくなり、打ち消し合う。

したがって、

$$
\begin{eqnarray}
	f_k(x) &=& {}_nC_k k F(x)^{k-1} (1-F(x))^{n-k} f(x)
	\\ &=&
	\cfrac{n!}{(k-1)!(n-k)!} F(x)^{k-1} (1-F(x))^{n-k} f(x)
	\tag{7}
\end{eqnarray}
$$

$(6)(7)$ に $k = n, 1$ を代入すると、最大値の式 $(2)(3)$ 、最小値の式 $(4)(5)$ を得る。


