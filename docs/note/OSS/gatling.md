---
title: Gatling
main_image: https://user-images.githubusercontent.com/13412823/43997632-cd415278-9e1b-11e8-8ad2-bf135d1270d3.png
---

Ver 2.3
http://gatling.io

# Concept

## Virtual User

- Apache Bench や wrk といった負荷テストツールを使えば、URL に対して効果的に負荷をかけられるが、リクエスト間のロジックを扱うことはできない
- Gatling は、独自のデータを持ち、独自のブラウジングパスをたどる仮想ユーザを扱うことができる

## Scenario

- Gatling では、スクリプトの形でユーザの振る舞いを定義する
- 1つのシナリオ = （期待される）ユーザの典型的な振る舞い
- e コマースサイトのシナリオの例
	1. ホームページにアクセス
	2. 商品カテゴリを選択
	3. そのカテゴリ内で商品検索
	4. 商品概要を開く
	5. ブラウザバック
	6. 別の商品概要を開く
	7. 商品を買う
	8. ログイン
	9. チェックアウト
	10. 支払い
	11. ログアウト
- シナリオは以下のように記述する
```scala
scenario("Standard User")
  .exec(http("Access Github").get("https://github.com"))
  .pause(2, 3)
  .exec(http("Search for 'gatling'").get("https://github.com/search?q=gatling"))
  .pause(2)
```

## Simulation

- 1種類あるいは複数種類のシナリオを定義し、シミュレーションを実行する
- `senario("$name")`で指定する Senario 名はレポートに現れない模様
- `http("$name")`で指定するリクエスト名をつけておけば、リクエストごとに分けて結果が見られる

```scala
val stdUser = scenario("Standard User") // etc..
val admUser = scenario("Admin User") // etc..
val advUser = scenario("Advanced User") // etc..

setUp(
  stdUser.inject(atOnceUsers(2000)),
  admUser.inject(nothingFor(60 seconds), rampUsers(5) over (400 seconds)),
  advUser.inject(rampUsers(500) over (200 seconds))
)
```

## Session

各 vertual user の裏側にはセッションがあり、データを inject したり、レスポンスの内容をキャプチャして次のリクエストに使用したりできる

## Feeder

外部ソースからテスト用データを inject する API

## Check

以下の機能を提供する
- レスポンスのステータスやヘッダ・ボディの中身が特定の条件を満たすかチェック
- レスポンスの内容をキャプチャしてセッションに保存し、以降のリクエストで使えるようにする

```scala
exec(...).check(status.is(200))
exec(...).check(bodyString.saveAs("key_name"))
```

## Assertions

- 負荷テストの受け入れ基準（ex. 99%ile レスポンスタイム）を定義
- 基準を満たさない場合、テスト全体としてエラーステータスを返す（テストレポートは作成される）

```scala
setUp(scn).assertions(
  global.responseTime.mean.lessThan(10),
  global.successfulRequests.percent.greaterThan(99)
)
```
失敗時：
```
Global: mean of response time is less than 10 : false
Global: percentage of successful requests is greater than 99 : true
[error] Simulation GatlingTest failed.
[info] Simulation(s) execution ended.
[error] Failed tests:
[error]         jp.hkawabata.gatling.GatlingTest
[error] (gatling:test) sbt.TestsFailedException: Tests unsuccessful
[error] Total time: 121 s, completed 2017/09/18 20:37:07
```
成功時：
```
Global: mean of response time is less than 50 : true
Global: percentage of successful requests is greater than 99 : true
[info] Simulation GatlingTest successful.
[info] Simulation(s) execution ended.
[success] Total time: 116 s, completed 2017/09/18 20:56:40

```


# Simulation

## Throttling

スループットの上限などのボトルネックを定める

- throttle メソッドの時間よりも
	- シナリオの時間の方が長い時：throttle の終了とともにテスト終了
	- シナリオの時間の方が短い時：シナリオ終了とともにテスト終了

```scala
setUp(scn).throttle(
  reachRps(10) in (30 seconds), // 30 sかけて上限を10 rpsまで引き上げる?
  holdFor(1 minute), // 1分間その上限を維持
  jumpToRps(20), // 上限を即時20 rps に変更
  holdFor(3 minutes)) // 3分間その上限を維持
)
```

- Simulation 単位ではなく、シナリオ単位で throttle を設定することもできる

```
scenario(...).throttle(...)
```


# Session


## Feeders

以下のようなものからデータを取り込んでリクエストに使用できる

- コード内で定義する`Array[Map[String, T]]`
- csv, tsv ファイル
- JSON ファイル
- JDBC
- sitemap ファイル

これらを取り込んだあと、以下のメソッドで順序を指定する

```
.queue    // default behavior: use an Iterator on the underlying sequence
.random   // randomly pick an entry in the sequence
.shuffle  // shuffle entries, then behave live queue
.circular // go back to the top of the sequence once the end is reached
```

> **【注意】**`.queue`,`.shuffle`を使用したり、ファイルを読み込むときに上記メソッドを指定しなかったりすると、繰り返し読み込みが行われないので、データ配列の長さを超えるリクエスト数に達すると`java.lang.IllegalStateException: Feeder is now empty, stopping engine`のような例外を吐いて終了する

> **【注意】**`feed`で使うためにファイルを読み込ませる場合、ファイルサイズの5-10倍のメモリを必要とするらしい
> 
> > Loading feeder files in memory uses a lot of heap, expect a 5-to-10-times ratio with the file size. This is due to JVM’s internal UTF-16 char encoding and object headers overhead. If memory is an issue for you, you might want to read from the filesystem on the fly and build your own Feeder.
> 
> `random`モードで使用するときなどはすべて読み込む必要があるため、他のモードであってもあらかじめファイル全部をメモリに読み込む模様。

# Reports

![20170918_gatling_report2](https://user-images.githubusercontent.com/13412823/43997629-c0efdbb6-9e1b-11e8-93c2-c7316bfe09ff.png)

![20170918_gatling_report](https://user-images.githubusercontent.com/13412823/43997628-c0b3de72-9e1b-11e8-8b73-20f87807a757.png)


# Scala コードから使う

## 設定

project/plugins.sbt

```scala
logLevel := Level.Warn

addSbtPlugin("io.gatling" % "gatling-sbt" % "2.2.2")
```

build.sbt

```scala
enablePlugins(GatlingPlugin)

libraryDependencies ++= Seq(
  "io.gatling.highcharts" % "gatling-charts-highcharts" % "2.2.2" % "test",
  "io.gatling" % "gatling-test-framework" % "2.2.2" % "test"
)
```

## テストコードサンプル

```scala
package jp.hkawabata.gatling

import io.gatling.core.Predef._
import io.gatling.core.controller.inject.InjectionStep
import io.gatling.core.structure.ScenarioBuilder
import io.gatling.http.Predef._
import io.gatling.http.protocol.HttpProtocolBuilder

import scala.concurrent.duration._

class GatlingTest extends Simulation {

  val httpConf: HttpProtocolBuilder = http
    .baseURL("http://node001.hkawabata.jp:8983")  // 複数サーバの場合は baseURLs を使えばラウンドロビンで負荷テスト実施
    /*
    .headers(Map(
      HttpHeaderNames.ContentType    -> HttpHeaderValues.ApplicationJson,
      HttpHeaderNames.Accept         -> HttpHeaderValues.ApplicationJson,
      HttpHeaderNames.AcceptEncoding -> "gzip,deflate"
    ))*/

  val scn: ScenarioBuilder = scenario("Basic sinario")
    .repeat(2){
      exec(http("request_1.1")
        .get("/solr/solrbook/select?indent=on&wt=json").queryParam("q", "summary:Solr"))
        .exec(http("request_1.2")
          .get("/solr/solrbook/select?indent=on&wt=json").queryParam("q", "pages:320"))
    }.pause(100 milliseconds)
    .exec(http("request_2")
    .get("/solr/solrbook/select?indent=on&wt=json").queryParam("q", "*:*"))

  val injections: Seq[InjectionStep with Product with Serializable] = Seq(
    rampUsersPerSec(1).to(50).during(20),
    constantUsersPerSec(50).during(20),
    nothingFor(5 seconds),
    atOnceUsers(200),
    nothingFor(5 seconds),
    rampUsers(1000) over (20 seconds),
    rampUsersPerSec(50).to(1).during(20)
  )

  setUp(scn.inject(injections)).protocols(httpConf)
}
```

## テスト実行

```bash
$ sbt gatling:test

...
Reports generated in 0s.
Please open the following file: /Users/kawabatahiroto/workspace/Scala/gatling/target/gatling/gatlingtest-1505541282743/index.html
[info] Simulation GatlingTest successful.
[info] Simulation(s) execution ended.
[success] Total time: 8 s, completed 2017/09/16 14:54:46
```

ログに書かれたパスにある index.html を開けばレポートが見られる


## sbt コマンド

| コマンド | 説明 |
| :-- | :-- |
| `sbt gatling:test` | 負荷テスト実行 |
| `sbt "gatling:testOnly <テストクラスのFQCN>"` | 指定したテストクラスのみ実行 |
| `sbt copyLogbackXml` | デフォルト設定の logback.xml を作成(src/test/resources/logback.xml) |
| `sbt startRecorder` | ブラウザ操作記録開始 |
| `sbt copyConfigFiles` | gatling.conf, recorder.confが存在しない場合に作成 |


# バイナリを解凍して使う

## ダウンロード・解凍

```bash
$ wget https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/2.2.2/gatling-charts-highcharts-bundle-2.2.2-bundle.zip

$ unzip gatling-charts-highcharts-bundle-2.2.2-bundle.zip

$ cd gatling-charts-highcharts-bundle-2.2.2
```

## ディレクトリ構成

```
$ tree
.
├── LICENSE
├── bin
│   ├── gatling.bat
│   ├── gatling.sh
│   ├── recorder.bat
│   └── recorder.sh
├── conf
│   ├── gatling-akka.conf
│   ├── gatling.conf
│   ├── logback.xml
│   └── recorder.conf
├── lib
│   ├── HdrHistogram-2.1.9.jar
│   ├── Saxon-HE-9.7.0-5.jar
│   ├── akka-actor_2.11-2.4.7.jar
│   ├── akka-slf4j_2.11-2.4.7.jar
│   ├── async-http-client-2.0.6.jar
│   ├── bcpkix-jdk15on-1.54.jar
│   ├── bcprov-jdk15on-1.54.jar
│   ├── boon-json-0.6.2.jar
│   ├── boon-reflekt-0.6.2.jar
│   ├── boopickle_2.11-1.2.0.jar
│   ├── commons-pool-1.6.jar
│   ├── concurrentlinkedhashmap-lru-1.4.2.jar
│   ├── config-1.3.0.jar
│   ├── fastring_2.11-0.2.4.jar
│   ├── gatling-app-2.2.2.jar
│   ├── gatling-charts-2.2.2.jar
│   ├── gatling-charts-highcharts-2.2.2.jar
│   ├── gatling-commons-2.2.2.jar
│   ├── gatling-core-2.2.2.jar
│   ├── gatling-http-2.2.2.jar
│   ├── gatling-jdbc-2.2.2.jar
│   ├── gatling-jms-2.2.2.jar
│   ├── gatling-metrics-2.2.2.jar
│   ├── gatling-recorder-2.2.2.jar
│   ├── gatling-redis-2.2.2.jar
│   ├── geronimo-jms_1.1_spec-1.1.1.jar
│   ├── jackson-annotations-2.7.0.jar
│   ├── jackson-core-2.7.5.jar
│   ├── jackson-databind-2.7.5.jar
│   ├── jackson-dataformat-csv-2.7.5.jar
│   ├── javassist-3.20.0-GA.jar
│   ├── jodd-core-3.7.1.jar
│   ├── jodd-lagarto-3.7.1.jar
│   ├── jodd-log-3.7.1.jar
│   ├── jsonpath_2.11-0.6.7.jar
│   ├── logback-classic-1.1.7.jar
│   ├── logback-core-1.1.7.jar
│   ├── netty-buffer-4.0.37.Final.jar
│   ├── netty-codec-4.0.37.Final.jar
│   ├── netty-codec-dns-2.0.6.jar
│   ├── netty-codec-http-4.0.37.Final.jar
│   ├── netty-common-4.0.37.Final.jar
│   ├── netty-handler-4.0.37.Final.jar
│   ├── netty-reactive-streams-1.0.6.jar
│   ├── netty-resolver-2.0.6.jar
│   ├── netty-resolver-dns-2.0.6.jar
│   ├── netty-transport-4.0.37.Final.jar
│   ├── netty-transport-native-epoll-4.0.37.Final-linux-x86_64.jar
│   ├── quicklens_2.11-1.4.7.jar
│   ├── reactive-streams-1.0.0.jar
│   ├── redisclient_2.11-3.1.jar
│   ├── scala-compiler-2.11.8.jar
│   ├── scala-java8-compat_2.11-0.8.0-RC1.jar
│   ├── scala-library-2.11.8.jar
│   ├── scala-logging_2.11-3.4.0.jar
│   ├── scala-parser-combinators_2.11-1.0.4.jar
│   ├── scala-reflect-2.11.8.jar
│   ├── scala-swing_2.11-1.0.2.jar
│   ├── scala-xml_2.11-1.0.5.jar
│   ├── scopt_2.11-3.5.0.jar
│   ├── slf4j-api-1.7.21.jar
│   ├── t-digest-3.1.jar
│   └── zinc
│       ├── compiler-interface-0.13.9-sources.jar
│       ├── config-1.3.0.jar
│       ├── gatling-compiler-2.2.2.jar
│       ├── incremental-compiler-0.13.9.jar
│       ├── logback-classic-1.1.7.jar
│       ├── logback-core-1.1.7.jar
│       ├── sbt-interface-0.13.9.jar
│       ├── scala-library.jar
│       ├── scala-reflect.jar
│       ├── scopt_2.10-3.5.0.jar
│       ├── slf4j-api-1.7.21.jar
│       └── zinc-0.3.9.jar
├── results
│   └── 0-1514261880838
│       ├── index.html
│       ├── js
│       │   ├── all_sessions.js
│       │   ├── assertions.json
│       │   ├── assertions.xml
│       │   ├── bootstrap.min.js
│       │   ├── gatling.js
│       │   ├── global_stats.json
│       │   ├── highcharts-more.js
│       │   ├── highstock.js
│       │   ├── jquery.min.js
│       │   ├── menu.js
│       │   ├── moment.min.js
│       │   ├── stats.js
│       │   ├── stats.json
│       │   ├── theme.js
│       │   └── unpack.js
│       ├── req_request-1-46da4.html
│       ├── req_request-1-redir-7e85b.html
│       ├── req_request-10-1cfbe.html
│       ├── req_request-10-redi-69a19.html
│       ├── req_request-2-93baf.html
│       ├── req_request-3-d0973.html
│       ├── req_request-4-e7d1b.html
│       ├── req_request-4-redir-036f2.html
│       ├── req_request-5-48829.html
│       ├── req_request-6-027a9.html
│       ├── req_request-7-f222f.html
│       ├── req_request-8-ef0c8.html
│       ├── req_request-9-d127e.html
│       ├── simulation.log
│       └── style
│           ├── arrow_down.png
│           ├── arrow_down_black.png
│           ├── arrow_right.png
│           ├── arrow_right_black.png
│           ├── bootstrap.min.css
│           ├── cible.png
│           ├── favicon.ico
│           ├── fond-degrade.gif
│           ├── fond-lueur.gif
│           ├── little_arrow_right.png
│           ├── logo-gatling.jpg
│           ├── logo.png
│           ├── sortable.png
│           ├── sorted-down.png
│           ├── sorted-up.png
│           ├── stat-fleche-bas.png
│           ├── stat-fond.png
│           ├── stat-l-roue.png
│           ├── stat-l-temps.png
│           └── style.css
├── target
│   └── test-classes
│       ├── computerdatabase
│       │   ├── BasicSimulation.class
│       │   └── advanced
│       │       ├── AdvancedSimulationStep01$Browse$.class
│       │       ├── AdvancedSimulationStep01$Edit$.class
│       │       ├── AdvancedSimulationStep01$Search$.class
│       │       ├── AdvancedSimulationStep01.class
│       │       ├── AdvancedSimulationStep02$Browse$.class
│       │       ├── AdvancedSimulationStep02$Edit$.class
│       │       ├── AdvancedSimulationStep02$Search$.class
│       │       ├── AdvancedSimulationStep02.class
│       │       ├── AdvancedSimulationStep03$Browse$.class
│       │       ├── AdvancedSimulationStep03$Edit$.class
│       │       ├── AdvancedSimulationStep03$Search$.class
│       │       ├── AdvancedSimulationStep03.class
│       │       ├── AdvancedSimulationStep04$Browse$.class
│       │       ├── AdvancedSimulationStep04$Edit$.class
│       │       ├── AdvancedSimulationStep04$Search$.class
│       │       ├── AdvancedSimulationStep04.class
│       │       ├── AdvancedSimulationStep05$Browse$.class
│       │       ├── AdvancedSimulationStep05$Edit$$anonfun$1.class
│       │       ├── AdvancedSimulationStep05$Edit$.class
│       │       ├── AdvancedSimulationStep05$Search$.class
│       │       └── AdvancedSimulationStep05.class
│       └── zincCache
└── user-files
    ├── bodies
    ├── data
    │   └── search.csv
    └── simulations
        └── computerdatabase
            ├── BasicSimulation.scala
            └── advanced
                ├── AdvancedSimulationStep01.scala
                ├── AdvancedSimulationStep02.scala
                ├── AdvancedSimulationStep03.scala
                ├── AdvancedSimulationStep04.scala
                └── AdvancedSimulationStep05.scala

18 directories, 163 files
```

## 各ファイルの配置

| ファイル | 配置場所 |
| :-- | :-- |
| `Simulation`ファイル | user-files/simulations 以下（必ずしもパッケージ階層を守る必要はない？） |
| その他自作の Scala ファイル（`Hoge.scala`） | 同上 |
| `Feeder`から読むためのデータファイル | user-files/data 以下 |
| properties ファイル | conf/ 以下 |
| logback.xml など | conf/ 以下 |


## 負荷テスト実行

```bash
$ bin/gatling.sh
```

## 複数サーバで実行した結果を合わせたレポートを作る

```bash
$ bin/gatling.sh -ro ${MY_SIMULATION_LOG_DIR}
```

`${MY_SIMULATION_LOG_DIR}`は result/ 以下にないとダメ？


# 各種設定

conf/gatling.conf に記述する設定項目

## レスポンスタイムの区切り境界値

`lowerBound`,`higherBound`に記述する（ms 単位）。

```
gatling {
  ...
  charting {
    indicators {
      lowerBound = 20      # Lower bound for the requests' response time to track in the reports and the console summary
      higherBound = 200    # Higher bound for the requests' response time to track in the reports and the console summary
      #percentile1 = 50      # Value for the 1st percentile to track in the reports, the console summary and Graphite
      #percentile2 = 75      # Value for the 2nd percentile to track in the reports, the console summary and Graphite
      #percentile3 = 95      # Value for the 3rd percentile to track in the reports, the console summary and Graphite
      #percentile4 = 99      # Value for the 4th percentile to track in the reports, the console summary and Graphite
    }
  }
  ...
}
```


# Tips

## 便利メソッド

| メソッド | 説明 |
| :-- | :-- |
| `exitHereIfFailed` | レスポンスステータスチェックなどが失敗した場合、そこで処理を止めて以降のシナリオには進まない（これがないと、エラーが起こっても次の exec に進む） |
| `tryMax(times: Int){ exec(...) }` | リトライ機能？ |
|  |  |
|  |  |
|  |  |

## アプリケーションのウォームアップ

定常的にリクエストが来るようなアプリケーションのテストを行う場合、テストの前に定常的な負荷を掛けておきたい。

- 方法1: テスト用シナリオとは別にウォームアップ用のシナリオを作成する
- 方法2: シナリオにウォームアップも含め、テスト後 simulation.log からウォームアップ中のレコードを削除してからレポートを作成する


# トラブルシューティング

## Unexpected character '"'

feeder を使って tsv ファイルを読んだときのエラー。

```
Exception in thread "main" java.lang.RuntimeException: Unexpected character ('"' (code 34)): Expected separator ('"' (code 34)) or end-of-line
```

tsv でダブルクオートがカラムの両端以外に来るとエラーになる？

vim で一括エスケープ（`:%s/\"/\\\"/g`）すると解消した。

## Cannot assign requested address

リクエストがほとんど全てエラーになる。

投げる側のエラー。

```
================================================================================
2019-03-18 17:05:39                                         140s elapsed
---- Access with param 'hoge' ------------------------------------
[####                                                                      ]  6%
          waiting: 12099  / active: 0      / done:801   
---- Access with param 'q' -----------------------------------------------------
[##-                                                                       ]  3%
          waiting: 5817945 / active: 505    / done:240650
---- Access with param 'q', 'all' -------------------------------------
[####-                                                                     ]  6%
          waiting: 12099  / active: 1      / done:800   
---- Requests ------------------------------------------------------------------
> Global                                                   (OK=28535  KO=213774)
> hoge                                                     (OK=359    KO=442   )
> q                                                        (OK=27818  KO=212890)
> q, all                                                   (OK=358    KO=442   )
---- Errors --------------------------------------------------------------------
> j.n.ConnectException: Cannot assign requested address: pfmtest 213522 (99.88%)
-api.example.jp/xxx.xxx.xxx.xxx:8080
> status.find.is(200), but actually found 500                       252 ( 0.12%)
================================================================================
```

デフォルトだとユーザごとにコネクションプールを持つ設定になっているらしく、コネクションが枯渇している模様。

`HttpProtocolBuilder`に`.shareConnections`を設定すると解決。

```scala
val httpConf: HttpProtocolBuilder = http.baseURLs(hosts.map(host => s"http://$host:$port")).shareConnections
```

# 読むと良いかもしれないページ

- [gatlingによる負荷試験で、負荷をかける側にしたチューニング](https://qiita.com/shokos@github/items/78d994d6673d8eb44348)
