---
title: Hive
main_image: https://user-images.githubusercontent.com/13412823/98496677-88707c00-2285-11eb-86bb-257fb07053e6.jpg
---

# HiveQL Tips

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
