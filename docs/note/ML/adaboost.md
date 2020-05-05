---
title: AdaBoost
---

# AdaBoost

アンサンブル学習の1手法、**ブースティング** の一種。

## 問題設定

入力値（特徴量） $$x_1, \cdots, x_m$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。


## 学習の手順

ランダムよりは少し良い程度の弱分類器を使い、以下の操作を行う。

1. $$N$$ 個の訓練データサンプルの重み $$\boldsymbol{w} = (w^{(1)}, \cdots, w^{(N)})$$ を同じ値（$$1/N$$）で初期化
2. 重みの大きなデータサンプルを優先的に見ながら、弱分類機をトレーニング
    - 重み付き誤分類率 $$\varepsilon = \displaystyle \sum_{i=1}^N w^{(i)} (\hat{y}^{(i)} \neq y^{(i)})$$ が最小となるように学習
    - ここで $$\hat{y}^{(i)} \neq y^{(i)}$$ は予測ラベル $$\hat{y}^{(i)}$$ が正解ラベル $$y^{(i)}$$ と一致すれば0、一致しないければ1
3. 誤分類されたデータの重みを増やし、正しく分類されたデータの重みを減らす
    - $$\alpha = 0.5 \log{\cfrac{1-\varepsilon}{\varepsilon}}$$ を用いて下式で重みを更新
        - $$\hat{y}^{(i)} = y^{(i)}$$ のとき：$$w^{(i)} \longleftarrow w^{(i)} e^{-\alpha}$$
        - $$\hat{y}^{(i)} \neq y^{(i)}$$ のとき：$$w^{(i)} \longleftarrow w^{(i)} e^{\alpha}$$
4. 重みを合計が1になるように正規化
5. 2〜4を繰り返し

## 実装

### コード

弱分類器（決定株）：

{% gist 9ce0ae44725f7885eada44b56a264e65 decision-stump.py %}

AdaBoost：

{% gist 9ce0ae44725f7885eada44b56a264e65 adaboost.py %}

### 動作確認

{% gist 9ce0ae44725f7885eada44b56a264e65 ~fit.py %}

個別の決定株：

![Decision Stumps](https://user-images.githubusercontent.com/13412823/81028224-70293a00-8ebb-11ea-9950-3abada25b814.png)


AdaBoost：

![AdaBoost](https://user-images.githubusercontent.com/13412823/81028228-73242a80-8ebb-11ea-9078-4e5cc8d0a2bf.png)
