---
title: 適合度の検定・独立性の検定
title-en: Hypothesis Testing for Goodness of Fit and Independence
---

# 適合度の検定・独立性の検定

## 適合度の検定

> **【問題設定】**
> 
> - 前提
> 	- すべてのデータはカテゴリ $c_1, \cdots, c_k$ のいずれか1つに属する
> 	- 標本数 $n$ が十分大きい
> - 調べたいこと
> 	- 実測したデータの分布が期待する分布と一致するか

### 理論

> **【定理】ピアソンの定理**
> 
> $k$ 個のカテゴリ $c_1, \cdots, c_k$ があり、母集団から取得した標本が全て、一定の確率でいずれか1つのカテゴリに属する場合を考える。
> 
> - $N_i$：標本を $n$ 件集めたとき、カテゴリ $c_i$ に属するサンプル数の実現値を表す確率変数
>   - $N_1 + \cdots + N_k = n$
> - $p_i$：カテゴリ $c_i$ にサンプルが属する理論的確率（母比率）
>   - $p_1 + \cdots + p_k = 1$
> - $\hat{p}_i$：実際の標本がカテゴリ $c_i$ に属した比率（標本比率）
>   - $\hat{p}_i := N_i / n$
> 
> とすると、**ピアソンの適合度基準**
> 
> $$
\chi^2 :=
\sum_{i=1}^k \cfrac{(N_i-np_i)^2}{np_i} =
\sum_{i=1}^k \cfrac{n(\hat{p}_i-p_i)^2}{p_i}
$$
> 
> は自由度 $k-1$ のカイ二乗分布 $\chi^2(k-1)$ に従う。

**【証明】**

$N_i$ は、確率 $p_i$ で成功する試行（抽出したサンプル1つがカテゴリ $c_i$ に属する）を $n$ 回繰り返したときの成功回数と考えられるから、

$$
N_i \sim B(n, p_i)
$$

二項分布の平均・分散はそれぞれ $E(n_i) = np_i, \ V(n_i) = np_i(1-p_i)$ で与えられ、$n$ が十分大きければ二項分布は正規分布に近似できるから、

$$
N_i \sim N(np_i, np_i(1-p_i)) \qquad\qquad (1)
$$

新しい確率変数

$$
W_i := \cfrac{N_i - np_i}{\sqrt{np_i}}
$$

を定義すると、$(1)$ および正規分布の和と積に関する再生性から、

$$
W_i \sim N(0, 1-p_i)
$$

ここで

$$
\begin{eqnarray}
	E(W_i) &=& E \left( \cfrac{N_i - np_i}{\sqrt{np_i}} \right) = \cfrac{np_i - np_i}{\sqrt{np_i}} = 0
	\\
	E(W_i W_j) &=& E \left(
		\cfrac{N_i - np_i}{\sqrt{np_i}}
		\cfrac{N_j - np_j}{\sqrt{np_j}}
	\right)
	\\ &=&
	E \left(
		\cfrac{N_i N_j - np_iN_j - np_jN_i + n^2p_ip_j}{\sqrt{n^2p_ip_j}}
	\right)
	\\ &=&
	\cfrac{E(N_iN_j) - np_iE(N_j) - np_jE(N_i) + n^2p_ip_j}{n\sqrt{p_ip_j}}
	\\ &=&
	\cfrac{E(N_iN_j) - n^2p_ip_j}{n\sqrt{p_ip_j}}
\end{eqnarray}
$$

$i = j$ のとき、$(1)$ より

$$
\begin{eqnarray}
	E(N_iN_i) &=& E(N_i^2)
	\\ &=& V(N_i) + E(N_i)^2
	\\ &=& np_i(1-p_i) + n^2p_i^2
\end{eqnarray}
$$

$i \ne j$ のとき、

$$
\begin{eqnarray}
	E(N_i N_j) &=&
	\sum_{k \ge 0, l \ge 0, k+l \le n} kl P(N_i=k,N_j=l)
	\\ &=&
	\sum_{k \ge 0, l \ge 0, k+l \le n}
	kl \cfrac{n!}{k!l!(n-(k+l))!}
	p_i^k p_j^l (1-p_i-p_j)^{n-(k+l)}
	\\ &=&
	n(n-1) p_i p_j (p_i + p_j + (1-p_i-p_j))^{n-2}
	\\ &=&
	n(n-1) p_i p_j
\end{eqnarray}
$$

よって、

$$
\begin{eqnarray}
	E(W_i W_j) &=& \begin{cases}
		\cfrac{np_i(1-p_i) + n^2p_i^2 - n^2p_i^2}{n\sqrt{p_ip_i}}
		&\qquad& i = j \\
		\cfrac{n(n-1)p_ip_j - n^2p_ip_j}{n\sqrt{p_ip_j}}
		&\qquad& i \ne j
	\end{cases}
	\\ &=&
	\begin{cases}
		1-p_i &\qquad& i=j \\
		- \sqrt{p_i p_j} &\qquad& i \ne j
	\end{cases}
\end{eqnarray}
$$

以上により、$W_i, W_j$ の共分散は

$$
\begin{eqnarray}
	\mathrm{Cov}(W_i, W_j)
	&=&
	E(W_i W_j) - E(W_i)E(W_j)
	\\ &=&
	E(W_iW_j) - 0 \cdot 0
	\\ &=&
	\begin{cases}
		1-p_i &\qquad& i=j \\
		- \sqrt{p_i p_j} &\qquad& i \ne j
	\end{cases}
\end{eqnarray}
$$

[分散共分散行列](../variance-covariance-matrix.md) $\Sigma_{ij} = \mathrm{Cov}(W_i, W_j)$ を考える。対称行列 $A_{ij} = \sqrt{p_ip_j}$ を定義すると、

$$
\Sigma = I - A
$$

と書ける。ただし、$I$ は単位行列。

（ToDo：続き）

> **【NOTE】**
> 
> $(1)$ より $Z_1, \cdots, Z_k$ は全て標準正規分布に従うため、$\sum_{i=1}^{k} Z_i^2$ を $\chi^2(k)$ にしたがう検定統計量とみなして良さそうに思える。  
> しかし、制約 $N_1 + \cdots + N_k = n$、$p_1 + \cdots + p_k = 1$ より、$n_1, \cdots, n_k$ のうち $k-1$ 個が決まれば残り1つは一意に定まり、$p_1, \cdots, p_k$ についても同様のことが言える。  
> よって $Z_1, \cdots, Z_k$ についても $k-1$ 個が決まれば残り1つが一意に決まるため、これらは独立な確率変数にならない。  
> したがって、$\sum_{i=1}^{k} Z_i^2$ は $\chi^2(k)$ に従わない。

> **【NOTE】$k=2$ のときのピアソンの定理の証明**
> 
> 一般の $k$ の場合は大変だが、$k=2$ の場合は証明が容易で、感覚的にも理解しやすい。
>
> $(1)$ を標準化して変数 $Z_i$ を定義すると、
> 
> $$
Z_i := \cfrac{N_i - np_i}{\sqrt{np_i(1-p_i)}} \sim N(0, 1)
$$
> 
> $N_i, p_i$ に関する制約
> 
> $$
N_1 + N_2 = n, \qquad p_1 + p_2 = 1
$$
> 
> より $\chi^2$ を計算すると、
> 
> $$
\begin{eqnarray}
	\chi^2 &=&
	\cfrac{(N_1-np_1)^2}{np_1} + \cfrac{(N_2-np_2)^2}{np_2}
	\\ &=&
	\cfrac{(N_1-np_1)^2}{np_1} + \cfrac{((n-N_1)-n(1-p_1))^2}{n(1-p_1)}
	\\ &=&
	\cfrac{(N_1-np_1)^2}{np_1} + \cfrac{(N_1-np_1)^2}{n(1-p_1)}
	\\ &=&
	\cfrac{(N_1-np_1)^2}{np_1(1-p_1)}
	\\ &=&
	\left(\cfrac{N_1-np_1}{\sqrt{np_1(1-p_1)}}\right)^2
	\\ &=&
	Z_1^2
\end{eqnarray}
$$
> 
> $Z_1 \sim N(0,1)$ なので、
> 
> $$
\chi^2 = Z_1^2 \sim \chi^2(1)
$$



### 具体例

日本人の血液型の比率は $\mathrm{A}:\mathrm{O}:\mathrm{B}:\mathrm{AB} = 4:3:2:1$ であると言われる。  
ある小学校の生徒100人を無作為に選んで血液型を調べたとき、その分布は以下のようになっていた。

| 血液型 | 人数 |
| :-- | :-- |
| A | 52 |
| O | 19 |
| B | 22 |
| AB | 7 |

有意水準を 5% として、この学校の血液型の分布は日本人の平均的な分布に一致すると言えるか。

#### 帰無仮説・対立仮説の設定

- 帰無仮説 $H_0$：この学校の血液型分布は日本人の平均的な分布に一致する
- 対立仮説 $H_1$：この学校の血液型分布は日本人の平均的な分布に一致しない

#### 検定統計量の選定

カテゴリ数は4なので、

- $p_A, p_O, p_B, p_{AB}$：各血液型の母比率
- $n_A, n_O, n_B, n_{AB}$：各血液型の標本数

とすると、帰無仮説 $H_0$ 下では、ピアソンの適合度基準

$$
\chi^2 = \sum_{i=A,O,B,AB} \cfrac{(n_i-np_i)^2}{np_i}
$$

は自由度 $4-1 = 3$ のカイ二乗分布に従う。  
これを検定統計量として用いる。

#### 棄却域の計算

帰無仮説 $H_0$ が棄却されるのは、実際の分布と平均的な分布とのズレが大きい場合。  
そのため、カイ二乗分布 $\chi^2(3)$ による片側検定を行う。  
有意水準 $\alpha = 0.05$ であるから、$\chi^2$ が自由度3のカイ二乗分布の上側5%点 $\chi_{0.05}^2$ 以上の範囲にあれば、帰無仮説 $H_0$ は棄却される。

自由度3のカイ二乗分布表より $\chi^2_{0.05} = 7.82$ と求まるので、帰無仮説 $H_0$ の棄却域は

$$
7.82 \le \chi^2
$$

#### 検定統計量の計算

母比率・標本比率は以下のようになるので、帰無仮説 $H_0$ が正しいと仮定すると

| 血液型 | 人数 | 母比率 $p$ |
| :-- | :-- | :-- |
| A | 52 | 0.4 |
| O | 19 | 0.3 |
| B | 22 | 0.2 |
| AB | 7 | 0.1 |
| 合計 | 100 | 1.0 |

$$
\begin{eqnarray}
	\chi^2 &=& \sum_{i=A,O,B,AB} \cfrac{(n_i-np_i)^2}{np_i}
	\\ &=&
	\cfrac{(52-40)^2}{40} + \cfrac{(19-30)^2}{30} +
	\cfrac{(22-20)^2}{20} + \cfrac{(7-10)^2}{10}
	\\ &\simeq&
	8.73
\end{eqnarray}
$$

これは棄却域に含まれるので、帰無仮説 $H_0$ は棄却される。

#### 結論

この学校生徒の血液型分布は、日本人の平均的な分布と比べて有意な差が見られる。


## 独立性の検定

> **【問題設定】**
> 
> - 前提
> 	- すべてのデータは複数の分類基準（ex. 性別と血液型）ごとに1つずつのカテゴリに属する
> 	- 標本数 $n$ が十分大きい
> - 調べたいこと
> 	- 複数の分類基準の間に関連性があるか

### 理論


|  | A 型 | O 型 | B 型 | AB 型 | (合計) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 男性 | 55 | 22 | 16 | 7 |  |
| 女性 | 40 | 32 | 24 | 4 |  |
| (合計) |  |  |  |  |  |

### 具体例