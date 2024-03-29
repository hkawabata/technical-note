---
title: 勾配ブースティング決定沐浴 (GBDT)
---

# 勾配ブースティング決定木 (GBDT) の概要

GBDT = Gradient Boosting Decision Tree

アンサンブル学習の[ブースティング](../ensemble-learning/boosting.md)と決定木、勾配降下法を組み合わせた手法。  
決定木で算出した予測値と目的変数の誤差を勾配降下法を用いて最小化する

# GBDT の計算手順

1. 決定木を作成し、予測値の初期値を計算
2. 予測値と目的関数の誤差を計算
3. この誤差が小さくなるように勾配効果法でパラメータを変更
4. 1〜3を決まった回数（もしくは収束するまで）繰り返す
5. 「予測対象のデータがそれぞれの決定木で属する葉のウェイトの和が予測値となる」？？？

# GBDT の実装

代表的なものに [XGBoost](xgboost.md) と [LightGBM](light-gbm.md) がある。

|  | XGBoost | LightGBM |
| :-- | :-- | :-- |
| 探索 | 深さ優先探索 | 幅優先探索 |
| デメリット | 計算が遅い | 過学習しやすい |
|  |  |  |
|  |  |  |

