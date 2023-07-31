---
title: 多重検定の問題
title-en: Multiple comparisons problem
---

# 多重検定の問題とは

例として、分散が等しい正規分布に従う3つの母集団 A, B, C の平均値を t 検定で比較する場合を考える。（cf. [母平均の検定](testing-for-the-mean.md)）

この際、

1. A と B の t 検定
2. B と C の t 検定
3. C と A の t 検定

の3つの検定をそれぞれ有意水準 $\alpha=0.05$ で行うとする。

実際に A, B, C の平均値が全て等しい場合であっても、標本のばらつきにより、有意差ありと誤判定されてしまう可能性がある（**第一種の過誤**）。  
母集団の平均値が等しい時、3つの検定全てで「有意差なし」となる確率は、

$$
(1-\alpha)^3 = 0.857
$$

であるから、1つ以上の検定で「有意差あり」と誤判定されてしまう確率は

$$
1- (1-\alpha)^3 = 0.143
$$

となり、1つ1つの t 検定の有意水準 $\alpha=0.05$ よりかなり大きくなってしまう。

同様に、有意水準 $\alpha$ の検定を $n$ 個組み合わせて検定を実施する場合、第一種の過誤が生じる確率は

$$
P_{\mathrm{err}1} = 1- (1-\alpha)^n
\tag{1}
$$

となる。

$\alpha$ が小さければ、

$$
P_{\mathrm{err}1} \simeq 1- (1-n\alpha) = n \alpha
\tag{1'}
$$

と近似できる。  
→ $n$ 個の検定を組み合わせる場合、検定全体で第一種の過誤が起こる確率は、**個別の検定の $n$ 倍になってしまう。**


# 補正の方法

逆に、「有意水準 $\alpha$ の検定を $n$ 個組み合わせた多重検定全体」の有意水準（帰無仮説が正しい場合に第一種の過誤が生じる確率 $P_{\mathrm{err}1}$ ）を $\alpha_0$ としたい場合を考える。  
方程式

$$
P_{\mathrm{err}1} = 1 - (1-\alpha)^n = \alpha_0
$$

を解けば

$$
\alpha = 1 - (1-\alpha_0)^{1/n}
\tag{2}
$$

を得るので、この $\alpha$ を個別の検定の有意水準とすれば良い。  
$\alpha_0$ が十分小さい場合は、

$$
\alpha \simeq 1 - \left( 1 - \cfrac{\alpha_0}{n} \right) = \cfrac{\alpha_0}{n}
\tag{2'}
$$

と近似できる。したがって、**検定全体に設定したい有意水準 $\alpha_0$ を検定の多重度 $n$ で割ったものを個別の検定の有意水準に用いれば良い。**

例えば前述の3母集団の平均値に関する t 検定を（全体の）有意水準 0.05 で実施したい場合、$n=3,\ \alpha_0=0.05$ であるから、$(2)$ に代入すると $\alpha = 0.016952\cdots$ が得られる。  
→ 個別の t 検定を有意水準 0.017 で実施すれば良い。

※ $(2')$ で近似すると $\alpha = 0.016666\cdots$ となり、近い値となる。


# 実験

## 母集団の組 (A,B), (B,C), (C,A) の t 検定

前述の分散が等しい3つの正規分布母集団 A, B, C を比較する3つの t 検定を何度も繰り返し、「母平均値が等しい時に1つ以上の検定で第一種の過誤が生じる確率」を求めてみる。

```python
import numpy as np
from scipy import stats

alpha = 0.05
mu = 10.0
sigma = 1.0
n_sample = 10
n_try = 100000

cnt_1err = 0
for i in range(1, n_try+1):
	x1 = np.random.normal(mu, sigma, n_sample)
	x2 = np.random.normal(mu, sigma, n_sample)
	x3 = np.random.normal(mu, sigma, n_sample)
	if stats.ttest_ind(x1, x2).pvalue < alpha or stats.ttest_ind(x2, x3).pvalue < alpha or stats.ttest_ind(x3, x1).pvalue < alpha:
		cnt_1err += 1
	if i % (n_try//10) == 0:
		print(cnt_1err, '/', i, '=', float(cnt_1err) / i)
```

```
1222 / 10000 = 0.1222
2500 / 20000 = 0.125
3725 / 30000 = 0.12416666666666666
4933 / 40000 = 0.123325
6157 / 50000 = 0.12314
7396 / 60000 = 0.12326666666666666
8665 / 70000 = 0.12378571428571429
9900 / 80000 = 0.12375
11132 / 90000 = 0.12368888888888889
12330 / 100000 = 0.1233
```

→ 各検定の有意水準 0.05 よりも高いが、理論上の第一種の過誤の確率 0.143 よりも低い。

> 【考察】母集団 A, B, C の組み合わせ全てを比較しており、以下の3つが独立な事象とならないから？  
> 
> - 事象1：A と B の比較で有意差が出る
> - 事象2：B と C の比較で有意差が出る
> - 事象3：C と A の比較で有意差が出る
>
> 例：A の標本に偏りがあれば、事象1,3両方の確率が高まりそう。逆に、A の標本に偏りがなければ、事象1,3両方の確率が小さくなりそう。


## 母集団の組 (A,B), (B,C), (C,D) の t 検定

前節のように3つの母集団の組み合わせ全てを調べると、(A,B), (B,C) いずれかで有意差が出れば (A,C) でも有意差が出る確率が高そう。  
→ 別の母集団 D を加えて、(A, B), (B, C), (C, D) の組を t 検定してみる。  

```python
cnt_1err = 0
for i in range(1, n_try+1):
	x1 = np.random.normal(mu, sigma, n_sample)
	x2 = np.random.normal(mu, sigma, n_sample)
	x3 = np.random.normal(mu, sigma, n_sample)
	x4 = np.random.normal(mu, sigma, n_sample)
	if stats.ttest_ind(x1, x2).pvalue < alpha or stats.ttest_ind(x2, x3).pvalue < alpha or stats.ttest_ind(x3, x4).pvalue < alpha:
		cnt_1err += 1
	if i % (n_try//10) == 0:
		print(cnt_1err, '/', i, '=', float(cnt_1err) / i)

"""
1300 / 10000 = 0.13
2631 / 20000 = 0.13155
3935 / 30000 = 0.13116666666666665
5249 / 40000 = 0.131225
6574 / 50000 = 0.13148
7862 / 60000 = 0.13103333333333333
9119 / 70000 = 0.13027142857142857
10438 / 80000 = 0.130475
11775 / 90000 = 0.13083333333333333
13071 / 100000 = 0.13071
"""
# -> やはり理論値より少し低い。
```

→ まだ理論上の第一種の過誤の確率 0.143 よりも低いが、理論値に近づいた。

> 【考察】事象の独立性は高まったが、やはり (A,B) と (B,C) の検定が独立でなく、(B,C) と (C,D) の検定が独立でないから？


## 母集団の組 (A,B), (C,D), (E,F) の t 検定

6つの母集団 A〜F を用意し、完全に独立な t 検定を3つ実施してみる。

```python
cnt_1err = 0
for i in range(1, n_try+1):
	x1 = np.random.normal(mu, sigma, n_sample)
	x2 = np.random.normal(mu, sigma, n_sample)
	x3 = np.random.normal(mu, sigma, n_sample)
	x4 = np.random.normal(mu, sigma, n_sample)
	x5 = np.random.normal(mu, sigma, n_sample)
	x6 = np.random.normal(mu, sigma, n_sample)
	if stats.ttest_ind(x1, x2).pvalue < alpha or stats.ttest_ind(x3, x4).pvalue < alpha or stats.ttest_ind(x5, x6).pvalue < alpha:
		cnt_1err += 1
	if i % (n_try//10) == 0:
		print(cnt_1err, '/', i, '=', float(cnt_1err) / i)

"""
1407 / 10000 = 0.1407
2891 / 20000 = 0.14455
4297 / 30000 = 0.14323333333333332
5696 / 40000 = 0.1424
7135 / 50000 = 0.1427
8567 / 60000 = 0.14278333333333335
9968 / 70000 = 0.1424
11472 / 80000 = 0.1434
12858 / 90000 = 0.14286666666666667
14301 / 100000 = 0.14301
"""
```

→ 完全に独立した t 検定3つであれば、理論上の第一種の過誤の確率 0.143 にほぼ等しい結果が得られた。