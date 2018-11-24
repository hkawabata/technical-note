---
title: 1. イントロダクション
---

# 1.1 Solr のインストール

```
# Solr をダウンロード・解凍
$ wget http://ftp.jaist.ac.jp/pub/apache/lucene/solr/6.3.0/solr-6.3.0.tgz
$ tar xvzf solr-6.3.0.tgz
```

# 1.2 Solr の起動・終了

## 起動
```bash
$ cd solr-6.3.0
$ bin/solr start -p 8983

Solr home directory /home/hkawabat/workspace/solr/solr-6.3.0 must contain a solr.xml file!
```
ホームディレクトリに solr.xml がない！と怒られるので、サンプルからコピー（Solr 6.4.1だと怒られなかった）。
```bash
$ cp example/exampledocs/solr.xml ./
$ bin/solr start -p 8983
Waiting up to 30 seconds to see Solr running on port 8983 [/]  
Started Solr server on port 8983 (pid=5988). Happy searching!
```
※ `-p`オプションはなくても可。

これで http://hostname:8983 から Solr の UI にアクセスできる。

## 終了
```bash
$ bin/solr stop
```

# 1.3 ドキュメントの登録・検索

## コアの作成
`mycore`というコアを作りたいとき
```bash
$ bin/solr create -c mycore

Setup new core instance directory:
/home/hkawabat/workspace/solr/solr-6.3.0/server/solr/mycore

Creating new core 'mycore' using command:
http://localhost:8983/solr/admin/cores?action=CREATE&name=mycore&instanceDir=mycore

{
  "responseHeader":{
    "status":0,
    "QTime":2977},
  "core":"mycore"}
```

## ドキュメントの登録
```bash
$ bin/post example/exampledocs/*.xml -c mycore
```

## ドキュメントの検索
UI コア名を選択し、"Query" から検索ができる。


# 1.4 Solr で日本語を扱う
"Analysis" の画面でトークナイズ・分析ができる。

## N-gram
1. "Field Value (index)" に文字列を入力
2. "Analysis Fieldname / FieldType" で text_cjk を選択
3. "Analyse Values" をクリック。

## 形態素解析
text_cjk の代わりに text_ja を選択する。


# 1.5 Solr のアーキテクチャ

![Alt text](https://user-images.githubusercontent.com/13412823/44068149-a6173138-9fb3-11e8-81ca-410009dbbb45.png)

## インターフェース層
外部とのやりとり。Solr クライアントから検索・更新リクエストを受け取り、処理結果をクライアントに返す。
Web(HTTP) か Java の API によるアクセスが可能。

## リクエストハンドラ

SolrCore へ渡される引数。複数種類あってプラガブルなイメージ？

## SolrCore
リクエストハンドラを使ってリクエストを実行
- 検索リクエストの場合
**サーチャ**を使用して**インデックス**を検索
- 更新リクエスト（文書の追加・更新・削除）の場合
**更新ハンドラ**を使ってインデックスを更新する。

## サーチャ
いくつかのキャッシュを内蔵する。

## キャッシュ
サーチャに内蔵され、頻繁に検索される検索語による検索結果や、絞り込み検索条件による検索結果を保存する。

## 更新ハンドラ

## インデックス

## レスポンスライタ
リクエストの処理結果を Solr クライアントに最適なフォーマット（JSON や XML）で返す。

## solrconfig.xml
Solr の構成を管理。
**Solr 起動時に一度読み込まれる**。
- リクエストハンドラやレスポンスライタの構成
- キャッシュの使用有無や大きさ
- その他様々な構成管理

## schema.xml → managed-schema (6.x から)
インデックスのスキーマ（インデックスを構成するフィールドやその型）を管理。
**Solr 起動時に一度読み込まれる**。


# 1.6 Solr ホームディレクトリ
ファイル参照の起点となるディレクトリ。以後、`$SOLR_HOME`と記述する。インストールディレクトリの`solr-6.3.0/`とは異なる。
以下の順で決定される：
1. JNDI から "java:comp/env/solr/home" で lookup し、オブジェクトがあればそれを String にキャストして採用
2. システムプロパティ`solr.solr.home`の値が設定されていればそれを採用
3. Solr の起動ディレクトリ直下の solr ディレクトリ

## ディレクトリ構成

```bash
$SOLR_HOME
├── configsets/
├── mycore/
├── README.txt
├── solr.xml
└── zoo.cfg
```

- solr.xml
solr の共通的な設定について記載するファイル。
- mycore（コア名）
コアの設定が格納されるディレクトリ。Solr は、`core.properties`を持つディレクトリをコアの設定ディレクトリと見なしてコアを起動する。

> core.properties の中に`name=collection1`と書くと、コア名は collection1 になる。
	→ 複数の別名ディレクトリの core.properties で同じ名前をつければ、1つの Solr インスタンスで複数のコアを起動できる。

```bash
mycore
├── conf/
├── core.properties
└── data/
```

