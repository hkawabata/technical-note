---
title: 2. スキーマの設定
---

# 2.1 スキーマとは

Solr のインデックス構造のこと。検索速度にも密接に関わり、非常に重要。

# 2.2 スキーマ定義ファイル

## コアの作成

コア作成。

```bash
$ ${SOLR}/bin/solr start
$ ${SOLR}/bin/solr create_core -c solrbook -d basic_configs

Copying configuration to new core instance directory:
/home/hkawabata/workspace/solr/solr-6.3.0/server/solr/solrbook

Creating new core 'solrbook' using command:
http://localhost:8983/solr/admin/cores?action=CREATE&name=solrbook&instanceDir=solrbook

{
  "responseHeader":{
    "status":0,
    "QTime":2037},
"core":"solrbook"}
```

| オプション | 意味 |
| :-- | :-- |
| -c | コア名 |
| -d | 雛形とするコアディレクトリ（$SOLR_HOME/config にある`basic_configs`,`data_driven_schema_configs`,`sample_techproducts_configs`のうち1つを選ぶ） |

## managed-schema と schema.xml

- managed-schema と schema.xml の記述内容は同じ
- 編集
	- schema.xml はエディタによる手動書き換えのみを想定
	- managed-schema はそれに加えて **Schema API** から書き換えができる
- 設定の反映
	- schema.xml を書き換えた場合はコアのリロード or Solr の再起動が必要
	- Schema API を利用して managed-schema を書き換えた場合は自動で設定反映
- managed-schema と schema.xml は**必ずどちらか一方だけを使う**（schema.xml を使いたい場合は別途設定が必要）

## スキーマ定義ファイルの配置場所

`$SOLR_HOME/<core_name>/conf/`


# 2.3 スキーマ定義の流れ

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!-- スキーマ名とバージョン -->
<schema name="スキーマ名" version="1.5">

  <!-- 1.ユニークキーフィールドの設定 -->
  <uniqueKey>id</uniqueKey>

  <!-- 2.フィールドタイプの定義 -->
  <types>
    <fieldType name="タイプ名" class="クラス名" [オプション属性] />
    <fieldType name="test_ja" class="solr.TextField" autoGeneratePhraseQueries="false" positionIncrementGap="100">
      <analyzer>
	    <!-- アナライザの定義 -->
        <tokenizer class="solr.JapaneseTokenizerFactory" mode="search" />
        <filter class="solr.JapaneseBaseFormFilterFactory" />
        <filter class="solr.JapanesePartOfSpeechStopFilterFactory" tags="lang/stoptags_ja.txt" >
        ...
      </analyzer>
    </fieldType>
    ...
  </types>

  <!-- 3.フィールドの定義 -->
  <fields>
    <field name="フィールド名" type="タイプ名" [オプション属性] />
    <field name="author" type="text_ja" multiValued="false" indexed="true" required="false" stored="true" />
    ...
    <dynamicField name="random_*" type="random" />
  </fields>

  <!-- 4.コピーフィールドの設定 -->
  <copyField source="cat" dest="text"/>

  <!-- 5.Similarityの設定 -->
  <similarity>...</similarity>
  
</schema>
```

## スキーマ定義の有効化

Schema API を利用している場合は自動で反映されるため何もする必要がない。
schema.xml を利用しているときは以下のどちらかを行う。
- Solr 再起動：
```bash
$ ${SOLR}/bin/solr restart
```
- Solr コアのリロード：
```bash
$ curl "http://<hostname>:8983/solr/admin/cores?action=RELOAD&core=solrbook"
```

リロードは GUI でも行える。

# 2.4 フィールドタイプ

## フィールドタイプの定義

- Schema API

```bash
$ curl -X POST -H 'Content-type:application/json' --data-binary '{
  "{追加・更新・削除を指定するキー}": {
    "name": "{フィールドタイプの名前}",
    "class": "{フィールドタイプが使用するクラス名}",
    "{オプション名}": "{値}"
  },
  ...
}' http://<hostname>:8983/solr/<core_name>/schema
```

| キー | 説明 |
| :-- | :-- |
| add-field-type | 追加 |
| replace-field-type | 更新 |
| delete-field-type | 削除 |

直接 json を打ち込まず、テキストファイルにしておいて`--data-binary @hoge.json`とすることもできる。

- schema.xml

```
<fieldType name="タイプ名" class="クラス名" {オプション}={値} />
```

## 非テキスト系フィールドタイプ

**数値や、単語分割の必要がない文字列を扱う際のフィールドタイプの総称**。

以下の例は、`solr.StrFiled`という「分割が必要ない文字列」を扱うときに指定するクラス名に`string`というエイリアスをつけているようなイメージ。

```
"add-field-type": {
  "name": "string",
  "class": "solr.StrField"
}
```

```
<fieldType name="string" class="solr.StrField" />
```

## テキスト系フィールドタイプ

**文字列のフィルタリングや単語分割を行うフィールドタイプの総称**。

非テキスト系フィールドタイプで指定したものに加え、アナライザの設定をする必要がある。以下の例では、
1. charFilter で文字列全体を正規化
2. tokenizer で単語に分割
3. filter で単語1つ1つを正規化

といった処理を行っている

```
"add-field-type": {
  "name": "text",
  "class": "solr.TextField",
  "analyzer": {
    "charFilters": [
      {
        "class": "solr.MappingCharFilterFactory",
        "mapping": "mapping.txt"
      }
    ],
    "tokenizer": {
	  "class": "solr.StandardTokenizerFactory"
    },
    "filters": [
      {
        "class": "solr.StopFilterFactory",
        "ignoreCase": "true",
        "words": "stopwords.txt"
      }
    ]
  }
}
```

```xml
<fieldType name="string" class="solr.StrField">
  <analyzer>
    <charFilter class="solr.MappingCharFilterFactory" mapping="mapping.txt" />
    <tokenizer class="solr.StandardTokenizerFactory" />
    <filter class="solr.StopFilterFactory" ignoreCase="true" words="stopwords.txt" />
  </analyzer>
</fieldType>
```


## アナライザ

以下の一連の設定をアナライザと呼ぶ
1. **charFilter: 文字フィルタ**
1. **tokenizer: トークナイザ**
1. **filter: トークンフィルタ**

トークナイザやトークンフィルタを使わない設定もできるが、**適用順序は必ずこの順でなければならない**

### トークナイザ

- JapaneseTokenizerFactory
	- 形態素解析器 Kuromoji を利用したトークナイザ
	- 20万語を超える辞書を内包
	- 辞書に載っていない言葉はユーザ辞書を定義してカバー
- タームとトークン
	- **トークン**：トークナイザが出力する単語。文書内での位置のオフセットや他のトークンとの位置関係の情報も持つ
	- **ターム**：文字列情報だけを持つ単語。転置インデックスを参照するための単位


# 2.5 フィールドの定義

```bash
$ curl -X POST -H 'Content-type:application/json' --data-binary '{
  "{追加・更新・削除を指定するキー}": {
    "name": "{フィールドの名前}",
    "type": "{フィールドタイプの名}",
    "{オプション名}": "{値}"
  },
  ...
}' http://<hostname>:8983/solr/<core_name>/schema
```

| キー | 説明 |
| :-- | :-- |
| add-field | 追加 |
| replace-field | 更新 |
| delete-field | 削除 |

よく使うオプション：

| オプション | デフォルト | 説明 |
| :-- | :-- | :-- |
| indexed | true | 検索可能なフィールドにしたい場合は true |
| stored | true | オリジナルのテキスト情報をインデックスに保管したければ true（これを false にすると、形態素解析などでばらばらになったトークンだけが保存され、もとの文書は保存されない） |
| required | false | 必須フィールドにしたければ true |
| multiValued | false | 1つのフィールドに複数の値を保持したければ true |

> "score" というフィールドは予約されている特殊フィールドのため定義できない。

## ユニークキー
ドキュメントを一意に区別するフィールド。
- 6.3.0時点では Schema API で変更できず、デフォルトで定義されるユニークキー "id" を使うか managed-schema を直接編集して別のキーに変更する
- schema.xml では`<uniqueKey>id</uniqueKey>`のように定義する

# 2.6 Analysis 画面

登録されるドキュメントや検索されるクエリがどのようにトークナイズされるのか調べることができる
![Alt text](https://user-images.githubusercontent.com/13412823/44068076-4ceb78da-9fb3-11e8-8634-af81ede607b1.png)

- 下に向かってみていくと、各フィルタやトークナイザによって処理（半角・全角の変換や単語分割、単語の標準化など）が行われる過程が見られる
- 「Verbose Output」のチェックを外すと、各段階の単語分割の結果だけが簡易的に表示される
