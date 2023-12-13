---
title: MAP (Mean Average Precision)
---
# 概要

**MAP = Mean Average Precision**

ランキングアルゴリズムの性能を評価する指標の1つ。

# 計算方法

## 変数の定義

- $q_j$：評価のためのテストクエリ
- $\left\vert Q \right\vert$：評価クエリの総数
- $n_j$：評価データセット中のドキュメントのうち、クエリ $q_j$ に適合するものの数（正解データ数）

## 平均適合率 (Average Precision) の計算

評価対象のランキングアルゴリズムに検索クエリ $q$ を与えた時、合計 $n$ 件の正解ドキュメントが順位 $r = r_1, r_2, \cdots, r_n\,(r_1\lt r_2 \lt \cdots \lt r_n)$ に現れるとする。  
また、検索結果の上位 $r_i$ 件で評価した適合率を $p(q, r_i)$ とする。  
全ての $p(r_i)$ を計算して平均を取った

$$
\mathrm{AP} := \cfrac{1}{n} \sum_{i=1}^n p(q, r_i)
$$

を **平均適合率 (Average Precision)** と呼ぶ。

例：3件の評価用クエリ $q_1,q_2,q_3$ について、評価用ドキュメント中に適合するものがそれぞれ $(n_1, n_2, n_3) = (4,3,2)$ 件あり、モデルによるランキング結果が以下のようになった時

| 順位 $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $\cdots$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $q_1$ の検索結果として正しい？ | o | x | o | o | x | o | x | x | x | x | $\cdots$ |
| 順位 $r$ までで評価した適合率 $p_1(r)$ | $1/1$ | - | $2/3$ | $3/4$ | - | $4/6$ | - | - | - | - | $\cdots$ |
| $q_2$ の検索結果として正しい？ | x | o | o | x | o | x | x | x | x | x | $\cdots$ |
| 順位 $r$ までで評価した適合率 $p_2(r)$ | - | $1/2$ | $2/3$ | - | $3/5$ | - | - | - | - | - | $\cdots$ |
| $q_3$ の検索結果として正しい？ | o | o | x | x | x | x | x | x | x | x | $\cdots$ |
| 順位 $r$ までで評価した適合率 $p_3(r)$ | $1/1$ | $2/2$ | - | - | - | - | - | - | - | - | $\cdots$ |

$$
\begin{eqnarray}
    \mathrm{AP}(q_1) &=& \cfrac{1}{4} \left(
        \cfrac{1}{1} +
        \cfrac{2}{3} +
        \cfrac{3}{4} +
        \cfrac{4}{6}
    \right)
    = \cfrac{37}{48} \simeq 0.771
    \\
    \mathrm{AP}(q_2) &=& \cfrac{1}{3} \left(
        \cfrac{1}{2} +
        \cfrac{2}{3} +
        \cfrac{3}{5}
    \right)
    = \cfrac{53}{90} \simeq 0.589
    \\
    \mathrm{AP}(q_3) &=& \cfrac{1}{2} \left(
        \cfrac{1}{1} +
        \cfrac{2}{2}
    \right)
    = 1.0
\end{eqnarray}
$$


## MAP (Mean Average Precision) の計算

**MAP**：複数のテストクエリ $q_1, \cdots, q_{\vert Q\vert}$ について AP を計算して平均をとったもの。

$$
\begin{eqnarray}
    \mathrm{MAP}
    &=& \displaystyle \frac{1}{\left|Q\right|} \sum_{j=1}^{\left|Q\right|} \mathrm{AP}(q_j)
    \\
    &=& \displaystyle \frac{1}{\left|Q\right|} \sum_{j=1}^{\left|Q\right|} \cfrac{1}{n_j} \sum_{i=1}^{n_j} p(q_j, r_i)
\end{eqnarray}
$$

例：前節の AP と同じ例を用いると、

$$
\begin{eqnarray}
    \mathrm{MAP} &=& \cfrac{1}{3} (\mathrm{AP}(q_1) + \mathrm{AP}(q_2) + \mathrm{AP}(q_3))
    \\ &=&
    \cfrac{1}{3} \left( \cfrac{37}{48} + \cfrac{53}{90} + 1.0 \right)
    \\ &\simeq& 0.787
\end{eqnarray}
$$
