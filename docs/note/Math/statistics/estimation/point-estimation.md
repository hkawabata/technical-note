---
title: 点推定
title-en: Point Estimation
---

# 点推定とは

標本の統計量から母集団の母数（母平均や母分散など）を推定すること。

推定された値（推定値）は上にハット記号（ $\hat{}$ ）をつけて表す。

# 点推定の例

以後、大きさ $N$ の母集団から $n$ 件の標本 $x_1, \cdots, x_n$ を抽出する場合を考える。

## 母平均の点推定

母平均の[不偏推定量](unbiased-estimator.md)は標本平均であるから、母平均 $\mu$ の推定値は

$$
\hat{\mu} = \cfrac{1}{n} \sum_{i=1}^n x_i
$$

## 母分散の点推定

母分散の[不偏推定量](unbiased-estimator.md)は不偏分散であるから、母分散 $\sigma^2$ の推定値は

$$
\hat{\sigma}^2 = \cfrac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
$$

ここで、$\bar{x}$ は標本平均。
