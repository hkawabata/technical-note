---
title: パーセプトロン
---

# パーセプトロンとは

分類問題を解くアルゴリズムの1つ。

- 二値分類
- 単純パーセプトロンでは線形分離可能な問題しか解けない

# 基本原理

## 問題設定

入力値（特徴量） $$x_1, \cdots, x_m$$ に対し、分類ラベル $$y$$ を出力するモデルを作りたい。

各入力値に重み $$w_1, \cdots, w_m$$ をかけて和を取った

$$z = \displaystyle \sum_{j=1}^{m} w_j x_j$$

を **総入力** と呼び、$$z$$ が閾値 $$\theta$$ 以上か否かで二値分類を行う。

$$
y = \phi(z) =
\begin{cases}
1  & (z \ge \theta ) \\
-1 & (z \lt \theta )
\end{cases}
$$

活性化関数 $$\phi(z)$$ はステップ関数となる。

本問題は、最適な重み $$w_1, \cdots, w_m$$ 及び閾値 $$\theta$$ を求める問題に帰着される。

ここで、総入力 $$z$$ にゼロ番目の入力・重みとして $$x_0 = 1, w_0 = - \theta$$ を与えることで、閾値 $$\theta$$ を重みの1つとして扱える：

$$z = - \theta + w_1 x_1 + \cdots + w_m x_m = \displaystyle \sum_{j=0}^{m} w_j x_j$$

$$
y = \phi(z) =
\begin{cases}
1  & (z \ge 0 ) \\
-1 & (z \lt 0 )
\end{cases}
$$


## 学習規則

1. 重みをゼロ or 値の小さい乱数で初期化
2. $$i$$ 番目の学習サンプル $$\boldsymbol{x}^{(i)} = ( x_0^{(i)}, \cdots, x_m^{(i)} )$$ ごとに以下の手順を実行
    1. 現時点のモデルを使い、$$\boldsymbol{x}^{(i)}$$ に対するラベル $$\hat y^{\ (i)}$$ を計算
    2. 計算した $$\hat y^{\ (i)}$$ が正解分類ラベル $$y^{(i)}$$ と異なっていたら、計算結果を正解へ近づける方向へ重みを更新
3. 収束するまで2を繰り返す

$$\hat y^{\ (i)} = x_0^{(i)} w_0 + \cdots + x_m^{(i)} w_m$$

$$w_j \leftarrow w_j + \eta (y^{(i)} - \hat y^{\ (i)}) x_j^{(i)}$$

ここで $$\eta (0 \lt \eta \le 1)$$ は学習率であり、1度に重みを更新する大きさを表す。

### 学習率の大きさと収束

- $$\eta$$ が大きすぎると永遠に収束しないので、十分に小さく取る必要がある
- $$\eta$$ が小さいほど重みの更新がゆっくりなので、学習が収束するまでに必要な繰り返し回数が大きくなる

### 線形分離性

- 学習用データセットが完全に線形分離できる場合、パーセプトロンは収束する
- 学習用データセットが完全には線形分離できない場合、以下のような収束条件を定めないと永遠に収束しない
  - 最大何回まで繰り返すか（エポック）
  - 判定誤りを何件まで許容するか


# 実装

```python
import numpy as np

class Perceptron:
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
        return 1 if np.dot(x, self.weight[:-1]) + self.weight[-1] > 0 else -1
    
    def fit(self, data, labels):
        """
        Parameters
        ----------
        data : 学習データの配列
        labels : 正解ラベルの配列
        """
        self.labels = labels
        self.data = np.append(data, np.array([[1.0] for _ in range(len(data))]), axis=1)
        for t in range(self.epoch):
            cnt_err = self.__cycle()
            if cnt_err <= self.max_err:
                break
        print('Converged in {} cycles.'.format(t))
        
    def __cycle(self):
        ids = np.array(range(len(self.data)))
        np.random.shuffle(ids)
        cnt_err = 0
        for i in ids:
            label_eval = 1 if np.dot(self.data[i], self.weight) > 0 else -1
            if label_eval != self.labels[i]:
                cnt_err += 1
                for j in range(self.d + 1):
                    self.weight[j] = self.weight[j] + self.eta * (self.labels[i] - label_eval) * self.data[i][j]
        return cnt_err
```

```python
data = np.array([
    [0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
    [1, 0], [2, 1], [3, 2], [4, 3], [5, 4]
])
labels = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1]

perceptron = Perceptron(2, max_err=2)
perceptron.fit(data, labels)

print(perceptron.predict([1, 3]))
# 1
print(perceptron.predict([7, 2]))
# -1
```

機械的に生成したデータで学習させた結果：

- 点：学習データ
- 背景：モデルの決定領域

![Unknown](https://user-images.githubusercontent.com/13412823/78036657-88320900-73a5-11ea-9c9d-c92c04350967.png)

![Unknown-1](https://user-images.githubusercontent.com/13412823/78036647-86684580-73a5-11ea-8466-a564e0d07e87.png)

