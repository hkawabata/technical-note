---
title: Factorization Machine
---

cf.
- https://qiita.com/s_katagiri/items/d630685dd2fe2627ecd3
- https://blog.recruit.co.jp/rco/47/

# 概要

**Factorization Machine (FM)** は、ユーザー属性とアイテム評価、さらにはその他の属性情報も組み合わせ推薦アルゴリズムで、[Matrix Factorization](matrix-factorization.md) の発展系。

2010年に Rendle が発表。

# 理論

基本的な協調フィルタリングや Matrix Factorization では、ユーザ $u_i$ がアイテム $v_j$ を評価した値 $r_{i,j}$ を並べた以下のような評価値テーブルを使っていた。

|  | $v_1$ | $v_2$ | $v_3$ | $v_4$ |
| :--- | ---- | ---- | ---- | ---- |
| $u_1$ | 0.5 |  | 0.2 | 0.8 |
| $u_2$ |  | 0.2 |  | 0.6 |
| $u_3$ |  |  | 0.3 |  |

対して Factorization Machine では、評価値 $r_{i,j}$ それぞれを1行に対応させ、ユーザ $u_i$ やアイテム $v_j$、その他の特徴量 $a_l$ を列に持つ以下のようなテーブルを考える：

|  | $u_1$ | $u_2$ | $u_3$ | $v_1$ | $v_2$ | $v_3$ | $v_4$ | $a_1$ | $a_2$ | $\cdots$ |
| :--- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $\boldsymbol{x}^{(1)}(r_{1,1}=0.5)$ | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 3.1 | 0.3 |  |
| $\boldsymbol{x}^{(2)}(r_{1,3}=0.2)$ | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2.5 | -0.2 |  |
| $\boldsymbol{x}^{(3)}(r_{1,4}=0.8)$ | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.3 | 0.9 |  |
| $\boldsymbol{x}^{(4)}(r_{2,2}=0.2)$ | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 3.0 | 0.8 |  |
| $\boldsymbol{x}^{(5)}(r_{2,4}=0.6)$ | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0.9 | -0.4 |  |
| $\boldsymbol{x}^{(6)}(r_{3,3}=0.3)$ | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1.7 | 0.3 |  |

$u_i, v_j$ の列は、値が1であれば、そのユーザやアイテムに関する評価値であることを示す。  
特徴量 $a_l$ は何でも良い：
- ユーザ属性：年齢 / 性別 / 自身で登録してもらった好きなジャンル
- アイテム属性：ジャンル / 価格 / 口コミ数
- ユーザ-アイテム間の関係：そのユーザがそのアイテムを閲覧 / 購入 / お気に入り登録

$u_i, v_j, a_l$ 全てを含めた特徴量の数（上の行列の列数）を $n$ として、$l$ 番目の評価値 $r^{(l)}$ の推定値 $\hat{r}^{(l)}$ を以下の式で計算する。

$$
\hat{r}^{(l)} = w_0 + \sum_{i=1}^n w_i x_i^{(l)} + \sum_{i=1}^n \sum_{j=i+1}^n (\boldsymbol{f}_i \cdot \boldsymbol{f}_j) x_i^{(l)} x_j^{(l)}
\tag{1}
$$

ただし、

$$
w_0 \in \mathbb{R},\quad
\boldsymbol{w} \in \mathbb{R}^n,\quad
\boldsymbol{f}_1, \cdots, \boldsymbol{f}_n \in \mathbb{R}^k
$$

は学習により最適化するモデル変数であり、
- $w_0$：定数項
- $\boldsymbol{w}$：各特徴量ごとの独立した重み
- $\boldsymbol{f}_i$：各特徴量ごとの重みで、特徴量間の相互作用を考えるため内積を取って使う
    - $k$ は $\boldsymbol{f}_i$ の次元を決めるハイパーパラメータで、$k \lt n$

$(1)$ を愚直に計算すると相互作用の項が $O(kn^2)$ の計算量になるが、式変形により

$$
\begin{eqnarray}
    \sum_{i=1}^n \sum_{j=i+1}^n (\boldsymbol{f}_i \cdot \boldsymbol{f}_j) x_i^{(l)} x_j^{(l)}
    &=&
    \cfrac{1}{2} \sum_{i=1}^n \sum_{j=1}^n (\boldsymbol{f}_i \cdot \boldsymbol{f}_j) x_i^{(l)} x_j^{(l)} -
    \cfrac{1}{2} \sum_{i=1}^n (\boldsymbol{f}_i \cdot \boldsymbol{f}_i) (x_i^{(l)})^2
    \\ &=&
    \cfrac{1}{2} \sum_{i=1}^n \sum_{j=1}^n \sum_{p=1}^k f_{ip} f_{jp} x_i^{(l)} x_j^{(l)} -
    \cfrac{1}{2} \sum_{i=1}^n \sum_{p=1}^k f_{ip}^2 (x_i^{(l)})^2
    \\ &=&
    \cfrac{1}{2} \sum_{p=1}^k
    \left( \sum_{i=1}^n f_{ip} x_i^{(l)} \right)
    \left( \sum_{j=1}^n f_{jp} x_j^{(l)} \right) -
    \cfrac{1}{2} \sum_{i=1}^n \sum_{p=1}^k \left(f_{ip} x_i^{(l)}\right)^2
    \\ &=&
    \cfrac{1}{2} \sum_{p=1}^k
    \left( \sum_{i=1}^n f_{ip} x_i^{(l)} \right)^2 -
    \cfrac{1}{2} \sum_{i=1}^n \sum_{p=1}^k \left(f_{ip} x_i^{(l)}\right)^2
    \\ &=&
    \cfrac{1}{2} \sum_{p=1}^k \left\{
        \left( \sum_{i=1}^n f_{ip} x_i^{(l)} \right)^2 -
        \sum_{i=1}^n \left(f_{ip} x_i^{(l)}\right)^2
    \right\}
    \tag{2}
\end{eqnarray}
$$

とすれば、計算量は $O(kn)$ に抑えられる。

損失関数 $L$ は予測値と実際の評価値の誤差平方和：

$$
L :=
\sum_{l=1}^m \left\{
    \cfrac{1}{2} \left(\hat{r}^{(l)} - r^{(l)} \right)^2
\right\} +
\cfrac{\lambda}{2} \left(
    w_0^2 +
    \sum_{i=1}^n w_i^2 +
    \sum_{i=1}^n \vert \boldsymbol{f}_i \vert^2
\right)
\tag{3}
$$

第二項は正則化項で、$\lambda$ はそのためのハイパーパラメータ。勾配計算の係数調整のため $1/2$ をかけてある。

$$
\begin{eqnarray}
    \cfrac{\partial L}{\partial w_0}
    &=&
    \sum_{l=1}^m \left\{
        \cfrac{\partial \hat{r}^{(l)}}{\partial w_0}
        \left(\hat{r}^{(l)} - r^{(l)} \right)
    \right\}
    + \lambda w_0
    \\ &=&
    \sum_{l=1}^m \left(\hat{r}^{(l)} - r^{(l)} \right)
    + \lambda w_0
    \tag{4}
    \\
    \\
    \cfrac{\partial L}{\partial w_i}
    &=&
    \sum_{l=1}^m \left\{
        \cfrac{\partial \hat{r}^{(l)}}{\partial w_i}
        \left(\hat{r}^{(l)} - r^{(l)} \right)
    \right\}
    + \lambda w_i
    \\ &=&
    \sum_{l=1}^m x_i^{(l)} \left(\hat{r}^{(l)} - r^{(l)} \right)
    + \lambda w_i
    \tag{5}
    \\
    \\
    \cfrac{\partial L}{\partial f_{ij}}
    &=&
    \sum_{l=1}^m \left\{
        \cfrac{\partial \hat{r}^{(l)}}{\partial f_{ij}}
        \left(\hat{r}^{(l)} - r^{(l)} \right)
    \right\}
    + \lambda f_{ij}
    \\ &=&
    \sum_{l=1}^m \left( x_i^{(l)} \sum_{p=1}^n x_p^{(l)} f_{pj} - (x_i^{(l)})^2 f_{ij} \right) \left(\hat{r}^{(l)} - r^{(l)} \right)
    + \lambda f_{ij}
    \tag{6}
\end{eqnarray}
$$

より、勾配降下法などを用いてパラメータを最適化する。


# Factorization Machine の強み

$n$ 個の特徴量間の相互作用の重みとしては、$n\times n$ 要素のパラメータ行列 $W_{ij}$ を考えるのが素直：

$$
\hat{r}^{(l)} = w_0 + \sum_{i=1}^n w_i x_i^{(l)} + \sum_{i=1}^n \sum_{j=i+1}^n W_{ij} x_i^{(l)} x_j^{(l)}
$$

Factorization Machine では、この $W_{ij}$を特徴量ごとの $k < n$ 次元ベクトル $\boldsymbol{f}_1,\cdots,\boldsymbol{f}_n$ の内積 $\boldsymbol{f}_i \cdot \boldsymbol{f}_j$ に置き換えた形になっている。

## 強み1：計算量の節約

- $W_{ij}$ の変数は $n^2$ 個
- $\boldsymbol{f}_1,\cdots,\boldsymbol{f}_n$ の変数は全部で $nk$ 個

なので、$k \ll n$ と取ればパラメータ数をかなり小さく抑えることができる。


## 強み2：疎なデータへの耐性

ユーザやアイテムは one-hot ベクトルとして表現されている。これに限らず、カテゴリデータを one-hot 化した特徴量を使いたいことも多い。  
こういった場合、特徴量ベクトル $\boldsymbol{x}$ が疎になるため、$x_i,x_j$ いずれかが0になる（つまり、相互作用項にあたる $x_i x_j$ が0になる）確率が高く、まともに $W_{ij}$ を学習できない。  
特に、one-hot 化されているユーザ同士、アイテム同士、カテゴリ同士では必ず $x_i x_j = 0$ となってしまう（いずれか1つの成分を除いて0となるため）。

一方で特徴量ベクトルの内積 $\boldsymbol{f}_i \cdot \boldsymbol{f}_j$ を用いる場合は、常に $x_i x_j = 0$ であっても、どこかで $x_i x_k \ne 0$ となる $k(\ne j)$ があれば、$x_i$ に対応するベクトル $\boldsymbol{f}_i$ を学習できる。  
同じことは $\boldsymbol{f}_j$ にも言えるので、他の特徴量を用いて学習した $\boldsymbol{f}_i, \boldsymbol{f}_j$ を用いて、間接的に $x_i, x_j$ の相互作用を求めることができる。


# 実装（途中）

性能が出ないのでバグやチューニング不足があるかも。

```python
import numpy as np
from matplotlib import pyplot as plt
import time


class FactorizationMachine:
    def __init__(self):
        pass
    
    def fit(self, X, Y, k, lamb=0.1, eta=1e-4, T=10000, eps=1e-6, r_test=0):
        self.n, self.d = X.shape
        self.k, self.lamb, self.eta = k, lamb, eta
        self.n_test = int(self.n * r_test)
        self.n_learn = self.n - self.n_test
        idx = np.array(range(self.n))
        np.random.shuffle(idx)
        self.idx_learn, self.idx_test = idx[:self.n_learn], idx[self.n_learn:]
        self.X, self.X_test = X[self.idx_learn], X[self.idx_test]
        self.Y, self.Y_test = Y[self.idx_learn], Y[self.idx_test]
        self.w0 = np.random.rand()
        self.w = np.random.rand(self.d)
        self.F = np.random.rand(self.d, k)
        #self.w0 = np.random.normal(0, 1)
        #self.w = np.random.normal(0, 1, self.d)
        #self.F = np.random.normal(0, 1, (self.d, k))
        self.__tune_initial_params_scale()
        self.loss = []
        self.loss_test = []
        self.loss_regular = []
        self.__set_baseline()
        self.__update_Y_pred()
        self.__update_Err()
        self.__update_loss()
        time_start = time.time()
        for t in range(T):
            if t % (T//100) == 0:
                progress = t / (T//100)
                print('{}/{} ({}%) : {} s, loss = {}'.format(t, T, progress, int(time.time()-time_start), self.loss[-1]))
            self.__update()
            if np.abs(self.loss[-1]-self.loss[-2]) < eps:
                break
        self.loss = np.array(self.loss)
        self.loss_test = np.array(self.loss_test)
        self.loss_regular = np.array(self.loss_regular)
    
    def __tune_initial_params_scale(self):
        tmp = self.X.dot(self.F)
        y_pred_tmp = self.w0 + (self.w * self.X).sum(axis=1) + tmp.sum(axis=1)**2 - (tmp**2).sum(axis=1)
        scale = np.abs(self.Y).mean() / np.abs(y_pred_tmp).mean()
        self.w0 *= scale
        self.w *= scale
        self.F *= np.sqrt(scale)
    
    def __set_baseline(self):
        y_base = self.Y.mean()
        Err_base = y_base - self.Y
        self.loss_base = (Err_base**2).mean()
    
    def __update(self):
        #grad_w0 = self.Err.sum() + self.lamb * self.w0
        #grad_w = (self.Err * self.X.T).sum(axis=1) + self.lamb * self.w
        grad_w0 = self.Err.mean() + self.lamb * self.w0
        grad_w = (self.Err * self.X.T).mean(axis=1) + self.lamb * self.w
        xf = self.X.dot(self.F)
        xxf = np.full((self.n_learn, self.d, self.k), np.nan)
        for i in range(len(xf)):
            xxf[i] = np.matrix(self.X[i]).T.dot(np.matrix(xf[i]))
        #grad_F = xxf.sum(axis=0) + self.lamb * self.F
        grad_F = xxf.mean(axis=0) + self.lamb * self.F
        self.w0 -= self.eta * grad_w0
        self.w -= self.eta * grad_w
        self.F -= self.eta * grad_F
        self.__update_Y_pred()
        self.__update_Err()
        self.__update_loss()
    
    def __update_Y_pred(self):
        tmp = self.X.dot(self.F)
        self.Y_pred = self.w0 + (self.w * self.X).sum(axis=1) + tmp.sum(axis=1)**2 - (tmp**2).sum(axis=1)
        tmp = self.X_test.dot(self.F)
        self.Y_pred_test = self.w0 + (self.w * self.X_test).sum(axis=1) + tmp.sum(axis=1)**2 - (tmp**2).sum(axis=1)
    
    def __update_Err(self):
        self.Err = self.Y_pred - self.Y
        self.Err_test = self.Y_pred_test - self.Y_test
    
    def __update_loss(self):
        l_regular = self.lamb * (self.w0**2 + (self.w**2).sum() + (self.F**2).sum())
        self.loss_regular.append(l_regular)
        #l = (self.Err**2).sum() + l_regular
        l = (self.Err**2).mean() + l_regular
        self.loss.append(l)
        #l_test = (self.Err_test**2).sum() + l_regular
        l_test = (self.Err_test**2).mean() + l_regular
        self.loss_test.append(l_test)
    
    def draw_loss(self):
        plt.plot(self.loss, color='tab:blue', label='total (learn)')
        plt.plot(self.loss-self.loss_regular, color='tab:blue', linestyle='dashed', label='error (learn)')
        plt.plot([self.loss_base]*len(self.loss), color='tab:green', linestyle='dashed', label='error (baseline)')
        if self.n_test > 0:
            plt.plot(self.loss_test, color='tab:orange', label='total (test)')
            plt.plot(self.loss_test-self.loss_regular, color='tab:orange', linestyle='dashed', label='error (learn)')
        plt.plot(self.loss_regular, color='black', linestyle='dashed', label='regularization')
        plt.xlabel('Epoch', fontsize=12)
        plt.ylabel('Loss', fontsize=12)
        plt.grid()
        plt.legend()
        plt.show()


model_fm = FactorizationMachine()
#model.fit(X_fm, Y_fm, k=10, lamb=0.1, eta=1e-4, T=100, eps=1e-6, r_test=0.5)
model_fm.fit(X_fm, y_fm, k=20, lamb=0.1, eta=1e-1, T=100, eps=1e-2, r_test=0.5)

model_fm = FactorizationMachine()
model_fm.fit(X_fm, y_fm, k=20, lamb=0.01, eta=1e0, T=1000, eps=1e-3, r_test=0.5)
model_fm.draw_loss()


model_fm = FactorizationMachine()
model_fm.fit(X_fm, y_fm, k=32, lamb=0.01, eta=1e0, T=1000, eps=5e-4, r_test=0.1)
model_fm.draw_loss()
```
