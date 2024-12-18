---
title: 方策反復法
title-en: policy iteration
---
# 方策反復法とは

**方策反復法 (Policy iteration)** は、モデルベースの強化学習の手法の1つ。  
状態遷移確率 $T(s'\vert s,a)$ と即時報酬 $R(s,s')$ が既知であるときの Policy ベースの強化学習の手法。  
取りうる全ての状態、行動の集合を $S, A$ として、動的計画法により状態価値 $V(s)\ (s \in S)$ および方策 $\pi(a\vert s)\ (s \in S,\ a \in A)$ を学習する。


# 理論（考え方）

- $T(s'\vert s,a)$：状態 $s$ において行動 $a$ をとったとき、状態 $s'$ に遷移する確率
- $R(s,s')$：状態 $s$ から $s'$ に遷移したときに得られる即時報酬
- $\pi(a\vert s)$：状態 $s$ において行動 $a$ を選択する確率（方策）
- $V_\pi(s)$：状態 $s$ から方策 $\pi$ に基づいて行動を決定するときの状態 $s$ の価値
- $\gamma$：未来の予測の不確実性を表す割引率（$0\lt \gamma \lt 1$）

とすると、**Bellman 方程式** は以下のようになる（導出の詳細は[強化学習概観](reinforcement-learning-overview.md)を参照）。  

$$
V_\pi(s)
=
\sum_a \pi(a \vert s) \sum_{s'} T(s' \vert s,a)
\left\{ R(s,s') + \gamma\ V_\pi(s') \right\}
\tag{1}
$$

まず、方策 $\pi(a\vert s)$ の初期値としてランダムな値を設定。
ただし、確率なので $0\lt\pi(a\vert s),\ \sum_a\pi(a\vert s) = 1$ となるようにする。

## 方策の評価

まずは方策 $\pi(a\vert s)$ を評価するため、この $\pi$ のもとでの各状態 $s$ の価値 $V_\pi(s)$ を求めたい。  
[価値反復法](value-iteration.md)と同様に、動的計画法で状態価値を計算する。

すべての状態 $s$ について、状態価値の初期値 $V_\pi^0(s)=0$ を設定する。  
強化学習が想定する状況では、状態の遷移を繰り返すことで報酬を得ていくので、$V_\pi^0(s)$ は **「各状態 $s$ から0ステップ先までの遷移した（つまり1度も遷移しない）ときの報酬」** と言い換えることができる。

次に、Bellman 最適方程式 $(1)$ を少し書き換えた以下の漸化式を考える：

$$
V^{i+1}_\pi(s)
=
\sum_a \pi(a \vert s) \sum_{s'} T(s' \vert s,a)
\left\{ R(s,s') + \gamma\ V_\pi^i(s') \right\}
\tag{1'}
$$

これを使って $V_\pi^0(s)$ から $V_\pi^1(s)$ を計算すると、右辺の $V_\pi^i(s')=V_\pi^0(s')$ 部分はゼロになるので、

$$
V_\pi^1(s) =
\sum_a \pi(a \vert s) \sum_{s'} T(s' \vert s,a)
R(s,s')
$$

式の通り、$V_\pi^1(s)$ は **「各状態 $s$ から方策 $\pi$ に従って1ステップ先まで遷移したときに得られる報酬の期待値」** となっている。

次に $V_\pi^1(s)$ から $V_\pi^2(s)$ を計算すると、

$$
V_\pi^2(s) =
\sum_a \pi(a \vert s)
\sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s') + \gamma\ V_\pi^1(s')
\right\}
$$

右辺について、
- $R(s,s')$ は $s\to s'$ の遷移で得られる即時報酬
- $V_\pi^1(s')$ は方策 $\pi$ にしたがって状態 $s'$ から1ステップだけ遷移したときの報酬期待値

であるから、$V_\pi^2(s)$ は **「各状態 $s$ から方策 $\pi$ に従って2ステップ先まで遷移したときに得られる報酬の期待値」** となる。

同様に漸化式 $(1')$ から $V_\pi^3(s),V_\pi^4(s),V_\pi^5(s),\cdots$ を計算していくと、$V_\pi^i(s)$ は **「各状態 $s$ から方策 $\pi$ に従って $i$ ステップ先まで遷移したときに得られる報酬の期待値」** となることが分かる。

$i\to \infty$ とすれば状態価値の定義そのものとなるが、現実的には無限回の計算はできないので、値がある程度収束した時点で計算を終了する必要がある。

計算を繰り返すほど $V_\pi^i(s)$ の値が正しい状態価値 $V_\pi(s)$ に近づいていくことは数学的に証明されている（らしい）ので、各計算ステップで

$$
\Delta (s) := \vert V_\pi^i(s) - V_\pi^{i-1}(s) \vert
$$

を計算し、全ての $s$ について $\Delta (s) \lt \varepsilon$となったら処理を終了し、最後の $V_\pi^i(s)$ を状態価値 $V_\pi(s)$ として採用する（$\varepsilon$ は収束条件を設定するための微小なハイパーパラメータ）。


## 方策の更新

前節で評価した状態価値 $V_\pi(s)$ に基づいて、各状態 $s$ における行動価値

$$
Q_\pi(s,a) :=
\sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s') + \gamma\ V_\pi(s')
\right\}
\tag{2}
$$

を計算する（詳細は[強化学習概観](reinforcement-learning-overview.md)を参照）。  
この行動価値 $Q_\pi(s,a)$ を用いて、事前に決めた行動選択方式に基づいて、方策を更新する。

方策の更新方法としては以下のようなものがあり、状況に応じて選択する：

| 行動選択の方式           | 説明                                                                                                                          |
| :---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| greedy 行動選択       | 行動価値が最も高い行動を常に選択する                                                                                                          |
| ε-greedy 行動選択     | $0\lt \varepsilon \lt 1$ の確率でランダムな行動を選択し、$1-\varepsilon$ の確率で行動価値が最も高い行動を選択する                                               |
| softmax 行動選択      | 行動価値が高い行動ほど高い確率で選択する<br>$\pi(a\vert s) = \cfrac{\exp(Q(s,a)/T)}{\sum_{a'} \exp(Q(s,a')/T)}$<br>$T$：温度と呼ばれ、確率の傾斜の度合いを表すパラメータ |
| エントロピー正則化行動選択<br> |                                                                                                                             |
| ソフト行動選択           |                                                                                                                             |

greedy な方策改善を行う場合、常に期待値が最大になるよう行動するので、得られる結果は[価値反復法](value-iteration.md)の場合と同じになる？（要確認）


## 方策の評価・更新の繰り返し

更新前後の $\pi(a\vert s)$ を比較して収束するまで、前2節の方策評価・方策更新を繰り返し、最後に得られた方策 $\pi(a\vert s)$ を採用する。

$$
\Delta(\pi) := \left\vert \pi^\mathrm{after}(a\vert s) - \pi^\mathrm{before}(a\vert s) \right\vert \lt \varepsilon\quad(0\lt \varepsilon \ll 1)
$$


# アルゴリズム

前節の議論から得られた計算手法を整理する。

1. すべての状態 $s\in S$ と行動 $a\in A$ について、方策 $\pi(a\vert s)$ をランダムな値で初期化
2. 方策 $\pi(a\vert s)$ を評価
    1. $i \gets 0$
    2. すべての状態 $s \in S$ について、初期値 $V_\pi^0(s)=0$ を設定
    3. $i \gets i+1$
    4. すべての $s \in S$ について、漸化式 $(1')$ により $V_\pi^{i-1}(s)$ から $V_\pi^i(s)$ を計算
    5. $\Delta(s) := \vert V_\pi^i(s) - V_\pi^{i-1}(s) \vert$ の値を求める
    6. すべての $s$ について $\Delta(s) \lt \varepsilon$ となったら反復処理を終了して次へ、そうでなければ3へ戻る
    7. 最後に計算した $V_\pi^i(s)$ の値を各状態の価値とみなす
3. 方策 $\pi(a\vert s)$ を更新
    1. 現在の方策 $\pi(a\vert s)$ に基づいて $(2)$ 式から行動価値 $Q(s,a)$ を計算
    2. 行動選択の方式に従って方策 $\pi(a\vert s)$ を更新
4. 更新前後の $\pi(a\vert s)$ を比較し、収束条件を満たせば次へ、満たさなければ2に戻る
5. 最後に計算した $\pi(a\vert s)$ を最終的な方策として採用


# 実装

迷路を走破して報酬を得る例。

{% gist 75c0f582b9d50c1944c664916ca6bf00 ~settings.py %}

{% gist 75c0f582b9d50c1944c664916ca6bf00 ~policy-iteration-maze.py %}

```python
states = [
    State(0, 0), State(0, 1), State(0, 2), State(0, 3, 1.0, is_goal=True),
    State(1, 0), State(1, 2), State(1, 3, -1.0, is_goal=True),
    State(2, 0), State(2, 1), State(2, 2), State(2, 3)
]
actions = [Action(0, 1), Action(0, -1), Action(1, 0), Action(-1, 0)]
environment = Environment(states, actions)
# シミュレーション & 結果の描画
planner = PolicyBasePlanner(environment)
planner.plan(mode=PolicyBasePlanner.ActionSelectMode.SOFTMAX)
V, policy = planner.V, planner.policy
A = {s:max(policy[s], key=policy[s].get) for s in states}
draw_result(environment, V, A)
```

![policy-iteration-1](https://gist.github.com/user-attachments/assets/9646e87e-5c6e-442a-8a4b-c917563f91c8)


```python
planner = PolicyBasePlanner(environment)
planner.plan(mode=PolicyBasePlanner.ActionSelectMode.GREEDY)
V, policy = planner.V, planner.policy
A = {s:max(policy[s], key=policy[s].get) for s in states}
draw_result(environment, V, A)
```

![policy-iteration-2](https://gist.github.com/user-attachments/assets/9f410747-d3c5-42f4-b89c-cd00353cc748)
