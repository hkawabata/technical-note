---
title: 主成分分析（PCA）
---

# 主成分分析（PCA）とは

Principal Component Analysis の略。

## 直感的な理解

（TODO）

## 理論

学習サンプルを射影した際に最も分散が大きくなる方向ベクトル

$$
\boldsymbol{a} =
\begin{pmatrix}
a_1 \\
\vdots \\
a_m
\end{pmatrix}
$$

を求めたい。  
定数倍の自由度を消すため、単位ベクトル条件を課しておく：

$$
\| \boldsymbol{a} \|^2 = \displaystyle \sum_{j=1}^m a_j^2 = 1
$$

データサンプルをこの方向ベクトル上へ射影する。  
サンプルと方向ベクトルとの内積を取れば良いから

$$
X^{(i)} = \boldsymbol{a} \cdot \boldsymbol{x}^{(i)} = \displaystyle \sum_{j=1}^m a_j x_j^{(i)}
$$

射影後の値の標本分散は

$$
\begin{eqnarray}
V(X^{(1)}, \cdots, X^{(n)})
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( X^{(i)} - \overline{X} \right)^2 \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) \right)^2
\end{eqnarray}
$$

これを最大化するような $$\boldsymbol{a}$$ を求める。

単位ベクトル条件下でラグランジュの未定乗数法を適用して、

$$
\begin{eqnarray}
L
&\equiv& V(X^{(1)}, \cdots, X^{(n)}) - \lambda \left( \displaystyle \sum_{j=1}^m a_j^2 - 1\right) \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) \right)^2 - \lambda \left( \displaystyle \sum_{j=1}^m a_j^2 - 1\right)
\end{eqnarray}
$$

$$
\begin{cases}
\cfrac{\partial L}{\partial a_k} = 0 \\
\displaystyle \sum_{j=1}^m a_j^2 = 1
\end{cases}
$$

偏微分方程式の左辺を変形：

$$
\begin{eqnarray}
\cfrac{\partial L}{\partial a_k}
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n 2 \left(x_k^{(i)} - \overline{x}_k \right) \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) - 2 \lambda a_k \\
&=& 2 \displaystyle \sum_{j=1}^m a_j \cfrac{1}{n-1} \sum_{i=1}^n \left(x_k^{(i)} - \overline{x}_k \right) \left(x_j^{(i)} - \overline{x}_j \right) - 2 \lambda a_k \\
&=& 2 \displaystyle \sum_{j=1}^m a_j C_{jk} - 2 \lambda a_k
\end{eqnarray}
$$

最後の変形では、$$x_j, x_k$$ の **共分散** $$C_{jk}$$ の定義式（下式）を用いた。

$$
C_{jk} \equiv \cfrac{1}{n-1} \sum_{i=1}^n \left(x_k^{(i)} - \overline{x}_k \right) \left(x_j^{(i)} - \overline{x}_j \right)
$$

**共分散行列**

$$
C = \cfrac{1}{n-1} \begin{pmatrix}
\displaystyle \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_1^{(i)} - \overline{x}_1 \right) & \cdots & \displaystyle \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_m^{(i)} - \overline{x}_m \right) \\
\vdots &  & \vdots \\
\displaystyle \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_1^{(i)} - \overline{x}_1 \right) & \cdots & \displaystyle \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_m^{(i)} - \overline{x}_m \right)
\end{pmatrix}
$$

を使い、全ての $$a_k$$ に関する偏微分方程式を1つのベクトル方程式にまとめることができる。

$$
C \boldsymbol{a} = \lambda \boldsymbol{a}
$$

これは、**共分散行列 $$C$$ の固有値 $$\lambda$$、固有ベクトル $$\boldsymbol{a}$$ を求める問題に等しい**。

→ 固有値・固有ベクトルは $$m$$ 個求まる。どれを選べば良いのか？

両辺に左から $$\boldsymbol{a}^T$$ をかけて、

$$
\boldsymbol{a}^T C \boldsymbol{a} = \boldsymbol{a}^T \lambda \boldsymbol{a}
$$

右辺は、

$$
\boldsymbol{a}^T \lambda \boldsymbol{a} = \lambda \| \boldsymbol{a} \|^2 = \lambda
$$

左辺は、

$$
C \boldsymbol{a} = \cfrac{1}{n-1} \begin{pmatrix}
\displaystyle \sum_{j=1}^m a_j \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_j^{(i)} - \overline{x}_j \right) \\
\vdots \\
\displaystyle \sum_{j=1}^m a_j \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_j^{(i)} - \overline{x}_j \right)
\end{pmatrix}
$$

より、

$$
\begin{eqnarray}
\boldsymbol{a}^T C \boldsymbol{a}
&=& (a_1, \cdots, a_m) \cfrac{1}{n-1}
\begin{pmatrix}
\displaystyle \sum_{j=1}^m a_j \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_j^{(i)} - \overline{x}_j \right) \\
\vdots \\
\displaystyle \sum_{j=1}^m a_j \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_j^{(i)} - \overline{x}_j \right)
\end{pmatrix} \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{k=1}^m a_k \sum_{j=1}^m a_j \sum_{i=1}^n \left(x_k^{(i)} - \overline{x}_k \right) \left(x_j^{(i)} - \overline{x}_j \right) \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{k=1}^m a_k \left(x_k^{(i)} - \overline{x}_k \right) \right) \left( \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) \right) \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) \right)^2 \\
&=& V(X^{(1)}, \cdots, X^{(n)})
\end{eqnarray}
$$

したがって、

$$
V(X^{(1)}, \cdots, X^{(n)}) = \lambda
$$

つまり、固有値 $$\lambda$$ は最大化したい分散そのもの。

よって最も大きい $$\lambda$$ に対応する固有ベクトル $$\boldsymbol{a}$$ を選べば良い。

（TODO: 2位以下は？）


## 実装
