---
title: ラプラシアン行列
title-en: Laplacian matrix
---
# 概要

ラプラシアン行列 = グラフ理論において、グラフを行列で表現したもの。  
グラフの色々な特性を見つけるのに役立つ。


# 定義

以後、説明のための例として、5つの頂点 $V_1, \cdots, V_5$ が6本のエッジ $e_1, \cdots, e_6$ で以下のようにつながるグラフ $G$ を考える。

```
V1 --e1--> V2 --------+
|          |          |
e2         e3         e4
|          |          |
v          v          v
V3 --e5--> V4 --e6--> V5
```


## 隣接行列

> **【定義】隣接行列**
> 
> グラフ $G$ の頂点の総数を $n$ として、以下を満たす $n\times n$ 行列 $A$ を $G$ の **隣接行列** という。
> - $i$ 番目の頂点と $j$ 番目の頂点が接続されていれば $A_{ij} = A_{ji} = 1$
> - そうでなければ $A_{ij} = A{ji} = 0$

上の例であれば、

$$
A = \begin{pmatrix}
    0 & 1 & 1 & 0 & 0 \\
    1 & 0 & 0 & 1 & 1 \\
    1 & 0 & 0 & 1 & 0 \\
    0 & 1 & 1 & 0 & 1 \\
    0 & 1 & 0 & 1 & 0 \\
\end{pmatrix}
$$


## 次数行列

> **【定義】次数行列**
> 
> グラフ $G$ の頂点の総数を $n$ として、以下を満たす $n\times n$ 行列 $D$ を $G$ の **次数行列** という。
> 
> - 対角成分：$i$ 番目の頂点に接続するエッジの数を $m_i$ とすると、$D_{ii} = m_i$
> - それ以外：$i\ne j$ なら $D_{ij} = 0$

上の例であれば、

$$
D = \begin{pmatrix}
    2 & 0 & 0 & 0 & 0 \\
    0 & 3 & 0 & 0 & 0 \\
    0 & 0 & 2 & 0 & 0 \\
    0 & 0 & 0 & 3 & 0 \\
    0 & 0 & 0 & 0 & 2 \\
\end{pmatrix}
$$


## 接続行列

> **【定義】接続行列**
> 
> 有向グラフ $G$ の頂点の総数を $n$、エッジの総数を $m$ として、以下を満たす $n\times m$ 行列 $B$ を $G$ の **接続行列** という。
> 
> $i$ 番目の頂点 $V_i$ と $j$ 番目のエッジ $e_j$ について、
> - $V_i$ と $e_j$ が接していなければ $B_{ij} = 0$
> - $V_i$ が $e_j$ の始点であれば $B_{ij} = 1$
> - $V_i$ が $e_j$ の終点であれば $B_{ij} = -1$

上の例であれば、

$$
B = \begin{pmatrix}
    1 & 1 & 0 & 0 & 0 & 0 \\
    -1 & 0 & 1 & 1 & 0 & 0 \\
    0 & -1 & 0 & 0 & 1 & 0 \\
    0 & 0 & -1 & 0 & -1 & 1 \\
    0 & 0 & 0 & -1 & 0 & -1 \\
\end{pmatrix}
$$


## ラプラシアン行列

> **【定義】ラプラシアン行列**
> 
> グラフ $G$ の隣接行列、次数行列をそれぞれ $A, D$ とするとき、ラプラシアン行列 $L$ は
> 
> $$
L := D-A
$$
> 
> $G$ が有向グラフであれば、$G$ の接続行列を $B$ として、以下のようにも書ける。
> 
> $$
L := D-A = BB^T
$$

上の例であれば、

$$
L = D - A = \begin{pmatrix}
    2 & -1 & -1 & 0 & 0 \\
    -1 & 3 & 0 & -1 & -1 \\
    -1 & 0 & 2 & -1 & 0 \\
    0 & -1 & -1 & 3 & -1 \\
    0 & -1 & 0 & -1 & 2 \\
\end{pmatrix}
$$


$BB^T$ も計算してみると、

$$
L = BB^T =
\begin{pmatrix}
    1 & 1 & 0 & 0 & 0 & 0 \\
    -1 & 0 & 1 & 1 & 0 & 0 \\
    0 & -1 & 0 & 0 & 1 & 0 \\
    0 & 0 & -1 & 0 & -1 & 1 \\
    0 & 0 & 0 & -1 & 0 & -1 \\
\end{pmatrix}
\begin{pmatrix}
    1 & -1 & 0 & 0 & 0 \\
    1 & 0 & -1 & 0 & 0 \\
    0 & 1 & 0 & -1 & 0 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 0 & 1 & -1 & 0 \\
    0 & 0 & 0 & 1 & -1 \\
\end{pmatrix}
=
\begin{pmatrix}
    2 & -1 & -1 & 0 & 0 \\
    -1 & 3 & 0 & -1 & -1 \\
    -1 & 0 & 2 & -1 & 0 \\
    0 & -1 & -1 & 3 & -1 \\
    0 & -1 & 0 & -1 & 2 \\
\end{pmatrix}
$$

> **【NOTE】有向グラフのエッジの向きはラプラシアン行列に反映されない**
> 
> 前述の通りラプラシアン行列には2つの計算方法があるが、そのうち $D-A$ はグラフの有向・無向と関係なく計算できる。したがって、ラプラシアン行列はエッジの向きに関係なく計算できる。  
> もう一つの計算方法 $BB^T$ に使われる接続行列 $B$ にはグラフの方向の情報が含まれるが、$BB^T$ を計算すると向きの情報は失われる。


## 正規化ラプラシアン行列

> **【定義】正規化ラプラシアン行列**
> 
> グラフ $G$ のラプラシアン行列 $L$ に対して、正規化ラプラシアン行列 $\tilde{L}$ を下式で定義する：
> 
> $$
\tilde{L} := D^{-1/2} L D^{-1/2}
$$
>
> $L := D - A$ であるから、$I$ を単位行列として、以下のように書くこともできる。
> 
> $$
\tilde{L} = D^{-1/2} (D-A) D^{-1/2} = I - D^{-1/2} A D^{-1/2}
$$

上の例では、

$$
D^{-1/2} = \begin{pmatrix}
    \frac{1}{\sqrt{2}} & 0 & 0 & 0 & 0 \\
    0 & \frac{1}{\sqrt{3}} & 0 & 0 & 0 \\
    0 & 0 & \frac{1}{\sqrt{2}} & 0 & 0 \\
    0 & 0 & 0 & \frac{1}{\sqrt{3}} & 0 \\
    0 & 0 & 0 & 0 & \frac{1}{\sqrt{2}} \\
\end{pmatrix}
$$

であるから、

$$
\tilde{L} = D^{-1/2} L D^{-1/2} = \begin{pmatrix}
    1 & -\frac{1}{\sqrt{6}} & -\frac{1}{2} & 0 & 0 \\
    -\frac{1}{\sqrt{6}} & 1 & 0 & -\frac{1}{3} & -\frac{1}{\sqrt{6}} \\
    -\frac{1}{2} & 0 & 1 & -\frac{1}{\sqrt{6}} & 0 \\
    0 & -\frac{1}{3} & -\frac{1}{\sqrt{6}} & 1 & -\frac{1}{\sqrt{6}} \\
    0 & -\frac{1}{\sqrt{6}} & 0 & -\frac{1}{\sqrt{6}} & 1 \\
\end{pmatrix}
$$


```python
import numpy as np

A = np.array([
    [0,1,1,0,0],
    [1,0,0,1,1],
    [1,0,0,1,0],
    [0,1,1,0,1],
    [0,1,0,1,0]
])
D = np.array([
    [2,0,0,0,0],
    [0,3,0,0,0],
    [0,0,2,0,0],
    [0,0,0,3,0],
    [0,0,0,0,2]
])

B = np.array([
    [1,1,0,0,0,0],
    [-1,0,1,1,0,0],
    [0,-1,0,0,1,0],
    [0,0,-1,0,-1,1],
    [0,0,0,-1,0,-1]
])

L = D - A
B.dot(B.T)
D_inv_root = np.diag(np.sqrt(1.0/np.diag(D)))
L_regular = D_inv_root.dot(L).dot(D_inv_root)
```