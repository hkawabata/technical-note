---
title: pandas
---

# pandas とは

データ分析を支援するライブラリ。

# 導入

```bash
pip install pandas
```

```python
import pandas as pd
```

# 用語
- `Series`：1次元配列に相当
- `DataFrame`：2次元配列に相当

# 使い方

## データの生成

### Series
```python
import pandas as pd
import numpy as np

s1 = pd.Series([0, 1, 2])
s2 = pd.Series(np.random.rand(3))
s3 = pd.Series({1:'a', 2:'b', 3:'c'})
s4 = pd.Series({'a':1, 'b':2, 'c':3})
```

```python
>>> print(s1)
0    0
1    1
2    2
dtype: int64

>>> print(s2)
0    0.405215
1    0.792087
2    0.030771
dtype: float64

>>> print(s3)
1    a
2    b
3    c
dtype: object

>>> print(s4)
a    1
b    2
c    3
dtype: int64
```

### DataFrame

```python
import pandas as pd
import numpy as np

# 多次元リストから作成
df1 = pd.DataFrame([[0,1,2,3], [4,5,6,7], [8,9,10,11]])
# 多次元リストから作成、行・列のラベルを指定
df2 = pd.DataFrame([[0,1,2,3], [4,5,6,7], [8,9,10,11]], index=['a','b','c'], columns=['A','B','C','D'])
# 多次元配列から作成
df3 = pd.DataFrame(np.random.rand(12).reshape(4,3))
# 辞書から作成
df4 = pd.DataFrame({'Name': ['Andy','Ben','Chris','Demi'], 'Initial': ['A','B','C','D'], 'Age':[20,15,23,25]}, columns=['Name', 'Age', 'Initial'])
```

```python
>>> print(df1)
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> print(df2)
   A  B   C   D
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11

>>> print(df3)
          0         1         2
0  0.348303  0.465540  0.338442
1  0.410867  0.944651  0.970990
2  0.526522  0.311577  0.876694
3  0.164944  0.760977  0.504524

>>> print(df4)                                                                                                                                       
    Name  Age Initial
0   Andy   20       A
1    Ben   15       B
2  Chris   23       C
3   Demi   25       D
```


## データの取り出し

```python
df = pd.DataFrame(np.array(range(120)).reshape(30, 4), columns=['A','B','C','D'])
```

```python
>>> # 先頭の指定数行を抜き出し(1)
>>> df.head(4)
    A   B   C   D
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15

>>> # 先頭の指定数行を抜き出し(2)
>>> df[:4]
    A   B   C   D
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15

>>> # 末尾の指定数行を抜き出し(1)
>>> df.tail(4)
      A    B    C    D
26  104  105  106  107
27  108  109  110  111
28  112  113  114  115
29  116  117  118  119

>>> # 末尾の指定数行を抜き出し(2)
>>> df[-4:]
      A    B    C    D
26  104  105  106  107
27  108  109  110  111
28  112  113  114  115
29  116  117  118  119

>>> # 指定した範囲の行を抜き出し
>>> df[5:8]
    A   B   C   D
5  20  21  22  23
6  24  25  26  27
7  28  29  30  31

>>> # 列ラベルを指定して抜き出し
>>> df['C']
0       2
1       6
2      10
3      14
4      18
5      22
6      26
7      30
8      34
9      38
10     42
11     46
12     50
13     54
14     58
15     62
16     66
17     70
18     74
19     78
20     82
21     86
22     90
23     94
24     98
25    102
26    106
27    110
28    114
29    118
Name: C, dtype: int64

>>> # 列ラベルを指定して抜き出し(複数)
>>> df[['B','D']]
      B    D
0     1    3
1     5    7
2     9   11
...
27  109  111
28  113  115
29  117  119

>>> # 位置を指定して取り出し
>>> df.iloc[3]
A    12
B    13
C    14
D    15
Name: 3, dtype: int64
>>> df.iloc[2:5]
    A   B   C   D
2   8   9  10  11
3  12  13  14  15
4  16  17  18  19
>>> df.iloc[3, 2]
14
>>> df.iloc[2:5, 2]
2    10
3    14
4    18
Name: C, dtype: int64
>>> df.iloc[:, 1:3]
      B    C
0     1    2
1     5    6
2     9   10
3    13   14
...
27  109  110
28  113  114
29  117  118

>>> # 条件付き取り出し(AND)
>>> df[(df['A']%3==0) & (df['B']%5==0)]
     A   B   C   D
6   24  25  26  27
21  84  85  86  87

>>> # 条件付き取り出し(OR)
>>> df[(df['A']%7==0) | (df['B']%5==0)]
      A    B    C    D
0     0    1    2    3
1     4    5    6    7
6    24   25   26   27
7    28   29   30   31
11   44   45   46   47
14   56   57   58   59
16   64   65   66   67
21   84   85   86   87
26  104  105  106  107
28  112  113  114  115
```


## データの追加と削除

### 破壊的な操作

```python
>>> df = pd.DataFrame(np.array(range(12)).reshape(3, 4), columns=['A','B','C','D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> # 新しい列の追加(破壊的操作)
>>> df['E'] = [0.1, 0.2, 0.3]
>>> df
   A  B   C   D    E
0  0  1   2   3  0.1
1  4  5   6   7  0.2
2  8  9  10  11  0.3

>>> # 列の値の上書き(破壊的操作)
>>> df['B'] = [10.0, 20.0, 30.0]
>>> df
   A     B   C   D    E
0  0  10.0   2   3  0.1
1  4  20.0   6   7  0.2
2  8  30.0  10  11  0.3

>>> # 列の削除(破壊的操作)
>>> del df['A']
>>> df
      B   C   D    E
0  10.0   2   3  0.1
1  20.0   6   7  0.2
2  30.0  10  11  0.3
```

### 非破壊的な操作

```python
>>> df = pd.DataFrame(np.array(range(12)).reshape(3, 4), columns=['A','B','C','D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

>>> # 列の値の追加(新しい配列を生成)
>>> df2 = df.assign(E=df['B']/df['C'])
>>> df2
   A  B   C   D         E
0  0  1   2   3  0.500000
1  4  5   6   7  0.833333
2  8  9  10  11  0.900000

>>> # 列の値の上書き(新しい配列を生成)
>>> df3 = df.assign(B=df['B']*10)
>>> df3
   A   B   C   D
0  0  10   2   3
1  4  50   6   7
2  8  90  10  11

>>> # 列の削除(新しい配列を生成)
>>> df4 = df.drop('C', axis=1)
>>> df4
   A  B   D
0  0  1   3
1  4  5   7
2  8  9  11

>>> # 行の削除(新しい配列を生成)
>>> df5 = df.drop(1, axis=0)
>>> df5
   A  B   C   D
0  0  1   2   3
2  8  9  10  11
```


## データのソート

```python

```



```python

```


```python

```

```python

```

```python

```

