---
title: 正規行列
title-en: Normal Matrix
---

# 定義

自身のエルミート転置が可換となる複素正方行列 $A$ を **正規行列** という。

$$
A^* A = A A^*
$$

（$A$ が実行列の場合は $A^TA = AA^T$ ）


# 特殊ケース

- [ユニタリー行列](unitary-matrix.md)
	- [直交行列](special-matrix/orthogonal-matrix.md)
- [エルミート行列](hermitian-matrix.md)
	- [対称行列](symmetric-matrix.md)
- [対角行列](diagonal-matrix.md)

# 性質

## ユニタリー行列を用いた対角化

> **【定理】**
> 
> $n$ 次正方行列 $A$ が正規行列であるとき、$U^*AU$ により $A$ を対角化できるようなユニタリー行列 $U$ が存在する。逆も成り立つ。

**【証明】**

- $P$：$A$ が正規行列である
- $Q$：$U^*AU$ により $A$ を対角化できるようなユニタリー行列 $U$ が存在する

とする。

**【$P \Longrightarrow Q$ の証明】**

（略）

**【$Q \Longrightarrow P$ の証明】**

$A$ を $U$ で対角化した行列を $\Lambda$ とする：

$$
\Lambda := U^* A U = \begin{pmatrix}
	\lambda_1 &  & O \\
	& \ddots & \\
	O & & \lambda_n
\end{pmatrix}
$$

両辺に左から $U$、右から $U^*$ をかけると、ユニタリー行列の性質 $U^* U = UU^* = I$ より、

$$
U\Lambda U^* = A
$$

この式から $A^*$ を計算すると、

$$
A^* = (U\Lambda U^*)^* = (U^*)^* \Lambda^* U^* = U \Lambda^* U^*
$$

よって、

$$
A^* A = (U \Lambda^* U^*)(U\Lambda U^*) = U \Lambda^* \Lambda U^*
$$

$$
A A^* = (U \Lambda U^*)(U\Lambda^* U^*) = U \Lambda \Lambda^* U^*
$$

ここで、

$$
\Lambda = \begin{pmatrix}
	\lambda_1 &  & O \\
	& \ddots & \\
	O & & \lambda_n
\end{pmatrix}
,\qquad
\Lambda^* = \begin{pmatrix}
	\lambda_1^* &  & O \\
	& \ddots & \\
	O & & \lambda_n^*
\end{pmatrix}
$$

であるから、

$$
\Lambda^* \Lambda = \Lambda \Lambda^* = \begin{pmatrix}
	|\lambda_1|^2 &  & O \\
	& \ddots & \\
	O & & |\lambda_n|^2
\end{pmatrix}
$$

以上により、

$$
A^* A = U \Lambda^* \Lambda U^* = U \Lambda \Lambda^* U^* = A A^*
$$
