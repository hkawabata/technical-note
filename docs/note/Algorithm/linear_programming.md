---
title: 線形計画法（作成中）
---

# 問題定義

制約条件のもとで、負でない変数の線形多項式で表現される目的関数を最大化 or 最小化する

目的関数：

$$\displaystyle z = \sum_{j=1}^N c_j x_j$$

$$max \left( z \right) \mbox{ or } min \left( z \right)$$

制約条件：

$$\begin{cases} \displaystyle \sum_{j=1}^N a_{ij} x_j \lesseqqgtr b_i, & i = 1, ..., M \\ x_j \ge 0, & j = 1, ..., N \end{cases}$$

## 問題の例

- 以下の条件で、売上を最大にするには製品A, Bをそれぞれいくつ作れば良いか？
	- ある工場で部品1, 2, 3の在庫がそれぞれ18000, 21000, 21000個
	- 製品A, Bそれぞれの販売単価、および作るのに必要な部品の個数は下表の通り

|  | 部品1 | 部品2 | 部品3 | 単価 |
| :-- | :-- | :-- | :-- | :-- |
| 製品A | 1 | 2 | 3 | 20000 |
| 製品B | 3 | 3 | 1 | 10000 |

$$z = 20000x_1 + 10000x_2$$

$$max \left( z \right)$$

$$\begin{cases} x_1 + 3x_2 \le 18000 \\ 2x_1 + 3x_2 \le 21000 \\ 3x_1 + x_2 \le 21000 \\ x_1, x_2 \ge 0 \end{cases}$$

このケースであれば、変数が2つしかないためグラフを利用して解ける。

→ $$x_1 = 6000, x_2 = 3000$$ で $$z$$ の最大値150,000,000

![LP](https://user-images.githubusercontent.com/13412823/65401522-9d7d1800-de03-11e9-98ba-075557da52c6.png)


## 重要な前提

上述の例のように、制約及び目的関数が全て線形多項式のみからなるの最大化・最小化問題においては、

- **実行可能領域は凸性を持つ**：領域内の任意の2点を結んだ線分も同じ領域に含まれる
- **解を与えるのは実行可能領域の境界のどこかになる**：2次元空間であれば境界の線分あるいは頂点
	- 線分の場合は、線分上のどの点でも同じ値となるため、実質的には頂点に限定して求めて良い

# 解法：シンプレックス法 (Simplex method)

## 基本思想

1. 最初に（最適解とは限らないが）実現可能な境界上の解を1つ見つける
2. その解からスタートして、境界に沿っていずれかの変数を増減させ、より目的関数を最大化 or 最小化する次の頂点（解）を見つける
3. どの変数を増減させても目的関数が増加しない状態になったら終了

## 流れ

### 1. 標準形への変換

- 以下のような問題に落とし込みたい
	- 目的関数の最小化問題
	- 多項式の制約は全て上限制約を課す不等式
	- 変数 $$x_i$$ は全て非負

$$min \left( z \right)$$

$$\begin{cases} \displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i, & i = 1, ..., M \\ x_j \ge 0, & j = 1, ..., N \end{cases}$$

#### 最大化問題であるとき

符号を反転させ、$$z' = -z$$ の最小化問題として扱う。

#### 下限制約を課す不等式があるとき

下限制約を課す不等式

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \ge b_i$$

は上限制約を課す不等式

$$\displaystyle \sum_{j=1}^N \left( -a_{ij} x_j \right) \le -b_i$$

に変換する。

#### 等式の制約があるとき

$$\displaystyle \sum_{j=1}^N a_{ij} x_j = b_i$$

は、

$$\begin{cases} \displaystyle \sum_{j=1}^N a_{ij} x_j \ge b_i \\ \displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i \end{cases}$$

に分解する。

#### 変数の値として負の数も許容されるとき

特定の変数 $$x_i$$ に非負条件がない場合、

$$\begin{cases} x_i = x_{i_1} - x_{i_2} \\ x_{i_1}, x_{i_2} \ge 0 \end{cases}$$

のように定義し、$$x_i$$ を $$x_{i_1} - x_{i_2}$$ に置き換えて処理を行う（変数は1つ増えることになる）。


### 2. スラック形への変換

- 非負条件以外の不等式制約を等式制約に変換したい

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i$$

$$\Longleftrightarrow \begin{cases} \displaystyle s_i = b_i - \sum_{j=1}^N a_{ij} x_j, & i = 1, ..., M \\ s_i \ge 0 \end{cases}$$

$$s_i$$ は不等式の余裕（= slack）を埋める変数であり、**スラック変数** と呼ばれる。

スラック変数をその他の変数と同様に扱い、$$s_i = x_{N+i}$$ と置く。

スラック形：

$$\begin{cases}z = \sum_{j=1}^N c_j x_j \\ \displaystyle x_{N+i} = b_i - \sum_{j=1}^N a_{ij} x_j, & i = 1, ..., M \\ x_1, ..., x_{N+M} \ge 0 \end{cases}$$

- **左辺がスラック変数である必要はなく、右辺の変数いずれかと入れ替えて別のスラック形に変形できる**
	- 左辺の変数 M 個：**基底変数**
	- 右辺の変数 N 個：**非基底変数**

### 3. 実現可能な基底解を1つ求める

- スラック形は M 個の連立方程式であり、変数の数（M+N）は M より大きいため、無限個の解を持つ
- 探索の開始地点として、領域境界の **実現可能基底解** を1つ求めたい

#### 標準形において $$b_i$$ が全て非負の場合

- 最初のスラック形において、非基底変数（= スラック変数以外）の N 個をゼロと置くことで、非負条件を満たす実現可能基底解を1組、一意に求めることができる

$$(x_1, ..., x_N, x_{N+1}, ..., x_{N+M}) = (0, ..., 0, b_1, ..., b_M)$$

#### 標準形において負の $$b_i$$ が存在する場合

$$x_1, ..., x_N = 0$$ とおくと非負条件を満たさない変数が存在するため、同じ方法は使えない。

まず実現可能な解が存在するかどうかから調べる必要がある。

新たなスラック変数 $$x^{\prime}_i$$ を導入し、以下の補助最小化問題を解く。

$$\begin{cases}z_2 = \sum_i x^{\prime}_i \\ \displaystyle x_{N+i} = \begin{cases} b_i - \sum_{j=1}^N a_{ij} x_j, & \mbox{if } b_i \ge 0 \\ \displaystyle x_{N+i} = b_i - \sum_{j=1}^N a_{ij} x_j + x^{\prime}_i, & \mbox{if } b_i \lt 0 \end{cases} \\ x_1, ..., x_{N+2M} \ge 0 \end{cases}$$

この補助問題をシンプレックス法で解く（必ず解ける）。

- 最適値がゼロ（$$min(z_2) = 0$$）の場合：**補助問題の最適解 = 元の問題の初期実行可能基底解として良い**
- 最適値が正（$$min(z_2) \ge 0$$）の場合：**元の問題は実行不可能**

## 二段階法