---
title: 主成分分析（PCA）
---

# 主成分分析（PCA）とは

Principal Component Analysis の略で、高次元データの特徴抽出（次元削減）の手法の1つ。  
うまくデータのばらつきが大きくなるように、データをより低次元の空間へ射影する。

## 問題設定

$$n$$ 個の $$m$$ 次元データサンプル

$$
\boldsymbol{x}^{(i)} = \begin{pmatrix}
x_1^{(i)} \\
\vdots \\
x_m^{(i)}
\end{pmatrix}
$$

を $$l\ (\le m)$$ 次元空間へ射影する（$$i = 1, \cdots, n$$）。

# 線形の主成分分析

## 次元削減の方法

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


# カーネル主成分分析

通常の主成分分析では、線形分離不可能なデータに対応できない。  
そこで、まず高次元空間に射影して線形分離可能にした上で線形の主成分分析を適用する。

## 理論

### 標準化による共分散行列の書き換え

$$m$$ 次元データサンプル

$$
\boldsymbol{x} =
\begin{pmatrix}
x_1 \\
\vdots \\
x_m
\end{pmatrix}
$$

を事前に標準化しておけば、各特徴量の平均がゼロになるので、共分散行列は、

$$
C = \cfrac{1}{n-1} \begin{pmatrix}
\displaystyle \sum_{i=1}^n x_1^{(i)} x_1^{(i)} & \cdots & \displaystyle \sum_{i=1}^n x_1^{(i)} x_m^{(i)} \\
\vdots &  & \vdots \\
\displaystyle \sum_{i=1}^n x_m^{(i)} x_1^{(i)} & \cdots & \displaystyle \sum_{i=1}^n x_m^{(i)} x_m^{(i)}
\end{pmatrix}
= \cfrac{1}{n-1} \sum_{i=1}^n \boldsymbol{x} \boldsymbol{x}^T
$$

と書ける。$$n$$ 個の全データサンプル $$\boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)}$$ を並べた $$m \times n$$ 行列

$$
D \equiv \left( \boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)} \right)
= \begin{pmatrix}
x_1^{(1)} & \cdots & x_1^{(n)} \\
\vdots &  & \vdots \\
x_m^{(1)} & \cdots & x_m^{(n)}
\end{pmatrix}
$$

を使えば、

$$
C = \cfrac{1}{n-1} DD^T
$$

となる。

### 高次元空間への射影による共分散行列の置き換え

関数 $$\boldsymbol{\phi} = (\phi_1, \cdots, \phi_M)$$ を用いて $$\boldsymbol{x}$$ を $$M\ (\gg m)$$ 次元空間に射影する：

$$
\boldsymbol{x} =
\begin{pmatrix}
x_1 \\
\vdots \\
x_m
\end{pmatrix}
\longmapsto
\boldsymbol{\phi} (\boldsymbol{x}) =
\begin{pmatrix}
\phi_1(\boldsymbol{x}) \\
\vdots \\
\phi_M(\boldsymbol{x})
\end{pmatrix}
$$

**高次元空間への射影を実際に計算して求めるのは計算コストが非常に大きい。**  
**そのため、射影後のベクトルの「内積」だけを使って以後の全ての計算を行う（カーネルトリック。詳細はサポートベクトルマシンのノートを参照）**

射影後の空間における共分散行列 $$C_{\phi}$$ は以下の式で書ける。

$$
C_{\phi} \equiv \cfrac{1}{n-1} \begin{pmatrix}
\displaystyle \sum_{i=1}^n \phi_1 \left(\boldsymbol{x}^{(i)}\right) \phi_1 \left(\boldsymbol{x}^{(i)}\right) & \cdots &
\displaystyle \sum_{i=1}^n \phi_1 \left(\boldsymbol{x}^{(i)}\right) \phi_M \left(\boldsymbol{x}^{(i)}\right) \\
\vdots &  & \vdots \\
\displaystyle \sum_{i=1}^n \phi_M \left(\boldsymbol{x}^{(i)}\right) \phi_1 \left(\boldsymbol{x}^{(i)}\right) & \cdots &
\displaystyle \sum_{i=1}^n \phi_M \left(\boldsymbol{x}^{(i)}\right) \phi_M \left(\boldsymbol{x}^{(i)}\right)
\end{pmatrix}
= \cfrac{1}{n-1} D_{\phi} D_{\phi}^T
$$

$$
D_{\phi} \equiv \begin{pmatrix}
\phi_1 \left(\boldsymbol{x}^{(1)} \right) & \cdots & \phi_1 \left(\boldsymbol{x}^{(n)} \right) \\
\vdots &  & \vdots \\
\phi_M \left(\boldsymbol{x}^{(1)} \right) & \cdots & \phi_M \left(\boldsymbol{x}^{(n)} \right)
\end{pmatrix}
$$

**但し、射影後の空間でもデータサンプルの平均がゼロになるようサンプルが標準化されている必要がある（次節）**。

### カーネル行列の定義

高次元空間における内積を定義するカーネル関数

$$
k\left(\boldsymbol{x}^{(i)}, \boldsymbol{x}^{(j)}\right)
\equiv \boldsymbol{\phi} \left(\boldsymbol{x}^{(i)}\right) \cdot \boldsymbol{\phi} \left(\boldsymbol{x}^{(j)}\right)
$$

を決め、$$n \times n$$ の **カーネル行列**

$$
\begin{eqnarray}
K &\equiv& \begin{pmatrix}
k\left(\boldsymbol{x}^{(1)}, \boldsymbol{x}^{(1)}\right)
& \cdots &
k\left(\boldsymbol{x}^{(1)}, \boldsymbol{x}^{(n)}\right)
\\
\vdots &  & \vdots \\
k\left(\boldsymbol{x}^{(n)}, \boldsymbol{x}^{(1)}\right)
& \cdots &
k\left(\boldsymbol{x}^{(n)}, \boldsymbol{x}^{(n)}\right)
\end{pmatrix} \\
&=& \begin{pmatrix}
\displaystyle \sum_{j=1}^M \phi_j \left(\boldsymbol{x}^{(1)}\right) \phi_j \left(\boldsymbol{x}^{(1)}\right)
& \cdots &
\displaystyle \sum_{j=1}^M \phi_j \left(\boldsymbol{x}^{(1)}\right) \phi_j \left(\boldsymbol{x}^{(n)}\right)
\\
\vdots &  & \vdots \\
\displaystyle \sum_{j=1}^M \phi_j \left(\boldsymbol{x}^{(n)}\right) \phi_j \left(\boldsymbol{x}^{(1)}\right)
& \cdots &
\displaystyle \sum_{j=1}^M \phi_j \left(\boldsymbol{x}^{(n)}\right) \phi_j \left(\boldsymbol{x}^{(n)}\right)
\end{pmatrix} \\
&=& D_{\phi}^T D_{\phi}
\end{eqnarray}
$$

を計算しておく。  
カーネル関数の決め方についてはサポートベクトルマシンのノートを参照。

カーネル行列は、射影後の空間でもデータサンプルの平均がゼロになるよう標準化（**中心化**）しておく：

$$
K \longleftarrow K - 1_n K - K 1_n + 1_n K 1_n
$$

$$1_n$$ はすべての要素が $$\frac{1}{n}$$ である $$n \times n$$ 行列：

$$
1_n \equiv \begin{pmatrix}
\frac{1}{n} & \cdots & \frac{1}{n} \\
\vdots &  & \vdots \\
\frac{1}{n} & \cdots & \frac{1}{n}
\end{pmatrix}
$$


> **【NOTE】カーネル行列の対称性**
>
> $$K = D_{\phi}^T D_{\phi}$$ より
>
> $$K^T = (D_{\phi}^T D_{\phi})^T = D_{\phi}^T (D_{\phi}^T)^T = D_{\phi}^T D_{\phi} = K$$
>
> なので、$$K$$ は対称行列。


### 固有方程式

$$M$$ 次元空間における共分散行列の固有方程式は、

$$
C_{\phi} \boldsymbol{a}_{\phi} = \lambda \boldsymbol{a}_{\phi}
$$

$$C_{\phi} = \cfrac{1}{n-1} D_{\phi} D_{\phi}^T$$ を代入すれば、

$$
\cfrac{1}{n-1} D_{\phi} D_{\phi}^T \boldsymbol{a}_{\phi} = \lambda \boldsymbol{a}_{\phi}
$$

を得る。

左から $$(n-1) D^T$$ をかけると、

$$
K D_{\phi}^T \boldsymbol{a}_{\phi} = (n-1) \lambda D_{\phi}^T \boldsymbol{a}_{\phi}
$$

ここで

$$
\boldsymbol{\nu} \equiv \cfrac{1}{(n-1) \lambda} D_{\phi}^T \boldsymbol{a}_{\phi}
$$

とおけば（係数 $$\cfrac{1}{(n-1) \lambda}$$ は後の計算を楽にするためにつけている）、

$$
K \boldsymbol{\nu} = (n-1) \lambda \boldsymbol{\nu}
$$

これは $$K$$ の固有方程式（固有値 $$(n-1) \lambda$$, 固有ベクトル $$\boldsymbol{\nu}$$）。

> **【NOTE】**
>
> **内積の行列である $$K = D_{\phi}^T D_{\phi}$$ は計算してあるが $$D_{\phi}$$ の要素の値は計算しないので、$$\boldsymbol{\nu} = D_{\phi}^T \boldsymbol{a}_{\phi}$$ から $$\boldsymbol{a}_{\phi}$$ を求めることはできない。**


### 最適解の選択

$$K$$ の固有方程式を解き、$$n$$ 個数の固有値・固有ベクトルを求める。

線形 PCA の節で見た通り、共分散行列の固有値 $$\lambda$$ は主成分空間における分散に一致する。  
$$n-1$$ は定数なので、$$K$$ の固有値 $$(n-1) \lambda$$ が大きいほど分散 $$\lambda$$ も大きい。  
よって線形 PCA と同様に、特徴抽出後の分散を大きくするには固有値が大きいものから順に固有ベクトルを $$l$$ 個選べば良い。


### データサンプルの射影

選択した $$K$$ の固有ベクトル $$\boldsymbol{\nu}_j =　\cfrac{1}{(n-1) \lambda_j} D_{\phi}^T \boldsymbol{a}_{\phi, j}\ (j = 1, \cdots, l)$$ に対応する $$\boldsymbol{a}_{\phi, j}$$ により、未知のデータサンプル $$\boldsymbol{x}$$ を新しい特徴量 $$X_j$$ に射影する：

$$
X_j = \boldsymbol{\phi} \left( \boldsymbol{x} \right) \cdot \boldsymbol{a}_{\phi, j}
$$

ここで

$$
\boldsymbol{\nu}_j = \cfrac{1}{(n-1) \lambda_j} D_{\phi}^T \boldsymbol{a}_{\phi, j}
$$

に左から $$D_{\phi}$$ をかけると、$$C_{\phi} = \cfrac{1}{n-1} D_{\phi} D_{\phi}^T$$ より

$$
D_{\phi} \boldsymbol{\nu}_j = \cfrac{1}{\lambda_j} C_{\phi} \boldsymbol{a}_{\phi, j}
$$

$$\boldsymbol{a}_{\phi, j}$$ は $$C_{\phi}$$ の固有ベクトル（$$C_{\phi} \boldsymbol{a}_{\phi, j} = \lambda_j \boldsymbol{a}_{\phi, j}$$）であるから、

$$
D_{\phi} \boldsymbol{\nu}_j = \boldsymbol{a}_{\phi, j}
$$

よって

$$
\begin{eqnarray}
X_j
&=& \boldsymbol{\phi} \left( \boldsymbol{x} \right) \cdot \boldsymbol{a}_{\phi, j} \\
&=& \boldsymbol{\phi} \left( \boldsymbol{x} \right)^T D_{\phi} \boldsymbol{\nu}_j \\
&=& \left( \phi_1\left(\boldsymbol{x}\right), \cdots, \phi_M\left(\boldsymbol{x}\right)\right)
\begin{pmatrix}
\phi_1 \left(\boldsymbol{x}^{(1)} \right) & \cdots & \phi_1 \left(\boldsymbol{x}^{(n)} \right) \\
\vdots &  & \vdots \\
\phi_M \left(\boldsymbol{x}^{(1)} \right) & \cdots & \phi_M \left(\boldsymbol{x}^{(n)} \right)
\end{pmatrix}
\begin{pmatrix}
\nu_{j, 1} \\
\vdots \\
\nu_{j, n}
\end{pmatrix}
\\
&=& \left( \boldsymbol{\phi}\left(\boldsymbol{x}\right) \cdot \boldsymbol{\phi}\left(\boldsymbol{x}^{(1)}\right), \cdots, \boldsymbol{\phi}\left(\boldsymbol{x}\right) \cdot \boldsymbol{\phi}\left(\boldsymbol{x}^{(n)}\right) \right)
\begin{pmatrix}
\nu_{j, 1} \\
\vdots \\
\nu_{j, n}
\end{pmatrix}
\\
&=& \left( k\left(\boldsymbol{x}, \boldsymbol{x}^{(1)}\right), \cdots, k\left(\boldsymbol{x}, \boldsymbol{x}^{(n)}\right) \right)
\begin{pmatrix}
\nu_{j, 1} \\
\vdots \\
\nu_{j, n}
\end{pmatrix}
\\
&=& \displaystyle \sum_{i=1}^n k\left(\boldsymbol{x}, \boldsymbol{x}^{(i)}\right) \nu_{j, i}
\end{eqnarray}
$$

カーネル関数 $$k$$ は計算可能であり、$$\nu_{j, i}$$ も計算済みであるから、この式により次元削減後の特徴量 $$X_j$$ を求めることができる。


## 実装

### コード


### 動作確認
