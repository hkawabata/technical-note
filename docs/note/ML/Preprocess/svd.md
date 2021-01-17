---
title: 特異値分解（SVD）
---

# 特異値分解（SVD）とは

Singular Value Decomposition の略で、高次元データの特徴抽出（次元削減）の手法の1つ。

## 問題設定

$$m$$ 個の $$n$$ 次元データサンプル

$$
\boldsymbol{x}^{(i)} = \begin{pmatrix}
x_1^{(i)} \\
\vdots \\
x_n^{(i)}
\end{pmatrix}
$$

を $$l\ (\le m)$$ 次元空間へ射影する（$$i = 1, \cdots, m$$）。

## 次元削減の方法

## 理論

### 1. 前提：特異値分解定理

$$m \times n$$ 行列

$$
A = \begin{pmatrix}
    a_{11} & \cdots & a_{1n}\\
    \vdots &  & \vdots \\
    a_{m1} & \cdots & a_{mn}\\
\end{pmatrix}
$$

に対して、$$m, n$$ 次の直行行列

$$
\begin{eqnarray}
    U = \begin{pmatrix}
        u_{11} & \cdots & u_{1m}\\
        \vdots &  & \vdots \\
        u_{m1} & \cdots & u_{mm}\\
    \end{pmatrix}
    = \left( \boldsymbol{u}_1, \cdots, \boldsymbol{u}_m \right)
    \\
    V = \begin{pmatrix}
        v_{11} & \cdots & v_{1n}\\
        \vdots & & \vdots \\
        v_{n1} & \cdots & v_{nn}\\
    \end{pmatrix}
    = \left( \boldsymbol{v}_1, \cdots, \boldsymbol{v}_m \right)
\end{eqnarray}
$$

と $$m \times n$$ 行列

$$
S = \begin{cases}
    \begin{pmatrix}
        s_1 &  & 0 \\
        & \ddots & \\
        0 &  & s_n \\
        0 & \cdots & 0 \\
        \vdots & & \vdots \\
        0 & \cdots & 0
    \end{pmatrix}
    & {\rm if} \quad m \gt n
    \\
    \begin{pmatrix}
        s_1 &  & 0 \\
        & \ddots & \\
        0 &  & s_n
    \end{pmatrix}
    & {\rm if} \quad m = n
    \\
    \begin{pmatrix}
        s_1 &  & 0 & 0 & \cdots & 0 \\
        & \ddots & & \vdots & & \vdots \\
        0 &  & s_m & 0 & \cdots & 0
    \end{pmatrix}
    & {\rm if} \quad m \lt n
\end{cases}
$$

$$
s_1 \ge s_2 \ge \cdots \ge s_{m, n}
$$

が存在し、

$$
A = USV^T
$$

### 2. 特異値分解の実行

次元削減対象の $$n$$ 次元の行ベクトル $$m$$ 個を縦に並べた行列を前節の $$A$$ に当てはめる。

（以下、ToDo）

### 3. 次元の削減

$$
s_1 \ge s_2 \ge \cdots \ge s_{m, n}
$$

なので、$$U$$ の左側の列ほど $$A$$ を構成する重要な成分。

$$t$$ 次元まで削減したい場合、
- $$U'$$: $$U$$ の $$t$$ 列目までの要素を抜き出した $$m \times t$$ 行列
- $$S'$$: $$S$$ の $$t$$ 行目、$$t$$ 列目までの要素を抜き出した $$t \times t$$ 行列
- $$V'$$: $$V$$ の $$t$$ 列目までの要素を抜き出した $$n \times t$$ 行列

を用いて計算した

$$
A' \equiv U' S' V'^T
$$

を $$A$$ の近似とできる。

![SVD](https://user-images.githubusercontent.com/13412823/104837549-ab0fb880-58f8-11eb-91dd-c66ac392f2fe.png)

次元削減の解としては、$$U'$$ を用いれば良い。


## 実装

### コード

（ToDo）

### 動作確認

（ToDo）
