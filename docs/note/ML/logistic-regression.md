---
title: ロジスティック回帰
---

# ロジスティック回帰とは

分類問題を解くアルゴリズムの1つ。  

- 二値分類
  - 「1クラス vs その他クラス」の二値分類を繰り返すことで、他クラス分類にも拡張できる
- 高い性能を発揮するのは線形分離可能な場合に限る

# 問題設定

入力値（特徴量） $$x_1, \cdots, x_m$$ に対し、分類ラベル $$y$$ を出力するモデルを作りたい。

# 仕組み

## 基本原理

### ロジット関数 / ロジスティック関数

クラスラベルが1か0かの二値分類を考える。  

ある入力データのクラスラベルが1となる確率を $$p$$ とすると、ラベルが0になる確率は $$1-p$$。  
この2つの確率の比 $$$$ を **オッズ比** と言う：

$${\rm odds ratio} = \cfrac{p}{1-p}$$

これを使い、**ロジット関数** を次のように定義する：

$${\rm logit}(p) = \displaystyle \log{\frac{p}{1-p}}$$

$$p$$ は確率なので $$0 \le p \le 1$$ であり、

$$
\begin{eqnarray}
\displaystyle \lim_{p \to +0} {\rm logit}(p)  &=&  -\infty \\
\displaystyle \lim_{p \to 1-0} {\rm logit}(p) &=& \infty
\end{eqnarray}
$$

なので、ロジット関数は任意の実数値を取り得る。  
言い換えると、**ロジット関数は0〜1の確率 $$p$$ を実数全体へと射影する。**

ロジット関数の逆関数 $$\phi(z)$$ を **ロジスティック関数** あるいは **シグモイド関数** と呼び、ロジスティック回帰においてはこちらが重要：

$$\phi(z) = \cfrac{1}{1+e^{-z}}$$

ロジット関数の逆関数であるから、**ロジスティック関数は任意の実数 $$z$$ を0〜1の確率 $$p$$ へ変換する。**  
図の通り、ロジット関数・ロジスティック関数はともに単調増加の連続関数であり、実数 $$z$$ が決まれば確率 $$p$$ も一意に定まる。

![download-5](https://user-images.githubusercontent.com/13412823/78424505-0d206980-76a9-11ea-972f-542b319c571c.png)

### ロジスティック関数と総入力

各入力値に重み $$w_1, \cdots, w_m$$ をかけて和を取った

$$z = \displaystyle \sum_{j=1}^{m} w_j x_j$$

を **総入力** と呼び、$$z$$ が閾値 $$\theta$$ 以上か否かで二値分類を行う。  
また、閾値 $$\theta$$ をゼロ番目の重み $$w_0 = - \theta$$ として挿入力に加える（$$x_0 = 1$$）ことで、ラベル判定の閾値を0にできる。  
したがって、問題は重み $$w_0, \cdots, w_m$$ の最適化問題に帰着する。

ここで、総入力 $$z$$ は重み $$w_0, \cdots, w_m$$ の線形関数であり、重みの値によってあらゆる実数値を取り得る。  
→ **「$$z$$ をロジスティック関数で射影したもの」=「サンプルがクラスラベル1に属する確率 $$p$$」とみなして重みを最適化する**

### 最適化すべき目的関数

実際に起こったこと（= データサンプルとそれに対する正解ラベル）を踏まえて、それが実現する確率が最も高いような重みを探す。  
つまり、各データサンプル $$\boldsymbol{x^{(i)}}$$ が正解ラベル $$y^{(i)}$$（0 or 1）に属する確率（**尤度** $$L$$）を最大化すれば良い。

目的関数（尤度）は、

$$
\begin{eqnarray}
L(\boldsymbol{w})
&=& \displaystyle \prod_i p(y^{(i)} \mid \boldsymbol{x^{(i)}}, \boldsymbol{w}) \\
&=& \displaystyle \prod_i p(y^{(i)} \mid z^{(i)}) \\
&=& \displaystyle \prod_i \left( \phi(z^{(i)}) y^{(i)} + (1-\phi(z^{(i)})) (1 - y^{(i)}) \right) \\
&=& \displaystyle \prod_i \left( \phi(z^{(i)}) \right)^{y^{(i)}} \left( 1-\phi(z^{(i)}) \right)^{1 - y^{(i)}}
\end{eqnarray}
$$

- $$p(y^{(i)} \mid z^{(i)})$$ は、総入力 $$z^{(i)}$$ が与えられたときにクラスラベルが $$y^{(i)}$$ となる条件付き確率。
- ラベル $$y^{(i)}$$ は 0 or 1 なので、最終的な数式に置いて $$y^{(i)}=1$$ なら左側、$$y^{(i)}=0$$ なら右側だけがうまく残る

積を計算すると尤度が小さい場合にアンダーフローが起こってしまう可能性がある。  
また、勾配降下法による最大化を行う際、積よりも和の方が微分が計算しやすい。  
→ 尤度そのものではなく、以下の対数尤度を最大化する。

$$
l(\boldsymbol{w})
= \log{L(\boldsymbol{w})}
= \displaystyle \sum_i y^{(i)} \log{\phi(z^{(i)})} + \sum_i (1-y^{(i)}) \log{(1-\phi(z^{(i)}))}
$$

### 勾配降下法による重みの更新

$$l(\boldsymbol{w})$$ の勾配 $$\nabla l(\boldsymbol{w})$$ の $$j$$ 成分は、

$$
\begin{eqnarray}
\cfrac{\partial l(\boldsymbol{w})}{\partial w_j}
&=& \displaystyle \left( \sum_i y^{(i)} \frac{1}{\phi(z^{(i)})} - \sum_i (1-y^{(i)}) \frac{1}{(1-\phi(z^{(i)}))} \right) \cfrac{\partial \phi(z^{(i)})}{\partial w_j} \\
&=& \displaystyle \left( \sum_i y^{(i)} (1+e^{-z^{(i)}}) - \sum_i (1-y^{(i)}) \frac{1+e^{-z^{(i)}}}{e^{-z^{(i)}}} \right) \cfrac{e^{-z^{(i)}}}{(1+e^{-z^{(i)}})^2}\ x_j^{(i)} \\
&=& \displaystyle \left( \sum_i y^{(i)} \frac{e^{-z^{(i)}}}{1+e^{-z^{(i)}}} - \sum_i (1-y^{(i)}) \frac{1}{1+e^{-z^{(i)}}} \right) x_j^{(i)} \\
&=& \displaystyle \left( \sum_i y^{(i)} (1-\phi(z^{(i)})) - \sum_i (1-y^{(i)}) \phi(z^{(i)}) \right) x_j^{(i)} \\
&=& \displaystyle \sum_i (y^{(i)} - \phi(z^{(i)}) ) x_j^{(i)}
\end{eqnarray}
$$

最大化問題なので、勾配に沿って目的関数を増やす向きに重みを更新する：

$$
w_j \longleftarrow w_j - \eta \cfrac{\partial J}{\partial w_j} = w_j + \eta \displaystyle \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}
$$

## 学習規則

1. 重みをゼロ or 値の小さい乱数で初期化
2. すべての学習サンプル $$\boldsymbol{x}^{(i)} = ( x_0^{(i)}, \cdots, x_m^{(i)} )$$ を使い、目的関数である対数尤度 $$l(\boldsymbol{w})$$ の勾配 $$\nabla l(\boldsymbol{w})$$ を計算
3. 勾配に沿って、対数尤度が大きくなるように重みを更新
4. 収束するまで2,3を繰り返す
