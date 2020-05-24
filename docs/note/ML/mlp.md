---
title: 多層パーセプトロン（作成中）
---

# 多層パーセプトロン（MLP）

MLP = Multi-Layer Perceptron

全ての入力（総入力）を受けて1つの出力値を計算・出力する単一ニューロンを多数組み合わせて、複雑な関数のモデリングを可能とする技術。

# 概観

下図に MLP の概観を示す。

![](https://user-images.githubusercontent.com/13412823/82748407-8a7c7680-9ddc-11ea-8478-e9c8be13fd17.png)

- **入力層**：生の入力データに相当する層
- **出力層**：モデルの最終的な出力に相当する層
- **隠れ層**：入力層と出力層の間の層。隠れ層が多く、各層のニューロンが多いほど複雑なモデルを表現できる

第1層以降の $$a_j^{(l)}$$ 1つ1つが単一ニューロンに相当し、1つ前の層の出力+バイアス項を入力として値を1つ出力する。

各ニューロンは、全入力

$$
z_j^{(l)} = \displaystyle \sum_{k} w_{k \rightarrow j}^{(l)} a_k^{(l-1)}
$$

に対し、何らかの活性化関数 $$\phi$$ を適用した活性化ユニット

$$
a_j^{(l)} = \phi(z_j^{(l)})
$$

を出力とする。

MLP の処理の流れは以下の通り。

1. 左の層から右の層へ順次ニューロンの計算を進め、入力 $$\boldsymbol{x}$$ に対して最終出力を計算
2. 最終出力を評価し、誤差を計算
3. 誤差を右の層から左の層へ順次伝播させ、重みを更新
4. 1〜3繰り返し

# 手順

## 1. 順伝播法（フォワードプロパゲーション）による出力計算

1. モデルへの入力値 $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ にバイアス $$x_0 = 1$$ を加え、最初の隠れ層の総入力 $$z_j^{(1)} = \sum_{i=0}^{n} w_{i \rightarrow j}^{(1)} x_i$$ を計算
2. 活性化関数を適用し、活性化ユニット $$a_j^{(1)} = \phi\left(z_j^{(1)}\right)$$ を計算
3. 得られた $$a_j^{(1)}$$ + バイアス $$a_0^{(1)} = 1$$ を入力として次の隠れ層の総入力 $$z_j^{(2)} = \sum_{i=0}^{h} w_{i \rightarrow j}^{(2)} a_i^{(1)}$$ を計算（$$h$$ は1つの隠れ層が含むニューロン数）
4. 2,3を繰り返し、出力層を計算

## 2. 誤差逆伝播法（バックプロパゲーション）による重み更新

### 準備

入力層を除く任意の第 $$l$$ 層を考える。

総出力の第 $$j$$ 成分 $$z_j^{(l)}$$、および活性化ユニット $$a_j^{(l)}$$ は、その層の重みと1つ前の層の活性化ユニットを用いて次のように計算される。

$$
\begin{eqnarray}
z_j^{(l)} &=& \displaystyle \sum_{k} w_{k \rightarrow j}^{(l)} a_k^{(l-1)} &\qquad\qquad& \rm{(0.1)} \\
a_j^{(l)} &=& \phi(z_j^{(l)}) &\qquad\qquad& \rm{(0.2)}
\end{eqnarray}
$$

最小化したいコスト関数（誤差平方和など）を $$J(W)$$ と置くと、第 $$l$$ 層の重みに対するコスト関数の勾配は以下のように計算できる。

$$
\begin{eqnarray}
\cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(l)}}
&=& \displaystyle \sum_{k} \cfrac{\partial J(W)}{\partial z_k^{(l)}} \cfrac{\partial z_k^{(l)}}{\partial w_{i \rightarrow j}^{(l)}} \\
&=& \cfrac{\partial J(W)}{\partial z_j^{(l)}} \cfrac{\partial z_j^{(l)}}{\partial w_{i \rightarrow j}^{(l)}} \\
&=& \cfrac{\partial J(W)}{\partial z_j^{(l)}} a_i^{(l-1)} \\
\end{eqnarray}
$$

誤差

$$
\delta_j^{(l)} \equiv \cfrac{\partial J(W)}{\partial z_j^{(l)}} \qquad\qquad \rm{(0.3)}
$$

を定義すると、

$$
\cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(l)}} = \delta_j^{(l)} a_i^{(l-1)} \qquad\qquad \rm{(0.4)}
$$

### 出力層の重みの勾配

最終層（出力層）を第 $$L$$ 層とする。

$$
z_j^{(L)} = \displaystyle \sum_{k} w_{k \rightarrow j}^{(L)} a_k^{(L-1)}
$$

出力層の重みに関するコスト関数の勾配は

$$
\cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(L)}}
= \delta_j^{(L)} a_i^{(L-1)} = \cfrac{\partial J(W)}{\partial z_j^{(L)}} a_i^{(L-1)} \qquad\qquad \rm{(1.1)}
$$

コスト関数 $$J(W)$$ は出力層の総出力 $$z_j^{(L)}$$ を使って計算するので、$$\cfrac{\partial J(W)}{\partial z_j^{(L)}}$$ の値は計算して求められる。


### 隠れ層の重みの勾配

隠れ層である第 $$l$$ 層（$$l \lt L$$）の重みに関するコスト関数の勾配は、

$$
\cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(l)}}
= \delta_j^{(l)} a_i^{(l-1)}
$$

$$\rm{(0.1), (0.2)}$$ を用いて誤差を計算する：

$$
\begin{eqnarray}
\delta_j^{(l)}
&=& \cfrac{\partial J(W)}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \cfrac{\partial J(W)}{\partial z_k^{(l+1)}} \cfrac{\partial z_k^{(l+1)}}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \delta_k^{(l+1)} \cfrac{\partial z_k^{(l+1)}}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \delta_k^{(l+1)}
\sum_i \cfrac{\partial z_k^{(l+1)}}{\partial a_i^{(l)}} \cfrac{\partial a_i^{(l)}}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \delta_k^{(l+1)}
\sum_i \cfrac{\partial z_k^{(l+1)}}{\partial a_i^{(l)}} \cfrac{\partial \phi\left(z_i^{(l)}\right)}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \delta_k^{(l+1)}
\cfrac{\partial z_k^{(l+1)}}{\partial a_j^{(l)}} \cfrac{\partial \phi\left(z_j^{(l)}\right)}{\partial z_j^{(l)}} \\
&=& \displaystyle \sum_{k} \delta_k^{(l+1)}
w_{j \rightarrow k}^{(l+1)} \cfrac{\partial \phi\left(z_j^{(l)}\right)}{\partial z_j^{(l)}} \\
&=& \cfrac{\partial \phi\left(z_j^{(l)}\right)}{\partial z_j^{(l)}} \left( \left(W^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \right){}_j \\
\end{eqnarray}
$$

全ての成分をまとめてベクトル表記にすると、

$$
\begin{eqnarray}
\boldsymbol{\delta}^{(l)}
&=& \cfrac{\partial J(W)}{\partial \boldsymbol{z}^{(l)}} \\
&=& \cfrac{\partial \phi\left(z_j^{(l)}\right)}{\partial \boldsymbol{z}^{(l)}} \odot \left(W^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \\
\end{eqnarray}
$$

※ $$\odot$$ は成分ごとに積を取る演算（アダマール積）。

したがって、1つ後ろの第 $$l+1$$ 層の誤差が分かれば第 $$l$$ 層の誤差も計算できる。

**前節で最終層（出力層）の誤差を計算済みであるから、再帰的に全ての誤差が計算できる。**


### 重みの更新

以上により、全ての重みに関するコスト関数の勾配が求まったので、

$$
W_{ij}^{(l)} \longleftarrow W_{ij}^{(l)} - \eta \cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(l)}}
$$

により重みを更新する。

$$\eta$$ は学習率。


# 実装

3層パーセプトロンによる多クラス分類器を作ってみる。

- 活性化関数：シグモイド関数 $$\phi(z) = \cfrac{1}{1 + e^{-z}}$$
  - $$\cfrac{\partial \phi(z)}{\partial z} = \cfrac{e^{-z}}{(1 + e^{-z})^2} = \phi(z)\left(1-\phi(z)\right)$$
- ロジスティック回帰と同様に正解ラベルが実現する確率（尤度）、厳密には対数尤度にマイナスをかけたものをコスト関数とする
  - $$J(W) = - \displaystyle \sum_i \sum_j y_j^{(i)} \log{\phi\left(z_j^{(L)(i)}\right)} - \sum_i \sum_j \left(1-y_j^{(i)}\right) \log{\left(1-\phi\left(z_j^{(L)(i)}\right)\right)}$$
    - $$y_j^{(i)}$$: $$i$$ 番目のサンプルの正解ラベルベクトルの第 $$j$$ 成分
    - $$z_j^{(L)(i)}$$: $$i$$ 番目のサンプルの出力層（第 $$L$$ 層）の全入力の第 $$j$$ 成分
  - $$\cfrac{\partial J(W)}{\partial w_{i \rightarrow j}^{(L)}} = - \sum_k \left(y_j^{(k)} - \phi\left(z_j^{(L)(k)}\right)\right) z_i^{(L)(k)}$$

## コード

{% gist 4da6cc3fc14a4ff65d7adef80c86e442 mlp3-classifier.py %}

## 動作確認

{% gist 4da6cc3fc14a4ff65d7adef80c86e442 ~fit-mlp3-classifier.py %}

![MLP3 分類器](https://user-images.githubusercontent.com/13412823/82753237-23bc8480-9dff-11ea-8ad8-64207769349f.png)
