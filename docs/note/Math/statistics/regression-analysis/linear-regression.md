---
title: 線形回帰
title-en: Linear Regression
---

# 線形回帰とは

実際に得られた標本から、目的変数 $Y$ を説明変数 $X$ の一次式で表現する回帰分析の手法。

$$
Y = aX + b \tag{1}
$$

# 回帰方程式の導出

目的変数 $Y$、説明変数 $X$ の $n$ 件の標本 $(x_1, y_1), \cdots, (x_n, y_n)$ が得られているとする。  
$X, Y$ の間の関係性を表すモデルとして線形関係 $(1)$ を仮定するとき、最小二乗法によりパラメータ $a, b$ を求める。

標本 $(x_k, y_k)$ に含まれるモデルからの誤差は

$$
\varepsilon_k := y_k - (a x_k + b)
$$

**残差平方和**：

$$
S := \sum_{k=1}^n \varepsilon_k^2 = \sum_{k=1}^n (y_k - a x_k - b)^2
$$

を定義し、これを最小化するようなパラメータ $a, b$ を求めれば良い。

$X, Y$ の標本平均を $\bar{x}, \bar{y}$ として、

$$
\begin{eqnarray}
	\cfrac{\partial S}{\partial a} &=& -2 \sum_{k=1}^n x_k (y_k - a x_k - b)
	\\ &=&
	-{2} \left(
		\sum_{k=1}^n x_k y_k
		- a \sum_{k=1}^n x_k^2
		- b n \bar{x}
	\right)
	\\
	\\
	\cfrac{\partial S}{\partial b} &=& -2 \sum_{k=1}^n (y_k - a x_k - b)
	\\ &=&
	-2 \left(
		n \bar{y}
		- an \bar{x} - nb
	\right)
\end{eqnarray}
$$

これらをゼロと置いた解が求める $a, b$ であるから、

$$
\begin{eqnarray}
	a &=& \cfrac{
		\sum_{k=1}^n x_k y_k - n \bar{x} \bar{y}
	}{
		\sum_{k=1}^n x_k^2 - n \bar{x}^2
	}
	=
	\cfrac{
		\sum_{k=1}^n (x_k - \bar{x}) (y_k - \bar{y})
	}{
		\sum_{k=1}^n (x_k - \bar{x})^2
	}
	= \cfrac{Cov(x, y)}{V(x)}
	\\
	b &=& \bar{y} - a \bar{x}
	=
	\bar{y} - \cfrac{Cov(x, y)}{V(x)} \bar{x}
\end{eqnarray}
$$



# 線形回帰に帰着できる非線形回帰モデル

## 弾性モデル

$$
Y = \beta X^\alpha
$$

両辺の対数を取ると、

$$
\log Y = \log \beta + \alpha \log X
$$

以下の置き換えにより線形回帰の式 $(1)$ にできる。

- $\log Y \to Y'$
- $\log X \to X'$
- $\log \alpha \to a$
- $\log \beta \to b$

## 指数回帰

$$
Y = \beta \alpha^X
$$

両辺の対数を取ると、

$$
\log Y = \log \beta + X \log \alpha
$$

以下の置き換えにより線形回帰の式 $(1)$ にできる。

- $\log Y \to Y'$
- $\log \alpha \to a$
- $\log \beta \to b$
