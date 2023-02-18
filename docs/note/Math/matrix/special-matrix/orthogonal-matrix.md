---
title: 直交行列
title-en: Orthogonal Matrix
---

# 直交行列の定義

転置行列と逆行列が等しくなる実行列 $A$ を **直交行列** と呼ぶ。

$$
A^T = A^{-1}
$$

言い換えると、$I$ を単位行列として

$$
A^T A = A A^T = I
$$

が成り立つ。

参考：直交行列の複素空間への拡張：[ユニタリー行列](unitary-matrix.md)

# 直交行列の性質

## 直交行列の積

> **【定理】** $A, B$ がそれぞれ直交行列であるとき、これらの積 $AB$ も直交行列になる。

**【証明】**

$A, B$ がそれぞれ直交行列なので、$I$ を単位行列として、

$$
A^T A = A A^T = I, B^T B = B B^T = I
$$

よって

$$
\begin{eqnarray}
	(AB)^T (AB) &=& B^T A^T A B
	\\ &=&
	B^T (A^T A) B
	\\ &=&
	B^T I B
	\\ &=&
	B^T B
	\\ &=&
	I
\end{eqnarray}
$$

$(AB)(AB)^T = I$ も同様に示せるので、

$$
(AB)^T(AB) = (AB)(AB)^T = I
$$

したがって、$AB$ も転置行列。

## 直交行列の行列式

> **【定理】** 直交行列 $A$ の行列式は $\det A = \pm 1$

**【証明】**

$$
A^T A = I
$$

の両辺の行列式を計算すると、

$$
\det (A^T A) = \det I
$$

行列式の性質 $\det(AB)=\det A \det B$ と、転置行列の行列式が元の行列の行列式に等しいことから、

$$
\det (A^T A) = \det A^T \det A = \det A \det A = (\det A)^2
$$

また、これと $\det I = 1$ より、

$$
(\det A)^2 = 1
$$

したがって

$$
\det A = \pm 1
$$

## 直交行列の固有値

> **【定理】** 直交行列 $A$ の固有値 $\lambda = \pm 1$

**【証明】**

直交行列 $A$ の固有値 $\lambda$ に対応する固有ベクトルを $\boldsymbol{x}_\lambda$ ($\ne 0$) とすると、

$$
A \boldsymbol{x}_\lambda = \lambda \boldsymbol{x}_\lambda
$$

ここで左辺について自身との内積を取ると、

$$
\begin{eqnarray}
	(A \boldsymbol{x}_\lambda) \cdot (A \boldsymbol{x}_\lambda)
	&=&
	(A \boldsymbol{x}_\lambda)^T(A \boldsymbol{x}_\lambda)
	\\ &=&
	\boldsymbol{x}_\lambda^T A^T A \boldsymbol{x}_\lambda
	\\ &=&
	\boldsymbol{x}_\lambda^T (A^T A) \boldsymbol{x}_\lambda
	\\ &=&
	\boldsymbol{x}_\lambda^T I \boldsymbol{x}_\lambda
	\\ &=&
	\boldsymbol{x}_\lambda^T \boldsymbol{x}_\lambda
	\\ &=&
	|| \boldsymbol{x}_\lambda ||^2
\end{eqnarray}
$$

右辺についても自身との内積を取ると、

$$
\begin{eqnarray}
	(\lambda \boldsymbol{x}_\lambda) \cdot (\lambda \boldsymbol{x}_\lambda)
	&=&
	\lambda^2 (\boldsymbol{x}_\lambda \cdot \boldsymbol{x}_\lambda)
	\\ &=&
	\lambda^2 || \boldsymbol{x}_\lambda ||^2
\end{eqnarray}
$$

したがって、

$$
|| \boldsymbol{x}_\lambda ||^2
=
\lambda^2 || \boldsymbol{x}_\lambda ||^2
$$

$\boldsymbol{x}_\lambda \ne 0$ より、

$$
1 = \lambda^2
$$

すなわち、

$$
\lambda = \pm 1
$$