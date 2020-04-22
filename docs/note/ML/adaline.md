---
title: ADALINE
---

# ADALINE とは

Adaptive Linear Neuron の略。  
分類問題を解くアルゴリズムで、パーセプトロンの改良のようなもの。

# 問題設定

入力値（特徴量） $$x_1, \cdots, x_m$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。

# 仕組み

## 基本原理

各入力値に重み $$w_1, \cdots, w_m$$ をかけて和を取った

$$z = \displaystyle \sum_{j=1}^{m} w_j x_j$$

を **総入力** と呼び、$$z$$ が閾値 $$\theta$$ 以上か否かで二値分類を行う。  
また、閾値 $$\theta$$ をゼロ番目の重み $$w_0 = - \theta$$ として総入力に加える（$$x_0 = 1$$）ことで、ラベル判定の閾値を0にできる。  
したがって、問題は重み $$w_0, \cdots, w_m$$ の最適化問題に帰着する。

ここまではパーセプトロンと同様。

パーセプトロンでは、総入力 $$z$$ に対する活性化関数を

$$
\phi(z) =
\begin{cases}
1  & (z \ge 0 ) \\
-1 & (z \lt 0 )
\end{cases}
$$

と定義し、ラベルの正解と予測の一致・不一致の区別のみを行い重みの更新を行った。  
ADALINE では、

$$
\phi(z) = z = \displaystyle \sum_{j=0}^{m} w_j x_j
$$

という線形活性化関数を導入する。  
→ **単純に正解ラベルと一致するかしないかではなく、「どれほど正解ラベルに近いか」という連続値による評価ができる**

ADALINE では、全サンプルに対するラベル判定誤差の平方和

$$
J(\boldsymbol{w})
= \displaystyle \frac{1}{2} \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right)^2
= \displaystyle \frac{1}{2} \sum_i \left( y^{(i)} - \sum_{j=0}^{m} w_j x_j^{(i)} \right)^2
$$

を目的関数（コスト関数）とし、これが最小になるよう、勾配降下法による学習を進めていく。  
式の先頭の $$\frac{1}{2}$$ は、後述の微分で余計な係数が消えるよう調整するパラメータなので重要ではない。

$$J(\boldsymbol{w})$$ の勾配 $$\nabla J(\boldsymbol{w})$$ の各成分は、

$$
\cfrac{\partial J(\boldsymbol{w})}{\partial w_j}
= - \displaystyle \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}
$$

よって、重み $$\boldsymbol{w}$$ の各成分を以下の式で更新するとコスト関数を小さくできる。

$$
w_j \longleftarrow w_j - \eta \cfrac{\partial J(\boldsymbol{w})}{\partial w_j} = w_j + \eta \displaystyle \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}
$$

ここで $$\eta (0 \lt \eta \le 1)$$ は学習率であり、1度に重みを更新する大きさを表す。


## 学習規則

1. 重みをゼロ or 値の小さい乱数で初期化
2. すべての学習サンプル $$\boldsymbol{x}^{(i)} = ( x_0^{(i)}, \cdots, x_m^{(i)} )$$ を使い、コスト関数 $$J(\boldsymbol{w})$$ の勾配 $$\nabla J(\boldsymbol{w})$$ を計算
3. 勾配に沿って、コスト関数が小さくなるように重みを更新
4. 収束するまで2,3を繰り返す

## 学習率と収束

「学習率が大きい = 1度の重み更新の幅が大きい」  
→ 学習率が大きすぎると収束しない

![download-4](https://user-images.githubusercontent.com/13412823/78420354-3a5d1f80-7689-11ea-9be0-3e4918c0237c.png)


# 実装

## コード

{% gist 26b3f5d976390dc98e440ffade96fcbb adaline.py %}

## 動作確認

- 点：学習データ
- 背景：モデルの決定領域

{% gist 26b3f5d976390dc98e440ffade96fcbb ~fit1.py %}

![download-1](https://user-images.githubusercontent.com/13412823/78419765-ffa4b880-7683-11ea-82b5-a7b654b716fb.png)

{% gist 26b3f5d976390dc98e440ffade96fcbb ~fit2.py %}

![download-2](https://user-images.githubusercontent.com/13412823/78419763-fddaf500-7683-11ea-9735-8383cfc7be7d.png)
