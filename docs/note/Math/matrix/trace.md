---
title: 行列のトレース
title-en: Trace of Matrix
---

# 行列のトレースとは

$n$ 次正方行列 $A$ に対して、対角成分 $a_{ii}$ の和を取ったものを $A$ の**トレース** と呼び、$\mathrm{tr}\ A$ で表す。

$$
\mathrm{tr}\ A = \sum_{i=1}^n a_{ii}
$$

# トレースの性質

## 固有値との関係

> **【定理】**
> 
> 正方行列 $A$ に対して、$\mathrm{tr}\ A$ は重複度も含めた $A$ の固有値の和になる

**【証明】**

$n$ 次正方行列 $A$ の特性方程式は、

$$
\det \begin{pmatrix}
	\lambda - a_{11} & -a_{12} & \cdots & -a_{1n} \\
	-a_{21} & \lambda - a_{22} & \cdots & -a_{2n} \\
	\vdots & \vdots & \ddots & \vdots \\
	-a_{n1} & -a_{n2} & \cdots & \lambda - a_{nn}
\end{pmatrix}
= 0
$$

左辺を展開すると、$\lambda$ の $n-2$ 次以下の項を $O(\lambda^{n-2})$ として、

$$
\lambda^n - (a_{11} + \cdots + a_{nn}) \lambda^{n-1} + O(\lambda^{n-2}) = 0
\qquad\qquad (1)
$$

また、$A$ の固有値 $\lambda_1, \cdots, \lambda_n$ は特性方程式の解であるから、この特性方程式は

$$
(\lambda - \lambda_1) (\lambda - \lambda_2) \cdots (\lambda - \lambda_n) = 0
$$

とも書ける。左辺を展開すると、

$$
\lambda^n - (\lambda_1 + \cdots + \lambda_n) \lambda^{n-1} + O(\lambda^{n-2}) = 0
\qquad\qquad (2)
$$

$(1),(2)$ を比較して、

$$
\sum_{i=1}^n \lambda_i = \sum_{i=1}^n a_{ii} = \mathrm{tr}\ A
$$


## 行列の内積

> **【定理】**
> 
> $n$ 次正方行列 $A, B$ に対して、$\mathrm{tr} (AB^T)$ は $A, B$ の内積になる：
> 
> $$\mathrm{tr} (AB^T) = \sum_{i=1}^n \sum_{j=1}^n a_{ij}b_{ij}$$

**【証明】**

行列 $AB^T$ の対角成分 $(AB^T)_{ii}$ は、

$$
(AB^T)_{ii}
= \sum_{j=1}^n a_{ij} (B^T)_{ji}
= \sum_{j=1}^n a_{ij} b_{ij}
$$

したがって、

$$
\mathrm{tr} (AB^T)
= \sum_{i=1}^n (AB^T)_{ii}
= \sum_{i=1}^n \sum_{j=1}^n a_{ij}b_{ij}
$$

## 可換性

> **【定理】**
> 
> $n$ 次正方行列 $A, B$ に対して、
> 
> $$\mathrm{tr}(AB) = \mathrm{tr}(BA)$$

**【証明】**

（ToDo）
