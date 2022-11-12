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


# 実装例

結果が期待通りにならないのでバグが有りそう。要確認

```python
import numpy as np
from matplotlib import pyplot as plt

T = 5000
w = 10
M = 500
L = 300

ts = np.arange(T) / 100
y_noise = np.random.normal(loc=0, scale=0.1, size=T)
y1 = y_noise + np.where(np.logical_and(4*np.pi < ts, ts < 9*np.pi), np.sin(ts), np.sin(3*ts))
y2 = y_noise + np.sin(ts) + np.where(np.logical_and(np.pi < ts, ts < np.pi*101/100), 5.0, 0)

#plt.plot(ts, y1)
#plt.show()
#plt.plot(ts, y2)
#plt.show()

def get_matrix(i_start, y):
    ret = []
    for i in range(i_start, i_start+M):
        ret.append(y[i:i+w])
    return np.array(ret).T

def calc_svd(matrix):
    U, s, V = np.linalg.svd(matrix)
    return U, s, V

def step(i_start, y):
    H = get_matrix(i_start, y)
    H_history = get_matrix(i_start-L, y)
    U, _, _ = calc_svd(H)
    U_history, _, _ = calc_svd(H_history)
    _, s, _ = calc_svd((U.T).dot(U_history))
    return 1 - s[0]

a_y1 = []
a_y2 = []
for i_start in range(L, T-w-M):
    if i_start % 100 == 0:
        print(i_start)
    a_y1.append(step(i_start, y1))
    a_y2.append(step(i_start, y2))

plt.plot(ts[L:T-w-M], a_y1)
plt.show()
plt.plot(ts[L:T-w-M], a_y2)
plt.show()
```