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

## 例

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


# 解法

## シンプレックス法 (Simplex method)

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

コンセプト：非負条件以外の不等式制約を等式制約に変換

$$\displaystyle \sum_{j=1}^N a_{ij} x_j \le b_i$$

$$\Longleftrightarrow \begin{cases} \displaystyle s_i = b_i - \sum_{j=1}^N a_{ij} x_j, & i = 1, ..., M \\ s_i \ge 0 \end{cases}$$
