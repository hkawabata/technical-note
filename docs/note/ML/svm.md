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

## 原理

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

を定義すると、最適解 $$\boldsymbol{w}$$ において

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

これら最適解の条件を $$L(\boldsymbol{w}, b, \boldsymbol{\lambda})$$ の式に代入すると、$$\boldsymbol{\lambda}$$ だけの式（**ラグランジュ双対関数**） $$l(\boldsymbol{\lambda})$$ が導かれる：

$$
\begin{eqnarray}
L(\boldsymbol{w}, b, \boldsymbol{\lambda})
&=&
\cfrac{1}{2} \|\boldsymbol{w}\|^2
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
+ \displaystyle \boldsymbol{w} \cdot \left( \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)} \right)
+ \displaystyle b \sum_{i=1}^{n} \lambda^{(i)} y^{(i)}
\\
&=&
\cfrac{1}{2} \|\boldsymbol{w}\|^2
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \|\boldsymbol{w}\|^2 + 0
\\
&=&
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \cfrac{1}{2} \|\boldsymbol{w}\|^2
\\
&=&
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \displaystyle \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \lambda^{(i)} \lambda^{(j)} y^{(i)} y^{(j)} \boldsymbol{x}^{(i)} \cdot \boldsymbol{x}^{(j)}
\\
&\equiv& l(\boldsymbol{\lambda})
\end{eqnarray}
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

広く使われるのは SMO という手法だが、ここでは勾配降下法（最急降下法）を使う。  
最大化問題なので、勾配ベクトルの向きに $$\lambda$$ を更新すれば良い。

$$
\begin{eqnarray}
\lambda^{(k)} &\longleftarrow& \lambda^{(k)} + \eta \cfrac{\partial l(\boldsymbol{\lambda})}{\partial \lambda^{(k)}} \\
&=& \lambda^{(k)} - \eta \left( 1 + \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(k)} y^{(j)} \boldsymbol{x}^{(k)} \cdot \boldsymbol{x}^{(j)} \right)
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

### コード

{% gist 3c7d782482f20a5e43aec642ac977a2a svm-hard.py %}

### 動作確認

{% gist 3c7d782482f20a5e43aec642ac977a2a ~fit-hard.py %}

```
w: [ 1.54177416 -0.81642494]
b: 0.10083610288436107
```

- 点：学習データ
- 背景：モデルの決定領域

![HardMarginSVM](https://user-images.githubusercontent.com/13412823/79533295-7d1fee00-80b2-11ea-8b3b-932316b8ceb5.png)


# ソフトマージン SVM

ハードマージン SVM は、学習データが完全に線形分離可能な場合しか収束しない。  
また、線形分離可能な場合であっても、少数の外れ値の影響を強く受ける。  
実際にはしばしば学習データにノイズが混ざるので、それを許容できるようにしたい。

## 原理

### 目的関数の導出

ハードマージン SVM の制約

$$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1 \qquad \text{(B)}$$

に対して、正値の **スラック変数** $$\boldsymbol{\xi} = (\xi^{(1)}, \cdots, \xi^{(n)})$$ を導入して制約を緩和する：

$$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1 - \xi^{(i)}$$

データサンプル $$\boldsymbol{x}^{(i)}$$ が誤分類される時、データは決定境界 $$\boldsymbol{w} \cdot \boldsymbol{x} + b = 0$$ を超えて反対側にあるので、

$$
\xi^{(i)} \gt 1
$$

したがって、ある自然数 $$K$$ に対して

$$\displaystyle \sum_{i=1}^{n} \xi^{(i)} \le K$$

であるならば、誤分類は $$K$$ 個以下であることが保証できる。  
→ **$$\xi^{(i)}$$ の和は誤分類の程度を表す**

誤分類が多くなることをペナルティとして表現するため、最小化すべき $$\cfrac{1}{2}\|\boldsymbol{w}\|^2$$ にコスト関数として $$\xi^{(i)}$$ の和を加えた

$$
\cfrac{1}{2}\|\boldsymbol{w}\|^2 + C \displaystyle \sum_{i=1}^{n} \xi^{(i)}
$$

を目的関数として最小化する。

ここで $$C \gt 0$$ は調整用のハイパーパラメータであり、
- $$C$$ が大きい = 誤分類のコストが高い = 誤分類に不寛容
- $$C$$ が小さい = 誤分類のコストが低い = 誤分類に寛容

ということになる。

![](https://user-images.githubusercontent.com/13412823/79444749-8f4c4e80-8016-11ea-9e72-6e0696128250.png)


### 制約条件

最小化に際してかかる制約は、

$$
\begin{cases}
y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1 - \xi^{(i)} \\
\xi^{(i)} \ge 0
\end{cases}
$$

### ラグランジュの未定乗数法による問題の書き換え

基本的にハードマージン SVM と同じ流れ。

ラグランジュ関数：

$$
L(\boldsymbol{w}, b, \boldsymbol{\xi}, \boldsymbol{\lambda}) \equiv
\cfrac{1}{2} \|\boldsymbol{w}\|^2
+ C \displaystyle \sum_{i=1}^{n} \xi^{(i)}
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)} \{ 1 - \xi^{(i)} - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \}
+ \displaystyle \sum_{i=1}^{n} \mu^{(i)} \xi^{(i)}
$$

（$$\lambda^{(i)}, \mu^{(i)}$$ は未定乗数）

KKT 条件：

$$
\begin{cases}
\cfrac{\partial L}{\partial b} (\boldsymbol{w}, b, \boldsymbol{\xi}, \boldsymbol{\lambda}) = \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} = 0 & \qquad & \text{(D-1)} \\
\cfrac{\partial L}{\partial \boldsymbol{w}} (\boldsymbol{w}, b, \boldsymbol{\xi}, \boldsymbol{\lambda}) = \boldsymbol{w} + \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)} = 0 & \qquad & \text{(D-2)} \\
\cfrac{\partial L}{\partial \boldsymbol{\xi}} (\boldsymbol{w}, b, \boldsymbol{\xi}, \boldsymbol{\lambda}) = C \boldsymbol{1} + \boldsymbol{\lambda} + \boldsymbol{\mu} = 0 & \qquad & \text{(D-3)} \\
\lambda^{(i)} = 0 \quad {\rm or} \quad 1 - \xi^{(i)} - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 0 & \qquad & \text{(D-4)} \\
\mu^{(i)} = 0 \quad {\rm or} \quad \xi^{(i)} = 0 & \qquad & \text{(D-5)} \\
1 - \xi^{(i)} - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \le 0 & \qquad & \text{(D-6)} \\
\xi^{(i)} \ge 0 & \qquad & \text{(D-7)} \\
\lambda^{(i)} \le 0 & \qquad & \text{(D-8)} \\
\mu^{(i)} \le 0 & \qquad & \text{(D-9)}
\end{cases}
$$

最適解の式 $$\text{(D-1)}, \text{(D-2)}, \text{(D-3)}$$ をラグランジュ関数に代入：

$$
\begin{eqnarray}
L(\boldsymbol{w}, b, \boldsymbol{\xi}, \boldsymbol{\lambda})
&=&
\cfrac{1}{2} \|\boldsymbol{w}\|^2
+ \displaystyle \sum_{i=1}^{n} (C + \lambda^{(i)} + \mu^{(i)}) \xi^{(i)}
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
+ \displaystyle \boldsymbol{w} \cdot \left( \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)} \right)
+ \displaystyle b \sum_{i=1}^{n} \lambda^{(i)} y^{(i)}
\\
&=&
\cfrac{1}{2} \|\boldsymbol{w}\|^2 + 0
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \|\boldsymbol{w}\|^2 + 0
\\
&=&
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \cfrac{1}{2} \|\boldsymbol{w}\|^2
\\
&=&
- \displaystyle \sum_{i=1}^{n} \lambda^{(i)}
- \displaystyle \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \lambda^{(i)} \lambda^{(j)} y^{(i)} y^{(j)} \boldsymbol{x}^{(i)} \cdot \boldsymbol{x}^{(j)}
\\
&\equiv& l(\boldsymbol{\lambda})
\end{eqnarray}
$$

**→ ハードマージン SVM のときと全く同じラグランジュ双対関数が導かれる。**  
これを最大化する。

違いは制約条件。$$\text{(D-3)}, \text{(D-9)}$$ を使うと、

$$
0 \ge \mu^{(i)} = - \lambda^{(i)} - C
$$

これと $$\text{(D-8)}$$ より、

$$-C \le \lambda^{(i)} \le 0$$

以上により、ソフトマージン SVM の双対問題の制約は

$$
\begin{cases}
\displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} = 0 & \qquad & \text{(D-1)} \\
-C \le \lambda^{(i)} \le 0 & \qquad & \text{(E)}
\end{cases}
$$

以後、ハードマージン SVM 同様に双対問題を解いて $$\boldsymbol{\lambda}$$ の最適解を求めれば良い。


### $$\lambda^{(i)}$$ の値とデータサンプルの位置

$$\text{(D-3)}$$ を使って $$\text{(D-5)}$$ を書き換える。

$$
\begin{cases}
\lambda^{(i)} = 0 \quad {\rm or} \quad 1 - \xi^{(i)} - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 0 & \qquad & \text{(D-4)} \\
\lambda^{(i)} = -C \quad {\rm or} \quad \xi^{(i)} = 0 & \qquad & \text{(D-5)'} \\
1 - \xi^{(i)} - y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \le 0 & \qquad & \text{(D-6)}
\end{cases}
$$

説明のため $$\text{(D-4)}, \text{(D-6)}$$ も再掲した。

$$C \gt 0$$ なので、$$\lambda^{(i)} = 0$$ と $$\lambda^{(i)} = -C$$ を同時に満たすことはできない。  
$$\lambda^{(i)}$$ の値による場合分けを行うと、

| $$\lambda^{(i)}$$ | $$\text{(D-4)}, \text{(D-5)'}$$ より | $$\text{(D-6)}$$ より | データサンプルの位置 |
| :-- | :-- | :-- | :-- |
| $$\lambda^{(i)} = -C$$ | $$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 1 - \xi^{(i)}$$ | - | 正/負の超平面より内側 |
| $$-C \lt \lambda^{(i)} \lt 0$$ | $$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) = 1$$ | - | 正/負の超平面上（**= サポートベクトル**） |
| $$\lambda^{(i)} = 0$$ | $$\xi^{(i)} = 0$$ | $$y^{(i)} (\boldsymbol{w} \cdot \boldsymbol{x}^{(i)} + b) \ge 1$$ | 正/負の超平面より外側 |


### 決定境界を求める

双対問題の最適解を用いて、決定境界となる平面の方程式を求める。

#### 超平面内側のベクトルを求める

上述の通り、データサンプルは $$\lambda^{(i)}$$ の値によって3つに分類できる。  
後の計算のため、以下の2つを求めておく。
- $$\lambda^{(i)} = -C$$：超平面より内側の点の集合 $$V_{in}$$
- $$-C \lt \lambda^{(i)} \lt 0$$：超平面上の点（サポートベクトル）の集合 $$V_s$$


#### $$\boldsymbol{w}$$ を求める

ハードマージン SVM 同様、

$$
\boldsymbol{w} = - \displaystyle \sum_{i=1}^{n} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)}
$$

で求まる。$$\lambda^{(i)} = 0$$ なものは考えなくて良いので、$$V_s, V_{in}$$ の和を取って、

$$
\boldsymbol{w} = - \displaystyle \sum_{\boldsymbol{x}^{(i)} \in V_s, V_{in}} \lambda^{(i)} y^{(i)} \boldsymbol{x}^{(i)}
$$


#### $$b$$ を求める

ハードマージン SVM 同様、全サポートベクトルについて求めた値を平均する。

$$
b = \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{x}^{(i)} \in V_s} (y^{(i)} - \boldsymbol{w} \cdot \boldsymbol{x}^{(i)})
$$

以上により $$\boldsymbol{w}, b$$ が求まり、決定境界となる平面が定まる。


## 実装

### コード

{% gist 3c7d782482f20a5e43aec642ac977a2a svm-soft.py %}

### 動作確認

{% gist 3c7d782482f20a5e43aec642ac977a2a ~fit-soft.py %}

![SoftMarginSVM](https://user-images.githubusercontent.com/13412823/79535086-60d28000-80b7-11ea-85f7-15602c137625.gif)

**→ $$C$$ が大きくなるほどハードマージン SVM に近付く。**


# カーネルトリック

ソフトマージン SVM により、外れ値や誤分類などが原因で完全には線形分離できないときにも分類が行えるようになった。  
しかし、下図のようにそもそも線形分離が正解とならないようなケースには対応できない。

![Unknown-3](https://user-images.githubusercontent.com/13412823/79540114-8a44d900-80c2-11ea-9d5a-a4892ac786ba.png)

## 原理

### 高次元空間への射影と線形分離

上の例では $$\boldsymbol{x} = (x_1, x_2)$$ の二次元の特徴量を取り扱っている。  
ここに第三の特徴量 $$x_3 \equiv x_1^2 + x_2^2$$ を導入し、$$\boldsymbol{\phi} = (x_1, x_2, x_1^2 + x_2^2)$$ に SVM を適用すれば下図の通り線形分離できる。

![Unknown-4](https://user-images.githubusercontent.com/13412823/79541142-44891000-80c4-11ea-9a97-380e4366d74a.png)

このように、元の特徴量次元よりも高次元へとうまく射影することで、あらゆる学習サンプルを線形分離できるようになる。

より一般的には、$$m$$ 次元特徴量 $$\boldsymbol{x} = (x_1, \cdots, x_m)$$ に $$M(\gt m)$$ 次元空間への射影

$$
\boldsymbol{x} = (x_1, \cdots, x_m) \longmapsto
\boldsymbol{\phi}(\boldsymbol{x}) = (\phi_1(\boldsymbol{x}), \cdots, \phi_M(\boldsymbol{x}))
$$

を行い、$$M$$ 次元空間で SVM を適用すれば良い。

ここで、**射影にかかるコストが問題になる**。  
あらゆる変数に対して汎用的に線形分離可能となるように射影を行おうとすると、射影前に比べて射影後の次元数は非常に大きくなり（$$m \ll M$$）、計算量も膨大になる。  
特に元から高次元の特徴量を扱う場合は顕著。  
例：

$$
\boldsymbol{x} = (x_1, x_2, x_3, x_4) \longmapsto
\boldsymbol{\phi}(\boldsymbol{x}) = (x_1^2, x_2^2, x_3^2, x_4^2, x_1 x_2, x_1 x_3, x_1 x_4, x_2 x_3, x_2 x_4, x_3 x_4)
$$

この問題をどうにかしたい。


### 内積とカーネルトリック

元の特徴量による双対問題の学習規則

$$
\lambda^{(k)} \longleftarrow \lambda^{(k)} - \eta \left( 1 + \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(k)} y^{(j)} \boldsymbol{x}^{(k)} \cdot \boldsymbol{x}^{(j)} \right)
$$

は、射影後の空間では下式に書き換えられる。

$$
\lambda^{(k)} \longleftarrow \lambda^{(k)} - \eta \left( 1 + \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(k)} y^{(j)} \boldsymbol{\phi}(\boldsymbol{x}^{(k)}) \cdot \boldsymbol{\phi}(\boldsymbol{x}^{(j)}) \right)
$$

重要なのは、**学習規則に現れる $$\boldsymbol{\phi}$$ が全て内積の形である** ということ。  
つまり、**射影後の変数 $$\boldsymbol{\phi}$$ そのものではなく、その内積だけが大事**。

なので、$$\boldsymbol{\phi}(\boldsymbol{x})$$ 自体を計算することなく、射影後の変数の内積（**カーネル** と呼ばれる）

$$
K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)})
\equiv \boldsymbol{\phi}(\boldsymbol{x}^{(k)}) \cdot \boldsymbol{\phi}(\boldsymbol{x}^{(j)})
= \displaystyle \sum_{i=1}^{M} \phi_i(\boldsymbol{x}^{(k)}) \phi_i(\boldsymbol{x}^{(j)})
$$

だけをうまく定義して計算できないかを考える。

当然、カーネル $$K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)})$$ はどんな関数でも良いわけではなく、上のように内積の形で表現できる関数でなければならない。  
具体的には、**Mercer の定理** を満たす関数であれば良い。

> **【NOTE】Mercer の定理**
>
> 関数 $$k(\boldsymbol{x}, \boldsymbol{y})$$ が
> - 対称関数：$$k(\boldsymbol{x}, \boldsymbol{y}) = k(\boldsymbol{y}, \boldsymbol{x})$$
> - 半正定値：任意の実数 $$c_i, c_j$$ に対して $$\displaystyle \sum_i \sum_j c_i c_j k(\boldsymbol{x}^{(i)}, \boldsymbol{x}^{(j)}) \ge 0$$
>
> の両方を満たす時、
>
> $$k(\boldsymbol{x}, \boldsymbol{y}) = \boldsymbol{\phi}(\boldsymbol{x}) \cdot \boldsymbol{\phi}(\boldsymbol{y})$$
>
> となるような関数 $$\boldsymbol{\phi}$$ が存在する。  
> 逆も成り立つ。

よく使われるカーネル：

| 名称 | 定義 |
| :-- | :-- |
| 多項式カーネル | $$K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)}) = (\boldsymbol{x}^{(k)} \cdot \boldsymbol{x}^{(j)} + c)^d$$ |
| ガウシアンカーネル | $$K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)}) = \exp \left( - \cfrac{\| \boldsymbol{x}^{(k)} - \boldsymbol{x}^{(j)} \|^2}{2 \sigma^2} \right)$$ |
| シグモイドカーネル | $$K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)}) = \tanh (a \boldsymbol{x}^{(k)} \cdot \boldsymbol{x}^{(j)} + b)$$ |

採用するカーネルを決めれば、

$$
\lambda^{(k)} \longleftarrow \lambda^{(k)} - \eta \left( 1 + \displaystyle \sum_{j=1}^{n} \lambda^{(j)} y^{(k)} y^{(j)} K(\boldsymbol{x}^{(k)}, \boldsymbol{x}^{(j)}) \right)
$$

により $$\boldsymbol{\lambda}$$ を最適化できる。


### 決定境界を求める

$$\boldsymbol{\lambda}$$ の最適解に対して、これまでと同様の方法で

$$
\begin{eqnarray}
\boldsymbol{w}_{\phi}
&=& - \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \in V_s, V_{in}} \lambda^{(i)} y^{(i)} \boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \\
b_{\phi}
&=& \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \in V_s} \left( y^{(i)} - \boldsymbol{w}_{\phi} \cdot \boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \right) \\
&=& \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \in V_s} \left( y^{(i)} + \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(j)}) \in V_s, V_{in}} \lambda^{(j)} y^{(j)} \boldsymbol{\phi}(\boldsymbol{x}^{(j)}) \cdot \boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \right) \\
&=& \cfrac{1}{|V_s|} \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \in V_s} \left( y^{(i)} + \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(j)}) \in V_s, V_{in}} \lambda^{(j)} y^{(j)} K(\boldsymbol{x}^{(j)}, \boldsymbol{x}^{(i)}) \right)
\end{eqnarray}
$$

を得る。  
ここで以下の点に注意。
- **この $$\boldsymbol{w}_{\phi}, b_{\phi}$$ は、元の $$m$$ 次元空間ではなく射影後の $$M$$ 次元空間における決定境界を表す**
- **カーネルトリックを利用しているので、$$\boldsymbol{\phi}(\boldsymbol{x}^{(i)})$$ の値は計算されておらず、したがって $$\boldsymbol{\phi}(\boldsymbol{x}^{(i)})$$ の表式があらわに残る $$\boldsymbol{w}_{\phi}$$ の値も計算はできない**

学習済みのモデルを使って入力 $$\boldsymbol{x}$$ のラベルを判別する際の決定境界は、$$\boldsymbol{x}$$ を $$M$$ 次元空間へ射影して

$$\boldsymbol{w}_{\phi} \cdot \boldsymbol{\phi}(\boldsymbol{x}) + b_{\phi} = 0$$

$$\boldsymbol{w}_{\phi}$$ の表式を代入すれば

$$- \displaystyle \sum_{\boldsymbol{\phi}(\boldsymbol{x}^{(i)}) \in V_s, V_{in}} \lambda^{(i)} y^{(i)} K(\boldsymbol{x}^{(i)}, \boldsymbol{x}) + b_{\phi} = 0$$

となり $$\boldsymbol{\phi}$$ が消えるので、$$\boldsymbol{\phi}$$ がどんな関数か分からなくてもクラス判別ができる。

> **【NOTE】**
>
> 決定境界の式を見れば分かる通り、判別を行うためにはモデル自身が
> - $$V_s, V_{in}$$ に属するデータサンプル（= サポートベクトル, 正/負の超平面内部の点）とその正解ラベル
> - $$\boldsymbol{\lambda}$$ の最適解
>
> を保持しておく必要がある。


## 実装

### コード

{% gist 3c7d782482f20a5e43aec642ac977a2a svm-kernel.py %}

### 動作確認

{% gist 3c7d782482f20a5e43aec642ac977a2a ~fit-kernel-1.py %}

![Unknown-5](https://user-images.githubusercontent.com/13412823/79570066-bb89cd00-80f3-11ea-9557-b6af06c5ea0c.png)

{% gist 3c7d782482f20a5e43aec642ac977a2a ~fit-kernel-2.py %}

![Unknown-6](https://user-images.githubusercontent.com/13412823/79570058-b9c00980-80f3-11ea-8072-755f93838d45.png)
