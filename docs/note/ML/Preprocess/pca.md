---
title: 主成分分析（PCA）
---

# 主成分分析（PCA）とは

Principal Component Analysis の略で、高次元データの特徴抽出（次元削減）の手法の1つ。  
うまくデータのばらつきが大きくなるように、データをより低次元の空間へ射影する。

## 直感的な理解

（TODO）

## 理論

### 第1主成分を求めるための最大化問題

第1主成分を表す方向ベクトルを

$$
\boldsymbol{a} =
\begin{pmatrix}
a_1 \\
\vdots \\
a_m
\end{pmatrix}
$$

と置く。  
$$\boldsymbol{a}$$ は、データサンプル $$\boldsymbol{x}$$ をその上に射影したとき、分散が最も大きくなるようなベクトル。

定数倍の自由度を消すため、単位ベクトル条件を課しておく：

$$
\| \boldsymbol{a} \|^2 = \displaystyle \sum_{j=1}^m a_j^2 = 1
$$

データサンプルを $$\boldsymbol{a}$$ 上へ射影する。  
サンプルと方向ベクトルとの内積を取れば良いから、射影後の値 $$X$$ は

$$
X^{(i)} = \boldsymbol{a} \cdot \boldsymbol{x}^{(i)} = \displaystyle \sum_{j=1}^m a_j x_j^{(i)}
$$

$$X$$ の標本分散は

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

を使い、全ての $$a_k$$ に関する偏微分方程式を行列形式にまとめることができる。

$$
C \boldsymbol{a} = \lambda \boldsymbol{a}
$$

これは、**共分散行列 $$C$$ の固有値 $$\lambda$$、固有ベクトル $$\boldsymbol{a}$$ を求める問題に等しい**。


### 最適解の選択

固有値問題の解（固有値・固有ベクトル）は $$m$$ 個求まるので、そのうちのどれを選べば良いのかを考える。

固有値問題の式に左から $$\boldsymbol{a}^T$$ をかけて、

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


### 第2主成分を求めるための最大化問題

**主成分はベクトル空間の基底であるから、互いに直行している必要がある**。

第2主成分

$$
\boldsymbol{b} =
\begin{pmatrix}
b_1 \\
\vdots \\
b_m
\end{pmatrix}
$$

は、第1主成分 $$\boldsymbol{a}$$ と直交する中で最も分散が大きくなる方向ベクトル。

単位ベクトル条件：

$$
\| \boldsymbol{b} \|^2 = \displaystyle \sum_{j=1}^m b_j^2 = 1
$$

$$\boldsymbol{a}$$ との直交条件：

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \sum_{j=1}^m a_j b_j = 1
$$

データサンプル $$\boldsymbol{x}$$ を射影：

$$
X^{(i)} = \boldsymbol{b} \cdot \boldsymbol{x}^{(i)} = \displaystyle \sum_{j=1}^m b_j x_j^{(i)}
$$

射影後の値の標本分散：

$$
\begin{eqnarray}
V(X^{(1)}, \cdots, X^{(n)})
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( X^{(i)} - \overline{X} \right)^2 \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{j=1}^m b_j \left(x_j^{(i)} - \overline{x}_j \right) \right)^2
\end{eqnarray}
$$

これを単位ベクトル条件、$$\boldsymbol{a}$$ との直交条件の下で最大化する。

ラグランジュの未定乗数法

$$
\begin{eqnarray}
L
&\equiv& V(X^{(1)}, \cdots, X^{(n)}) - \lambda \left( \displaystyle \sum_{j=1}^m b_j^2 - 1\right)
- \mu \displaystyle \sum_{j=1}^m a_j b_j \\
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n \left( \sum_{j=1}^m b_j \left(x_j^{(i)} - \overline{x}_j \right) \right)^2 - \lambda \left( \displaystyle \sum_{j=1}^m b_j^2 - 1\right)
- \mu \displaystyle \sum_{j=1}^m a_j b_j
\end{eqnarray}
$$

$$
\begin{cases}
\cfrac{\partial L}{\partial b_k} = 0 \\
\displaystyle \sum_{j=1}^m b_j^2 = 1 \\
\displaystyle \sum_{j=1}^m a_j b_j = 0
\end{cases}
$$

$$
\begin{eqnarray}
\cfrac{\partial L}{\partial b_k}
&=& \cfrac{1}{n-1} \displaystyle \sum_{i=1}^n 2 \left(x_k^{(i)} - \overline{x}_k \right) \sum_{j=1}^m a_j \left(x_j^{(i)} - \overline{x}_j \right) - 2 \lambda b_k - \mu a_k \\
&=& 2 \displaystyle \sum_{j=1}^m b_j \cfrac{1}{n-1} \sum_{i=1}^n \left(x_k^{(i)} - \overline{x}_k \right) \left(x_j^{(i)} - \overline{x}_j \right) - 2 \lambda b_k - \mu a_k \\
&=& 2 \displaystyle \sum_{j=1}^m b_j C_{jk} - 2 \lambda b_k - \mu a_k
\end{eqnarray}
$$

全ての $$b_k$$ をまとめて表記すると、

$$
C \boldsymbol{b} = \lambda \boldsymbol{b} + \cfrac{1}{2} \mu \boldsymbol{a}
$$


## 注意

- PCA では分散を最大化するため、結果は変数のスケールに影響を受ける
  - **→ 事前に変数を標準化しておく**


## 実装
