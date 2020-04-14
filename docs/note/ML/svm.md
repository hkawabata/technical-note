---
title: サポートベクトルマシン（SVM）
---

# サポートベクトルマシン（SVM）とは

分類問題を解くアルゴリズムの1つ。

分類問題において、一般に決定境界は無数に考えられ、1つに特定できない：

![Unknown](https://user-images.githubusercontent.com/13412823/78503499-daa66780-77a1-11ea-9319-955d0329e69a.png)

（上図において、いずれの決定境界を採用しても誤判定はゼロ）

SVM では、**以下の平行な2平面間の距離（マージン）を最大化し、その中間の平面を決定境界とする**。
- **正の超平面**：正のラベルに属する点のうち、最も負のラベルの領域に近い点を通る超平面
- **負の超平面**：負のラベルに属する点のうち、最も正のラベルの領域に近い点を通る超平面

※ 説明の便宜上、二値分類における一方のクラスラベルを「正のラベル」、もう一方を「負のラベル」と呼んでいる

学習サンプルのうち、決定境界からの距離が一番近い点を **サポートベクトル** と呼び、SVM において重要な役割を果たす。

> **【NOTE】サポートベクトル**
> - サポートベクトルは正・負の超平面それぞれに存在する
> - 決定境界から等距離に複数の点が存在しうるため、正・負1つずつとは限らない

![Unknown-3](https://user-images.githubusercontent.com/13412823/79214130-3dc08a00-7e85-11ea-842e-8aa2b64a6b5f.png)

図では緑色の矢印の長さがマージンを表す。当然、右側のほうがマージンが大きい。


# 問題設定

入力値（特徴量） $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。


# ハードマージン SVM

訓練サンプルが完全に線形分離可能である場合に使える手法。

## 基本原理

### 目的関数（マージン）の導出

入力値 $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ に対して2値分類を行う決定境界となる平面の方程式を、係数 $$\boldsymbol{w} = (w_1, \cdots, w_m)$$、切片 $$b$$ を用いて

$$
\boldsymbol{w} \cdot \boldsymbol{x} + b = 0
$$

とおく。マージンが最大となるよう、$$\boldsymbol{w}$$, $$b$$ を最適化する。  
この決定境界は、正の超平面と負の超平面の中間に取る。  
与えられた学習サンプルを $$\boldsymbol{x}^{(1)}, \cdots, \boldsymbol{x}^{(n)}$$ とすれば、決定境界から正・負それぞれの超平面までの距離 $$d$$ は

$$
d = \underset{i}{\min} \cfrac{|\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b|}{\|\boldsymbol{w}\|}
= \cfrac{1}{\|\boldsymbol{w}\|} \underset{i}{\min} |\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b|
$$

> **【NOTE】ヘッセの公式**
>
> 点 $$(X_1, \cdots, X_m)$$ と超平面 $$a_1 x_1 + \cdots + a_m x_m + b = 0$$ との距離は下式で求まる。
>
> $$\cfrac{|a_1 X_1 + \cdots + a_m X_m + b|}{\sqrt{a_1^2 + \cdots + a_m^2}}$$

平面の方程式の両辺を定数倍しても同じ平面を表すので、$$\underset{i}{\min} |\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b| = 1$$ となるように調整する。  
この制約により、$$\boldsymbol{w}, b$$ の定数倍の自由度が消えて一意に求められるようになる。  
結果、

$$
d = \cfrac{1}{\|\boldsymbol{w}\|}
$$

最大化したいマージンは $$2d$$ で表されるから、$$\cfrac{2}{\|\boldsymbol{w}\|}$$ の最大化問題を解けば良い。  
実際の計算では、等価な問題である $$\cfrac{1}{2}\|\boldsymbol{w}\|^2$$ の最小化問題を解く（こちらの方が解きやすい）。

### 制約条件

全ての学習サンプルは正・負の超平面よりも遠くに存在し、上述の調整により

$$\underset{i}{\min} |\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b| = 1 \qquad \text{(A)}$$

であるから、制約条件として下式が課される。

$$
| \boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b | \ge 1
\Longleftrightarrow \begin{cases}
\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b \ge 1  & {\rm if}\ y^{(i)} = 1 \\
\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b \le -1 & {\rm if}\ y^{(i)} = -1
\end{cases}
$$

二値分類のクラスラベル $$y^{(i)}$$ は、計算の便宜上 1 または -1 としてある。これにより、制約条件は

$$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1 \qquad \text{(B)}$$

とシンプルに記述できる。  
等号が成立するのは、データサンプル $$\boldsymbol{x}^{(i)}$$ がサポートベクトルであるとき。


### ラグランジュの未定乗数法による問題の書き換え

不等式制約条件下のラグランジュの未定定数法を適用する（**ラグランジュの未定乗数法についてはそちらの技術ノートを参照**）。  
未定乗数 $$\boldsymbol{\lambda} = (\lambda^{(1)}, \cdots, \lambda^{(n)})$$ を用いて、**ラグランジュ関数**

$$
L(\boldsymbol{w}, b, \boldsymbol{\lambda}) \equiv \cfrac{1}{2} \|\boldsymbol{w}\|^2 - \displaystyle \sum_{i=1}^{n} \lambda^{(i)} \{ 1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \}
$$

を定義すると、最適解において

$$
\begin{cases}
\cfrac{\partial L}{\partial b} (\boldsymbol{w}, b, \boldsymbol{\lambda}) = 0 & \qquad & \text{(C-1)} \\
\cfrac{\partial L}{\partial \boldsymbol{w}} (\boldsymbol{w}, b, \boldsymbol{\lambda}) = 0 & \qquad & \text{(C-2)} \\
\lambda^{(i)} = 0 \quad {\rm or} \quad 1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 0 & \qquad & \text{(C-3)} \\
1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \le 0 & \qquad & \text{(C-4)} \\
\lambda^{(i)} \le 0 & \qquad & \text{(C-5)}
\end{cases}
$$

が成り立つ（**KKT 条件**）。1,2行目の偏微分方程式から

$$
\begin{cases}
\displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} = 0 & \qquad & \text{(C-1)'} \\
\boldsymbol{w} + \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)} = 0 & \qquad & \text{(C-2)'}
\end{cases}
$$

これら最適解の条件を $$L(\boldsymbol{w}, b, \boldsymbol{\lambda})$$ の展開式に代入すると、$$\boldsymbol{\lambda}$$ だけの式（**ラグランジュ双対関数**）にできる：

$$
l(\boldsymbol{\lambda}) \equiv L(\boldsymbol{w}(\boldsymbol{\lambda}), b(\boldsymbol{\lambda}), \boldsymbol{\lambda}) =
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \displaystyle \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \lambda^{(i)} \lambda^{(j)} y^{(i)} y^{(j)} \boldsymbol{x}^{(i)} \cdot \boldsymbol{x}^{(j)}
$$

この問題では **強双対性** が成り立つため、$$\frac{1}{2} \|\boldsymbol{w}\|^2$$ の最小化問題の代わりに $$l(\boldsymbol{\lambda})$$ の最大化問題（**双対問題**）を解けば元問題の解が得られる。

双対問題には以下の制約がある。

$$
\begin{cases}
\displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} = 0 & \qquad & \text{(C-1)'} \\
\lambda^{(i)} \le 0& \qquad & \text{(C-5)}
\end{cases}
$$


### 双対問題を解く

勾配降下法（最急降下法）で解く。  
最大化問題なので、勾配ベクトルの向きに $$\lambda$$ を更新すれば良い。

$$
\begin{eqnarray}
\lambda^{(k)} &\longleftarrow& \lambda^{(k)} + \eta \cfrac{\partial l(\boldsymbol{\lambda})}{\partial \lambda^{(k)}} \\
&=& \lambda^{(k)} - \eta \left( 1 + \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(k)} y^{(j)} \boldsymbol{x}^{(k)} \cdot \boldsymbol{x}^{(j)} \right) \\
&=& \lambda^{(k)} - \eta \left( 1 + y^{(k)} \boldsymbol{x}^{(k)} \cdot \left( \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(j)} \boldsymbol{x}^{(j)} \right) \right)
\end{eqnarray}
$$

$$\eta$$ は学習率（$$0 \lt \eta \le 1$$）。

この学習規則でトレーニングすることで、最適な $$\boldsymbol{\lambda}$$ が求まる。


### 決定境界を求める

双対問題の最適解を用いて、決定境界となる平面の方程式を求める。

#### サポートベクトルを求める

後の計算のためにサポートベクトルを求めておく。

$$\lambda^{(i)} \neq 0$$ となる $$i$$ を探す。  
KKT 条件の $$\text{(C-3)}$$ より $$1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 0$$ が成り立つので、$$\boldsymbol{x}^{(i)}$$ がサポートベクトルとなる。


#### $$\boldsymbol{w}$$ を求める

$$\boldsymbol{\lambda}$$ の最適解が求まっているので、$$\text{(C-2)'}$$ により $$\boldsymbol{w}$$ も求まる：

$$
\boldsymbol{w} = - \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)}
$$

ここで $$\boldsymbol{x}^{(i)}$$ がサポートベクトルでない場合は $$1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \neq 0$$ なので、KKT 条件 $$\text{(C-3)}$$ より、$$\lambda^{(i)} = 0$$  
つまり、和を取るのはサポートベクトルだけで良い：

$$
\boldsymbol{w} = - \displaystyle \sum_{\boldsymbol{x}^{(i)} \in V_s} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)}
$$

（$$V_s$$ はサポートベクトルの集合）

一般に、サポートベクトルは学習サンプル全体のうちの極一部であるから、計算量の節約になる。


#### $$b$$ を求める

$$\boldsymbol{x}^{(i)}$$ がサポートベクトルの場合、$$1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 0$$  
したがって、サポートベクトルが1つ求まれば $$b$$ も求まる。  
実際には、誤差を小さくするため全てのサポートベクトルで平均を取るのが良い。

添字 $$i$$ のサポートベクトル $$\boldsymbol{x}^{(i)}$$ から求まる $$b$$ の値は、

$$
b^{(i)} = \cfrac{1}{y^{(i)}} - \boldsymbol{w} \cdot \boldsymbol{x}^{(i)}
= y^{(i)} - \boldsymbol{w} \cdot \boldsymbol{x}^{(i)}
$$

最後に、$$y^{(i)} = 1, -1$$ なので $$\cfrac{1}{y^{(i)}} = y^{(i)}$$ であることを用いた。

$$b^{(i)}$$ の平均を取ると、

$$
b = \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{x}^{(i)} \in V_s} b^{(i)}
= \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{x}^{(i)} \in V_s} (y^{(i)} - \boldsymbol{w} \cdot \boldsymbol{x}^{(i)})
$$

以上により $$\boldsymbol{w}, b$$ が求まり、決定境界となる平面が定まる。


## 実装

```python
class SVM:
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
        self.w = np.zeros(d)
        self.b = 0

    def predict(self, x):
        """
        Parameters
        ----------
        x : 分類したいデータ（d次元ベクトル）
        """
        return 1 if np.dot(self.w, x)+self.b > 0 else -1

    def fit(self, data, labels):
        """
        Parameters
        ----------
        data : 学習データ
        labels : 学習データの教師ラベル
        """
        self.labels = labels
        self.data = data
        self.lambdas = np.zeros(len(data))
        self.K = np.zeros([len(data), len(data)])
        for i in range(len(data)):
            for j in range(i, len(data)):
                k_ = np.dot(self.data[i], self.data[j])
                self.K[i][j] = k_
                self.K[j][i] = k_

        n_pos = np.count_nonzero(labels == 1)
        n_neg = len(labels) - n_pos

        # 双対問題を解く
        for t in range(self.epoch):
            cnt_0_pos, cnt_0_neg = self.__cycle()
            if cnt_0_pos > n_pos-2 and cnt_0_neg > n_pos-2:
                break
        if cnt_0_pos < n_pos*0.9 or cnt_0_neg < n_neg*0.9:
            # 繰り返しが足りない？ 1割以上で lambda != 0
            raise Exception('not converged.')

        # サポートベクトルを抽出
        i_sv = []
        for i in range(len(self.lambdas)):
            if self.lambdas[i] != 0:
                i_sv.append(i)
        # w を計算
        for i in i_sv:
            self.w -= self.lambdas[i] * self.labels[i] * self.data[i]
        # b を計算
        for i in i_sv:
            self.b += self.labels[i] - np.dot(self.w, self.data[i])

    def __cycle(self):
        dl = []
        cnt_0_pos_ = 0
        cnt_0_neg_ = 0
        for i in range(len(self.data)):
            dl_ = 1
            for j in range(len(self.data)):
                dl_ += self.lambdas[j] * self.labels[i] * self.labels[j] * self.K[i][j]
            dl_ *= -self.eta
            dl.append(dl_)
        self.lambdas += np.array(dl)
        for i in range(len(self.lambdas)):
            if self.lambdas[i] > 0:
                # lambda はゼロ以下の必要があるので正になったらゼロにする
                self.lambdas[i] = 0
                if self.labels[i] == 1:
                    cnt_0_pos_ += 1
                else:
                    cnt_0_neg_ += 1
        return cnt_0_pos_, cnt_0_neg_
```

機械的に生成したデータで学習させた結果：

```python
# 学習データ作成
N = 200
c1 = [-2, -1]
c2 = [2, 2]
r1 = 2.0*np.random.rand(N//2)
r2 = 2.5*np.random.rand(N//2)
theta1 = np.random.rand(N//2) * 2 * np.pi
theta2 = np.random.rand(N//2) * 2 * np.pi
data1 = np.array([r1 * np.sin(theta1) + c1[0], r1 * np.cos(theta1) + c1[1]]).T
data2 = np.array([r2 * np.sin(theta2) + c2[0], r2 * np.cos(theta2) + c2[1]]).T
data = np.concatenate([data1, data2])
labels = np.array([1 if i < N//2 else -1 for i in range(N)])

# 学習
svm = SVM(2, max_err=N//10, epoch=1000, eta=0.01)
svm.fit(data, labels)
print('w: {}'.format(svm.w))
print('b: {}'.format(svm.b))
```

```
w: [-1.96480834 -1.067739  ]
b: 0.060744495623293426
```

- 点：学習データ
- 背景：モデルの決定領域

![Unknown-4](https://user-images.githubusercontent.com/13412823/79233520-f4336780-7ea3-11ea-9c82-4f183d27553e.png)
