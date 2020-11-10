---
title: Hive
main_image: https://user-images.githubusercontent.com/13412823/98496677-88707c00-2285-11eb-86bb-257fb07053e6.jpg
---

# HiveQL

## 文字列の結合

```sql
select
  key,
  value,
  concat(key, '/', value)
from
  my_table
```

```
A a A/a
A b A/b
B a B/a
...
```

## 条件分岐による値の設定

```sql
select
  key1,
  key2,
  -- 単純な値による分岐
  case key1
    when 'A' then 'a'
    when 'B' then 'b'
    else 'other'
  end,
  -- より複雑な条件による分岐
  case
    when key1 = 'A' then 'Good'
    when key1 = 'B' and key2 = 'OK' then 'Normal'
    else 'Bad'
  end
from
  my_table
```

```
A OK a     Good
B OK b     Normal
B NG b     Bad
C OK other Bad
```

## WITH 句

- 誤：テンポラリテーブルを作成して処理結果を格納し、何度も使い回せる機能
- 正：定義した処理を都度呼び出して実行できる機能

→ **WITH で定義した処理を複数回呼び出すと、その回数だけ同じ処理が実行される（= 効率化はされない）**  
→ 同じ処理結果を使い回したいのであれば、WITH ではなく別にテンポラリテーブルを作る

```sql
with
proccessed1 as (
  select
    *
  from
    my_table1
  where
    ...
),
proccessed2 as (
  select
    *
  from
    my_table2
  where
    ...
)

select
  *
from
  processed1 join processed2
  on processed1.key = processed2.key
```

## GROUP BY の際に複数の値を文字列として結合

```sql
select
  key,
  collect_list(value),
  concat_ws(',', collect_list(value)),
  collect_set(value),
  concat_ws(',', collect_set(value))
from
  my_table
group by
  key
```

```
A  ['a', 'a', 'b']       a,a,b    ['a', 'b']       a,b
B  ['a', 'c']            a,c      ['a', 'c']       a,c
C  ['a', 'c', 'b', 'c']  a,c,b,c  ['a', 'c', 'b']  a,c,b
```

## GROUP BY の際にキー全ての合計も出力

`with rollup`句を使う。

```sql
select
  key1,
  key2,
  count(distinct value)
from
  my_table
group by
  key1,
  key2
with rollup
```

```
A    a    10
A    b    20
A    c    5
B    a    30
B    b    15
A    NULL 35
B    NULL 45
NULL NULL 80
```

## 正規表現による置換・抽出

### 置換

```sql
select regexp_replace('aA1 bB2 cC3', '[A-Z]', '_')
```

```
a_1 b_2 c_3
```

### 抽出

```sql
select regexp_extract('BirthDate: 2000/1/1', ': ([0-9/]+)')
```

```
2000/1/1
```
