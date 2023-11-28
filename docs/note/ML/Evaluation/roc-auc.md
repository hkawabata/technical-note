---
title: ROC 曲線
title-en: ROC Curve
---
# 概要

ROC = 受信者操作特性（Receiver Operating Characteristic）の略。  
縦軸に **真陽性率（True Positive Rate, TPR）**、横軸に **偽陽性率（False Positive Rate, FPR）** を取り、分類モデルの性能を評価する際に用いられる。

- 真陽性率：正解が陽性のデータのうち、モデルが正しく陽性と判定できたものの割合
    - 高いほど良い
    - 再現率（Recall）と同じ
- 偽陽性率：正解が陰性のデータのうち、モデルが誤って陽性と判定してしまったものの割合
    - 低いほど良い

$$
\begin{eqnarray}
    \mathrm{TPR} &=& \cfrac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}
    \\
    \mathrm{FPR} &=& \cfrac{\mathrm{FP}}{\mathrm{FP} + \mathrm{TN}}
\end{eqnarray}
$$


# ROC 曲線の描画

モデルの評価関数の閾値 $T$ を色々変えながら、$N$ 件のテストデータを使って以下の操作を繰り返す。

1. テストデータに対する真偽を判定
2. 判定結果と正解を比べて真陽性率と偽陽性率を計算
3. (真陽性率, 偽陽性率) をグラフにプロット

![ROC](https://user-images.githubusercontent.com/13412823/80943194-9b5f4b00-8e21-11ea-9a30-bbdbe4ffea2d.png)

# ROC 曲線の見方

- グラフの左下
    - TPR も FPR も低い = 全てを陰性判定するモデル
- グラフの右上
    - TPR も FPR も高い = 全てを陽性判定するモデル
    - 陽性判定の精度は高いが、陰性判定の精度は低い
- グラフの左上
    - TPR が高く FPR が低い = 陽性も陰性も誤判定が少なく良いモデル
- グラフの右下
    - FPR が高く TPR が低い = 誤判定ばかりしてしまうモデル
    - ランダム以下の性能


# ROC-AUC

複数の閾値で総合的にモデルの性能を評価する数値として、ROC 曲線の下側の面積である **AUC**（Area Under the Curve）が用いられることが多い。  

- **ROC-AUC が大きい = 少ない誤りで真だと判定できている = 性能が良い**
- ROC-AUC = 0.5（前節の図の波線）は完全にランダムなモデルに相当

前節の図で言えば、AUC が最大の model 3 が最も高性能と言える。

# PR 曲線と ROC 曲線の使い分け

[PR 曲線](precision-recall-curve.md)を参照。

