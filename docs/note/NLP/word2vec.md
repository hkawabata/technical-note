---
title: Word2Vec
---

# Word2Vec

ニューラルネットワークを用いたコーパスの学習により、単語の分散表現を得る手法。

## one-hot ベクトル

> I say hello. You say goodbye.

| 単語 | インデックス | one-hot ベクトル |
| :-- | :-- | :-- |
| i | 0 | $$(1,0,0,0,0,0)$$ |
| say | 1 | $$(0,1,0,0,0,0)$$ |
| hello | 2 | $$(0,0,1,0,0,0)$$ |
| . | 3 | $$(0,0,0,1,0,0)$$ |
| you | 4 | $$(0,0,0,0,1,0)$$ |
| goodbye | 5 | $$(0,0,0,0,0,1)$$ |

全部で単語は6種類 → 6次元のベクトル

$$
Words =
\begin{pmatrix}
    {\rm i} \\
    {\rm say} \\
    {\rm hello} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm .}
\end{pmatrix}
=
\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 1 & 0 & 0
\end{pmatrix}
$$

これを学習データとして、「周辺のコンテキスト語から単語を当てる」問題を解く。
ここでは以後、当てたい単語の前後1単語ずつをコンテキストとして用いる。

## CBOW モデル

continuous bag-of-words の略。

### 学習の入力と正解ラベル

正解ラベル = 当てたい単語：

$$
A =
\begin{pmatrix}
    {\rm say} \\
    {\rm hello} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye}
\end{pmatrix}
=
\begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

入力1 = 当てたい単語の1語前のコンテキスト：

$$
C^{\rm b} =
\begin{pmatrix}
    {\rm i} \\
    {\rm say} \\
    {\rm hello} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say}
\end{pmatrix}
=
\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0
\end{pmatrix}
$$

入力2 = 当てたい単語の1語後のコンテキスト：

$$
C^{\rm f} =
\begin{pmatrix}
    {\rm hello} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm .}
\end{pmatrix}
=
\begin{pmatrix}
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 1 & 0 & 0
\end{pmatrix}
$$

隠れ層の値：

$$
H = \cfrac{1}{2} \left( C^{\rm b} W^{\rm in} + C^{\rm f} W^{\rm in} \right)
$$

出力層の値：

$$
Z = H W^{\rm out}
$$

SoftMax で所属確率に変換する：

$$
S_{ij} = \cfrac{\exp{Z_{ij}}}{\sum_k \exp{Z_{ik}}}
$$

### 逆伝播

$$
\cfrac{\partial J}{\partial W_{ij}^{\rm in}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial W_{ij}^{\rm in}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{1}{2} \left( C_{ki}^{\rm b} + C_{ki}^{\rm f} \right) \delta_{jl}
= \displaystyle \sum_{k} \cfrac{\partial J}{\partial H_{kj}} \cfrac{1}{2} \left( C_{ki}^{\rm b} + C_{ki}^{\rm f} \right)
= \cfrac{1}{2} \left( \left( C^{\rm b} + C^{\rm f} \right)^T \cfrac{\partial J}{\partial H} \right)_{ij}
$$

$$
\cfrac{\partial J}{\partial C_{ij}^{\rm b, f}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial C_{ij}^{\rm b, f}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{1}{2} W_{jl}^{\rm in} \delta_{ik}
= \displaystyle \sum_{l} \cfrac{\partial J}{\partial H_{il}} \cfrac{1}{2} W_{jl}^{\rm in}
= \cfrac{1}{2} \left( \cfrac{\partial J}{\partial H} W^{ {\rm in}\ T} \right)_{ij}
$$

$$
\cfrac{\partial J}{\partial W_{ij}^{\rm out}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} \cfrac{\partial Z_{kl}}{\partial W_{ij}^{\rm out}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} H_{ki} \delta_{jl}
= \displaystyle \sum_{k} \cfrac{\partial J}{\partial Z_{kj}} H_{ki}
= \left( H^T \cfrac{\partial J}{\partial Z} \right)_{ij}
$$


$$
\cfrac{\partial J}{\partial H_{ij}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial Z_{ij}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} W_{jl}^{\rm out} \delta_{ik}
= \displaystyle \sum_{l} \cfrac{\partial J}{\partial Z_{il}} W_{jl}^{\rm out}
= \left( \cfrac{\partial J}{\partial Z} W^{ {\rm out}\ T} \right)_{ij}
$$

### 単語の分散表現

学習により得られた $$W^{\rm in}$$ の各行が、行番号 = 単語インデックスに対応する単語の分散表現になっている。


## 高速 CBOW モデル

### 改善1：入力層 → 隠れ層

単語数が多くなるとベクトル / 行列の次元が増えるので、$$C^{\rm b} W^{\rm in}, C^{\rm f} W^{\rm in}$$ の計算時間が膨大になる。

ここで $$C^{\rm b}, C^{\rm f}$$ の各行は one-hot ベクトルなので、**成分の1つが1で他成分が0**。  
→ つまり、$$C^{\rm b} W^{\rm in}, C^{\rm f} W^{\rm in}$$ の計算は、$$C^{\rm b}, C^{\rm f}$$ の成分が1である列番号に対応する $$W^{\rm in}$$ の行を抜き出すことに等しい。

$$
\begin{eqnarray}
C^{\rm f} W^{\rm in} &=&
\begin{pmatrix} \hline
    0 & 0 & \color{blue}{1} & 0 & 0 & 0 \\ \hline \hline
    0 & 0 & 0 & \color{red}{1} & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 1 & 0 & 0
\end{pmatrix}
\left(
\begin{array}{|c||c||c||c|}
    w_{00} & w_{01} & w_{02} & w_{03} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{50} & w_{51} & w_{52} & w_{53}
\end{array}
\right)
\\
&=&
\begin{pmatrix}
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
\end{pmatrix}
+
\begin{pmatrix}
    0 & 0 & 0 & 0 \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
\end{pmatrix}
+
\cdots
+
\begin{pmatrix}
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    w_{30} & w_{31} & w_{32} & w_{33}
\end{pmatrix}
\\
&=&
\begin{pmatrix}
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    w_{50} & w_{51} & w_{52} & w_{53} \\
    w_{30} & w_{31} & w_{32} & w_{33}
\end{pmatrix}
\end{eqnarray}
$$

よって、**行列の積を計算する代わりに、単語インデックスに対応する $$W^{\rm in}$$ の行を抜き出せば良い**。


### 改善2：隠れ層 → 出力層

単語数が多くなるとベクトル / 行列の次元が増えるので、出力層 $$Z = H W^{\rm out}$$ やその確率値（SoftMax）の計算時間が膨大になる。

これを回避するため、**「各単語への所属確率を計算する多値分類問題」を「当てたい単語か否かの2値分類問題」に近似する**。

具体的には、出力 $$Z$$ について SoftMax を取る代わりに各成分 $$Z_{ij}$$ にシグモイド関数を適用し、「$$i$$ 番目のデータサンプルが 単語 $$j$$ を指す確率」として解釈して学習を行う。

$$
P_{ij} = \cfrac{1}{1 + \exp \left(-Z_{ij}\right)}
$$

$$P_{ij}$$ のうち、必要な成分だけを計算することで学習を効率化する。


最終出力 $$P$$ の1行目の成分 $$P_{ij}$$ の正解ラベルは以下の通り。

$$
P_{ij}^{\rm correct} = \begin{cases}
1 & \mbox{if } j=y_i \\
0 & \mbox{if } j \neq y_i
\end{cases}
$$

ここで、$$y_i$$ は $$i$$ 番目のサンプルの正解単語のインデックス。

コスト $$J_{ij}$$ として、対数尤度

$$
J_{ij} = - \left( P_{ij}^{\rm correct} \log P_{ij} + \left( 1 - P_{ij}^{\rm correct} \right) \log \left( 1 - P_{ij} \right) \right)
$$

を用いる。

逆伝播の式は

$$
\cfrac{\partial J_{ij}}{\partial P_{ij}} = - \cfrac{P_{ij}^{\rm correct}}{P_{ij}} + \cfrac{1 - P_{ij}^{\rm correct}}{1 - P_{ij}}
$$

$$
\cfrac{\partial J_{ij}}{\partial Z_{ij}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J_{ij}}{\partial P_{kl}} \cfrac{\partial P_{kl}}{\partial Z_{ij}}
= \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J_{ij}}{\partial P_{kl}} P_{kl} \left( 1 - P_{kl} \right) \delta_{ik} \delta_{jl}
= \cfrac{\partial J_{ij}}{\partial P_{ij}} P_{ij} \left( 1 - P_{ij} \right)
$$

$$J_{ij}$$ は $$Z_{ij}$$ のみの関数であるから、

$$
\cfrac{\partial J_{ij}}{\partial H_{kl}}
= \cfrac{\partial J_{ij}}{\partial Z_{ij}} \cfrac{\partial Z_{ij}}{\partial H_{kl}}
= \begin{cases}
\cfrac{\partial J_{ij}}{\partial Z_{ij}} W_{lj}^{\rm out} & \mbox{if } k = i \\
\\
0 & \mbox{if } k \neq i
\end{cases}
$$

$$
\cfrac{\partial J_{ij}}{\partial W_{kl}^{\rm out}}
= \cfrac{\partial J_{ij}}{\partial Z_{ij}} \cfrac{\partial Z_{ij}}{\partial W_{kl}^{\rm out}}
= \begin{cases}
\cfrac{\partial J_{ij}}{\partial Z_{ij}} H_{ik} & \mbox{if } l = j \\
\\
0 & \mbox{if } l \neq j
\end{cases}
$$

#### 正例の学習

以後、上の例の2行目（行番号は0からスタートするので $$i=1$$）のデータサンプル
- 正解単語 hello (index = 2)
- 1つ前のコンテキスト語 say (index = 1)
- 1つ後のコンテキスト語 . (index = 3)

を例として考える。

正解単語のインデックスが2であるから、$$Z_{12}, P_{12}$$ を計算する：

$$
Z_{12} = \displaystyle \sum_{k} H_{1k} W_{k2}^{\rm out}
$$

$$
P_{12} = \cfrac{1}{1 + \exp \left(-Z_{12}\right)}
$$

コスト関数は $$P_{12}^{\rm correct} = 1$$ より

$$
J_{12} = - \log P_{12}
$$



#### 負例の学習：Negative Sampling

全ての負例を学習するとコストが大きいので、不正解の単語をいくつかピックアップして学習を行う（= **Negative Sampling**）。

ここでは
- say (index = 1)
- goodbye (index = 5)

の2つを選ぶことにする。

コスト関数は $$P_{11}^{\rm correct}, P_{15}^{\rm correct} = 0$$ より

$$
J_{11} = - \log \left( 1 - P_{11} \right)
$$

$$
J_{15} = - \log \left( 1 - P_{15} \right)
$$

#### 誤差逆伝播

コスト関数

$$J = J_{14} + J_{11} + J_{15}$$

に対して前述の誤差逆伝播の式を適用する。


## 実装

```python
import numpy as np
from datetime import datetime

class Embedding:
    """
    入力 → 隠れ層
    """
    
    def __init__(self, W):
        self.W = W
        self.dW = None
    
    def forward(self, contexts, is_training=False):
        """
        contexts : 周辺語の ID 行列（データ数 x 周辺語数）
        """
        batch_size, context_size = contexts.shape
        out = np.zeros((batch_size, self.W.shape[1]))
        for i in range(context_size):
            idx = contexts[:, i]
            out += self.W[idx]
        out /= context_size
        if is_training:
            self.cache = contexts
        return out
    
    def backward(self, dout):
        contexts = self.cache
        self.cache = None
        context_size = contexts.shape[1]
        self.dW = np.zeros_like(self.W)
        for i in range(context_size):
            idx = contexts[:, i]
            for j, word_id in enumerate(idx):
                self.dW[word_id] += dout[j]
            self.dW *= context_size
            
        return None


class NegativeSampler:
    def __init__(self, corpus, power=0.75, sample_size=3):
        """
        corpus      : 単語 ID の配列からなるコーパス # one-hot ベクトルから成るコーパス
        power       : ネガティブサンプリングにおいて、出現頻度の小さい単語を優遇（1未満の正数、ゼロに近いほど優遇）
        sample_size : 負例を何件サンプリングするか
        """
        self.sample_size = sample_size
        
        u, counts = np.unique(corpus, return_counts=True)
        
        p = np.zeros_like(u)
        for i in range(len(u)):
            p[u[i]] = counts[i]
        # 出現頻度の小さい単語を少し出やすくする
        p = np.power(p, power)
        p = p / np.sum(p)
        self.p = p
    
    def get_neg_samples(self, target):
        """
        target : 正例（正解ラベル）の配列
        """
        return np.array([self.__get_neg_samples_for_1record(t) for t in target])
    
    def __get_neg_samples_for_1record(self, target):
        """
        target : 正例（正解ラベル）1件
        """
        p = self.p.copy()
        p[target] = 0
        p = p / np.sum(p)
        return np.random.choice(range(len(p)), size=self.sample_size, replace=False, p=p)


class NegativeSamplingLoss:
    def __init__(self, W, corpus, power=0.75, neg_sample_size=3):
        """
        W : 重み
        corpus : 単語 ID の配列からなるコーパス # one-hot ベクトルから成るコーパス
        power : ネガティブサンプリングにおいて、出現頻度の小さい単語を優遇（1未満の正数、ゼロに近いほど優遇）
        neg_sample_size : 負例を何件サンプリングするか
        """
        self.W = W
        self.neg_sample_size = neg_sample_size
        self.neg_sampler = NegativeSampler(corpus, power, neg_sample_size)
        self.loss_layers = [SigmoidLoss() for _ in range(neg_sample_size+1)]
        
    def forward(self, h, word_ids_answer, is_training=False):
        """
        h : 隠れ層のデータ
        word_ids_answer : 正解単語の id リスト
        """
        batch_size = h.shape[0]
        
        loss = 0
        
        # 正例のフォワード
        out = np.sum(h*self.W[:, word_ids_answer].T, axis=1)
        p_correct = np.full(batch_size, 1.0)
        loss += self.loss_layers[0].forward(out, p_correct)
        # 負例のフォワード
        ## バッチサイズ x 負例サンプルサイズの単語 ID 行列
        neg_samples = self.neg_sampler.get_neg_samples(word_ids_answer)
        for i in range(self.neg_sample_size):
            out = np.sum(h*self.W[:, neg_samples[:, i]].T, axis=1)
            p_correct = np.zeros(batch_size)
            loss += self.loss_layers[i+1].forward(out, p_correct)
        
        if is_training:
            self.cache = (word_ids_answer, neg_samples, h)
        
        return loss
        
    def backward(self):
        word_ids_answer, neg_samples, h = self.cache
        self.cache = None
        batch_size = len(word_ids_answer)
        
        self.dW = np.zeros_like(self.W)
        
        # 正例のバックワード
        dout = self.loss_layers[0].backward()
        target_W = self.W[:, word_ids_answer]
        dh = (dout * target_W).T
        dtarget_W = dout * h.T
        for i in range(batch_size):
            self.dW[:, word_ids_answer[i]] += dtarget_W[:, i]
        # 負例のバックワード
        for j in range(self.neg_sample_size):
            dout = self.loss_layers[j+1].backward()
            neg_word_ids = neg_samples[:, j]
            target_W = self.W[:, neg_word_ids]
            dh += (dout * target_W).T
            dtarget_W = dout * h.T
            for i in range(batch_size):
                self.dW[:, neg_word_ids[i]] += dtarget_W[:, i]

        return dh
            

class SigmoidLoss:
    eps = 1e-10
    
    def __init__(self):
        self.cache = None
    
    def forward(self, out_actual, p_expected):
        p_actual = 1.0 / (1.0 + np.exp(-out_actual))
        # ゼロ除算 (divide by zero encountered in log) 回避
        p_actual = np.where(self.eps<p_actual, p_actual, self.eps)
        p_actual = np.where(p_actual<1.0-self.eps, p_actual, 1.0-self.eps)
        
        loss = - (p_expected * np.log(p_actual) + (1.0-p_expected) * np.log(1.0-p_actual))
        self.cache = (p_actual, p_expected)
        return loss.sum()
    
    def backward(self, dout=1.0):
        p_actual, p_expected = self.cache
        batch_size = len(p_expected)
        dx = (p_actual - p_expected) * dout / batch_size
        return dx


class CBOW:
    test_rate = 0.3
    
    def __init__(self, epochs=10, eta=0.01, batch_size=10,
                 hidden_size=5, context_size_backward=1, context_size_forward=1):
        self.hidden_size = hidden_size # 50-500くらいが良いらしい
        self.epochs = epochs
        self.eta = eta
        self.batch_size = batch_size
        self.context_size_backward = context_size_backward # 2-10 くらいが良いらしい
        self.context_size_forward = context_size_forward # 2-10 くらいが良いらしい
        
        self.id2word = None  # ID -> 単語の変換
        self.word2id = None  # 単語 -> ID の変換
        self.layer1 = None   # 入力層 -> 隠れ層
        self.layer2 = None   # 隠れ層 -> 出力層 -> コスト計算
        self.loss = []       # コスト関数の評価値を保存する配列
    
    def fit(self, words):
        # 前処理
        corpus = self.__generate_corpus(words)
        contexts, correct_labels = self.__generate_contexts_and_correct_labels(corpus)
        self.__init_layers(corpus)
        x_train = contexts
        y_train = correct_labels
        
        n_train = len(x_train) // self.batch_size
        time_last_log = datetime.now()
        for e in range(1, self.epochs+1):
            for t in range(1, n_train+1):
                idx_batch = np.random.choice(range(len(x_train)), size=self.batch_size, replace=False)
            
                # 順伝搬 (forward propagation)
                h = self.layer1.forward(x_train[idx_batch], is_training=True)
                loss = self.layer2.forward(h, y_train[idx_batch], is_training=True)
                self.loss.append(loss)
            
                # 逆伝搬 (back propagation)
                dh = self.layer2.backward()
                self.layer1.backward(dh)
            
                # 重みアップデート
                self.layer1.W -= self.eta * self.layer1.dW
                self.layer2.W -= self.eta * self.layer2.dW
            
                time_now = datetime.now()
                if (time_now - time_last_log).seconds > 300:
                    print(time_now.strftime('%Y/%m/%d %H:%M:%S'), 'epoch {}/{} train {}/{} loss = {}'.format(e, self.epochs, t, n_train, loss))
                    time_last_log = time_now
    
    def __generate_corpus(self, words):
        """
        単語 ID コーパス生成
        """
        self.id2word = np.unique(words)
        self.word2id = {}
        for i in range(len(self.id2word)):
            self.word2id[self.id2word[i]] = i
        corpus = np.array([self.word2id[w] for w in words])
        return corpus
    
    def __generate_contexts_and_correct_labels(self, corpus):
        """
        コンテキスト / 正解ラベル生成
        """
        size_l, size_r = self.context_size_backward, self.context_size_forward
        size_total = size_l + size_r
        contexts = []
        correct_labels = corpus[size_l:-size_r]
        for i in range(size_l, len(corpus)-size_r):
            for j in reversed(range(1, size_l+1)):
                contexts.append(corpus[i-j])
            for j in range(1, size_r+1):
                contexts.append(corpus[i+j])
        contexts = np.reshape(contexts, (len(correct_labels), size_total))

        return contexts, correct_labels
    
    def __init_layers(self, corpus):
        """
        レイヤ初期化
        """
        n_uniq_word = len(self.id2word)
        W_in = 0.01 * np.random.randn(n_uniq_word, self.hidden_size)
        W_out = 0.01 * np.random.randn(self.hidden_size, n_uniq_word)
        self.layer1 = Embedding(W_in)
        self.layer2 = NegativeSamplingLoss(W_out, corpus, power=0.75, neg_sample_size=5)
```

動作確認：

```python
words = [
    'I', 'say', 'hello', '.',
    'You', 'say', 'goodbye', '.',
    'I', 'say', 'goodbye', '.',
    'You', 'say', 'hello', '.'
]

cbow = CBOW(epochs=100, eta=0.1, hidden_size=2, batch_size=3)
cbow.fit(words)

%matplotlib inline
from matplotlib import pyplot as plt
plt.plot(range(len(cbow.loss)), cbow.loss)
plt.grid()
plt.show()
plt.scatter(cbow.layer1.W[:, 0], cbow.layer1.W[:, 1])
for i in range(len(cbow.id2word)):
    plt.annotate(cbow.id2word[i], (cbow.layer1.W[i][0], cbow.layer1.W[i][1]))
plt.show()

for i in range(len(cbow.id2word)):
    print('{}\t{}'.format(cbow.id2word[i], cbow.layer1.W[i]))
```

![学習曲線](https://user-images.githubusercontent.com/13412823/118568181-3d926c80-b7b2-11eb-82e5-f07df9192169.png)

![単語の分散表現](https://user-images.githubusercontent.com/13412823/118568182-3f5c3000-b7b2-11eb-8de2-43773c721295.png)

