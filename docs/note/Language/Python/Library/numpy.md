---
title: numpy
---

# numpy 概要

効率的な数値計算のためのライブラリ。

# インストール

```
$ pip install numpy
```

# 使い方

```python
import numpy as np
```

## 配列・行列の生成

### list を numpy 配列に変換

```python
l = [1,2,3,4,5]
a = np.array(l)
# array([1, 2, 3, 4, 5])
```

### 多次元 list を numpy 行列に変換

```python
# 行ベクトル
np.matrix([0, 1])
"""
matrix([[0, 1]])
"""

# 列ベクトル
np.matrix([
	[0],
	[1]
])
"""
matrix([[0],
        [1]])
"""

# 行列
np.matrix([
	[0, 1, 2],
	[3, 4, 5]
])
"""
matrix([[0, 1, 2],
        [3, 4, 5]])
"""
```

### 乱数配列

```python
# 平均0、標準偏差1の正規分布
rand = np.random.normal(loc=0, scale=1.0, size=(3,4))
"""
array([[ 0.25231664,  0.57895262,  0.59728289,  0.37939539],
       [-0.80000888, -0.36862112, -0.772507  ,  0.89776578],
       [-2.49653143,  1.17558449, -0.37644545,  1.50055032]])
"""

# 0以上3未満の整数
np.random.randint(3, size=(3,4))
"""
array([[0, 1, 1, 2],
       [0, 1, 2, 2],
       [1, 0, 0, 1]])
"""

# 0以上1未満の小数
np.random.rand(3,4)
"""
array([[0.58274554, 0.41312968, 0.34026029, 0.58275797],
       [0.58989403, 0.04602324, 0.06885702, 0.09617708],
       [0.54617384, 0.94229429, 0.91238302, 0.33197529]])
"""
```

### メッシュ（格子列）

```python
x = np.array(range(5))
y = np.array(range(3, 6))
XX, YY = np.meshgrid(x, y)
"""
>>> XX
array([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])
>>> YY
array([[3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5]])
"""
```

## 行列の演算

```python
m1 = np.matrix([
	[1, 2],
	[3, 4]
])
m2 = np.matrix([
	[-1, 3],
	[2, 1]
])
m3 = np.matrix([
	[-1, 3, 2],
	[2, 1, -1]
])
m4 = np.matrix([
	[1, 2],
	[3, 4],
	[5, 6]
])
```

### 行列の積

```python
# 行列の積
m1 * m2
"""
matrix([[ 3,  5],
        [ 5, 13]])
"""
m1 * m3
"""
matrix([[ 3,  5,  0],
        [ 5, 13,  2]])
"""
m3 * m4
"""
matrix([[18, 22],
        [ 0,  2]])
"""
m4 * m3
"""
matrix([[ 3,  5,  0],
        [ 5, 13,  2],
        [ 7, 21,  4]])
"""

# 行列の整数乗（各成分の累乗ではなく、行列としての累乗）
m1 ** 2
"""
matrix([[ 7, 10],
        [15, 22]])
"""
m1 ** 3
"""
matrix([[ 37,  54],
        [ 81, 118]])
"""
```

### 転置行列

```python
m1.T
"""
matrix([[1, 3],
        [2, 4]])
"""
```


### 逆行列

```python
m1.I
"""
matrix([[-2. ,  1. ],
        [ 1.5, -0.5]])
"""
```

### 固有値

```python
A = np.matrix([
	[1, 2],
	[3, 4]
])

lmd, U = np.linalg.eig(A)
"""
lmd: 固有値
	array([-0.37228132,  5.37228132])
U: 固有ベクトルを（lmd と対応する並び順で）列ベクトルとして並べた行列
	matrix([[-0.82456484, -0.41597356],
	        [ 0.56576746, -0.90937671]])
"""

lmd1, lmd2 = lmd[0], lmd[1]
u1, u2 = U[:,0], U[:,1]

# 検算
A * u1 - lmd1 * u1 < 1e-10
A * u2 - lmd2 * u2 < 1e-10
"""
matrix([[ True],
        [ True]])
matrix([[ True],
        [ True]])
"""

# おまけ：固有ベクトル行列 U による A の対角化
U.I * A * U
"""
matrix([[-3.72281323e-01,  8.23749941e-16],
        [ 3.53579641e-16,  5.37228132e+00]])
"""
```

### 各成分の演算

```python
# 和
m2 + m1
"""
matrix([[0, 5],
        [5, 5]])
"""

# 差
m2 - m1
"""
matrix([[-2,  1],
        [-1, -3]])
"""

# 積（アダマール積：成分どうしの積）
np.multiply(m2, m1)  # m2 * m1 は使えない！（行列の積が計算されてしまう）
"""
matrix([[ 8, 10],
        [ 5,  8]])
"""

# 商
m2 / m1
"""
matrix([[-1.        ,  1.5       ],
        [ 0.66666667,  0.25      ]])
"""

# 商（小数点切り捨て）
m2 // m1
"""
matrix([[-1,  1],
        [ 0,  0]])
"""

# 累乗
np.power(m2, m1)
"""
matrix([[-1,  9],
        [ 8,  1]])
"""
```

### 結合

```python
m1 = np.matrix([
	[0, 1, 2],
	[3, 4, 5]
])
m2 = np.matrix([
	[6, 7, 8],
	[9, 10, 11]
])
v_r = np.matrix([12, 13, 14])
v_c = np.matrix([
	[15],
	[16]
])

# 縦に結合
np.concatenate((m1, m2, v_r), axis=0)
"""
matrix([[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]])
"""

# 横に結合
np.concatenate((m1, m2, v_c), axis=1)
"""
matrix([[ 0,  1,  2,  6,  7,  8, 15],
        [ 3,  4,  5,  9, 10, 11, 16]])
"""
```


## 通常の関数をユニバーサル関数に変換

```python
# 1つの引数から1つの結果を出力する関数
def myfunc1to1(x):
	if x >= 0:
		return x * 10
	else:
		return x * -10

# 2つの引数から2つの結果を出力する関数
def myfunc2to2(x, y):
	return x+y, x-y

# 2つの引数から1つの結果を出力する関数
def myfunc2to1(x, y):
	return x+y-1

# 1つの引数から2つの結果を出力する関数
def myfunc1to2(x):
	return x**2, x*2

np_myfunc1to1 = np.frompyfunc(myfunc1to1, nin=1, nout=1)
np_myfunc2to2 = np.frompyfunc(myfunc2to2, nin=2, nout=2)
np_myfunc2to1 = np.frompyfunc(myfunc2to1, nin=2, nout=1)
np_myfunc1to2 = np.frompyfunc(myfunc1to2, nin=1, nout=2)

a1 = np.array(range(9)) - 4
a2 = np.array(range(9)) * 0.1
"""
>>> a1
array([-4, -3, -2, -1,  0,  1,  2,  3,  4])
>>> a2
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
"""

np_myfunc1to1(a1)
"""
array([40, 30, 20, 10, 0, 10, 20, 30, 40], dtype=object)
"""
np_myfunc2to2(a1, a2)
"""
(array([-4.0, -2.9, -1.8, -0.7, 0.4, 1.5, 2.6, 3.7, 4.8], dtype=object),
 array([-4.0, -3.1, -2.2, -1.3, -0.4, 0.5, 1.4, 2.3, 3.2], dtype=object))
"""
np_myfunc2to1(a1, a2)
"""
array([-5.0, -3.9, -2.8, -1.7, -0.6, 0.5, 1.6, 2.7, 3.8], dtype=object)
"""
np_myfunc1to2(a1)
"""
(array([16, 9, 4, 1, 0, 1, 4, 9, 16], dtype=object),
 array([-8, -6, -4, -2, 0, 2, 4, 6, 8], dtype=object))
"""
```
