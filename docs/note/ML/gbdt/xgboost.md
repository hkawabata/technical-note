---
title: XGBoost
---

# XGBoost とは

= eXtreme Gradient Boosting, 勾配ブースティング回帰木

[GBDT (勾配ブースティング決定木)](gbdt.md)の実装の1つ。

# 問題設定

$m$ 次元の特徴量を持つ $n$ 件のデータサンプル

$$
\boldsymbol{x}^{(i)} = \left( x_1^{(i)}, \cdots, x_m^{(i)} \right) \qquad (i = 1, \cdots, n)
$$

と、その正解ラベル $y^{(i)}$ が与えられた時、この分類ラベルの予測値 $\hat{y}^{(i)}$ を与えるモデルを学習する。

# 理論

## 概要

[勾配ブースティング決定木](gbdt.md)の手法により、1個の決定木から始めて、最終的に $T$ 個の決定木を学習する。

- $K_t$：$t$ 番目の決定木が持つ葉の数
- $w_{tk}$：$t$ 番目の決定木の $k$ 番目の葉の重み（$k = 1, \cdots, K_t$）

![XGBoost](https://user-images.githubusercontent.com/13412823/260421209-42af205f-a89c-49f7-a772-8e04f557702a.png)


## 詳細

### 損失関数の定義

$t$ 番目の決定木に $\boldsymbol{x}^{(i)}$ を入力した際の出力（葉の重み）を $f_t \left( \boldsymbol{x}^{(i)} \right)$ とする。  
$r$ ラウンド目まで学習が進んでいるとき（$r$ 個目の決定木まで作り終わっているとき）、モデルの予測値は以下の式で計算される。

$$
\hat{y}^{(i)} = \sum_{t=1}^r f_t \left( \boldsymbol{x}^{(i)} \right)
\tag{1}
$$

学習のための損失関数は、

$$
L = \sum_{i=1}^n l \left( \hat{y}^{(i)}, y^{(i)} \right) + \sum_{t=1}^r \Omega(f_t)
\tag{2}
$$

$(2)$ の第一項は純粋な損失関数であり、残差二乗和

$$
\sum_{i=1}^n l \left( \hat{y}^{(i)}, y^{(i)} \right)
=
\sum_{i=1}^n \cfrac{1}{2} \left\| \hat{y}^{(i)} - y^{(i)} \right\|^2
\tag{3}
$$

など、微分可能な凸関数を用いる。  
※ 係数の1/2は、後の計算で微分すると2が出るのでそれと打ち消すことを考えてかけてある。

> **【NOTE】**
> 
> $(3)$ 式では、ラベル $y$ を one-hot ベクトルとして表現し、その差の絶対値の二乗を取っている。たとえば
> - ラベルが一致する場合
>     - $\hat{y} = y = (0,0,1,0)$
>     - $\Longrightarrow\ l(\hat{y},y) = (0-0)^2 + (0-0)^2 + (1-1)^2 + (0-0)^2 = 0$
> - ラベルが不一致の場合
>     - $\hat{y} = (1,0,0,0),\ y = (0,0,1,0)$
>     - $\Longrightarrow \ l(\hat{y},y) = (1-0)^2 + (0-0)^2 + (0-1)^2 + (0-0)^2 = 2$

$(2)$ の第二項は正則化項であり、$\gamma, \lambda$ を正の定数として以下の式で表される。

$$
\Omega(f_t) = \gamma K_t + \cfrac{\lambda}{2} \sum_{k=1}^{K_t} w_{tk}^2 
\tag{4}
$$

- 第一項：葉の数が多くなりすぎる（= モデルが複雑になりすぎる）ことへのペナルティ
- 第二項：重みの絶対値が大きくなることに対するペナルティ


### 損失関数から定数を除く

学習のラウンド $r$ が進むごとの損失関数の漸化式を考える。  
まず $(1)$ より、

$$
\hat{y}_r^{(i)} = \hat{y}_{r-1}^{(i)}
+
f_r \left( \boldsymbol{x}^{(i)} \right)
\tag{5}
$$

これを用いて $l \left( \hat{y}_r^{(i)}, y^{(i)}_r \right)$ をテイラー展開すると、

$$
\begin{eqnarray}
	l \left( \hat{y}^{(i)}, y^{(i)} \right)
	&=&
	l \left( \hat{y}_{r-1}^{(i)} +
	f_r \left( \boldsymbol{x}^{(i)} \right),
	y^{(i)} \right)
	\\ &\simeq&
	l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)
	+ \cfrac{\partial l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)}{\partial \hat{y}_{r-1}^{(i)}}
	f_r \left( \boldsymbol{x}^{(i)} \right)
	+ \cfrac{1}{2!} \cfrac{\partial^2 l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)}{\partial {\hat{y}_{r-1}^{(i)}}^2 }
	f_r \left( \boldsymbol{x}^{(i)} \right)^2
	\\ &=&
	l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)
	+ g^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)
	+ \cfrac{1}{2} h^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)^2
	\tag{6}
\end{eqnarray}
$$

ただし、

$$
g^{(i)} := \cfrac{\partial l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)}{\partial \hat{y}_{r-1}^{(i)}}
,\qquad
h^{(i)} := \cfrac{\partial^2 l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)}{\partial {\hat{y}_{r-1}^{(i)}}^2 }
\tag{7}
$$

> **【NOTE】疑問点**
> 
> $(1)$ より、ラウンド数 $r$ が大きい時は
> $$
\hat{y}_{r-1}^{(i)} = \sum_{t=1}^{r-1} f_t \left( \boldsymbol{x}^{(i)} \right) \gg f_r \left( \boldsymbol{x}^{(i)} \right)
$$
> とみなし、$f_r$ の高次の項を無視しても良さそう。  
> でも、$r$ が小さいときは $f_r$ が $\hat{y}_{r-1}$ に対して無視できない大きさになるのでは。  
> → ラウンド数が大きくなれば $f_r$ 高次の項を無視できる学習が多数になるので、初期ラウンドにおける誤差の大きさは許容している？
> 
> ただ、$(3)$ のように残差二乗和や残差二乗平均を損失関数 $l$ として用いる場合、3次以上の項の係数である3階以上の微分がゼロになるので気にしなくても良いかも？

ここで、$r$ ラウンド目の学習においては、
- $\hat{y}_{r-1}^{(i)}$ は1ラウンド前の予測ラベル
- $y_{(i)}$ は正解ラベル

であるから、共に定数となる。  
したがって、$l \left( \hat{y}_{r-1}^{(i)}, y^{(i)} \right)$ も定数とみなせる。

次に正則化項 $\Omega$ に関しても、$t \le r-1$ の部分は学習済みであるから、$r$ ラウンド目の学習では定数とみなせる。

以上により、定数部分を除いた損失関数

$$
\tilde{L}_r = \sum_{i=1}^n
\left[
	g^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)
	+
	\cfrac{1}{2} h^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)^2
\right]
+
\gamma K_r + \cfrac{\lambda}{2} \sum_{k=1}^{K_r} w_{rk}^2
\tag{8}
$$

を考えれば良い。


### 重みを最適化する

次に、$(8)$ を最適化したい重み $w_{rk}$ の表式に変換する。  
$I_k$ を、$r$ 番目の決定木の $k$ 番目の葉に属するサンプルのインデックス $i$ の集合とする。  
$f_r \left( \boldsymbol{x}^{(i)} \right)$ は各サンプル $\boldsymbol{x}^{(i)}$ を $r$ 番目の決定木に入力した時の葉の重みであるから、

$$
\sum_{i=1}^n
g^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)
=
\sum_{k=1}^{K_r}
\sum_{i \in I_k}
g^{(i)} w_{rk}
,\qquad
\sum_{i=1}^n
h^{(i)} f_r \left( \boldsymbol{x}^{(i)} \right)
=
\sum_{k=1}^{K_r}
\sum_{i \in I_k}
h^{(i)} w_{rk}^2
\tag{9}
$$

のように和の取り方を変えられる。
これを用いて $(8)$ は

$$
\tilde{L}_r = \sum_{k=1}^{K_r}
\left[
	\sum_{i \in I_k} g^{(i)} w_{rk}
	+ \cfrac{1}{2} \sum_{i \in I_k} h^{(i)} w_{rk}^2
	+ \cfrac{\lambda}{2} w_{rk}^2
\right]
+ \gamma K_r
\tag{10}
$$

$\tilde{L}_r$ が最小値を取る時、任意の $k$ に関して

$$
\cfrac{\partial \tilde{L}_r}{\partial w_{rk}}
=
\sum_{i \in I_k} g^{(i)}
+
\sum_{i \in I_k} h^{(i)} w_{rk}
+
\lambda w_{rk}
= 0
\tag{11}
$$

これを解くと、重み $w_{rk}$ の最適解を得る：

$$
w_{rk} = - \cfrac{\displaystyle \sum_{i \in I_k} g^{(i)}}{\displaystyle \sum_{i \in I_k} h^{(i)} + \lambda}
\tag{12}
$$

重みが最適解となるときの損失関数は、

$$
\begin{eqnarray}
	\tilde{L}_r &=& \sum_{k=1}^{K_r}
	\left[
		\sum_{i \in I_k} g^{(i)}
		\left( - \cfrac{\sum_{i \in I_k} g^{(i)}}{\sum_{i \in I_k} h^{(i)} + \lambda} \right)
		+ \cfrac{1}{2} \left(\sum_{i \in I_k} h^{(i)} 
		+ \lambda \right)
		\left( \cfrac{\sum_{i \in I_k} g^{(i)}}{\sum_{i \in I_k} h^{(i)} + \lambda} \right)^2
	\right]
	+ \gamma K_r
	\\ &=&
	- \cfrac{1}{2} \sum_{k=1}^{K_r}
	\cfrac{ \left(\sum_{i \in I_k} g^{(i)} \right)^2 }{\sum_{i \in I_k} h^{(i)} + \lambda}
	+ \gamma K_r
\end{eqnarray}
\tag{13}
$$

$(13)$ の $\tilde{L}_r$ は **決定木の構造を評価するための関数** として使うことができ、値が小さいほど良い構造となる。

### 決定木の構築

あらゆる構造の決定木を作って $\tilde{L}_r$ の値を調べて最も良いものを選ぶのが理想だが、現実的ではない。  
→ **単一の葉からスタートして、葉を分割するか否か？の評価を繰り返す** 貪欲法により決定木を構築していく。

ある葉を分割するかどうかの判別方法については、
- 分割しない場合の（重み最適化済みの）損失関数 $\tilde{L}_r$
- 分割する場合の（重み最適化済みの）損失関数 $\tilde{L}_{r, \mathrm{split}}$

の差をとり、損失関数が小さい方を採用すれば良い。

- $I$：注目している葉に属するサンプルのインデックス $i$ の集合
- $I_L, I_R$：注目している葉を分割した場合に左側・右側の葉に属するサンプルのインデックス $i$ の集合
	- $I_L \cup I_R = I,\ \ I_L \cap I_R = \varnothing$
- $K$：現在の葉の数

とすれば、

$$
\begin{eqnarray}
	\Delta \tilde{L}_r
	&:=&
	\tilde{L}_r - \tilde{L}_{r, \mathrm{split}}
	\\ &=&
	- \cfrac{1}{2}
	\cfrac{ \left(\sum_{i \in I} g^{(i)} \right)^2 }{\sum_{i \in I} h^{(i)} + \lambda}
	+ \gamma K
	+ \cfrac{1}{2}
	\cfrac{ \left(\sum_{i \in I_L} g^{(i)} \right)^2 }{\sum_{i \in I_L} h^{(i)} + \lambda}
	+ \cfrac{1}{2}
	\cfrac{ \left(\sum_{i \in I_R} g^{(i)} \right)^2 }{\sum_{i \in I_R} h^{(i)} + \lambda}
	- \gamma (K + 1)
	\\ &=&
	\cfrac{1}{2}
	\left[
		\cfrac{ \left(\sum_{i \in I_L} g^{(i)} \right)^2 }{\sum_{i \in I_L} h^{(i)} + \lambda}
		+ \cfrac{ \left(\sum_{i \in I_R} g^{(i)} \right)^2 }{\sum_{i \in I_R} h^{(i)} + \lambda}
		- \cfrac{ \left(\sum_{i \in I} g^{(i)} \right)^2 }{\sum_{i \in I} h^{(i)} + \lambda}
	\right]
	- \gamma
	\tag{14}
\end{eqnarray}
$$

$\Delta \tilde{L}_r$ が正であれば葉を分割し、負であれば分割しない。  
これは **決定木の学習において、$\Delta \tilde{L}_r$ を情報利得とみなす** ことに等しい。

一般的な決定木の学習については[決定木のノート](../decision-tree.md)を参照。


# 実装

## python ライブラリの利用

```bash
pip install xgboost
```

{% gist 532b186b959e8f73ddbc0f914c121921 ~model-library.py %}


## スクラッチ実装

ここでは、純粋な損失関数として残差二乗和 $(3)$ を用いる。

$$
\begin{eqnarray}
    g^{(i)} &=& \cfrac{\partial}{\partial \hat{y}_{r-1}^{(i)}}
    \left( \cfrac{1}{2} \left\| \hat{y}^{(i)}_{r-1} - y^{(i)} \right\|^2 \right)
    = \left( \hat{y}^{(i)}_{r-1} - y^{(i)} \right)
    \\
    h^{(i)} &=& \cfrac{\partial^2}{\partial {\hat{y}_{r-1}^{(i)}}^2 }
    \left( \cfrac{1}{2} \left\| \hat{y}^{(i)}_{r-1} - y^{(i)} \right\|^2 \right)
    = 1
\end{eqnarray}
$$

計算の効率化はあまり考えず、$\Delta \tilde{L}_r$ による決定技の分割部分に重点を置いて実装。

### モデル

{% gist 532b186b959e8f73ddbc0f914c121921 ~model-scratch.py %}

### 学習：手作りデータ

$$
y = \begin{cases}
    0 \qquad \mathrm{if} \ \ x_2 \ge \sin x_1,\ x_1 x_2 \le 0  \\
    1 \qquad \mathrm{if} \ \ x_2 \ge \sin x_1,\ x_1 x_2 \gt 0  \\
    2 \qquad \mathrm{if} \ \ x_2 \lt \sin x_1
\end{cases}
$$

{% gist 532b186b959e8f73ddbc0f914c121921 ~classify-handmade-dataset.py %}

```
number of tree nodes   : [217, 51, 125, 107, 131, 131, 103, 111, 105, 113]
model accurady (train) : [0.9213333333333333, 0.9096666666666666, 0.9203333333333333, 0.9167777777777778, 0.9225555555555556, 0.921, 0.9213333333333333, 0.9204444444444444, 0.922, 0.9222222222222223]
model accurady (test)  : [0.901, 0.89, 0.915, 0.906, 0.916, 0.907, 0.911, 0.904, 0.911, 0.909]
```

| 学習曲線 | 決定境界 |
| -- | -- |
| ![xgboost-handmade](https://user-images.githubusercontent.com/13412823/263500528-722ed4a8-2314-4465-9d88-3f9d0346b817.png) | ![xgboost-decision-boundary](https://user-images.githubusercontent.com/13412823/263500531-54d48730-a44c-4b27-ab3e-9dbe0dcd769f.png) |

- ブーストするまでもなく、ほぼ最初の決定木で高い精度が出ている
    - 特徴量が少なく、決定境界が複雑でないから収束が早い？
- 決定境界はほぼ正確で、ノイズに対する過学習も抑制できている


### 学習：sklearn データセット

{% gist 532b186b959e8f73ddbc0f914c121921 ~classify-sklearn-dataset.py %}

```
number of tree nodes   : [69, 47, 33, 15, 13, 7, 13, 7, 13, 9]
model accurady (train) : [1.0, 0.4112903225806452, 1.0, 0.9435483870967742, 1.0, 0.967741935483871, 1.0, 0.967741935483871, 1.0, 0.9838709677419355]
model accurady (test)  : [0.7407407407407407, 0.37037037037037035, 0.9074074074074074, 0.8148148148148148, 0.9074074074074074, 0.8703703703703703, 0.9074074074074074, 0.8703703703703703, 0.8703703703703703, 0.8888888888888888]
```

| iris | wine |
| -- | -- |
| ![xgboost-iris](https://user-images.githubusercontent.com/13412823/263500532-4a928f6b-98cd-481f-82eb-f9c7c51ae718.png) | ![xgboost-wine](https://user-images.githubusercontent.com/13412823/263500533-45f6fda7-d540-418f-acde-28258daf2f70.png) |

- iris, wine いずれも学習を数サイクル回すと結果が収束
- wine の方は train / test の正解率の差が大きめで過学習の傾向
    - パラメータをチューニングする余地がありそう