---
title: 最適化アルゴリズム
---


目的関数（コスト関数）を最小化するための種々のアルゴリズムについてのノート。

# 最適化アルゴリズム

- $$X = \left( \boldsymbol{x}^{(1)}, \cdots. \boldsymbol{x}^{(N)} \right)$$: 全学習サンプルの集合
- $$\boldsymbol{w}$$: 更新すべき重み
- $$J(\boldsymbol{w}, X)$$: 重み $$\boldsymbol{w}$$、学習データ $$X$$ に対するコスト関数
- $$\eta$$: 学習率

## 勾配降下法

コスト関数の勾配を下る方向に重みを更新する。

![GradientDescent](https://user-images.githubusercontent.com/13412823/83935415-68c7ba00-a7f4-11ea-9c36-c860f4e3f527.png)


### 最急降下法

毎回の重み更新ステップに全ての学習サンプルを使う。

$$
\boldsymbol{w} \longleftarrow \boldsymbol{w} - \eta \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right)
$$


### SGD

確率的勾配降下法。  
毎回の重み更新ステップにランダム抽出した1件 $$\boldsymbol{x}^{(i_r)}$$ だけを使う。

$$
\boldsymbol{w} \longleftarrow \boldsymbol{w} - \eta \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, \boldsymbol{x}^{(i_r)}\right)
$$


### ミニバッチ SGD

毎回の重み更新ステップにランダム抽出した $$n\ (\lt N)$$ 件の集合 $$X_{batch}$$ を使う。

$$
\boldsymbol{w} \longleftarrow \boldsymbol{w} - \eta \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X_{batch}\right)
$$


## Momentum

お椀の中を転がって一番下を目指すイメージ。  
勾配に加えて「現在の速度」の概念を導入し、各ステップにおいて以下の操作を行う。

- 速度更新：勾配を下る方向へ加速
- 移動：現在の速度の方向へ

$$
\begin{eqnarray}
\boldsymbol{v} &\longleftarrow& \alpha \boldsymbol{v} - (1 - \alpha) \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right) \\
\boldsymbol{w} &\longleftarrow& \boldsymbol{w} + \boldsymbol{v}
\end{eqnarray}
$$

![Momentum](https://user-images.githubusercontent.com/13412823/83935416-6a917d80-a7f4-11ea-8373-c94a63ae1c7b.png)


## AdaGrad

学習を進めるにつれて学習率を減衰させる手法。

$$
\begin{eqnarray}
\boldsymbol{h} &\longleftarrow& \boldsymbol{h} +
\left( \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right) \right)^2 \\
\boldsymbol{w} &\longleftarrow& \boldsymbol{w} -
\cfrac{\eta}{\sqrt{\boldsymbol{h}+\epsilon}}
\cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right)
\end{eqnarray}
$$

$$\epsilon$$ はゼロ除算を避けるための非常に小さな正の定数。

![AdaGrad](https://user-images.githubusercontent.com/13412823/83935417-6b2a1400-a7f4-11ea-8563-c0bc7b34a6a6.png)


## RMSProp

AdaGrad の改良。  
AdaGrad では $$\boldsymbol{h}$$ が大きくなり続けるので、繰り返し回数が大きくなると重みが更新されなくなる。

$$
\begin{eqnarray}
\boldsymbol{h} &\longleftarrow& \alpha \boldsymbol{h} + (1 - \alpha)
\left( \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right) \right)^2 \\
\boldsymbol{w} &\longleftarrow& \boldsymbol{w} -
\cfrac{\eta}{\sqrt{\boldsymbol{h}+\epsilon}}
\cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right)
\end{eqnarray}
$$

![RMSProp](https://user-images.githubusercontent.com/13412823/83935418-6b2a1400-a7f4-11ea-9a66-b266b9438acd.png)


## Adam

Momentum と RMSProp を合わせた手法。

$$
\begin{eqnarray}
\boldsymbol{v} &\longleftarrow& \alpha_v \boldsymbol{v} - (1 - \alpha_v) \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right) \\
\boldsymbol{h} &\longleftarrow& \alpha_h \boldsymbol{h} + (1 - \alpha_h)
\left( \cfrac{\partial J}{\partial \boldsymbol{w}}\left(\boldsymbol{w}, X\right) \right)^2 \\
\boldsymbol{w} &\longleftarrow& \boldsymbol{w} -
\cfrac{\eta}{\sqrt{\boldsymbol{h}+\epsilon}} v
\end{eqnarray}
$$

![Adam](https://user-images.githubusercontent.com/13412823/83935419-6c5b4100-a7f4-11ea-8382-3e581e803a5a.png)


# 実装・動作確認

## コード

{% gist 9a1a242bd183fa3d4a7c4b9b52edd19a optimizer.py %}

## 動作確認

{% gist 9a1a242bd183fa3d4a7c4b9b52edd19a ~plot.py %}

（出力されるグラフ：各アルゴリズムの説明を参照）
