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
\tag{4}
$$


# パラメータ推定の理論

ここでは例として、$\mathrm{AR}(1)$ と $\mathrm{ARCH}(1)$ の組み合わせモデルを例にパラメータ推定を行う。

$$
\begin{eqnarray}
	r_t &=& \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
	\tag{5}
	\\ \\
	\varepsilon_t &=& \sigma_t \nu_t
	\qquad (\nu_t \sim N(0,1))
	\tag{6}
	\\ \\
	\sigma_t^2 &=& \omega + \alpha \varepsilon_{t-1}^2
	\tag{7}
\end{eqnarray}
$$

推定の手法としては

- 二段階推定
- 同時推定

の2通りの方法がある。


## 二段階推定

1. $\mathrm{AR}(1)$ モデルのパラメータ $\phi_0, \phi_1$ を推定 by 最尤推定（最小二乗法）
2. $\mathrm{ARCH}(1)$ モデルのパラメータ $\omega, \alpha$ を推定 by 最尤推定

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
\varepsilon_t \sim N(0, \sigma_t^2(\omega, \alpha))
$$

であるから、$\omega, \alpha, \varepsilon_{t-1}$ が与えられたときに $\varepsilon_t$ が得られる条件付き確率は、

$$
f(\varepsilon_t | \omega, \alpha, \varepsilon_{t-1})
=
\cfrac{1}{\sqrt{2\pi \sigma_t^2(\omega, \alpha)}}
\exp\left(
	- \cfrac{\varepsilon_t^2}{2 \sigma_t^2(\omega, \alpha)}
\right)
\tag{8}
$$

よって ${\varepsilon_3, \cdots, \varepsilon_T}$ の同時確率は、

$$
\begin{eqnarray}
	L(\omega, \alpha) &:=& f(\varepsilon_3, \cdots, \varepsilon_T | \omega, \alpha)
	\\ &=&
	\prod_{t=3}^T f(\varepsilon_t | \omega, \alpha, \varepsilon_{t-1})
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-2}
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\sigma_t^2(\omega, \alpha)}}
	\exp\left(
		- \cfrac{1}{2}
		\cfrac{ \varepsilon_t^2 }{\sigma_t^2(\omega, \alpha)}
	\right)
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-2}
	\exp\left(
		- \cfrac{1}{2}
		\sum_{t=3}^T
		\cfrac{ \varepsilon_t^2 }{\sigma_t^2(\omega, \alpha)}
	\right)
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\sigma_t^2(\omega, \alpha)}}
	\tag{9}
\end{eqnarray}
$$

> **【NOTE】**
> 
> $\varepsilon_{t-1}$ の表式には $r_{t-2}$ が現れるため、和は $3 \le t$ について取っている。

これを尤度関数とみなし、最大化するためのパラメータを求める。

対数を取ると、

$$
\begin{eqnarray}
	l(\omega, \alpha_1) &:=& \log L(\omega, \alpha_1)
	\\ &=&
	- (T-2) \log \sqrt{2\pi}
	- \cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{ \varepsilon_t^2 }{\sigma_t^2(\omega, \alpha)}
	- \cfrac{1}{2} \sum_{t=3}^T \log \sigma_t^2(\omega, \alpha)
	\\ &=&
	- (T-2) \log \sqrt{2\pi}
	- \cfrac{1}{2}
	\sum_{t=3}^T
	\left\{
		\cfrac{ \varepsilon_t^2 }{\sigma_t^2(\omega, \alpha)} +
		\log \sigma_t^2(\omega, \alpha)
	\right\}
	\tag{10}
\end{eqnarray}
$$

$l(\omega, \alpha_1)$ が最大値を取る時、

$$
\begin{eqnarray}
	\cfrac{\partial l(\omega, \alpha)}{\partial \omega}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{\partial \sigma_t^2}{\partial \omega}
	\left\{
		\cfrac{ \varepsilon_t^2 }{(\sigma_t^2(\omega, \alpha))^2} -
		\cfrac{1}{\sigma_t^2(\omega, \alpha)}
	\right\}
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{ \varepsilon_t^2 }{(\sigma_t^2(\omega, \alpha))^2} -
		\cfrac{1}{\sigma_t^2(\omega, \alpha)}
	\right\}
	= 0
	\\
	\cfrac{\partial l(\omega, \alpha)}{\partial \alpha}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{\partial \sigma_t^2}{\partial \alpha}
	\left\{
		\cfrac{ \varepsilon_t^2 }{(\sigma_t^2(\omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2(\omega, \alpha)}
	\right\}
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T \varepsilon_{t-1}^2 \left\{
		\cfrac{ \varepsilon_t^2 }{(\sigma_t^2(\omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2(\omega, \alpha)}
	\right\}
	= 0
\end{eqnarray}
$$

これを $\omega, \alpha$ について解析的に解くのは難しい。  
そのため、勾配法・ニュートン法などの数値的な手法を用いて、$l(\omega, \alpha)$ を最大化する $\omega, \alpha$ を求める。

※ $l(\omega, \alpha)$ の定数項 $- (T-2) \log \sqrt{2\pi}$ はパラメータに依存しないため、最大化問題を考える上では取り除いて計算して良い。  


## 同時推定

$\mathrm{AR}(1)+\mathrm{ARCH}(1)$ モデルのパラメータ $\phi_0, \phi_1, \alpha, \omega$ を同時に推定する。

同時推定では、先に $\phi_0, \phi_1$ を推定していないため、$\varepsilon_t, \varepsilon_{t-1}$ が未知。
そのため、$(8)$ をそのまま使うことができない。

しかし $(5)$ より

$$
\varepsilon_t = r_t - \phi_0 - \phi_1 r_{t-1},\quad \varepsilon_{t-1} = r_{t-1} - \phi_0 - \phi_1 r_{t-2}
$$

であるから、$\varepsilon_t, \varepsilon_{t-1}$ は既知の値 $r_t, r_{t-1}$ と推定対象のパラメータ $\phi_0, \phi_1$ で表せる：

$$
\varepsilon_t = \varepsilon_t(\phi_0, \phi_1)
$$

$\varepsilon_t$ が $\phi_0, \phi_1$ に依存するため、$\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2$ も $\phi_0, \phi_1$ に依存：

$$
\begin{eqnarray}
	\sigma_t^2 &=& \sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)
	\\ &=&
	\omega + \alpha \varepsilon_t^2(\phi_0, \phi_1)
\end{eqnarray}
$$

よって $(8)$ は、$\omega, \alpha, \phi_0, \phi_1, r_t, r_{t-1}$ が与えられたときに $\varepsilon_t(\phi_0, \phi_1)$ が得られる条件付き確率として書き換えられる：

$$
f(\varepsilon_t(\phi_0, \phi_1) | \phi_0, \phi_1, \omega, \alpha, r_t, r_{t-1})
=
\cfrac{1}{\sqrt{2\pi \sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}}
\exp\left(
	- \cfrac{\varepsilon_t^2(\phi_0, \phi_1)}{2 \sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
\right)
\tag{11}
$$

尤度関数、対数尤度関数についても $(9)(10)$ を $\varepsilon_t \to \varepsilon_t(\phi_0, \phi_1),\ \sigma_t^2 (\omega, \alpha) \to \sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)$ で書き換えればよく、

$$
\begin{eqnarray}
	L(\omega, \alpha, \phi_0, \phi_1) &:=& f(\varepsilon_2(\phi_0, \phi_1), \cdots, \varepsilon_T(\phi_0, \phi_1) | \phi_0, \phi_1, \omega, \alpha, \boldsymbol{r})
	\\ &=&
	\prod_{t=3}^T f(\varepsilon_t(\phi_0, \phi_1) | \phi_0, \phi_1, \omega, \alpha, r_t, r_{t-1})
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-2}
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}}
	\exp\left(
		- \cfrac{1}{2}
		\cfrac{ \varepsilon_t^2(\phi_0, \phi_1) }{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right)
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}} \right)^{T-2}
	\exp\left(
		- \cfrac{1}{2}
		\sum_{t=3}^T
		\cfrac{ \varepsilon_t^2(\phi_0, \phi_1) }{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right)
	\prod_{t=3}^T
	\cfrac{1}{\sqrt{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}}
	\tag{12}
	\\
	\\
	l(\omega, \alpha, \phi_0, \phi_1)
	&:=&
	\log L(\omega, \alpha_1, \phi_0, \phi_1)
	\\ &=&
	- (T-2) \log \sqrt{2\pi} -
	\cfrac{1}{2}
	\sum_{t=3}^T
	\left\{
		\cfrac{ \varepsilon_t^2(\phi_0, \phi_1) }{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)} +
		\log \sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)
	\right\}
	\tag{13}
\end{eqnarray}
$$

対数尤度を最大化するために使う $\omega, \alpha_1$ による微分についても、$\varepsilon_t$ が $\omega, \alpha_1$ によらないため、二段階推定の式の置き換えで良い：

$$
\begin{eqnarray}
	\cfrac{\partial l(\omega, \alpha, \phi_0, \phi_1)}{\partial \omega}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{ \varepsilon_t(\phi_0, \phi_1)^2 }{(\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right\}
	= 0
	\\
	\cfrac{\partial l(\omega, \alpha, \phi_0, \phi_1)}{\partial \alpha_1}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T \varepsilon_{t-1}(\phi_0, \phi_1)^2 \left\{
		\cfrac{ \varepsilon_t(\phi_0, \phi_1)^2 }{(\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right\}
	= 0
\end{eqnarray}
$$

対数尤度の $\phi_0, \phi_1$ による微分についても計算する。

$$
\begin{eqnarray}
	\cfrac{\partial \varepsilon_t^2(\phi_0, \phi_1)}{\partial \phi_0}
	&=&
	2 \varepsilon_t(\phi_0, \phi_1) \cfrac{\partial \varepsilon_t(\phi_0, \phi_1)}{\partial \phi_0}
	\\ &=&
	- 2 \varepsilon_t(\phi_0, \phi_1)
	\\
	\cfrac{\partial \varepsilon_t^2(\phi_0, \phi_1)}{\partial \phi_1}
	&=&
	2 \varepsilon_t(\phi_0, \phi_1) \cfrac{\partial \varepsilon_t(\phi_0, \phi_1)}{\partial \phi_1}
	\\ &=&
	- 2 r_{t-1} \varepsilon_t(\phi_0, \phi_1)
	\\
	\cfrac{\partial \sigma_t^2(\omega, \alpha, \phi_0, \phi_1)}{\partial \phi_0}
	&=&
	\alpha \cdot \cfrac{\partial \varepsilon_{t-1}^2(\phi_0, \phi_1)}{\partial \phi_0}
	=
	- 2 \alpha \varepsilon_{t-1}(\phi_0, \phi_1) 
	\\
	\cfrac{\partial \sigma_t^2(\omega, \alpha, \phi_0, \phi_1)}{\partial \phi_1}
	&=&
	\alpha \cdot \cfrac{\partial \varepsilon_{t-1}^2(\phi_0, \phi_1)}{\partial \phi_1}
	=
	-2 \alpha r_{t-2} \varepsilon_{t-1}(\phi_0, \phi_1)
\end{eqnarray}
$$

であるから、

$$
\begin{eqnarray}
	\cfrac{\partial l(\phi_0, \phi_1, \omega, \alpha)}{\partial \phi_0}
	&=&
	-\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{
			\cfrac{\partial \varepsilon_t^2}{\partial \phi_0}
			\sigma_t^2 -
			\varepsilon_t^2
			\cfrac{\partial \sigma_t^2}{\partial \phi_0}
		}{
			(\sigma_t^2)^2
		}
		+
		\cfrac{\partial \sigma_t^2}{\partial \phi_0}
		\cfrac{1}{\sigma_t^2}
	\right\}
	\\ &=&
	-\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{
			- 2 \varepsilon_t
			\sigma_t^2 +
			2 \alpha \varepsilon_{t-1}
			\varepsilon_t^2
		}{
			(\sigma_t^2)^2
		}
		-
		\cfrac{2 \alpha \varepsilon_{t-1}}{\sigma_t^2}
	\right\}
	\\ &=&
	\sum_{t=3}^T \left[
	\cfrac{\varepsilon_t(\phi_0, \phi_1)}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	-
	\alpha \varepsilon_{t-1}(\phi_0, \phi_1)
	\left\{
		\cfrac{ \varepsilon_t(\phi_0, \phi_1)^2 }{(\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right\}
	\right]
	\\ &=& 0
	\\
	\\
	\cfrac{\partial l(\phi_0, \phi_1, \omega, \alpha)}{\partial \phi_1}
	&=&
	-\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{
			\cfrac{\partial \varepsilon_t^2}{\partial \phi_1}
			\sigma_t^2 -
			\varepsilon_t^2
			\cfrac{\partial \sigma_t^2}{\partial \phi_1}
		}{
			(\sigma_t^2)^2
		}
		+
		\cfrac{\partial \sigma_t^2}{\partial \phi_1}
		\cfrac{1}{\sigma_t^2}
	\right\}
	\\ &=&
	-\cfrac{1}{2}
	\sum_{t=3}^T \left\{
		\cfrac{
			- 2 \varepsilon_t r_{t-1}
			\sigma_t^2 +
			2 \alpha r_{t-2} \varepsilon_{t-1}
			\varepsilon_t^2
		}{
			(\sigma_t^2)^2
		}
		-
		\cfrac{2 \alpha r_{t-2} \varepsilon_{t-1}}{\sigma_t^2}
	\right\}
	\\ &=&
	\sum_{t=3}^T \left[
	\cfrac{r_{t-1} \varepsilon_t(\phi_0, \phi_1)}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	-
	r_{t-2} \alpha \varepsilon_{t-1}(\phi_0, \phi_1)
	\left\{
		\cfrac{ \varepsilon_t(\phi_0, \phi_1)^2 }{(\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha))^2 } -
		\cfrac{1}{\sigma_t^2 (\phi_0, \phi_1, \omega, \alpha)}
	\right\}
	\right]
	\\ &=& 0
\end{eqnarray}
$$

以上の4つの微分方程式に対し、勾配法・ニュートン法などの数値的な手法を用いて $l(\omega, \alpha_1, \phi_0, \phi_1)$ を最大化するパラメータを求める。


# パラメータ推定の実装・実験

## 実験データの生成

$\phi_0 = 1.3,\ \phi_1 = 0.7,\ \alpha_1 = 0.5,\ \omega = 0.3$ の条件で機械的に $\mathrm{AR}(1)+\mathrm{ARCH}(1)$ モデルのデータを生成。

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_generate.py %}

![Figure_1](https://user-images.githubusercontent.com/13412823/249420334-4b3c6721-0522-4a37-8f2d-3bd107d58f6f.png)


## パラメータ推定：二段階推定

生成したデータに対して二段階推定を適用し、パラメータを推定する。

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_estimate_2step.py %}

パラメータの推定値：実際の値に近い推定値を得られている

```
========== Estimation Result
phi0  = 1.2454814064569888 (err: -4.193737964847019 %)
phi1  = 0.7108127831407725 (err: 1.5446833058246425 %)
alpha = 0.49184768646712124 (err: -1.6304627065757527 %)
omega = 0.29954663741689064 (err: -0.15112086103645045 %)
```

残差の正規性を確認：

- $\varepsilon_t$ は正規分布ではない
- $\nu_t$ は正規分布に従っていそう

→ よくモデルに当てはまっている

```python
stats.shapiro(err)
# ShapiroResult(statistic=0.9771683812141418, pvalue=4.263784871469905e-37)
stats.shapiro(nu)
# ShapiroResult(statistic=0.9998605251312256, pvalue=0.8355695009231567)
```

パラメータ・尤度関数の収束：epoch 数が増えるとともに収束してく様子が分かる

![Figure_2](https://user-images.githubusercontent.com/13412823/248642577-04c1ddf4-644d-4830-a961-46f240da4903.png)

対数尤度関数と最大化パス：局所最適解ではなく、正しく最大値を与えるパラメータを求めることができていそう

![Figure_3](https://user-images.githubusercontent.com/13412823/248642578-70122702-ebf9-49e4-8472-6d583a435b35.png)


## パラメータ推定：同時推定

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_estimate_concurrent.py %}

パラメータの推定値：実際の値に近い推定値を得られている

```
========== Estimation Result
phi0  = 1.2928559649768947 (err: -0.5495411556234879 %)
phi1  = 0.7021406124770047 (err: 0.30580178242924283 %)
alpha = 0.49202068041505176 (err: -1.5958639169896482 %)
omega = 0.29920945610885463 (err: -0.2635146303817856 %)
```

残差の正規性を確認：

- $\varepsilon_t$ は正規分布ではない
- $\nu_t$ は正規分布に従っていそう

→ よくモデルに当てはまっている

```python
stats.shapiro(err)
# ShapiroResult(statistic=0.9771093130111694, pvalue=3.904022902595043e-37)
stats.shapiro(nu)
# ShapiroResult(statistic=0.9998559951782227, pvalue=0.8136035799980164)
```

パラメータ・尤度関数の収束：

![Figure_4](https://user-images.githubusercontent.com/13412823/248642579-5d28c62c-162a-40c2-ba53-b4a00a47bb1c.png)


## パラメータ推定：同時推定 (SciPy)

{% gist ea0f90c43f0a4c6a8aa7b8c705b1be8a 20230621_ar1-arch1-model_estimate_scipy.py %}

```
phi0  = 1.2949697022923172 (error: -0.3869459775140629 %)
phi1  = 0.7016821234998044 (error: 0.24030335711492223 %)
alpha = 0.4920619600131017 (error: -1.5876079973796586 %)
omega = 0.29919803901173 (error: -0.2673203294233373 %)
```