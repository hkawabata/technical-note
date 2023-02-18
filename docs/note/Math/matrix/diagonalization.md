---
title: 行列の対角化
title-en: Matrix Diagonalization
---

# 行列の対角化とは

$n$ 次正方行列 $A$ に対して、$D := P^{-1}AP$ が[対角行列](special-matrix/diagonal-matrix.md)になるような[正則行列](special-matrix/regular-matrix.md) $P$ が存在するとき、行列 $A$ は **対角化可能** であるといい、この変換操作を **対角化** という。

# 対角化可能であるための必要十分条件

> **【定理】**
> 
> - $n$ 次正方行列 $A$ が対角化可能であるための必要十分条件は、$A$ の固有値ベクトル $\boldsymbol{u}_1, \cdots, \boldsymbol{u}_n$ が線形独立である（$n$ 次元空間の基底とできる）こと
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
また、$P$ は正則であるから、$\boldsymbol{p}_1, \cdots, \boldsymbol{p}_n$ は線形独立である。

以上の議論を反対にたどることで、逆も示すことができる。

また、以上の議論により、以下の定理も得る。

> **【定理】**
> 
> 正方行列 $A$ の対角化で得られる対角行列 $D$ の対角成分 $\lambda_1, \cdots, \lambda_n$ は行列 $A$ の固有値である



