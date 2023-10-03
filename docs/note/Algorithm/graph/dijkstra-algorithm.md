---
title-en: Dijkstra's algorithm
title: ダイクストラ法
---

# 問題定義

グラフ構造において、各エッジが重みをもつとき、ある頂点から別の頂点への最短経路を求めたい。

# 解法

具体例をもとに手順を解説する。  
以下のグラフにおいて A から各ノードへの最短経路を求める。

![図0](https://user-images.githubusercontent.com/13412823/272174880-eb429286-adb3-4f76-a2bb-fd2b22aeb755.png)


## 準備

以下の変数を準備して初期化。

| 変数 | 内容 | 初期化 |
| :-- | :-- | :-- |
| `shortest_weight` | 「**現時点で判明している**」A から各ノードまでの最短距離を保持する辞書 | $\infty$ |
| `shortest_path` | 「**現時点で判明している**」A から各ノードまでの最短パスを保持する辞書 | null |
| `n_last_fix` | 現時点の最新ステップで最短経路が確定したノード | null |

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

## 処理の流れ

【0】スタート地点 A 自身までの最短距離が0であるのは明らか。
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

【1】最短経路が未確定のノードのうち、`n_last_fix` に直接繋がっているノード `n` それぞれについて、以下のルールで `shortest_weight`, `shortest_path` を更新する
- `d_old`：現時点でわかっているそのノードまでの最短距離 `shortest_weight[n]`
- `d_new`：現時点で判明しているスタート地点から `n_last_fix` までの最短距離`shortest_weight[n_last_fix]` + `n_last_fix` から `n` までの距離
- `d_new < d_old` なら、
    - `shortest_weight[n] = d_new` 
    - `shortest_path[n] = shortest_path[n_last_fix] + n` 

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

【2】最短経路が未確定のノードを全て見て、**現時点の重みが一番小さいノードの重みと経路を fix**（**他のルート経由では、絶対にこれより長くなる**）

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

【3】`n_last_fix` が更新されなくなるまで1,2を繰り返す。

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


# 実装

```python
import sys
from graphviz import Graph

graph = {
    # from, to, weight
    ('A', 'B', 7),
    ('A', 'C', 4),
    ('A', 'D', 2),
    ('B', 'C', 2),
    ('C', 'D', 3),
    ('B', 'E', 6),
    ('C', 'F', 2),
    ('D', 'F', 6),
    ('E', 'F', 4)
}

def show_graph(graph):
    g = Graph(format='png')
    g.graph_attr['rankdir'] = 'LR'
    for f, t, w in graph:
        g.edge(str(f), str(t), str(w))
    g.view()

def dijkstra(graph, i_start):
    # 変数準備
    todo = set()   # 未処理のノードを格納
    done = set()   # S からの最短距離を求め終わったノードを格納
    shortest_weight = {i_start: 0}          # スタートから各ノードまでの最短距離を記録
    shortest_path = {i_start: [i_start]}  # スタートから各ノードまでの最短パスを記録
    edges = {}     # 直接つながるエッジの重みを格納
    # 諸々を初期化
    for f, t, w in graph:
        todo.add(f)
        todo.add(t)
        if f not in edges:
            edges[f] = {}
        if t not in edges:
            edges[t] = {}
        edges[f][t] = w
        edges[t][f] = w
    todo.remove(i_start)
    done.add(i_start)
    n_last_fix = i_start
    while True:
        # 1ステップ前に FIX されたノードから直接つながるノードへの距離を見て最短経路を更新
        for t in edges[n_last_fix]:
            w = shortest_weight[n_last_fix] + edges[n_last_fix][t]
            if t not in shortest_weight or w < shortest_weight[t]:
                shortest_weight[t] = w
                shortest_path[t] = shortest_path[n_last_fix] + [t]
        w_min = sys.maxsize
        # 一番近い値は FIX
        for n in todo:
            if n in shortest_weight and shortest_weight[n] < w_min:
                w_min = shortest_weight[n]
                n_last_fix = n
        if w_min == sys.maxsize:
            break
        todo.remove(n_last_fix)
        done.add(n_last_fix)
    for i_goal in shortest_weight:
        print('from {} to {}: weight={}, path={}'.format(i_start, i_goal, shortest_weight[i_goal], shortest_path[i_goal]))
```

![Graph gv](https://user-images.githubusercontent.com/13412823/271911536-88878413-8d86-42af-bdd3-e86fb33ceb8e.png)


```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to C: weight=4, path=['A', 'C']
from A to D: weight=2, path=['A', 'D']
from A to B: weight=6, path=['A', 'C', 'B']
from A to F: weight=6, path=['A', 'C', 'F']
from A to E: weight=10, path=['A', 'C', 'F', 'E']

>>> dijkstra(graph, 'C')
from C to C: weight=0, path=['C']
from C to D: weight=3, path=['C', 'D']
from C to A: weight=4, path=['C', 'A']
from C to B: weight=2, path=['C', 'B']
from C to F: weight=2, path=['C', 'F']
from C to E: weight=6, path=['C', 'F', 'E']
```

ツリー状である時

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

<img width="400" alt="Graph02" src="https://user-images.githubusercontent.com/13412823/271907032-d193e110-022e-4d2a-9f8b-846418f4904d.png">

```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to D: weight=2, path=['A', 'D']
from A to C: weight=4, path=['A', 'C']
from A to B: weight=5, path=['A', 'B']
from A to G: weight=7, path=['A', 'C', 'G']
from A to H: weight=6, path=['A', 'C', 'H']
from A to F: weight=12, path=['A', 'B', 'F']
from A to E: weight=11, path=['A', 'B', 'E']

>>> dijkstra(graph, 'E')
from E to E: weight=0, path=['E']
from E to B: weight=6, path=['E', 'B']
from E to F: weight=13, path=['E', 'B', 'F']
from E to A: weight=11, path=['E', 'B', 'A']
from E to D: weight=13, path=['E', 'B', 'A', 'D']
from E to C: weight=15, path=['E', 'B', 'A', 'C']
from E to G: weight=18, path=['E', 'B', 'A', 'C', 'G']
from E to H: weight=17, path=['E', 'B', 'A', 'C', 'H']
```

グラフが分断されている時

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

<img width="500" alt="Graph03" src="https://user-images.githubusercontent.com/13412823/271907037-e169680f-6767-4df7-8102-4601f64e9f8c.png">

```python
>>> dijkstra(graph, 'A')
from A to A: weight=0, path=['A']
from A to D: weight=3, path=['A', 'C', 'D']
from A to C: weight=2, path=['A', 'C']
from A to B: weight=4, path=['A', 'C', 'B']

>>> dijkstra(graph, 'E')
from E to E: weight=0, path=['E']
from E to F: weight=4, path=['E', 'F']
from E to G: weight=5, path=['E', 'F', 'G']
```