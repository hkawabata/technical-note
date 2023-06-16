---
title: 定常過程
title-en: Stationarity
---

# 定常過程

時間や位置によってその確率分布が変化しない、という確率過程。  
時系列モデルにおいて重要な概念。

## 弱定常性

時系列データ $S = \{r_1, r_2, \cdots, r_T\}$ において以下が成り立つとき、$S$ は **弱定常性(weak stationary)を持つ** という。

- $r_t$ の期待値・分散が時刻 $t$ によらず一定
- $r_{t+h}$ と $r_t$ 自己共分散 $\mathrm{Cov} (r_{t+h}, r_t)$ が時刻には寄らず、ラグ $h$ にのみ依存

$$
\begin{eqnarray}
	E(r_t) &=& \mu \\
	V(r_t) &=& \gamma_0 \\
	\mathrm{Cov} (r_{t+h}, r_t) &=& \gamma_h
\end{eqnarray}
$$

全データ長が $T$ であるとき、これらの推定値は

$$
\begin{eqnarray}
	\hat{\mu} &=& \cfrac{1}{T} \sum_{t=1}^T r_t
	\\
	\hat{\gamma_0} &=& \cfrac{1}{T} \sum_{t=1}^T (r_t - \hat{\mu})^2
	\\
	\hat{\gamma_h} &=& \cfrac{1}{T} \sum_{t=1}^{T-h} (r_t-\hat{\mu}) (r_{t+h}-\hat{\mu})
\end{eqnarray}
$$

## 強定常性

任意のデータ点数 $k$、ラグ $h$ に対して、$S$ の部分列 $S_0 = \{r_1, r_2, \cdots, r_k\}$ と $S_h = \{r_{h+1}, r_{h+2}, \cdots, r_{h+k}\}$ の同時分布 $f$ が等しい、すなわち

$$
f(r_1, r_2, \cdots, r_k) = f(r_{h+1}, r_{h+2}, \cdots, r_{h+k})
$$

が成り立つとき、$S$ は **強定常性(strict stationary)を持つ** という。

言い換えれば、「長さが同じであれば、どの時点の部分列を取っても同時分布が等しい」

