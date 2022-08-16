---
title: 特異スペクトル変換
---

# 特異スペクトル変換 (SST) とは
= Singular Spectrum Transformation

行列の特異値分解を利用した、時系列データの異常検知の手法。

# 手順

時系列データ

$$
\boldsymbol{x} = \left( x_1, x_2, \cdots, x_T \right)
$$

に対して、注目する時刻 $t$ から、ウインドウ幅 $w$ 個の要素を取り出し、$\boldsymbol{y_t}$ とする：

$$
\left( x_1, \cdots, \underbrace{x_t, x_{t+1}, x_{t+2}, \cdots, x_{t+(w-1)}}_{\boldsymbol{y_t}}, x_{t+(w-1)+1}, x_{t+(w-1)+2}, \cdots, x_T \right)
$$

ウインドウを1ずつずらし、同様の操作をして $\boldsymbol{y_{t+1}}, \cdots, \boldsymbol{y_{t+M-1}}$ を抽出する：

$$
\begin{eqnarray}
  &\left( x_1, \cdots, x_t, \underbrace{x_{t+1}, x_{t+2}, \cdots, x_{t+(w-1)}, x_{t+(w-1)+1}}_{\boldsymbol{y}_{t+1}}, x_{t+(w-1)+2}, \cdots, x_T \right)
\\
&\left( x_1, \cdots, x_t, x_{t+1}, \underbrace{x_{t+2}, \cdots, x_{t+(w-1)}, x_{t+(w-1)+1}, x_{t+(w-1)+2}}_{\boldsymbol{y}_{t+2}}, \cdots, x_T \right)
\\
&\vdots
\\
  &\left( x_1, \cdots, x_{t+(M-1)-2}, x_{t+(M-1)-1}, \underbrace{x_{t+(M-1)}, \cdots, x_{t+(w-1)+(M-1)}}_{\boldsymbol{y}_{t+(M-1)}}, \cdots, x_T \right)
\end{eqnarray}
$$

これら $\boldsymbol{y}_t , \cdots, \boldsymbol{y}_{t+(M-1)}$ を転置した列ベクトルを並べた行列

$$
H_T
\equiv
\left(\boldsymbol{y}_t^T , \cdots, \boldsymbol{y}_{t+(M-1)}^T \right)
=
\begin{pmatrix}
x_t         & x_{t+1}       & \cdots & x_{t+(M-1)}    \\
x_{t+1}     & x_{t+2}       &        & x_{t+(M-1)+1} \\
\vdots      &               & \ddots & \vdots \\
x_{t+(w-1)} & x_{t+(w-1)+1} & \cdots & x_{t+(w-1)+(M-1)}
\end{pmatrix}
$$

を定義する。
