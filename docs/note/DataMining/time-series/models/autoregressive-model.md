---
title: 自己回帰モデル（AR モデル）
title-en: Autoregressive Model
---

# 定義

時系列 $S=\{r_1, \cdots, r_T\}$ について、各 $r_t$ が過去 $k$ ステップまでの値 $r_{t-k}, \cdots, r_{t-1}$ に依存するモデルを **$k$ 次の自己回帰モデル（AR モデル）** といい、$\mathrm{AR}(k)$ で表す。

$$
r_t = \phi_0 + \phi_1 r_{t-1} + \cdots + \phi_k r_{t-k} + \varepsilon_t
\tag{1}
$$

ここで $\phi_0, \cdots, \phi_k$ は定数であり、$\varepsilon_t$ には[ホワイトノイズ](../white-noise.md)を仮定。

$(1)$ 式において、$\phi_0 + \phi_1 r_{t-1} + \cdots + \phi_k r_{t-k}$ 部分は過去のデータ点だけで定まり、時刻 $t$ における新しい情報を持つのは $\varepsilon_t$ のみ。

# AR(1) モデル

## 定式化

$$
r_t = \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
\tag{2}
$$

## モデルの定常性

モデルの期待値が時間経過とともに発散するようなケースは、現実世界のデータではあまり実用的ではない。  
なので、$\mathrm{AR}(1)$ が定常過程となるための条件を確認する。

$(2)$ 式を用いて再帰的に過去データに遡っていくと、

$$
\begin{eqnarray}
	r_t &=& \phi_0 + \phi_1 r_{t-1} + \varepsilon_t
	\\ &=&
	\phi_0 + \phi_1 (\phi_0 + \phi_1 r_{t-2} + \varepsilon_{t-1}) + \varepsilon_t
	\\ &=&
	\phi_0(1 + \phi_1) + \phi_1^2 r_{t-2} + (\varepsilon_t + \phi_1 \varepsilon_{t-1})
	\\ &=&
	\phi_0(1 + \phi_1) + \phi_1^2 (\phi_0 + \phi_1 r_{t-3} + \varepsilon_{t-2}) +
	(\phi_1 \varepsilon_{t-1} + \varepsilon_t)
	\\ &=&
	\phi_0(1 + \phi_1 + \phi_1^2) + \phi_1^3 r_{t-3} +
	(\varepsilon_t + \phi_1 \varepsilon_{t-1} + \phi_1^2 \varepsilon_{t-2})
	\\ &=&
	\cdots
	\\ &=&
	\phi_0 \sum_{k=0}^{p-1} \phi_1^k +
	\phi_1^p r_{t-p} +
	\sum_{k=0}^{p-1} \phi_1^k \varepsilon_{t-k}
	\tag{3}
\end{eqnarray}
$$

$(3)$ の両辺の期待値を取ると、$E(\varepsilon_t) = 0$ より

$$
\begin{eqnarray}
	E(r_t) &=&
	\phi_0 \sum_{k=0}^{p-1} \phi_1^k +
	\phi_1^p E(r_{t-p}) +
	\sum_{k=0}^{p-1} \phi_1^k E(\varepsilon_{t-k})
	\\ &=&
	\begin{cases}
		\phi_0 \cfrac{\phi_1^p-1}{\phi_1-1} + \phi_1^p E(r_{t-p}) \qquad & (\phi_1 \ne 1) \\
		\\
		\phi_0 (p-1) + E(r_{t-p}) & (\phi_1 = 1)
	\end{cases}
\end{eqnarray}
$$

$r_t$ が[定常過程](../stationary-process.md)であるためには、$p \to \infty$ としたときに $E(r_t)$ が発散しないことが必要。これを満たす条件は、$-1 \lt \phi_1 \lt 1$ あるいは $\phi_1 = 1, \phi_0 = 0$

次に $(3)$ の両辺の分散を取る。  
右辺の確率変数 $r_{t-p}$ と $\varepsilon_{t-0}, \varepsilon_{t-1}, \cdots \varepsilon_{t-(p-1)}$ は全て独立であるから、
$$
\begin{eqnarray}
	V(r_t) &=& V \left(
		\phi_0 \sum_{k=0}^{p-1} \phi_1^k +
		\phi_1^p r_{t-p} +
		\sum_{k=0}^{p-1} \phi_1^k \varepsilon_{t-k}
	\right)
	\\ &=&
	V \left( \phi_0 \sum_{k=0}^{p-1} \phi_1^k \right) +
	V \left( \phi_1^p r_{t-p} \right) +
	V \left( \sum_{k=0}^{p-1} \phi_1^k \varepsilon_{t-k} \right)
	\\ &=&
	0 + \phi_1^{2p} V(r_{t-p}) +
	\sum_{k=0}^{p-1} V( \phi_1^k \varepsilon_{t-k})
	\\ &=&
	\phi_1^{2p} V(r_{t-p}) +
	\sum_{k=0}^{p-1} \phi_1^{2k} V(\varepsilon_{t-k})
\end{eqnarray}
$$

$r_t$ が定常過程であるためには、$V(r_t)$ についても $p \to \infty$ で発散しないことが必要。  
よって $\phi_1=1$ は不適。

> **【NOTE】**
> 
> 現実世界のデータ分析においては、非定常な $\phi_1=1$ のケースも重要。
> このケースを[単位根過程](../unit-root-process.md)と呼ぶ。


## 定常な AR(1) モデルの期待値・分散・自己相関係数

### 期待値

定常過程であるから、

$$
E(r_t) = E(r_{t-k}) \qquad (k = 1, 2, \cdots)
$$

よって $(2)$ の両辺で期待値を取れば、

$$
E(r_t) = \phi_0 + \phi_1 E(r_t) + 0
$$

ゆえに

$$
E(r_t) = \cfrac{\phi_0}{1-\phi_1}
\tag{4}
$$

### 分散

$(2)$ の両辺で分散を取る。  
$\phi_0, \phi_1 r_{t-1}, \varepsilon_t$ はそれぞれ独立であるから、

$$
\begin{eqnarray}
	V(r_t)
	&=&
	V(\phi_0 + \phi_1 r_{t-1} + \varepsilon_t)
	\\ &=&
	V(\phi_0) + V(\phi_1 r_{t-1}) + V(\varepsilon_t)
	\\ &=&
	0 + \phi_1^2 V(r_{t-1}) + V(\varepsilon_t)
\end{eqnarray}
$$

定常過程なので

$$
V(r_{t-1}) = V(r_t)
$$

であるから、

$$
V(r_t) = \phi_1^2 V(r_t) + V(\varepsilon_t)
$$

したがって、

$$
V(r_t) = \cfrac{V(\varepsilon_t)}{1-\phi_1^2}
\tag{5}
$$

### 自己相関係数

共分散の公式より、ラグ $h$ の自己共分散は

$$
\mathrm{Cov}(r_t, r_{t-h}) = E(r_t r_{t-h}) - E(r_t)E(r_{t-h})
$$

定常過程より $E(r_{t-h}) = E(r_t)$ だから、

$$
\mathrm{Cov}(r_t, r_{t-h}) = E(r_t r_{t-h}) - E(r_t)^2
$$

$(3)$ より

$$
\begin{eqnarray}
	E(r_t r_{t-h})&=&
	E \left(
		r_{t-h} \phi_0 \sum_{k=0}^{h-1} \phi_1^k +
		\phi_1^h r_{t-h}^2 +
		\sum_{k=0}^{h-1} \phi_1^k \varepsilon_{t-k} r_{t-h}
	\right)
	\\ &=&
	E(r_{t-h}) \phi_0 \sum_{k=0}^{h-1} \phi_1^k +
	\phi_1^h E(r_{t-h}^2) +
	\sum_{k=0}^{h-1} \phi_1^k E(\varepsilon_{t-k} r_{t-h})
	\\ &=&
	E(r_t) \phi_0 \cfrac{1-\phi_1^h}{1-\phi_1} +
	\phi_1^h E(r_t^2) +
	\sum_{k=0}^{h-1} \phi_1^k E(\varepsilon_{t-k}) E(r_{t-h})
	\\ &=&
	E(r_t)^2 (1-\phi_1^h) + \phi_1^h E(r_t^2) +
	\sum_{k=0}^{h-1} \phi_1^k \cdot 0 \cdot E(r_t)
	\\ &=&
	E(r_t)^2 (1-\phi_1^h) + \phi_1^h E(r_t^2)
\end{eqnarray}
$$

途中、ホワイトノイズ $\varepsilon_{t-k}$ と元の時系列 $r_{t-h}$ とは独立なので

$$
E(\varepsilon_{t-k} r_{t-h}) = E(\varepsilon_{t-k})E(r_{t-h})
$$

が成り立つこと、および $(4)$ を用いた。

以上より、

$$
\begin{eqnarray}
	\mathrm{Cov}(r_t, r_{t-h})
	&=&
	E(r_t)^2 (1-\phi_1^h) + \phi_1^h E(r_t^2) - E(r_t)^2
	\\ &=&
	\phi_1^h \left(E(r_t^2) - E(r_t)^2\right)
	\\ &=&
	\phi_1^h V(r_t)
\end{eqnarray}
$$

したがって、自己相関係数は

$$
\rho = \cfrac{\mathrm{Cov}(r_t, r_{t-h})}{V(r_t)} = \phi_1^h
\tag{6}
$$


## 実データへの適用

実データから $\phi_0$、$\phi_1$、および $\varepsilon_t$ の分散 $\sigma^2$ の推定値 $\hat{\phi_0}, \hat{\phi_1}, \hat{\sigma}^2$ を求める。

### 最尤推定による計算

誤差項の分布として正規分布を仮定する。

$$
\varepsilon_t \sim N(0, \sigma^2)
$$

$r_{t-1},\phi_0,\phi_1,\sigma$ が与えられたときに $r_t$ が得られる条件付き確率は、

$$
f(r_t|r_{t-1},\phi_0,\phi_1, \sigma)
=
\cfrac{1}{\sqrt{2\pi}\sigma}
\exp\left\{
	- \cfrac{1}{2\sigma^2} (r_t - \phi_0 - \phi_1 r_{t-1} )^2
\right\}
$$

よって $S = {r_1, \cdots, r_T}$ の同時確率は、

$$
\begin{eqnarray}
	L(\phi_0, \phi_1, \sigma) := f(r_1, \cdots, r_T | \phi_0, \phi_1, \sigma)
	&=&
	\prod_{t=2}^T f(r_t|r_{t-1},\phi_0,\phi_1, \sigma)
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}\sigma} \right)^{T-1}
	\prod_{t=2}^T \exp \left\{
		- \cfrac{1}{2\sigma^2}
		(r_t - \phi_0 - \phi_1 r_{t-1} )^2
	\right\}
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi}\sigma} \right)^{T-1}
	\exp \left\{
		- \cfrac{1}{2\sigma^2}
		\sum_{t=2}^T (r_t - \phi_0 - \phi_1 r_{t-1} )^2
	\right\}
\end{eqnarray}
$$

これを尤度関数とみなし、最大化するためのパラメータを求める。

対数を取ると、

$$
l(\phi_0, \phi_1, \sigma) := \log L(\phi_0, \phi_1, \sigma)
=
- (T-1) \log \left( \sqrt{2\pi}\sigma \right)
- \cfrac{1}{2\sigma^2}
\sum_{t=2}^T (r_t - \phi_0 - \phi_1 r_{t-1} )^2
$$

対数尤度 $l$ が最大値を取る時、

$$
\begin{eqnarray}
	\cfrac{\partial l(\phi_0, \phi_1, \sigma)}{\partial \phi_0}
	&=&
	\cfrac{1}{\sigma^2}
	\sum_{t=2}^T (r_t - \phi_0 - \phi_1 r_{t-1} ) = 0
	\\
	\cfrac{\partial l(\phi_0, \phi_1, \sigma)}{\partial \phi_1}
	&=&
	\cfrac{1}{\sigma^2}
	\sum_{t=2}^T r_{t-1} (r_t - \phi_0 - \phi_1 r_{t-1} ) = 0
	\\
	\cfrac{\partial l(\phi_0, \phi_1, \sigma)}{\partial \sigma}
	&=&
	- \cfrac{T-1}{\sigma} + \cfrac{1}{\sigma^3}
	\sum_{t=2}^T (r_t - \phi_0 - \phi_1 r_{t-1} )^2 = 0
\end{eqnarray}
$$

第1式、第2式を変形すると、

$$
\begin{eqnarray}
	\sum_{t=2}^T r_t - (T-1) \phi_0 - \phi_1 \sum_{t=1}^{T-1} r_t &=& 0
	\\
	\sum_{t=2}^T r_{t-1}r_t - \phi_0 \sum_{t=1}^{T-1} r_t - \phi_1 \sum_{t=1}^{T-1} r_t^2 &=& 0
\end{eqnarray}
$$

行列形式で書くと、

$$
\begin{pmatrix}
	T-1 & \displaystyle \sum_{t=1}^{T-1} r_t \\
	\displaystyle \sum_{t=1}^{T-1} r_t & \displaystyle \sum_{t=1}^{T-1} r_t^2
\end{pmatrix}
\begin{pmatrix}
	\phi_0 \\ \phi_1
\end{pmatrix}
=
\begin{pmatrix}
	\displaystyle \sum_{t=2}^T r_t \\
	\displaystyle \sum_{t=2}^T r_{t-1}r_t
\end{pmatrix}
$$

よって $\phi_0, \phi_1$ の推定値

$$
\begin{pmatrix}
	\hat{\phi}_0 \\ \hat{\phi}_1
\end{pmatrix}
=
\begin{pmatrix}
	T-1 & \displaystyle \sum_{t=1}^{T-1} r_t \\
	\displaystyle \sum_{t=1}^{T-1} r_t & \displaystyle \sum_{t=1}^{T-1} r_t^2
\end{pmatrix}^{-1}
\begin{pmatrix}
	\displaystyle \sum_{t=2}^T r_t \\
	\displaystyle \sum_{t=2}^T r_{t-1}r_t
\end{pmatrix}
\tag{7}
$$

を得る。

これらを $\partial l / \partial \sigma = 0$ の式に代入すると、

$$
\hat{\sigma}^2 =
\cfrac{\sum_{t=2}^T (r_t - \hat{\phi}_0 - \hat{\phi}_1 r_{t-1} )^2}{T-1}
\tag{8}
$$


### 最小二乗法による計算

自己回帰の式 $(2)$ を、$x$ の一次関数

$$
y = \phi_0 + \phi_1 x
$$

と読み替える。  
$(x,y)$ の実現値として $(r_1, r_2), (r_2, r_3), \cdots, (r_{T-1}, r_T)$ を当てはめ、[最小二乗法](../../../Algorithm/least_square.md)によって $\phi_0, \phi_1$ を求める。  
また、$\varepsilon$ を回帰直線と実データとの残差と考えれば、$\sigma^2$ の推定値は残差の標本分散を計算すれば良い。

> **【NOTE】**
> 
> 最小二乗法は誤差を正規分布と仮定した場合の最尤推定とも解釈できるので、推定結果は前述の $(7)(8)$ と一致する。


### 標本分散・標本自己共分散による計算

標本平均 $\bar{r}$ は

$$
\bar{r} = \cfrac{1}{T} \sum_{t=1}^T r_t
$$

これを用いて標本分散は

$$
\hat{\gamma_0} = \cfrac{1}{T} \sum_{t=1}^T (r_t-\bar{r})^2
$$

標本自己共分散は

$$
\hat{\gamma_1} = \cfrac{1}{T} \sum_{t=1}^{T-1} (r_t - \bar{r}) (r_{t+1}-\bar{r})
$$

と計算できる。  
これらを期待値・分散・自己共分散の推定値として用いる。

$(6)$ で $h=1$ の場合の式を考え、$V(r_t) \to \hat{\gamma_0},\ \mathrm{Cov}(r_t, r_{t-1}) \to \hat{\gamma_1}$ とすれば、

$$
\hat{\phi_1}
=
\cfrac{\hat{\gamma_1}}{\hat{\gamma_0}}
=
\cfrac{
	\displaystyle
	\sum_{t=1}^{T-1} (r_t - \bar{r}) (r_{t+1}-\bar{r})
}{
	\displaystyle
	\sum_{t=1}^T (r_t-\bar{r})^2
}
$$

次に $(4)$ で $E(r_t) \to \bar{r}$ とすれば、

$$
\hat{\phi_0} = \left( 1-\hat{\phi_1} \right) \bar{r}
$$

最後に $(5)$ で $V(r_t) \to \hat{\gamma_0}, \ V(\varepsilon) \to \hat{\sigma}^2$ と置けば、

$$
\hat{\sigma}^2
=
\left( 1-\hat{\phi_1}^2 \right) \hat{\gamma_0}
$$


### 【実験】手作り AR(1) モデルのパラメータ推定

推定対象の時系列データ：$\phi_0 = 1.3, \ \phi_1 = 0.7, \sigma = 0.1$ で機械的にデータを生成。

![Figure_3](https://user-images.githubusercontent.com/13412823/243610812-308929d5-1774-4531-9091-ce8cd80a3deb.png)

- 適当な初期値を与えて生成しても、最初の10ステップほどで、ある程度値が収束して定常化
	- 収束後の値は $(4)$ から計算した $\phi_0 / (1-\phi_1) = 4.333$ と一致
- その後は完全にランダムに見えるが、実際には後述の通り自己回帰性が見られる


| 最小二乗法（最尤推定）による推定 | 標本分散・標本自己共分散による推定 |
| :-- | :-- |
| ![Figure_1](https://user-images.githubusercontent.com/13412823/243601123-9bb4469a-cece-462a-8edf-c4257a7a88c7.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/243601134-e042aedc-a621-4716-9166-02bae8623fd4.png) |

- 一見ランダムに見える時系列から、元の $\mathrm{AR}(1)$ モデルのパラメータ $\phi_0 = 1.3, \ \phi_1 = 0.7, \sigma = 0.1$ を求めることができた
- 時系列長 $T$ が大きいほど、各パラメータの推定の誤差（標準偏差）は小さくなる


残差の正規性の確認（QQ-plot）：

![Figure_1](https://user-images.githubusercontent.com/13412823/248294085-093edc56-e345-43b5-8847-00d056223e94.png)


{% gist d839d197bea1f4c50c3c607ff70e0aae 20230606_ar1-model.py %}
