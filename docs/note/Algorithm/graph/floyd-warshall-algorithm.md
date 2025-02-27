---
title: ワーシャルフロイド法
title-en: Floyd–Warshall Algorithm
---
# 問題設定

重み付きグラフにおいて、所属ノードの全ペアの最短距離（最小コスト）を求めたい。  
ただし、負閉路（= 1周するとコストの総和がマイナスになる経路）は存在しないものとする（そこを回り続けることでいくらでもコストを下げられるため）。

# アルゴリズム

グラフは隣接行列 $G$ の形で表現し、$G_{ij}$ はノード $n_i$ からノード $n_j$ までの最短距離を表す。

## 【0】隣接行列の初期化

与えられたグラフの隣接行列を初期化する：
- 自分自身への最短距離はゼロで初期化：
    - $G_{ii} = 0$
- ノード $n_i \to n_j\ (i \ne j)$ の重み $w$ のエッジがある場合は $w$ で初期化：
    - $G_{ij} = w$
    - グラフが無向グラフの場合、逆方向のエッジも同じ重みなので $G_{ji}=w$
- ノード $n_i \to n_j\ (i \ne j)$ のエッジが存在しない場合は無限大で初期化：
    - $G_{ij} = \infty$

## 【1】ある経由点だけを通って良い場合の最短距離の計算

あるノード $n_\mathrm{via}$ を経由して $n_\mathrm{from}$ から $n_\mathrm{to}$ へ移動する経路（他のノードは通らない）を考える。  
経由ノード $n_\mathrm{via}$ をある1つのノードに固定し、全ての $(n_\mathrm{from}, n_\mathrm{to})$ の組み合わせについて以下のルールで $G_\mathrm{from,to}$ の値をを更新していく。

$$
G_\mathrm{from,to} \gets \min \left( G_\mathrm{from,to},\ \ G_\mathrm{from,via}+G_\mathrm{via,to} \right)
$$

これが終わると、全ての $G_\mathrm{from,to}$ について、**「途中で経由ノード $n_\mathrm{via}$ だけを通って良い（通らなくても良い）場合の最短距離」の値が入った状態** になる。

$n_\mathrm{from}$ と $n_\mathrm{to}$ の間に仮想的なエッジが張られ、その重みが $n_\mathrm{via}$ だけを経由して良い場合の最短距離になっているイメージ。  
この仮想的なエッジのおかげで、以後のステップでは $n_\mathrm{via}$ を経由するかどうかは考えなくて良くなる。

## 【2】全ての点を順番に経由点として固定して1を繰り返し

全てのノードを順番に $n_\mathrm{via}$ として固定し、1の操作を繰り返す。  
全てのループが完了した時点で、$G_{ij}$ はノード $n_i, n_j$ 間の最短距離の値となる。


# 実装・動作確認

## 実装

{% gist 74bbaf40b7faac66127c0fd04125293e 20250217_floyd_warshall.py %}


## 動作確認

正の重みだけを持つケース：

![Digraph gv](https://gist.github.com/user-attachments/assets/ff382ba9-2215-498b-b81f-8b9668b03869)

```python
graph = {
    # from, to, weight
    ('A', 'B'): 7,
    ('A', 'C'): 4,
    ('A', 'D'): 2,
    ('B', 'C'): 2,
    ('C', 'D'): 3,
    ('B', 'E'): 6,
    ('C', 'F'): 2,
    ('D', 'F'): 6,
    ('E', 'F'): 4
}
show_graph(graph, is_directed=True)
```

```python
>>> floyd_warshall(graph, is_directed=True)
To      A    B    C    D     E    F
From                               
A     0.0  7.0  4.0  2.0  13.0  6.0
B     inf  0.0  2.0  5.0   6.0  4.0
C     inf  inf  0.0  3.0   inf  2.0
D     inf  inf  inf  0.0   inf  6.0
E     inf  inf  inf  inf   0.0  4.0
F     inf  inf  inf  inf   inf  0.0

>>> floyd_warshall(graph, is_directed=False)   # 無向グラフとして計算
To       A    B    C    D     E    F
From                                
A      0.0  6.0  4.0  2.0  10.0  6.0
B      6.0  0.0  2.0  5.0   6.0  4.0
C      4.0  2.0  0.0  3.0   6.0  2.0
D      2.0  5.0  3.0  0.0   9.0  5.0
E     10.0  6.0  6.0  9.0   0.0  4.0
F      6.0  4.0  2.0  5.0   4.0  0.0
```


重みに負の値を含むケース（負閉路なし）：

![Digraph gv](https://gist.github.com/user-attachments/assets/08c29b98-795d-406f-95d8-f02bbaceb004)

```python
graph = {
    # (from, to): weight
    ('A', 'B'): 7,
    ('A', 'C'): 4,
    ('A', 'D'): 2,
    ('B', 'C'): 2,
    ('C', 'D'): -3,
    ('B', 'E'): -6,
    ('D', 'F'): 6,
    ('E', 'F'): 4,
    ('F', 'C'): 2
}
show_graph(graph, is_directed=True)
```

```python
>>> floyd_warshall(graph, is_directed=True)
To      A    B    C    D    E    F
From                              
A     0.0  7.0  4.0  1.0  1.0  5.0
B     inf  0.0  0.0 -3.0 -6.0 -2.0
C     inf  inf  0.0 -3.0  inf  3.0
D     inf  inf  8.0  0.0  inf  6.0
E     inf  inf  6.0  3.0  0.0  4.0
F     inf  inf  2.0 -1.0  inf  0.0

>>> floyd_warshall(graph, is_directed=False)
無向グラフに負のエッジがあるため、最小コストを計算できません.
```