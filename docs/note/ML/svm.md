---
title: サポートベクトルマシン（SVM）
---

# サポートベクトルマシン（SVM）とは

分類問題を解くアルゴリズムの1つ。

分類問題において、一般に決定境界は無数に考えられ、1つに特定できない：

![Unknown](https://user-images.githubusercontent.com/13412823/78503499-daa66780-77a1-11ea-9319-955d0329e69a.png)

（上図において、いずれの決定境界を採用しても誤判定はゼロ）

SVM では、**以下の平行な2平面間の距離（マージン）を最大化する**。
- **正の超平面**：正のラベルに属する点のうち、最も負のラベルの領域に近い点を通る超平面
- **負の超平面**：負のラベルに属する点のうち、最も正のラベルの領域に近い点を通る超平面

※ 説明の便宜上、二値分類における一方のクラスラベルを「正のラベル」、もう一方を「負のラベル」と呼んでいる

![Unknown-1](https://user-images.githubusercontent.com/13412823/78503497-d8dca400-77a1-11ea-805e-e21d929e6be1.png)

図では緑色の矢印の長さがマージンを表す。当然、右側のほうがマージンが大きい。


# 問題設定

入力値（特徴量） $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ に対し、分類ラベル $$y$$ を出力するモデルを作る。


# 仕組み

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
実際の計算では、等価な問題である $$\cfrac{1}{2}\|\boldsymbol{w}\|^2$$ の最小化を解く（こちらの方が解きやすい）。

### 制約条件

全ての学習サンプルは正・負の超平面よりも遠くに存在し、上述の調整により

$$\underset{i}{\min} |\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b| = 1$$

であるから、制約条件として下式が課される。

$$
| \boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b | \ge 1
\Longleftrightarrow \begin{cases}
\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b \ge 1  & {\rm if}\ y^{(i)} = 1 \\
\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b \le -1 & {\rm if}\ y^{(i)} = -1
\end{cases}
$$

2値分類のクラスラベルは計算の便宜上 1, -1 としてあり、これにより制約条件は

$$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1$$

とシンプルに記述できる。


### ラグランジュの未定乗数法による問題の書き換え

不等式制約条件下のラグランジュの未定定数法を適用する（**ラグランジュの未定乗数法についてはそちらの技術ノートを参照**）。  
未定乗数 $$\boldsymbol{\lambda} = (\lambda^{(1)}, \cdots, \lambda^{(n)})$$ を用いて、ラグランジュ関数

$$
L(\boldsymbol{w}, b, \boldsymbol{\lambda}) \equiv \cfrac{1}{2} \|\boldsymbol{w}\|^2 - \displaystyle \sum_{i=1}^{n} \lambda^{(i)} \{ 1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \}
$$

を定義すると、KKT 条件により、最適解において

$$
\begin{cases}
\cfrac{\partial L}{\partial b} (\boldsymbol{w}, b, \boldsymbol{\lambda}) = 0 \\
\cfrac{\partial L}{\partial \boldsymbol{w}} (\boldsymbol{w}, b, \boldsymbol{\lambda}) = 0 \\
\lambda^{(i)} \{ 1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \} = 0 \\
1 - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \le 0 \\
\lambda^{(i)} \le 0
\end{cases}
$$

が成り立つ。1,2行目の偏微分方程式から

$$
\begin{cases}
\displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} = 0 \\
\boldsymbol{w} + \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)} = 0
\end{cases}
$$

これら最適解の条件を $$L(\boldsymbol{w}, b, \boldsymbol{\lambda})$$ の展開式に代入すると、$$\boldsymbol{\lambda}$$ だけの式（ラグランジュ双対関数）にできる：

$$
l(\boldsymbol{\lambda}) \equiv L(\boldsymbol{w}(\boldsymbol{\lambda}), b(\boldsymbol{\lambda}), \boldsymbol{\lambda}) =
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \displaystyle \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \lambda^{(i)} \lambda^{(j)} y^{(i)} y^{(j)} \boldsymbol{x}^{(i)} \cdot \boldsymbol{x}^{(j)}
$$

この問題では強双対性が成り立つため、$$\frac{1}{2} \|\boldsymbol{w}\|^2$$ の最小化問題の代わりに $$l(\boldsymbol{\lambda})$$ の最大化問題（双対問題）を解けば元問題の解が得られる。


## 双対問題を解く

最急降下法で解く。

$$
\lambda^{(i)} \longleftarrow \lambda^{(i)} + \eta \cfrac{\partial l(\boldsymbol{\lambda})}{\partial \lambda^{(i)}}
= \lambda^{(i)} - \eta \left( 1 + \displaystyle \sum_{i=1}^{n} \sum_{j=1}^{n} \lambda^{(j)} y^{(i)} y^{(j)} \boldsymbol{x}^{(i)} \cdot \boldsymbol{x}^{(j)} \right)
$$

（TODO）
