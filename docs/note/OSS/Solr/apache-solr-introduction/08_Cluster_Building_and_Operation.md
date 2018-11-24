---
title: 8. クラスタ構築と運用
---

# 8.1 単一ノードの限界

- 大量のドキュメントを扱いたい時
	- ストレージやメモリリソースの限界
- 一度に大量のインデクシングを行いつつ、大量の検索リクエストを処理する必要がある時
	- ストレージへの I/O、検索時の CPU 負荷、目盛りの枯渇

# 8.2 分散インデックスと分散検索

## 分散インデックス

1つの巨大なインデックスを小さなインデックスに分割し、複数ノードに分散配置。
- ストレージの分散により、論理的に巨大なインデックスを構築可能
- 並列処理により、インデクシングのスループット（DPS: Documents Per Second）

## 分散検索

複数ノードに分散配置されたインデックス（=**シャード**）を一括して検索。
複数シャードを一括検索するには、shards パラメータに Solr エンドポイントの URL（から http:// を除いたもの）をカンマ区切りで指定する。

```bash
curl "http://${HOSTNAME}:${PORT}/solr/${COLLECTION}/select?indent=on&q=*:*&wt=json&shards=${HOST1}:${PORT1}/solr/${COLLECTION},${HOST2}:${PORT2}/solr/${COLLECTION},..."
```

内部的には、最初にリクエストを受け取るノードが shards パラメータで指定されたノードに対して検索リクエストを発行し、結果をマージしてクライアントに返す。


## 分散検索のエラー回避

検索対象のシャードでエラーが発生し、ノードの一部がダウンしているとき、分散検索を行うと以下のようなエラーが発生する。

`org.apache.solr.client.solrj.SolrServerException: Server refused connection at: http://localhost:8985/solr/myCollection`

このエラーは shards.tolerant=true をつけることで回避できる（当然、ダウンしたノードが持つシャードのデータは得られない）。

また、shards.info=true を指定すればシャードごとの情報も得られる。

```json
$ curl "http://${HOSTNAME}:8984/solr/${COLLECTION}/select?indent=on&q=*:*&wt=json&shards=localhost:8984/solr/solrbook,localhost:8985/solr/solrbook&shards.tolerant=true&shards.info=true" | jq '.["shards.info"]'
{
  "localhost:8984/solr/solrbook": {
    "numFound": 99,
    "maxScore": 1,
    "shardAddress": "http://localhost:8984/solr/solrbook",
    "time": 6
  },
  "localhost:8985/solr/solrbook": {
    "error": "java.net.ConnectException: Connection refused (Connection refused)",
    "trace": "java.net.ConnectException: Connection refused (Connection refused)\n\tat java.net.PlainSocketImpl.socketConnect(Native Method)\n\tat java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:350)\n\tat java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)\n\tat java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:188)\n\tat java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)\n\tat java.net.Socket.connect(Socket.java:589)\n\tat org.apache.http.conn.scheme.PlainSocketFactory.connectSocket(PlainSocketFactory.java:117)\n\tat org.apache.http.impl.conn.DefaultClientConnectionOperator.openConnection(DefaultClientConnectionOperator.java:177)\n\tat org.apache.http.impl.conn.ManagedClientConnectionImpl.open(ManagedClientConnectionImpl.java:304)\n\tat org.apache.http.impl.client.DefaultRequestDirector.tryConnect(DefaultRequestDirector.java:611)\n\tat org.apache.http.impl.client.DefaultRequestDirector.execute(DefaultRequestDirector.java:446)\n\tat org.apache.http.impl.client.AbstractHttpClient.doExecute(AbstractHttpClient.java:882)\n\tat org.apache.http.impl.client.CloseableHttpClient.execute(CloseableHttpClient.java:82)\n\tat org.apache.http.impl.client.CloseableHttpClient.execute(CloseableHttpClient.java:55)\n\tat org.apache.solr.client.solrj.impl.HttpSolrClient.executeMethod(HttpSolrClient.java:498)\n\tat org.apache.solr.client.solrj.impl.HttpSolrClient.request(HttpSolrClient.java:262)\n\tat org.apache.solr.client.solrj.impl.HttpSolrClient.request(HttpSolrClient.java:251)\n\tat org.apache.solr.client.solrj.SolrClient.request(SolrClient.java:1219)\n\tat org.apache.solr.handler.component.HttpShardHandler.lambda$submit$0(HttpShardHandler.java:195)\n\tat java.util.concurrent.FutureTask.run(FutureTask.java:266)\n\tat java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)\n\tat java.util.concurrent.FutureTask.run(FutureTask.java:266)\n\tat org.apache.solr.common.util.ExecutorUtil$MDCAwareThreadPoolExecutor.lambda$execute$0(ExecutorUtil.java:229)\n\tat java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)\n\tat java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)\n\tat java.lang.Thread.run(Thread.java:748)\n",
    "shardAddress": "http://localhost:8985/solr/solrbook",
    "time": 6
  }
}
```


# 8.3 レプリケーション

- 大量の検索トラフィックが流れてくる場合、単一のノードでは処理しきれない
- ハードウェア障害などにより一部ノードがダウンすると、そのノードが復旧するまでデータが欠損してしまう

→ インデックスのレプリカ（複製）を作成し、負荷分散を図る & 耐障害性を向上させる

## レプリケーションの概要

- マスター・スレーブ構成を取り、レプリケーションを管理できる
- Solr のレプリケーションは検索やインデクシングなどと同様に、リクエストハンドラとして実装されている

## マスター/スレーブの設定方法と設定項目

### マスター
solrconfig.xml
```xml
<config>
  ...
  <!-- A request handler for replication -->
  <requestHandler name="/replication" class="solr.ReplicationHandler">
    <lst name="master">
      <str name="replicationAfter">optimize</str>
      <str name="backupAfter">optimize</str>
      <str name="confFiles">schema.xml,stopwords.txt,elevate.xml</str>
      <str name="commitReserveDuration">00:00:10</str>
    </lst>
    <int name="maxNumberOfBackups">2</int>
    <lst name="invariants">
      <str name="maxWriteMBPerSec">16</str>
    </lst>
  </requestHandler>
  ...
</config>
```

| 項目 | 説明 |
| :-- | :-- |
| replicateAfter | レプリケーションを行うタイミングを指定。startup（マスターが起動した時）, commit, optimize から選択できる |
| backupAfter | インデックスのバックアップタイミングを指定。startup, commit, optimize から選択できる |
| confFiles | カンマ区切りで指定された設定ファイルをレプリケーション実行時にスレーブへコピー。ファイルパスは絶対パスか、conf からの相対パスで指定 |
| commitReserveDuration | コミットが頻繁に行われたり、ネットワークが遅くレプリケーションが追いつかない時、指定した時間よりも短い間隔でレプリケーションが行われないように調整。デフォルトは10秒 |
| maxNumvberOfBackups | バックアップが保持する世代数を整数値で指定。これを超えると古い世代から削除される |
| maxWriteMBPerSec | レプリケーション実行時の最大書き込み速度を MB/s で指定 |


### スレーブ
solrconfig.xml
```xml
<config>
  ...
  <!-- A request handler for replication -->
  <requestHandler name="/replication" class="solr.ReplicationHandler">
    <lst name="slave">
            <str name="masterUrl">http://localhost:8984/solr/solrbook/replication</str>
      <str name="pollInterval">00:00:20</str>
      <str name="compression">internal</str>
      <str name="httpConnTimeout">5000</str>
      <str name="httpReadTimeout">10000</str>
      <str name="httpBasicAuthUser">hkawabata</str>
      <str name="httpBasicAuthPassword">password</str>
    </lst>
  </requestHandler>
  ...
</config>
```

| 項目 | 説明 |
| :-- | :-- |
| masterUrl | マスターのレプリケーションハンドラのエンドポイント URL を指定 |
| pollInterval | スレーブがマスターをポーリングする間隔。00:00:00 を指定すると、ポーリングを行わない |
| compression | インデックスファイルを転送するときに圧縮する<br>・internal: 全て自動的に行う<br>・external: マスターは Accept-encoding ヘッダを守る設定がされていることを確認する必要がある（？？？） |
| httpConnTimeout | スレーブがマスターに接続する際のタイムアウト値（ms） |
| httpReadTimeout | スレーブがマスターから読み込みを行う際のタイムアウト値（ms） |
| httpBasicAuthUser | マスターに Basic 認証が有効にされている場合にユーザ名を指定 |
| httpBasicPassword | マスターに Basic 認証が有効にされている場合にパスワードを指定 |


## マスター/スレーブのセットアップ

マスター/スレーブのサーバをそれぞれ起動すると、以下のようなレプリケーションの管理画面にアクセスできる（http://ホスト名:ポート番号/solr/#/コレクション名/replication）。

![20171022_solr_master](https://user-images.githubusercontent.com/13412823/44092661-1a2e3276-a00c-11e8-924f-6afa973331a5.png)

![20171022_solr_slave](https://user-images.githubusercontent.com/13412823/44092663-1a84f8f4-a00c-11e8-97aa-305247395dfc.png)

## レプリケーションの確認

master に対してデータを登録すると、slave のポーリングのタイミングでレプリケーションが実行される。

### マスター管理画面

![20171022_solr_master2](https://user-images.githubusercontent.com/13412823/44092662-1a5a627e-a00c-11e8-9e84-8fbfc0e9da58.png)

- Index カラム
	- Master (Searching): マスターが検索で使用しているインデックスの情報
	- Master (Replicable): マスターのレプリケーション可能なインデックスの情報
- Version カラム: インデックスバージョン
- Gen カラム: インデックスの世代バージョン
- Size カラム: インデックスが使用するストレージサイズ
- Disable Replication: レプリケーションを停止する

### スレーブ管理画面

![20171022_solr_slave2](https://user-images.githubusercontent.com/13412823/44092665-1aad1528-a00c-11e8-8f93-031b7ef45581.png)

- Next Run: 次のレプリケーション実行タイミングまでの秒数
- Iterations: レプリケーションが実行された日時と成否
- Index カラム:
	- Master (Searching): スレーブが参照しているマスターのインデックス
	- Slave (Searching): スレーブが検索で使用しているインデックス
- Replicate now: カウントダウンを待たず即時にレプリケーションを実行する
- Disable Polling: レプリケーション自体は有効なまま、スレーブ側で更新を一時停止する

コマンドラインからレプリケーションを実行したい場合は以下のようにする

```bash
$ curl -s "http://${SLAVE_HOST}:${PORT}/solr/${COLLECTION}/replication?command=fetchindex"
```


# 8.4 レガシーなクラスタ

分散インデックス・分散検索・レプリケーションを組み合わせて、マスター2台、スレーブ4台からなるレガシーなクラスタを構築する。
（略）

# 8.5 SolrCloud

- マスター/スレーブ構成には障害点が存在し、運用・管理コストが生じる
- **SolrCloud**: 単一障害点を極力なくし、運用・管理コストを最小化することを目的とする分散環境の仕組み
	- ZooKeeper を利用
	- 以下の機能を提供
		- ノードのステータス管理
		- 設定ファイルの中央集中管理
		- 分散インデクシング
		- レプリケーション
		- 自動フェイルオーバー
		- リーダー（マスター）ノードの自動選出

ここでは Web GUI を中心に操作を行うが、HTTP API も提供されている。
- Collections API
- ConfigSets API

## ZooKeeper のインストールと起動

Solr 設定ファイルや SolrCloud のクラス他情報を管理するコーディネーションサービスとして、ZooKeeper が必要。

ZooKeeper をダウンロード

```bash
$ wget http://ftp.riken.jp/net/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
$ tar -xf zookeeper-3.4.6.tar.gz
$ cd zookeeper-3.4.6
```

以下のような設定ファイル zoo.cfg を bin/conf に配置
```
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/tmp/zookeeper
clientPort=2181
```

ZooKeeper 起動

```bash
$ bin/zkServer.sh start
...
Starting zookeeper ... STARTED
```

## SolrCloud 構築

Solr に同梱されている zkcli.sh を使って znode を作成

```bash
$ ${SOLR}/server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:2181 -cmd makepath /solr
```

この znode に接続して SolrCloud 起動（4サーバ）

```bash
$ bin/solr start -h localhost -p 8983 -d ./server -z localhost:2181/solr -s ./server/solr_cloud01
$ bin/solr start -h localhost -p 8985 -d ./server -z localhost:2181/solr -s ./server/solr_cloud02
$ bin/solr start -h localhost -p 8987 -d ./server -z localhost:2181/solr -s ./server/solr_cloud03
$ bin/solr start -h localhost -p 8989 -d ./server -z localhost:2181/solr -s ./server/solr_cloud04
```

適当な設定ファイルのセット（managed-schema など）を ZooKeeper に登録

```bash
server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:2181/solr -cmd upconfig -confdir ${SOME_PATH}/conf -confname ${CONFIG_NAME}
```

![20171028_solrcloud_ui](https://user-images.githubusercontent.com/13412823/44092666-1af65d50-a00c-11e8-9fed-0b0cb7f3f115.png)

登録した設定ファイルを使って「Collections」>「Add Collection」から新しいコレクションを作成

→ これで検索・インデクシングができる状態になった。

![20171028_solrcloud_ui2](https://user-images.githubusercontent.com/13412823/44092667-1b1bafec-a00c-11e8-8d94-a79d45968c32.png)


## 分散インデクシングと分散検索、レプリケーション

- 分散インデクシング
	- レガシーなクラスタ：各ドキュメントをどのノードに置くかはユーザが制御する必要があった
	- SolrCloud：画像の「range」を見れば分かる通り、更新リクエストが送られたノードがどれかに関係なく、ユニークキーから計算したハッシュ値の値の範囲で自動的にどのシャードにデータを置くか制御する
- レプリケーション
	- レガシーなクラスタ：マスターでインデクシングされた最終出力であるインデックスファイルがスレーブにコピーされて差分更新
	- SolrCloud：ドキュメントを受け取ったリーダーはそのドキュメントをレプリカにも転送し、リーダー・レプリカはそれぞれ自身でインデクシングを行う
- サービス上の違い
	- リアルタイム性
		- レガシーなクラスタ：マスタのインデックスをスレーブに同期するまでにタイムラグが発生するため、リアルタイム性を求めにくい
		- SolrCloud：各ノードで並列にインデクシングを行うので即時に全レプリカに変更が反映され、ソフトコミットも利用可能
	- 可用性
		- SolrJ の`CloudSolrClient`を使えば、ZooKeeper にクラスタ情報を問い合わせて稼働中のノードに対して自動でドキュメントを送信でき、可用性の高いシステムを構築できる

![20171028_solrcloud_ui3](https://user-images.githubusercontent.com/13412823/44092668-1b423220-a00c-11e8-96ba-5f4f0fb737f1.png)

SolrCloud における分散インデクシングの流れ：

1. いずれかのノードが更新リクエストとともにドキュメントを受け取る
2. そこでハッシュ値を計算し、インデックス先のシャードを算出してそのシャードのリーダーにドキュメントを転送する
3. ドキュメントを受け取ったリーダーはドキュメントを自身のインデックスに登録し、同じシャードのレプリカへ同じドキュメントを転送する
4. リーダーからドキュメントを転送されたレプリカはそれを自身のインデックスに登録する


## フェールオーバー

SolrCloud は強力なフェイルオーバー機能を備える。

- 検索のフェイルオーバー
	- ノードがダウンしても、そのノードを迂回して検索が行われ、エラーが発生しない
- インデクシングのフェイルオーバー
	- ノードがダウンしている場合、そのレプリカへの転送は停止する

## インデックスのリカバリ

- レガシーなクラスタでは、ノードのダウン中にインデックスの更新があった場合、ノードの復帰後に**管理者によって**ノード間でインデックスの同期が必要
- SolrCloud では、ノードが復帰した際に自動でリカバリが行われる

インデックスのリカバリの段階：
1. トランザクションログのリプレイ
	- JVM がクラッシュしたときと同じく、起動時に自動でトランザクションログのリプレイを実行（スタンドアローンの場合と同様）
2. PeerSync
	- リーダーのトランザクションログと自身のトランザクションログを比較
	- リーダーとの差分が小さい場合は、リーダーから差分のトランザクションログをコピーしてリプレイを実行してリカバリ完了
3. インデックスのレプリケーション
	- PeerSync においてリーダーと自身の差分が大きい場合に実行
	- インデックスファイル自体のレプリケーションを行う

復帰ノードのステータスが Active になるのは、リカバリが完了した後。


## リーダーの選出

- レガシーなクラスタでは、マスターがダウンした場合クラスタの状態が不安定になり、早急に復帰させる必要がある
- SolrCloud では、リーダーがダウンした場合同じシャードのレプリカの中から1台が選出され自動的にリーダーに昇格する


## SolrCloud の拡張

検索トラフィックが増えて QPS を増やしたい場合などに、オンラインでレプリカを追加できる。

1. 以下のように新しく2つのノードを起動すると、管理画面の「Cloud」>「Tree」にて、"/live_nodes" にこれらのノードが追加される

```bash
$ bin/solr start -h localhost -p 8991 -d ./server -z localhost:2181/solr -s ./server/solr_cloud05
$ bin/solr start -h localhost -p 8993 -d ./server -z localhost:2181/solr -s ./server/solr_cloud06
```

2. その後、「Collections」で対象コレクションを選択し、追加したい Shard で「add replica」からレプリカを追加できる
3. レプリカを追加すると自動でインデックスのリカバリが開始される
