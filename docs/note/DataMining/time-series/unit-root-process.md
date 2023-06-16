---
title: 単位根過程
title-en: Unit Root Process
---

# 単位根過程

## 定義・定式化

ある時系列 $S = \{r_1, \cdots, r_T\}$ に関して以下が成り立つとき、その時系列を **単位根過程** と呼ぶ。

- $S$ 自体は[定常過程](stationary-process.md)ではない
- $S$ の差分を取った $\Delta S = \{r_2-r_1, r_3-r_2, \cdots, r_T-r_{T-1}\}$ が定常過程である


これを定式化すると、
$$
r_t = \phi_0 + r_{t-1} + \varepsilon_t
\tag{1}
$$

差分 $\Delta r_t := r_t - r_{t-1}$ を用いると、

$$
\Delta r_t = \phi_0 + \varepsilon_t
\tag{2}
$$

とも書ける。

$(1)$ を再帰的に過去のステップにさかのぼると、

$$
r_t = (t-1) \phi_0 + r_1 + \sum_{k=2}^t \varepsilon_k
\tag{3}
$$


## ランダムウォーク

$\phi_0 = 0$ の場合を **ランダムウォーク過程** と呼び、$(1)$ は

$$
r_t = r_{t-1} + \varepsilon_t
\tag{4}
$$

となる。

再帰的に過去のステップにさかのぼると、

$$
r_t = r_1 + \sum_{k=2}^t \varepsilon_k
\tag{5}
$$

これは初期値にホワイトノイズの和を足したもの。


## 自己回帰モデルとの関係

$\mathrm{AR}(1)$ モデル（cf. [自己回帰モデル](models/autoregressive-model.md)）

$$
r_t = \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
$$

における、$\phi_1 = 1$ の場合が単位根過程 $(1)$ になる。




> **【NOTE】単位根が重要である理由**
> 
> - $\mathrm{AR}(1)$ モデルにおける、$|\phi_1| > 1$ のケースでは、値が無限大に発散する。現実世界で無限大に発散するデータはほぼ存在しないため、これを考慮する必要はない。しかし $\phi_1=1$については、 $\phi_0 = 0$ であれば平均値は発散しないが、分散は発散するため、分析の対象外かどうか判断しにくい
> - 例えば株価と大気中CO2濃度は、いずれも時間とともに増加する傾向にある。本来関係のないこれら2つの間に相関性を導き出してしまう「[見せかけの回帰](spurious-regression.md)」の原因となるため、相関を調べたい時系列が単位根過程かどうかを事前に調べる必要がある。


## 単位根の検定

単位根を持つかどうかの検定手法として [Dickey-Fuller 検定](../../Math/statistics/hypothesis-testing/dickey-fuller-testing.md)（拡張版は **ADF 検定**）がある。


## 時間経過と値のばらつき

$(3)$ より、$t$ が十分大きい時、中心極限定理により

$$
r_t = (t-1) \phi_0 + r_1 + \sum_{k=2}^t \varepsilon_k \sim N((t-1) \phi_0 + r_1, (t-1) \sigma^2)
$$

したがって $t$ が大きくなるにつれて、$r_t$ の期待値と分散は増大していく（ただし、$\phi_0=0$ のランダムウォークにおいては期待値は一定）。

$t=1000$ までの過程を $N=1000$ 回実験して、
- 各試行の時系列をプロット
- $t=10, 100, 1000$ の時点の標本平均、標本標準偏差を計算

| ランダムウォーク $(\phi_0 = 0)$ | 一般の単位根過程 $(\phi_0 \ne 0)$ |
| :-- | :-- |
| ![Figure_1](https://user-images.githubusercontent.com/13412823/246478290-f0b79d44-06f2-42f3-ba52-90da736281f9.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/246478302-61252bfd-b881-4667-bc36-f1f2ca363b28.png) |
| $\bar{r}_{10} = -0.051, \bar{r}_{100} = -0.295, \bar{r}_{1000} = 0.687$ <br> $V(r_{10}) = 8.80, V(r_{100}) = 101.71, V(r_{1000}) = 1013.34$ | $\bar{r}_{10} = 2.719, \bar{r}_{100} = 29.642, \bar{r}_{1000} = 298.137$ <br> $V(r_{10}) = 9.39, V(r_{100}) = 103.21, V(r_{1000}) = 1071.25$ |

→ 理論通りの平均、分散が得られた。

```python
import numpy as np
from matplotlib import pyplot as plt

def generate(phi0, sigma, n):
	r = [0]
	rand = np.random.normal(0, sigma, n-1)
	for i in range(n-1):
		r.append(r[-1]+phi0+rand[i])
	return r


N = 1000
N_check = np.array(range(1,10+1))*100-1
T = 1000
sigma=1.0
#phi0 = 0
phi0 = 0.3


result = []
for i in range(T):
	result.append(generate(phi0, sigma, N))

result = np.array(result)

plt.title(r'$\phi_0={}, \sigma={}$'.format(phi0, sigma))
plt.xlabel('Time steps', fontsize=14)
plt.ylabel('$r_t$', fontsize=14)
for t in range(T):
	plt.plot(range(N), result[t], lw=0.1, color='blue')

plt.plot(range(N), result.mean(axis=0), color='red', label='average')

std = result.std(axis=0)
ave = result.mean(axis=0)
plt.errorbar(N_check, ave[N_check], yerr=std[N_check],
			 ecolor='black', markeredgecolor = "black", color='w',
			 lw=0.7,
			 capsize=5, fmt='o', label=r'$\pm 1 \sigma$')

plt.legend()
plt.show()

print(ave[[9,99,999]])
# [  2.71907164  29.64150098 298.13659285]
print(std[[9,99,999]])
# [ 3.06399715 10.15863065 32.72955234]
```


