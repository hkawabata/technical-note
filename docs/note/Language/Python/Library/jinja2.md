---
title: jinja2
---
# jinja2 概要

Python のテンプレートエンジンのライブラリ。

# インストール

```bash
$ pip install -U Jinja2
```

# 使い方

```python
from jinja2 import Template
```

## 変数の代入

{% gist 111f259961178fecd04c5e7f2dbb8de8 ~dainyu.py %}

## 条件分岐：if

### 変数の値のチェック

{% gist 111f259961178fecd04c5e7f2dbb8de8 ~if-value.py %}

```python
>>> print(template.render(score=100))

100点です！

>>> print(template.render(score=70))

合格点です。

>>> print(template.render(score=30))

不合格なので再試験です。
```

### 変数が定義されているかのチェック

{% gist 111f259961178fecd04c5e7f2dbb8de8 ~if-exist.py %}

```python
>>> print(template.render(flag=1))

flag という変数が定義されており、値は 1 です。

>>> print(template.render())

flag という変数は定義されていません。
```


## 繰り返し文：for

### list, set

{% gist 111f259961178fecd04c5e7f2dbb8de8 ~for-list.py %}

```python
>>> print(template.render(xs=[1,2,3,4,5]))

- 1

- 2

- 3

- 4

- 5
```

### dict

{% gist 111f259961178fecd04c5e7f2dbb8de8 ~for-dict.py %}

```python
>>> print(template.render(dic={1:10,2:20,3:30}))

<table>
  
  <tr>
    <td>1</td>
    <td>10</td>
  </tr>
  
  <tr>
    <td>2</td>
    <td>20</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>30</td>
  </tr>
  
</table>
```

