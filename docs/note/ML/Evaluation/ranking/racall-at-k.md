---
title: Recall@k
---
# 概要

ランキングアルゴリズムの性能を評価する指標の1つ。**R@k** のように略記することが多い。  
ランキング結果の上位 $k$ 件を見て、全正解数のうち何件が含まれるかの割合を計算する。


# 計算例

全部で7件の正解があるとき

| 順位 $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $\cdots$ |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 検索結果の正誤 | o | x | o | o | x | o | x | x | o | x | $\cdots$ |
| R@k | $1/7$ | $1/7$ | $2/7$ | $3/7$ | $4/7$ | $4/7$ | $4/7$ | $4/7$ | $5/7$ | $5/7$ | $\cdots$ |
