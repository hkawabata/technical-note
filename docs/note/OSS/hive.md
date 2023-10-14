---
title: Hive
main_image: https://user-images.githubusercontent.com/13412823/98496677-88707c00-2285-11eb-86bb-257fb07053e6.jpg
---

# Hive とは

Hadoop 上で動作するデータウェアハウス（DWH）向けの OSS。  
特徴として、Hadoop 上の MapReduce 処理を SQL-like な言語（**HiveQL**）で実行できる。

# アーキテクチャ

## テーブルの実体

- Hive テーブルの実体 = HDFS 上のファイル
- `create` コマンド実行時点で `/user/$USER/warehouse` 配下に配置される

## データの更新不可

- Hive のデータの実体は HDFS 上にあるため、上書きや削除ができない
- → `delete` 文、`update` 文は存在しない

# HiveQL

## データベース操作

### 一覧・詳細

```sql
-- 一覧表示
show databases;

-- DB 詳細情報表示
describe database my_db;
```

### 使う DB を選択

```sql
use my_db;
```

## テーブル操作

### 一覧・詳細

```
-- 一覧表示
show tables;

-- テーブル情報表示
describe my_table;
-- テーブル詳細情報表示
describe formatted my_table;
```

### 作成

```sql
create table if not exists example (
  id       bigint,
  name     string,
  birth    date,
  height   double,
  tag      array<string>,
  skill    map<string, string>,
  team     struct<name:string,role:array<string>>
)
-- 処理効率化のためのパーティショニング
--partitioned by (year int, month int, day int)

-- 行フォーマット（デリミタ指定）
row format delimited
fields terminated by '\t'           -- フィールド区切り文字
collection items terminated by ','  -- コレクションの要素の区切り文字
map keys terminated by ':'          -- Mapのkey-valueの区切り文字
lines terminated by '\n'            -- 行の区切り文字

-- 行フォーマット（シリアライズ・デシリアライズクラス指定）
-- row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'  -- JSON
;
```

### 削除

```sql
drop table if exists my_db.example;
```

### 名前変更

```sql
alter table example rename to example_new;
```

## テーブルへのデータ挿入

### 直接挿入

```sql
insert into table example
select
  100001, 'Taro', '1990-12-03', 172.4,
  array('elem1', 'elem2'), map('key1','value1','key2','value2'),
  named_struct('name', 'team-A', 'role', array('leader'))
from
  (select 'dummy') dummy  -- from 節がないとエラーになるので仕方なくダミー文を書く
;
```

### ファイルから挿入【tsv,csv など】

> **【元ファイル】**

example.tsv：

```
100002 Jiro 1991-11-05 169.0 elem2,elem3,elem4 key2:value2,key3:value3 team-A,[member]
100003 Saburo 1993-05-30 178.5 elem5,elem6,elem7 key4:value4,key5:value5 team-B,[member,pm]
```

```sql
load data inpath '/path/to/example.tsv' into table example;
```

```sql
> select * from example;

+-------------+---------------+----------------+-----------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------+--+
| example.id  | example.name  | example.birth  | example.height  |               example.tag                |                    example.skill                     |                             example.team                             |
+-------------+---------------+----------------+-----------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------+--+
| 100001      | Taro          | 1990-12-03     | 172.4           | ["elem1","elem2"]                        | {"key1":"value1","key2":"value2"}                    | {"name":"team-A","role":["leader"]}                                  |
| 100002      | Jiro          | 1991-11-05     | 169.0           | ["elem2","elem3","elem4"]                | {"key2":"value2","key3":"value3"}                    | {"name":"team-A","role":["[member]"]}                                |
| 100003      | Saburo        | 1993-05-30     | 178.5           | ["elem5","elem6","elem7"]                | {"key4":"value4","key5":"value5"}                    | {"name":"team-B","role":["[member,pm]"]}                                |
+-------------+---------------+----------------+-----------------+------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------+--+
```

→ **array と struct が混ざったような構造だと、うまく読み込めない...？（要深堀り）**  
→ JSON として読み込む方法が良さそう

### ファイルから挿入【JSON】

```sql
create table if not exists example (
  id       bigint,
  name     string,
  birth    date,
  height   double,
  tag      array<string>,
  skill    map<string, string>,
  team     struct<name:string,role:array<string>>
)
row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'  -- この行を追加
;
```

example.json：

```json
{"id":100002,"name":"Jiro","birth":"1991-11-05","height":169.0,"tag":["elem2","elem3","elem4"],"skill":{"key2":"value2","key3":"value3"},"team":{"name":"team-A","role":["member"]}}
{"id":100003,"name":"Saburo","birth":"1993-05-30","height":178.5,"tag":["elem5","elem6","elem7"],"skill":{"key4":"value4","key5":"value5"},"team":{"name":"team-B","role":["member","pm"]}}
```

```sql
load data inpath '/path/to/example.json' into table example;
```

```sql
> select * from example;

+-------------+---------------+----------------+-----------------+----------------------------+------------------------------------+-------------------------------------------+--+
| example.id  | example.name  | example.birth  | example.height  |        example.tag         |           example.skill            |               example.team                |
+-------------+---------------+----------------+-----------------+----------------------------+------------------------------------+-------------------------------------------+--+
| 100002      | Jiro          | 1991-11-05     | 169.0           | ["elem2","elem3","elem4"]  | {"key2":"value2","key3":"value3"}  | {"name":"team-A","role":["member"]}       |
| 100003      | Saburo        | 1993-05-30     | 178.5           | ["elem5","elem6","elem7"]  | {"key4":"value4","key5":"value5"}  | {"name":"team-B","role":["member","pm"]}  |
+-------------+---------------+----------------+-----------------+----------------------------+------------------------------------+-------------------------------------------+--+
2 rows selected (0.232 seconds)
```

### 別テーブルから HiveQL を実行した結果を挿入

```sql
insert into table example
select
  id, name, birth, height, tag, skill, team
from
  other_table
;
```

## 集合操作

### 和集合

```sql
select
  *
from (
  select a, b, c from table1
  union all
  select a, b, x as c from table2
)
```

## 条件指定

`WHERE` 句で使える色々

### 値の一致

```sql
where
  value = 'A'
```

### 値の大小比較

```sql
where
  value < 100
```

### NULL 判定

```sql
where
  value is null
```

```sql
where
  value is not null
```

### 配列が特定の値を含む

```sql
where
  array_contains(values, 'A')
```

### 値が集合内のいずれかの値に一致

```sql
where
  value in ('A', 'B', 'C')
```


## 文字列の結合

```sql
select
  key,
  value,
  concat(key, '/', value)
from
  my_table
;
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
;
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

→ **WITH で定義した処理を複数回呼び出すと、その回数だけ同じ処理が実行される（= 一度処理した結果をメモリ上に保持して使い回す、といった効率化はされない）**  
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
;
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
;
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
;
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
select
  regexp_replace('aA1 bB2 cC3', '[A-Z]', '_')
;
```

```
a_1 b_2 c_3
```

### 抽出

```sql
select
  regexp_extract('BirthDate: 2000/1/1', ': ([0-9/]+)')
;
```

```
2000/1/1
```


## 複数要素の展開

```sql
select
  key,
  values,
  value
from
  my_table
  literal view explode(values) t as value
```

```
A  ['a', 'b', 'c']  a
A  ['a', 'b', 'c']  b
A  ['a', 'b', 'c']  c
B  ['a', 'c']       a
B  ['a', 'c']       c
```

```sql
select
  key,
  values,
  pos,
  value
from
  my_table
  literal view posexplode(values) t as pos, value
```

```
A  ['a', 'b', 'c']  1  a
A  ['a', 'b', 'c']  2  b
A  ['a', 'b', 'c']  3  c
B  ['a', 'c']       1  a
B  ['a', 'c']       2  c
```


# ユーザ定義関数 (UDF, UDTF, UDAF)

| 種類 | 説明 |
| :-- | :-- |
| UDF | User-Defined Function<br>単一レコードから単一の値を生成する、通常のユーザ関数 |
| UDAF | User-Defined Aggregation Function<br>値のグループを受け入れ、単一の値を返すユーザー定義の集計関数 |
| UDTF | User-Defined Table Function<br>単一行で動作し、出力としてテーブルの複数の行を生成するユーザー定義テーブル生成関数 |

- `ObjectInspector`：Hive テーブル内の列のデータを扱うための重要なコンポーネントであり、Hive のデータ型と Java オブジェクトの間の変換を処理するために使用される

## pom.xml

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~pom.xml %}


## UDF

### UDF の実装：引数も返り値も基本型の場合

基本型：int, double, string, boolean など。

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~1_string-to-boolean.java %}


### UDF の実装：引数が array、返り値が基本型の場合

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~2_array-to-int.java %}


### UDF の実装：引数が map、返り値が array の場合

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~3_map-to-array.java %}


### UDF の実装：引数も返り値も struct 場合

正確には、より複雑なケースとして、struct の array から struct の array への変換を実装。

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~4_struct-to-struct.java %}


### UDF の利用

```bash
mvn clean package
hdfs dfs -put target/my-hive-udf.jar /path/to/
```

{% gist 9ab9e66ccfc4583f799dbcf1835ff6ce ~use-udf.hql %}


## UDAF

[公式のマニュアル](https://cwiki.apache.org/confluence/display/hive/genericudafcasestudy)が詳しい。

### UDAF の実装

UDAF の実装は2段階。

1. resolver の実装
    - resolver の役割：引数型の誤りチェック & 異なる引数型に応じて適切な evaluator を返す
    - 抽象クラス`AbstractGenericUDAFResolver`を継承し、`getEvaluator`メソッドをオーバーライド
2. evaluator の実装
    - evaluator の役割：
    - 抽象クラス`GenericUDAFEvaluator`を継承し、以下のメソッドをオーバーライド

`getEvaluator`メソッドの返り値の型は抽象クラス`GenericUDAFEvaluator`であり、これを継承する具象クラスも実装する必要がある。

`GenericUDAFEvaluator`の具象クラスでは、以下のメソッドをオーバーライドする。

| メソッド | 役割 |
| :-- | :-- |
| `AggregationBuffer getNewAggregationBuffer()` |  |
| `void reset(AggregationBuffer aggregationBuffer)` |  |
| `void iterate(AggregationBuffer aggregationBuffer, Object[] objects)` |  |
| `Object terminatePartial(AggregationBuffer aggregationBuffer)` |  |
| `void merge(AggregationBuffer aggregationBuffer, Object o)` |  |
| `Object terminate(AggregationBuffer aggregationBuffer)` |  |



### UDAF の利用

(ToDo)
## UDTF
