---
title: k 近傍法
---

# k 近傍法（kNN）とは

分類問題を解くアルゴリズムの1つ。k-Nearest Neighbor

教師データから識別関数を学習しない **怠惰学習（lazy learner）** の代表例。

# 問題設定

入力値（特徴量） $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。

# 仕組み

ラベルを判定したい未知のデータの近傍 $$k$$ 件の正解データサンプルで多数決を取る。

## 訓練

データの前処理だけ行えばよく、事前の学習は必要ない。

- 教師データ（入力 $$\boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)}$$ とその正解ラベル $$y^{(1)}, \cdots, y^{(n)}$$）をモデル内に保持する
- **特徴量ごとにスケールが異なると寄与率に差が出るので、入力は標準化しておく**

## ラベル判定

未知の入力 $$\boldsymbol{x}$$ に対し、全教師データとの間の距離

$$
d^{(i)} = \| \boldsymbol{x} - \boldsymbol{x}^{(i)} \|
$$

を計算する（$$\boldsymbol{x}$$ も標準化する）。

**距離 $$d^{(i)}$$ が小さい方から $$k$$ 件の教師データを探し、それらの正解ラベルの多数決でラベルを決定する**。

ハイパーパラメータ $$k$$ は事前に決めておく。


# 実装

## コード

{% gist fda2ceb4e8a90edd21a39400eeabaef3 knn.py %}

## 動作確認

{% gist fda2ceb4e8a90edd21a39400eeabaef3 ~fit.py %}

![kNN](https://user-images.githubusercontent.com/13412823/80159295-96babb80-8605-11ea-8984-6d7924be83ad.png)
