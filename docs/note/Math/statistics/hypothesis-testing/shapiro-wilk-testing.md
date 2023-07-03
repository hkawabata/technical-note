---
title: Shapiro-Wilk 検定
title-en: Shapiro-Wilk testing
---

# 概要

**Shapiro-Wilk 検定** は、統計分布の正規性に対する検定手法の1つ。  
視覚的にデータの正規性を確認する手法として [QQ-plot](statistics/qq-plot.md) があるが、Shapiro-Wilk 検定では、この QQ-plot が対角線がどのくらい離れているか？を評価する。

Shapiro-Wilk = シャピロ・ウィルク

- 帰無仮説 $H_0$：母集団は正規分布に従う
- 対立仮説 $H_1$：母集団は正規分布に従わない

# 方法

母集団から抽出した $n$ 件のサンプルを $x_1, \cdots, x_n$ とする。  
ただし、これらのサンプルは小さい順に並べてラベリングし、

$$
x_1 \le x_2 \le \cdots \le x_n
\tag{1}
$$

が成り立つようにしておく。

標準正規分布 $N(0,1)$ の[順序統計量](statistics/order-statistics.md)の期待値を列ベクトル

$$
\boldsymbol{m} := (m_1, \cdots, m_n)^T
$$

で表すと、サンプルの[分散共分散行列](statistics/variance-covariance-matrix.md) $V$ は、

$$
V_{ij} = E((x_i-m_i)(x_j-m_j))
$$

この $\boldsymbol{m}, V$ を用いて計算した係数

$$
(a_1, \cdots, a_n) = \cfrac{
	\boldsymbol{m}^T V^{-1}
}{
	\displaystyle
	\sqrt{\boldsymbol{m}^T V^{-1} V^{-1} \boldsymbol{m}}
}
$$

を用いて、Shapiro-Wilk の検定統計量は、

$$
W = \cfrac{
	\left( \displaystyle \sum_{i=1}^n a_i x_i \right)^2
}{
	\displaystyle \sum_{i=1}^n (x_i - \bar{x})
}
\tag{2}
$$

と表される。

- （$W$ がどんな分布に従うのか？）
- （$\boldsymbol{m}, V$ は正規分布の順序統計量の期待値と分散共分散。計算が非常に複雑になりそうだがどう計算すれば良いのか？）


> **【NOTE】検定統計量 $W$ の意味**
> 
> 本当の正規分布からの順序統計量の期待値とサンプルの順序統計量との相関のようなもの、らしい。

R や Python では検定のためのライブラリが用意されている。

```python
import numpy as np
import scipy.stats as stats

def shapirowilk(x):
	return stats.shapiro(x)

def random_t(n, N):
	ts = []
	for i in range(N):
		x = np.random.normal(0, 1.0, n)
		t = x.mean() / np.sqrt(((x-x.mean())**2).sum() / (n-1)) * np.sqrt(n)
		ts.append(t)
	return np.array(ts)

N = 1000
xs = {
	'N(5,3)': np.random.normal(5, 3.0, N),
	'chi_sq(5)': np.random.chisquare(5, N),
	'chi_sq(20)': np.random.chisquare(20, N),
	'chi_sq(80)': np.random.chisquare(80, N),
	't(1)': random_t(1+1, N),
	't(4)': random_t(4+1, N),
	't(16)': random_t(16+1, N),
	't(64)': random_t(64+1, N)
}

for k, x in xs.items():
	print('===== {}\n{}'.format(k, stats.shapiro(x)))

"""
===== N(5,3)
ShapiroResult(statistic=0.9979013800621033, pvalue=0.24376340210437775)
===== chi_sq(5)
ShapiroResult(statistic=0.9184432625770569, pvalue=8.526575381303006e-23)
===== chi_sq(20)
ShapiroResult(statistic=0.959893524646759, pvalue=6.205465015538675e-16)
===== chi_sq(80)
ShapiroResult(statistic=0.9906898140907288, pvalue=5.834726835018955e-06)
===== t(1)
ShapiroResult(statistic=0.14431166648864746, pvalue=0.0)
===== t(4)
ShapiroResult(statistic=0.9579213261604309, pvalue=2.346669840258965e-16)
===== t(16)
ShapiroResult(statistic=0.9955364465713501, pvalue=0.005186939146369696)
===== t(64)
ShapiroResult(statistic=0.997844398021698, pvalue=0.22344598174095154)
"""
```

