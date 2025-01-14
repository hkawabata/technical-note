---
title: GARCH モデル
title-en: GARCH model
---

# 概要

時系列データ $r_t$ について、[ARCH モデル](arch-model.md)を一般化した以下のモデルを **GARCH モデル** (= Generalized ARCH) と呼び、$\mathrm{GARCH}(p,q)$ で表す。

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
	\tag{3}
\end{eqnarray}
$$

$(3)$ は GARCH モデルの分散の式であり、ARCH モデルの分散の式

$$
E(\varepsilon_t^2) = \sigma_t^2 = \omega + \sum_{i=1}^p \alpha_i \varepsilon_{t-i}^2
\qquad (\omega \gt 0,\ \ \alpha_i \ge 0)
\tag{4}
$$

と比べて、**過去のノイズ（残差）だけでなく、過去のノイズの分散も現在のノイズの分散に影響を与える** モデルとなっている。


# モデルの弱定常条件【WIP】

（TODO：証明）

$\mathrm{ARCH}(p)$ と同様に、$\mathrm{GARCH}(p,q)$ が弱定常過程となる条件は

$$
\sum_{i=1}^p \alpha_i + \sum_{i=1}^q \beta_i \lt 1
\tag{5}
$$

で表される。


# パラメータ推定の理論【WIP】

パラメータ推定の理論に関する良い文献が見つからない。
尤度関数の計算までは色々な記事に書かれているが、その後どうするのか。
- 二段階推定で、条件付き分散の値を得る方法
- 条件付き分散の微分の計算

cf. [分散の初期化方法](https://stats.stackexchange.com/questions/133286/initial-value-of-the-conditional-variance-in-the-garch-process)

ここでは例として、$\mathrm{AR}(1)$ と $\mathrm{GARCH}(1,1)$ の組み合わせモデルを例にパラメータ推定を行う。

$$
\begin{eqnarray}
	r_t &=& \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
	\tag{6}
	\\ \\
	\varepsilon_t &=& \sigma_t \nu_t
	\qquad (\nu_t \sim N(0,1))
	\tag{7}
	\\ \\
	\sigma_t^2 &=& \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2
	\tag{8}
\end{eqnarray}
$$

$(8)$ 式を再帰的に展開していくと、

$$
\begin{eqnarray}
	\sigma_t^2
	&=&
	\omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2
	\\ &=&
	\omega + \alpha \varepsilon_{t-1}^2 + \beta (\omega + \alpha \varepsilon_{t-2}^2 + \beta \sigma_{t-2}^2)
	\\ &=&
	\omega + \alpha \varepsilon_{t-1}^2 +
	\beta (\omega + \alpha \varepsilon_{t-2}^2) +
	\beta^2 (\omega + \alpha \varepsilon_{t-3}^2 + \beta \sigma_{t-3}^2)
	\\ &=&
	\cdots
	\\ &=&
	(\omega + \alpha \varepsilon_{t-1}^2) +
	\beta (\omega + \alpha \varepsilon_{t-2}^2) +
	\beta^2 (\omega + \alpha \varepsilon_{t-3}^2) +
	\cdots +
	\beta^{t-3} (\omega + \alpha \varepsilon_2^2) +
	\beta^{t-2} \sigma_2^2
	\\ &=&
	\sum_{i=1}^{t-2} \beta^{i-1} (\omega + \alpha \varepsilon_{t-i}^2) +
	\beta^{t-2} \sigma_2^2
	\\ &=&
	\sum_{i=2}^{t-1} \beta^{t-i-1} (\omega + \alpha \varepsilon_i^2) +
	\beta^{t-2} \sigma_2^2
\end{eqnarray}
$$

$\sigma_t^2$ の初期値 $\sigma_2^2$ はデータから計算できないので、ここでは $\varepsilon_2^2$ で近似する（他にもいくつか初期値の決め方があるらしい）：

$$
\begin{eqnarray}
	\sigma_t^2
	&\simeq&
	\sum_{i=1}^{t-2} \beta^{i-1} (\omega + \alpha \varepsilon_{t-i}^2) +
	\beta^{t-2} \varepsilon_2^2
	\\ &=&
	\sum_{i=2}^{t-1} \beta^{t-i-1} (\omega + \alpha \varepsilon_i^2) +
	\beta^{t-2} \varepsilon_2^2
\end{eqnarray}
$$

$\sigma_t^2$ を $\omega,\ \alpha,\ \beta$ で微分すると、

$$
\begin{eqnarray}
	\cfrac{\partial \sigma_t^2}{\partial \omega}
	&=&
	\sum_{i=1}^{t-2} \beta^{i-1}
	=
	\cfrac{1-\beta^{t-2}}{1-\beta}
	\\
	\\
	\cfrac{\partial \sigma_t^2}{\partial \alpha}
	&=&
	\sum_{i=2}^{t-1} \beta^{t-i-1} \varepsilon_i^2
	\\
	\\
	\cfrac{\partial \sigma_t^2}{\partial \beta}
	&=&
	\sum_{i=2}^{t-1} (t-i-1) \beta^{t-i-2} (\omega + \alpha \varepsilon_i^2) +
	(t-2) \beta^{t-3} \varepsilon_2^2
	\\ &=&
	\sum_{i=2}^{t-2} (t-i-1) \beta^{t-i-2} (\omega + \alpha \varepsilon_i^2) +
	(t-2) \beta^{t-3} \varepsilon_2^2
\end{eqnarray}
$$

対数尤度関数：

$$
l(\phi_0, \phi_1, \alpha, \beta, \omega)
=
- (T-2) \log \sqrt{2\pi} -
\cfrac{1}{2}
\sum_{t=3}^T
\left(
	\cfrac{ \varepsilon_t^2 (\phi_0, \phi_1) }{ \sigma_t^2 (\alpha, \beta, \omega) } +
	\log \sigma_t^2(\alpha, \beta, \omega)
\right)
$$



$$
\begin{eqnarray}
	\cfrac{\partial l(\alpha, \beta, \omega)}{\partial \omega}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{\partial \sigma_t^2}{\partial \omega}
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{1-\beta^{t-2}}{1-\beta}
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	\\
	\\
	\cfrac{\partial l(\alpha, \beta, \omega)}{\partial \alpha}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{\partial \sigma_t^2}{\partial \alpha}
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\left( \sum_{i=2}^{t-1} \beta^{t-i-1} \varepsilon_i^2 \right)
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	\\
	\\
	\cfrac{\partial l(\alpha, \beta, \omega)}{\partial \beta}
	&=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\cfrac{\partial \sigma_t^2}{\partial \beta}
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	\\ &=&
	\cfrac{1}{2}
	\sum_{t=3}^T
	\left(
		\sum_{i=2}^{t-2} (t-i-1) \beta^{t-i-2} (\omega + \alpha \varepsilon_i^2) +
	(t-2) \beta^{t-3} \varepsilon_2^2
	\right)
	\left(
		\cfrac{ \varepsilon_t^2 }{ (\sigma_t^2)^2 } -
		\cfrac{1}{\sigma_t^2}
	\right)
	
\end{eqnarray}
$$

→ 複雑すぎる気がする。考え方が間違っているのでは。


# パラメータ推定の実装・実験

## 実験データの生成

$\phi_0 = 1.3,\ \phi_1 = 0.7,\ \alpha_1 = 0.5,\ \beta_1 = 0.2,\ \omega = 0.3$ の条件で機械的に $\mathrm{AR}(1)+\mathrm{GARCH}(1,1)$ モデルのデータを生成。

{% gist b165d44328a5d9828bd56314c7a2a3d8 20230629_ar1-garch11-model_generate.py %}


## パラメータ推定：同時推定

前述の尤度関数の微分が間違っているのか計算がうまくいかないので、 尤度関数の微分を数値的に計算。

```python
import numpy as np

def loglike_ar1_garch11(r, phi0, phi1, alpha, beta, omega):
	"""
	AR(1)-GARCH(1,1)モデルの対数尤度関数
	"""
	eps_sq = (r[1:] - phi0 - phi1*r[:-1])**2
	sigma_sq = [eps_sq[0]]
	for e_sq in eps_sq[:-1]:
		sigma_sq.append(omega + alpha * e_sq + beta * sigma_sq[-1])
	l = - np.mean(eps_sq / sigma_sq + np.log(sigma_sq))  # 最小化したいのでマイナス1をかけている
	return l

d = 1e-2
eps = 1e-10
max_steps = 100000

phi0_est, phi1_est, alpha_est, beta_est, omega_est = np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand(), np.random.rand()
while alpha_est + beta_est >= 1.0:
	alpha_est, beta_est = np.random.rand(), np.random.rand()

ls = [loglike_ar1_garch11(r, phi0_est, phi1_est, omega_est, alpha_est, beta_est)]
for i in range(max_steps):
	phi0_est  += (loglike_ar1_garch11(r, phi0_est+d, phi1_est, omega_est, alpha_est, beta_est) - ls[-1])
	phi1_est  += (loglike_ar1_garch11(r, phi0_est, phi1_est+d, omega_est, alpha_est, beta_est) - ls[-1])
	omega_est += (loglike_ar1_garch11(r, phi0_est, phi1_est, omega_est+d, alpha_est, beta_est) - ls[-1])
	alpha_est += (loglike_ar1_garch11(r, phi0_est, phi1_est, omega_est, alpha_est+d, beta_est) - ls[-1])
	beta_est  += (loglike_ar1_garch11(r, phi0_est, phi1_est, omega_est, alpha_est, beta_est+d) - ls[-1])
	ls.append(loglike_ar1_garch11(r, phi0_est, phi1_est, omega_est, alpha_est, beta_est))
	if np.abs(ls[-1]-ls[-2]) < eps:
		print('{} step で収束しました'.format(i))
		break
	if i % 1000 == 0:
		print(i, ls[-1], phi0_est, phi1_est, omega_est, alpha_est, beta_est)
```

## パラメータ推定：同時推定 (SciPy)

{% gist b165d44328a5d9828bd56314c7a2a3d8 20230629_ar1-garch11-model_estimate_scipy.py %}

```
phi0  = 1.326121955597641 (error: 2.0093811998185274 %)
phi1  = 0.7003553862320409 (error: 0.050769461720128514 %)
alpha = 0.4964593598411822 (error: -0.7081280317635552 %)
beta  = 0.3303489105814988 (error: 10.116303527166268 %)
omega = 2.1402121185193836 (error: -2.71763097639166 %)
```

```python
>>> stats.shapiro(err)
ShapiroResult(statistic=0.9507026672363281, pvalue=0.0)
>>> stats.shapiro(nu)
ShapiroResult(statistic=0.9998607635498047, pvalue=0.8367221355438232)
```