---
title: 主成分分析（PCA）
---

# 主成分分析（PCA）とは

Principal Component Analysis の略で、高次元データの特徴抽出（次元削減）の手法の1つ。  
うまくデータのばらつきが大きくなるように、データをより低次元の空間へ射影する。


## 次元削減の方法

$$m$$ 次元データ $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ を、可能な限り特徴量の分散が大きくなるように $$l(\le m)$$ 次元空間へ圧縮する方法は以下の通り。

### 1. 共分散行列の固有方程式を解く

$$\boldsymbol{x}$$ の特徴量同士の **共分散**

$$
C_{jk} \equiv \cfrac{1}{n-1} \sum_{i=1}^n \left(x_j^{(i)} - \overline{x}_j \right) \left(x_k^{(i)} - \overline{x}_k \right)
$$

を並べた **共分散行列**

$$
C \equiv \cfrac{1}{n-1} \begin{pmatrix}
\displaystyle \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_1^{(i)} - \overline{x}_1 \right) & \cdots & \displaystyle \sum_{i=1}^n \left(x_1^{(i)} - \overline{x}_1 \right) \left(x_m^{(i)} - \overline{x}_m \right) \\
\vdots &  & \vdots \\
\displaystyle \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_1^{(i)} - \overline{x}_1 \right) & \cdots & \displaystyle \sum_{i=1}^n \left(x_m^{(i)} - \overline{x}_m \right) \left(x_m^{(i)} - \overline{x}_m \right)
\end{pmatrix}
$$

を作り、これに対する固有方程式

$$
C \boldsymbol{a} = \lambda \boldsymbol{a}
$$

を解く（固有値 $$\lambda$$ と対応する固有ベクトル $$\boldsymbol{a}$$ を求める）。

- $$x_j^{(i)}$$: $$i$$ 番目のデータサンプルの $$j$$ 番目の特徴量
- $$\overline{x}_j$$: $$j$$ 番目の特徴量の全データサンプル平均


### 2. 固有ベクトルを選択する

固有値 $$\lambda$$ が大きい方から順に、$$l$$ 個の固有ベクトル $$\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$$ を選ぶ。  
固有ベクトル $$\boldsymbol{a}_1, \cdots, \boldsymbol{a}_l$$ をそれぞれ **第1主成分、... 第 $$l$$ 主成分** と呼ぶ。

### 3. 主成分により元データを射影する

主成分 $$\boldsymbol{a}_i$$ による元データの射影

$$
\boldsymbol{X}^{(i)} = (X_1^{(i)}, \cdots, X_l^{(i)})
$$

$$
X_j^{(i)} = \boldsymbol{x}^{(i)} \cdot \boldsymbol{a}_j
$$

を求め、新しい特徴量とする。


## 直感的なイメージ

2次元空間のデータを1次元に射影する例。

![PCA](https://user-images.githubusercontent.com/13412823/80565188-d3821a80-8a2a-11ea-84a7-1781d035c523.png)


## 導出

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

共分散行列 $$C$$ を使い、全ての $$a_k$$ に関する偏微分方程式を行列形式にまとめることができる。

$$
C \boldsymbol{a} = \lambda \boldsymbol{a}
$$

これは、**共分散行列 $$C$$ の固有値 $$\lambda$$、固有ベクトル $$\boldsymbol{a}$$ を求める固有方程式**。


### 最適解の選択

固有方程式の解（固有値・固有ベクトル）は $$m$$ 個求まるので、そのうちのどれを選べば良いのかを考える。

固有方程式に左から $$\boldsymbol{a}^T$$ をかけて、

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

全ての $$b_k$$ をまとめて行列形式で書くと、

$$
C \boldsymbol{b} = \lambda \boldsymbol{b} + \cfrac{1}{2} \mu \boldsymbol{a}
$$

両辺に左から $$\boldsymbol{a}^T$$ をかけると、

$$
\boldsymbol{a}^T C \boldsymbol{b} = \lambda \boldsymbol{a} \cdot \boldsymbol{b} + \cfrac{1}{2} \mu \| \boldsymbol{a} \|^2
$$

単位ベクトル条件、直交条件より

$$
\boldsymbol{a}^T C \boldsymbol{b} = \cfrac{1}{2} \mu
$$

ここで、共分散行列 $$C$$ は定義より明らかに対称行列（$$C_{ij} = C_{ji}, C^T = C$$）であるから、

$$
\begin{eqnarray}
\cfrac{1}{2} \mu
&=& \boldsymbol{a}^T C \boldsymbol{b} \\
&=& (\boldsymbol{a}^T C \boldsymbol{b})^T \\
&=& \boldsymbol{b}^T C^T \boldsymbol{a} \\
&=& \boldsymbol{b}^T C \boldsymbol{a} \\
&=& \boldsymbol{b}^T \lambda \boldsymbol{a} \\
&=& \lambda \boldsymbol{b} \cdot \boldsymbol{a} \\
&=& 0
\end{eqnarray}
$$

つまり $$\mu = 0$$ なので

$$
C \boldsymbol{b} = \lambda \boldsymbol{b}
$$

第1主成分のときと同じ、$$C$$ の固有方程式が得られた。  
したがって、$$\boldsymbol{b}$$ は $$C$$ の固有ベクトルのうち $$\boldsymbol{a}$$ 以外で固有値が最大となるもの（= **固有値が2番目に大きいもの**）を選べば良い。

対称行列の性質として、**対称行列の固有ベクトルは互いに直行する** ので、$$\boldsymbol{a}$$ との直交条件を確認する必要はない。


### 第3主成分以降

第2成分同様に、「上位の成分と直交する」という制約を課してラグランジュの未定定数を適用すれば、やはり $$C$$ の固有方程式が得られる。


## 注意

- PCA では分散を最大化するため、結果は特徴量のスケールに影響を受ける
  - **→ 事前に特徴量を標準化しておく**：$$x_j'^{(i)} = \cfrac{x_j^{(i)} - \overline{x}_j}{\sigma_j}$$


## 実装

### コード

{% gist 2d65ecb7fce51816fd3a8bbedcad9ebe pca.py %}

### 動作確認

{% gist 2d65ecb7fce51816fd3a8bbedcad9ebe ~fit.py %}

![transformed](https://user-images.githubusercontent.com/13412823/80590257-959aeb80-8a56-11ea-8a7d-be65038f6326.png)

![contribution](https://user-images.githubusercontent.com/13412823/80590253-93d12800-8a56-11ea-8447-0ccb1f2b3adc.png)
