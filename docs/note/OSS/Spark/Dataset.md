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
case class MyRecord(obj: MySubObj, list: List[String], num: Int, str: String)
val schema: StructType = ScalaReflection.schemaFor[MyRecord].dataType.asInstanceOf[StructType]

val records: Dataset[MyRecord] = spark.read.schema(schema).json("sample.json").as[MyRecord]
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
df.write.mode(SaveMode.Overwrite).
  option("header", "true").
  csv("/path/to/save/directory")
```

## 種々の操作

### select

※ カラム名の大文字・小文字は区別されない模様

#### 特定カラムの抽出

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

#### if-else

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

### filter

```scala
csvLabeled.filter($"num" === 1).show()
csvLabeled.filter($"num" > 1).show()
csvLabeled.filter($"num" >= 2).show()
json.filter($"num" > 15 and $"obj.n" < 3).show()
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

### join

