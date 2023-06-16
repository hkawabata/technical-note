---
title: Ljung-Box 検定
title-en: Ljung-Box Testing
---

# Ljung-Box 検定

Ljung-Box = リュング・ボックス

注目する時系列データにおいて、[自己相関](../correlation/autocorrelation.md)があるかどうかを調べる検定。


## 理論

長さ $n$ の時系列データ $S_0 = \{x_1, \cdots, x_n\}$ と、そこから一定時間（= ラグ）$h$ だけずらしたデータ $S_h = \{x_{1+h}, \cdots, x_{n+h}\}$ との相関係数 $r_h$（自己相関係数）の計算式は以下の通り。

$$
r_h = \cfrac{
	\displaystyle
	\sum_{k=1}^n (x_k - \bar{x}) (x_{k+h} - \bar{x})
}{
    \displaystyle
    \sqrt{
	    \sum_{k=1}^n (x_k-\bar{x})^2
    }
    \sqrt{
	    \sum_{k=1}^n (x_{k+h}-\bar{x})^2
    }
}
\tag{1}
$$

ラグ $h$ の上限 $m$ を決め、$h = 1, \cdots, m$ それぞれに対して自己相関係数 $r_1, \cdots, r_m$ を計算し、以下のように重みを付けて二乗和を取った $Q_{BP}(m), Q_{LB}(m)$ をそれぞれ **Box-Pierce 検定統計量**、**Ljung-Box 検定統計量** と呼ぶ。

$$
\begin{eqnarray}
	Q_{BP}(m) &:=& n \sum_{h=1}^m r_h^2
	\tag{2}
	\\
	Q_{LB}(m) &:=& n(n+2) \sum_{h=1}^m \cfrac{r_h^2}{n-h}
	\tag{3}
\end{eqnarray}
$$

Ljung-Box 検定統計量 $(3)$ は、Box-Pierce 検定統計量 $(2)$ の修正版（時系列長 $n$ が小さい場合にも使える）となっている。  
データが平均0の同じ分布に従い、自己相関がなく完全にランダムであると仮定する場合（= **ヌルモデル**）、時系列の長さ $n$ が十分大きければ、これらの検定統計量は自由度 $m$ のカイ二乗分布に従う（証明：後述の NOTE を参照）。

この性質を用いて、

- 帰無仮説 $H_0$：Ljung-Box 統計量がカイ二乗分布に従う = 時系列に自己相関がない
- 対立仮説 $H_1$：Ljung-Box 統計量はカイ二乗分布に従わない = 時系列に自己相関がある

として、片側カイ二乗検定を行う。  
事前に決めた有意水準において対立仮説が採択された場合、**時系列データに自己相関がある**と結論づける。

> **【NOTE】Ljung-Box 検定の課題：ラグ $h$ の上限である $m$ の選択が難しい**
> 
> - $m$ が小さすぎる場合：高次の相関を見逃す
> - $m$ が大きすぎる場合：検出力が低下する
> 
> → 実用的な場面では、複数の $m$ に対して Ljung-Box 統計量を計算し、総合的に判断するのが一般的


> **【NOTE】$Q_{BP}$ がカイ二乗分布に従うことの証明**
> 
> 注目する時系列データの任意のデータ点が母平均 $E(x_k) = 0$、母分散 $V(x_k) = \sigma^2$ のヌルモデルに従うとする。  
> $n$ が十分大きいとき、標本平均・標本分散は母平均・母分散に近づくから、
> 
> $$
\begin{eqnarray}
	\sum_{k=1}^n (x_k-\bar{x})^2 &\simeq& n V(x_k) = n \sigma^2
	\\
	\sum_{k=1}^n (x_{k+h}-\bar{x})^2 &\simeq& n V(x_{k+h}) = n \sigma^2
	\\
	\sum_{k=1}^n (x_k - \bar{x}) (x_{k+h} - \bar{x})
	&\simeq&
	\sum_{k=1}^n (x_k - E(x_k)) (x_{k+h} - E(x_{k+h}))
	=
	\sum_{k=1}^n x_k x_{k+h}
\end{eqnarray}
$$
> 
> これらを $(1)$ に代入して、
> 
> $$
r_h \simeq \cfrac{1}{n \sigma^2} \sum_{k=1}^n x_k x_{k+h}
$$
> 
> ここで、$x_k,\ x_{k+h}$ は互いに独立であるから、独立な確率変数の積に関する期待値・分散の公式より、
> 
> $$
\begin{eqnarray}
	E(x_k x_{k+h}) &=& E(x_k) E(x_{k+h}) = 0
	\\
	\\
	V(x_k x_{k+h}) &=& V(x_k) V(x_{k+h}) + E(x_k)^2 V(x_{k+h}) + E(x_{k+h})^2 V(x_k)
	\\ &=&
	\sigma^2 \cdot \sigma^2 + 0^2 \cdot \sigma^2 + 0^2 \cdot \sigma^2
	\\ &=&
	\sigma^4
\end{eqnarray}
$$
> 
> $n$ が十分大きいとき、[中心極限定理](../central-limit-theorem.md)により、
> 
> $$
\begin{eqnarray}
	& \cfrac{1}{n} \sum_{k=1}^n x_k x_{k+h} &\sim N \left( E(x_k x_{k+h}), \cfrac{V(x_k x_{k+h})}{n} \right)
	\\ \Longrightarrow \ &
	\cfrac{1}{n} \sum_{k=1}^n x_k x_{k+h} &\sim N \left( 0, \cfrac{\sigma^4}{n} \right)
\end{eqnarray}
$$
> 
> したがって、
> 
> $$
\begin{eqnarray}
	& r_h \simeq \cfrac{1}{n \sigma^2} \sum_{k=1}^n x_k x_{k+h}
	\sim N \left( 0, \cfrac{1}{n} \right)
	\\ \Longrightarrow \ &
	\sqrt{n}\ r_h \sim N(0,1)
\end{eqnarray}
$$
> 
> となる。
> 
> $$
Q_{BP}(m) = n \sum_{h=1}^m r_h^2 = \sum_{h=1}^m \left(\sqrt{n}\ r_h \right)^2
$$
> 
> であるから、$Q_{BP}(m)$ は標準正規分布 $N(0,1)$ に従う独立な $m$ 個の確率変数 $\sqrt{n}\ r_1, \cdots, \sqrt{n}\ r_m$ の平方和で表せる。ゆえに
> 
> $$
Q_{BP}(m) \sim \chi^2 (m)
$$


## 実験

### 自己相関あり・なしデータの比較

```python
from matplotlib import pyplot as plt
import numpy as np
import statsmodels.api as sm

def ljungbox(d, lags):
	result = sm.stats.acorr_ljungbox(d,lags=lags)
	print(result)


n = 1000
d_random = np.random.normal(0, 1.0, n)  # 完全ランダムなデータ
d_acorr = np.zeros(n)                   # 自己相関を持つデータ
for i in range(n):
	if i < 3:
		d_acorr[i] = d_random[i]
	else:
		d_acorr[i] = d_random[i] + 0.5 * d_random[i-3]



ljungbox(d_random, 5)
"""
    lb_stat  lb_pvalue
1  1.412350   0.234667
2  1.424601   0.490514
3  5.484168   0.139589
4  6.407541   0.170710
5  7.193854   0.206618
"""
ljungbox(d_acorr, 5)
"""
      lb_stat     lb_pvalue
1    2.118131  1.455641e-01
2    2.527147  2.826422e-01
3  210.852281  1.905388e-45
4  215.427317  1.806495e-45
5  215.707116  1.234344e-44
"""
```

- ランダムデータではラグ1〜5いずれにおいても p 値が大きい
	- 1%や5%といった一般的な有意水準では帰無仮説は棄却されない
- 自己相関ありのデータではラグ3以上において p 値が非常に小さい
	- 一般的な有意水準で見れば帰無仮説は棄却され、自己相関ありという検定結果が得られる


### ライブラリを使わず実装

```python
x = np.array([1.2,3.1,2.1,5.9,2.8,9.1,4.1,11.9])

x_ave = x.mean()

q = 0
for lag in range(1, 8):
	T = len(x)
	d1 = x[:T-lag]
	d2 = x[lag:]
	r = ((d1-x_ave)*(d2-x_ave)).sum() / ((x-x_ave)**2).sum()
	q += r**2 * T * (T+2) / (T-lag)  # Ljung-Box 検定統計量
	print(lag, r, q)

"""
1 -0.11001309909076905 0.13831865110348995
2 0.5101068474854883 3.607771929124599
3 -0.2783107309806339 4.847081736788196
4 0.09644526634817903 5.03311552480762
5 -0.34844223557815784 8.270768632399738
6 -0.09961730107361173 8.667712899327363
7 -0.27016874711049466 14.507005052547715
"""

ljungbox(x,7)
"""
     lb_stat  lb_pvalue
1   0.138319   0.709958
2   3.607772   0.164658
3   4.847082   0.183343
4   5.033116   0.283916
5   8.270769   0.141931
6   8.667713   0.193146
7  14.507005   0.042865
"""
```

→ statsmodel による $Q_{LB}$ の計算結果と自分で計算した結果が一致。