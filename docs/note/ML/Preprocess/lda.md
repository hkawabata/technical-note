---
title: 線形判別分析（LDA）
---

# フィッシャーの線形判別

高次元データの教師あり特徴抽出（次元削減）の手法の1つ。  
以下の条件がうまくバランスするようにデータを射影する。

- 別クラスのデータをできるだけ遠くへ離す
- 同じクラスのデータをできるだけ近くに固める


## 問題設定

$$n$$ 個の $$d$$ 次元データサンプル

$$
\boldsymbol{x}^{(i)} = \begin{pmatrix}
x_1^{(i)} \\
\vdots \\
x_d^{(i)}
\end{pmatrix}
$$

を $$k\ (\le d)$$ 次元空間へ射影する（$$i = 1, \cdots, n$$）。

## 次元削減の方法


### 1. クラス間・クラス内の共分散行列の計算

$$n_C$$ 個のサンプルが属するクラスラベル $$C$$ のデータサンプル平均

$$
\boldsymbol{m}_C \equiv \displaystyle \cfrac{1}{n_C} \sum_{\boldsymbol{x}^{(i)} \in C} \boldsymbol{x}^{(i)}
$$

全データサンプル平均

$$
\boldsymbol{m} \equiv \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} \boldsymbol{x}^{(i)}
$$

を用いて、以下の2つの行列を計算する。

**クラス間共分散行列**：

$$
\begin{eqnarray}
S_B
&\equiv& \displaystyle \sum_{C} n_C \left( \boldsymbol{m}_C - \boldsymbol{m} \right) \left( \boldsymbol{m}_C - \boldsymbol{m} \right)^T \\
&=& \begin{pmatrix}
\displaystyle \sum_{C} n_C \left(m_{C,1} - m_1 \right) \left(m_{C,1} - m_1 \right) & \cdots & \displaystyle \sum_{C} n_C \left(m_{C,1} - m_1 \right) \left(m_{C,d} - m_d \right) \\
\vdots &  & \vdots \\
\displaystyle \sum_{C} n_C \left(m_{C,d} - m_d \right) \left(m_{C,1} - m_1 \right) & \cdots & \displaystyle \sum_{C} n_C \left(m_{C,d} - m_d \right) \left(m_{C,d} - m_d \right)
\end{pmatrix}
\end{eqnarray}
$$

**クラス内共分散行列**：

$$
\begin{eqnarray}
S_W
&\equiv& \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right) \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right)^T \\
&=& \begin{pmatrix}
\displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( x_1^{(i)} - m_{C,1} \right) \left( x_1^{(i)} - m_{C,1} \right) & \cdots & \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( x_1^{(i)} - m_{C,1} \right) \left( x_d^{(i)} - m_{C,d} \right) \\
\vdots &  & \vdots \\
\displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( x_d^{(i)} - m_{C,d} \right) \left( x_1^{(i)} - m_{C,1} \right) & \cdots & \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( x_d^{(i)} - m_{C,d} \right) \left( x_d^{(i)} - m_{C,d} \right)
\end{pmatrix}
\end{eqnarray}
$$

### 2. 行列の固有方程式を解く

行列 $$S_W^{-1} S_B$$ の固有方程式

$$
S_W^{-1} S_B \boldsymbol{w} = \lambda \boldsymbol{w}
$$

を解き、固有値 $$\lambda$$ とそれに対応する固有ベクトル $$\boldsymbol{w}$$ を求める。

### 3. 固有ベクトルを選択する

固有値 $$\lambda$$ が大きい順に $$k$$ 個の固有ベクトル $$\boldsymbol{w}_1, \cdots, \boldsymbol{w}_k$$ を選ぶ。

### 4. 固有ベクトルにより元データを射影する

選んだ固有ベクトルによる元データの射影

$$
\begin{eqnarray}
\boldsymbol{X}^{(i)} &=& \left( X_1, \cdots, X_k \right) \\
X_j^{(i)} &=& \boldsymbol{x}^{(i)} \cdot \boldsymbol{w}_j
\end{eqnarray}
$$

を求め、新しい特徴量とする。


## 導出

データサンプル $$\boldsymbol{x}^{(i)}$$ を射影する方向ベクトルを

$$
\boldsymbol{w} = \begin{pmatrix}
w_1 \\
\vdots \\
w_d
\end{pmatrix}
$$

と置く。

### 別クラスのデータをできるだけ遠くへ離す

射影の後、クラスが異なるデータサンプルができるだけ離れるようにしたい。  
→ 各クラスのサンプル平均が、全サンプル平均から離れていれば良い

各クラスのサンプル平均と全サンプル平均との間で、射影後の差分の平方和を取って、

$$
\begin{eqnarray}
J_B(\boldsymbol{w})
&\equiv& \displaystyle \sum_{C} n_C \left( \boldsymbol{w} \cdot \boldsymbol{m}_C - \boldsymbol{w} \cdot \boldsymbol{m} \right)^2 \\
&=& \displaystyle \sum_{C} n_C \left( \boldsymbol{w} \cdot \left( \boldsymbol{m}_C - \boldsymbol{m} \right) \right)^2 \\
&=& \displaystyle \sum_{C} n_C \boldsymbol{w}^T \left( \boldsymbol{m}_C - \boldsymbol{m} \right) \left( \boldsymbol{m}_C - \boldsymbol{m} \right)^T \boldsymbol{w} \\
&=& \boldsymbol{w}^T \left( \displaystyle \sum_{C} n_C \left( \boldsymbol{m}_C - \boldsymbol{m} \right) \left( \boldsymbol{m}_C - \boldsymbol{m} \right)^T \right) \boldsymbol{w} \\
&=& \boldsymbol{w}^T S_B \boldsymbol{w}
\end{eqnarray}
$$

これが大きくなれば良い。


### 同じクラスのデータをできるだけ近くに固める

射影の後、クラスが同じデータサンプルはできるだけ近くに固まるようにしたい。  

各データサンプルと、属するクラスのサンプル平均との間で、射影後の差分の平方和を取って、

$$
\begin{eqnarray}
J_W(\boldsymbol{w})
&\equiv& \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( \boldsymbol{w} \cdot \boldsymbol{x}^{(i)} - \boldsymbol{w} \cdot \boldsymbol{m}_C \right)^2 \\
&=& \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( \boldsymbol{w} \cdot \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right) \right)^2 \\
&=& \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \boldsymbol{w}^T \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right) \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right)^T \boldsymbol{w} \\
&=& \boldsymbol{w}^T \left( \displaystyle \sum_{C} \sum_{\boldsymbol{x}^{(i)} \in C} \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right) \left( \boldsymbol{x}^{(i)} - \boldsymbol{m}_C \right)^T \right) \boldsymbol{w} \\
&=& \boldsymbol{w}^T S_W \boldsymbol{w}
\end{eqnarray}
$$

これが小さくなれば良い。

### 最大化問題へ

以上より、$$J_B(\boldsymbol{w})$$ をなるべく大きく、$$J_W(\boldsymbol{w})$$ をなるべく小さくしたいので、

$$
J(\boldsymbol{w}) \equiv \cfrac{J_B(\boldsymbol{w})}{J_W(\boldsymbol{w})} = \cfrac{\boldsymbol{w}^T S_B \boldsymbol{w}}{\boldsymbol{w}^T S_W \boldsymbol{w}}
$$

を最大化するような $$\boldsymbol{w}$$ を求めれば良い。

$$
\begin{eqnarray}
\cfrac{\partial J(\boldsymbol{w})}{\partial \boldsymbol{w}}
&=& \cfrac{1}{\left( \boldsymbol{w}^T S_W \boldsymbol{w} \right)^2}
\left(
\left( \boldsymbol{w}^T S_W \boldsymbol{w} \right) \left( S_B + S_B^T \right) \boldsymbol{w} -
\left( \boldsymbol{w}^T S_B \boldsymbol{w} \right) \left( S_W + S_W^T \right) \boldsymbol{w}
\right) \\
&=& \cfrac{2}{\left( \boldsymbol{w}^T S_W \boldsymbol{w} \right)^2}
\left(
\left( \boldsymbol{w}^T S_W \boldsymbol{w} \right) S_B \boldsymbol{w} -
\left( \boldsymbol{w}^T S_B \boldsymbol{w} \right) S_W \boldsymbol{w}
\right)
\end{eqnarray}
$$

ここで、
- $$S_B, S_W$$ が対称行列であること（$$S_B^T = S_B, S_W^T = S_W$$）
- 行列の微分の公式 $$\cfrac{\partial}{\partial \boldsymbol{x}} \left( \boldsymbol{x}^T A \boldsymbol{x} \right) = \left( A + A^T \right) \boldsymbol{x}$$

を用いた。

最適解においては

$$
\cfrac{\partial J(\boldsymbol{w})}{\partial \boldsymbol{w}} = 0
$$

であるから、

$$
\left( \boldsymbol{w}^T S_W \boldsymbol{w} \right) S_B \boldsymbol{w} =
\left( \boldsymbol{w}^T S_B \boldsymbol{w} \right) S_W \boldsymbol{w}
$$

スカラー $$\boldsymbol{w}^T S_W \boldsymbol{w}$$ で両辺を割り、左から $$S_W^{-1}$$ をかけると、

$$
S_W^{-1} S_B \boldsymbol{w} =
\cfrac{ \boldsymbol{w}^T S_B \boldsymbol{w} }{ \boldsymbol{w}^T S_W \boldsymbol{w} } \boldsymbol{w}
$$

これは、行列 $$S_W^{-1} S_B$$ の固有方程式であり、固有値 $$\cfrac{ \boldsymbol{w}^T S_B \boldsymbol{w} }{ \boldsymbol{w}^T S_W \boldsymbol{w} }$$ は最大化したい $$J(\boldsymbol{w})$$ そのもの。

$$
S_W^{-1} S_B \boldsymbol{w} =
J(\boldsymbol{w}) \boldsymbol{w}
$$


### 解の選択

固有値が $$J(\boldsymbol{w})$$ の値に一致するので、固有値が大きいものから順に $$k$$ 個の固有ベクトル $$\boldsymbol{w}_1, \cdots, \boldsymbol{w}_k$$ を選べば良い。

行列 $$S_W^{-1} S_B$$ は対称行列であるから、固有ベクトルは互いに直交する（基底にできる）。
