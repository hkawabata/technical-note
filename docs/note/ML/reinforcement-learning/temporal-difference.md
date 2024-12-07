---
title: TD 法・Monte Carlo 法
title-en: TD-Learning, Monte Carlo Method
---
# TD 法・Monte Carlo 法とは

**TD 法（Temporal Difference Learning）**、**Monte Carlo 法** は、モデルフリーの強化学習手法の1つ。

# 理論（考え方）

## TD 法

ある時点において、各状態 $s$ の価値評価の見積もりを $V(s)$ とする。$V(s)$ は状態 $s$ から行動したときに得られる報酬の期待値（の見積もり）を表す。

ここで、実際に状態 $s$ から行動 $a$ を取った結果、報酬 $r$ を得て状態 $s'$ に遷移したとする。  
すると、実際に得られた価値は見積もった期待値である $V(s)$ ではなく、$r+\gamma V(s')$ ということになる（$0\lt\gamma\lt 1$ は未来の見積もりの不確実性に対する割引率）。すなわち、

$$
r+\gamma V(s') - V(s)
$$

は見積もりの誤差と考えられる（**Temporal Difference Error, TD 誤差**）。

この誤差を使って価値評価の見積もり $V(s)$ を修正する：

$$
V(s) \gets V(s) + \alpha \left\{ r+\gamma V(s') - V(s) \right\}
$$

ここで、$0\lt\alpha$ は学習率。

実際に行動して得られた報酬を用いて $V(s)$ の修正を繰り返すことで、$V(s)$ を真の値に近づけていく。

ここまでの議論では、1回だけ遷移した結果から誤差を考えて $V(s)$ の値にフィードバックしたが、遷移回数を1回に限らず、複数回遷移して得られた結果を使うこともできる。  
時刻 $t$ から1回、2回、3回、...、$n$ 回と遷移（$s_t \to s_{t+1} \to s_{t+2} \to \cdots \to s_{t+n}$）してみたとき、得られた即時報酬を $r_{t+1},r_{t+2},\cdots,r_{t+n}$ とすると、得られた価値の実現値 $G_t^{(n)}$ は以下のようになる：

$$
\begin{eqnarray}
    G_t^{(1)} &=& r_{t+1} + \gamma V(s_{t+1}) \\
    G_t^{(2)} &=& r_{t+1} + \gamma r_{t+2} + \gamma^2 V(s_{t+2}) \\
    G_t^{(3)} &=& r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 V(s_{t+3}) \\
    G_t^{(4)} &=& r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 r_{t+4} + \gamma^4 V(s_{t+4}) \\
    && \vdots \\
    G_t^{(n)} &=& r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 r_{t+4} + \cdots + \gamma^{n-1} r_{t+n} + \gamma^n V(s_{t+n}) 
\end{eqnarray}
$$

これと状態価値の事前見積もり $V(s_t)$ との誤差を用いて

$$
V(s_t) \gets V(s_t) + \alpha \left\{ r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 r_{t+4} + \cdots + \gamma^{n-1} r_{t+n} + \gamma^n V(s_{t+n}) - V(s_t) \right\}
$$

により価値評価 $V(s)$ を更新する手法を **Multistep Learning** という。  


## Monte Carlo 法

Multistep Learning において、特に状態遷移できる回数に上限がある（エピソードの終了時刻 $T$ が存在する）場合に、1エピソード分の遷移を使って価値評価を更新（$n=T-t$）すると、

$$
V(s_t) \gets V(s_t) + \alpha \left\{ r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 r_{t+4} + \cdots + \gamma^{T-t-1} r_T + \gamma^{T-t} V(s_T) - V(s_t) \right\}
$$

ここで、時刻 $T$ でエピソードは終了するため、時刻 $T$ より先の状態価値 $V(s_T)$ はゼロとして良い。したがって、

$$
V(s_t) \gets V(s_t) + \alpha \left\{ r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \gamma^3 r_{t+4} + \cdots + \gamma^{T-t-1} r_T - V(s_t) \right\}
$$

これを、**Monte Carlo 法** という。


## TD (λ) 法

TD 法の Multistep Learning では、最も学習がうまくいくようなステップ数 $n$ を選ぶことは容易ではない。  
固定された $n$ ステップの遷移を使うのではなく、いろいろなステップ数の遷移の結果の重み付け平均を取って利用する手法として **TD (λ) 法** がある。

パラメータ $0 \lt \lambda \lt 1$ を導入し、$G_t^{(1)},G_t^{(2)},\cdots,G_t^{(T-t)}$ に関して以下の重み付き平均を取る：

$$
G_t^\lambda := (1-\lambda) \sum_{n=1}^{T-t-1} \lambda^{n-1} G_t^{(n)} + \lambda^{T-t-1} G_t^{(T-t)}
$$

価値評価 $V(s)$ の更新式は、

$$
V(s_t) \gets V(s_t) + \alpha \left\{G_t^\lambda - V(s_t) \right\}
$$

> **【NOTE】**
> 
> $G_t^\lambda$ 定義式の右辺第一項の $1-\lambda$ は、$G_t^{(n)}$ の重み係数の合計が1になるようにかけてある：
>
> $$
\begin{eqnarray}
    &&(1-\lambda)(1 + \lambda + \lambda^2 + \cdots + \lambda^{T-t-2}) + \lambda^{T-t-1} \\
    &=&
    (1 + \lambda + \lambda^2 + \cdots + \lambda^{T-t-2}) - (\lambda + \lambda^2 + \lambda^3 + \cdots + \lambda^{T-t-2} + \lambda^{T-t-1}) + \lambda^{T-t-1} \\
    &=& 1
\end{eqnarray}
$$
