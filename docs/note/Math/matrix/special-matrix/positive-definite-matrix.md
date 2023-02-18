---
title: 正定値行列
title-en: Positive Definite Matrix
---

# 正定値行列・半正定値行列の定義

$A$ が $n$ 次の実対称行列またはエルミート行列であるとき、任意の $n$ 次元列ベクトル $\boldsymbol{x} \ne \boldsymbol{0}$ が

$$
A \boldsymbol{x} \cdot \boldsymbol{x} \gt 0
$$

を満たすとき、$A$ を **正定値行列** という。  
少しだけ条件を緩めて、

$$
A \boldsymbol{x} \cdot \boldsymbol{x} \ge 0
$$

を満たすとき、$A$ を **半正定値行列** という。  

> **【NOTE】**
> 
> 実空間の場合
> 
> $$
A \boldsymbol{x} \cdot \boldsymbol{x} = (A \boldsymbol{x})^T \boldsymbol{x} = \boldsymbol{x}^T A \boldsymbol{x}
$$
> 
> であるから、正定値行列の定義は
> 
> $$
\boldsymbol{x}^T A \boldsymbol{x} \gt 0
$$
> 
> とも書ける。複素数空間でも同様に
> 
> $$
\boldsymbol{x}^* A \boldsymbol{x} \gt 0
$$


# 正定値行列・半正定値行列の性質

## （半）正定値行列となるための必要十分条件

> **【定理】**
> 
> エルミート行列 $A$ について、
> 
> - $P$：$A$ が（半）正定値行列である
> - $Q$：$A$ の固有値が全て正（非負）の実数である
> 
> とすると、$P \Longleftrightarrow Q$ 

以後、証明は正定値行列の場合について行う。半正定値行列の場合も同様に証明できる。

**【$P \Longrightarrow Q$ の証明】**

$A$ の固有値を $\lambda$、それに対応する固有ベクトルを $\boldsymbol{u}$ とすると、

$$
A \boldsymbol{u} \cdot \boldsymbol{u} = \lambda \boldsymbol{u} \cdot \boldsymbol{u} = \lambda | \boldsymbol{u} |^2
$$

$A$ は正定値行列なので、

$$
A \boldsymbol{u} \cdot \boldsymbol{u} \gt 0
$$

よって

$$
\lambda | \boldsymbol{u} |^2 \gt 0
$$

$| \boldsymbol{u} |^2 \gt 0$ なので、$\lambda \gt 0$

**【$Q \Longrightarrow P$ の証明】**

$A$ の固有値を $\lambda_1, \cdots, \lambda_n \gt 0$ とする。

$A$ はエルミート行列なので、正規行列でもある。  
よって、あるエルミート行列 $U$ によって対角行列 $D$ に対角化できる：

$$
D := U^* A U = \begin{pmatrix}
	\lambda_1 &  & O \\
	& \ddots & \\
	O & & \lambda_n
\end{pmatrix}
$$

両辺に左から $U$、右から $U^*$ をかけて、

$$
A = UDU^*
$$

よって任意の列ベクトル $\boldsymbol{x}$ に対して、

$$
\begin{eqnarray}
	A \boldsymbol{x} \cdot \boldsymbol{x}
	&=&
	(A \boldsymbol{x})^* \boldsymbol{x}
	\\ &=&
	\boldsymbol{x}^* A^* \boldsymbol{x}
	\\ &=&
	\boldsymbol{x}^* A \boldsymbol{x} &\qquad (A^* = A)
	\\ &=&
	\boldsymbol{x}^* UDU^* \boldsymbol{x}
	\\ &=&
	(U^* \boldsymbol{x})^* D (U^* \boldsymbol{x})
\end{eqnarray}
$$

ここで

$$
U^* \boldsymbol{x} = \begin{pmatrix}
	a_1 \\
	\vdots \\
	a_n
\end{pmatrix}
$$

とおけば、

$$
\begin{eqnarray}
	A \boldsymbol{x} \cdot \boldsymbol{x}
	&=&
	(U^* \boldsymbol{x})^* D (U^* \boldsymbol{x})
	\\ &=&
	(a_1^*, \cdots, a_n^*)
	\begin{pmatrix}
		\lambda_1 &  & O \\
		& \ddots & \\
		O & & \lambda_n
	\end{pmatrix}
	\begin{pmatrix}
		a_1 \\
		\vdots \\
		a_n
	\end{pmatrix}
	\\ &=&
	a_1^* \lambda_1 a_1 + \cdots + a_n^* \lambda_n a_n
	\\ &=&
	\sum_{i=1}^n \lambda_i |a_i|^2 \gt 0
\end{eqnarray}
$$

これが任意の $\boldsymbol{x}$ に対して成り立つから、$A$ は半正定値行列である。
