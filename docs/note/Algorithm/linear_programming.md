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

# 解法

## シンプレックス法 (Simplex method)

### 標準形への変換

- 以下のような問題に落とし込みたい
	- 目的関数の最小化問題
	- 制約は全て上限制約の不等式

$$min \left( z \right)$$

$$\begin{cases} \displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i, & i = 1, ..., M \\ x_j \ge 0, & j = 1, ..., N \end{cases}$$

#### 最大化問題であるとき

符号を反転させ、$$z' = -z$$ の最小化問題として扱えば良いだけ。

#### 下限制約の不等式があるとき

上限制約の不等式

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \ge b_i$$

は下限制約の不等式

$$\displaystyle \sum_{j=1}^N \left( -a_{ij} x_j \right) \le -b_i$$

に変換できる。

#### 等式の制約があるとき

$$\displaystyle \sum_{j=1}^N a_{ij} x_j = b_i$$

は、

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \ge b_i$$

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i$$

に分解する。

#### 変数の値として負の数も許容されるとき

$$x_i$$

### スラック形への変換
