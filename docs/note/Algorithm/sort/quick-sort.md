---
title: クイックソート
title-en: quick sort
---
# 概要

配列のソートアルゴリズムの1つ。

# アルゴリズム

1. 配列の要素数が1以下ならソート終了
2. 要素数が2以上の場合、配列の要素のうち基準値 $a_\mathrm{base}$ を1つ選ぶ
    1. たとえば配列の末尾の要素など
3. 配列の要素を以下の2つに分ける
    1. 【A】$a_\mathrm{base}$ 以下のもの
    2. 【B】$a_\mathrm{base}$ より大きいもの
4. 部分集合 A, B をソートし、【A】【B】の順に並べる
    1. A, B をソートするにあたって、全く同じ手順1〜4を再帰的に適用する


# 計算量

## 時間計算量



## 空間計算量

元の配列以外のメモリ領域を使わないので、$O(N)$

# 具体例

順序が確定したものを `<2>` のように表す。

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


# 実装

{% gist 12061820cfef20172e8a7549464995de ~2_quick-sort.py %}

```python
def quick_sort_split(arr, i_from, i_to):
    pivot = arr[i_to]  # 簡単のため、単純に末尾をピボットに選ぶ
    i_split = i_from
    for j in range(i_from, i_to):
        # ピボットよりも小さい値が見つかったら左端から詰めこんでいく
        if arr[j] <= pivot:
            arr[i_split], arr[j] = arr[j], arr[i_split]
            i_split += 1
    # 末尾のピボットデータを切れ目に移動
    arr[i_split], arr[i_to] = arr[i_to], arr[i_split]
    return i_split

def quick_sort(array, i_from=None, i_to=None):
    if i_from is None or i_to is None:
        a = array.copy()
        i_from, i_to = 0, len(array)-1
    else:
        a = array
    if i_from < i_to:
        i_split = quick_sort_split(a, i_from, i_to)
        quick_sort(a, i_from, i_split-1)  # ピボット以下をソート
        quick_sort(a, i_split+1, i_to)    # ピボット以上をソート
    return a
```

テスト：

{% gist 12061820cfef20172e8a7549464995de ~test-sort-algorithm.py %}

```python
>>> test_sort_algorithm(quick_sort)
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

計算量の実験：

{% gist 12061820cfef20172e8a7549464995de ~measure-processing-speed.py %}

```python
Ns = np.arange(1, 10+1) * 10000
time_ave, time_std = measure_processing_speed(quick_sort, Ns, T=3)

coe = np.polyfit(Ns, time_ave, 1)
n = np.arange(Ns[0], Ns[-1]+1)
fit_curve = coe[0]*n**2+coe[1]*n+coe[2]
plt.title('Quick Sort')
plt.xlabel('Array Length $n$')
plt.ylabel('Processing Time $y$ [s]')
plt.plot(n, fit_curve, label='Fit: $y = an^2+bn+c$')
plt.errorbar(Ns, time_ave, yerr=time_std,
             capsize=3, fmt='o', markersize=3,
             ecolor='black', markeredgecolor = "black", color='w')
plt.grid()
plt.legend()
plt.show()
```

