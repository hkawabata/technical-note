---
title: ジョルダン標準形
title-en: Jordan Normal Form
---

# ジョルダン標準形とは

## 定義

以下を満たす $n$ 次正方行列 $J_{n}(\lambda)$ を **ジョルダンブロック（ジョルダン細胞）** と呼ぶ。

- 対角成分に同じ値 $\lambda$ が並ぶ
- 対角成分の1つ上の成分が全て1
- 他の成分が全て0

$$
J_n(\lambda) := \begin{pmatrix}
	\lambda & 1 & & & O \\
	& \lambda & 1 & & \\
	& & \ddots & \ddots & \\
	& & & \lambda & 1 & \\
	O & & & & \lambda
\end{pmatrix}
$$

$n$ 次正方行列 $A$ の固有値を $\lambda_1, \cdots, \lambda_k$ とすると、各固有値に対応するジョルダンブロックを斜めに並べた $n$ 次正方行列

$$
J := \begin{pmatrix}
	J_{n_1}(\lambda_1) & & O \\
	& \ddots & \\
	O & & J_{n_l}(\lambda_k) \\
\end{pmatrix}
$$

$$n_1 + \cdots + n_l = n$$

を、行列 $A$ の **ジョルダン標準形** といい、適切な[正則行列](special-matrix/regular-matrix.md) $P$ を用いて

$$P^{-1}AP = J$$

と変換できる。

ここで、$J$ の表式において $n$ と $\lambda$ の添字の最大値が $l,k$ で異なるのは、1つの固有値から複数のジョルダンブロックが求まることがあるため（以下の NOTE を参照）。

> **【NOTE】**
> 
> ジョルダン標準形におけるジョルダン細胞のサイズは、固有値の重複度と一致するとは限らない。  
> 例えば3次元正方行列 $A$ の固有値が5（重複度3）だったとして、そのジョルダン標準形には以下の3通りが考えられる（後述の計算方法を参照）。
> 
> $$
\begin{pmatrix}
	5 & 1 & 0 \\
	0 & 5 & 1 \\
	0 & 0 & 5
\end{pmatrix},\quad
\begin{pmatrix}
	5 & 1 & 0 \\
	0 & 5 & 0 \\
	0 & 0 & 5
\end{pmatrix},\quad
\begin{pmatrix}
	5 & 0 & 0 \\
	0 & 5 & 0 \\
	0 & 0 & 5
\end{pmatrix}
$$



## 意義

- 任意の行列が[対角化](diagonalization.md)できるとは限らない
- 代わりに、対角化できない行列もジョルダン標準形に変換できる
- これにより、対角行列とまではいかなくとも、対角行列に可能な限り近い形に変換して使いやすくできる

# ジョルダン標準形への変換

$n$ 次正方行列 $A$ のジョルダン標準形 $J$ を求める方法について記述する。

## 理論

ジョルダン標準形は、行列 $A$ の異なる固有値ごとにジョルダンブロックを求め、それらの斜めに並べることで求められる。

### 行列が対角化可能である場合

ジョルダン標準形は対角化によって得られる対角行列そのもの（ジョルダンブロックの大きさが全て1である特殊ケース）であるから、[対角化](diagonalization.md)を行えば良い。

生成行列 $P$ は固有値ごとの固有ベクトルを列ベクトルとして横に並べたものに等しい。

### 行列が対角化可能でない場合

行列 $A$ が対角化できないのは、$A$ の固有値の中に「固有値の重複度 $r >$ 固有空間の次元（固有値に属する線形独立な固有ベクトルの個数）」となるようなものが存在するとき。

このような固有値以外では、属するジョルダンブロックは全てサイズ1の $J_1(\lambda)$ となる。  
よって以後は、固有空間の次元が重複度よりも小さいような固有値に属するジョルダンブロックの求め方について記述する。

#### ジョルダンブロックの求め方

> **【定理】**
> 
> $n$ 次正方行列 $A$ の固有値 $\lambda$ に対応する「サイズ $k$ 以上のジョルダンブロックの数」は、$\lambda$ の $k$ 階の[広義固有空間](generalized-eigenvector.md)を $V^{(k)}$ として、
> 
> $$
\dim V^{(k)} - \dim V^{(k-1)}
$$
> 
> で表される。
> 
> 別表現として、[次元定理](rank-nullity-theorem.md)より $\dim V^{(k)} = n - \mathrm{rank}(A-\lambda I)^k$ なので、
> 
> $$
\mathrm{rank}(A-\lambda I)^{k-1} - \mathrm{rank}(A-\lambda I)^k
$$
> 
> とも表せる。

> **【定理】**
> 
> $n$ 次正方行列 $A$ の固有値 $\lambda$ に対応する $k$ 階の広義固有空間 $V^{(k)}$ について、
> 
> $$
V^{(1)} \subset V^{(2)} \subset V^{(3)} \subset \cdots
$$
>
> であり、固有値 $\lambda$ の重複度を $r$ とすると、
> 
> $$
\dim V^{(d)} = r
$$
> 
> となる $d$ が存在する。さらに、
> 
> $$
\begin{eqnarray}
	\dim V^{(1)} \lt \dim V^{(2)} \lt \cdots \lt \dim V^{(d)} \\
	\dim V^{(d+m)} = \dim V^{(d)} \quad (m \gt 0)
\end{eqnarray}
$$
> 
> が成り立つ。

これらの定理を用いると、固有値に対応するジョルダンブロックの大きさと数を調べられる。

例えば重複度 $r=14$ の固有値 $\lambda$ について、$(A-\lambda I),\ (A-\lambda I)^2,\ (A-\lambda I)^3, \cdots$ の rank から広義固有空間の次元を調べていった結果、以下の表が得られたとする。

| $k$ | $\dim V^{(k)}$ | $\dim V^{(k)}-\dim V^{(k-1)}$<br>$= k$ 階の広義固有ベクトルの個数<br>$=k$ 以上のサイズのジョルダンブロック数 |
| :-- | :-- | :-- |
| 0 | 0 | - |
| 1 | 5 | 5 |
| 2 | 9 | 4 |
| 3 | 11 | 2 |
| 4 | 13 | 2 |
| 5 | 14 | 1 |
| 6 | 14 | 0 |
| 7 | 14 | 0 |
| 8 | 14 | 0 |
| $\vdots$ | $\vdots$ | $\vdots$ |

（※ $k=5$ の時点で $\dim V^{(5)} = r$ となっているので、$k \ge 6$ は調べずとも明らか）

1. サイズ5以上のブロックが1つで、サイズ6以上のブロックは存在しないから、ブロックの1つは $J_5(\lambda)$
	1. → サイズ5以上のブロックは全て求まった
2. サイズ4以上のブロックは2つあり、1より、そのうちサイズ5以上のものは1つだけなので、もう一つは $J_4(\lambda)$
	1. → サイズ4以上のブロックも全て求まった
3. サイズ3以上のブロックは2つで、いずれも1,2で求められているため、サイズがちょうど3のブロックは存在しない
4. サイズ2以上のブロックは4つで、そのうちサイズ3以上のものは1〜3より2つだけなので、残り2つは $J_2(\lambda),\ J_2(\lambda)$
5. サイズ1以上のブロックは5つで、そのうちサイズ2以上のものは1〜4より4つだけなので、残り1つは $J_1(\lambda)$

という流れで、固有値 $\lambda$ に対応するジョルダンブロックは $J_5(\lambda),\ J_4(\lambda),\ J_2(\lambda),\ J_2(\lambda),\ J_1(\lambda)$ だと分かる。  
これらを任意の順番で斜めに並べれば良い（他の固有値に対応するブロックと順番が入れ替わっても良い）。

#### 生成行列の部分行列の求め方

> **【定理】**
> 
> 行列 $A$ の固有値 $\lambda$ に対応する $k$ 階の広義固有ベクトル $\boldsymbol{u}^{(k)}$ について、$(A-\lambda I) \boldsymbol{u}^{(k)}$ は $k-1$ 階の広義固有ベクトルになる。

> **【定理】**
> 
> 行列 $A$ の固有値 $\lambda$ に対応する $k$ 階の広義固有ベクトル $\boldsymbol{u}^{(k)}$ について、
> 
> $$
\left(
	(A-\lambda I)^{k-1} \boldsymbol{u}^{(k)},
	(A-\lambda I)^{k-2} \boldsymbol{u}^{(k)},
	\cdots,
	(A-\lambda I) \boldsymbol{u}^{(k)},
	\boldsymbol{u}^{(k)},
\right)
$$
> 
> を列ベクトルとしてこの順に並べた $n \times k$ 行列は、ジョルダン標準形生成行列の部分行列にでき、大きさ $k$ のジョルダンブロックに対応する。
> 
> 同じ固有値 $\lambda$ に対応するジョルダンブロックが複数存在する場合、
> - それぞれのブロックの大きさ $k_1, \cdots, k_m$ に対応する広義固有ベクトル $\boldsymbol{u}_1^{(k_1)}, \cdots, \boldsymbol{u}_m^{(k_m)}$ を互いに線形独立となるように取ることができる
> - それらから計算した $m$ 個の $n \times k_i$ 行列を構成する列ベクトル（重複度 $r$ と同じ本数だけ存在する）は全て互いに線形独立になる

これらの定理を用いて、ジョルダン標準形の生成行列 $P$ に関して、各ジョルダンブロックに対応する部分行列を求めることができる。

例えば前節と同じ例を用いると、

| $k$ | $\dim V^{(k)}$ | $\dim V^{(k)}-\dim V^{(k-1)}$<br>$= k$ 階の広義固有ベクトルの個数<br>$=k$ 以上のサイズのジョルダンブロック数 | $V^{(k)}$ の基底ベクトル | $k$ 階の広義固有ベクトル |
| :-- | :-- | :-- | :-- | :-- |
| 0 | 0 | - | - | - |
| 1 | 5 | 5 | $\boldsymbol{x}_1^{(1)}, \cdots, \boldsymbol{x}_5^{(1)}$ | $\boldsymbol{u}_1^{(1)},\ \boldsymbol{u}_2^{(1)},\ \boldsymbol{u}_3^{(1)},\ \boldsymbol{u}_4^{(1)},\ \boldsymbol{u}_5^{(1)}$ |
| 2 | 9 | 4 | $\boldsymbol{x}_1^{(2)}, \cdots, \boldsymbol{x}_9^{(2)}$ | $\boldsymbol{u}_1^{(2)},\ \boldsymbol{u}_2^{(2)},\ \boldsymbol{u}_3^{(2)},\ \boldsymbol{u}_4^{(2)}$ |
| 3 | 11 | 2 | $\boldsymbol{x}_i^{(3)} (i = 1, \cdots, 11)$ | $\boldsymbol{u}_1^{(3)},\ \boldsymbol{u}_2^{(3)}$ |
| 4 | 13 | 2 | $\boldsymbol{x}_1^{(4)}, \cdots, \boldsymbol{x}_{13}^{(4)}$ | $\boldsymbol{u}_1^{(4)},\ \boldsymbol{u}_2^{(4)}$ |
| 5 | 14 | 1 | $\boldsymbol{x}_1^{(5)}, \cdots, \boldsymbol{x}_{14}^{(5)}$ | $\boldsymbol{u}_1^{(5)}$ |

1. 方程式 $(A-\lambda I)^k \boldsymbol{u}=\boldsymbol{0}$ を解き、各 $V^{(k)}$ の基底ベクトル（表の $\boldsymbol{x}_i^{(k)}$）を求める
2. 5階の広義固有ベクトル：
	1. 表より、1つだけ存在する
	2. $V^{(5)}$ の基底ベクトル $\boldsymbol{x}_1^{(5)}, \cdots, \boldsymbol{x}_{14}^{(5)}$ の中から、$V^{(4)}$ の基底ベクトル $\boldsymbol{x}_1^{(4)}, \cdots, \boldsymbol{x}_{13}^{(4)}$ と線形独立なものを1つ選ぶ（複数候補があればどれでも良い）
	3. 選んだものを5階の広義固有ベクトル $\boldsymbol{u}_1^{(5)}$ とする
	4. これに $A-\lambda I$ を1〜4回かけた $(A-\lambda I) \boldsymbol{u}_1^{(5)}, \cdots, (A-\lambda I)^4 \boldsymbol{u}_1^{(5)}$ を順に4〜1階の広義固有ベクトル $\boldsymbol{u}_1^{(4)}, \boldsymbol{u}_1^{(3)}, \boldsymbol{u}_1^{(2)}, \boldsymbol{u}_1^{(1)}$ とする
	5. $n \times 5$ 行列  $\left(\boldsymbol{u}_1^{(1)}, \boldsymbol{u}_1^{(2)}, \boldsymbol{u}_1^{(3)}, \boldsymbol{u}_1^{(4)}, \boldsymbol{u}_1^{(5)}\right)$ は $J_5(\lambda)$ に対応する $P$ の部分行列になる
3. 4階の広義固有ベクトル：
	1. 1つはこれまでのステップで求められている（$\boldsymbol{u}_1^{(4)}$）ので、あと1つを求めたい
	2. $V^{(4)}$ の基底ベクトル $\boldsymbol{x}_1^{(4)}, \cdots, \boldsymbol{x}_{13}^{(4)}$ の中から、$\boldsymbol{u}_1^{(4)}$ 及び $V^{(3)}$ の基底ベクトル $\boldsymbol{x}_1^{(3)}, \cdots, \boldsymbol{x}_{11}^{(3)}$ と線形独立なものを1つ選ぶ
	3. 選んだものを残る4階の広義固有ベクトル $\boldsymbol{u}_2^{(4)}$ とする
	4. これに $A-\lambda I$ を1〜3回かけた $(A-\lambda I) \boldsymbol{u}_2^{(4)}, (A-\lambda I)^2 \boldsymbol{u}_2^{(4)}, (A-\lambda I)^3 \boldsymbol{u}_2^{(4)}$ を順に3〜1階の広義固有ベクトル $\boldsymbol{u}_2^{(3)}, \boldsymbol{u}_2^{(2)}, \boldsymbol{u}_2^{(1)}$ とする
	5. $n \times 4$ 行列  $\left(\boldsymbol{u}_2^{(1)}, \boldsymbol{u}_2^{(2)}, \boldsymbol{u}_2^{(3)}, \boldsymbol{u}_2^{(4)}\right)$ は $J_4(\lambda)$ に対応する $P$ の部分行列になる
4. 3階の広義固有ベクトル
	1. これまでのステップで2つとも求め終わっている（$\boldsymbol{u}_1^{(3)}, \boldsymbol{u}_2^{(3)}$）
5. 2階の広義固有ベクトル
	1. 2つはこれまでのステップで求められている（$\boldsymbol{u}_1^{(2)}, \boldsymbol{u}_2^{(2)}$）ので、あと2つを求めたい
	2. $V^{(2)}$ の基底ベクトル $\boldsymbol{x}_1^{(2)}, \cdots, \boldsymbol{x}_9^{(2)}$ の中から、$\boldsymbol{u}_1^{(2)}, \boldsymbol{u}_2^{(2)}$ 及び $V^{(1)}$ の基底ベクトル $\boldsymbol{x}_1^{(1)}, \cdots, \boldsymbol{x}_5^{(1)}$ と線形独立なものを2つ選ぶ
	3. 選んだものを残る2階の広義固有ベクトル $\boldsymbol{u}_3^{(2)}, \boldsymbol{u}_4^{(2)}$ とする
	4. これらに $A-\lambda I$ を1回かけた $(A-\lambda I) \boldsymbol{u}_3^{(2)}, (A-\lambda I) \boldsymbol{u}_4^{(2)}$ を1階の広義固有ベクトル $\boldsymbol{u}_3^{(1)}, \boldsymbol{u}_4^{(1)}$ とする
	5. $n \times 2$ 行列 $\left(\boldsymbol{u}_3^{(1)}, \boldsymbol{u}_3^{(2)}\right),\ \left(\boldsymbol{u}_4^{(1)}, \boldsymbol{u}_4^{(2)}\right)$ はともに $J_2(\lambda)$ に対応する $P$ の部分行列になる
6. 1階の広義固有ベクトル
	1. 4つはこれまでのステップから求められている（$\boldsymbol{u}_1^{(1)}, \boldsymbol{u}_2^{(1)}, \boldsymbol{u}_3^{(1)}, \boldsymbol{u}_4^{(1)}$）ので、あと1つを求めたい
	2. $V^{(1)}$ の基底ベクトル $\boldsymbol{x}_1^{(1)}, \cdots, \boldsymbol{x}_5^{(1)}$ の中から、$\boldsymbol{u}_1^{(1)}, \boldsymbol{u}_2^{(1)}, \boldsymbol{u}_3^{(1)}, \boldsymbol{u}_4^{(1)}$ と線形独立なものを1つ選ぶ
	3. 選んだものを残る1階の広義固有ベクトル $\boldsymbol{u}_5^{(1)}$ とする
	4. $n \times 1$ 行列 $\boldsymbol{u}_5^{(1)}$ は $J_1(\lambda)$ に対応する $P$ の部分行列になる

という流れで、固有値 $\lambda$ に対するジョルダン標準形生成行列 $P$ の部分行列

- $\left(\boldsymbol{u}_1^{(1)}, \boldsymbol{u}_1^{(2)}, \boldsymbol{u}_1^{(3)}, \boldsymbol{u}_1^{(4)}, \boldsymbol{u}_1^{(5)}\right)$ 
- $\left(\boldsymbol{u}_2^{(1)}, \boldsymbol{u}_2^{(2)}, \boldsymbol{u}_2^{(3)}, \boldsymbol{u}_2^{(4)}\right)$
- $\left(\boldsymbol{u}_3^{(1)}, \boldsymbol{u}_3^{(2)}\right)$
- $\left(\boldsymbol{u}_4^{(1)}, \boldsymbol{u}_4^{(2)}\right)$
- $\boldsymbol{u}_5^{(1)}$

が求まる。


## 具体例

### 【1】2次

### 【2】3次・2重解

$$
A = \begin{pmatrix}
	1 & 1 & 1 \\
	3 & 0 & -3 \\
	-4 & 3 & 6
\end{pmatrix}
$$

$A$ の固有多項式は

$$
\det (A-\lambda I) =
\det
\begin{pmatrix}
	1-\lambda & 1 & 1 \\
	3 & -\lambda & -3 \\
	-4 & 3 & 6-\lambda
\end{pmatrix}
=
-(\lambda-2)^2 (\lambda-3) 
$$

なので、
- 固有値は $\lambda_1 = 3, \lambda_2 = 2$
- それぞれの重複度は $r_1 = 1, r_2 = 2$

**■ 固有値ごとのジョルダン細胞と生成ベクトル**

**○ $\lambda_1 = 3$ について**

**○ $\lambda_1 = 2$ について**

**【1階の固有空間 $V^{(1)}$】**

**【2階の固有空間 $V^{(2)}$】**





重複度2以上の固有値 $\lambda=2$ について調べる。  

$$
\begin{eqnarray}
	\mathrm{rank}(A-2I)
	&=&
	\mathrm{rank} \begin{pmatrix}
		-1 & 1 & 1 \\
		3 & -2 & -3 \\
		-4 & 3 & 4
	\end{pmatrix}
	\\ &=&
	\mathrm{rank} \begin{pmatrix}
		-1 & 1 & 1 \\
		0 & 1 & 0 \\
		0 & -1 & 0
	\end{pmatrix}
	\\ &=&
	\mathrm{rank} \begin{pmatrix}
		-1 & 1 & 1 \\
		0 & 1 & 0 \\
		0 & 0 & 0
	\end{pmatrix}
	\\ &=&
	2
\end{eqnarray}
$$


よって3次元固有ベクトル $(x, y, z)$ に2つの独立した制約がかかるので、線形独立な固有ベクトルの数は $3-2=1$

よって、固有値 $\lambda=2$ に属する線形独立な固有ベクトルは1つしか存在しない。  
したがって、$A$ のジョルダン標準形 $J$ は

$$
J = \begin{pmatrix}
	J_2(2) & O \\
	O & J_1(3)
\end{pmatrix}
=
\begin{pmatrix}
	2 & 1 & 0 \\
	0 & 2 & 0 \\
	0 & 0 & 3
\end{pmatrix}
$$



### 【3】3次・3重解



### 【4】6次・5重解

$$
A = \begin{pmatrix}
	0 & 1 & 1 & 1 & 1 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

$A$ の固有多項式は

$$
\det (A-\lambda I) =
\det
\begin{pmatrix}
	-\lambda & 1 & 1 & 1 & 1 & 1 \\
	0 & -\lambda & 0 & 0 & 0 & 1 \\
	0 & 0 & -\lambda & 0 & 0 & 1 \\
	0 & 0 & 0 & -\lambda & 0 & 1 \\
	0 & 0 & 0 & 0 & -\lambda & 1 \\
	0 & 0 & 0 & 0 & 0 & 1-\lambda
\end{pmatrix}
=
-\lambda^5(1-\lambda)
$$

なので、
- 固有値は $\lambda_1 = 1, \lambda_2 = 0$
- それぞれの重複度は $r_1 = 1, r_2 = 5$

**■ 固有値ごとのジョルダン細胞と生成ベクトル**

**○ $\lambda_1 = 1$ について**

重複度 $r_1 = 1$ なので、固有ベクトルがジョルダン細胞 $J_1(1)$ を与える。

$$
(A - \lambda I) \boldsymbol{u}
=
\begin{pmatrix}
	-1 & 1 & 1 & 1 & 1 & 1 \\
	0 & -1 & 0 & 0 & 0 & 1 \\
	0 & 0 & -1 & 0 & 0 & 1 \\
	0 & 0 & 0 & -1 & 0 & 1 \\
	0 & 0 & 0 & 0 & -1 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6
\end{pmatrix}
= 0
$$

を解くと、

$$u_1 = 5u_6,\ u_2=u_3=u_4=u_5=u_6$$

よって $\lambda_1$ に属する固有ベクトル $\boldsymbol{u}(\lambda_1)$ は、

$$
\boldsymbol{u}(\lambda_1) = u_6 \begin{pmatrix}
	5 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1
\end{pmatrix}
\tag{4.1}
$$

**○ $\lambda_2 = 0$ について**

重複度 $r_2=5\gt 1$ なので、対角化できるとは限らず、ジョルダン細胞の大きさを調べる必要がある。

$$
\begin{eqnarray}
\dim V^{(1)} &=& 6-\mathrm{rank}(A-0I)
\\ &=&
6-\mathrm{rank} \begin{pmatrix}
	0 & 1 & 1 & 1 & 1 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
=
6-\mathrm{rank} \begin{pmatrix}
	0 & 1 & 1 & 1 & 1 & 0 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\\ &=& 6-2 = 4
\\
\\
\dim V^{(2)} &=& 6-\mathrm{rank}(A-0I)^2
\\ &=&
6-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 5 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
=
6-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
= 6-1 = 5
\end{eqnarray}
$$

$\dim V^{(2)} = r_2$ となったので、$\dim V^{(3)}$ 以上について調べる必要はない。

| $k$ | $\dim V^{(k)}$ | $\dim V^{(k)}-\dim V^{(k-1)}$<br>$= k$ 階の広義固有ベクトルの個数<br>$=k$ 以上のサイズのジョルダンブロック数 |
| :-- | :-- | :-- |
| 0 | 0 | - |
| 1 | 4 | 4 |
| 2 | 5 | 1 |

表より、$\lambda_2=0$ に属するジョルダンブロックは $J_2(0)$ が1つ、$J_1(0)$ が $4-1=3$ つ。

**【1階の固有空間 $V^{(1)}$】**

$\lambda_2$ に属する固有ベクトル $\boldsymbol{u}^{(1)}(\lambda_2)$ を求める。  

$$
(A-0I) \boldsymbol{u}^{(1)}(\lambda_2)
=
\begin{pmatrix}
	0 & 1 & 1 & 1 & 1 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_6 = 0,\ u_5 = -u_2-u_3-u_4$ が得られるので、

$$
\boldsymbol{u}^{(1)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ -u_2-u_3-u_4 \\ 0
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ -1 \\ 0 \end{pmatrix} +
u_3 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ -1 \\ 0 \end{pmatrix} +
u_4 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ -1 \\ 0 \end{pmatrix}
\tag{4.2}
$$

**【2階の固有空間 $V^{(2)}$】**

2階の広義固有空間の基底 $\boldsymbol{u}^{(2)}(\lambda_2)$ を求める。

$$
(A-0I)^2 \boldsymbol{u}^{(2)}(\lambda_2)
=
\begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_6=0$ が得られるので、

$$
\boldsymbol{u}^{(2)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ 0
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_3 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_4 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} +
u_5 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}
\tag{4.3}
$$


**【ジョルダンブロックを生成する広義固有ベクトルの導出】**

1階・2階の固有空間 $(4.2)\ (4.3)$ を比較する。  
$\boldsymbol{u}^{(2)}(\lambda_2)$ に現れる線形独立な5つのベクトルのうち、$\boldsymbol{u}^{(1)}(\lambda_2)$ と線形独立なものを選べば、それが2階の広義固有ベクトルである。  
$\dim V^{(2)} - \dim V^{(1)} = 1$ なので1つ選ぶと、

$$
\boldsymbol{u}_1^{(2)}(\lambda_2) := (0,1,0,0,0,0)^T
\tag{4.4}
$$

このベクトルに $A$ をかけると、1つ下の階数である1階の固有ベクトルが得られる：

$$
\boldsymbol{u}_1^{(1)}(\lambda_2)
:=
A \boldsymbol{u}_1^{(2)}(\lambda_2)
=
(1,0,0,0,0,0)^T
\tag{4.5}
$$

ここまでの議論で、1〜2階の広義固有ベクトルが1つずつ求まったので、残りは1階の固有ベクトルが3つ。

$\boldsymbol{u}^{(1)}(\lambda_2)$ に現れる線形独立な4つのベクトルのうち、$\boldsymbol{u}_1^{(1)}(\lambda_2)$ と線形独立なものを3つ選べば、それが残る1階の固有ベクトルである。  
$(4.2)$ 式より、求める固有ベクトルは

$$
\begin{eqnarray}
	\boldsymbol{u}_2^{(1)}(\lambda_2) = (0,1,0,0,-1,0)^T \\
	\boldsymbol{u}_3^{(1)}(\lambda_2) = (0,0,1,0,-1,0)^T \tag{4.6} \\
	\boldsymbol{u}_4^{(1)}(\lambda_2) = (0,0,0,1,-1,0)^T
\end{eqnarray}
$$

これでジョルダンブロックを生成するベクトルが全て求まった。

**■ ジョルダン標準形とその生成行列の導出**

- $\lambda_1=1$ に属するジョルダンブロック：$J_1(1)$
- $\lambda_2=0$ に属するジョルダンブロック：$J_2(0),\ J_1(0),\ J_1(0),\ J_1(0)$

であるから、$A$ のジョルダン標準形（の1つ）は

$$
J = J_1(1) \oplus J_2(0) \oplus J_1(0) \oplus J_1(0) \oplus J_1(0)
=
\begin{pmatrix}
	\color{red}{1} & 0 & 0 & 0 & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{1} & 0 & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{0} & 0 & 0 & 0 \\
	0 & 0 & 0 & \color{red}{0} & 0 & 0 \\
	0 & 0 & 0 & 0 & \color{red}{0} & 0 \\
	0 & 0 & 0 & 0 & 0 & \color{red}{0}
\end{pmatrix}
\tag{4.7}
$$

$(4.1)\ (4.4)\ (4.5)\ (4.6)$ より、ジョルダン標準形の生成行列（の1つ）を計算すると、

$$
\begin{eqnarray}
	P &=& \left(
		\boldsymbol{u}(\lambda_1)\ \middle|\ 
		\boldsymbol{u}_1^{(1)}(\lambda_2),\ 
		\boldsymbol{u}_1^{(2)}(\lambda_2)\ \middle|\ 
		\boldsymbol{u}_2^{(1)}(\lambda_2)\ \middle|\ 
		\boldsymbol{u}_3^{(1)}(\lambda_2)\ \middle|\ 
		\boldsymbol{u}_4^{(1)}(\lambda_2)
	\right)
	\\ &=&
	\left(
	\begin{array}{c|cc|c|c|c}
		5 & 1 & 0 & 0 & 0 & 0 \\
		1 & 0 & 1 & 1 & 0 & 0 \\
		1 & 0 & 0 & 0 & 1 & 0 \\
		1 & 0 & 0 & 0 & 0 & 1 \\
		1 & 0 & 0 & -1 & -1 & -1 \\
		1 & 0 & 0 & 0 & 0 & 0
	\end{array}
	\right)
\end{eqnarray}
\tag{4.8}
$$

※ 1列目・2〜3列目・4列目・5列目・6列目のブロックは入れ替え可能（ブロック内の並び替えは不可）だが、検算のため $(4.7)$ と対応する順序に合わせた。

掃き出し法により $P$ の逆行列を求めると、

$$
P^{-1} = \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 1 \\
	1 & 0 & 0 & 0 & 0 & -5 \\
	0 & 1 & 1 & 1 & 1 & -4 \\
	0 & 0 & -1 & -1 & -1 & 3 \\
	0 & 0 & 1 & 0 & 0 & -1 \\
	0 & 0 & 0 & 1 & 0 & -1
\end{pmatrix}
$$

これらを用いて $P^{-1}AP$ を計算すると、

$$
P^{-1}AP = \begin{pmatrix}
	1 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 1 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$

となり、$J$ に一致する。


### 【5】7次・6重解

$$
A = \begin{pmatrix}
	0 & -1 & 1 & 0 & 0 & -1 & 1 \\
	0 & 0 & 0 & 1 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 & -1 \\
	0 & 0 & 0 & 0 & 0 & 0 & -1 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
$$

$A$ の固有多項式は

$$
\det (A-\lambda I) =
\det
\begin{pmatrix}
	-\lambda & -1 & 1 & 0 & 0 & -1 & 1 \\
	0 & -\lambda & 0 & 1 & 0 & 0 & 1 \\
	0 & 0 & -\lambda & 0 & 0 & 1 & -1 \\
	0 & 0 & 0 & -\lambda & 0 & 0 & -1 \\
	0 & 0 & 0 & 0 & 1-\lambda & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & -\lambda & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & -\lambda \\
\end{pmatrix}
=
\lambda^6(1-\lambda)
$$

なので、
- 固有値は $\lambda_1 = 1, \lambda_2 = 0$
- それぞれの重複度は $r_1 = 1, r_2 = 6$

**■ 固有値ごとのジョルダン細胞と生成ベクトル**

**○ $\lambda_1 = 1$ について**

重複度 $r_1 = 1$ なので、固有ベクトルがジョルダン細胞 $J_1(1)$ を与える。

$$
(A - \lambda I) \boldsymbol{u}
=
\begin{pmatrix}
	-1 & -1 & 1 & 0 & 0 & -1 & 1 \\
	0 & -1 & 0 & 1 & 0 & 0 & 1 \\
	0 & 0 & -1 & 0 & 0 & 1 & -1 \\
	0 & 0 & 0 & -1 & 0 & 0 & -1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & -1 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & -1 \\
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6 \\ u_7\end{pmatrix}
= \boldsymbol{0}
$$

を解くと、

$$u_1=u_2=u_3=u_4=u_6=u_7=0$$

よって $\lambda_1$ に属する固有ベクトル $\boldsymbol{u}(\lambda_1)$ は、

$$
\boldsymbol{u}(\lambda_1) = u_5 \begin{pmatrix}
	0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0
\end{pmatrix}
\tag{5.1}
$$


**○ $\lambda_2 = 0$ について**

重複度 $r_2=6\gt 1$ なので、対角化できるとは限らず、ジョルダン細胞の大きさを調べる必要がある。

行基本変形を用いて、$\lambda_2=0$ に属する $k$ 階の広義固有空間 $V^{(k)}$ の次元を調べていく。

$$
\begin{eqnarray}
\dim V^{(1)} &=& 7-\mathrm{rank}(A-0I)
\\ &=&
7-\mathrm{rank} \begin{pmatrix}
	0 & -1 & 1 & 0 & 0 & -1 & 1 \\
	0 & 0 & 0 & 1 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 1 & -1 \\
	0 & 0 & 0 & 0 & 0 & 0 & -1 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
=
7-\mathrm{rank} \begin{pmatrix}
	0 & -1 & 1 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 1 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 1 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
\\ &=& 7-5 = 2
\\
\\
\dim V^{(2)} &=& 7-\mathrm{rank}(A-0I)^2
\\ &=&
7-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & -1 & 0 & 1 & -3 \\
	0 & 0 & 0 & 0 & 0 & 0 & -1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
=
7-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & -1 & 0 & 1 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
\\ &=& 7-3 = 4
\\
\\
\dim V^{(3)} &=& 7-\mathrm{rank}(A-0I)^3
\\ &=&
7-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 0 & 2 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\\ &=& 7-2 = 5
\\
\\
\dim V^{(4)} &=& 7-\mathrm{rank}(A-0I)^4
\\ &=&
7-\mathrm{rank} \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\\ &=& 7-1 = 6
\end{eqnarray}
$$

$\dim V^{(4)} = r_2$ となったので、$V^{(5)}$ 以上について調べる必要はない。

| $k$ | $\dim V^{(k)}$ | $\dim V^{(k)}-\dim V^{(k-1)}$<br>$= k$ 階の広義固有ベクトルの個数<br>$=k$ 以上のサイズのジョルダンブロック数 |
| :-- | :-- | :-- |
| 0 | 0 | - |
| 1 | 2 | 2 |
| 2 | 4 | 2 |
| 3 | 5 | 1 |
| 4 | 6 | 1 |

表より、$\lambda_2=0$ に属するジョルダンブロックは $J_4(0)$ が1つ、$J_2(0)$ が $2-1=1$ つ。


**【1階の固有空間 $V^{(1)}$】**

$\lambda_2$ に属する固有ベクトル $\boldsymbol{u}^{(1)}(\lambda_2)$ を求める。  

$$
(A-0I) \boldsymbol{u}^{(1)}(\lambda_2)
=
\begin{pmatrix}
	0 & -1 & 1 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 1 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 1 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6 \\ u_7\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_4 = u_5 = u_6 = u_7 = 0,\ u_2 = u_3$ が得られるので、

$$
\boldsymbol{u}^{(1)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_2 \\ 0 \\ 0 \\ 0 \\ 0
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}
\tag{5.2}
$$

**【2階の固有空間 $V^{(2)}$】**

2階の広義固有空間の基底 $\boldsymbol{u}^{(2)}(\lambda_2)$ を求める。

$$
(A-0I)^2 \boldsymbol{u}^{(2)}(\lambda_2)
=
\begin{pmatrix}
	0 & 0 & 0 & -1 & 0 & 1 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6 \\ u_7\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_5=u_7=0,\ u_6=u_4$ が得られるので、

$$
\boldsymbol{u}^{(2)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ 0 \\ u_4 \\ 0
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_3 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_4 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} 
\tag{5.3}
$$


**【3階の固有空間 $V^{(3)}$】**

3階の広義固有空間の基底 $\boldsymbol{u}^{(3)}(\lambda_2)$ を求める。

$$
(A-0I)^3 \boldsymbol{u}^{(3)}(\lambda_2)
=
\begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 0 & 2 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6 \\ u_7\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_5=u_7=0$ が得られるので、

$$
\boldsymbol{u}^{(3)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ 0 \\ u_6 \\ 0
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_3 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_4 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_6 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}
\tag{5.4}
$$


**【4階の固有空間 $V^{(4)}$】**

4階の広義固有空間の基底 $\boldsymbol{u}^{(4)}(\lambda_2)$ を求める。

$$
(A-0I)^4 \boldsymbol{u}^{(4)}(\lambda_2)
= \begin{pmatrix}
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}u_1 \\ u_2 \\ u_3 \\ u_4 \\ u_5 \\ u_6 \\ u_7\end{pmatrix}
= \boldsymbol{0}
$$

を解くと $u_5=0$ が得られるので、

$$
\boldsymbol{u}^{(4)}(\lambda_2) = \begin{pmatrix}
	u_1 \\ u_2 \\ u_3 \\ u_4 \\ 0 \\ u_6 \\ u_7
\end{pmatrix}
=
u_1 \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_2 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_3 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_4 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} +
u_6 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} +
u_7 \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
\tag{5.5}
$$

**【ジョルダンブロックを生成する広義固有ベクトルの導出】**

3階・4階の固有空間 $(5.4)\ (5.5)$ を比較する。  
$\boldsymbol{u}^{(4)}(\lambda_2)$ に現れる線形独立な6つのベクトルのうち、$\boldsymbol{u}^{(3)}(\lambda_2)$ と線形独立なものを選べば、それが4階の広義固有ベクトルである。  
$\dim V^{(4)} - \dim V^{(3)} = 1$ なので1つ選べば良く、条件を満たすのは

$$
\boldsymbol{u}_1^{(4)}(\lambda_2) := (0,0,0,0,0,0,1)^T
\tag{5.6}
$$

のみ。  
このベクトルに $A$ をかけるたび、1つ下の階数の固有ベクトルが得られる：

$$
\begin{eqnarray}
	\boldsymbol{u}_1^{(3)}(\lambda_2)
	&:=&
	A \boldsymbol{u}_1^{(4)}(\lambda_2)
	&=&
	(1,1,-1,-1,0,1,0)^T
	\\
	\boldsymbol{u}_1^{(2)}(\lambda_2)
	&:=&
	A \boldsymbol{u}_1^{(3)}(\lambda_2)
	&=&
	(-3,-1,1,0,0,0,0)^T
	\tag{5.7}
	\\
	\boldsymbol{u}_1^{(1)}(\lambda_2)
	&:=&
	A \boldsymbol{u}_1^{(2)}(\lambda_2)
	&=&
	(2,0,0,0,0,0,0)^T
\end{eqnarray}
$$

ここまでの議論で、1〜4階の広義固有ベクトルが1つずつ求まったので、残りは2階と1階の広義固有ベクトルが1つずつ。

よって、次に1階・2階の固有空間 $(5.2)\ (5.3)$ を比較する。  
$\boldsymbol{u}^{(2)}(\lambda_2)$ に現れる線形独立な4つのベクトルのうち、$\boldsymbol{u}^{(1)}(\lambda_2)$ および $\boldsymbol{u}_1^{(2)}(\lambda_2)$ と線形独立なものを1つ選べば、それが残る2階の広義固有ベクトルである。

$$
\boldsymbol{u}_2^{(2)}(\lambda_2) := (0,0,0,1,0,1,0)^T
\tag{5.8}
$$

を選ぶと、このベクトルに $A$ をかけることで1階の固有ベクトルを得る：

$$
\boldsymbol{u}_2^{(1)}(\lambda_2)
:=
A \boldsymbol{u}_1^{(4)}(\lambda_2)
=
(-1,1,1,0,0,0,0)^T
\tag{5.9}
$$

これでジョルダンブロックを生成するベクトルが全て求まった。

**■ ジョルダン標準形とその生成行列の導出**

- $\lambda_1=1$ に属するジョルダンブロック：$J_1(1)$
- $\lambda_2=0$ に属するジョルダンブロック：$J_4(0),\ J_2(0)$

であるから、$A$ のジョルダン標準形（の1つ）は

$$
J = J_1(1) \oplus J_4(0) \oplus J_2(0) =
\begin{pmatrix}
	\color{red}{1} & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{1} & \color{red}{0} & \color{red}{0} & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{0} & \color{red}{1} & \color{red}{0} & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{0} & \color{red}{0} & \color{red}{1} & 0 & 0 \\
	0 & \color{red}{0} & \color{red}{0} & \color{red}{0} & \color{red}{0} & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & \color{red}{0} & \color{red}{1} \\
	0 & 0 & 0 & 0 & 0 & \color{red}{0} & \color{red}{0} \\
\end{pmatrix}
\tag{5.10}
$$

$(5.1)\ (5.6)\ (5.7)\ (5.8)\ (5.9)$ より、ジョルダン標準形の生成行列（の1つ）を計算すると、

$$
\begin{eqnarray}
	P &=& \left(
		\boldsymbol{u}(\lambda_1)\ \middle|\ 
		\boldsymbol{u}_1^{(1)}(\lambda_2),\ 
		\boldsymbol{u}_1^{(2)}(\lambda_2),\ 
		\boldsymbol{u}_1^{(3)}(\lambda_2),\ 
		\boldsymbol{u}_1^{(4)}(\lambda_2)\ \middle|\ 
		\boldsymbol{u}_2^{(1)}(\lambda_2),\ 
		\boldsymbol{u}_2^{(2)}(\lambda_2)
	\right)
	\\ &=&
	\left(
	\begin{array}{c|cccc|cc}
		0 & 2 & -3 & 1 & 0 & -1 & 0 \\
		0 & 0 & -1 & 1 & 0 & 1 & 0 \\
		0 & 0 & 1 & -1 & 0 & 1 & 0 \\
		0 & 0 & 0 & -1 & 0 & 0 & 1 \\
		1 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 1 & 0 & 0 & 1 \\
		0 & 0 & 0 & 0 & 1 & 0 & 0
	\end{array}
	\right)
\end{eqnarray}
\tag{5.11}
$$

※ 1列目・2〜5列目・6〜7列目のブロックは入れ替え可能（ブロック内の並び替えは不可）だが、検算のため $(10)$ と対応する順序に合わせた。

掃き出し法により $P$ の逆行列を求めると、

$$
P^{-1} = \begin{pmatrix}
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0.5 & -0.5 & 1 & -0.5 & 0 & 0.5 & 0 \\
	0 & -0.5 & 0.5 & -0.5 & 0 & 0.5 & 0 \\
	-0 & -0 & -0 & -0.5 & -0 & 0.5 & -0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0.5 & 0.5 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0.5 & 0 & 0.5 & 0
\end{pmatrix}
$$

これらを用いて $P^{-1}AP$ を計算すると、

$$
P^{-1}AP = \begin{pmatrix}
	1 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 1 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 1 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 1 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
	0 & 0 & 0 & 0 & 0 & 0 & 1 \\
	0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\end{pmatrix}
$$

となり、$J$ に一致する。

```python
P = np.matrix([
		[1, 0, 0, 0, 0, 5],
        [0, 1, -1, -1, -1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1]])
```

```python
import numpy as np

def to_tex(A_):
	ret = r'\begin{pmatrix}' + '\n'
	for r in A_:
		row = np.array(r)[0]
		ret += '\t'
		ret += ' & '.join([str(a) for a in row])
		ret += r' \\' + '\n'
	ret += r'\end{pmatrix}'
	print(ret.replace('.0 ', ' ').replace('-0 ', '0 '))

A = np.matrix([[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1]])

P = np.matrix([[0, 0, 0, 1, 0, -5],
[-1, -1, -1, 0, 1, -1],
[0, 0, 1, 0, 0, -1],
[0, 1, 0, 0, 0, -1],
[1, 0, 0, 0, 0, -1],
[0, 0, 0, 0, 0, -1]])

Pinv = np.matrix([[0, 0, 0, 0, 1, -1],
[0, 0, 0, 1, 0, -1],
[0, 0, 1, 0, 0, -1],
[1, 0, 0, 0, 0, -5],
[0, 1, 1, 1, 1, -4],
[0, 0, 0, 0, 0, -1]])

J = np.matrix([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1]])

to_tex(A)
to_tex(J)
to_tex(P)
to_tex(Pinv)
```


# 性質

## 変換可能性


