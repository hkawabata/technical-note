---
title: 行列の対角化
title-en: Matrix Diagonalization
---

# 行列の対角化とは

$n$ 次正方行列 $A$ に対して、$D := P^{-1}AP$ が[対角行列](special-matrix/diagonal-matrix.md)になるような[正則行列](special-matrix/regular-matrix.md) $P$ が存在するとき、行列 $A$ は **対角化可能** であるといい、この変換操作を **対角化** という。

# 対角化可能であるための必要十分条件

> **【定理】**
> 
> - $n$ 次正方行列 $A$ が対角化可能であるための必要十分条件は、$A$ が線形独立な $n$ 個の固有値ベクトル $\boldsymbol{u}_1, \cdots, \boldsymbol{u}_n$ を持つ（固有ベクトルを $n$ 次元空間の基底とできる）こと
> - 具体的には、$\boldsymbol{u}_i$ を列ベクトルと見て横に並べた行列 $P = (\boldsymbol{u}_1, \cdots, \boldsymbol{u}_n)$ を用いて $A$ を対角化できる

**【証明】**

正則行列 $P$ を用いて、

$$
D = P^{-1} A P
$$

で $A$ を対角化できるとする。  
式の両辺に左から $P$ をかけて、

$$
PD = AP
$$

ここで

$$
D = \begin{pmatrix}
	\lambda_1 & & O \\
	& \ddots & \\
	O & & \lambda_n
\end{pmatrix}
$$

と置き、$P$ を列ベクトル $n$ 個を並べた

$$P = (\boldsymbol{p}_1, \cdots, \boldsymbol{p}_n)$$

の形式で表現すると、

$$
\begin{eqnarray}
	AP &=& A (\boldsymbol{p}_1, \cdots, \boldsymbol{p}_n)
	\\ &=&
	(A \boldsymbol{p}_1, \cdots, A \boldsymbol{p}_n)
	\\ \\
	PD &=&
	(\boldsymbol{p}_1, \cdots, \boldsymbol{p}_n)
	\begin{pmatrix}
		\lambda_1 & & O \\
		& \ddots & \\
		O & & \lambda_n
	\end{pmatrix}
	\\ &=&
	(\lambda_1 \boldsymbol{p}_1, \cdots, \lambda_n \boldsymbol{p}_n)
\end{eqnarray}
$$

これと $PD=AP$ より、$i=1,\cdots,n$ について

$$A\boldsymbol{p}_i = \lambda_i \boldsymbol{p}_i$$

これは固有値・固有ベクトルの定義そのもの。  
また、$P$ は正則であるから、固有ベクトル $\boldsymbol{p}_1, \cdots, \boldsymbol{p}_n$ は線形独立である。

以上の議論を反対にたどることで、逆も示すことができる。

また、以上の議論により、以下の定理も得る。

> **【定理】**
> 
> 正方行列 $A$ を対角化して得られる対角行列 $D$ の対角成分 $\lambda_1, \cdots, \lambda_n$ は行列 $A$ の固有値である


# 対角化を使った計算

## 行列の対角化

### 理論

前述の通り、$A$ の固有値と固有ベクトルがわかれば、
- $A$ が対角化可能か判別できる
- $A$ が対角化可能であれば、対角化された対角行列 $D$ と、対角化の計算に使う正則行列 $P$ が求まる

### 具体例

正方行列 $A$ を対角化した行列 $D$ と、その対角化に利用する正則行列 $P$ を求める。

#### 【1】対角化できる場合（固有値に重解なし）

$$
A = \begin{pmatrix}
	3 & 0 & 2 \\
	−3 & 2 & 5 \\
	4 & 0 & 1
\end{pmatrix}
$$

$A$ の固有方程式は

$$
\begin{eqnarray}
	& \det (A-\lambda E) = 0
	\\ \\ \Longleftrightarrow \ &
	\det \begin{pmatrix}
		3-\lambda & 0 & 2 \\
		−3 & 2-\lambda & 5 \\
		4 & 0 & 1-\lambda
	\end{pmatrix}
	= 0
	\\ \\ \Longleftrightarrow \ &
	(\lambda-2)(\lambda-5)(\lambda+1) = 0
\end{eqnarray}
$$

よって $A$ の固有値は $\lambda = -1, 2, 5$  
したがって、固有方程式が重根を持たない（固有値がすべて異なる）ので、固有ベクトルは線形独立となり、**$A$ は対角化可能**。

$A$ を対角化した行列（の1つ）は、固有値を対角成分に並べれば良いから、

$$
D = \begin{pmatrix}
	-1 & 0 & 0 \\
	0 & 2 & 0 \\
	0 & 0 & 5
\end{pmatrix}
$$

次に、それぞれの固有値に対応する固有ベクトル $\boldsymbol{u} = (x, y, z)^T$ を求める。

$\lambda=-1$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = - \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		3x + 2z = -x \\
		-3x + 2y + 5z = -y \\
		4x - z = -z
	\end{cases}
	\\ \Longleftrightarrow \ &
	y = \cfrac{13}{3}x,\ z = -2x
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} = k\begin{pmatrix}3\\13\\-6\end{pmatrix}
	\quad (x = 3k)
\end{eqnarray}
$$

$\lambda=2$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = 2 \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		3x + 2z = 2x \\
		-3x + 2y + 5z = 2y \\
		4x - z = 2z
	\end{cases}
	\\ \Longleftrightarrow \ &
	x = 0,\ z = 0
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} = k\begin{pmatrix}0\\1\\0\end{pmatrix}
	\quad (y = k)
\end{eqnarray}
$$

$\lambda=5$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = 2 \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		3x + 2z = 5x \\
		-3x + 2y + 5z = 5y \\
		4x - z = 5z
	\end{cases}
	\\ \Longleftrightarrow \ &
	y = \cfrac{2}{3}x,\ z = x
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} = k\begin{pmatrix}3\\2\\3\end{pmatrix}
	\quad (x = 3k)
\end{eqnarray}
$$

以上により、$D = P^{-1}AP$ を与える正則行列 $P$（の1つ）は

$$
P = \begin{pmatrix}
	3 & 0 & 3 \\
	13 & 1 & 2 \\
	-6 & 0 & 3
\end{pmatrix}
$$

#### 【2】対角化できる場合（固有値に重解あり）

$$
A = \begin{pmatrix}
	2 & -1 & 1 \\
	0 & 3 & -1 \\
	0 & 0 & 2
\end{pmatrix}
$$

$A$ の固有方程式は

$$
\begin{eqnarray}
	& \det (A-\lambda E) = 0
	\\ \\ \Longleftrightarrow \ &
	\det \begin{pmatrix}
		2-\lambda & -1 & 1 \\
		0 & 3-\lambda & -1 \\
		0 & 0 & 2-\lambda
	\end{pmatrix}
	= 0
	\\ \\ \Longleftrightarrow \ &
	(\lambda-2)^2(\lambda-3) = 0
\end{eqnarray}
$$

よって $A$ の固有値は $\lambda = 2, 2, 3$  
重複度2以上の固有値が存在するため、現時点では対角化できるか分からない。

次に、それぞれの固有値に対応する固有ベクトル $\boldsymbol{u} = (x, y, z)^T$ を求める。

$\lambda=2$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = 2 \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		2x - y + z = 2x \\
		3y - z = 2y \\
		2z = 2z
	\end{cases}
	\\ \Longleftrightarrow \ &
	y = z
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} =
	k\begin{pmatrix}1\\0\\0\end{pmatrix} +
	l\begin{pmatrix}0\\1\\1\end{pmatrix}
\end{eqnarray}
$$

よって、重複度2の固有値 $\lambda = 2$ に対して線形独立な固有ベクトルが2つ存在し、この他に重複度が2以上の固有値は存在しないため、$A$ には独立な $n$ 個の固有ベクトルが存在する。  
したがって、**$A$ は対角化可能**。

$\lambda=3$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = 3 \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		2x - y + z = 3x \\
		3y - z = 3y \\
		2z = 3z
	\end{cases}
	\\ \Longleftrightarrow \ &
	y = -x,\ z = 0
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} =
	k\begin{pmatrix}1\\-1\\0\end{pmatrix}
	\quad (x = k)
\end{eqnarray}
$$

以上により、対角行列 $D = P^{-1}AP$ を与える正則行列 $P$（の1つ）は

$$
P = \begin{pmatrix}
	1 & 0 & 1 \\
	0 & 1 & -1 \\
	0 & 1 & 0
\end{pmatrix}
$$

であり、対角行列 $D$ は

$$
D = \begin{pmatrix}
	2 & 0 & 0 \\
	0 & 2 & 0 \\
	0 & 0 & 3
\end{pmatrix}
$$


#### 【3】対角化できない場合

$$
A = \begin{pmatrix}
	1 & 3 & 2 \\
	0 & -1 & 0 \\
	1 & 2 & 0
\end{pmatrix}
$$

$A$ の固有方程式は

$$
\begin{eqnarray}
	& \det (A-\lambda E) = 0
	\\ \\ \Longleftrightarrow \ &
	\det \begin{pmatrix}
		1-\lambda & 3 & 2 \\
		0 & -1-\lambda & 0 \\
		1 & 2 & -\lambda
	\end{pmatrix}
	= 0
	\\ \\ \Longleftrightarrow \ &
	(\lambda+1)^2(\lambda-2) = 0
\end{eqnarray}
$$

よって $A$ の固有値は $\lambda = -1, -1, 2$  
重複度2以上の固有値が存在するため、現時点では対角化できるか分からない。

次に、それぞれの固有値に対応する固有ベクトル $\boldsymbol{u} = (x, y, z)^T$ を求める。

$\lambda=-1$ のとき、

$$
\begin{eqnarray}
	& A \boldsymbol{u} = - \boldsymbol{u}
	\\ \Longleftrightarrow \ &
	\begin{cases}
		x + 3y + 2z = -x \\
		-y = -y \\
		x + 2y = -z
	\end{cases}
	\\ \Longleftrightarrow \ &
	y = 0,\ z = x
	\\ \Longleftrightarrow \ &
	\boldsymbol{u} = k\begin{pmatrix}1\\0\\-1\end{pmatrix}
	\quad (x = k)
\end{eqnarray}
$$

よって、重複度2の固有値 $\lambda = -1$ に対して線形独立な固有ベクトルが1つしかないので、$A$ には独立な $n$ 個の固有ベクトルが存在しない。  
したがって、**$A$ は対角化できない**。


## 行列のべき乗の計算

### 理論

正方行列 $A$ が正則行列 $P$ で対角化可能であり、$P$ で対角化して得られる対角行列を $D$ とする。

$$
D = P^{-1} A P = \begin{pmatrix}
	\lambda_1 & & O \\
	& \ddots & \\
	O & & \lambda_n
\end{pmatrix}
$$

$A$ について解くと、

$$A = PDP^{-1}$$

よって任意の自然数 $k$ に対して

$$
\begin{eqnarray}
	A^k &=& (PDP^{-1})^k
	\\ &=&
	PDP^{-1}PDP^{-1} \cdots PDP^{-1}
	\\ &=&
	PD(P^{-1}P)D(P^{-1}P)D \cdots (P^{-1}P) D P^{-1}
	\\ &=&
	PD^kP^{-1}
	\\ &=&
	P
	\begin{pmatrix}
		\lambda_1^k & & O \\
		& \ddots & \\
		O & & \lambda_n^k
	\end{pmatrix}
	P^{-1}
\end{eqnarray}
$$

### 具体例

前節と共通の行列

$$
A = \begin{pmatrix}
	3 & 0 & 2 \\
	−3 & 2 & 5 \\
	4 & 0 & 1
\end{pmatrix}
$$

に関して $A^k$ を計算する。  

まず、$P^{-1}$ を求める。吐き出し法により、

$$
\begin{eqnarray}
	& \left( \begin{array}{ccc|ccc}
		3 & 0 & 3 & 1 & 0 & 0 \\
		13 & 1 & 2 & 0 & 1 & 0 \\
		-6 & 0 & 3 & 0 & 0 & 1
	\end{array} \right)
	\\ \\ \longrightarrow \ &
	\left( \begin{array}{ccc|ccc}
		3 & 0 & 3 & 1 & 0 & 0 \\
		11 & 1 & 0 & -\frac{2}{3} & 1 & 0 \\
		0 & 0 & 9 & 2 & 0 & 1
	\end{array} \right)
	\\ \\ \longrightarrow \ &
	\left( \begin{array}{ccc|ccc}
		3 & 0 & 0 & \frac{1}{3} & 0 & -\frac{1}{3} \\
		11 & 1 & 0 & -\frac{2}{3} & 1 & 0 \\
		0 & 0 & 9 & 2 & 0 & 1
	\end{array} \right)
	\\ \\ \longrightarrow \ &
	\left( \begin{array}{ccc|ccc}
		3 & 0 & 0 & \frac{1}{3} & 0 & -\frac{1}{3} \\
		0 & 1 & 0 & -\frac{17}{9} & 1 & \frac{11}{9} \\
		0 & 0 & 9 & 2 & 0 & 1
	\end{array} \right)
	\\ \\ \longrightarrow \ &
	\left( \begin{array}{ccc|ccc}
		1 & 0 & 0 & \frac{1}{9} & 0 & -\frac{1}{9} \\
		0 & 1 & 0 & -\frac{17}{9} & 1 & \frac{11}{9} \\
		0 & 0 & 1 & \frac{2}{9} & 0 & \frac{1}{9}
	\end{array} \right)
\end{eqnarray}
$$

よって

$$
P^{-1} = \begin{pmatrix}
	\frac{1}{9} & 0 & -\frac{1}{9} \\
	-\frac{17}{9} & 1 & \frac{11}{9} \\
	\frac{2}{9} & 0 & \frac{1}{9}
\end{pmatrix}
=
\cfrac{1}{9}
\begin{pmatrix}
	1 & 0 & -1 \\
	-17 & 9 & 11 \\
	2 & 0 & 1
\end{pmatrix}
$$

したがって、

$$
\begin{eqnarray}
	A^k &=& PDP^{-1}
	\\ &=&
	\cfrac{1}{9}
	\begin{pmatrix}
		3 & 0 & 3 \\
		13 & 1 & 2 \\
		-6 & 0 & 3
	\end{pmatrix}
	\begin{pmatrix}
		(-1)^k & 0 & 0 \\
		0 & 2^k & 0 \\
		0 & 0 & 5^k
	\end{pmatrix}
	\begin{pmatrix}
		1 & 0 & -1 \\
		-17 & 9 & 11 \\
		2 & 0 & 1
	\end{pmatrix}
	\\ &=&
	\cfrac{1}{9}
	\begin{pmatrix}
		3\cdot(-1)^k+6\cdot5^k & 0 & -3\cdot(-1)^k+3\cdot5^k \\
		13\cdot(-1)^k-17\cdot2^k+4\cdot5^k & 9\cdot2^k & -13\cdot(-1)^k+11\cdot2^k+2\cdot5^k \\
		-6\cdot(-1)^k+6\cdot5^k & 0 & 6\cdot(-1)^k+3\cdot5^k
	\end{pmatrix}
\end{eqnarray}
$$

cf. [Python プログラムで検算](https://gist.github.com/hkawabata/dc3fde3a6b0ebc3de3f5b7f01e00a6e4)
