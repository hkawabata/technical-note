---
title: ε-greedy アルゴリズム
title-en: epsilon-greedy algorithm
---

# ε-greedy とは

強化学習において、多腕バンディット問題を解くためのアルゴリズムの1つ。


# 問題設定

- $n$ 本の arm（スロットマシンの腕）$a_1, \cdots, a_n$ がある
- 各 arm から報酬1が得られる確率 $p_1, \cdots, p_n$ は同じとは限らない（未知）
- arm のうち1つを選んでスロットを回す試行を全 $T$ 回実施
- 得られる報酬の総量がなるべく大きくなるように arm の選び方を決めたい

# アルゴリズム

ハイパーパラメータ $0 \lt \varepsilon \lt 1$ を導入し、以下の試行を繰り返す。
- 確率 $\varepsilon$ でランダムな arm を選択（= 探索, exploration）
- 確率 $1-\varepsilon$ でその時点の最適な arm を選択（= 活用, exploitation）
    - 最適な arm ：例えば、それまでの探索・活用で最も平均報酬が高かった arm


# 課題

- 最適な $\varepsilon$ を設定しないと探索が不足したり、逆に探索しすぎて十分な活用ができない
    - しかし実用的な問題において「最適な $\varepsilon$」 は未知
- ランダム性を持つ手法であるため、同じ問題設定やパラメータで複数回実行すると結果が異なる可能性がある

→ $\varepsilon$ の値を動的に変更する改善アルゴリズムも存在


# 実装

{% gist 3294454bfd0c3f0930a253e7a8b63471 ~epsilon-greedy.py %}

## 各 arm の信頼区間の収束を確認

{% gist 3294454bfd0c3f0930a253e7a8b63471 ~exp-confidence-interval.py %}

```python
>>> ps = [0.4, 0.5, 0.6, 0.7]
>>> eg = EpsilonGreedy()
>>> eg.execute(ps, 10000, 0.3)

===== Settings =====
epsilon           : 0.3
arm-probabilities : [0.4, 0.5, 0.6, 0.7]
epochs            : 10000

===== Result =====
best arm     : 3
total reward : 6406
    
    --- arm 0
    probability   : 0.4
    number of try : 987
    reward sum    : 420
    reward ave    : 0.42553 +/- 0.03085 (95% CI)
    
    --- arm 1
    probability   : 0.5
    number of try : 1021
    reward sum    : 505
    reward ave    : 0.49461 +/- 0.03067 (95% CI)
    
    --- arm 2
    probability   : 0.6
    number of try : 1045
    reward sum    : 621
    reward ave    : 0.59426 +/- 0.02977 (95% CI)
    
    --- arm 3
    probability   : 0.7
    number of try : 6947
    reward sum    : 4860
    reward ave    : 0.69958 +/- 0.01078 (95% CI)
```

![eps-greedy-ave](https://gist.github.com/assets/13412823/fde8d834-f20c-4fa9-a0aa-eec7aabd8775)

- 試行回数が増えるほど、各 arm で報酬を得る推定確率の信頼区間が収束
- 割と早めに信頼区間が収束している
    - arm 同士を比べた時に95%信頼区間がハッキリ分離していれば性能が低い方の arm を早めに切り捨てる（それ以降探索しない）、という手法で性能を改善できそう


## total regret の増加が鈍化することを確認


{% gist 3294454bfd0c3f0930a253e7a8b63471 ~exp-total-regret.py %}

![eps-greedy-regret](https://gist.github.com/assets/13412823/2a863e66-e582-471b-b45b-151ac2071959)

この実験では、試行回数1000を少し超えたあたりで最適な arm の選択が完了し、時間あたりの regret 増加速度が鈍化しているのが分かる。


## ε の値による収束までの時間の違いを確認

{% gist 3294454bfd0c3f0930a253e7a8b63471 ~exp-various-epsilon.py %}

![eps-greedy-various-epsilon](https://gist.github.com/assets/13412823/b34bf7de-db69-4591-9ea5-f8da71b16ecf)

- 短期的には、$\varepsilon$ が大きいモデルほど total reward が大きい
    - 探索の割合が大きいので、正しい arm の選択が素早く収束する
- 長期的には、$\varepsilon$ が小さいモデルほど total reward が大きい
    - 時間が経つと、どのモデルも十分に探索され、活用において最適な arm を選ぶようになる
    - 結果、適切な arm を活用する割合が大きい（$\varepsilon$ が小さい）モデルほど最適な arm が多く選ばれる
