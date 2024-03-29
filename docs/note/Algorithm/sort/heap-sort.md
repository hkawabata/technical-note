---
title: ヒープソート
title-en: heap sort
---
# 概要

配列のソートアルゴリズムの1つ。

# アルゴリズム

## 前提

ソート対象の配列の長さを $n$ とし、この配列を二分木として考える。  
配列のインデックス $i$ を0始まり（$i=0, 1, 2, \cdots, n-1$）とすれば、$i$ 番目のノードの子ノードのインデックスは $2i+1, 2i+2$ で表される

```
                   A[i=0]
                /          \
          B[i=1]            C[i=2]
        /       \          /       \
     D[i=3]    E[i=4]   F[i=5]    G[i=6]
     /    \     /
H[i=7] I[i=8] J[i=9]
```

## 処理の流れ

配列の $i$ 番目の要素を $a_i$ で表す。

### 前準備：ヒープの構築

1. $i_\mathrm{max} \gets n-1$ で変数を初期化
2. $i \gets i_\mathrm{max}$ で変数を初期化
3. $a_i$ が子ノードを持ち、かつ $a_i$ の値よりも子ノード $a_{2i+1}, a_{2i+2}$ のいずれかの値の方が大きい場合は以下の操作を行う（ここでは簡単のため $a_{2i+1} \lt a_{2i+2}$ とする）
    - 値が大きい方の子ノード $a_{2i+2}$ と $a_i$ の値を交換：$a_i, a_{2i+2} \gets a_{2i+2}, a_i$
    - 値を交換した子ノードのインデックスで $i$ を更新：$i \gets 2i+2$
    - 更新後の $i$ に対して、条件を満たさなくなるまで3の操作を再起的に繰り返す
4. $i_\mathrm{max}$ の値を1小さくする：$i_\mathrm{max} \gets i_\mathrm{max}-1$
5. $i_\mathrm{max} >= 0$ なら2に戻る。$i_\mathrm{max} = -1$ になったらヒープ構築完了

### ソートの実行

1. $i_\mathrm{max} \gets n-1$ で変数を初期化
2. $i \gets 0$ で変数を初期化
3. $a_i$ と $a_{i_\mathrm{max}}$ の値を交換
4. $i_\mathrm{max}$ の値を1小さくする：$i_\mathrm{max} \gets i_\mathrm{max}-1$
5. 配列 $a_0,a_1,\cdots,a_{n-1}$ の部分配列 $a_0,a_1,\cdots,a_{i_\mathrm{max}}$ に関して、前節「前準備：ヒープの構築」の3の操作を実行する
6. $i_\mathrm{max} \gt 0$ なら2に戻る。$i_\mathrm{max} = 0$ ならソート完了


# 具体例

具体例として、以下の配列をソートする。  
配列は以下のように二分木として解釈する。

```
[1 3 5 0 4 2]
       1
     /   \
   3       5
  / \     /
 0   4   2
```

順序が確定したものを `<2>` のように表す。

## ヒープの構築

```
[1 3 5 0 4 2]
       1
     /   \
   3       5
  / \     /
 0   4   2

========== i_max = 5,4,3 ==========

- a(5),a(4),a(3)は子ノードを持たないのでスキップ

========== i_max = 2 ==========

- a(2)=5: 子ノード a(5)=2 と比べると自身の値の方が大きい
  - 入れ替えない

========== i_max = 1 ==========

- a(1)=3: 子ノード a(3)=0, a(4)=4 と比べると右の子ノード a(4) が最大
  - 入れ替える

[1 4 5 0 3 2]
       1
     /   \
   4       5
  / \     /
 0   3   2

- 入れ替えた子ノード a(4) は子を持たないので探索終了

========== i_max = 0 ==========

- a(0)=1: 子ノード a(1)=4, a(2)=5 と比べると右の子ノード a(2) が最大
  - 入れ替える

[5 4 1 0 3 2]
       5
     /   \
   4       1
  / \     /
 0   3   2

- 入れ替えた子ノード a(2) は子を持つ
  - a(2) の子ノードの大小関係をチェック
- a(2)=1: 子ノード a(5)=2 と比べると子ノード a(5) の値の方が大きい
  - 入れ替える

[5 4 2 0 3 1]
       5
     /   \
   4       2
  / \     /
 0   3   1

- 入れ替えた子ノード a(5) は子を持たないので探索終了

---> ヒープが完成
```

## ソートの実行

```
- ヒープにおいては a(0) が最大値であるから、a(0) と末尾の a(5) を交換
  - a(5) が確定

[1 4 2 0 3 <5>]
       1
     /   \
   4       2
  / \     /
 0   3  <5>

========== i_max = 4 ==========

- a(0)=1: 子ノード a(1)=4, a(2)=2 と比べると左の子ノード a(1) が最大
  - 入れ替える

[4 1 2 0 3 <5>]
       4
     /   \
   1       2
  / \     /
 0   3  <5>

- 入れ替えた子ノード a(1) は未確定な子を持つ
  - a(1) の子ノードの大小関係をチェック
- a(1)=1: 子ノード a(3)=0, a(4)=3 と比べると右の子ノード a(4) が最大
  - 入れ替える

[4 3 2 0 1 <5>]
       4
     /   \
   3       2
  / \     /
 0   1  <5>

- 入れ替えた子ノード a(4) は子を持たないので探索終了
  - 確定ノードを除いたヒープの再構築完了
- ヒープの最大値 a(0) と末尾の a(4) を交換
  - a(4) が確定

[1 3 2 0 <4> <5>]
       1
     /   \
   3       2
  / \     /
 0  <4> <5>

========== i_max = 3 ==========

- a(0)=1: 子ノード a(1)=3, a(2)=2 と比べると左の子ノード a(1) が最大
  - 入れ替える

[3 1 2 0 <4> <5>]
       3
     /   \
   1       2
  / \     /
 0  <4> <5>

- 入れ替えた子ノード a(1) は未確定な子を持つ
  - a(1) の子ノードの大小関係をチェック
- a(1)=1: 未確定の子ノードは左の子ノード a(3)=0 のみであり、親ノードの方が大きい
  - 入れ替えない
- 入れ替えられない深さまできたので探索終了
  - 確定ノードを除いたヒープの再構築完了
- ヒープの最大値 a(0) と末尾の a(3) を交換
  - a(3) が確定

[0 1 2 <3> <4> <5>]
       0
     /   \
   1       2
  / \     /
<3> <4> <5>

========== i_max = 2 ==========

- a(0)=0: 子ノード a(1)=1, a(2)=2 と比べると右の子ノード a(2) が最大
  - 入れ替える

[2 1 0 <3> <4> <5>]
       2
     /   \
   1       0
  / \     /
<3> <4> <5>

- 入れ替えた子ノード a(2) は未確定な子を持たないので探索終了
  - 確定ノードを除いたヒープの再構築完了
- ヒープの最大値 a(0) と末尾の a(2) を交換
  - a(2) が確定

[0 1 <2> <3> <4> <5>]
       0
     /   \
   1      <2>
  / \     /
<3> <4> <5>

========== i_max = 1 ==========

- a(0)=0: 未確定の子ノード a(1)=1 と比べると子ノード a(1) の方が大きい
  - 入れ替える

[1 0 <2> <3> <4> <5>]
       1
     /   \
   0      <2>
  / \     /
<3> <4> <5>

- 入れ替えた子ノード a(1) は未確定な子を持たないので探索終了
  - 確定ノードを除いたヒープの再構築完了
- ヒープの最大値 a(0) と末尾の a(1) を交換
  - a(1) が確定

[0 <1> <2> <3> <4> <5>]
       0
     /   \
  <1>     <2>
  / \     /
<3> <4> <5>

========== i_max = 0 ==========

- i_max がゼロになったので探索終了
  - 最後の a(0) も確定

[<0> <1> <2> <3> <4> <5>]
      <0>
     /   \
  <1>     <2>
  / \     /
<3> <4> <5>

---> ソート完了
```


# 計算量

## 時間計算量

- 最初のヒープ作成の計算量：$O(n \log n)$
    - $i_\mathrm{max}$ を末尾の $i_\mathrm{max}=n-1$ から先頭の $i_\mathrm{max}=1$ までスキャンする計算オーダーは $O(n)$
    - それぞれの $i_\mathrm{max}$ に対して部分二分木を探索する計算オーダーは以下の理由により $O(\log n)$
        - 二分木の深さを $d$ とすると、各深さのノード数は $1, 2, 4, 8, \cdots$ と二倍で増えていくことから、全ノード数 $n \simeq 1 + 2 + 2^2 + \cdots + 2^{d-1} = 2^d-1$
        - これを $d$ について解けば $d \simeq \log_2 (n+1)$
        - 1つの $i_\mathrm{max}$ に関する二分木の探索ではいずれか一方の子ノードを選びながら最大で深さ $d$ まで辿るので、計算量は $O(d) \sim O(\log n)$
- ソートの計算量：$O(n\log n)$
    - 1ステップごとに配列の末尾が決定するので、ステップ数は $n$
    - 各ステップごとに最大で二分木の深さ $d$ まで探索するので、ステップごとの計算量は $O(d)\sim O(\log n)$

以上により、最初のヒープ作成とその後のソートの計算量はいずれも $O(n\log n)$ であるから、ヒープソートの時間計算量も $O(n\log n)$

## 空間計算量

元の配列の要素の交換で処理が完結するため、元の配列以上のメモリ空間は必要ない。  
したがって、空間計算量は $O(n)$

# 実装

{% gist 12061820cfef20172e8a7549464995de ~3_heap-sort.py %}

テスト：

```python
>>> test_sort_algorithm(HeapSort())
OK: [1, 6, 2, 7, 5, 4, 3] --> [1 2 3 4 5 6 7]
OK: [2, 4, 3, 7, 6, 5, 1] --> [1 2 3 4 5 6 7]
OK: [3, 1, 5, 7, 6, 4, 2] --> [1 2 3 4 5 6 7]
OK: [3, 6, 5, 7, 4, 2, 1] --> [1 2 3 4 5 6 7]
OK: [4, 3, 7, 6, 5, 2, 1] --> [1 2 3 4 5 6 7]
OK: [5, 2, 1, 7, 6, 4, 3] --> [1 2 3 4 5 6 7]
OK: [5, 7, 2, 6, 4, 3, 1] --> [1 2 3 4 5 6 7]
OK: [6, 4, 3, 7, 5, 2, 1] --> [1 2 3 4 5 6 7]
OK: [7, 2, 5, 6, 4, 3, 1] --> [1 2 3 4 5 6 7]
OK: [7, 6, 5, 4, 3, 2, 1] --> [1 2 3 4 5 6 7]
All 5040 tests passed.
```

[（参考）`test_sort_algorithm`：指定した長さの全ての組み合わせの配列を生成してソート結果をテストする関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-test-sort-algorithm-py)

平均時間計算量 $O(n\log n)$ の確認：

```python
Ns = np.arange(1, 20+1) * 1000
ave, std = experiment_computing_time(HeapSort(), Ns)
draw_computing_order(Ns, ave, std)
```

- [（参考）`experiment_computing_time`：処理時間を複数回測定して平均と標準偏差を計算する関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-experiment-computing-time-py)
- [（参考）`draw_computing_order`：配列長と処理時間の関係を表す回帰関数を最小二乗法で求めて描画する関数](https://gist.github.com/hkawabata/12061820cfef20172e8a7549464995de#file-draw-computing-order-py)

![heap_sort](https://gist.github.com/assets/13412823/60dd52f6-5a2a-463e-ac61-81057356f4ba)

