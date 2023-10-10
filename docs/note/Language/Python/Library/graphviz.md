---
title: graphviz
---
# 概要

# インストール

```bash
brew install graphviz  # graphviz 自体のインストール
pip install graphviz   # python から使うためのライブラリ
```

# 使い方

## 無向グラフ

```python
from graphviz import Graph

g = Graph(format='png', filename='graph')
# グラフ全体の設定
g.graph_attr.update(
    rankdir='LR'
)
# ノードの汎用設定
g.node_attr.update(
    shape='box',             # ノード設定：形を長方形に
    style='filled',          # ノード設定：
    color='red',             # ノード設定：
    fontname='MS Gothic',    # ノード設定：
    fontsize='20',           # ノード設定：
    fontcolor='magenta',     # ノード設定：
    fillcolor='lightblue',   # ノード設定：
    height='0.8',            # ノード設定：高さ
    width='1.6'              # ノード設定：横幅
)
g.edge_attr.update(
    color='orange'
)

g.node('A')             # ノードの名前とラベルを同じ値に
g.node('B', 'Bob')      # ノードの名前とラベルを別の値に
g.node('C',
       shape='square',  # 形を正方形に
       penwidth='5'     # ペンの太さ（線の太さ）
)

g.edge('A', 'B', 'foo')  # A から B へ「foo」というエッジを張る
g.edge('A', 'C', 'bar',
       color='green',
       fontcolor='blue',
       penwidth='3'
)
g.view()
```

## 有向グラフ

```python
from graphviz import Digraph

g = Digraph(format='png', filename='digraph')
g.edge('0', '1', 'foo')
g.edge('0', '2', 'bar',
       arrowhead='dot',
       color='red',
       fontcolor='blue'
)
g.view()
```

## クラスター

```python
g = Digraph(format='png', filename='cluster')
with g.subgraph(name='Cluster 1') as c1:
    c1.node('C1-1')
    c1.node('C1-2')
    c1.edge('C1-1', 'C1-2')

with g.subgraph(name='Cluster 2') as c2:
    c2.node('C2-1')
    c2.node('C2-2')
    c2.edge('C2-1', 'C2-2')

g.node('Root')
g.edge('Root', 'C1-1', 'AAA')
g.edge('Root', 'C2-1', 'BBB')
g.edge('C1-2', 'C2-2', 'CCC')
g.view()
```
