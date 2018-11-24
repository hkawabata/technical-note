---
title: 10. 開発運用の TIPS
---

# 10.1 サイジング

## CPU

必要な CPU リソースは以下のもので決まる

1. クエリ実行頻度（QPS）
2. クエリの種類
	- OR, AND を多くつなげたものは高負荷
	- グルーピングなどの拡張機能の利用
3. クエリ以外
	- データサイズやコミット頻度

## メモリ

- JVM ヒープサイズを十分確保していおくことで、適切にキャッシュが利用できる
	- 検討が難しい場合は 4-8GB をひとまず割り当ててみる
- インデックスの更新がそれほど頻繁でないシステムであれば、OS のファイルキャッシュをインデックスファイル用に確保しておくことで I/O 負荷を下げ、検索性能向上が見込める
- 一般に、利用可能な RAM のうち1/3-1/2を Solr JVM、残りを OS のファイルキャッシュに割り当てるのが適切とされる

## ストレージ

- ドキュメントのサイズと数、store の有無から見積もる
	- インデクシングさえしておけば検索は可能なので、必要なものだけ store するようにする
- ディスクサイズはインデックスサイズの最低でも2倍確保する
	- オプティマイズやマージの際に、一時的に既存のインデックスと同程度のディスク容量が必要になるため


# 10.2 モニタリング

## 管理画面からの確認

管理画面でコレクションを選択し、「Plugins/Stats」から各種統計情報を取得できる

## REST API からの確認

MBean Request Handler へ REST API からアクセスして性能情報を取得できる。

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/admin/mbeans?stats=true&wt=json&indent=true"
```

以下のパラメータが指定できる

| パラメータ | 値 | 説明 |
| :-- | :-- | :-- |
| cat | CORE<br>QUERYHANDLER<br>QUERYPARSER<br>UPDATEHANDLER<br>CACHE<br>HIGHLIGHTING<br>OTHER | 表示する情報を指定した最上位カテゴリのものだけに限定 |
| key | documentCache<br>searcher<br>etc... | JMX の type に相当。取得したい情報のキー |
| wt | standard<br>javabin<br>json<br>python<br>ruby<br>php<br>phps | 出力フォーマット |
| indent | true<br>false | true なら出力結果を整形 |


## JMX からの確認

- **JMX (Java Management Extensions)**: Java におけるリソースのモニタリングや監視、操作を行うための API
- 監視用ミドルウェアは多数存在するが、ここでは JDK 付属の GUI ツールである JConsole を使用
- JMX 経由で情報を取得するには Solr と環境変数の設定が必要：
	- 監視対象コアの solrconfig.xml に`<jmx />`の記述が必要
	- Solr 起動前に`export ENABLE_REMOTE_JMX_OPTS="true"`と環境変数を設定

```bash
$ jconsole
```

ホストと JMX のポート（デフォルトは18983）を指定して接続：

![20171031_jconsole001](https://user-images.githubusercontent.com/13412823/44093003-1259e382-a00d-11e8-9987-1a08f822b3d5.png)

負荷テストツール Gatling を使って大量のリクエストを投げたとき（グラフの中頃の時刻）：

![20171031_jconsole002](https://user-images.githubusercontent.com/13412823/44093004-1285d5fa-a00d-11e8-900d-65e2fb08fc64.png)

また、MBeans メニューから様々な情報が取得できる。

主なモニタリング項目（REST API と共通）：

![20171031_solr_jmx](https://user-images.githubusercontent.com/13412823/44093005-12b01572-a00d-11e8-9af8-f92019c5eddb.png)

他にもイロイロある。


# 10.3 Solr 4 系からのバージョンアップ

## Java バージョンの変更

Solr 6 系ではサーバ・クライアントともに Java 8 以上が必要。

## war デプロイの廃止および起動方法の変更

- Solr 4 まで：war 形式のウェブアプリケーションとして提供される
- Solr 5 から：スタンドアローンの検索サーバ（組み込みの Jetty 上で動作）
	- Tomcat や GlassFish など外部のサーブレットコンテナへのデプロイはサポート対象外

## デフォルトの SchemaFactory の変更

- Solr 6 より、SchemaFactory として ManagedIndexSchemaFactory がデフォルトに
- 従来の schema.xml からの移行手順は2通り：
	1. schema.xml を conf/ 以下に配置して Solr を起動する（schema.xml から managed-schema が自動生成される）
	2. schema.xml をそのまま使う（ClassicIndexSchemaFactory を使うよう solrconfig.xml に設定を書く）

## デフォルトの Similarity の変更

Solr 6 より、TFIDFSimilarity → BM25Similarity

## SolrJ API の変更

4系までの`org.apache.solr.client.solrj.SolrServer`は廃止。`org.apache.solr.client.solrj.SolrClient`を利用する。


# 10.4 ログの設定

## Solr ログ

- Solr 及びバンドルされている Jetty のログは、デフォルトでは ${SOLR}/server/logs 以下に出力される
	- solr.log が現在のログファイル
	- ファイルサイズが 4MB を超えるとローテーション
	- 末尾の番号が大きいほど古い
	- 9世代を超えると削除

```bash
$ ls -1 server/logs
archived
solr-8983-console.log
solr.log
solr.log.1
solr.log.2
solr.log.3
solr.log.4
solr.log.5
solr.log.6
solr.log.7
solr.log.8
solr.log.9
solr_gc.log.0.current
```

- ログローテートの設定を変更する場合、${SOLR}/server/resources/log4j.properties を修正する
- ログ出力先を変更する場合、Solr 起動時に環境変数を設定する

```bash
$ export SOLR_LOGS_DIR=/path/to/log/dir
$ bin/solr start
```

- コンソールログの出力
	- デフォルトでは ${SOLR_LOGS_DIR} 以下の solr-(ポート番号)-console.log に書き出される
	- Solr 起動時に -f オプションを指定すると Solr がフォアグラウンドで起動し、ターミナルにログが書き出される
- ログレベルの変更（デフォルトは INFO）
	1. 環境変数 SOLR_LOG_LEVEL を指定
	2. Solr 起動時に -v（DEBUG）または -q（WARN）オプションを指定
	3. API から変更（`curl -s "http://${HOSTNAME}:${PORT}/solr/admin/info/logging" --data-binary "set=root:DEBUG&wt=json"`）
- 検索リクエストログ
	- ログレベルを INFO にしていれば、以下のフォーマットで検索リクエストとヒット件数、処理時間が Solr ログに出力される

```bash
2017-10-30 23:19:37.780 INFO  (qtp55909012-22) [   x:solrbook] o.a.s.c.S.Request [solrbook]  webapp=/solr path=/select params={q=summary:Solr&indent=on&wt=json} hits=0 status=0 QTime=0
```

※ QTime は Solr 内部のリクエスト処理時間であり、結果を JSON に整形する時間や通信時間は含まれない

- スロークエリの特定
	- **スロークエリ**：通常のクエリよりも処理に時間がかかるクエリ
	- ログレベルを INFO にしておけば前述の通りログファイルの QTime を見てスロークエリを特定できる
	- ログレベルを WARN 以上にしている場合、以下のように solrconfig.xml に書いておけば指定閾値以上の時間がかかったリクエストをスロークエリとして記録しておいてくれる
```xml
<slowQueryThresholdMillis>1000</slowQueryThresholdMillis>
```


## GC ログ

- Solr ログと同じ ${SOLR_LOGS_DIR}/solr_gc.log.0.current に記録される
- 古いログは ${SOLR_LOGS_DIR}/archived/ 以下に置かれる


# 10.5 Distributed IDF

- Similarity 計算には IDF 値が必要
- 本来は全ドキュメントを使って統計量を取るべき
- 分散検索環境でシャートが複数ある場合
	- Solr 4 まではシャードごとの IDF を計算して Similarity を算出しておりランキングが不正確になる恐れ
	- Solr 5 以上では **Distributed IDF** が導入され、分散検索時も正確なランキングが返せるように

デフォルトでは Distributed IDF は無効なので、solrconfig.xml に以下の設定を行う。

```xml
<statsCache class="org.apache.solr.search.stats.ExactStatsCache"/>
```

class 属性に指定できるもの：

| クラス | 説明 |
| :-- | :-- |
| `LocalStatsCache` | シャードごとのローカル IDF を使う（Distributed IDF 無効, デフォルト） |
| `ExactStatsCache` | コレクションのグローバル IDF を使う |
| `ExactSharedStatsCache` | `ExactStatsCache`と同じだが、後続のリクエストで同じタームについて IDF が必要になった場合に、前のリクエストで使った値を再利用する |
| `LRUStatsCache` | グローバル IDF を LRU キャッシュでキャッシュする |

シャード数やリクエスト数が多く、Distributed IDF の計算オーバーヘッドが懸念される場合は後ろの2つを使うことを検討する。


# 10.6 FAQ

大事そうなものを抜粋。

## 定義できるフィールド数に制限はあるか？

- 明確な数値として上限はない
- Solr メーリングリストで話されていた上限：
	- ノードあたりのドキュメント数 5000万-1億
	- ドキュメントあたりのフィールド数 250
	- ドキュメントあたりの文字数 25万
	- ファセットの数 25
	- SolrCloud のクラスター数 32ノード程度
	- 1度に検索結果として返すドキュメント数 250


## Solr 起動が極端に遅い

- トランザクションログのサイズを確認してみる。これが大きすぎると起動が遅くなる
