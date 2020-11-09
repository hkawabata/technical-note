---
title: Hive
main_image: https://user-images.githubusercontent.com/13412823/98496677-88707c00-2285-11eb-86bb-257fb07053e6.jpg
---

# HiveQL

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

## Group By の際にキー全ての合計も出力

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
