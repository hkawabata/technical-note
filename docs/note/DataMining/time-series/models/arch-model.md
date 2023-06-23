---
title: ARCH モデル
title-en: ARCH model
---

# 概要

## ARCH モデル

以下を満たす時系列データモデルを **ARCH モデル** と呼び、$\mathrm{ARCH}(p)$ で表す。  
= AutoRegressive Conditional Heteroscedasticity

$$
\begin{eqnarray}
	r_t &=& \mu + \varepsilon_t
	\tag{1}
	\\ \\
	\varepsilon_t &=& \sigma_t \nu_t
	\qquad (\nu_t \sim N(0,1))
	\tag{2}
	\\ \\
	E(\varepsilon_t^2) &=& \sigma_t^2 = \omega + \sum_{i=1}^p \alpha_i \varepsilon_{t-i}^2
	\qquad (\omega \gt 0,\ \ \alpha_i \ge 0)
	\tag{3}
\end{eqnarray}
$$

$\mu$ は定数でも良いし、自己回帰モデル $\mathrm{AR}(k)$ などのモデルを適用しても良い。

ARCH モデルの考え方：**近い過去のタイムステップに大きなノイズが来たら、次のステップでも大きな変動が起こる確率が高い**

ex. ある企業の株価が大きく下がると、翌日の市場では「次は上がると信じてたくさん買う」「これ以上損したくないのでたくさん売る」のように大きな変動が起こりがち

式の解釈：

- $(1)$：現在の値 = 期待値+現在のノイズ
- $(2)$：現在のノイズ = 条件付き標準偏差 x ホワイトノイズ
- $(3)$：条件付き分散 = 定数パラメータ + 過去 $p$ ステップまでの(重み x ノイズの二乗)の和
	- $p$ は「現在に影響を与える過去のノイズは何ステップ分か？」を表す

ARCH モデルにおける $E(\varepsilon_t^2) = V(\varepsilon_t) + E(\varepsilon_t)^2 = \sigma_t^2$ は変動の大きさを表し、**ボラティリティ** と呼ばれる。

株価等の金融分析において、**ボラティリティは重要なリスク指標となる**。


## GARCH モデル

ARCH モデルを一般化した以下のモデルを **GARCH モデル** (= Generalized ARCH) と呼び、$\mathrm{GARCH}(p,q)$ で表す。

$$
\begin{eqnarray}
	r_t &=& \mu + \varepsilon_t
	\tag{1}
	\\ \\
	\varepsilon_t &=& \sigma_t \nu_t
	\qquad (\nu_t \sim N(0,1))
	\tag{2}
	\\ \\
	E(\varepsilon_t^2) &=& \sigma_t^2 = \omega +
	\sum_{i=1}^p \alpha_i \varepsilon_{t-i}^2 +
	\sum_{i=1}^q \beta_i \sigma_{t-i}^2
	\qquad (\omega \gt 0,\ \ \alpha_i, \beta_i \ge 0)
	\tag{4}
\end{eqnarray}
$$

$(3)$ 式が $(4)$ 式に置き換わっており、**過去のノイズ（残差）に加えて、過去のノイズの分散も現在のノイズの分散に影響を与える** モデルとなっている。


# モデルの弱定常条件

（TODO：証明）

$\mathrm{ARCH}(p)$ が弱定常過程となる条件は、特性方程式

$$
1- \sum_{i=1}^p \alpha_i z^i = 0
$$

の全ての解の絶対値が1より大きくなること。これは $\alpha_i \ge 0$ の条件下では

$$
\sum_{i=1}^p \alpha_i \lt 1
$$

と同値。

同様に、$\mathrm{GARCH}(p,q)$ が弱定常過程となる条件は

$$
\sum_{i=1}^p \alpha_i + \sum_{i=1}^q \beta_i \lt 1
$$


# モデルの適用・パラメータ推定

例として、$\mathrm{AR}(1)$ と $\mathrm{ARCH}(1)$ の組み合わせモデルを例にパラメータ推定を行う。

$$
\begin{eqnarray}
	r_t &=& \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
	\tag{5}
	\\ \\
	\varepsilon_t &=& \nu_t \sqrt{ \omega + \alpha_1 \varepsilon_{t-1}^2 }
	\qquad (\nu_t \sim N(0,1))
	\tag{6}
\end{eqnarray}
$$

## 理論

1. $\mathrm{AR}(1)$ モデルのパラメータ $\phi_0, \phi_1$ を推定 by 最尤推定（最小二乗法）
2. $\mathrm{ARCH}(1)$ モデルのパラメータ $\omega, \alpha_1$ を推定 by 最尤推定

という **二段階推定** を行う。


### AR(1) のパラメータ推定

まずは通常の $\mathrm{AR}(1)$ モデルとして考え、誤差を正規分布とみなした最尤推定（最小二乗法）により $\phi_0, \phi_1$ の推定値 $\hat{\phi}_0, \hat{\phi}_1$ を計算する。  
詳細な理論は[自己回帰モデル](autoregressive-model.md)を参照。


### ARCH(1) のパラメータ推定

$\hat{\phi}_0, \hat{\phi}_1$ が求まったので、各タイムステップの残差 $\varepsilon_2, \cdots, \varepsilon_T$ を計算する。

$$
\varepsilon_t = r_t - \hat{\phi}_0 - \hat{\phi}_1 r_{t-1}
$$

ここで、$(6)$ より

$$
\varepsilon_t \sim N(0, \omega + \alpha_1 \varepsilon_{t-1}^2)
$$

であるから、$\omega, \alpha_1, \varepsilon_{t-1}$ が与えられたときに $\varepsilon_t$ が得られる条件付き確率は、

$$
f(\varepsilon_t | \omega, \alpha_1, \varepsilon_{t-1})
=
\cfrac{1}{\sqrt{2\pi(\omega + \alpha_1 \varepsilon_{t-1}^2)}}
\exp\left(
	- \cfrac{\varepsilon_t^2}{2 (\omega + \alpha_1 \varepsilon_{t-1}^2)}
\right)
$$

よって ${\varepsilon_2, \cdots, \varepsilon_T}$ の同時確率は、

$$
\begin{eqnarray}
	L(\omega, \alpha_1) := f(\varepsilon_2, \cdots, \varepsilon_T | \omega, \alpha_1)
	&=&
	\prod_{t=3}^T f(\varepsilon_t | \omega, \alpha_1, \varepsilon_{t-1})
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-1}
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\omega + \alpha_1 \varepsilon_{t-1}^2}}
	\exp\left(
		- \cfrac{1}{2}
		\cfrac{ \varepsilon_t^2 }{\omega + \alpha_1 \varepsilon_{t-1}^2 }
	\right)
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-1}
	\exp\left(
		- \cfrac{1}{2}
		\sum_{t=3}^T
		\cfrac{ \varepsilon_t^2 }{\omega + \alpha_1 \varepsilon_{t-1}^2 }
	\right)
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\omega + \alpha_1 \varepsilon_{t-1}^2}}
\end{eqnarray}
$$

これを尤度関数とみなし、最大化するためのパラメータを求める。

対数を取ると、

$$
l(\omega, \alpha_1) := \log L(\omega, \alpha_1)
=
- (T-1) \log \sqrt{2\pi}
- \cfrac{1}{2}
\sum_{t=3}^T
\cfrac{ \varepsilon_t^2 }{\omega + \alpha_1 \varepsilon_{t-1}^2 }
- \cfrac{1}{2} \sum_{t=3}^T \log (\omega + \alpha_1 \varepsilon_{t-1}^2)
$$

$l(\omega, \alpha_1)$ が最大値を取る時、

$$
\begin{eqnarray}
	\cfrac{\partial l(\omega, \alpha_1)}{\partial \omega}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{ \varepsilon_t^2 }{(\omega + \alpha_1 \varepsilon_{t-1}^2)^2 }
	- \cfrac{1}{2} \sum_{t=3}^T \cfrac{1}{\omega + \alpha_1 \varepsilon_{t-1}^2}
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{ \varepsilon_t^2 - \omega - \alpha_1 \varepsilon_{t-1}^2 }{(\omega + \alpha_1 \varepsilon_{t-1}^2)^2 }
	= 0
	\\
	\cfrac{\partial l(\omega, \alpha_1)}{\partial \alpha_1}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{ \varepsilon_{t-1}^2 \varepsilon_t^2 }{(\omega + \alpha_1 \varepsilon_{t-1}^2)^2 }
	- \cfrac{1}{2} \sum_{t=3}^T \cfrac{\varepsilon_{t-1}^2}{\omega + \alpha_1 \varepsilon_{t-1}^2}
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{ \varepsilon_{t-1}^2(\varepsilon_t^2 - \omega - \alpha_1 \varepsilon_{t-1}^2) }{(\omega + \alpha_1 \varepsilon_{t-1}^2)^2 }
	= 0
\end{eqnarray}
$$

これを $\omega, \alpha_1$ について解析的に解くのは難しい。  
そのため、勾配法・ニュートン法などの数値的な手法を用いて、$l(\omega, \alpha_1)$ を最大化する $\omega, \alpha_1$ を求める。

※ $l(\omega, \alpha_1)$ の定数項 $- (T-1) \log \sqrt{2\pi}$ はパラメータに依存しないため、最大化問題を考える上では取り除いて計算して良い。  


## 実験

### 実験データの生成

$\phi_0 = 1.3,\ \phi_1 = 0.7,\ \alpha_1 = 0.5,\ \omega = 0.3$ の条件で機械的に $\mathrm{AR}(1)+\mathrm{ARCH}(1)$ モデルのデータを生成。

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_generate.py %}

![Figure_1](https://user-images.githubusercontent.com/13412823/247385982-048a5684-d065-476a-8033-87a6141c653a.png)


### 二段階推定によるパラメータ推定

生成したデータに対して二段階推定を適用し、パラメータを推定する。

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_estimate.py %}

パラメータの推定値：実際の値に近い推定値を得られている

| パラメータ | 実際の値 | 推定値 | 誤差 |
| :-- | :-- | :-- | :-- |
| $\phi_0$ | 1.3 | 1.265 | -2.68% |
| $\phi_1$ | 0.7 | 0.708 | +1.09% |
| $\alpha_1$ | 0.5 | 0.480 | -3.93% |
| $\omega$ | 0.3 | 0.290 | -3.45% |

パラメータ / 尤度関数の収束：epoch 数が増えるとともに収束してく様子が分かる

![Figure_2](https://user-images.githubusercontent.com/13412823/247450712-65d095c5-5890-4513-8e5b-4feaddc10bf5.png)

対数尤度関数と最大化パス：局所最適解ではなく、正しく最大値を与えるパラメータを求めることができていそう

![Figure_3](https://user-images.githubusercontent.com/13412823/247453430-9d474c84-3aec-4292-aae6-ec0e8c755794.png)
