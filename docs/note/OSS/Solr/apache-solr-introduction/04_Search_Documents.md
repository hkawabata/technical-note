---
title: 4. ドキュメントの検索
---

# 4.1 検索の基本動作

## 検索の仕組み

- 検索リクエストを受け取った**サーチハンドラ**は、**サーチコンポーネント**という単位で絵リクエストを処理する。
- サーチコンポーネントの1つである **QueryComponent** において実際の検索処理が行われる。
- 検索結果は**レスポンスライタ**によって JSON や XML に整形され、クライアントに渡される。

## 検索リクエストとパラメータ

- http://{hostname}:8983/solr/#/{core}/query にアクセスすると、GUI を使って検索が実行できる。
- このとき発行された http リクエストの内容は、検索結果画面の上部に表示される。
http://{hostname}:8983/solr/{core}/{request_handler}?{param1}={value1}&{param2}={value2}&...

| パラメータ | 説明 | 備考 |
| :-- | :-- | :-- |
| Request-Handler (qt) |  |
| q | "{フィールド名}:{値}" の書式で実行するクエリ（**検索式**）を指定。AND, OR で複数つなぐこともできる |
| fq | 絞り込み検索。q パラメータで指定した検索式の実行結果に対し、AND 条件で検索式を追加・適用できる | q パラメータで AND を使っても同じ結果が得られるが、こちらを使ったほうが効果的（後述） |
| sort |  |
| start, rows | 検索結果のうち何番目から（start）何件（rows）表示するか。0番目が先頭 |
| fl | 検索結果に表示するフィールド。カンマ区切りで複数指定可能。何も指定しなければ、stored が true な全フィールドが返る（`*`を指定したときも同じ） | 他に、特殊なフィールド "score"（クエリに対してどれほど関連度が高いか）を指定することもできる |
| df |  |
| Raw Query Parameters |  |
| wt | write-type? json や xml, python などが指定できる |
| indent | 見やすく整形（改行・インデント）するかどうか | HTTP リクエストを送る際は on/off で指定 |
| debugQuery |  |
| dismax |  |
| edismax |  |
| hl | ハイライトの設定を行うかどうか |
| facet |  |
| spatial |  |
| spellcheck |  |


## サーチハンドラ

ドキュメントの追加/更新/削除や検索のリクエストを Solr 送る場合、リクエスト内容に応じた**リクエストハンドラ**を同時に指定する必要がある。
検索時に使われる**サーチハンドラ**の設定は、solrconfig.xml に記述されている。

ex.
```xml
<requestHandler name="/select" class="solr.SearchHandler">
    <lst name="defaults">
      <str name="echoParams">explicit</str>
      <int name="rows">10</int>
      <str name="fl">id,score</str>
    </lst>
    <lst name="appends">
        <str name="fl">title</str>
    </lst>
    <lst name="invariants">
        <int name="rows">3</int>
    </lst>
</requestHandler>
```

![20170828_solr001](https://user-images.githubusercontent.com/13412823/44068077-4d1342e8-9fb3-11e8-866a-a59231d961cd.png)
![20170828_solr002](https://user-images.githubusercontent.com/13412823/44068078-4d3bbdcc-9fb3-11e8-9496-56db775e6cf8.png)

| クエリパラメータ設定 | 説明 |
| :-- | :-- |
| default | リクエストパラメータが指定されなければここの値を使う |
| appends | リクエストパラメータにここの値を追加する |
| invariants | リクエストパラメータとしてここの値を必ず使う（ユーザがパラメータを指定しても無視される） |


## レスポンスライタ

- 検索結果を整形してクライアントに返すコンポーネント。レスポンスの書式は wt パラメータで指定できる。
- solrj を使ったアクセスの場合は javabin という特殊な wt が使用される。

# 4.2 検索レスポンス

```json
{
  "responseHeader": {
    "status": 0,
    "QTime": 0,
    "params": {
      "q": "title:Apache",
      "indent": "on",
      "fl": "title,isbn,score",
      "rows": "3",
      "wt": "json",
      "_": "1503854924731"
    }
  },
  "response": {
    "numFound": 5,
    "start": 0,
    "maxScore": 6.8303885,
    "docs": [
      {
        "isbn": "978-4-7741-8124-0",
        "title": "詳解 Apache Spark",
        "score": 6.8303885
      },
      {
        "isbn": "978-4-7741-4223-4",
        "title": "Apacheポケットリファレンス",
        "score": 6.8303885
      },
      {
        "isbn": "978-4-7741-5036-9",
        "title": "サーバ構築の実際がわかる　Apache［実践］運用／管理",
        "score": 4.97977
      }
    ]
  }
}
```

## ヘッダ情報

| キー名 | 説明 |
| :-- | :-- |
| status | 検索処理のステータス。正常な場合0 |
| QTime | 検索実行時間 [ms]（Solr サーバ側で処理にかかった時間） |
| params | 検索リクエストのパラメータ |

## 検索結果

| キー名 | 説明 |
| :-- | :-- |
| numFound | 検索にヒットしたドキュメント数 |
| start | 検索結果の取得開始位置。start パラメータで指定した値 |
| maxScore | 検索結果全体での最大スコア。fl パラメータで score を指定した場合のみ出力される |
| docs | 検索結果のドキュメント本体（のうち、fl で指定したフィールド） |


# 4.3 検索結果のソート

- sort パラメータを`fieldname asc`のように指定すれば、検索結果をソートできる
- 複数フィールドでソートしたい場合は`field1 asc,field2 desc,...`のように書く
- HTTP リクエスト：http://{hostname}:8983/solr/{core}/select?sort={field1}+desc,{field2}+asc
- ソート可能なフィールドの条件は、
	- multiValued = false
	- indexed = true
	- 非テキスト系フィールド型（数値・単語分割が必要ない文字列）

> **【メモ】**
> テキスト系フィールド型のフィールドでソートしようとすると、エラーにはならず結果が返ってきた。
> 調べてみると、「エラーにならないが正しくソートされない」といった感じらしい。


# 4.4 ハイライト

## ハイライトの基本動作

- Solr では以下をまとめて**ハイライト**と呼ぶ
	- 文書の要約（※言い換えや短縮ではなく、ヒットした文字列周辺の文書のこと）
	- 検索後の強調表示
- ハイライト機能は、検索文字列がドキュメントのどの部分にヒットしたのかを目立たせたいときに使う。

> **【メモ】**
> Solr GUI 上で目立たせる機能ではなく、ヒットした文字列を修飾する HTML タグなどを埋め込んだ文字列を返し、それをアプリケーション側で利用することを想定した機能。

## ハイライトの設定

1. hl パラメータを on にする
2. 以下のパラメータを使えるようになるので設定する

| パラメータ | 説明 |
| :-- | :-- |
| hl.fl | ハイライトを返させるフィールド |
| hl.simple.pre | 強調部分（検索語にマッチした部分）に付加する prefix |
| hl.simple.post | 強調部分（検索後にマッチした部分）に付加する suffix |
| hl.requireFieldMatch |  |
| hl.usePhraseHighlighter |  |
| hl.highlightMultiTerm |  |

hl=on を設定すると、ドキュメントのユニークキーを key、強調された要約文を value とする "highlighting" フィールドがレスポンスに追加される。

ex. 
`fl=pages&hl=on&hl.fl=title,summary&hl.simple.pre=<font color="red">&hl.simple.post=</font>`とした場合（fl パラメータに title, summary を指定する必要はない）。

```json
"response":{"numFound":7,"start":0,"docs":[
  {"pages":320},
  ...
},
"highlighting": {
  "http://gihyo.jp/book/2010/978-4-7741-4175-6": {
    "title": [
      "<font color=\"red\">Apache</font> Solr入門――オープンソース全文検索エンジン"
    ],
    "summary": [
      "<font color=\"red\">Apache</font> Solrとは，オープンソースの検索エンジンです。<font color=\"red\">Apache</font> LuceneというJavaの全文検索システムをベースに豊富な拡張性をもたせ，多くの開発者が利用できるように作ら"
    ]
  },
  ...
}      
```


# 4.5 絞り込み検索

- fq パラメータを用いる。q パラメータで指定した検索式に加え、別の検索式を適用してさらなる絞込が可能
- q パラメータ内で AND を使って複数の検索式を適用しても同じ結果が得られるが、fq を使う方が Solr のキャッシュを利用できるため高速


# 4.6 ファセット

## ファセットとは

- **ファセット**：検索結果をフィールドごとにグルーピングする仕組み
- ある検索クエリにヒットした本をジャンルごとに分類したい場合などに使える

> **【メモ】**
> - クライアントに返却される情報は「どのファセットのドキュメントが何件あったか」というカウント情報のみであり、各ドキュメントがどのファセットに属するかという情報は含まれない
> - よって、各ファセットのドキュメント一覧を取得するには、フロントアプリケーション側で再度、fq パラメータを使って絞り込み用の HTTP リクエストを発行する必要がある

## フィールドによるファセット

ex. `fl=pages&facet=on&facet.field=genre&facet.field=author`とした場合

```json
"response":{"numFound":7,"start":0,"docs":[
  {"pages":320},
  ...
},
"facet_counts":{
  "facet_queries": {},
  "facet_fields": {
    "genre": [
      "サーバ・インフラ・ネットワーク",4,
      "ネットワーク・UNIX・データベース",4,
      ...,
      "メール・インターネット",0,
      "自作・周辺機器・CD／DVD作成",0
    ],
    "author": [
      "大谷純",2,
      "株式会社ロンウイット",2,
      ...
      "フジイカクホ",0,
      "ボイスワーク",0
    ]
  },
  "facet_ranges": {},
  "facet_intervals": {},
  "facet_heatmaps": {}
}
```

※フィールド複数指定は GUI では行えない

## クエリによるファセット

ex. `fl=pages&facet=on&facet.query=pages:[0 TO 100]&facet.query=pages:[100 TO 200]&facet.query=pages:[200 TO 300]&facet.query=pages:[300 TO 400]`とした場合

```json
"response":{"numFound":7,"start":0,"docs":[
  {"pages":320},
  ...
},
"facet_counts":{
  "facet_queries": {
    "pages:[0 TO 100]": 0,
    "pages:[100 TO 200]": 1,
    "pages:[200 TO 300]": 1,
    "pages:[300 TO 400]": 5
  },
  "facet_fields": {},
  "facet_ranges": {},
  "facet_intervals": {},
  "facet_heatmaps": {}
}
```

## ファセットの仕組み

- ファセットの処理は、サーチコンポーネントの1つである **FacetComponent** として実装されている
- QueryComponent で得た検索結果と、ファセットの条件に合うドキュメントの集合との論理積を取って件数をカウントする
