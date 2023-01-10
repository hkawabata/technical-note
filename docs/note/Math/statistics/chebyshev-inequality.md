---
title: チェビシェフの不等式
title-en: Chebyshev's inequality
---

# 定義

確率変数 $X$ が平均 $\mu$、分散 $\sigma^2$ の確率分布に従うとき、任意の定数 $k$ に対して、**チェビシェフの不等式**

$$
P(|X - \mu| \ge k \sigma) \le \cfrac{1}{k^2}
$$

が成り立つ。$k\sigma \to k$ とおきかえれば、

$$
P(|X - \mu| \ge k) \le \cfrac{\sigma^2}{k^2}
$$

と書くこともできる。

# 解釈

チェビシェフの不等式左辺の確率の条件

$$
|X - \mu| \ge k \sigma
$$

は、「$X$ が、平均値（期待値）$\mu$ から標準偏差 $\sigma$ の $k$ 倍以上離れた値を取る」と解釈できる。

チェビシェフの不等式右辺の $\cfrac{1}{k^2}$ はこの条件が満たされる確率の上限を定めている。

したがってチェビシェフの不等式は、**「確率変数 $X$ が平均値（期待値）から一定以上外れた値を取る割合の上限」** を与える不等式になっている。


# 利用法

ある確率変数 $X$ について、
- 正確な確率分布は不明だが、
- 十分な数のデータサンプルが集まり、平均 $\mu$ と分散 $\sigma^2$ が求められている

ような場合に、$X$ の値が一定範囲内に収まる確率の上限値・下限値を求めるのに役立つ。

→ ex.「母集団の正確な分布か分からないが、**$X$ の値はが平均値から10以上外れる確率は最悪の場合でも5%以下**」のような見積もりができる。

## 例題1

- $\mu = 5$
- $\sigma^2 = 4 \quad (\therefore \sigma = 2)$

であり正確な確率分布が不明な確率変数 $X$ の実現値が、$X \le 2$ あるいは $8 \le X$ となる最大の確率を求める。

問題を言い換えると、$X$ が平均値から $\pm 3$ 以上、すなわち $\pm 1.5 \sigma$ 以上離れる確率を求めれば良いから、チェビシェフの不等式に $k=1.5$ を代入すると、

$$
P(|X - 5| \ge 3) \le \cfrac{1}{1.5^2} = 0.444\cdots
$$

したがって、求める最大確率は 0.444。

## 例題2

- $\mu = -7$
- $\sigma^2 = 1 \quad (\therefore \sigma = 1)$

であり正確な確率分布が不明な確率変数 $X$ の実現値が、$-9 \le X \le -5$ となる最小の確率を求める。

問題を言い換えると、$X$ が平均値から $\pm 2$ 以内、すなわち $\pm 2 \sigma$ 以内の範囲に収まる確率を求めれば良いから、チェビシェフの不等式に $k = 2$ を代入すると

$$
P(|X + 7| \ge 2) \le \cfrac{1}{2^2} = 0.25
$$

求める確率はこの式の左辺の余事象である $P(|X + 7| \le 2)$ なので、式変形して

$$
P(|X + 7| \le 2) = 1 - P(|X + 7| \ge 2) \ge 0.25
$$

したがって、求める最小確率は 0.25。

# 証明

分散の定義より、確率密度関数を $f(x)$ とすれば、

$$
\sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx
$$

積分区間を $\mu \pm k \sigma$ で区切って、

$$
\begin{eqnarray}
  \sigma^2 &=& \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx \\
  &=&
    \int_{-\infty}^{\mu - k \sigma} (x - \mu)^2 f(x) dx +
    \int_{\mu - k \sigma}^{\mu + k \sigma} (x - \mu)^2 f(x) dx +
    \int_{\mu + k \sigma}^{\infty} (x - \mu)^2 f(x) dx \\
  &\ge&
    \int_{-\infty}^{\mu - k \sigma} (x - \mu)^2 f(x) dx +
    \int_{\mu + k \sigma}^{\infty} (x - \mu)^2 f(x) dx
\end{eqnarray}
$$

最後の不等式導出では、$(x-\mu)^2$ および確率密度関数 $f(x)$ がともに非負であるため積分値も非負となることを用いた。

最後の式の積分区間では $x \le \mu - k \sigma$ または $\mu + k \sigma \le x$、すなわち $|x-\mu| \ge k \sigma$ であるから、

$$
(x - \mu)^2 \ge (k\sigma)^2
$$

したがって、

$$
\begin{eqnarray}
  \sigma^2
  &\ge&
    \int_{-\infty}^{\mu - k \sigma} (x - \mu)^2 f(x) dx +
    \int_{\mu + k \sigma}^{\infty} (x - \mu)^2 f(x) dx \\
  &\ge&
    \int_{-\infty}^{\mu - k \sigma} (k \sigma)^2 f(x) dx +
    \int_{\mu + k \sigma}^{\infty} (k \sigma)^2 f(x) dx \\
  &=&
    (k \sigma)^2
    \left(
      \int_{-\infty}^{\mu - k \sigma} f(x) dx +
      \int_{\mu + k \sigma}^{\infty} f(x) dx
    \right) \\
  &=&
    (k \sigma)^2
    (
      P(x \le \mu - k \sigma) +
      P(x \ge \mu + k \sigma)
    ) \\
  &=&
    (k \sigma)^2 P(|x - \mu| \ge k \sigma)
\end{eqnarray}
$$

この両辺を $k^2 \sigma^2$ で割ればチェビシェフの不等式を得る。