---
title: Dickey-Fuller 検定
title-en: Dickey-Fuller Testing
---

# Dickey-Fuller 検定

注目する時系列データに[自己回帰モデル](../../../DataMining/time-series/models/autoregressive-model.md)を適用するとき、それが[単位根](../../../DataMining/time-series/unit-root-process.md)を持つかどうかを調べる検定。

## 理論

時系列 $r_t$ に対し、一次の自己回帰モデル $\mathrm{AR}(1)$ を適用する。

$$
r_t = \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
\tag{1}
$$

両辺から $r_{t-1}$ を引いて $\Delta r_t = r_t - r_{t-1}$ と置くと、

$$
\Delta r_t = \phi_0 + (\phi_1-1) r_{t-1} + \varepsilon_t
\tag{2}
$$

- 帰無仮説 $H_0$：時系列 $r_t$ が単位根を持つ（$\phi_1 = 1$）
- 対立仮説 $H_1$：時系列 $r_t$ が単位根を持たず（$|\phi_1| < 1$）、弱定常である

（ToDo：検定統計量と分布について記載 → 分かりやすい分布による検定はできない？？）



# ADF 検定

Dickey-Fuller 検定の拡張。


## 実験

```python
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

def generate(phi0, phi1, sigma, n):
	es = np.random.normal(size=n-1)
	r = [0.0 if phi1==1.0 else phi0/(1.0-phi1)]  # 定常な AR(1) モデルの期待値を初期値に設定
	for e in es:
		r.append(phi0 + phi1*r[-1] + e)
	return r

def my_dftest(r):
	dftest = adfuller(r)
	print('ADF Statistic   : %f' % dftest[0])
	print('p-value         : %f' % dftest[1])
	print('Critical values :')
	for k, v in dftest[4].items():
		print('\t', k, v)

def func(phi0, phi1, sigma, n):
	r = generate(phi0=phi0, phi1=phi1, sigma=sigma, n=n)
	my_dftest(r)
	plt.plot(range(n), r)
	plt.title(r'$\phi_0={}, \phi_1={}, \sigma={}$'.format(phi0, phi1, sigma))
	plt.show()

func(phi0=1, phi1=0.7, sigma=0.5, n=300)
"""
ADF Statistic   : -6.710218
p-value         : 0.000000
Critical values :
	 1% -3.4524113009049935
	 5% -2.8712554127251764
	 10% -2.571946570731871
"""
func(phi0=1, phi1=0.9, sigma=0.5, n=300)
"""
ADF Statistic   : -3.672402
p-value         : 0.004519
Critical values :
	 1% -3.4524113009049935
	 5% -2.8712554127251764
	 10% -2.571946570731871
"""
func(phi0=1, phi1=0.99, sigma=0.5, n=300)
"""
ADF Statistic   : -1.095170
p-value         : 0.716994
Critical values :
	 1% -3.4524113009049935
	 5% -2.8712554127251764
	 10% -2.571946570731871
"""
func(phi0=1, phi1=1.0, sigma=0.5, n=300)
"""
ADF Statistic   : -0.079003
p-value         : 0.951490
Critical values :
	 1% -3.4525611751768914
	 5% -2.87132117782556
	 10% -2.5719816428028888
"""
```

| ![Figure_1](https://user-images.githubusercontent.com/13412823/245361312-35cb8ea8-0d98-443a-b9e3-06d2a056147b.png)<br>$p = 0.000000$ | ![Figure_2](https://user-images.githubusercontent.com/13412823/245361321-0a6c3c9c-80a8-410a-a513-161917af2d8b.png)<br>$p = 0.004519$ |
| :--: | :--: |
| ![Figure_3](https://user-images.githubusercontent.com/13412823/245361327-f2c31635-6b90-4553-84a6-ddea99f298cf.png)<br>$p = 0.716994$ | ![Figure_4](https://user-images.githubusercontent.com/13412823/245361329-567db1e7-b536-438c-855d-ef8badc6a357.png)<br>$p = 0.951490$ |

