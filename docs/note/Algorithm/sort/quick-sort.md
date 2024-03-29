---
title: クイックソート
title-en: quick sort
---
# 概要

配列のソートアルゴリズムの1つ。

# アルゴリズム

1. 配列の要素数が1以下ならソート終了
2. 要素数が2以上の場合、配列の要素のうち基準値 $a_\mathrm{pivot}$ を1つ選ぶ
    1. たとえば配列の末尾の要素など
3. 配列の要素を以下の2つに分ける
    1. 【A】$a_\mathrm{pivot}$ 以下のもの
    2. 【B】$a_\mathrm{pivot}$ より大きいもの
4. 部分集合 A, B をソートし、【A】【B】の順に並べる
    1. A, B をソートするにあたって、全く同じ手順1〜4を再帰的に適用する


# 具体例

順序が確定した要素を `<2>` のように表す。

```
[4 3 5 1 2]
末尾の2を基準に選ぶと、
[1] [<2>] [4 3 5]
[1] は要素数1以下なのでソート完了
[4 3 5] をソートする

[4 3 5]
末尾の5を基準に選ぶと、
[4 3] [<5>] []
[] は要素数1以下なのでソート終了
[4 3] をソートする

[4 3]
末尾の3を基準に選ぶと、
[] [<3>] [4]
[] も [4] も要素数が1以下なのでソート終了
--> [<3> <4>]

[4 3 5]
--> [4 3] [<5>] []
--> [<3> <4>] [<5>]
--> [<3> <4> <5>]

[4 3 5 1 2]
--> [1] [<2>] [4 3 5]
--> [<1>] [<2>] [<3> <4> <5>]
--> [<1> <2> <3> <4> <5>]

全体のソート完了
```


# 計算量

## 時間計算量

### 平均計算量

うまく基準値を選べている場合、元の配列を分割した部分集合はだいたい均等な大きさになる。  
要素数が1になるまで分割するのにかかる分割回数（深さ）は $\log n$ のオーダーであり、それぞれの深さで $n$ 個の要素を1度ずつ探索するので、平均計算量は $O(n\log n)$

### 最悪計算量

配列の末尾や先頭の要素を基準値 $a_\mathrm{pivot}$ とするアルゴリズムでは、配列が最初から昇順ソート or 降順ソートされている場合、基準値が配列の最大値 / 最小値になってしまう。  
こうなると、分割しても全ての要素が一方の部分集合に集中してしまい、計算量が節約できない。  
このとき、1度分割しても分割後の部分集合の要素数は1しか減らないので、計算量は

$$
n + (n-1) + (n-2) + \cdots + 1 = \cfrac{n(n+1)}{2} \sim O(n^2)
$$


## 空間計算量

元の配列以外のメモリ領域を使わないので、$O(N)$


# 実装

{% gist 12061820cfef20172e8a7549464995de ~2_quick-sort.py %}

テスト：

```python
>>> test_sort_algorithm(QuickSort())
OK: [1, 6, 2, 7, 5, 4, 3] --> [1, 2, 3, 4, 5, 6, 7]
OK: [2, 4, 3, 7, 6, 5, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [3, 1, 5, 7, 6, 4, 2] --> [1, 2, 3, 4, 5, 6, 7]
OK: [3, 6, 5, 7, 4, 2, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [4, 3, 7, 6, 5, 2, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [5, 2, 1, 7, 6, 4, 3] --> [1, 2, 3, 4, 5, 6, 7]
OK: [5, 7, 2, 6, 4, 3, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [6, 4, 3, 7, 5, 2, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [7, 2, 5, 6, 4, 3, 1] --> [1, 2, 3, 4, 5, 6, 7]
OK: [7, 6, 5, 4, 3, 2, 1] --> [1, 2, 3, 4, 5, 6, 7]
All 5040 tests passed.
```

[（参考）`test_sort_algorithm`：指定した長さの全ての組み合わせの配列を生成してソート結果をテストする関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-test-sort-algorithm-py)

平均時間計算量 $O(n\log n)$ の確認：

```python
Ns = np.arange(1, 20+1) * 1000
ave, std = experiment_computing_time(QuickSort(), Ns)
draw_computing_order(Ns, ave, std)
```

- [（参考）`experiment_computing_time`：処理時間を複数回測定して平均と標準偏差を計算する関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-experiment-computing-time-py)
- [（参考）`draw_computing_order`：配列長と処理時間の関係を表す回帰関数を最小二乗法で求めて描画する関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-draw-computing-order-py)

![quick_sort](https://gist.github.com/assets/13412823/99d8158d-556e-415a-a7f3-b09d54b3d3df)

最悪時間計算量 $O(n^2)$ の確認：

{% gist 12061820cfef20172e8a7549464995de ~array-generator.py %}

```python
import sys
import time

Ns = np.arange(1, 10+1) * 2000
T = 10
# 関数の再帰呼び出し回数の上限を引き上げておく
sys.setrecursionlimit(Ns.max()*10)  

t_ave = []
t_std = []
for n in Ns:
    ts = []
    for _ in range(T):
        a = ArrayGenerator.asc(n)
        t1 = time.time()
        a_sorted = QuickSort().sort(a)
        t2 = time.time()
        ts.append(t2-t1)
    t_ave.append(np.mean(ts))
    t_std.append(np.std(ts))

draw_computing_order(Ns, np.array(t_ave), np.array(t_std))
```

![quick_sort_asc](https://gist.github.com/assets/13412823/dd75f50f-19aa-4f6e-b75c-549a10710898)
