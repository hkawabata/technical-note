---
title: 点推定
title-en: Point Estimation
---

# 点推定とは

標本の統計量から母集団の母数（母平均や母分散など）を推定すること。

推定された値（推定値）は上にハット記号（ $\hat{}$ ）をつけて表す。

# 点推定の例

以後、大きさ $N$ の母集団から $n$ 件の標本 $x_1, \cdots, x_n$ を抽出する場合を考える。

## 母平均の点推定

母平均の[不偏推定量](unbiased-estimator.md)は標本平均であるから、母平均 $\mu$ の推定値は

$$
\hat{\mu} = \cfrac{1}{n} \sum_{i=1}^n x_i
$$

## 母分散の点推定

母分散の[不偏推定量](unbiased-estimator.md)は不偏分散であるから、母分散 $\sigma^2$ の推定値は

$$
\hat{\sigma}^2 = \cfrac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
$$

ここで、$\bar{x}$ は標本平均。


## 最尤推定

あるパラメータ $\theta$ に依存する確率密度関数 $f(x;\theta)$ に従う確率変数 $x$ について、ある標本が与えられたとする。  
このとき、その標本が得られる確率 $L(\theta; x)$ を最大化する $\theta$ を $\theta$ の **最尤推定値** と呼び、このように推定値を求める手法を **最尤推定** という。  
また、この確率 $L(\theta; x)$ を **尤度関数** という。

通常、最尤推定値は以下の方程式を解くことで求める。

$$
\cfrac{\partial L(\theta; x)}{\partial \theta} = 0  \tag{1}
$$

また、尤度関数 $L(\theta; x)$ が多数の関数の積で表されるとき、$(1)$ をそのまま用いると計算が大変になる：

$$
L(\theta;x) = f_1(\theta;x) \cdot f_2(\theta;x) \cdots f_k(\theta;x)
$$

このようなとき、$L$ の代わりに $\log{L}$ を尤度として用い（**対数尤度**）、

$$
\cfrac{\partial}{\partial \theta} \log{L(\theta; x)} = 0  \tag{1}
$$

を解くことで $\theta$ の最尤推定値を求める。

> **【NOTE】**
> 
> $L(\theta;x)$ が大きいほど $\log L(\theta;x)$ も大きくなるので、$\log L(\theta;x)$ が最大のとき $L(\theta;x)$ も最大。  
> すなわち、対数を取っても取らなくても、求まる最尤推定値は等しい。


### 具体例1

偏りがあると思われるコインの表が出る確率を $p$ とする。  
このコインを5回投げると、表・表・裏・表・裏となった。  
この事象の実現確率（尤度関数）は

$$
L(p) = p \cdot p \cdot (1-p) \cdot p \cdot (1-p) = p^3 (1-p)^2
$$

よって

$$
\cfrac{\partial L(p)}{\partial p} = 3p^2(1-p)^2 - 2p^3(1-p)
= p^2(1-p)(3-5p)
$$

であり、$p=0,1$ は実際の $p$ の値としては不適なので、最尤推定値は

$$
\hat{p} = \cfrac{3}{5}
$$

次に、対数尤度で考えてみる。

$$
\log{L(p)} = 3 \log p + 2 \log (1-p)
$$

であるから、

$$
\cfrac{\partial}{\partial p} \log L(p)
= \cfrac{3}{p} - \cfrac{2}{1-p}
= \cfrac{3-5p}{p(1-p)}
$$

よって最尤推定値は

$$
\hat{p} = \cfrac{3}{5}
$$


### 具体例2

期待値0の正規分布が仮定できる母集団から $n=10$ 件の標本 $x_1, \cdots, x_{10}$ を抽出すると、結果は以下の通りだった。

```
10.08  8.04  -1.37  3.83    7.65,
3.85   0.71   4.75  12.35  -17.46
```

この母集団の分散 $\sigma^2$ を推定したい。

期待値0の正規分布の確率密度関数は

$$
f(x;\sigma)
=
\cfrac{1}{\sqrt{2\pi} \sigma}
\exp \left( - \cfrac{x^2}{2\sigma^2} \right)
$$

$n$ 件の標本の同時確率密度関数（尤度関数）は

$$
\begin{eqnarray}
	L(\sigma)
	&=&
	f(x_1;\sigma) \cdot f(x_2;\sigma) \cdots f(x_n;\sigma)
	\\ &=&
	\left( \cfrac{1}{\sqrt{2\pi} \sigma} \right)^n
	\exp \left( - \cfrac{ \sum_{k=1}^n x_k^2}{2\sigma^2} \right)
\end{eqnarray}
$$

対数尤度を取ると、

$$
\log L(\sigma)
=
- \cfrac{n}{2} \log 2\pi - n \log \sigma
- \cfrac{ \sum_{k=1}^n x_k^2 }{2\sigma^2}
$$

であるから、

$$
\cfrac{\partial}{\partial \sigma} \log L(\sigma)
=
- \cfrac{n}{\sigma}
+ \cfrac{ \sum_{k=1}^n x_k^2 }{\sigma^3}
=
\cfrac{ \sum_{k=1}^n x_k^2 - n \sigma^2 }{\sigma^3}
$$

よって最尤推定値は

$$
\hat{\sigma}^2 = \cfrac{ \sum_{k=1}^n x_k^2 }{n}
$$

これは標本分散に等しい。

実際の標本10件の値と $n=10$ を代入すると、

$$
\hat{\sigma}^2 = \cfrac{ 736.5795 }{10} \simeq 73.66
$$

> **【NOTE】** 分散の最尤推定値は、不偏分散
> 
> $$
s^2 = \cfrac{\sum_{k=1}^n x_k^2}{n-1}
$$
> 
> とは一致しない。