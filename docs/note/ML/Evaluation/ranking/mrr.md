---
title: MRR (Mean Reciprocal Rank)
---
# 概要

**MRR = Mean Reciprocal Rank**

ランキングアルゴリズムの性能を評価する指標の1つ。

# 計算方法

$\vert Q \vert$ 個の評価用検索クエリ $q_i\,(i=1,\cdots,\vert Q \vert)$ によるランキング結果に関して、クエリに適合するドキュメントが最初に現れる順位を $r(q_i)$ とする。

$$
\mathrm{MRR} = \cfrac{1}{\vert Q \vert} \sum_{i=1}^{\vert Q \vert} \cfrac{1}{r(q_i)}
$$

具体例：4つのクエリ $q_1,q_2,q_3,q_4$ について、ランキングモデルの検索結果が以下のようになったとき（o：正解、x：不正解）

| 順位 $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | $\cdots$ | 初めて正解ドキュメントが当たる順位 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $q_1$ | o | o | x | o | o | x | x | $\cdots$ | 1 |
| $q_2$ | x | o | x | x | x | o | x | $\cdots$ | 2 |
| $q_3$ | x | o | o | o | o | o | o | $\cdots$ | 2 |
| $q_4$ | x | x | x | x | o | x | o | $\cdots$ | 5 |

$$
\mathrm{MRR} = \cfrac{1}{4} \left(
    \cfrac{1}{1} + \cfrac{1}{2} + \cfrac{1}{2} + \cfrac{1}{5}
\right)
= \cfrac{1}{4} \cdot \cfrac{22}{10}
= \cfrac{11}{20} = 0.55
$$

# 特徴

ランキング結果の最初の正解だけに焦点を合わせる（2番目以降の正解には注目しない）。

- 最適な結果1つだけが重要な場合など、対象を絞った用途のランキングの評価に適する
- 前述の具体例における $q_2$ と $q_3$ のように、検索結果のリスト全体で見ると正解率が全く異なる場合でも、初めて正解になる順位が同じなら同じ重みになる
    - → トップ1件ではなく関連アイテムのリストを参照したいユーザーにとっては適切な評価指標ではない可能性あり
