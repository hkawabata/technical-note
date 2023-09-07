---
title: Dataset
---

Spark 2.x 系について記述。

-   `DataFrame`, `Dataset`：RDD に代わる、ストレージ効率化・パフォーマンス最適化に役立つ新しいスキーマ情報を持つデータセット
  -  `DataFrame` = `Dataset[Row]`
-   SparkSQL: `DataFrame` / `Dataset` が持つ SQL-like な操作を行う API

## 準備

```scala
import org.apache.spark.sql.{Dataset, DataFrame, SparkSession, Row}
import org.apache.spark.sql.catalyst.expressions.aggregate._
import org.apache.spark.sql.expressions._
import org.apache.spark.sql.functions._

val spark: SparkSession = SparkSession.builder().
  config("spark.serializer", "org.apache.spark.serializer.KryoSerializer").
  config("spark.dynamicAllocation.enabled", "true").
  getOrCreate()
```


## 読み込み

### JSON

`DataFrame` として読み込み

```bash
$ cat sample.json
{"obj":{"n":1,"s":"a"},"list":["A","AA","AAA"],"num":10,"str":"aaa"}
{"obj":{"n":2,"s":"b"},"list":["B","BB","BBB"],"num":20,"str":"bbb"}
{"obj":{"n":3,"s":"c"},"list":["C","CC","CCC"],"num":30,"str":"ccc"}
```

```scala
val json: DataFrame = spark.read.json("sample.json")
json.show()
```

```
+------------+---+-----+---+
|        list|num|  obj|str|
+------------+---+-----+---+
|[A, AA, AAA]| 10|[1,a]|aaa|
|[B, BB, BBB]| 20|[2,b]|bbb|
|[C, CC, CCC]| 30|[3,c]|ccc|
+------------+---+-----+---+
```

`Dataset` として読み込み

```scala
import org.apache.spark.sql.catalyst.ScalaReflection
import org.apache.spark.sql.types.StructType

case class MySubObj(n: Int, s: String)
case class MyData(obj: MySubObj, list: List[String], num: Int, str: String)
val schema: StructType = ScalaReflection.schemaFor[MyData].dataType.asInstanceOf[StructType]

val records: Dataset[MyData] = spark.read.schema(schema).json("sample.json").as[MyData]
```

### CSV

```bash
$ cat sample.csv
1,0.9,a,A
2,0.8,b,B
3,0.7,c,C
```

```scala
val csv: DataFrame = spark.read.csv("sample.csv")
csv.show()
```

```
+---+---+---+---+
|_c0|_c1|_c2|_c3|
+---+---+---+---+
|  1|0.9|  a|  A|
|  2|0.8|  b|  B|
|  3|0.7|  c|  C|
+---+---+---+---+
```

カラム名を設定

```scala
val csvLabeled = csv.toDF("numInt", "numDouble", "strSmall", "strLarge")
csvLabeled.show()
```

```
+------+---------+--------+--------+
|numInt|numDouble|strSmall|strLarge|
+------+---------+--------+--------+
|     1|      0.9|       a|       A|
|     2|      0.8|       b|       B|
|     3|      0.7|       c|       C|
+------+---------+--------+--------+
```

### TSV

```bash
$ cat sample.tsv
1	0.9	a	A
2	0.8	b	B
3	0.7	c	C
```

```scala
val tsv: DataFrame = spark.read.option("sep", "\t").csv("sample.tsv")
tsv.show()
```

```
+---+---+---+---+
|_c0|_c1|_c2|_c3|
+---+---+---+---+
|  1|0.9|  a|  A|
|  2|0.8|  b|  B|
|  3|0.7|  c|  C|
+---+---+---+---+
```

## 書き込み

```scala
import org.apache.spark.sql.SaveMode
df.write.mode(SaveMode.Overwrite).  // ErrorIfExists, Overwrite
  option("header", "true").         // ヘッダをファイル先頭に付与
  option("compression", "gzip").    // gzip 圧縮
  option("delimiter", "\t").        // カラムのデリミタをタブに
  csv("/path/to/save/directory")    // ファイル保存
```

### SaveMode

| SaveMode | 意味 |
| :-- |  :-- |
| `SaveMode.ErrorIfExists` | データが既に存在する場合、例外を投げる (default) |
| `SaveMode.Append` | データが既に存在する場合、既存データに追記 |
| `SaveMode.Overwrite` | データが既に存在する場合、上書き |
| `SaveMode.Ignore` | データが既に存在する場合、保存を中止し、例外も投げない |

## 種々の操作

### Dataset の 内容確認

```scala
val ds: Dataset[...] = ...
df.show(numRows=30, truncate=false)   // 30行目まで表示 & 長くても "..." で省略しない
df.show()  // デフォルト引数 (numRows=20, truncate=true)
```

### DataFrame → case class の Dataset

（ToDo）

```scala
val df = ...

case class MyCaseClass()
df.as[MyCaseClass]
df.as[(String, String, Int)]
```


### Row の操作

値の取り出し：

```scala
val df: DataFrame = ...
val rowRDD: RDD[Row] = df.rdd
val tupleRDD: RDD[(String, Int, Double)] = rowRDD.map{
  case Row(f1: String, f2: Int, f3: Double) =>
    (f1, f2, f3)
}
```

### カラム名設定

ToDo：`toDF`

### select

※ カラム名の大文字・小文字は区別されない模様

```scala
csvLabeled.select("numInt").show()
csvLabeled.select($"numInt", $"strSmall").show()
```

```
+------+
|numInt|
+------+
|     1|
|     2|
|     3|
+------+
```

```
+------+--------+
|numInt|strSmall|
+------+--------+
|     1|       a|
|     2|       b|
|     3|       c|
+------+--------+
```

### カラムの値の操作

#### 型キャスト

```scala
// キャスト前
csvLabeled
// org.apache.spark.sql.DataFrame = [numInt: string, numDouble: string ... 2 more fields]

// キャスト後
import org.apache.spark.sql.types.{IntegerType, StringType, DoubleType}
val csvConverted = csvLabeled.select(
  $"numInt" cast IntegerType,
  $"numDouble" cast DoubleType,
  $"strSmall",
  $"strLarge"
)
// org.apache.spark.sql.DataFrame = [numInt: int, numDouble: double ... 2 more fields]
```

#### 数値演算

```scala
// 演算
csvConverted.select(
  $"numInt",
  $"numDouble",
  $"numInt" / 2,
  $"numInt" * 100 + $"numDouble" * 3
).show()
```

```
+------+---------+------------+----------------------------------+
|numInt|numDouble|(numInt / 2)|((numInt * 100) + (numDouble * 3))|
+------+---------+------------+----------------------------------+
|     1|      0.9|         0.5|                             102.7|
|     2|      0.8|         1.0|                             202.4|
|     3|      0.7|         1.5|                             302.1|
+------+---------+------------+----------------------------------+
```

#### 文字列演算

```scala
// 文字列
csvConverted.select(
  concat($"strSmall", $"strLarge") as "concat-str-str",
  concat($"strSmall", $"numInt") as "concat-str-num",
  concat_ws("-", $"strLarge", $"strSmall") as "concat_ws-str-str",
  concat_ws("/", $"strLarge", $"numDouble") as "concat_ws-str-num",
  format_string("%s/%03d-%f", $"strLarge", $"numInt", $"numDouble") as "format_string"
).show()

csvConverted.select(
  concat($"strSmall", $"strLarge") as "c1",
  concat($"strSmall", $"numInt") as "c2",
  concat_ws("-", $"strLarge", $"strSmall") as "c3",
  concat_ws("/", $"strLarge", $"numDouble") as "c4",
  format_string("%s/%03d-%f", $"strLarge", $"numInt", $"numDouble") as "c5"
).show()
```

```
+---+---+---+-----+--------------+
| c1| c2| c3|   c4|            c5|
+---+---+---+-----+--------------+
| aA| a1|A-a|A/0.9|A/001-0.900000|
| bB| b2|B-b|B/0.8|B/002-0.800000|
| cC| c3|C-c|C/0.7|C/003-0.700000|
+---+---+---+-----+--------------+
```

#### コレクション操作

```scala
val dsCollection = Seq(
  (List(1, 10, 100, 10, 0.1), Set(1, 10, 1000, 100)),
  (List(2, 20, 200, 20, 0.2), Set(2, 20, 2000, 200)),
  (List(3, 30, 300, 30, 0.3), Set(3, 30, 3000, 300))
).toDF("array", "set")

val dfArray = Seq(
  (List(1, 10, 100, 10, 0.1), List(10, 100)),
  (List(2, 20, 200, 20, 0.2), List(20, 200)),
  (List(3, 30, 300, 30, 0.3), List(30, 300))
).toDF("arr1", "arr2")
```

```scala
dfArray.select(
  array_contains($"arr1", 1),
  sort_array($"arr1")
).show()
```

```
+-----------------------+----------------------+
|array_contains(arr1, 1)|sort_array(arr1, true)|
+-----------------------+----------------------+
|                   true|  [0.1, 1.0, 10.0, ...|
|                  false|  [0.2, 2.0, 20.0, ...|
|                  false|  [0.3, 3.0, 30.0, ...|
+-----------------------+----------------------+
```

#### if-else

`when(<条件1>, <値1>).when(<条件2>, <値2>).otherwise(<値3>)` のような構文を使う。

```scala
csvConverted.select(
  $"numInt",
  $"numDouble",
  when($"numInt" === 3, "pattern-1").when($"numInt" < 3 and $"numDouble" < 0.9, "pattern-2").otherwise("pattern-3") as "if-else"
).show()
```

```
+------+---------+---------+
|numInt|numDouble|  if-else|
+------+---------+---------+
|     1|      0.9|pattern-3|
|     2|      0.8|pattern-2|
|     3|      0.7|pattern-1|
+------+---------+---------+
```

#### 配列の展開

```scala
scala> json.show()
+------------+---+-----+---+
|        list|num|  obj|str|
+------------+---+-----+---+
|[A, AA, AAA]| 10|[1,a]|aaa|
|[B, BB, BBB]| 20|[2,b]|bbb|
|[C, CC, CCC]| 30|[3,c]|ccc|
+------------+---+-----+---+

scala> json.select(
     |   $"list",
     |   explode($"list")
     | ).show()
+------------+---+
|        list|col|
+------------+---+
|[A, AA, AAA]|  A|
|[A, AA, AAA]| AA|
|[A, AA, AAA]|AAA|
|[B, BB, BBB]|  B|
|[B, BB, BBB]| BB|
|[B, BB, BBB]|BBB|
|[C, CC, CCC]|  C|
|[C, CC, CCC]| CC|
|[C, CC, CCC]|CCC|
+------------+---+
```

#### null を別の値に置換

```scala
// price カラムが null だったらゼロに置き換える
df.na.fill(0, Array("price"))
```

### filter

```scala
csvLabeled.filter($"num" === 1).show()
csvLabeled.filter($"num" > 1).show()
csvLabeled.filter($"num" >= 2).show()
json.filter($"num" > 15 and $"obj.n" < 3).show()
```


### select + where

項目を `select` で選択し、続く `where` で条件によってデータを絞る。

```scala
json.select("str").where($"num" > 15 and $"obj.n" < 3)
```


### データのグルーピング・集約

データのグルーピング・集約には `groupBy` と `agg`, `sum`, `max` などの集約関数を組み合わせる。

```scala
case class MyRecord(s1: String, s2: String, n: Int, d: Double)
val ds: Dataset[MyRecord] = Seq(
  MyRecord("a", "x", 1, 0.8),
  MyRecord("a", "y", 2, 0.7),
  MyRecord("b", "x", 3, 0.6),
  MyRecord("b", "y", 4, 0.5),
  MyRecord("b", "x", 1, 0.4),
  MyRecord("c", "y", 2, 0.3),
  MyRecord("c", "x", 3, 0.2),
  MyRecord("c", "y", 4, 0.1)
).toDS()
```

```scala
scala> ds.groupBy("s1").agg(
     |   max("n"),
     |   sum("d"),
     |   collect_list("s2"),
     |   collect_set("s2")
     | ).orderBy("s1").show()
+---+------+------+----------------+---------------+
| s1|max(n)|sum(d)|collect_list(s2)|collect_set(s2)|
+---+------+------+----------------+---------------+
|  a|     2|   1.5|          [x, y]|         [y, x]|
|  b|     4|   1.5|       [x, y, x]|         [y, x]|
|  c|     4|   0.6|       [y, x, y]|         [y, x]|
+---+------+------+----------------+---------------+

scala> ds.groupBy("s1", "s2").max("n", "d").orderBy("s1", "s2").show()
+---+---+------+------+                                                         
| s1| s2|max(n)|max(d)|
+---+---+------+------+
|  a|  x|     1|   0.8|
|  a|  y|     2|   0.7|
|  b|  x|     3|   0.6|
|  b|  y|     4|   0.5|
|  c|  x|     3|   0.2|
|  c|  y|     4|   0.3|
+---+---+------+------+
```

| 集約関数 | 説明 |
| :-- | :-- |
| `max` | 最大値 |
| `min` | 最小値 |
| `sum` | 合計 |
| `avg` | 平均値 |
| `collect_set` | 値を集めた set（重複排除） |
| `collect_list` | 値を集めた list（重複あり） |
| `corr(col1, col2)` | 相関係数 |
| `count` | 件数（重複も数える） |
| `countDistinct` | 件数（重複排除） |
| `covar_pop(col1, col2)` | 母共分散 |
| `covar_samp(col1, col2)` | 標本共分散 |
| `first` | グループ先頭の値 |
| `last` | グループ末尾の値 |
| `mean` | = `avg` |
| `stddev_pop` | 母標準偏差 |
| `stddev_samp` | 標本標準偏差 |
| `stddev` | = `stddev_samp` |
| `var_pop` | 母分散 |
| `var_samp` | 標本分散 |
| `variance` | = `var_samp` |

### ソート

```scala
scala> ds.orderBy($"s1".desc, $"n").show()
+---+---+---+---+
| s1| s2|  n|  d|
+---+---+---+---+
|  c|  y|  2|0.3|
|  c|  x|  3|0.2|
|  c|  y|  4|0.1|
|  b|  x|  1|0.4|
|  b|  x|  3|0.6|
|  b|  y|  4|0.5|
|  a|  x|  1|0.8|
|  a|  y|  2|0.7|
+---+---+---+---+
```

### 集合同士の操作

```scala
val ds1: Dataset[String] = Seq("a", "b", "c", "d").toDS()
val ds2: Dataset[String] = Seq("a", "b", "e", "f").toDS()
```

#### 結合

```scala
scala> ds1.unionAll(ds2).show()
+-----+
|value|
+-----+
|    a|
|    b|
|    c|
|    d|
|    a|
|    b|
|    e|
|    f|
+-----+
```

#### 積集合

```scala
scala> ds1.intersect(ds2).show()
+-----+
|value|
+-----+
|    b|
|    a|
+-----+
```

#### 差分

```scala
scala> ds1.except(ds2).show()
+-----+
|value|
+-----+
|    d|
|    c|
+-----+

scala> ds2.except(ds1).show()
+-----+
|value|
+-----+
|    f|
|    e|
+-----+
```

#### join

```scala
case class MyRecord2(name: String, birthPlace: String)
case class MyRecord3(name: String, age: Int)
val ds1 = Seq(
  MyRecord2("a", "New York"),
  MyRecord2("b", "Tokyo"),
  MyRecord2("c", "London"),
  MyRecord2("d", "Beijing")
).toDS
val ds2 = Seq(
  MyRecord3("a", 10),
  MyRecord3("b", 20),
  MyRecord3("e", 30)
).toDS
```

inner join：

```scala
scala> ds1.join(ds2, ds1("name") === ds2("name"), "inner").show()
+----+----------+----+---+
|name|birthPlace|name|age|
+----+----------+----+---+
|   a|  New York|   a| 10|
|   b|     Tokyo|   b| 20|
+----+----------+----+---+
```

outer join：

```scala
scala> ds1.join(ds2, ds1("name") === ds2("name"), "leftouter").show()
+----+----------+----+----+
|name|birthPlace|name| age|
+----+----------+----+----+
|   a|  New York|   a|  10|
|   b|     Tokyo|   b|  20|
|   c|    London|null|null|
|   d|   Beijing|null|null|
+----+----------+----+----+

scala> ds1.join(ds2, ds1("name") === ds2("name"), "rightouter").show()
+----+----------+----+---+
|name|birthPlace|name|age|
+----+----------+----+---+
|   a|  New York|   a| 10|
|   b|     Tokyo|   b| 20|
|null|      null|   e| 30|
+----+----------+----+---+

scala> ds1.join(ds2, ds1("name") === ds2("name"), "fullouter").show()
+----+----------+----+----+
|name|birthPlace|name| age|
+----+----------+----+----+
|null|      null|   e|  30|
|   d|   Beijing|null|null|
|   c|    London|null|null|
|   b|     Tokyo|   b|  20|
|   a|  New York|   a|  10|
+----+----------+----+----+
```

cross join：

```scala
scala> ds1.crossJoin(ds2).show()
+----+----------+----+---+
|name|birthPlace|name|age|
+----+----------+----+---+
|   a|  New York|   a| 10|
|   a|  New York|   b| 20|
|   a|  New York|   e| 30|
|   b|     Tokyo|   a| 10|
|   b|     Tokyo|   b| 20|
|   b|     Tokyo|   e| 30|
|   c|    London|   a| 10|
|   c|    London|   b| 20|
|   c|    London|   e| 30|
|   d|   Beijing|   a| 10|
|   d|   Beijing|   b| 20|
|   d|   Beijing|   e| 30|
+----+----------+----+---+
```