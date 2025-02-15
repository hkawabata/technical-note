---
title: ベルマンフォード法
title-en: Bellman–Ford algorithm
---
# 問題定義

エッジが重みを持つ**有向グラフ**構造において、ある頂点から別の頂点への最短経路を求めたい。  
エッジが負の値を持つ（通るとコストが下がるエッジがある）ケースも想定する。

> **【NOTE】無向グラフだとなぜダメ？**
> 
> 無向グラフに負のエッジがある場合、負のエッジの両端を何度も往復することで無限にコスト総和を小さくできてしまうため、問題自体が解なしとなり意味をなさない


# アルゴリズム

有向グラフにおける[ダイクストラ法](dijkstra-algorithm.md)を、エッジが負の重みを持つ場合にも拡張したもの。

- ダイクストラ法だとなぜダメ？
    - ダイクストラ法では、各ステップごとに1つのノードまでの最短距離が確定できた
    - そのため、以後のステップでは確定済みノードには注目する必要がなかった
    - しかし負のエッジがあると、その後のステップで「もっとコスト総和が小さい経路」が発見される可能性がある
- ダイクストラ法をどう改善する？
    - 処理途中では最短経路を確定させず、各ステップで「前ステップで最小コストが更新されたノード」から伸びる経路を全て見直す
    - 途中で全てのノードの最短経路が更新されなくなったら処理終了

具体例をもとに手順を解説する。  
以下のグラフにおいて A から各ノードへの最短経路を求める。

![図0](https://gist.github.com/user-attachments/assets/cd07126f-f6d5-4332-84a1-cdb86dce0553)


## 【0】変数の初期化

以下の変数を準備して初期化。

| 変数                   | 内容                                            | 初期値                                      |
| :------------------- | :-------------------------------------------- | :--------------------------------------- |
| `shortest_weight`    | 「**現時点で判明している**」A から各ノードまでの最短距離（最小コスト）を保持する辞書 | ・スタート地点：0<br>・その他のノード：$\infty$           |
| `shortest_path`      | 「**現時点で判明している**」A から各ノードまでの最短パスを保持する辞書        | ・スタート地点：`array(スタート地点)`<br>・その他のノード：null |
| `nodes_last_updated` | 最新ステップで最短経路が更新されたノードのリスト                      | `array(スタート地点)`                          |

![図1](https://gist.github.com/user-attachments/assets/0d93ce55-7748-4cf7-bff6-242de8ccfbb9)

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

nodes_last_updated = ['A']
```

## 【1】前ステップの更新ノードから遷移できる隣接ノードの情報を更新

`nodes_last_updated` に含まれるノード `n_last_updated` それぞれについて、そこから1ホップで遷移できるノード `n_next` までの最短距離 `shortest_weight`（+最短パス `shortest_path`）を以下のルールで更新：
- $d_\mathrm{old}$：現時点でわかっているスタートから遷移先ノードまでの最短距離 `shortest_weight[n_next]`
- $d_\mathrm{new}$：以下の2つの和
    - スタートから `n_last_updated` までの最短距離`shortest_weight[n_last_updated]`
    - `n_last_updated` から `n_next` までの距離
- $d_\mathrm{new} \lt d_\mathrm{old}$ なら最短距離・最短経路を更新：
    - `shortest_weight[n] = d_new` 
    - `shortest_path[n] = shortest_path[n_last_fix] + n_next` 

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
```

![図2](https://gist.github.com/user-attachments/assets/75601912-2287-41b4-b74b-6387a12cdb55)

## 【2】「前ステップの更新ノード」の更新

1で更新されたノードのリストを新たな `nodes_last_updated` に格納する。

```python
nodes_last_updated = ['B', 'C', 'D']
```

## 【3】最短距離が収束するまで1,2を繰り返す

全ノード数を $N$ として、最大 $N-1$ 回まで1,2の操作を繰り返す。  
ループ回数が $N-1$ 回以下であっても、あるステップで最短距離が更新されたノードがゼロ件だった場合（`nodes_last_updated = array()`）、そこでループを終了する。

![図3](https://gist.github.com/user-attachments/assets/599b21b9-80ea-4991-985a-914eb09b9b6a)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 7,
    'C': 4,
    'D': 1,             # updated
    'E': 1,             # updated
    'F': 8              # updated
}

shortest_path = {
    'A': ['A'],            # (fixed)
    'B': ['A', 'B'],
    'C': ['A', 'C'],
    'D': ['A', 'C', 'D'],  # updated
    'E': ['A', 'B', 'E'],  # updated
    'F': ['A', 'D', 'F']   # updated
}

nodes_last_updated = ['D', 'E', 'F']
```

![図4](https://gist.github.com/user-attachments/assets/0f6b0287-1d47-4534-893e-856663a0c0f5)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 7,
    'C': 4,
    'D': 1,
    'E': 1,
    'F': 5              # updated
}

shortest_path = {
    'A': ['A'],                # (fixed)
    'B': ['A', 'B'],
    'C': ['A', 'C'],
    'D': ['A', 'C', 'D'],
    'E': ['A', 'B', 'E'],
    'F': ['A', 'B', 'E', 'F']  # updated
}

nodes_last_updated = ['F']
```

![図5](https://gist.github.com/user-attachments/assets/d704dc28-5ea0-44de-b9c9-f7b5d94529f7)

```python
shortest_weight = {
    'A': 0,             # (fixed)
    'B': 7,             # fixed
    'C': 4,             # fixed
    'D': 1,             # fixed
    'E': 1,             # fixed
    'F': 5              # fixed
}

shortest_path = {
    'A': ['A'],                # (fixed)
    'B': ['A', 'B'],           # fixed
    'C': ['A', 'C'],           # fixed
    'D': ['A', 'C', 'D'],      # fixed
    'E': ['A', 'B', 'E'],      # fixed
    'F': ['A', 'B', 'E', 'F']  # fixed
}

nodes_last_updated = []
```

この例では、$N-1 = 5$ ステップよりも小さい4ステップでループが終了した。


## 【3】負閉路の判定と最短経路の確定

グラフに **負閉路**（1周するとコスト総和がマイナスになる経路）が存在する場合、これを何周も周回することでいくらでもコスト総和を下げられるので、「最短経路」が存在しない。  
→ 問題の回答としては「解なし」

したがってループが $N-1$ 周しても `nodes_last_updated` が空でない場合は、「負閉路があるため最短経路なし」を最終結果とする。

ループがそれ以下の回数で収束しているか、ちょうど $N-1$ 周で `nodes_last_updated` が空になった場合は、そのときの `shortest_weight`, `shortest_path` が最短距離 & 最短経路となる。


# 実装・動作確認

## 実装

{% gist bad05cf6461186d97b9403ff9f6dfedc 20250216_bellman_ford.py %}


## 動作確認

アルゴリズム解説の節で挙げた例：

![Digraph gv](https://gist.github.com/user-attachments/assets/d43194d4-5f6e-49a2-a7cb-3628adb36a32)

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
show_graph(graph)
bellman_ford(graph, 'A')
```

```python
>>> bellman_ford(graph, 'A')
from A to A: weight=0, path=['A']
from A to B: weight=7, path=['A', 'B']
from A to C: weight=4, path=['A', 'C']
from A to D: weight=1, path=['A', 'C', 'D']
from A to E: weight=1, path=['A', 'B', 'E']
from A to F: weight=5, path=['A', 'B', 'E', 'F']
```


負閉路（negative cycle）がある例：

![Digraph2 gv](https://gist.github.com/user-attachments/assets/861db199-5ab0-404e-9c06-e297bd56105b)

```python
graph = {
    # (from, to): weight
    ('A', 'B'): 7,
    ('A', 'C'): 4,
    ('A', 'D'): 2,
    ('B', 'C'): 2,
    ('C', 'D'): -3,
    ('B', 'E'): -6,
    ('D', 'F'): -1,
    ('E', 'F'): 4,
    ('F', 'C'): 2
}
show_graph(graph)
bellman_ford(graph, 'A')
```

```python
>>> bellman_ford(graph, 'A')
Negative cycle exists.
```
