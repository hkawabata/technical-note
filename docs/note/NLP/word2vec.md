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
\begin{pmatrix}
    0 & 0 & \color{blue}{1} & 0 & 0 & 0 \\
    0 & 0 & 0 & \color{red}{1} & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 1 & 0 & 0
\end{pmatrix}
\left(
\begin{pmatrix}
    w_{00} & w_{01} & w_{02} & w_{03} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{50} & w_{51} & w_{52} & w_{53}
\end{pmatrix}
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

{% gist 643afd8e457683417df22416c0a7a1e6 word2vec.py %}

動作確認：

{% gist 643afd8e457683417df22416c0a7a1e6 ~fit-plot.py %}

![学習曲線](https://user-images.githubusercontent.com/13412823/118573959-7a646080-b7be-11eb-964e-18911c0f9fb7.png)

![単語の分散表現](https://user-images.githubusercontent.com/13412823/118573965-7c2e2400-b7be-11eb-8303-85e1a7467435.png)

```
.	[-2.11021881 -0.8555051 ]
I	[-2.09877201  3.68470591]
You	[-2.21292083  3.86925015]
goodbye	[-1.29194497  1.94738739]
hello	[-1.40466781  2.15441167]
say	[-3.4324403  -1.48782928]
```

