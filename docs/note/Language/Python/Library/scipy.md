---
title: SciPy
---

# 概要

数学・科学・工学のための数値解析ソフトウェア。

| サブモジュール | 用途 |
|:--|:--|
|scipy.cluster|クラスター分析|
|scipy.constants|物理定数|
|scipy.fft|離散フーリエ変換|
|scipy.integrate|数値積分|
|scipy.interpolate|補間|
|scipy.io|データ入出力|
|scipy.linalg|線形代数|
|scipy.misc|その他ルーチン|
|scipy.ndimage|多次元画像処理|
|scipy.odr|直交距離回帰|
|scipy.optimize|数理最適化|
|scipy.signal|信号処理|
|scipy.sparse|疎行列|
|scipy.spatial|空間的データ構造とアルゴリズム|
|scipy.special|特別機能|
|scipy.stats|統計分布|

# インストール

```bash
$ pip install scipy
```


# 使い方

## 数理最適化 scipy.optimize

```python
import scipy.optimize as opt

def objective_func(params, arg1, arg2, ...):
	p1 = params[0]
	p2 = params[1]
	p3 = params[2]
	...
	return ...

result = opt.minimize(fun=objective_func,           # 最小化したい目的関数
					  x0=[0.5, 0.5, 0.5],  # 推測対象のパラメータ初期値
					  args=(...),          # fun の第二引数以降
					  bounds=((1e-3, 1.0),(1e-3, 1.0),(1e-3, 1.0)) # 各パラメータの取りうる範囲（上限・下限）
					  )
```

例：

与えられたデータ点から回帰直線 $y=ax+b$ を求めるため、残差平方和

$$
f(a, b) = \sum_i (y_i-ax_i-b)^2
$$

を最小化する $a, b$ を求める。

```python
import numpy as np
import scipy.optimize as opt
from matplotlib import pyplot as plt

N = 20
a, b = 2, -4
x = np.random.rand(N) * 10
y = a * x + b + np.random.normal(0, 1.0, N)

def objective_func(params, x, y):
	a = params[0]
	b = params[1]
	return ((y-a*x-b)**2).sum()

result = opt.minimize(fun=objective_func, x0=[1.0,1.0], args=(x,y),
					 bounds=((None, None), (None, None)))

print(result.x)
# [ 1.90845014 -3.56271663]

plt.scatter(x, y)
plt.plot(np.arange(10), result.x[0]*np.arange(10)+result.x[1])
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/249348155-106bb16b-cbd2-4ddf-af3f-eecf273015ba.png)


## 統計分布 scipy.stats

```python
import numpy as np
import scipy.stats as stats

# 確率密度関数 Probability Density Function
stats.norm.pdf(x=0, loc=2.0, scale=1.0)
stats.t.pdf(x=0, df=5)
stats.chi2.pdf(x=1.0, df=3)
# 累積確率密度関数 Cumulative Distribution Function
stats.norm.cdf(x=0, loc=2.0, scale=1.0)
stats.t.cdf(x=0, df=5)
stats.chi2.cdf(x=1.0, df=3)
# ランダム生成 Random VariableS
stats.norm.rvs(loc=0, scale=1, size=[4,3])
stats.t.rvs(df=5, size=[4,3])
stats.chi2.rvs(df=3, size=[4,3])
```

他にも各種分布の取り扱いが可能。

| 分布 | モジュール | パラメータ |
| :-- | :-- | :-- |
| 正規分布 | `stats.norm` | `loc`：期待値<br>`scale`：標準偏差 |
| t 分布 | `stats.t` | `df`：自由度 (degree of freedom) |
| カイ二乗分布 | `stats.chi2` | `df`：自由度 |
| F 分布 | `stats.f` | `dfn`：分子自由度 (numerator degree of freedom)<br>`dfd`：分母自由度 (denominator degree of freedom) |
| ベータ分布 | `stats.beta` | `a, b` |
| ガンマ分布 | `stats.gamma` | `a` |
| 一様分布 | `stats.uniform` | `loc=0, scale=1.0`<br>`loc` 〜 `loc+scale` の範囲の一様分布 |
| ベルヌーイ分布 | `stats.bernoulli` | `p` |
| 二項分布 | `stats.binom` | `n, p` |
| ポアソン分布 | `stats.poisson` | `mu` |
