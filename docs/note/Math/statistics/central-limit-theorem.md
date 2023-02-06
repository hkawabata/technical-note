---
title: 中心極限定理
title-en: Central Limit Theorem
---

# 定理

$n$ 個の確率変数 $X_1, \cdots, X_n$ が

- **互いに独立している**
- **平均 $\mu$、分散 $\sigma^2$ の同一の確率分布（正規分布でなくて良い）に従う**

とき、これらの平均

$$
\bar{X} = X_1 + \cdots + X_n = \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} X_n
$$

を新しい確率変数とみなすと、$n$ を無限大に発散させたとき、$\bar{X}$ の確率分布は平均 $\mu$、分散 $\cfrac{\sigma^2}{n}$ の正規分布に収束する。

言い換えると、**母集団の分布がどんな形であれ, 標本の数 $n$ が十分に大きい場合の標本平均 $\bar{X}$ の分布は正規分布へと近づいていく**。


# 証明

## 平均・分散の証明

$\bar{X}$ の平均 $E(\bar{X}) = \mu$、分散 $V(\bar{X}) = \cfrac{\sigma^2}{n}$ であることは、一般的な期待値と分散の性質

$$E(aX) = aE(X)$$

$$E(X+Y) = E(X) + E(Y)$$

$$V(aX) = a^2 V(X)$$

$$V(X+Y) = V(X) + V(Y) + 2 \mathrm{Cov}(X, Y)$$

（ここで $\mathrm{Cov}$ は共分散であり、$X,Y$ が互いに独立ならゼロ）

を用いて、以下のように計算して示せる。

$$
\begin{eqnarray}
  E(\bar{X}) &=& E \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} E(X_i) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} \mu \\
  &=& \cfrac{1}{n} n\mu = \mu
\end{eqnarray}
$$

$$
\begin{eqnarray}
  V(\bar{X}) &=& V \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} V(X_i) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} \sigma^2 \\
  &=& \cfrac{1}{n^2} n \sigma^2 = \cfrac{\sigma^2}{n}
\end{eqnarray}
$$

## 正規分布に従うことの証明

$\bar{X}$ が正規分布に従う $\Longleftrightarrow$ $\bar{X}$ を標準化した確率変数 $Z$ が標準正規分布に従う

なので、$n \rightarrow \infty$ のときに $Z$ が標準正規分布に従うことを証明すれば良い。  
それには、[モーメント母関数](moment-generating-function.md)（積率母関数）が標準正規分布のものに収束することを示せば十分。

前節で計算した平均値と分散の値を用いて $\bar{X}$ を標準化すると、

$$
\begin{eqnarray}
  Z &\equiv& \cfrac{\bar{X}-\mu}{\sigma / \sqrt{n}}
  \\ &=&
  \cfrac{\sqrt{n}}{\sigma} \left(
    \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} X_i - \mu
  \right)
  \\ &=&
  \cfrac{1}{\sigma \sqrt{n}} \left(
    \displaystyle \sum_{i=1}^{n} X_i - n \mu
  \right)
  \\ &=&
  \cfrac{1}{\sigma \sqrt{n}} \left(
    \displaystyle \sum_{i=1}^{n} (X_i - \mu)
  \right)
\end{eqnarray}
$$

ここで $X_i$ を標準化した確率変数

$$
Z_i \equiv \cfrac{X_i-\mu}{\sigma}
$$

を導入すれば、

$$
Z = \cfrac{1}{\sqrt{n}} \displaystyle \sum_{i=1}^{n}Z_i
$$

$Z$ のモーメント母関数は

$$
\begin{eqnarray}
  M_Z(t) &=& E \left( \exp{(tZ)} \right)
  \\ &=&
  E \left(
    \exp{ \left(
      \cfrac{t}{\sqrt{n}} \displaystyle \sum_{i=1}^{n}Z_i
    \right) }
  \right)
  \\ &=&
  E \left(
    \displaystyle \prod_{i=1}^{n} \exp{ \left( \cfrac{t}{\sqrt{n}} Z_i \right) }
  \right)
  \\ &=&
  \displaystyle \prod_{i=1}^{n} E \left(
    \exp{ \left( \cfrac{t}{\sqrt{n}} Z_i \right) }
  \right)
  \\ &=&
  \displaystyle \prod_{i=1}^{n} M_{Z_i} \left (\cfrac{t}{\sqrt{n}} \right)
\end{eqnarray}
$$

よって、$Z$ のモーメント母関数は各変数 $Z_1, \cdots, Z_n$ のモーメント母関数の積で表現できる。

$Z_1, \cdots, Z_n$ は全て同じ確率分布に従うから、モーメント母関数も等しく、

$$
M_Z(t) = \left( M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right) \right)^n
$$

となる（$k$ は 1〜$n$ のどれでも良い）。

$M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)$ をマクローリン展開すると、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
M_{X_k}(0) +
\cfrac{M'_{Z_k}(0)}{1!}\left(\cfrac{t}{\sqrt{n}}\right) +
\cfrac{M''_{Z_k}(0)}{2!}\left(\cfrac{t}{\sqrt{n}}\right)^2 +
\cfrac{M'''_{Z_k}(0)}{3!}\left(\cfrac{t}{\sqrt{n}}\right)^3 + \cdots
$$

ここで、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
\int_{-\infty}^{\infty} \exp{\left(\cfrac{tZ_k}{\sqrt{n}}\right)} f(Z_k) dZ_k
$$

であるから、

$$
M_{Z_k}(0) = \int_{-\infty}^{\infty} f(Z_k) dZ_k = 1
$$

（任意の確率密度関数の全区間積分は1）

また、$Z_k$ は標準化されており、モーメント母関数の性質と分散・期待値の公式から、

$$
M'_{Z_k}(0) = E(Z_k) = 0
$$

$$
M''_{Z_k}(0) = E(Z^2_k) = V(Z_k) - E(Z_k)^2 = 1-0^2=1
$$

これらをマクローリン展開の式に代入し、$\cfrac{t}{\sqrt{n}}$ の3次以上の式を $O((t/\sqrt{n})^3)$ でまとめて表すと、

$$
M_{Z_k} \left (\cfrac{t}{\sqrt{n}} \right)
=
1 + \cfrac{t^2}{2n} + O ((t/\sqrt{n})^3)
$$

これを $M_\bar{X}(t)$ の式に代入すれば、

$$
\begin{eqnarray}
  M_Z(t) &=& \left( M_{Z_k} \left( \cfrac{t}{\sqrt{n}} \right) \right)^n
  \\ &=&
  \left(
    1 + \cfrac{t^2}{2n} + O ((t/\sqrt{n})^3)
  \right)^n
  \\ &\longrightarrow&
  \exp{\left( \cfrac{t^2}{2} \right)} \qquad (n \rightarrow \infty)
\end{eqnarray}
$$

最後の式は標準正規分布のモーメント母関数に一致する（証明終了）。


# 実験

いろいろな確率分布から標本を繰り返し抽出して、中心極限定理が成り立つことを確認する。

```python
import numpy as np
from matplotlib import pyplot as plt
from abc import ABC, abstractmethod

class Distribution(ABC):
	@abstractmethod
	def get_name(self):
		pass
	
	@abstractmethod
	def get_average_of_samples(self, n):
		pass
	
	def get_mu(self):
		return self.__mu
	
	def get_sigma(self):
		return self.__sigma
	
	def set_mu(self, mu):
		self.__mu = mu
	
	def set_sigma(self, sigma):
		self.__sigma = sigma


class UniformDist(Distribution):
	"""
	一様分布
	"""
	def __init__(self, a, b):
		self.set_mu((a + b) * 0.5)
		variance = (b-a)**2/12.0
		self.set_sigma(np.sqrt(variance))
		self.__a = a
		self.__b = b
	
	def get_name(self):
		return 'Uniform Distribution'
	
	def get_average_of_samples(self, n):
		samples = np.random.rand(n) * (self.__b - self.__a) + self.__a
		return samples.mean()


class BinomialDist(Distribution):
	"""
	二項分布
	"""
	def __init__(self, n, p):
		self.set_mu(n*p)
		variance = n*p*(1-p)
		self.set_sigma(np.sqrt(variance))
		self.__n = n
		self.__p = p
	
	def get_name(self):
		return 'Binomial Distribution'
	
	def get_average_of_samples(self, n):
		samples = np.random.binomial(self.__n, self.__p, n)
		return samples.mean()


class BetaDist(Distribution):
	"""
	ベータ分布
	"""
	def __init__(self, a, b):
		self.set_mu(a/(a+b))
		variance = a*b/(a+b+1)/(a+b)**2
		self.set_sigma(np.sqrt(variance))
		self.__a = a
		self.__b = b
	
	def get_name(self):
		return 'Beta Distribution'
	
	def get_average_of_samples(self, n):
		samples = np.random.beta(self.__a, self.__b, n)
		return samples.mean()


def gauss(x, mu, sigma):
	"""
	x を引数とする正規分布の確率密度関数を計算
	"""
	ret = np.exp(- (x-mu)**2 * 0.5 / sigma**2)
	ret /= np.sqrt(2.0 * np.pi) * sigma
	return ret

def func(dist):
	"""
	与えられた確率分布について色々な標本サイズで標本平均を繰り返し計算し、
	標本平均の分布が正規分布に近づくことをグラフで確認する
	"""
	T = 100000  # n個の標本を抽出して平均を取る操作を何度繰り返すか
	n_samples = [2, 4, 8, 16, 32, 64]  # 標本サイズ
	# 標本を繰り返し抽出して平均値を記録
	plt.figure(figsize=(10, 6))
	plt.subplots_adjust(wspace=0.3, hspace=0.4)
	for i in range(len(n_samples)):
		n = n_samples[i]
		sample_mean = np.empty(T, dtype='float')
		for t in range(T):
			sample_mean[t] = dist.get_average_of_samples(n)
		# ヒストグラム描画のための階級幅を計算
		mean_max = sample_mean.max()
		mean_min = sample_mean.min()
		bins = np.linspace(mean_min, mean_max, 50)  # 階級の区切り
		# ヒストグラムを描画
		plt.subplot(2, 3, i+1)
		plt.hist(sample_mean, bins=bins, density=True)
		# 中心極限定理により収束が期待される正規分布を描画
		mu = dist.get_mu()
		sigma = dist.get_sigma() / np.sqrt(n)
		x_norm = np.linspace(mean_min-(mean_max-mean_min)*0.2, mean_max+(mean_max-mean_min)*0.2, 100)
		norm = gauss(x_norm, mu=mu, sigma=sigma)
		plt.title(r'$n_{{\rm sample}} = {}$'.format(n))
		plt.plot(x_norm, norm, lw=1.0, color='red', label=r'$N(\mu, \sigma)$')
		if i == 0:
			plt.legend()
	plt.suptitle(dist.get_name())
	plt.show()

func(UniformDist(0, 6))
func(BinomialDist(10, 0.7))
func(BinomialDist(100, 0.2))
func(BetaDist(9, 3))
func(BetaDist(2, 2))
```