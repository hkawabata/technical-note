---
title: モーメント母関数（積率母関数）
title-en: Moment-Generating Function
---

# モーメント（積率）とは

確率変数 $X$ の確率分布 $f(X)$ の平均値やばらつき、ひずみ、尖度を数値化する特性値。


# モーメント母関数とは

適切な処理を施すことで各種モーメントを簡単に計算することができる「モーメントを生み出す関数」。

以下の式で定義される。

$$
M_X(t) \equiv E(e^{tX}) = \int_{-\infty}^{\infty} e^{tX} f(X) dX
$$

ここで、$E$ は期待値を表す。


# モーメント母関数の性質

## 確率分布関数との関係

虚数に拡張してフーリエ逆変換を使うことで、モーメント母関数から確率分布関数 $f(x)$ を一意に計算できる（証明略）。

したがって、**確率分布関数とモーメント母関数は1対1で対応しており、モーメント母関数を求めることは、確率分布を求めることと等しい。**

## 平均・分散との関係

モーメント母関数の定義式において、$e^{tX}$ の $t$ についてのマクローリン展開を適用すると、

$$
\begin{eqnarray}
  M_X(t) &=& E(e^{tX})
  \\ &=&
  E \left(
    1 + \cfrac{X}{1!} t + \cfrac{X^2}{2!} t^2 + \cdots
  \right)
\end{eqnarray}
$$

期待値の線形性から、

$$
M_X(t) = 1 + \cfrac{E(X)}{1!} t + \cfrac{E(X^2)}{2!} t^2 + \cdots
$$

これを $t$ で $n$ 回微分すると、$t$ の $(n-1)$ 次以下の項は消えて、

$$
\cfrac{d^n M_X}{dt^n} (t) =
E(X^n) +
\cfrac{E(X^{n+1})}{1!}t +
\cfrac{E(X^{n+2})}{2!}t^2 + \cdots
$$

この式に $t=0$ を代入すると、

$$
\cfrac{d^n M_X}{dt^n} (0) = E \left( X^n \right)
$$

よって、**モーメント母関数の $n$ 階微分にゼロを代入すると $X^n$ の期待値を得る。**
$E(X), E(X^2)$ を計算すれば、分散 $V(X) = E(X^2) - E(X)^2$ も計算できる。


# 具体例

## 正規分布

確率分布関数は

$$
f(X) =
\cfrac{1}{\sqrt{2\pi}\sigma}
\exp{
  \left(
    - \cfrac{(X-\mu)^2}{2\sigma^2}
  \right)
}
$$

モーメント母関数は

$$
\begin{eqnarray}
  M_X(t)
  &=&
  \int_{-\infty}^{\infty} e^{tX} f(X) dX
  \\ &=&
  \cfrac{1}{\sqrt{2\pi}\sigma}
  \int_{-\infty}^{\infty} \exp{
    \left(
      tX - \cfrac{(X-\mu)^2}{2\sigma^2}
    \right)
  } dX
  \\ &=&
  \cfrac{1}{\sqrt{2\pi}\sigma}
  \exp{\left(
    \mu t + \cfrac{\sigma^2 t^2}{2}
  \right)}
  \int_{-\infty}^{\infty} \exp{
    \left(
      - \cfrac{\left(X-(\mu + \sigma^2 t)\right)^2}{2\sigma^2}
    \right)
  } dX
  \\ &=&
  \cfrac{1}{\sqrt{2\pi}\sigma}
  \exp{\left(
    \mu t + \cfrac{\sigma^2 t^2}{2}
  \right)}
  \sqrt{2 \pi \sigma}
  \\ &=&
  \exp{\left(
    \mu t + \cfrac{\sigma^2 t^2}{2}
  \right)}
\end{eqnarray}
$$

$t$ で微分すると、

$$
M'_X(t) = \left( \mu + \sigma^2 t \right)
\exp{\left(
  \mu t + \cfrac{\sigma^2 t^2}{2}
\right)}
$$

$$
M''_X(t) = \left(
  \sigma^2 + \left( \mu + \sigma^2 t \right)^2
\right)
\exp{\left(
  \mu t + \cfrac{\sigma^2 t^2}{2}
\right)}
$$

よって

$$
E(X) = M'_X(0) = \mu
$$

$$
E(X^2) = M''_X(0) = \sigma^2 + \mu^2
$$

$$
V(X) = E(X^2) - E(X)^2 = \sigma^2
$$


## 指数分布

確率分布関数は $\lambda \gt 0$ を用いて以下の式で書ける。

$$
f(X) =
\begin{cases}
  \lambda e^{-\lambda X} & & X \ge 0 \\
  0 & & X \lt 0
\end{cases}
$$

モーメント母関数は

$$
\begin{eqnarray}
  M_X(t)
  &=&
  \int_{-\infty}^{\infty} e^{tX} f(X) dX
  \\ &=&
  \lambda \int_{0}^{\infty} e^{tX-\lambda X} dX
  \\ &=&
  \lambda \int_{0}^{\infty} e^{-(\lambda-t)X} dX
  \\ &=&
  \cfrac{\lambda}{\lambda - t}
\end{eqnarray}
$$

ただし途中、積分が発散しないための条件として $\lambda \gt t$ を課している。

$t$ で微分すると、

$$
M'_X(t) = \cfrac{\lambda}{(\lambda - t)^2}
$$

$$
M''_X(t) = \cfrac{2 \lambda}{(\lambda - t)^3}
$$

よって

$$
E(X) = M'_X(0) = \cfrac{1}{\lambda}
$$

$$
E(X^2) = M''_X(0) = \cfrac{2}{\lambda^2}
$$

$$
V(X) = E(X^2) - E(X)^2 = \cfrac{1}{\lambda^2}
$$

## 一様分布

確率分布関数は $a \lt b$ である定数 $a, b$ を用いて以下の式で書ける。

$$
f(X) = \begin{cases}
0 & X \lt a, b \lt X
\\
\cfrac{1}{b-a}& a \le X \le b
\end{cases}
$$

モーメント母関数は

$$
\begin{eqnarray}
  M_X(t)
  &=&
  \int_{-\infty}^{\infty} e^{tX} f(X) dX
  \\ &=&
  \cfrac{1}{b-a} \int_{a}^{b} e^{tX} dX
  \\ &=&
  \cfrac{1}{b-a} \cfrac{e^{tb} - e^{ta}}{t}
\end{eqnarray}
$$

$t$ で微分すると、

$$
\begin{eqnarray}
  M'_X(t) &=& \cfrac{1}{b-a}
  \cfrac{(be^{bt}-ae^{at})t - (e^{bt}-e^{at})}{t^2}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{(bt-1)e^{bt}-(at-1)e^{at}}{t^2}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  M''_X(t) &=& \cfrac{1}{b-a}
  \cfrac{(b^2te^{bt}-a^2te^{at})t^2 - ((bt-1)e^{bt}-(at-1)e^{at})2t}{t^4}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{(b^2t^2-2bt+2)e^{bt}-(a^2t^2-2at+2)e^{at}}{t^3}
\end{eqnarray}
$$

$M'_X(t), M''_X(t)$ ともに $t=0$ を代入すると分母・分子がともに0になってしまい、単純な代入ができない。
そのため、[ロピタルの定理](../calculus/lhopital-theorem.md)を用いて極限を求める。

$$
\begin{eqnarray}
  E(X) = \lim_{t \to 0} M'_X(t) &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{((bt-1)e^{bt}-(at-1)e^{at})'}{(t^2)'}
  \\ &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{b^2te^{bt}-a^2te^{at}}{2t}
  \\ &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{b^2e^{bt}-a^2e^{at}}{2}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{b^2-a^2}{2}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{(b-a)(b+a)}{2}
  \\ &=&
  \cfrac{a+b}{2}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  E(X^2) = \lim_{t \to 0} M''_X(t) &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{((b^2t^2-2bt+2)e^{bt}-(a^2t^2-2at+2)e^{at})'}{(t^3)'}
  \\ &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{b^3t^2e^{bt}-a^3t^2e^{at}}{3t^2}
  \\ &=&
  \cfrac{1}{b-a} \lim_{t \to 0}
  \cfrac{b^3e^{bt}-a^3e^{at}}{3}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{b^3-a^3}{3}
  \\ &=&
  \cfrac{1}{b-a}
  \cfrac{(b-a)(b^2+ab+a^2)}{3}
  \\ &=&
  \cfrac{b^2+ab+a^2}{3}
\end{eqnarray}
$$

よって

$$
\begin{eqnarray}
  V(X) &=& E(X^2) - E(X)^2
  \\ &=&
  \cfrac{b^2+ab+a^2}{3} - \left( \cfrac{a+b}{2} \right)^2
  \\ &=&
  \cfrac{b^2-2ab+a^2}{12}
  \\ &=&
  \cfrac{(b-a)^2}{12}
\end{eqnarray}
$$
