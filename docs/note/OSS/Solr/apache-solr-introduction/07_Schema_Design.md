---
title: 7. スキーマ設計
---

# 7.1 スキーマ定義ファイル

## スキーマ定義ファイルの配置場所と設定

managed-schema あるいは schema.xml は、通常はコアディレクトリは以下の conf/ に配置する。
スキーマ定義ファイルの格納場所は、schema.xml で設定できる。
以下はデフォルトの設定。
```xml
<schemaFactory class="ManagedIndexSchemaFactory">
	<!-- Schema API を使って編集可能にする場合は true にしておく -->
	<bool name="mutable">true</bool>
	<!-- スキーマ定義ファイル名 -->
	<str name="managedSchemaResourceName">managed-schema</str>
</schemaFactory>
```

従来の schema.xml を使う場合は以下のように設定する。

```xml
<schemaFactory class="ClassicIndexSchemaFactory" />
```

## スキーマ定義の構成要素

| 要素 | 定義の省略の可否 | Schema API での編集可否 |
| :-- | :-- | :-- |
| フィールドタイプ | x（必須） | o |
| フィールド | o | o |
| ダイナミックフィールド | o | o |
| ユニークキーフィールド | o | x |
| コピーフィールド | o | o |
| Similarity | o | 一部 o |

## スキーマレスモード

- スキーマにフィールドを定義しなくても検索・更新ができる仕組み
- インデクシング時にスキーマ定義に設定されていないフィールドが存在した場合、フィールド値からフィールドタイプを推測して自動的にフィールドが定義される
- 推測に際しては、フィールド値を Java のプリミティブ型のラッパークラスで解析し、パースできるフィールドタイプを単純に選択する
	- ex. true なら boolean, 1なら int
- 整数値と文字列が混在するようなフィールドの場合に意図してフィールドタイプにならない可能性があるため、推奨されない
- そのため、スキーマレスモードよりはダイナミックフィールドを利用するのが一般的


# 7.2 フィールドタイプ

## フィールドタイプの設定オプション

| オプション | デフォルト | 説明 |
| :-- | :-- | :-- |
| name | - | **必須**。フィールドの名称 |
| class | - | **必須**。フィールドタイプの実装クラス |
| indexed | true | 検索対象フィールドか否か |
| stored | true | フィールド値を保存するか否か |
| sortMissingLast | false | そのフィールドを使ってソートする際、フィールド値を持たないドキュメントを最後に持ってくる |
| sortMissingFirst | false | そのフィールドを使ってソートする際、フィールド値を持たないドキュメントを最初に持ってくる |
| multiValued | false | フィールドが複数の値を持つか |
| omitNorms | 非テキスト系は true<br>テキスト系は false | norm 値を保存するなら false |
| omitTermFreqAndPositions | 非テキスト系は true<br>テキスト系は false | tf 値とポジションを保存するなら false |
| omitPositions | false | true の場合、Position 情報は保存されないが、tf 値は保持する |
| positionIncrementGap | 0 | multiValued=true のフィールドにおいてフィールド値をまたがるフレーズ検索をする場合の調整パラメータ（整数） |
| postingsFormat | なし | フォーマット |
| required | false | フィールド値を持つことを必須とするか |
| termVectors<br>termPositions<br>termOffsets<br>termPayloads | false | termVectors / termPositions / termOffsets / termPayloads を保存するか |
| autoGeneratePhraseQueries | false | 自動でフレーズ検索を行うかどうか |
| docValues | 非テキスト系は true<br>テキスト系は false | ソートやファセット時、特定のフィールドの値だけを参照したいときに高速でサーチするための列指向フィールドを作成するかどうか（後述） |
| useDocValuesAsStored | false | docValues=true とした場合、stored=true が設定されていなくても検索結果にフィールド値を含めるかどうか |
| similarity | BM25 | フィールドタイプごとに similarity を指定する場合は設定する |

- sortMissingLast, sortMissingFirst
	- ともに false の場合、フィールド値を持たないドキュメントは昇順ソートなら最初、降順ソートなら最後に配置される
	- ともに true の場合、常に最後に配置される？（未確認。sortMissingLast が優先されるのか？）

- autoGeneratePhraseQueries
	- 検索時にトークナイズされたトークンを自動的にフレーズとして扱い、フレーズ検索を行う設定
	- ex. デフォルト検索式 OR で「検索エンジン」というキーワードで検索した時（「検索」「エンジン」とトークナイズされる）
		- autoGeneratePhraseQueries=false（デフォルト）：
			- 「検索」OR「エンジン」の検索
			- どちらかの単語を含んでいればヒット
		- autoGeneratePhraseQueries=true：
			- 「検索」の後に「エンジン」が出現するドキュメントを探すフレーズ検索
			- この順で（間になにも挟まず）両トークンが並んでいればヒット
- omitNorms
	- **norm 値**：ドキュメントと検索クエリの「近さ」をスコア化する際、「複数文書が同じキーワードにヒットしても文書が長い（単語数が多い）ほどスコアを低くする」といった調整を行うため、あらかじめ Solr が計算する値
	- omitNorms=true を設定すると norm 値が省略され、インデックスが小さくなり、検索時のメモリ消費量も抑えられる
- subFieldSuffix（point / location フィールドタイプ）
	- 内部で管理するサブフィールドに使用する suffix
	- point や location フィールドタイプは複数の値（ex. 経度・緯度）を持てるが、内部的にはそれらの値は別々のフィールドとして管理される
	- これらの内部的なフィールド管理用に suffix を定義する必要がある
- dimension（point フィールドタイプ）
	- 複数の値を保持するフィールドの次元数を指定する
	- location のような経度・緯度なら2、xyz 3次元座標をもたせるなら3を指定する
- docValues
	- ソートやファセット機能では、大量のドキュメントに対し、特定のフィールドの値だけを高速参照する必要がある
	- 通常のインデックス：
		- ドキュメント ID を第一のキーとして各フィールドの値を並べて持つ（**行指向**）
		- 特定フィールドしか必要がなくても全データをサーチする必要がある
		- この負荷を軽減するためフィールド値キャッシュが利用される
	- docValues=true が指定された時：
		- フィールドを第一のキーとして持ち、各ドキュメントの該当フィールドの値を並べて持つ（**列指向**）フィールドが作られ、インデックスの一部として管理される
		- 特定フィールドのみを高速でロードできるため、フィールド値キャッシュは利用されなくなる
		- インデックスファイルのサイズは増加するが、Java ヒープ領域の利用サイズを減らす効果がある
```json
# 通常のインデックス（行指向）
{
	"doc1": {"field1": 1, "field2": 2, "field3": 3},
	"doc2": {"field1": 4, "field2": 3, "field3": 6},
	"doc3": {"field1": 7, "field2": 2, "field3": 7},
	...
}

# docValues=true としたときに追加されるデータ形式（列指向）
{
	"field1": {"doc1": 1, "doc2": 4, "doc3": 7, ...},
	"field2": {"doc1": 2, "doc2": 3, "doc3": 2, ...},
	"field3": {"doc1": 3, "doc2": 6, "doc3": 7, ...},
}
```


## 非テキスト系フィールドタイプ

schema.xml の定義の書式については2章参照。

- 設定で任意のフィールドタイプ名をつけられるが、非テキスト系フィールドタイプでは慣習的に決まった名前が広く使用されているため、独自の名前をつけるのは推奨されない
- 以下は basic_configs をベースとしたスキーマに定義されているフィールドタイプの一覧

| フィールドタイプ名 | クラス | 説明 |
| :-- | :-- | :-- |
| string | solr.StrField | 文字列 |
| boolean | solr.BoolField | true / false |
| int | solr.TrieIntField | integer |
| long | solr.TrieLongField | long |
| float | solr.TrieFloatField | float |
| double | solr.TrieDoubleField | double |
| date | solr.TrieDateField | 日付（年月日時分秒ミリ秒） |
| binary | solr.BinaryField | 画像などのバイナリ |
| random | solr.RandomSortField | ランダムソートを行うフィールド |
| point | solr.PointType | 多次元の値の検索を行うフィールド |
| location | solr.LatLonType | 経度と緯度の検索を行うフィールド |
| location_rpt | solr.SpatialRecursivePrefixTreeFieldType | 経度と緯度の検索を行うフィールド |
| currency | solr.CurrencyField | レートを考慮した外貨計算を行うフィールド |

- 他にも以下のようなフィールドタイプクラスが用意されている

| クラス | 説明 |
| :-- | :-- |
| solr.UUIDField | ユニークな値を自動設定するフィールド |
| solr.CollectionField | Unicode に変換したソートや範囲検索を可能にするフィールド |
| solr.ICUCollationField | solr.CollationField と同様だが、ICU4J ライブラリを使用して高速化 |
| solr.EnumField | ユーザ定義された列挙値をフィールドに使用 |
| solr.PreAnalyzedField | すでにトークン化された内容をフィールドに使用 |


## テキスト系フィールドタイプ

schema.xml の定義の書式については2章参照。アナライザを内包する書式。
- テキスト系フィールドタイプでは、フィールドタイプ名の先頭に "text" をつける慣習がある

## アナライザ

以下のように1つだけアナライザを設定した場合、インデクシング時もクエリの際にも同じ設定が適用される。

```xml
<fieldType name="text_hoge" class="solr.TextField" positionIncrementGap="100" multiValued="true">
	<analyzer>...</analyzer>
</fieldType>
```

対して、以下のようにインデクシング時とクエリの際とで異なる設定を用いることもできる。

```xml
<fieldType name="text_hoge" class="solr.TextField" positionIncrementGap="100" multiValued="true">
	<analyzer type="index">...</analyzer>
	<analyzer type="query">...</analyzer>
</fieldType>
```

アナライザの設定では、文字フィルタ・トークナイザ・トークンフィルタをこの順序で記載する

- 文字フィルタ（charFilter）：省略可能、数の制限なし
- トークナイザ（tokenizer）：必須、1つだけ
- トークンフィルタ（filter）：省略可、数の制限なし

```xml
<analyzer>
	<charFilter>...</charFilter>
	<tokenizer>...</tokenizer>
	<filter>...</filter>
</analyzer>
```


## 文字フィルタ

できることの例：
- 特殊文字を置換する
- 日本語の半角・全角を一方に寄せる
- ドイツ語などのリガチャー（合字）を処理する


### MappingCharFilterFactory

指定されたマッピングファイルに基づき、文字単位で置換を行う
→検索時の表記ゆれ処理を文字単位で行える

```xml
<charFilter class="solr.MappingCharFilterFactory" mapping="lang/mapping-hoge.txt"/>
```

マッピングファイルの書式：

```
"ｻﾞ" => "ザ"
"①" => "1"
"壱" => "一"
...
```

マッピングは1行ずつ個別に動作するため、以下のように定義しても A は C にならない。

```
"A" => "B"
"B" => "C"
```

### ICUNormalizer2CharFilterFactory

Unicode 正規化にもとづき、半角英数字や機種依存文字を置き換える。
ex. 「㌔」→「キロ」

```xml
<charFilter class="solr.ICUNormalizer2CharFilterFactory"/>
```

### PatternReplaceCharFilterFactory

指定した正規表現にマッチする文字を置換する。
以下は、小文字アルファベット以外の文字を空文字に置き換える設定。

```xml
<charFilter class="solr.PatternReplaceCharFilterFactory" pattern="([^a-z])" replacement=""/>
```

### HTMLStringCharFilterFactory

テキストから HTML タグを取り除く。

```xml
<charFilter class="solr.HTMLStringCharFilterFactory"/>
```


## 代表的なトークナイザ

### JapaneseTokenizerFactory

形態素解析器「Kuromoij」を利用したトークナイザ。

オプション一覧：

| オプション | 値 | 説明 |
| :-- | :-- | :-- |
| mode | search, normal, extended | トークン分割モード。デフォルトは search |
| userDictionary | ユーザ辞書のファイル名 |  |
| userDictionaryEncoding | ユーザ辞書のエンコード | Java の CharSet クラスに対応。デフォルトは UTF-8 |
| discardPunctuation | true, false | 括弧などの特殊文字を残す場合は false。デフォルトは true |
| nBestCost<br>nBestExamples | 任意の数値<br>任意の例文 | N-best 機能を使用する場合の設定 |

mode による違い：
- normal
	- 辞書にある単語単位で分割
	- 「羽田空港に行く」→「羽田空港 / に / 行く」
- search
	- 辞書にある単語単位で分割し、更に辞書の単語を分割
	- 「羽田空港に行く」→「羽田 / 羽田空港 / 空港 / に / 行く」
- extended
	- search mode の内容に加え、辞書未登録の単語を一文字単位で分割
	- 「アキバに行く」→「ア / キ / バ / に / 行く」

```xml
<tokenizer class="solr.JapaneseTokenizerFactory" mode="search" userDictionary="lang/userdict_hoge.txt"/>
```

ユーザ辞書のフォーマット：`登録単語,登録単語を更に分割した場合の単語群（スペース区切り）,単語の読み（カタカナスペース区切り）,品詞名`

```
関西国際空港,関西 国際 空港,カンサイ コクサイ クウコウ,カスタム名詞
```

> **【注意】**ユーザ定義辞書を反映させるために必要なこと
> - Solr コアのリロード or 再起動
> - インデックスの再生成

### WhitespaceTokenizerFactory

英語のような、単語の間がホワイトスペースで区切られている言語に向くトークナイザ。

### StandardTokenizerFactory

- 連続した英数字やカタカナを1単語として切り出す
- ハイフンや句読点は除去（小数点のピリオドは例外）
- 英数字・カタカナ以外の全角文字は1文字単位で分割

ex.「本日, Solr-6.4がリリースされました」→「本日 / Solr / 6.4 / が / リリース / さ / れ / ま / し / た」


### NGramTokenizerFactory

日本語や中国語など、文章を構成する単語がスペースで区切られていない言語に向くトークナイザ。
機械的に指定した文字数で文書から文字列を切り出す。

ex. 「Solrは検索エンジンです」→「So / ol / lr / rは / は検 / 検索 / 索エ / エン / ンジ / ジン / ンで / です / す。」

```xml
<tokenizer class="solr.NGramTokenizerFactory" minGramSize="2" maxGramSize="2"/>
```


## 代表的なトークンフィルタ

### JapaneseBaseFormFilterFactory

動詞や形容詞など活用のある品詞を基本形に変換する。

### JapanesePartOfSpeechStopFilterFactory

単語の品詞情報によって単語のフィルタリングを行う（助詞を取り除く、など）。
基本的に品詞情報を付与してくれる JapaneseTokenizerFactory と組み合わせて使う。

```xml
<filter class="solr.JapanesePartOfSpeechStopFilterFactory" tags="lang/stoptags_hoge.txt"/>
```

### CJKWidthFilterFactory

全角と半角の文字を正規化する。
- 日本語の半角カタカナを全角に置換
- 全角英数字を半角に置換

### StopFilterFactory

テキストファイルに列挙した単語（ストップワード）を取り除くトークンフィルタ。
大文字小文字を区別しない場合は ignoreCase="true" を指定する。

```xml
<filter class="solr.StopFilterFactory" ignoreCase="true" words="lang/stopwords_hoge.txt"/>
```

### JapaneseKatakanaStemFilterFactory

カタカナ語末尾にある長音記号「ー」の表記ゆれを吸収する。
ex. 「フィルター」,「コンピューター」→「フィルタ」,「コンピュータ」

minimumLength オプションを指定しておくと、（末尾の「ー」を含めて）指定した文字数以上のカタカナ語のみにフィルタが適用される。
ex. minimumLength=4,「マザー」→「マザー」

```xml
<filter class="solr.JapaneseKatakanaStemFilterFactory" minimumLength="4"/>
```


### LowerCaseFilterFactory

ASCII 文字のトークンにおける大文字を全て小文字に変換する。
ex. 「Java」「JAVA」「java」→「java」「java」「java」


### SynonymFilterFactory

「首相」で検索したときに「内閣総理大臣」をヒットさせたいような場合に用いるトークンフィルタ。

```xml
<filter class="solr.SynonymFilterFactory" synonyms="lang/synonyms.txt" mode="normal" ignoreCase="true" expand="true" tokenizerFactory="solr.JapaneseTokenizerFactory" userDictionary="lang/userdict_hoge.txt"/>
```

シノニム辞書ファイルのフォーマット：
- 片方向：`検索語 => 同義語`
- 双方向：`同義語1,同義語2,同義語3,...`

```
トマト => 野菜
引っ越し,引越し,引越
```


# 7.3 フィールドの定義

フィールド定義の書式（schema.xml / managed-schema）：
```xml
<field name="id" type="string" indexed="true" stored="true" required="true"/>
```

| オプション | デフォルト | 説明 |
| :-- | :-- | :-- |
| name | - | **必須**。 |
| type | - | **必須**。 |
| default | - | デフォルト値 |
| indexed | true | 検索可能なフィールドにしたい場合は true |
| stored | true | オリジナルのテキスト情報をインデックスに保管したければ true<br>（これを false にすると、形態素解析などでばらばらになったトークンだけが保存され、もとの文書は保存されない：**検索結果として取得したりハイライトしたりできない**） |
| sortMissingLast | false | フィールド値を持たない場合のソート設定 |
| sortMissingFirst | false | フィールド値を持たない場合のソート設定 |
| multiValued | false | 1つのフィールドに複数の値を保持したければ true |
| omitNorms | 非テキスト系は true<br>テキスト系は false | norm 値を保存するなら false |
| omitTermFreqAndPositions | 非テキスト系は true<br>テキスト系は false | tf 値とポジションを保存するなら false |
| omitPositions | false | true の場合、Position 情報は保存されないが、tf 値は保持する |
| required | false | 必須フィールドにしたければ true |
| termVectors<br>termPositions<br>termOffsets<br>termPayloads | false | termVectors / termPositions / termOffsets / termPayloads を保存するか |
| docValues |  | 7.2節参照 |
| useDocValuesAsStored | true | 7.2節参照 |
| simularity | BM25 | フィールドタイプごとに similarity を指定する場合は設定する |

ユースケースと設定：

| ユースケース | indexed | stored | multiValued | omitNorms | termVectors | termPositions | docValues |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 検索対象フィールド | true |  |  |  |  |  |  |
| 内容を結果として取得するフィールド |  | true（※） |  |  |  |  | true（※） |
| ユニークキーとして使うフィールド | true |  | false |  |  |  |  |
| ソート用のフィールド | true |  | false | true |  |  | true |
| クエリブースト利用フィールド |  |  |  | false |  |  |  |
| ドキュメントブースト利用フィールド |  |  |  | false |  |  |  |
| ハイライトフィールド | true | true |  |  | true | true |  |
| ファセットフィールド | true |  |  |  |  |  | true |
| マルチバリューフィールド |  |  | true |  |  |  |  |
| データ長を考慮せずスコア計算するフィールド |  |  |  | true |  |  |  |
| MorLikeThis 検索フィールド |  |  |  |  | true |  |  |

※「内容を取得するフィールド」は、stored か docValues どちらかが true であれば良い


## ダイナミックフィールドの定義

**ダイナミックフィールド**：フィールド名とフィールドタイプの組み合わせを動的に決定できるフィールド

```xml
<dynamicField name="*_dt" type="data" indexed="true" stored="true"/>
```

`name="*_dt"`はフィールド名のルールで、ワイルドカード（*）が使える。
この例の場合、インデックスに登録するときや検索する時にフィールド名が _dt で終わっていたらこの設定を適用する。


## ユニークキーフィールドの定義

**ユニークキーフィールド**：Solr のドキュメントをユニークに決定するキーとなるフィールド

```xml
<fields>
	<field name="hoge" indexed="true" ... />
	...
</fields>
<uniqueKey>hoge</uniqueKey>
```


## コピーフィールドの定義

**コピーフィールド**：ドキュメントをインデックスに登録する際、指定したフィールドにフィールド値をコピーするよう Solr に指示する機能

```xml
<field name="title" type="string" indexed="true" stored="false"/>
<field name="text" type="string" indexed="true" stored="false"/>
...
<copyField source="title" dest="text" maxChars="100"/>
```

maxChars で文字数を制限して、ドキュメントの先頭部分だけを格納するフィールド（ニュース記事の先頭一部とか）を作ったりできるのがメリット...？？

複数のフィールドから同じフィールドへコピーを行っても良いが、その場合 dest にあたるフィールドは multiValued="true" である必要がある。


## その他のフィールドとオプション

### \_version\_ フィールド

内部管理用のフィールド。インデックスを作成するとき自動で管理番号が登録される。
ユーザが意識して値を登録することはない。

### \_root\_ フィールド

ネストされたドキュメントの親子関係を関連付けるフィールド。
ユーザが意識して値を登録することはない。

### random フィールド

ランダムソート専用のフィールドであり、ユーザが意識して値を登録することはない。

### default オプション

date タイプでは NOW が便利。
そのドキュメントの追加 or 更新時点のシステム時刻が設定される。

```xml
<field name="last_update" type="date" indexed="true" stored="true" default="NOW" />
```


# 7.4 Similarity の定義

**スコア**：ドキュメントとクエリの相関度合い
**Similarity**：スコアの計算方式

Similarity は Solr 5 以前は TF-IDF がデフォルトだったが、Solr 6 からは BM25 がデフォルトになった。
TF-IDF（= ClassicSimilarity）を使わせたい場合は以下のように設定する。

```xml
<fieldType name="hoge" class="solr.TextField" ...>
	<analyzer>...</analyzer>
	<similarity class="solr.ClassicSimilarityFactory"/>
</fieldType>
```
