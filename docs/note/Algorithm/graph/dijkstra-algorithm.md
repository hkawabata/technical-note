---
title-en: Dijkstra's algorithm
title: ダイクストラ法
---

# 問題定義

エッジが重みを持つグラフ構造において、ある頂点から別の頂点への最短経路を求めたい。  
ただし、**各エッジの重みは0以上（通ることでコストが下がる経路は存在しない）** とする。

※ 負の重みを持つ場合、グラフが有向グラフであれば[ベルマンフォード法](bellman–ford-algorithm.md)を適用できる。

# アルゴリズム

具体例をもとに手順を解説する。  
以下のグラフにおいて A から各ノードへの最短経路を求める。

![図0](https://user-images.githubusercontent.com/13412823/272174880-eb429286-adb3-4f76-a2bb-fd2b22aeb755.png)


## 【0】変数の初期化

以下の変数を準備して初期化。

| 変数                | 内容                                     | 初期値      |
| :---------------- | :------------------------------------- | :------- |
| `shortest_weight` | 「**現時点で判明している**」A から各ノードまでの最短距離を保持する辞書 | $\infty$ |
| `shortest_path`   | 「**現時点で判明している**」A から各ノードまでの最短パスを保持する辞書 | null     |
| `n_last_fix`      | 最新ステップで最短経路が確定したノード                    | null     |

![図1](https://user-images.githubusercontent.com/13412823/272174914-39e9ea0c-210e-4af8-a03f-abd0e6f398fd.png)

```python
shortest_weight = {
    'A': float('inf'),
    'B': float('inf'),
    ...,
    'F': float('inf')
}

shortest_path = {
    'A': None,
    'B': None,
    ...,
    'F': None
}

n_last_fix = None
```


## 【1】スタート地点自身までの最短経路を確定

スタート地点 A 自身までの最短距離が0であるのは明らかなので、A までの最短距離と経路を確定させる：
- `shortest_weight['A'] = 0` (Fix)
- `shortest_path['A'] = ['A']` (Fix)
- `n_last_fix = 'A'`

![図2](https://user-images.githubusercontent.com/13412823/272174910-adce19bc-da76-49f2-8931-d1d54c8ae4e2.png)

```python
shortest_weight = {
    'A': 0,             # fixed
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf')
}

shortest_path = {
    'A': ['A'],         # fixed
    'B': None,
    'C': None,
    'D': None,
    'E': None,
    'F': None
}

n_last_fix = 'A'  # updated
```

## 【2】最後に確定したノードの隣接ノードの情報を更新

最短経路が未確定のノードのうち、`n_last_fix` の隣接ノード `n_next` それぞれについて、以下のルールで `shortest_weight`, `shortest_path` を更新する
- $d_\mathrm{old}$：現時点でわかっているスタートからそのノードまでの最短距離 `shortest_weight[n_next]`
- $d_\mathrm{new}$：以下の2つの和
    - 確定済みの `n_last_fix` までの最短距離`shortest_weight[n_last_fix]`
    - `n_last_fix` から `n_next` までの距離
- $d_\mathrm{new} \lt d_\mathrm{old}$ なら最短距離・最短経路を更新：
    - `shortest_weight[n_next] = d_new` 
    - `shortest_path[n_next] = shortest_path[n_last_fix] + n_next` 

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 7,             # updated
    'C': 4,             # updated
    'D': 2,             # updated
    'E': float('inf'),
    'F': float('inf')
}

shortest_path = {
    'A': ['A'],         # (fixed)
    'B': ['A', 'B'],    # updated
    'C': ['A', 'C'],    # updated
    'D': ['A', 'D'],    # updated
    'E': None,
    'F': None
}

n_last_fix = 'A'
```

### 【3】未確定のうち距離が一番小さいノードの距離・経路を確定

最短経路が未確定のノードを全て見て、**現時点の距離が一番小さいノードの距離と経路を fix**（**他のルート経由では、絶対にこれより長くなる**）

今回の例だと `shortest_weight['D']` の2が最小なので D を fix。  
よって `n_last_fix = 'D'`

![図3](https://user-images.githubusercontent.com/13412823/272174907-ee9fdd2d-96b0-4a88-9b60-219114ce9c71.png)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 7,
    'C': 4,
    'D': 2,             # (fixed)
    'E': float('inf'),
    'F': float('inf')
}

shortest_path = {
    'A': ['A'],         # (fixed)
    'B': ['A', 'B'],
    'C': ['A', 'C'],
    'D': ['A', 'D'],    # (fixed)
    'E': None,
    'F': None
}

n_last_fix = 'D'  # updated
```

### 【4】2,3を繰り返し

`n_last_fix` が更新されなくなるまで2,3を繰り返す。

![図4](https://user-images.githubusercontent.com/13412823/272174904-408c4283-7fb5-4dfa-a5a5-4a05b5c22c3a.png)

```python
shortest_weight = {
    'A': 0,              # (fixed)
    'B': 7,
    'C': 4,              # [1]not updated --> [2]fixed
    'D': 2,              # (fixed)
    'E': float('inf'),
    'F': 8               # [1]updated
}

shortest_path = {
    'A': ['A'],          # (fixed)
    'B': ['A', 'B'],
    'C': ['A', 'C'],     # [1]not updated --> [2]fixed
    'D': ['A', 'D'],     # (fixed)
    'E': None,
    'F': ['A', 'D', 'F'] # [1]updated
}
n_last_fix = 'C'  # updated
```


![図5](https://user-images.githubusercontent.com/13412823/272174900-643091be-6db5-46cd-b75b-aef2fefa298e.png)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 6,             # [1]updated --> [2]fixed
    'C': 4,             # (fixed)
    'D': 2,             # (fixed)
    'E': float('inf'),
    'F': 6              # updated
}

shortest_path = {
    'A': ['A'],           # (fixed)
    'B': ['A', 'C', 'B'], # [1]updated --> [2]fixed
    'C': ['A', 'C'],      # (fixed)
    'D': ['A', 'D'],      # (fixed)
    'E': None,
    'F': ['A', 'C', 'F']  # [1]updated
}

# B, F は最短距離が同じなので、どちらを先に fix しても良い. ここでは B を選択
n_last_fix = 'B'  # updated
```

![図6](https://user-images.githubusercontent.com/13412823/272174898-0bcb14ed-5dd3-4394-96fd-92289af5b494.png)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 6,             # (fixed)
    'C': 4,             # (fixed)
    'D': 2,             # (fixed)
    'E': 12,            # [1]updated
    'F': 6              # [1]not updated --> [2]fixed
}

shortest_path = {
    'A': ['A'],                # (fixed)
    'B': ['A', 'C', 'B'],      # (fixed)
    'C': ['A', 'C'],           # (fixed)
    'D': ['A', 'D'],           # (fixed)
    'E': ['A', 'C', 'B', 'E'], # [1]updated
    'F': ['A', 'C', 'F']       # [1]not updated --> [2]fixed
}

n_last_fix = 'F'  # updated
```

![図7](https://user-images.githubusercontent.com/13412823/272174891-ae2dcb6c-9fa3-4f7c-9ec8-4e965dc86273.png)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 6,             # (fixed)
    'C': 4,             # (fixed)
    'D': 2,             # (fixed)
    'E': 10,            # [1]updated --> [2]fixed
    'F': 6              # (fixed)
}

shortest_path = {
    'A': ['A'],                # (fixed)
    'B': ['A', 'C', 'B'],      # (fixed)
    'C': ['A', 'C'],           # (fixed)
    'D': ['A', 'D'],           # (fixed)
    'E': ['A', 'C', 'F', 'E'], # [1]updated --> [2]fixed
    'F': ['A', 'C', 'F']       # (fixed)
}

n_last_fix = 'E'  # updated
```

→ 全てのノードが fix され、これ以降は繰り返しても `n_last_fix` は更新されない。  
→ このときの`shortest_path`と`shortest_weight`が、求める最短経路とその重み。

![図8](https://user-images.githubusercontent.com/13412823/272174887-d189076c-bc26-45e4-b1c2-6ea9fab3e8a8.png)


# 実装・動作確認

## 実装

{% gist 0ad400c415ed0b29812559d24f5e5082 20231004_dijkstra.py %}

## 動作確認

前述の「処理の流れ」で扱ったグラフのとき：

![Graph gv](https://user-images.githubusercontent.com/13412823/271911536-88878413-8d86-42af-bdd3-e86fb33ceb8e.png)

```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to B: weight=6, path=['A', 'C', 'B']
from A to C: weight=4, path=['A', 'C']
from A to D: weight=2, path=['A', 'D']
from A to E: weight=10, path=['A', 'C', 'F', 'E']
from A to F: weight=6, path=['A', 'C', 'F']

>>> dijkstra(graph, 'C')
from C to A: weight=4, path=['C', 'A']
from C to B: weight=2, path=['C', 'B']
from C to C: weight=0, path=['C']
from C to D: weight=3, path=['C', 'D']
from C to E: weight=6, path=['C', 'F', 'E']
from C to F: weight=2, path=['C', 'F']
```

ツリー状である時

<img width="400" alt="Graph02" src="https://user-images.githubusercontent.com/13412823/271907032-d193e110-022e-4d2a-9f8b-846418f4904d.png">

```python
graph = {
    # from, to, weight
    ('A', 'B', 5),
    ('A', 'C', 4),
    ('A', 'D', 2),
    ('B', 'E', 6),
    ('B', 'F', 7),
    ('C', 'G', 3),
    ('C', 'H', 2)
}
show_graph(graph)
```

```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to B: weight=5, path=['A', 'B']
from A to C: weight=4, path=['A', 'C']
from A to D: weight=2, path=['A', 'D']
from A to E: weight=11, path=['A', 'B', 'E']
from A to F: weight=12, path=['A', 'B', 'F']
from A to G: weight=7, path=['A', 'C', 'G']
from A to H: weight=6, path=['A', 'C', 'H']

>>> dijkstra(graph, 'E')
from E to A: weight=11, path=['E', 'B', 'A']
from E to B: weight=6, path=['E', 'B']
from E to C: weight=15, path=['E', 'B', 'A', 'C']
from E to D: weight=13, path=['E', 'B', 'A', 'D']
from E to E: weight=0, path=['E']
from E to F: weight=13, path=['E', 'B', 'F']
from E to G: weight=18, path=['E', 'B', 'A', 'C', 'G']
from E to H: weight=17, path=['E', 'B', 'A', 'C', 'H']
```

グラフが分断されている時

<img width="500" alt="Graph03" src="https://user-images.githubusercontent.com/13412823/271907037-e169680f-6767-4df7-8102-4601f64e9f8c.png">

```python
graph = {
    # from, to, weight
    ('A', 'B', 5),
    ('A', 'C', 2),
    ('A', 'D', 7),
    ('B', 'C', 2),
    ('C', 'D', 1),
    ('E', 'F', 4),
    ('F', 'G', 1)
}
show_graph(graph)
```

```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to B: weight=4, path=['A', 'C', 'B']
from A to C: weight=2, path=['A', 'C']
from A to D: weight=3, path=['A', 'C', 'D']
from A to E: weight=inf, path=None
from A to F: weight=inf, path=None
from A to G: weight=inf, path=None

>>> dijkstra(graph, 'E')
from E to A: weight=inf, path=None
from E to B: weight=inf, path=None
from E to C: weight=inf, path=None
from E to D: weight=inf, path=None
from E to E: weight=0, path=['E']
from E to F: weight=4, path=['E', 'F']
from E to G: weight=5, path=['E', 'F', 'G']
```


# 計算量

- 1回のループで最短経路が1つ確定するので、ノード数を $V$ とすると、このループを $V$ 回繰り返す必要があるため、その計算量は $O(V)$
- また、1つの最短経路が確定すると、そのノードから接続された隣接ノードまでの距離を更新する必要があり、隣接ノードは最大で $V-1$ 個あるため、この計算量も $O(V)$

以上により、ダイクストラ法の計算量は $O(V^2)$ となる。

※ 優先度付きキューを利用する改良版だと、$O((E+V) \log V)$（$E$ はエッジ数）に削減できるらしい（要調査）

```python
import itertools
import datetime
import random
import numpy as np
from matplotlib import pyplot as plt

def gen_graph(n_node, n_edge):
    nodes = np.arange(n_node)
    pairs = np.array(list(itertools.combinations(nodes, 2)))
    idx = np.random.choice(range(len(pairs)), n_edge, replace=False)
    graph = set()
    for f, t in pairs[idx]:
        graph.add((f, t, np.random.rand()))
    return graph

def simulate_various_n_edge(T=10):
    plt.figure(figsize=(9, 8))
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    ns_node = [100, 400, 1000]
    for i in range(len(ns_node)):
        n_node = ns_node[i]
        ns_edge = [int(n) for n in np.linspace(n_node, n_node*(n_node-1)/4, 10)]
        dt_mean, dt_std = [], []
        for n_edge in ns_edge:
            buff = []
            for _ in range(T):
                graph = gen_graph(n_node, n_edge)
                n_start = random.choice([f for f, _, _ in graph])
                start = datetime.datetime.now()
                dijkstra(graph, n_start)
                buff.append((datetime.datetime.now()-start).total_seconds())
            dt_mean.append(np.mean(buff))
            dt_std.append(np.std(buff))
        plt.subplot(len(ns_node), 1, i+1)
        plt.title(r'$N_{{node}}={}$'.format(n_node))
        plt.errorbar(ns_edge, dt_mean, dt_std, color='black')
        plt.scatter(ns_edge, dt_mean)
        plt.grid()
        if i == len(ns_node)//2:
            plt.ylabel('Time [seconds]')
        elif i == len(ns_node)-1:
            plt.xlabel(r'$N_{{edge}}$')
    plt.show()

def simulate_complete_graph(T=10):
    ns_node = [int(n) for n in np.linspace(100, 1000, 10)]
    dt_mean, dt_std = [], []
    for n_node in ns_node:
        buff = []
        for _ in range(T):
            graph = gen_graph(n_node, int(n_node*(n_node-1)/2))
            n_start = random.choice([f for f, _, _ in graph])
            start = datetime.datetime.now()
            dijkstra(graph, n_start)
            buff.append((datetime.datetime.now()-start).total_seconds())
        dt_mean.append(np.mean(buff))
        dt_std.append(np.std(buff))
    plt.errorbar(ns_node, dt_mean, dt_std, color='black')
    plt.scatter(ns_node, dt_mean)
    plt.xlabel(r'$N_{{node}}$')
    plt.ylabel('Time [seconds]')
    plt.grid()
    plt.show()
```

ノード数固定でエッジ数を変化させる：

![Figure_2](https://gist.github.com/user-attachments/assets/52090d9d-d963-4c1f-972b-42f8c11a734d)

完全グラフ（全てのノードが全ての他のノードとエッジで接続）のノード数を変化させる：

![Figure_1](https://gist.github.com/user-attachments/assets/69494aeb-2595-4d31-8363-fbf1bfafc44e)

