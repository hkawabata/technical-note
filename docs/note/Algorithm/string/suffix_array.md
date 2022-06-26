---
title: Suffix Array
---

# Suffix Array とは

与えられた文字列に対し、取りうる suffix（接尾辞）を辞書順に並べた配列。

文字列のパターンマッチングを効率的に行うためのデータ構造。

| パターンマッチ方法 | 文字列 S（長さ $n$）中にあるパターン P（長さ $m$）を全て見つける計算量 |
| :-- | :-- |
| 逐次走査 | $O(mn)$ |
| Suffix Array | $O(m \log{n})$ |

例えば文字列`ABAAACBBAACC`には以下の12の suffix がある。

| suffix | 開始位置 |
| :-- | :-- |
| `ABAAACBBAACC` | 0 |
| `BAAACBBAACC` | 1 |
| `AAACBBAACC` | 2 |
| `AACBBAACC` | 3 |
| `ACBBAACC` | 4 |
| `CBBAACC` | 5 |
| `BBAACC` | 6 |
| `BAACC` | 7 |
| `AACC` | 8 |
| `ACC` | 9 |
| `CC` | 10 |
| `C` | 11 |

Suffix Array はこれを辞書順に並べて、

```python
suffix_array = [
  'AAACBBAACC',
  'AACBBAACC',
  'AACC',
  'ABAAACBBAACC',
  'ACBBAACC',
  'ACC',
  'BAAACBBAACC',
  'BAACC',
  'BBAACC',
  'C',
  'CBBAACC',
  'CC'
]
```

文字列そのものを配列に格納すると $O(n^2)$ のメモリを食う。

→ suffix の代わりに、suffix の開始位置を格納する（$O(n)$）。

```python
suffix_array = [2, 3, 8, 0, 4, 9, 1, 7, 6, 11, 5, 10]
```


# Suffix Array の構築

## 手順

(TODO)

## 具体例

(TODO)


# Suffix Array によるパターンマッチング

## 問題設定

**【問題】文字列 S 中にあるパターン P の位置を全て見つける**

## 基本的な考え方

- この問題は、以下のように書き換えられる。
  - **【問題】文字列 S の suffix のうち、その先頭（接頭辞、prefix）がパターン P に一致するものを全て見つける**
  - ex. 文字列`ABABAA`中にあるパターン`AB`の位置を全て見つける場合、6つの suffix `ABABAA`,`BABAA`,`ABAA`,`BAA`,`AA`,`A` のうち、先頭が`AB`のものを見つければ、その suffix の開始位置が求める答えになる
- Suffix Array では suffix が辞書順に並ぶので、条件を満たす suffix は Suffix Array 中では連続して固まっている

| `ABABAA`の suffix | 開始位置 | パターン`AB`で始まるか？ |
| :-- | :-- | :-- |
| `A` | 5 | x |
| `AA` | 4 | x |
| `ABAA` | 2 | o |
| `ABABAA` | 0 | o |
| `BAA` | 3 | x |
| `BABAA` | 1 | x |


## 処理の流れ（一例）

例題として、S = `ABAAACBBAACBAC`から P = `BA`を探す。

### 1. Suffix Array の構築

文字列 S の suffix_array を構築する

- 例題の場合、下表に相当する suffix_array が得られる

| suffix | 開始位置 |
| :-- | :-- |
| `AAACBBAACBAC` | 2 |
| `AACBAC` | 8 |
| `AACBBAACBAC` | 3 |
| `ABAAACBBAACBAC` | 0 |
| `AC` | 12 |
| `ACBAC` | 9 |
| `ACBBAACBAC` | 4 |
| `BAAACBBAACBAC` | 1 |
| `BAACBAC` | 7 |
| `BAC` | 11 |
| `BBAACBAC` | 6 |
| `C` | 13 |
| `CBAC` | 10 |
| `CBBAACBAC` | 5 |

```python
suffix_array = [2, 8, 3, 0, 12, 9, 4, 1, 7, 11, 6, 13, 10, 5]
```

### 2. マッチ範囲の左端を探す

Suffix Array を二分探索し、パターン P と一致、もしくは P よりも辞書順が後であるような最小の suffix（`suffix_left`）を探す。

- 例題の場合、`BAAACBBAACBAC`（開始位置：1）を得る

### 3. パターンマッチ結果の存在チェック

`suffix_left`がパターン P で始まるかチェック。

- 始まるなら1件以上マッチする。次へ
- 始まらないなら1件もマッチしない。処理終了

### 4. マッチ範囲の右端を探す

Suffix Array を二分探索し、パターン P で始まる最大の suffix（`suffix_right`）を探す。

- 例題の場合、`BAC`（開始位置：11）を得る

### 5. 解を求める

`suffix_left`と`suffix_right`の間にある全ての suffix の開始位置が求める答えとなる。

- 例題の場合、Suffix Array 内の`BAAACBBAACBAC`（開始位置：1）と`BAC`（開始位置：11）の間を調べて 1, 7, 11 が答え
