---
title: Word2Vec
---

# 概要

ニューラルネットワークを用いたコーパスの学習により、単語の分散表現を得る手法。


# 理論

以後、学習するコーパスの例として以下の文を考える。

> I say hello to him. You say goodbye to her.


## one-hot ベクトル

各単語を **one-hot ベクトル**（= 成分の1つが1で他は0であるベクトル）で表現する。  
文末のドットも単語として考えると、例文には I, say, hello, to, him, you, goodbye, her, 及びドットの9単語が存在するので、one-hot ベクトルは9次元になる。

| 単語 | インデックス | one-hot ベクトル |
| :-- | :-- | :-- |
| i | 0 | $$(1,0,0,0,0,0,0,0,0)$$ |
| say | 1 | $$(0,1,0,0,0,0,0,0,0)$$ |
| hello | 2 | $$(0,0,1,0,0,0,0,0,0)$$ |
| to | 3 | $$(0,0,0,1,0,0,0,0,0)$$ |
| him | 4 | $$(0,0,0,0,1,0,0,0,0)$$ |
| . | 5 | $$(0,0,0,0,0,1,0,0,0)$$ |
| you | 6 | $$(0,0,0,0,0,0,1,0,0)$$ |
| goodbye | 7 | $$(0,0,0,0,0,0,0,1,0)$$ |
| her | 8 | $$(0,0,0,0,0,0,0,0,1)$$ |


## 擬似タスクと単語の分散表現

例文内の出現順に単語の行ベクトルを並べた行列を考える（単語の区切りを見やすくするため、水平線を入れてある）。

$$
\begin{pmatrix}
    {\rm i} \\
    {\rm say} \\
    {\rm hello} \\
    {\rm to} \\
    {\rm him} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm to} \\
    {\rm her} \\
    {\rm .}
\end{pmatrix}
=
\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}
\tag{1}
$$

この行列から行を取り出して学習データを作成し、
- 周辺のコンテキスト語から単語を予測する（**CBOW モデル**）
- 真ん中の単語から周辺の単語を予測する（**skip-gram モデル**）

といった擬似的なタスク（欲しいのは単語の分散表現であり、これを解くこと自体が目的ではない）をニューラルネットワークで解く。  

このニューラルネットワークは、
- $C$：学習のためのコンテキストデータ（context）。予測したい単語の前後の単語の行ベクトルを並べた行列であり、モデルによって詳細は異なる
- $H$：隠れ層（hidden）の中間行列
- $W^\mathrm{in}$：入力層 → 隠れ層を計算するための重み行列（weight）
- $W^\mathrm{out}$：隠れ層 → 出力層を計算するための重み行列
- $Z$：出力層の行列

とすると、

$$
\begin{eqnarray}
    H &=& C W^\mathrm{in}
    \\
    Z &=& H W^\mathrm{out}
\end{eqnarray}
\tag{2}
$$

の形の式で表される。  

$C$ は単語の行ベクトルを並べた行列なので、$CW^\mathrm{in}$ の計算は、複数の単語の行ベクトルをまとめて重み行列 $W^\mathrm{in}$ に左からかける操作に等しい。  
簡単のため、単語1つだけ、例えば hello：$\boldsymbol{v}_\mathrm{hello} = (0,0,1,0,0,0,0,0,0)$ を $W^\mathrm{in}$ に左からかけることを考えると、

$$
\boldsymbol{v}_\mathrm{hello} W^\mathrm{in} =
(0,0,1,0,0,0,0,0,0)
\begin{pmatrix}
    w_{00} & w_{01} & w_{02} & w_{03} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    \color{red}{w_{20}} & \color{red}{w_{21}} & \color{red}{w_{22}} & \color{red}{w_{23}} \\
    w_{30} & w_{31} & w_{32} & w_{33} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{50} & w_{51} & w_{52} & w_{53} \\
    w_{60} & w_{61} & w_{62} & w_{63} \\
    w_{70} & w_{71} & w_{72} & w_{73} \\
    w_{80} & w_{81} & w_{82} & w_{83}
\end{pmatrix}
=
(w_{20}, w_{21}, w_{22}, w_{23})
\tag{3}
$$

$\boldsymbol{v}_\mathrm{hello}$ は one-hot ベクトルであるから、この操作は、$W^\mathrm{in}$ から行番号2（= 単語 hello のインデックス）の行を抜き出す操作に等しい。  
このように、単語ベクトルを $W^\mathrm{in}$ にかけると、その単語のインデックスを行番号とする行が抜き出される。

→ つまり、**重み $W^\mathrm{in}$ の各行は、その行番号をインデックスとする単語の計算にしか影響しない。したがって、$W^\mathrm{in}$ の各行を、各単語のベクトル表現とみなすことができる。**

これが Word2Vec における単語の分散表現である。


## CBOW モデル

continuous bag-of-words の略。  
周辺語から単語を予測するニューラルネットワークを構成する。

ここでは、予測したい単語の前後1単語ずつをコンテキストとして用いる例について説明する。

![cbow](https://gist.github.com/assets/13412823/031dfc7a-49e6-4692-8828-babf91168930)

### 入力と正解ラベル

入力1 = 当てたい単語の1語前のコンテキスト（backward context）：

$$
C^{\rm b} =
\begin{pmatrix}
    {\rm i} \\
    {\rm say} \\
    {\rm hello} \\
    {\rm to} \\
    {\rm him} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm to}
\end{pmatrix}
=
\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\tag{4}
$$

入力2 = 当てたい単語の1語後のコンテキスト（forward context）：

$$
C^{\rm f} =
\begin{pmatrix}
    {\rm hello} \\
    {\rm to} \\
    {\rm him} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm to} \\
    {\rm her} \\
    {\rm .}
\end{pmatrix}
=
\begin{pmatrix}
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}
\tag{5}
$$

正解ラベル = 当てたい単語（Answer）。  
前後1単語ずつをコンテキストに用いるので、コーパスの最初と最後の単語を除く（前後一単語が存在しないため）：

$$
A =
\begin{pmatrix}
    {\rm say} \\
    {\rm hello} \\
    {\rm to} \\
    {\rm him} \\
    {\rm .} \\
    {\rm you} \\
    {\rm say} \\
    {\rm goodbye} \\
    {\rm to} \\
    {\rm her}
\end{pmatrix}
=
\begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
\tag{6}
$$

> **【NOTE】**
> 
> 先頭行を除くのではなく、文頭を示す特殊単語を追加したりするのも良さそう：
> 
> > (文頭) I say hello to him . (文頭) You say hello to her.


### 学習：順伝播

入力から隠れ層の値 $H$ を計算する（前後の単語で平均を取る）：

$$
H = \cfrac{1}{2} \left( C^{\rm b} W^{\rm in} + C^{\rm f} W^{\rm in} \right)
\tag{7}
$$

次に、隠れ層から出力層の値 $Z$ を計算する：

$$
Z = H W^{\rm out}
\tag{8}
$$

ここで、$W^{\rm in}, W^{\rm out}$ は重み行列であり、学習前に乱数で初期化する。  
one-hot ベクトルの次元（= 文中のユニークな単語数）を $n$、隠れ層の次元を $h$ とすると、$W^{\rm in}$ は $n \times h$ 行列、$W^{\rm out}$ は $h \times n$ 行列。

最後に、SoftMax で文中 $i$ 番目の単語がインデックス $j$ の単語に一致する確率に変換する。

$$
S_{ij} = \cfrac{\exp{Z_{ij}}}{\sum_k \exp{Z_{ik}}}
\tag{9}
$$

これを用いてコスト関数 $J$（誤差平方和など）を計算し、勾配を求めて誤差逆伝播の処理を行う。

> **【NOTE】**
> 
> $C^\mathrm{b}, C^\mathrm{f}$ にかける重み $W^\mathrm{in}$ は共通で良いのか？  
> 前と後で単語の出現率の傾向は違うはず。予測対象の単語の前後で別の重み $W^\mathrm{in,f}, W^\mathrm{in,b}$ を計算し、それぞれから単語に対応する成分を抽出・結合して分散表現とするのではダメ？


### 学習：逆伝播

モデルの各パラメータによるコスト関数 $J$ の微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial J}{\partial W_{ij}^{\rm in}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial W_{ij}^{\rm in}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{1}{2} \left( C_{ki}^{\rm b} + C_{ki}^{\rm f} \right) \delta_{jl}
    \\ &=& \displaystyle \sum_{k} \cfrac{\partial J}{\partial H_{kj}} \cfrac{1}{2} \left( C_{ki}^{\rm b} + C_{ki}^{\rm f} \right)
    &=& \cfrac{1}{2} \left( \left( C^{\rm b} + C^{\rm f} \right)^T \cfrac{\partial J}{\partial H} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial C_{ij}^{\rm b, f}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial C_{ij}^{\rm b, f}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{1}{2} W_{jl}^{\rm in} \delta_{ik}
    \\ &=& \displaystyle \sum_{l} \cfrac{\partial J}{\partial H_{il}} \cfrac{1}{2} W_{jl}^{\rm in}
    &=& \cfrac{1}{2} \left( \cfrac{\partial J}{\partial H} W^{ {\rm in}\ T} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial W_{ij}^{\rm out}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} \cfrac{\partial Z_{kl}}{\partial W_{ij}^{\rm out}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} H_{ki} \delta_{jl}
    \\ &=& \displaystyle \sum_{k} \cfrac{\partial J}{\partial Z_{kj}} H_{ki}
    &=& \left( H^T \cfrac{\partial J}{\partial Z} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial H_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial Z_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} W_{jl}^{\rm out} \delta_{ik}
    \\ &=& \displaystyle \sum_{l} \cfrac{\partial J}{\partial Z_{il}} W_{jl}^{\rm out}
    &=& \left( \cfrac{\partial J}{\partial Z} W^{ {\rm out}\ T} \right)_{ij}
\end{eqnarray}
\tag{10}
$$

これらを用いて各パラメータを更新する。


### 単語の分散表現

学習により得られた $W^{\rm in}$ の各行が、行番号 = 単語インデックスに対応する単語の分散表現になっている。


## skip-gram モデル

真ん中の単語から周辺の単語を予測するニューラルネットワークを構成する。

ここでは、コンテキストとなる単語の前後1単語ずつを予測する例について説明する。

![skip-gram](https://gist.github.com/assets/13412823/3fef27c2-e4e4-4290-a107-c01ca2382274)


### 入力と正解ラベル

入力 = コンテキストとなる単語（Context）：

$$
C =
\begin{pmatrix}
    {\rm i} \\ \hline
    {\rm say} \\ {\rm say} \\ \hline
    {\rm hello} \\ {\rm hello} \\ \hline
    {\rm to} \\ {\rm to} \\ \hline
    {\rm him} \\ {\rm him} \\ \hline
    {\rm .} \\ {\rm .} \\ \hline
    {\rm you} \\ {\rm you} \\ \hline
    {\rm say} \\ {\rm say} \\ \hline
    {\rm goodbye} \\ {\rm goodbye} \\ \hline
    {\rm to} \\ {\rm to} \\ \hline
    {\rm her} \\ {\rm her} \\ \hline
    {\rm .}
\end{pmatrix}
=
\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}
$$

先頭の i と末尾のドット以外は、文中の前後2つの単語が正解データとなるため、2つずつ $C$ に含めてある。

正解ラベル $A$ = 当てたい周辺語（Answer）は、$C$ の前後1単語ずつを予測するので、

$$
A =
\begin{pmatrix}
    {\rm say} \\ \hline
    {\rm i} \\
    {\rm hello} \\ \hline
    {\rm say} \\
    {\rm to} \\ \hline
    {\rm hello} \\
    {\rm him} \\ \hline
    {\rm to} \\
    {\rm .} \\ \hline
    {\rm him} \\
    {\rm you} \\ \hline
    {\rm .} \\
    {\rm say} \\ \hline
    {\rm you} \\
    {\rm goodbye} \\ \hline
    {\rm say} \\
    {\rm to} \\ \hline
    {\rm goodbye} \\
    {\rm her} \\ \hline
    {\rm to} \\
    {\rm .} \\ \hline
    {\rm her}
\end{pmatrix}
=
\begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ \hline
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\ \hline
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$


### 学習：順伝播

入力から隠れ層の行列 $H$ を計算式が $(7)$ ではなく

$$
H = C W^{\rm in}
$$

になるだけで、その他は CBOW と同様。
- 隠れ層から出力層を計算する式は CBOW と同じ $(8)$
- 出力層から $(9)$ 式で「文中 $i$ 番目の単語がインデックス $j$ の単語に一致する確率」に変換するのも同じ
- 確率からコスト関数 $J$ を計算して誤差を逆伝播させるのも同じ

$$
\begin{eqnarray}
    H &=& C W^\mathrm{in}
    \\
    Z &=& H W^\mathrm{out}
    \\
    S_{ij} &=& \cfrac{\exp{Z_{ij}}}{\sum_k \exp{Z_{ik}}}
\end{eqnarray}
$$


### 学習：逆伝播

モデルの各パラメータによるコスト関数 $J$ の微分を計算すると、

$$
\begin{eqnarray}
    \cfrac{\partial J}{\partial W_{ij}^{\rm in}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial W_{ij}^{\rm in}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} C_{ki} \delta_{jl}
    \\ &=& \displaystyle \sum_{k} \cfrac{\partial J}{\partial H_{kj}} C_{ki}
    &=& \left( C^T \cfrac{\partial J}{\partial H} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial C_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial C_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} W_{jl}^{\rm in} \delta_{ik}
    \\ &=& \displaystyle \sum_{l} \cfrac{\partial J}{\partial H_{il}} W_{jl}^{\rm in}
    &=& \left( \cfrac{\partial J}{\partial H} W^{ {\rm in}\ T} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial W_{ij}^{\rm out}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} \cfrac{\partial Z_{kl}}{\partial W_{ij}^{\rm out}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} H_{ki} \delta_{jl}
    \\ &=& \displaystyle \sum_{k} \cfrac{\partial J}{\partial Z_{kj}} H_{ki}
    &=& \left( H^T \cfrac{\partial J}{\partial Z} \right)_{ij}
    \\
    \cfrac{\partial J}{\partial H_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial H_{kl}} \cfrac{\partial H_{kl}}{\partial Z_{ij}}
    &=& \displaystyle \sum_{k} \sum_{l} \cfrac{\partial J}{\partial Z_{kl}} W_{jl}^{\rm out} \delta_{ik}
    \\ &=& \displaystyle \sum_{l} \cfrac{\partial J}{\partial Z_{il}} W_{jl}^{\rm out}
    &=& \left( \cfrac{\partial J}{\partial Z} W^{ {\rm out}\ T} \right)_{ij}
\end{eqnarray}
$$

これらを用いて各パラメータを更新する。


## CBOW / skip-gram 学習の高速化

### 改善1：入力層 → 隠れ層

単語数が多くなるとベクトル / 行列の次元が増えるので、$C W^{\rm in}$ の計算時間が膨大になる。

ここで $C$ の各行は one-hot ベクトルなので、**成分の1つが1で他成分が0**。  
→ つまり、$CW^{\rm in}$ の計算は、$C$ の成分が1である列番号に対応する $W^{\rm in}$ の行を抜き出すことに等しい：

$$
\begin{eqnarray}
C W^{\rm in} &=&
\begin{pmatrix}
    0 & 0 & \color{blue}{1} & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & \color{red}{1} & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
    w_{00} & w_{01} & w_{02} & w_{03} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{50} & w_{51} & w_{52} & w_{53} \\
    w_{60} & w_{61} & w_{62} & w_{63} \\
    w_{70} & w_{71} & w_{72} & w_{73} \\
    w_{80} & w_{81} & w_{82} & w_{83}
\end{pmatrix}
\\
&=&
\begin{pmatrix}
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
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
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    w_{50} & w_{51} & w_{52} & w_{53}
\end{pmatrix}
\\
&=&
\begin{pmatrix}
    \color{blue}{w_{20}} & \color{blue}{w_{21}} & \color{blue}{w_{22}} & \color{blue}{w_{23}} \\
    \color{red}{w_{30}} & \color{red}{w_{31}} & \color{red}{w_{32}} & \color{red}{w_{33}} \\
    w_{40} & w_{41} & w_{42} & w_{43} \\
    w_{50} & w_{51} & w_{52} & w_{53} \\
    w_{60} & w_{61} & w_{62} & w_{63} \\
    w_{10} & w_{11} & w_{12} & w_{13} \\
    w_{70} & w_{71} & w_{72} & w_{73} \\
    w_{30} & w_{31} & w_{32} & w_{33} \\
    w_{80} & w_{81} & w_{82} & w_{83} \\
    w_{50} & w_{51} & w_{52} & w_{53}
\end{pmatrix}
\end{eqnarray}
$$

よって、**行列の積を計算する代わりに、単語インデックスに対応する $W^{\rm in}$ の行を抜き出せば良い**。


### 改善2：隠れ層 → 出力層

単語数が多くなるとベクトル / 行列の次元が増えるので、出力層 $Z = H W^{\rm out}$ やその確率値（SoftMax）の計算時間が膨大になる。

これを回避するため、**「各単語への所属確率を計算する多値分類問題」を「当てたい単語か否かの2値分類問題」に近似する**。

具体的には、出力 $Z$ について SoftMax を取る代わりに各成分 $Z_{ij}$ にシグモイド関数を適用し、「$i$ 番目のデータサンプルが単語 $j$ を指す確率」として解釈して学習を行う。

$$
P_{ij} = \cfrac{1}{1 + \exp \left(-Z_{ij}\right)}
$$

$P_{ij}$ のうち、必要な成分だけを計算することで学習を効率化する。


最終出力 $P$ の1行目の成分 $P_{ij}$ の正解ラベルは以下の通り。

$$
P_{ij}^{\rm correct} = \begin{cases}
1 & \mbox{if } j=y_i \\
0 & \mbox{if } j \neq y_i
\end{cases}
$$

ここで、$y_i$ は $i$ 番目のサンプルの正解単語のインデックス。

コスト $J_{ij}$ として、対数尤度

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

$J_{ij}$ は $Z_{ij}$ のみの関数であるから、

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

以後、上の例の2行目（行番号は0からスタートするので $i=1$）のデータサンプル
- 正解単語 hello (index = 2)
- 1つ前のコンテキスト語 say (index = 1)
- 1つ後のコンテキスト語 to (index = 3)

を例として考える。

正解単語のインデックスが2であるから、$Z_{12}, P_{12}$ を計算する：

$$
Z_{12} = \displaystyle \sum_{k} H_{1k} W_{k2}^{\rm out}
$$

$$
P_{12} = \cfrac{1}{1 + \exp \left(-Z_{12}\right)}
$$

コスト関数は $P_{12}^{\rm correct} = 1$ より

$$
J_{12} = - \log P_{12}
$$



#### 負例の学習：Negative Sampling

全ての負例を学習するとコストが大きいので、不正解の単語をいくつかピックアップして学習を行う（= **Negative Sampling**）。

ここでは
- say (index = 1)
- goodbye (index = 7)

の2つを選ぶことにする。

コスト関数は $$P_{11}^{\rm correct}, P_{17}^{\rm correct} = 0$$ より

$$
J_{11} = - \log \left( 1 - P_{11} \right)
$$

$$
J_{17} = - \log \left( 1 - P_{17} \right)
$$

#### 誤差逆伝播

コスト関数

$$J = J_{12} + J_{11} + J_{17}$$

に対して前述の誤差逆伝播の式を適用する。



# 実装

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

→ hello と goodbye, I と you が近いところにいる。
