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

g = Graph()
g.edge('0', '1', 'foo')
g.edge('0', '2', 'bar')
g.view()
```

## 有向グラフ

```python
from graphviz import Digraph

g = Digraph()
g.edge('0', '1', 'foo')
g.edge('0', '2', 'bar')
g.view()
```
