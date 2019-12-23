---
title: クイックスタート
---

# 1. Java / Python のインストール

Spark は Java / Scala / Python の API を提供している。

- Java / Scala を使う場合
  - Java をインストール
  - `JAVA_HOME`の値を /etc/profile に追記
- Python を使う場合
  - Python をインストール


# 2. Spark のダウンロード

公式サイトからバージョンを選択してダウンロードして展開。

```bash
$ wget https://www.apache.org/dyn/closer.lua/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
$ tar -xf spark-2.4.4-bin-hadoop2.7.tgz
$ cd spark-2.4.4-bin-hadoop2.7
```

# 3. 設定

設定ファイルを conf/ に配置。

主要な設定ファイルの .template ファイルが conf/ に用意されている。

```
# log4j.properties
# 大量の INFO ログを抑制するための設定
log4j.rootCategory=WARN, console
```

# 4. spark-shell の起動

Scala / Python では対話環境が使える。

Scala:

```bash
$ bin/spark-shell
```

Python:

```bash
$ bin/pyspark
```

サンプルコードを叩いてみる：

```scala
scala> val rdd = sc.makeRDD(Seq(1, 2, 3, 4, 5))
rdd: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at makeRDD at <console>:27

scala> rdd.map(x => x * 10).reduce((x, y) => x + y)
res0: Int = 150
```

`sc`は`SparkContext`オブジェクトで、対話環境の場合は自動で変数`sc`として作られる。

# 5. spark-submit の起動

jar に固めたアプリケーションを実行する（以下は Scala の例）。

build.sbt に依存性を記述：

```scala
name := "myapp"

version := "1.0"

scalaVersion := "2.11.7"

libraryDependencies ++= Seq(
  // "provided": Spark 自身がパッケージを持っているので jar に混ぜ込む必要がない
  "org.apache.spark" %% "spark-core" % "2.4.4" % "provided"
)
```

アプリケーションを実装：

```scala
import org.apache.spark.{SparkConf, SparkContext}

object MainApp {
  def main(args: Array[String]): Unit = {
    // ここはドライバの処理
    // SparkContext インスタンスを作成
    val conf = new SparkConf().setAppName(getClass.getName)
    val sc = new SparkContext(conf)

    // RDD を作成
    val rdd = sc.makeRDD(Seq(1, 2, 3, 4, 5))

    // 分散処理
    val rdd2 = rdd.map{
      x =>
        // ここはエグゼキュータ内の処理
        // map や filter の中の処理は各エグゼキュータで並列に実行される
        x * 10
    }

    // 処理結果をファイルとして保存
    rdd2.saveAsTextFile("/path/to/result")
  }
}
```

jar に固めて実行：

```bash
$ bin/spark-submit --class MainApp myapp.jar
```
