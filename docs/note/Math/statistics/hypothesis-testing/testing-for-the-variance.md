---
title: 分散の検定
title-en: Hypothesis Testing for the Variance
---

# 等分散性の検定

## F 検定

> **【問題設定】**
> 
> - 前提
> 	- 2つの母集団が **正規分布** に従い、**互いに独立** している
> - 調べたいこと
> 	- 2つの母集団の母分散に有意差があるか否か？

### 理論

正規分布 $N(\mu_1, \sigma_1^2), N(\mu_2, \sigma_2^2)$ に従う独立した確率変数 $X_1, X_2$ を考える。  
これらの母集団からそれぞれ $n_1, n_2$ 件の標本を抽出した時、その標本不偏分散を $s_1^2, s_2^2$ とすると、

$$
\chi_i^2 := \cfrac{(n_i-1)s_i^2}{\sigma_i^2} \sim \chi^2(n_i-1) \qquad (i=1,2)
$$

cf. [不偏分散とカイ二乗分布の定理](../distribution/chi-square-distribution.md)

よって

$$
F := \cfrac{\chi_1^2/(n_1-1)}{\chi_2^2/(n_2-1)}
= \cfrac{s_1^2 / \sigma_1^2}{s_2^2 / \sigma_2^2}
\sim F(n_1-1, n_2-1)
$$

cf. [F 分布](../distribution/f-distribution.md)

以上により、$X_1, X_2$ の母集団の分散 $\sigma_1^2, \sigma_2^2$ が等しいという帰無仮説の下では、

$$
F = \cfrac{s_1^2}{s_2^2}
\sim F(n_1-1, n_2-1)
$$

が成り立つ。これを用いて **F 検定** を行う。

> **【NOTE】F 分布の下側確率**
> 
> F 検定では両側検定を行うことが多いため、上側2.5%点・下側2.5%点の両方が必要になる。しかし、一般的な F 分布表では上側確率に対応する点しか書かれていない。
> 
> F 分布の性質より、確率変数 $F$ について、
> 
> $$
F \sim F(n_1, n_2) \Longleftrightarrow \cfrac{1}{F} \sim F(n_2, n_1)
$$
> 
> であるから、F 分布の下側確率に対応する点を求めるには、自由度の順序を入れ替えた F 分布についての上側確率に対応する点を求め、その逆数を取れば良い。

### 具体例

ある工場で、同じ部品 A を製造する機械 B が2台ある（B1, B2 とする）。  
この2台で製造された部品をサンプリングして重さ $[\mathrm{g}]$ を測定したところ、以下の結果を得た。
- B1 からサンプリングした部品 A（$n_1=11$ 個）の重さの不偏分散 $s_1^2 = 1.03$
- B2 からサンプリングした部品 A（$n_2=8$個）の重さの不偏分散 $s_2^2 = 4.30$

機械 B1, B2 が作る部品の重さがそれぞれ正規分布 $N(\mu_1, \sigma_1), N(\mu_2, \sigma_2)$ に従うと仮定する場合、有意水準 $\alpha=0.05$ として、機械 B1, B2 が作る部品の重さの真の分散 $\sigma_1^2, \sigma_2^2$ は等しいと言えるか？

#### 帰無仮説・対立仮説の設定

- 帰無仮説 $H_0$：機械 B1, B2 が作る部品の重さの分散は等しい（$\sigma_1^2 = \sigma_2^2$）
- 対立仮説 $H_1$：機械 B1, B2 が作る部品の重さの分散は等しくない（$\sigma_1^2 \ne \sigma_2^2$）

#### 検定統計量の選定

部品の重さは正規分布に従うから、その標本不偏分散 $s_1^2, s_2^2$ について

$$
F := \cfrac{s_1^2 / \sigma_1^2}{s_2^2 / \sigma_2^2}
\sim F(n_1-1, n_2-1)
$$

は $F(n_1-1, n_2-1)$ に従う。$n_1=11, n_2=8$ なので、

$$
F \sim F(10, 7)
$$

これを検定統計量として用いる。

#### 棄却域の計算

有意水準 $\alpha = 0.05$ の両側検定であるから、検定統計量 $F$ が
- $F(10, 7)$ の下側2.5%点 $F_{0.975}(10,7)$ 以上
- かつ、$F(10, 7)$ の上側2.5%点 $F_{0.025}(10,7)$ 以下

の範囲にあれば、帰無仮説 $H_0$ は妥当と言える。  

F 分布表より $F_{0.025}(10,7) = 4.76,\ F_{0.975}(10,7) = 1/F_{0.025}(7,10) = 1/3.95 = 0.253$ と求まるので、帰無仮説 $H_0$ の棄却域は

$$
F \le 0.253, 4.76 \le F
$$

#### 検定統計量の計算

帰無仮説 $\sigma_1^2 = \sigma_2^2$ の元では、検定統計量 $F$ は

$$
F = \cfrac{s_1^2}{s_2^2} = \cfrac{1.03}{4.30} \simeq 0.240
$$

これは棄却域に含まれるので、帰無仮説 $H_0$ は棄却される。

#### 結論

機械 B1, B2 が作る部品の重さの分散は等しいとは言えない。（機械 B2 の方が有意にばらつきが大きい）