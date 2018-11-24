---
title: 5. 高度なインデクシング
---

# 5.1 バッチ処理

以下のように、add, delete, commit, optimize といった更新コマンドを組み合わせ、1回のリクエストでまとめて実行できる(xml ファイルについても同様)

```json
{
  "add": {
    "doc": {
      "フィールド名": "値",
      "フィールド名": ["複数の値1", "複数の値2", ...],
      ...
    },
    "オプション名": "値",
    "オプション名": "値",
    ...
  },
  "add": {
    ...
  },
  "commit": {},
  "delete": {"id": "book1"},
  "delete": {"query": "title:タイトル2"},
  "commit": {},
  "optimize": {}
}
```

# 5.2 インデクシング前処理

インデクシング前にデータの抽出・加工・フィルタリングなどの前処理を行いたい場合、UpdateRequestProcessor の仕組みを用いる。

## UpdateRequestProcessor の設定

solrconfig.xml に記述する。
`updateRequestProcessorChain`の仕組みを使い、複数の処理を記述できる

```xml
<updateRequestProcessorChain name="hoge">
	<!-- 内容が重複したドキュメントがないか調べ、二重登録を防ぐ -->
	<processor class="solr.processor.SignatureUpdateProcessorFactory">
		<bool name="enabled">true</bool>
		<str name="signatureField">id</str>
		<bool name="overwriteDupes">false</bool>
		<str name="fields">name,features,cat</str>
		<str name="signatureClass">solr.processor.Lookup3Signature</str>
	</processor>
	<!-- 更新リクエストをログに記録する -->
	<processor class="solr.LogUpdateProcessorFactory" />
	<!-- 実際に更新を行う（必須） -->
	<processor class="solr.RunUpdateProcessorFactory" />
</updateRequestProcessorChain>
```

これを適用するには、update リクエスト時に`update.chain`パラメータで使用するチェインの name を指定する

```bash
$ curl -H 'Content-type:text/json' --data-binary @hoge.json http://<hostname>:8983/solr/<core_name>/update?update.chain=hoge&commit=true
```

常時このチェインを有効にするには、solrconfig.xml に以下の設定を記述する

```xml
<requestHandler name="/update" class="solr.UpdateRequestHandler">
	<lst name="defaults">
		<str name="update.chain">hoge</str>
	</lst>
</requestHandler>
```

## RegexReplaceProcessorFactory

正規表現による文字列置換を行う。

以下は、`tel`,`zipCode`フィールドに "-" が含まれる場合に削除する例。

```xml
<!-- regex という名前でチェインを定義 -->
<updateRequestProcessorChain name="regex">
	<processor class="solr.processor.RegexReplaceProcessorFactory">
		<str name="fieldName">tel</str>
		<str name="fieldName">zipCode</str>
		<str name="pattern">-</str>
		<str name="replacement"></str>
		<!-- \や$などのメタ文字をリテラルとして扱うかどうか -->
		<bool name="literalReplacement">true</bool>
	</processor>
<updateRequestProcessorChain>

<!-- /update/regrep というパスに regex チェインを使うリクエストハンドラを設定 -->
<requestHandler name="/update/regrep" class="solr.UpdateRequestHandler">
	<lst name="default">
		<str name="update.chain">regex</str>
	</lst>
</requestHandler>
```

使用時：

```bash
$ curl -H 'Content-type:text/json' --data-binary @hoge.json http://<hostname>:8983/solr/<core_name>/update/regex?commit=true
```


## StatelessScriptUpdateProcessorFactory

JVM がサポートするスクリプト言語（JavaScript, JRuby など）を使用して任意のインデクシング前処理を行う。

以下は`${SOLR_HOME}/conf/hoge.js`を使うための設定。

```xml
<!-- script という名前でチェインを定義 -->
<updateRequestProcessorChain name="script">
	<processor class="solr.processor.StatelessScriptUpdateProcessorFactory">
		<str name="script">hoge.js</str>
	</processor>
<updateRequestProcessorChain>

<!-- /update/script というパスに script チェインを使うリクエストハンドラを設定 -->
<requestHandler name="/update/script" class="solr.UpdateRequestHandler">
	<lst name="default">
		<str name="update.chain">script</str>
	</lst>
</requestHandler>
```

hoge.js の内容（ドキュメントの add 時に title フィールドの長さを表すフィールドを追加する）：

```javascript
function processAdd(cmd) {
	doc = cmd.solrDoc; // org.apache.solr.common.SolrInputDocument
	title = doc.getFieldValue("title")
	doc.addField("titleLength", title.length)
}
function processDelete(cmd) {
	// no operation
}
function processMergeIndexes(cmd) {
	// no operation
}
function processCommit(cmd) {
	// no operation
}
function processRollback(cmd) {
	// no operation
}
function finish() {
	// no operation
}
```

使用時：

```bash
$ curl -H 'Content-type:text/json' --data-binary @hoge.json http://<hostname>:8983/solr/<core_name>/update/script?commit=true
```


## その他の UpdateRequestProcessor

他にも様々な機能を提供するものがある（詳細は省略）

- 自動で UUID を振る
- デフォルト値をセットする
- 複数の値を保つ場合にデリミタで結合する
- HTML タグを取り除く
- 両端をトリムする
- 指定した最大文字数を超える文字列を切り捨てる
- multiValued で値が重複する場合に取り除く
- etc...


# 5.3 データのインポート

`DataImportHandler`(DIH) を使い、RDB や RSS, XML ファイルなど外部のデータソースに格納されたデータをインポートしてインデクシングできる。
DIH は以下の3つからなる。
- `DataSource`: インポート元のデータベースや XML ファイル
- `Entity`: Solr ドキュメント群にマッピングされる概念的なデータの単位。RDB でいうとテーブルやビューなど
- `EntityProcessor`: Entity からドキュメントへのマッピングを行う

他、フィールド値の変換を行う`Transformer`も設定できる。

## 使用するための設定

- solrconfig.xml

```xml
<requestHandler name="/dataimport" class="apache.solr.handler.dataimport.DataImportHandler">
	<lst name="defaults">
		<str name="config">do-data-config.xml</str>
	</lst>
</requestHandler>
```

do-data-config.xml は DIH 設定ファイルで、任意の名前で良い

- DIH 設定ファイル

```xml
<dataConfig>
	<dataSource type="JdbcDataSource" ... />
	<document>
		<entity name="" processor="SqlEntityProcessor" transformer="">
			<field column="solr_schema_field1"/>
			...
			<entity name=""/>
		</entity>
	</document>
</dataConfig>
```

- entity 要素の下に entity 要素を...というように階層化できる


# 5.4 疑似リアルタイム検索

ドキュメントの更新が行われた場合に、それを即時検索結果に反映させること。

## ハードコミットとソフトコミット

- **ハードコミット**
	- ディスクへの同期・キャッシュのウォームアップを伴う
	- 負荷が高い
- **ソフトコミット**
	- メモリ上でのみコミット操作が行われる
	- 負荷がかからず、更新内容が即座に検索結果に反映される
	- JVM のクラッシュやサーバのハードウェア障害などが発生した場合にデータが失われるリスクが有る
	- 実行するには、リクエスト時に`softCommit=true`を指定する

## 自動ソフトコミット

solrconfig.xml に以下の設定をすれば、自動ソフトコミットを設定できる。

```xml
<updateHandler class="solr.DirectUpdateHandler2">
	...
	<autoSoftCommit>
		<!-- 1000件以上のドキュメントが追加されると自動でコミット -->
		<maxDocs>1000</maxDocs>
		<!-- 最後に追加されてから100ミリ秒以上経ったら自動でコミット -->
		<maxTime>100</maxTime>
	</autoSoftCommit>
	...
</updateHandler>
```


# 5.5 バイナリ形式のドキュメントのインデクシング

`ExtractingRequestHandler`を使うと、PDF や Microsoft Word などのバイナリファイルからメタデータやコンテンツを抽出してインデクシングを行える。
（詳細略）

# 5.6 インデックス作成時に関連する solrconfig.xml の設定

## indexConfig

`indexConfig`フィールドにてインデックス作成、チューニングの設定ができる

```xml
<config>
	<indexConfig>
	...
	</indexConfig>
</config>
```

| 要素 | デフォルト | 説明 |
| :-- | :-- | :-- |
| useCompoundFile | false | true にすると合成ファイルインデックスが用いられ、インデックスを構成するファイル数が少なくなってファイルディスクリプタの節約になる |
| ramBufferSizeMB | 100 | インデックス更新時、更新内容を一旦メモリにバッファするが、ここで指定した閾値を超えるとディスクにフラッシュされる |
| maxBufferedDocs | なし | ramBufferSizeMB と同様だが、データサイズではなくドキュメント数で指定する |
| mergePolicyFactory | TieredMergePolicyFactory | インデックスセグメントのマージポリシーを指定 |
| lockType | native | インデックス更新時のインデックスディレクトリのロック設定（native, simple, single から選択） |
| writeLockTimeout | 1000 | インデックスの書き込みロックが解かれるのを待つ最大時間 |
| deletionPolicy | SolrDeletionPolicy | ロールバックに備えてどの程度のコミットを保持しておくかの指定 |
| reopenReaders | true | true の場合、クローズしてからオープンという処理ではなく、より効率的なリオープン処理を利用してインデックスの再読み込みを行う |
| infoStream | なし | true の場合、インデックスファイルの処理に関するデバック情報を出力する。実際のログ出力先の設定などは log4j.properties で実施 |


## インデックスセグメントとマージポリシー

- Solr(Lucene) のインデックスは、内部的には**セグメント**（複数のバイナリファイルからなる）という単位で分割される
- **インデックスを更新してコミットするたびに新しいセグメントが作成され**、一度作成されたセグメントは変更されない
- セグメントが増えてくると検索性能が悪化するため、Solr は**自動で**多数の小さなセグメント群を少数の大きなセグメント群にマージする
- マージはコミットと同時に行われる
- いつ、どのような基準でマージを行うかのポリシーを設定できる
	- インデックス中の最大セグメント数を小さく設定：
		- 検索性能向上：見るべきセグメントが少なくて済むため
		- インデクシングスループット低下：頻繁にマージを行う負荷のため
	- インデックス中の最大セグメント数を大きく設定：
		- 小さく設定したときの逆
- マージによって検索性能は向上するが、頻繁にマージを行うとマージ自体の負荷でインデクシングのスループットが低下する


## オプティマイズ

- **オプティマイズ**：自動で行われるマージとは異なり、任意のタイミングで、指定のセグメント数になるまで強制的にマージを行う
- オプティマイズはコミットの実行を伴うため、未コミットの更新内容があった場合はインデックスに反映される

```bash
$ curl http://<hostname>:8983/solr/<core_name>/update?optimize=true
```

オプティマイズのオプション

| オプション | デフォルト | 説明 |
| :-- | :-- | :-- |
| waitSearcher | true | (commit と共通) true だと、新しいサーチャで検索が可能になるまで optimize を実行したクライアントに制御を戻さない |
| softCommit | false | (commit と共通) true だと、ソフトコミットを実行する |
| maxSegments | 1 | セグメント数がこの値に達するまで最適化を行う |

オプティマイズやマージの効果は、処理前後の`${SOLR}/server/solr/<core_name>/data/index/`の中身を見れば確認できる

```
$ ls server/solr/<core_name>/data/index/ -l
total 1032
drwxrwxr-x 2 hkawabata hkawabata   4096  7月 22 17:06 .
drwxrwxr-x 5 hkawabata hkawabata   4096  7月 16 18:47 ..
-rw-rw-r-- 1 hkawabata hkawabata 600223  7月 22 17:06 _2.fdt
-rw-rw-r-- 1 hkawabata hkawabata    230  7月 22 17:06 _2.fdx
-rw-rw-r-- 1 hkawabata hkawabata   1309  7月 22 17:06 _2.fnm
-rw-rw-r-- 1 hkawabata hkawabata   2259  7月 22 17:06 _2.nvd
-rw-rw-r-- 1 hkawabata hkawabata     88  7月 22 17:06 _2.nvm
-rw-rw-r-- 1 hkawabata hkawabata    500  7月 22 17:06 _2.si
-rw-rw-r-- 1 hkawabata hkawabata  73687  7月 22 17:06 _2_Lucene50_0.doc
-rw-rw-r-- 1 hkawabata hkawabata  70945  7月 22 17:06 _2_Lucene50_0.pos
-rw-rw-r-- 1 hkawabata hkawabata 113511  7月 22 17:06 _2_Lucene50_0.tim
-rw-rw-r-- 1 hkawabata hkawabata   2999  7月 22 17:06 _2_Lucene50_0.tip
-rw-rw-r-- 1 hkawabata hkawabata 150500  7月 22 17:06 _2_Lucene54_0.dvd
-rw-rw-r-- 1 hkawabata hkawabata   2400  7月 22 17:06 _2_Lucene54_0.dvm
-rw-rw-r-- 1 hkawabata hkawabata    165  7月 22 17:06 segments_4
```


# 5.7 トランザクションログ

- Solr ではインデックスとは別に、**トランザクションログ**という形で更新データを保存する
- インデックス更新時の挙動：
	1. update: トランザクションログを`${SOLR_DATA}/tlog/tlog.*`に書き込み
	2. commit or softCommit:
		- ソフトコミット：ヒープ上のインデックスに書き込み
		- （ハード）コミット：ファイルシステム上のインデックスに書き込み

## トランザクションログの設定

```xml
<config>
	<updateHandler class="solr.DirectUpdateHandler2">
		<updateLog>
			<str name="dir">${solr.ulog.dir:}</str>
			<int name="numRecordsToKeep">500</int>
			<int name="maxNumLogsToKeep">20</int>
			<int name="numVersionBuckets">65536</int>
		</updateLog>
	</updateHandler>
</config>
```

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| numRecordsToKeep | 100 | 1ログファイルに保持する更新レコードの数 |
| maxNumLogsToKeep | 10 | ログファイルの最大保持数 |
| numVersionBuckets | 65536 | 並べ替えられた更新をチェックする際、最大バージョンを追跡するために使用されるバケットの数。<br>これを大きくするとヒープの消費が増え（8バイト(long) x バケット数）、バージョンバケットへのアクセスを同期するコストが削減される |


## リアルタイム Get

- **インデックスの更新内容を検索可能にするには、サーチャを再生成して新しいインデックスをオープンする必要がある**
- **リアルタイム Get**：トランザクションログを用いて、新しいサーチャを生成せず、未コミットのものも含めて全てのインデックスを検索できる仕組み
	- インデクシング前なので、ユニークキー以外の値でドキュメントを取得することはできない
	- 指定されたユニークキーをトランザクションログ内から探し、見つかればそのドキュメントを返し、見つからなければユニークキーを使ってインデックス内を検索する
- リアルタイム Get には、Solr に暗黙的に存在する /get ハンドラを使用する

以下はデフォルトの設定：
```xml
<requestHandler name="/get" class="solr.RealTimeGetHandler">
	<lst name="defaults">
		<str name="omitHeader">true</str>
		<str name="wt">json</str>
		<str name="indent">true</str>
	</lst>
</requestHandler>
```

リアルタイム Get においても、fq パラメータによる検索結果のフィルタリングが可能


## インデックスのリカバリ

- ソフトコミットによってメモリ上のインデックスに存在したデータがハードウェア障害などによるプロセス異常終了で消失しても、トランザクションログにインデックス情報が残っている
- プロセス起動（復帰）時、自動でトランザクションログに残っているドキュメントのリプレイ（再読込）が行われ、**メモリ上ではなくファイルシステム上のインデックスに反映される**
