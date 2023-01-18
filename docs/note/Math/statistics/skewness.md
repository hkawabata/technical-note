---
title: 歪度
title-en: skewness
---

# 歪度とは

確率分布の左右対称性を表す指標。

確率変数 $X$ の期待値を $\mu$、標準偏差を $\sigma$ として、

$$
E\left( \left( \cfrac{X - \mu}{\sigma} \right)^3 \right) =
\cfrac{1}{n} \displaystyle \sum_{i=1}^{n} \left( \cfrac{X_i - \mu}{\sigma} \right)^3
$$

で定義される。$X$ を標準化した確率変数

$$
Z \equiv \cfrac{X - \mu}{\sigma}
$$

を導入すれば、$Z$ の3次のモーメントの形で表現することもできる：

$$
E(Z^3) = M'''_Z(0)
$$

cf. [モーメント母関数](moment-generating-function.md)

# 解釈

$\left( \cfrac{X - \mu}{\sigma} \right)^3$ の値は、
- $X$ が平均値よりも大きければ大きいほど、絶対値の大きな正の値を取る
- $X$ が平均値よりも小さければ小さいほど、絶対値の大きな負の値を取る

平均値からの遠さを3乗することで、平均値から遠いデータが指標に与える寄与率を高くしている。
これにより、
- 平均値から正の方向に大きく離れたデータが多い → 歪度は絶対値の大きな正の値に
- 平均値から負の方向に大きく離れたデータが多い → 歪度は絶対値の大きな負の値に

後述の具体例のように、正の方向に裾野が長いと歪度は正になる。

# 具体例

| $\mathrm{skew} \gt 0$ | $\mathrm{skew} \lt 0$ | $\mathrm{skew} = 0$ |
| :--: | :--: | :--: |
| ![Figure_1](https://user-images.githubusercontent.com/13412823/211734961-20285fa9-858d-4cf3-9e79-0eea9d200fef.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/211734957-2c4e2c16-b5e4-40df-b05c-50629aa526f6.png) | ![Figure_3](https://user-images.githubusercontent.com/13412823/211734949-7969ac1c-4ba7-4f58-9cff-50bbc70c3793.png)

（描画に使った Python コード）
```python
import numpy as np
import scipy
import math
from matplotlib import pyplot as plt

def plot_beta(a, b, n, dx):
    # ベータ分布に従う乱数の生成
	x = np.random.beta(a, b, n)
	# 統計量の計算
	ave = np.average(x)
	skew = scipy.stats.skew(x)
	x_max, x_min = np.max(x), np.min(x)
	# 度数分布表の描画
	n_bins = int((x_max - x_min) / dx)
	plt.title(r'Beta Distribution ($\alpha = {}, \beta = {}$), skew = {:.4f}'.format(a, b, skew))
	plt.hist(x, bins=n_bins, density=True)
	plt.axvline(ave, color='red', label='average = {:.4f}'.format(ave))
	# ベータ関数の描画
	B = math.gamma(a) * math.gamma(b) / math.gamma(a + b)
	x_beta = np.linspace(x_min, x_max, 1000)
	beta = x_beta**(a-1) * (1-x_beta)**(b-1) / B
	plt.plot(x_beta, beta)
	plt.legend()
	plt.show()

plot_beta(2, 7, 10000, 0.01)
plot_beta(7, 2, 10000, 0.01)
plot_beta(7, 7, 10000, 0.01)
```

