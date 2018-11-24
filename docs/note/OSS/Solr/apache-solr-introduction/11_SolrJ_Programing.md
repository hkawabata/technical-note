---
title: 11. SolrJ プログラミング
---

# 11.1 SolrJ クライアントアプリケーション

- **SolrJ**
	- Solr と通信するための機能を Java クラスライブラリとして提供しているもの
	- 単体で動作するものではなく、サーバとリクエストをやり取りするためのもの

## ドキュメントの登録

### org.apache.solr.common.SolrInputDocument

Solr にドキュメントを登録するためのオブジェクト。

```java
SolrInputDocument doc = new SolrInputDocument();

String name = "field1";
String value = "value1";
float boost = 1.0f;

doc.addField(name, value, boost)
```


### org.apache.solr.client.solrj.SolrClient

- Solr と接続するためのクライアントクラス（抽象クラス）。
- これを実装した具象クラスを使って Solr とやりとりする。

### org.apache.solr.client.solrj.impl.HttpSolrClient

- SolrClient を実装した具象クラス
- スタンドアローンモードの Solr に接続する一般的なクライアントクラス

```java
String solrUrl = "http://my-solr-server:8983/solr/core1";
HttpSolrClient client = new HttpSolrClient.Builder(solrUrl).build();
```

### org.apache.solr.client.solrj.impl.LBHttpSolrClient

- SolrClient を実装した具象クラス
- ロードバランシングしながら複数のスタンドアローンモードの Solr に接続する
- 複数のスレーブにレプリケーションしているレガシーなクラスタを使う場合に有用

```java
List<String> solrUrls = new ArrayList<String>();
...
LBHttpSolrClient client = new LBHttpSolrClient.Builder().withBaseSolrUrls(solrUrls.toArray(new String[0])).build();
```


### org.apache.solr.client.solrj.impl.ConcurrentUpdateSolrClient

- SolrClient を実装した具象クラス
- Solr にドキュメントを送信することに特化し、大量のドキュメントをバッファリングしながら効率よく送信できる
- バッファキューのサイズや処理を行うスレッド数を指定できる

```java
ConcurrentUpdateSolrClient client = new ConcurrentUpdateSolrClient.Builder(solrUrl).withQueueSize(queueSize).withThreadCount(threadCount).build();
```


### org.apache.solr.client.solrj.impl.CloudSolrClient

- SolrClient を実装した具象クラス
- SolrCloud モードで起動する Solr クラスタに接続するためのクライアント
- Solr に直接接続するのではなく、SolrCloud を管理する ZooKeeper に接続してクラスタの情報を問い合わせ、リクエストを処理可能な Solr ノードにリクエストを送信する

```java
List<String> zookeeperHosts = new ArrayList<String>();
...

CloudSolrClient client = new CloudSolrClient.Builder().withZkHosts(zookeeperHosts).build();
client.setDefaultCollection(collectionName);
```

### org.apache.solr.client.solrj.response.UpdateResponse

- `SolrClient#add(SolrInputDocument)`でドキュメントを登録するときのレスポンスクラス

```java
UpdateResponse response = client.add(doc);
if (response.getStatus() == 0) {
    client.commit();
}
```

| メソッド | 取れる値 |
| :-- | :-- |
| getElapsedTime() | 経過時間 |
| getQTime() | 検索にかかった時間 |
| getRequestUrl() | リクエスト URL |
| getResponse() | レスポンス情報 |
| getResponseHeader() | レスポンスヘッダ情報 |
| getStatus() | ステータス情報 |

何かしらの例外が発生した場合、以下のようにして更新をキャンセルできる

```java
client.rollback();
```


## ドキュメントの検索

### org.apache.solr.client.solrj.SolrQuery

- このオブジェクトを使って Solr に送信するクエリを組み立てる

```java
SolrQuery query = new SolrQuery(queryString)

// 取得するドキュメントリストの開始位置と件数
query.setStart(start);
query.setRows(rows);

// ソート設定
query.setSort(sortField, Enum.valueOf(org.apache.solr.client.solrj.SolrQuery.ORDER.class, sortOrder));
```

### org.apache.solr.client.solrj.response.QueryResponse

- SolrQuery を送信して受け取るレスポンスクラス

```java
QueryResponse response = client.query(query);
```

### org.apache.solr.common.SolrDocumentList

- レスポンスから取得できるドキュメントリスト

```java
SolrDocumentList docList = response.getResults();
```

### org.apache.solr.common.SolrDocument

- 個別のドキュメント

```java
for (SolrDocument doc: docList) {
    Map<String, Object> docMap = new HashMap<String, Object>();
    for (String fieldName: doc.getFieldNames()) {
        docMap.put(fieldName, doc.getFieldValue(fieldName));
    }
    ...
}
```


## ドキュメントの削除

```java
UpdateResponse response = client.deleteById(id);
```


## インテグレーションテスト（結合テスト）

Solr では、テスト環境（サーバ）を用意に準備する機能（**solr-test-framework**）が提供されている。

```
<!-- https://mvnrepository.com/artifact/org.apache.solr/solr-test-framework -->
<dependency>
    <groupId>org.apache.solr</groupId>
    <artifactId>solr-test-framework</artifactId>
    <version>6.3.0</version>
    <scope>test</scope>
</dependency>
```

これを使えばサーバを別で立てなくてもテスト用の SolrCloud をテストコード内でセットアップできる。


