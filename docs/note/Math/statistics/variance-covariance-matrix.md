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

## 正定値行列

> **【定理】**
> 
> 分散共分散行列は正定値行列である

**【証明】**



## 固有ベクトルの内積

- 正定値行列であることを使うと固有ベクトルの内積は0か1
