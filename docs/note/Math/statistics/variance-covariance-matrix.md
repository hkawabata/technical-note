---
title: 分散共分散行列
title-en: Variance-Covariance Matrix
---

# 定義

$n$ 個の確率変数 $X_1, X_2, \cdots, X_n$ に対して、

- $V(X_i)$：$X_i$ の分散
- $\mathrm{Cov}(X_i, X_j)$：$X_i, X_j$ の共分散
- $\mu_i$：$X_i$ の平均値

とすると、**分散共分散行列** は以下の式で定義される。

$$
\Sigma := \begin{pmatrix}
	V(X_1) & \mathrm{Cov}(X_1, X_2) & \cdots & \mathrm{Cov}(X_1, X_n) \\
	\mathrm{Cov}(X_2, X_1) & V(X_2) & \cdots & \mathrm{Cov}(X_2, X_n) \\
	\vdots & \vdots & \ddots & \vdots \\
	\mathrm{Cov}(X_n, X_1) & \mathrm{Cov}(X_n, X_2) & \cdots & V(X_n)
\end{pmatrix}
$$

$ij$ 成分の式として表すと、

$$
\Sigma_{ij} = E \left( (X_i-\mu_i)(X_j-\mu_j) \right)
$$

とも書ける。


# 性質

## 半正定値行列

> **【定理】**
> 
> 分散共分散行列は[半正定値行列](../matrix/special-matrix/positive-definite-matrix.md)である

**【証明】**

 母集団の大きさを $N$ とし、確率変数 $X_i$ の $N$ 個のサンプルのうち $k$ 番目のものを $X_i^{(k)}$ で表すと、

$$
\begin{eqnarray}
	\Sigma_{ij} &=& E \left( (X_i-\mu_i)(X_j-\mu_j) \right)
	\\ &=&
	\cfrac{1}{N} \sum_{k=1}^N (X_i^{(k)}-\mu_i)(X_j^{(k)}-\mu_j)
\end{eqnarray}
$$

ここで $Y_i^{(k)} := X_i^{(k)}-\mu_i$ と置いて、列ベクトル

$$
\boldsymbol{y}_i := \begin{pmatrix}
	Y_i^{(1)} \\ \vdots \\ Y_i^{(N)}
\end{pmatrix}
$$

を考えると、

$$
\begin{eqnarray}
	\Sigma_{ij}
	&=&
	\cfrac{1}{N} \sum_{k=1}^N Y_i^{(k)} Y_j^{(k)}
	\\ &=&
	\cfrac{1}{N} \boldsymbol{y}_i^T \boldsymbol{y}_j
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
	\Sigma &=& \cfrac{1}{N} \begin{pmatrix}
		\boldsymbol{y}_1^T \boldsymbol{y}_1 & \cdots & \boldsymbol{y}_1^T \boldsymbol{y}_n \\
		\vdots & \ddots & \vdots \\
		\boldsymbol{y}_n^T \boldsymbol{y}_1 & \cdots & \boldsymbol{y}_n^T \boldsymbol{y}_n
	\end{pmatrix}
	\\ &=&
	\cfrac{1}{N} \begin{pmatrix}
		\boldsymbol{y}_1^T \\ \vdots \\ \boldsymbol{y}_n^T
	\end{pmatrix}
	\left( \boldsymbol{y}_1, \cdots, \boldsymbol{y}_n \right)
	\\ &=&
	\cfrac{1}{N} Y^T Y
	\qquad \qquad \left(
		Y := \left( \boldsymbol{y}_1, \cdots, \boldsymbol{y}_n \right)
	\right)
\end{eqnarray}
$$

以上により、任意の実ベクトル $\boldsymbol{v} \ne \boldsymbol{0}$ に対して、

$$
\begin{eqnarray}
	\Sigma \boldsymbol{v} \cdot \boldsymbol{v}
	&=&
	\boldsymbol{v}^T \Sigma^T \boldsymbol{v}
	\\ &=&
	\boldsymbol{v}^T \Sigma \boldsymbol{v}
	\\ &=&
	\cfrac{1}{N} \boldsymbol{v}^T Y^T Y \boldsymbol{v}
	\\ &=&
	\cfrac{1}{N} (Y\boldsymbol{v})^T Y\boldsymbol{v}
	\\ &=&
	\cfrac{1}{N} |Y\boldsymbol{v}|^2 \ge 0
\end{eqnarray}
$$

が成り立つので、分散共分散行列は半正定値行列である。

