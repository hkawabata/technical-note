---
title: 尖度
title-en: kurtosis
---

# 尖度とは

確率変数の確率密度関数や度数分布の鋭さを表す指標。  
正規分布では値が3になるので、
- 尖度が3以上：正規分布よりも尖っている
- 尖度が3以下：正規分布よりも扁平

という形で正規分布を基準として利用されることが多い。

確率変数 $X$ の期待値を $\mu$、標準偏差を $\sigma$ として、

$$
E\left( \left( \cfrac{X - \mu}{\sigma} \right)^4 \right) =
\cfrac{1}{n} \displaystyle \sum_{i=1}^{n} \left( \cfrac{X_i - \mu}{\sigma} \right)^4
$$

で定義される。$X$ を標準化した確率変数

$$
Z \equiv \cfrac{X - \mu}{\sigma}
$$

を導入すれば、$Z$ の4次のモーメントの形で表現することもできる：

$$
E(Z^4) = M''''_Z(0)
$$

cf. [モーメント母関数](moment-generating-function.md)
