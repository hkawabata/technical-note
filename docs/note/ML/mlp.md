---
title: 多層パーセプトロン（作成中）
---

# 多層パーセプトロン（MLP）

MLP = Multi-Layer Perceptron

全ての入力（総入力）を受けて1つの出力値を計算・出力する単一ニューロンを多数組み合わせて、複雑な関数のモデリングを可能とする技術。

# 手順

## 1. 順伝播法（フォワードプロパゲーション）による出力計算

![](https://user-images.githubusercontent.com/13412823/82748407-8a7c7680-9ddc-11ea-8478-e9c8be13fd17.png)

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
