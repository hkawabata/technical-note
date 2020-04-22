---
title: ロジスティック回帰
---

# ロジスティック回帰とは

分類問題を解くアルゴリズムの1つ。

- 二値分類
  - 「1クラス vs その他クラス」の二値分類を繰り返すことで、他クラス分類にも拡張できる
- 高い性能を発揮するのは線形分離可能な場合に限る


# 問題設定

入力値（特徴量） $$x_1, \cdots, x_m$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。


# 仕組み

## 原理

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
また、閾値 $$\theta$$ をゼロ番目の重み $$w_0 = - \theta$$ として総入力に加える（$$x_0 = 1$$）ことで、ラベル判定の閾値を0にできる。  
したがって、問題は重み $$w_0, \cdots, w_m$$ の最適化問題に帰着する。

ここで、総入力 $$z$$ は重み $$w_0, \cdots, w_m$$ の線形関数であり、重みの値によってあらゆる実数値を取り得る。  
→ **「$$z$$ をロジスティック関数で射影したもの」=「サンプルがクラスラベル1に属する確率 $$p$$」とみなして重みを最適化する**


### 最適化すべき目的関数

実際に起こったこと（= データサンプルとそれに対する正解ラベル）を踏まえて、それが実現する確率が最も高いような重みを探す。  
つまり、各データサンプル $$\boldsymbol{x}^{(i)}$$ が正解ラベル $$y^{(i)}$$（0 or 1）に属する確率（**尤度** $$L$$）を最大化すれば良い。

目的関数（尤度）は、

$$
\begin{eqnarray}
L(\boldsymbol{w})
&=& \displaystyle \prod_i p(y^{(i)} \mid \boldsymbol{x}^{(i)}, \boldsymbol{w}) \\
&=& \displaystyle \prod_i p(y^{(i)} \mid z^{(i)}) \\
&=& \displaystyle \prod_i \left( \phi(z^{(i)}) y^{(i)} + (1-\phi(z^{(i)})) (1 - y^{(i)}) \right) \\
&=& \displaystyle \prod_i \left( \phi(z^{(i)}) \right)^{y^{(i)}} \left( 1-\phi(z^{(i)}) \right)^{1 - y^{(i)}}
\end{eqnarray}
$$

- $$p(y^{(i)} \mid z^{(i)})$$ は、総入力 $$z^{(i)}$$ が与えられたときにクラスラベルが $$y^{(i)}$$ となる条件付き確率。
- 最後の式変形において、ラベル $$y^{(i)}$$ は 0 or 1 なので、$$y^{(i)}=1$$ なら左側、$$y^{(i)}=0$$ なら右側だけがうまく残ることを利用

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
&=& \displaystyle \sum_i \left(y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}
\end{eqnarray}
$$

最大化問題なので、勾配に沿って目的関数を増やす向きに重みを更新する：

$$
w_j \longleftarrow w_j - \eta \cfrac{\partial J}{\partial w_j} = w_j + \eta \displaystyle \sum_i \left( y^{(i)} - \phi(z^{(i)}) \right) x_j^{(i)}
$$


### 収束後のラベル判定

総入力 $$z$$ のラベルが1となる確率はロジスティック関数 $$\phi(z)$$）で与えられる。  
よって予測クラスラベル $$\hat y$$ は

$$
\hat y = \begin{cases}
1  & (\phi(z) \ge 0.5 ) \\
0 & (\phi(z) \lt 0.5 )
\end{cases}
$$

$$\phi(z) = 0.5$$ は $$z = 0$$ に対応するので、ロジスティック関数を計算する必要はなく、

$$
\hat y = \begin{cases}
1  & (z \ge 0 ) \\
0 & (z \lt 0 )
\end{cases}
$$


## 学習規則

1. 重みをゼロ or 値の小さい乱数で初期化
2. すべての学習サンプル $$\boldsymbol{x}^{(i)} = ( x_0^{(i)}, \cdots, x_m^{(i)} )$$ を使い、目的関数である対数尤度 $$l(\boldsymbol{w})$$ の勾配 $$\nabla l(\boldsymbol{w})$$ を計算
3. 勾配に沿って、対数尤度が大きくなるように重みを更新
4. 収束するまで2,3を繰り返す


# 実装

## コード

```python
import numpy as np

class LogisticRegression:
    def __init__(self, d, eta=0.001, epoch=100, max_err=10):
        """
        Parameters
        ----------
        d : 次元（変数の数）
        eta : 学習率
        epoch : エポック
        max_err : 許容する判定誤りの最大数
        """
        self.d = d
        self.eta = eta
        self.epoch = epoch
        self.max_err = max_err
        self.weight = np.zeros(d+1)  # 閾値を重みと見做す分、1つ増える

    def predict(self, x):
        """
        Parameters
        ----------
        x : 分類したいデータ（d次元ベクトル）
        """
        x_st = self.__standardize(x)
        return 1 if np.dot(x_st, self.weight[:-1]) + self.weight[-1] > 0 else 0

    def fit(self, data, labels):
        """
        Parameters
        ----------
        data :
        labels :
        """
        self.labels = labels
        self.m = np.mean(data, axis=0)
        self.std = np.std(data, axis=0)
        self.data = np.append(self.__standardize(data), np.array([[1.0] for _ in range(len(data))]), axis=1)
        for t in range(self.epoch):
            cnt_err = self.__cycle()
            if cnt_err <= self.max_err:
                print('Converged in {} cycles ({} errors in {} samples).'.format(t+1, cnt_err, len(data)))
                break

    def __cycle(self):
        """
        学習の1サイクル
        """
        cnt_err = 0
        dw = np.zeros(len(self.weight))
        for i in range(len(self.data)):
            z = np.dot(self.data[i], self.weight)
            dw += (self.labels[i] - self.__logistic(z)) * self.data[i]
            if (self.labels[i] == 0 and 0 < z) or (self.labels[i] == 1 and 0 >= z):
                cnt_err += 1
        dw *= self.eta
        self.weight += dw
        return cnt_err

    def __logistic(self, z):
        return 1 / (np.exp(-z) + 1)

    def __standardize(self, d):
        """
        データを標準化する
        """
        return (d - self.m) / self.std
```

## 動作確認

機械的に生成したデータで学習させた結果：

```python
# 学習データ作成
N = 200
c1 = [0, 0]
c2 = [-3, 4]
r1 = 2*np.random.rand(N//2)
r2 = 2.5*np.random.rand(N//2)
theta1 = np.random.rand(N//2) * 2 * np.pi
theta2 = np.random.rand(N//2) * 2 * np.pi
data1 = np.array([r1 * np.sin(theta1) + c1[0], r1 * np.cos(theta1) + c1[1]]).T
data2 = np.array([r2 * np.sin(theta2) + c2[0], r2 * np.cos(theta2) + c2[1]]).T
data = np.concatenate([data1, data2])
labels = np.array([1 if i < N//2 else -1 for i in range(N)])

# 学習
max_err = N//100
eta=1e-6
epoch=1000
lr = LogisticRegression(2, max_err=max_err, eta=eta, epoch=epoch)
lr.fit(data, labels)
```

- 点：学習データ
- 背景：モデルの決定領域

![Unknown-4](https://user-images.githubusercontent.com/13412823/79441227-f1ef1b80-8011-11ea-980d-022f7a0871bb.png)
