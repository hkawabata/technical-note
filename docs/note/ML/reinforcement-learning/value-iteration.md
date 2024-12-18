---
title: 価値反復法
title-en: value iteration
---
# 価値反復法とは

**価値反復法 (Value iteration)** は、モデルベースの強化学習の手法の1つ。  
状態遷移確率 $T(s'\vert s,a)$ と即時報酬 $R(s,s')$ が既知であるときの Value ベースの手法。  
取りうる全ての状態の集合を $S$ として、動的計画法により状態価値 $V(s)\ (s \in S)$ を計算する。

# 理論（考え方）

- $T(s'\vert s,a)$：状態 $s$ において行動 $a$ をとったとき、状態 $s'$ に遷移する確率
- $R(s,s')$：状態 $s$ から $s'$ に遷移したときに得られる即時報酬
- $V_\pi(s)$：状態 $s$ から方策 $\pi$ に基づいて行動を決定するときの状態 $s$ の価値
- $\gamma$：未来の予測の不確実性を表す割引率（$0\lt \gamma \lt 1$）

とすると、常に価値を最大化するように学習する Value ベースの手法では、**Bellman 方程式** は以下のようになる（導出の詳細は[強化学習概観](reinforcement-learning-overview.md)を参照）。  
ここで $\max_a\left\{f(a)\right\}$ は、$a$ に関する $f(a)$ の最大値を表す。

$$
V(s) =
\max_a \left\{ \sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s') + \gamma\ V_\pi(s')
\right\} \right\}
\tag{1}
$$

まず、すべての状態 $s$ について、状態価値の初期値 $V^0(s)=0$ を設定する。  
強化学習が想定する状況では、状態の遷移を繰り返すことで報酬を得ていくので、$V^0(s)$ は **「各状態 $s$ から0ステップ先までの遷移した（つまり1度も遷移しない）ときの報酬」** と言い換えることができる。

次に、Bellman 最適方程式 $(1)$ を少し書き換えた以下の漸化式を考える：

$$
V^{i+1}(s) =
\max_a \left\{ \sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s') + \gamma\ V^i(s')
\right\}
\right\}
\tag{1'}
$$

これを使って $V^0(s)$ から $V^1(s)$ を計算すると、右辺の $V^i(s')=V^0(s')$ 部分はゼロになるので、

$$
V^1(s) =
\max_a \left\{ \sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s')
\right\}
\right\}
$$

式の通り、$V^1(s)$ は **「各状態 $s$ から1ステップ先まで遷移したときに得られる報酬期待値の最大値」** となっている。

次に $V^1(s)$ から $V^2(s)$ を計算すると、

$$
V^2(s) =
\max_a \left\{ \sum_{s'} T(s' \vert s,a)
\left\{
    R(s,s') + \gamma\ V^1(s')
\right\}
\right\}
$$

右辺について、
- $R(s,s')$ は $s\to s'$ の遷移で得られる即時報酬
- $V^1(s')$ は状態 $s'$ から1ステップだけ遷移したときの報酬期待値の最大値

であるから、$V^2(s)$ は **「各状態 $s$ から2ステップ先まで遷移したときに得られる報酬期待値の最大値」** となる。

同様に漸化式 $(1')$ から $V^3(s),V^4(s),V^5(s),\cdots$ を計算していくと、$V^i(s)$ は **「各状態 $s$ から $i$ ステップ先まで遷移したときに得られる報酬期待値の最大値」** となることが分かる。

$i\to \infty$ とすれば状態価値の定義そのものとなるが、現実的には無限回の計算はできないので、値がある程度収束した時点で計算を終了する必要がある。

計算を繰り返すほど $V^i(s)$ の値が正しい状態価値 $V(s)$ に近づいていくことは数学的に証明されている（らしい）ので、各計算ステップで

$$
\Delta (s) := \vert V^i(s) - V^{i-1}(s) \vert
$$

を計算し、全ての $s$ について $\Delta (s) \lt \varepsilon$となったら処理を終了し、最後の $V^i(s)$ を状態価値 $V(s)$ として採用する（$\varepsilon$ は収束条件を設定するための微小なハイパーパラメータ）。


# アルゴリズム

前節の議論から得られた計算手法を整理する。

1. $i \gets 0$
2. すべての状態 $s \in S$ について、初期値 $V^0(s)=0$ を設定
3. $i \gets i+1$
4. すべての $s \in S$ について、漸化式 $(1')$ により $V^{i-1}(s)$ から $V^i(s)$ を計算
5. $\Delta(s) := \vert V^i(s) - V^{i-1}(s) \vert$ の値を求める
6. すべての $s$ について $\Delta(s) \lt \varepsilon$ となったら反復処理を終了して7へ、そうでなければ3へ戻る
7. 最後に計算した $V^i(s)$ の値を各状態の価値とみなす


# 実装

迷路を走破して報酬を得る例。

{% gist 75c0f582b9d50c1944c664916ca6bf00 ~settings.py %}

{% gist 75c0f582b9d50c1944c664916ca6bf00 ~value-iteration-maze.py %}

## 実験1

```python
# 問題のセットアップ
states = [
    State(0, 0), State(0, 1), State(0, 2), State(0, 3, 1.0, is_goal=True),
    State(1, 0), State(1, 2), State(1, 3, -1.0, is_goal=True),
    State(2, 0), State(2, 1), State(2, 2), State(2, 3)
]
actions = [Action(0, 1), Action(0, -1), Action(1, 0), Action(-1, 0)]
environment = Environment(states, actions)
# シミュレーション & 結果の描画
planner = ValueBasePlanner(environment)
planner.plan()
V, A = planner.V, planner.A
draw_result(environment, V, A)
```

![value-iteration-1](https://gist.github.com/user-attachments/assets/8e41b96a-92ab-47c9-bb5a-f75443bcfab1)


## 実験2：近くのゴールが有利になる例

```python
states = [
    State(0, 0), State(0, 1), State(0, 2), State(0, 3, 1.0, is_goal=True),
    State(1, 0), State(1, 2), State(1, 3, -1.0, is_goal=True),
    State(2, 0), State(2, 1), State(2, 2), State(2, 3),
    State(3, 0, 0.9, is_goal=True), State(3, 1), State(3, 2), State(3, 3),
    State(4, 0), State(4, 1), State(4, 3)
]
actions = [Action(0, 1), Action(0, -1), Action(1, 0), Action(-1, 0)]
environment = Environment(states, actions)
planner = ValueBasePlanner(environment)
planner.plan(gamma=0.9)
V, A = planner.V, planner.A
draw_result(environment, V, A)
```

![value-iteration-2](https://gist.github.com/user-attachments/assets/24c4c945-28ba-437d-a317-efa9ca384248)

→ 報酬最大のゴールでなくても、割引率の影響で近くのゴールが優先される効果が働く。


## 実験3：永遠に往復する例

```python
states = [
    State(0, 0), State(0, 1), State(0, 2), State(0, 3, 1.0, is_goal=True),
    State(1, 0), State(1, 2), State(1, 3, -1.0, is_goal=True),
    State(2, 0, reward=0.3), State(2, 1), State(2, 2), State(2, 3)
]
actions = [Action(0, 1), Action(0, -1), Action(1, 0), Action(-1, 0)]
environment = Environment(states, actions)
# シミュレーション & 結果の描画
planner = ValueBasePlanner(environment)
planner.plan()
V, A = planner.V, planner.A
draw_result(environment, V, A)
```

![value-iteration-3](https://gist.github.com/user-attachments/assets/9565aecc-8f8c-4981-9061-9e07f3535557)

→ ゴール以外に報酬ポイントがあると、永遠に往復して何度も報酬を獲得するのが正解になってしまう。
