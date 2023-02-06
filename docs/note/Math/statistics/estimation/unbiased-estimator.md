---
title: 不偏推定量
title-en: Unbiased Estimator
---

# 不偏推定量とは

母集団が非常に大きい時、全てのデータを使って平均や分散などの統計量を計算するのはコストが大きい。  
そのため、母集団の一部を標本として抽出し、その標本から母集団全体の統計量を **推定** する。

標本から計算した推定量の期待値が、母集団の真の値と等しくなるような推定量を **不偏推定量** と呼ぶ。

# 不偏推定量の例

大きさ $N$ の母集団から $n$ 件の標本 $x_1, \cdots, x_n$ を抽出する場合を考える。

## 平均

### 母平均の不偏推定量

- $\mu$：母集団全体の平均値（**母平均**）
- $\bar{x}$：標本の平均値（**標本平均**）

とする。

$$
\begin{eqnarray}
	\mu &=& \cfrac{1}{N} \sum_{i=1}^{N} x_i = E(x_i) \\
	\bar{x} &=& \cfrac{1}{n} \sum_{i=1}^{n} x_i
\end{eqnarray}
$$

> **【定理】**
>
> 母平均 $\mu$ の不偏推定量 = 標本平均 $\bar{x}$

【証明】

標本平均 $\bar{x}$ の期待値を計算すると、期待値の線形性より

$$
\begin{eqnarray}
	E(\bar{x}) &=& E\left( \cfrac{1}{n} \sum_{i=1}^{n} x_i \right)
	\\ &=&
	\cfrac{1}{n} \sum_{i=1}^{n} E(x_i)
	\\ &=&
	\cfrac{1}{n} \sum_{i=1}^{n} \mu
	\\ &=&
	\cfrac{1}{n} n \mu
	\\ &=&
	\mu
\end{eqnarray}
$$

となり、母平均に一致。


## 分散

### 母分散の不偏推定量

$\sigma^2$ を母集団全体の分散（**母分散**）とする。

$$
\begin{eqnarray}
	\sigma^2 &=& \cfrac{1}{N} \sum_{i=1}^N (x_i - \mu)^2 =
	E \left( (x_i - \mu)^2 \right) = V(x_i) \\
	\mu &=& \cfrac{1}{N} \sum_{i=1}^{N} x_i = E(x_i)
\end{eqnarray}
$$

> **【定理】**
>
> **不偏分散** $s^2$ を
>
> $$
s^2 \equiv \cfrac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2
$$
> 
> で定義すると、母分散 $\sigma^2$ の不偏推定量 = 不偏分散 $s^2$

**【証明】**

$$
\begin{eqnarray}
	\sum_{i=1}^n (x_i - \mu)^2
	&=&
	\sum_{i=1}^n ( (x_i - \bar{x}) + (\bar{x} - \mu) )^2
	\\ &=&
	\sum_{i=1}^n (x_i - \bar{x})^2 +
	\sum_{i=1}^n (\bar{x} - \mu)^2 +
	2 \sum_{i=1}^n (x_i - \bar{x}) (\bar{x} - \mu)
	\\ &=&
	\sum_{i=1}^n (x_i - \bar{x})^2 +
	(\bar{x} - \mu)^2 \sum_{i=1}^n 1 +
	2 (\bar{x} - \mu) \left( \sum_{i=1}^n x_i - \sum_{i=1}^n \bar{x} \right)
	\\ &=&
	\sum_{i=1}^n (x_i - \bar{x})^2 +
	n (\bar{x} - \mu)^2 +
	2 (\bar{x} - \mu) (n \bar{x} - n \bar{x})
	\\ &=&
	\sum_{i=1}^n (x_i - \bar{x})^2 +
	n (\bar{x} - \mu)^2
\end{eqnarray}
$$

両辺の期待値を取ると、期待値の線形性より

$$
\sum_{i=1}^n E \left( (x_i - \mu)^2 \right)
=
E \left( \sum_{i=1}^n (x_i - \bar{x})^2 \right) +
n E \left( (\bar{x} - \mu)^2 \right)
$$

ここで、

$$
\begin{eqnarray}
	E \left( (x_i - \mu)^2 \right) &=& V(x_i)
	\\ &=&
	\sigma^2
	\\
	E \left( (\bar{x} - \mu)^2 \right)
	&=&
	V(\bar{x})
	\\ &=&
	V\left( \cfrac{x_1 + \cdots + x_n}{n} \right)
	\\ &=&
	\cfrac{1}{n^2} \sum_{i=1}^n V(x_i)
	\\ &=&
	\cfrac{1}{n^2} \sum_{i=1}^n \sigma^2
	\\ &=&
	\cfrac{1}{n^2} n \sigma^2
	\\ &=&
	\cfrac{\sigma^2}{n}
\end{eqnarray}
$$

であるから、

$$
\sum_{i=1}^n \sigma^2
=
E \left( \sum_{i=1}^n (x_i - \bar{x})^2 \right) +
n \cfrac{\sigma^2}{n}
$$

右辺第2項を移項して両辺を $n-1$ で割ると、

$$
\sigma^2 = E \left( \cfrac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 \right) = E(s^2)
$$

となり、不偏分散 $s^2$ の期待値が母分散 $\sigma^2$ に一致する。

### 不偏分散の直感的理解

標本分散

$$
\cfrac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

の計算では、真の母平均 $\mu$ ではなく、標本平均 $\bar{x}$ と $x_i$ の差の平方和を取っている。  
そのため、真の母平均と差を取る場合に比べて計算結果に誤差が含まれる。  
この誤差が前節の計算式において

$$
E \left( (\bar{x} - \mu)^2 \right)
$$

の項として現れており、標本分散の期待値は母分散に比べて小さくなってしまう。

### 実験：不偏分散の期待値は本当に母分散になるか？

標準正規分布に従う母集団からランダムな標本抽出を繰り返して、標本分散と不偏分散を計算してみる。

{% gist 02b35f69c96a0ad4d9ebc3a6f6b47c53 unbiased-variance.py %}

![Figure_1](https://user-images.githubusercontent.com/13412823/216799668-0108ecf7-0f22-4740-a57e-8b6b5448642b.png)

- 標本分散 0.8979 $\lt$ 母分散1.0
- 不偏分散 0.9976 $\simeq$ 母分散1.0
