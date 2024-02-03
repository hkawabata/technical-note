---
title: node2vec
---
# 概要

（重み付き）無向グラフに対して [Word2Vec](../../NLP/word2vec.md) の技術を応用し、グラフの各ノードをベクトル空間に embedding する手法。

元論文：[node2vec: Scalable Feature Learning for Networks](https://arxiv.org/abs/1607.00653)


# 理論

以後、例として以下の重み付きグラフを考える。エッジの横の数字は重みを表す。

```
      4       1
  A ----- B ------ C
  |     /        /
2 |   / 2      / 3
  | /        /
  D ------ E
      1
```

## ランダムウォークによるパスのサンプリング

グラフ内の全てのノード $n$ 個を出発点として、長さ $k$ のランダムウォーク探索を $m$ 回ずつ行う。

このランダムウォークにおいて、次に移るノードの選び方は完全なランダムではなく、以下の2つの重み $\alpha, w$ の積 $\alpha w$ を用いて遷移確率に重みづけを行う。

### 重み1：幅優先 or 深さ優先

グラフにおいて「ノードが似ている」には2つの考え方がある。

1. **homophily**：2つのノードがグラフ上で近くに存在するか
2. **structural equivalence**：構造が似ているか
    1. ex. 多数のノードと繋がっているもの同士（ノードはグラフ上で遠く離れていても良い）

homophily を重視して類似度を定義する場合、近くのノードを優先的に探索したいので、**幅優先探索（breadth first search, BFS）** が望ましい。  
structural equivalence を重視する場合、遠くであっても似た構造のノードを見つけたいので、**深さ優先探索（depth first search, DFS）** が適する。

![node2vec-bfs-dfs](https://gist.github.com/assets/13412823/71bdcae3-1dd7-4064-b8e6-d58b8db8aa70)


解きたい問題に応じて、BFS/DFS どちらをどの程度重視するかを制御するため、パラメータ $p,q \gt 0$ を導入する。

```
previous : A
now      : D
next     : ?

      A ----- B ------ C
      |     /        /
a=1/p |   / a=1    /
      | /        /
      D ------ E
        a=1/q
```

図のグラフで A から D へ移ってきたあと、その次にどこへ移るかを考える。
D からの遷移先は A,B,E の3つが考えられるが、これを条件により3つに分類し、遷移確率に重みづけを行う：

1. 移ってくる前のノード（A）
    1. 重み $\alpha = 1/p$
2. 移ってくる前のノード $t$ に隣接するノード（B）
    1. 重み $\alpha = 1$
3. その他。$t$ から離れたノード（E）
    1. 重み $\alpha = 1/q$

**$p$ が小さいほど元のノードに戻りやすいので幅優先（BFS）、$q$ が小さいほど元のノードから離れて行きやすいので深さ優先（DFS）**。


### 重み2：エッジ自体の重み

今いるノードから隣のノードに伸びる各エッジの重み $w$ を考慮する。

```
       w=4     w=1
    A ----- B ------ C
    |     /        /
w=2 |   / w=2    / w=3
    | /        /
    D ------ E
       w=1
```

## Word2Vec (skip-gram) による学習

（skip-gram の詳細については [word2vec](../../NLP/word2vec.md) のノートを参照）

長さ $k=3$、回数 $m=2$ のランダムウォークの結果、以下のようなパスがサンプリングできたとする。

```
[path A1]  A -> B -> C -> E
[path A2]  A -> D -> B -> A
[path B1]  B -> A -> B -> D
[path B2]  B -> D -> A -> B
[path C1]  C -> E -> C -> E
[path C2]  C -> E -> D -> A
[path D1]  D -> A -> B -> C
[path D2]  D -> B -> A -> D
[path E1]  E -> C -> B -> A
[path E2]  E -> D -> A -> B
```

ノードを Word2Vec でいう単語だと考えれば、これらのパスは、Word2Vec で言うコーパス（学習対象の文章）にあたる。

前後1単語の範囲で skip-gram のための学習データを作ると、得られる（入力, 正解）の組は

```
[path A1]  (A, B), (B, A), (B, C), (C, B), (C, E), (E, C)
[path A2]  (A, D), (D, A), (D, B), (B, D), (B, A), (A, B)
[path B1]  (B, A), (A, B), (A, B), (B, A), (B, D), (D, B)
[path B2]  ...
[path C1]  ...
[path C2]  ...
[path D1]  ...
[path D2]  ...
[path E1]  ...
[path E2]  ...
```

ノード A〜E を one-hot ベクトル $\boldsymbol{v}_A, \cdots, \boldsymbol{v}_E$ で表す：

$$
\begin{eqnarray}
    \boldsymbol{v}_A &=& (1,0,0,0,0) \\
    \boldsymbol{v}_B &=& (0,1,0,0,0) \\
    \boldsymbol{v}_C &=& (0,0,1,0,0) \\
    \boldsymbol{v}_D &=& (0,0,0,1,0) \\
    \boldsymbol{v}_E &=& (0,0,0,0,1)
\end{eqnarray}
$$

これを用いると、入力データ（コンテキスト）$Context$ は

$$
Context =
\begin{pmatrix}
    A \\ B \\ B \\ C \\ C \\ E \\ \hline
    A \\ D \\ D \\ B \\ B \\ A \\ \hline
    B \\ A \\ A \\ B \\ B \\ D \\ \hline
    \\ \vdots \\ \\
\end{pmatrix}
=
\begin{pmatrix}
    1&0&0&0&0 \\ 0&1&0&0&0 \\ 0&1&0&0&0 \\ 0&0&1&0&0 \\ 0&0&1&0&0 \\ 0&0&0&0&1 \\ \hline
    1&0&0&0&0 \\ 0&0&0&1&0 \\ 0&0&0&1&0 \\ 0&1&0&0&0 \\ 0&1&0&0&0 \\ 1&0&0&0&0 \\ \hline
    0&1&0&0&0 \\ 1&0&0&0&0 \\ 1&0&0&0&0 \\ 0&1&0&0&0 \\ 0&1&0&0&0 \\ 0&0&0&1&0 \\ \hline
    \\ && \vdots \\ \\
\end{pmatrix}
$$

正解データ $Answer$ は

$$
Answer =
\begin{pmatrix}
    B \\ A \\ C \\ B \\ E \\ C \\ \hline
    D \\ A \\ B \\ D \\ A \\ B \\ \hline
    A \\ B \\ B \\ A \\ D \\ B \\ \hline
    \\ \vdots \\ \\
\end{pmatrix}
=
\begin{pmatrix}
    0&1&0&0&0 \\ 1&0&0&0&0 \\ 0&0&1&0&0 \\ 0&1&0&0&0 \\ 0&0&0&0&1 \\ 0&0&1&0&0 \\ \hline
    0&0&0&1&0 \\ 1&0&0&0&0 \\ 0&1&0&0&0 \\ 0&0&0&1&0 \\ 1&0&0&0&0 \\ 0&1&0&0&0 \\ \hline
    1&0&0&0&0 \\ 0&1&0&0&0 \\ 0&1&0&0&0 \\ 1&0&0&0&0 \\ 0&0&0&1&0 \\ 0&1&0&0&0 \\ \hline
    \\ && \vdots \\ \\
\end{pmatrix}
$$

これらを用いて skip-gram による学習を行えば、A〜E のベクトル表現が得られる。


# 実装

word2vec 部分は gensim ライブラリを使う。  
パラメータは適当にせっていしたので、チューニングの余地がありそう。

{% gist 4b6d26c20b014782573a81dec04a069c 20240201_node2vec.py %}


## 例1

![node2vec1](https://gist.github.com/assets/13412823/e9bf2408-fe2f-4653-a88f-fdc351eb855a)

{% gist 4b6d26c20b014782573a81dec04a069c ~example1.py %}

| 幅優先 | 深さ優先 |
| :-- | :-- |
| ![ex1-bfs](https://gist.github.com/assets/13412823/e002f397-9478-4dd7-ab83-2fd1a277a415) | ![ex1-dfs](https://gist.github.com/assets/13412823/91acf187-dbc5-415d-aa90-1a9a8e8fa159) |

- 幅優先
    - グラフ上で近いノードとの類似度が高い
- 深さ優先
    - ハブになっている C, D, J, L, Q は類似度が高い
    - C から見ると、距離的に近い A, B との類似度も高い
- いずれも遠方で構造も似ていないノードは類似度が低い


## 例2

![node2vec2](https://gist.github.com/assets/13412823/0d7cc3be-af6e-4049-ba71-2b6053155878)

{% gist 4b6d26c20b014782573a81dec04a069c ~example2.py %}

| 幅優先 | 深さ優先 |
| :-- | :-- |
| ![ex2-bfs](https://gist.github.com/assets/13412823/d7ae811b-2c62-4fe1-9619-a96cc840599e) | ![ex2-dfs](https://gist.github.com/assets/13412823/0a865187-ef93-4d14-b216-83ad9db2049d) |

A から見て、
- 幅優先
    - グラフ上で近い H, G, I, K, J, L との類似度が高い
    - グラフ上で遠い D, E, F は embedding 空間上でも距離が遠い
- 深さ優先
    - ハブになっている A, B, C の類似度が高い
    - 距離的に近い G, H, I, J, K, L との類似度も高い
    - G, H, I などはグラフ上では近い位置にあるが embedding 空間では遠い
