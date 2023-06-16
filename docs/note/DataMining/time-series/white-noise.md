---
title: ホワイトノイズ（白色雑音）
title-en: White Noise
---

# 定義

時系列 $\{\varepsilon_1, \cdots, \varepsilon_T\}$ が

$$
\begin{eqnarray}
	E(\varepsilon_t) &=& 0
	\\
	V(\varepsilon_t) &=& \sigma^2 = \mathrm{const.}
	\\
	\mathrm{Cov}(\varepsilon_t, \varepsilon_{t+h}) &=& 0
\end{eqnarray}
$$

を満たすとき、この時系列を **ホワイトノイズ（白色雑音）** と呼び、

$$
\varepsilon_t \sim \mathrm{W.N.}(\sigma^2)
$$

と書く。


# 特徴

- 分布が完全なランダムで、別の時点のデータに影響を受けない
- どの時点においても分散が一定