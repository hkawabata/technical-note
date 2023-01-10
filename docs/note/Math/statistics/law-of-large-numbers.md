---
title: 大数の法則
---

= Law of Large Numbers

# 大数の法則とは

試行回数を多くすればするほど（サンプルが多いほど）データの平均値は真の平均値に近づく、という法則。

# 証明

※ 数学的な厳密性はやや怪しめ。

確率変数 $X$ が以下を満たす母集団に属するとする。
- 期待値 $E(X) = \mu$
- 分散 $V(X) = \sigma^2$

ここから $n$ 個の標本を無作為に復元抽出したときの標本平均 $\bar{X}_n$ は、

$$
\bar{X}_n = \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i
$$

この $\bar{X}_n$ を新たな確率変数とみなしたとき、その期待値と分散は

$$
\begin{eqnarray}
  E(\bar{X}_n) &=& E \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} E(X_i) \\
  &=& \cfrac{1}{n} \displaystyle \sum_{i=1}^{n} \mu \\
  &=& \cfrac{1}{n} n\mu = \mu
\end{eqnarray}
$$

$$
\begin{eqnarray}
  V(\bar{X}_n) &=& V \left( \displaystyle \cfrac{1}{n} \sum_{i=1}^{n} X_i \right) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} V(X_i) \\
  &=& \cfrac{1}{n^2} \displaystyle \sum_{i=1}^{n} \sigma^2 \\
  &=& \cfrac{1}{n^2} n \sigma^2 = \cfrac{\sigma^2}{n}
\end{eqnarray}
$$

よって、[チェビシェフの不等式](chebyshev-inequality.md)

$$
P(|X - \mu| \ge k) \le \cfrac{\sigma^2}{k^2}
$$

で $X \to \bar{X}_n$ と置き換えると、$\mu \to \mu$、$\sigma^2 \to \cfrac{\sigma^2}{n}$ であるから

$$
P \left(|\bar{X}_n - \mu| \ge k \right) \le \cfrac{\sigma^2}{n k^2}
$$

これと余事象の式から、

$$
P \left(|\bar{X}_n - \mu| \lt k \right)
=
1 - P \left(|\bar{X}_n - \mu| \ge k \right)
\ge
1 - \cfrac{\sigma^2}{n k^2}
$$

両辺で $n \to \infty$ の極限を取ると、

$$
\lim_{n \to \infty} P \left(|\bar{X}_n - \mu| \lt k \right) \ge 1
$$

確率は1を超えないので、

$$
\lim_{n \to \infty} P \left(|\bar{X}_n - \mu| \lt k \right) = 1
$$

$k$ は任意の定数であるから、任意の十分小さい正数を取れる。
したがって、「$n$ を十分大きく取れば、$\bar{X}_n$ の値が $\mu$ を取る確率が1に近づく」と言える。


# 実験

ランダムにサイコロを振り、試行回数が増えるほど平均値が3.5に近づく様子を観測する。

```python
import numpy as np
from matplotlib import pyplot as plt

N = 5000
dice = np.random.randint(1, 6+1, N)
sum_of_dice = 0
ave = []
for i in range(N):
	sum_of_dice += dice[i]
	ave.append(sum_of_dice/(i + 1))

plt.xlabel('Number of Trial')
plt.ylabel('Average of Value')
plt.axhline(y=3.5, color='red')
plt.plot(ave)
plt.grid()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/211140859-196c1377-a26e-4a3a-a239-baf2f0ca4958.png)
