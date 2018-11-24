---
title: 6. 高度な検索
---

# 6.1 クエリパーサ

- **クエリパーサ**：ユーザが入力したキーワード文字列を、Solr が解釈できる構造に変換する
- 使用するクエリパーサは defType パラメータで指定する

## Standard クエリパーサ

以下の検索式をサポート

- 単語検索（ex. `q=Apache&df=title`）
- フィールド指定検索（ex. `q=title:Apache`）
- 全文検索（`q=*:*`）
- 論理演算子・グループ化（ex. `q=検索式1 AND (検索式2 OR 検索式3 NOT 検索式4)`）
- 範囲検索（ex. `q=pages:[100 TO *]`, `q=genre:[C TO D]`）
- ワイルドカード検索（ex. `q=title:プログラ?`,`q=title:*ログラム`）
- 正規表現検索（`/`で囲った部分を正規表現として解釈。ex. `q=/[cm]ap/`）
- フレーズ検索（複数単語の出現順序を保証。ex. `q=title:"Apache Solr"`）
- あいまい検索（指定した編集距離（0-2）以内の単語に当たれば OK。ex. `q=title:プログラム~1`）
- 近傍検索（複数単語が指定した距離以内に近さにあれば OK。フレーズ検索と異なり、順序は指定不可。ex. `q=title:"Ruby プログラミング"~1`）
- 単語の重み付け（ex. `q=title:Apache^0.5 OR summary:Solr^2.0`）
- 定数スコア（ex. `q=title:Apache^=1.0 AND genre:パソコン`）


## DisMax クエリパーサ

- 複数フィールドを横断するクエリが書きやすい
	- 例：title または text に「Apache」「Solr」両方を含んでいてほしいとき
		- Standard クエリパーサでは`q=(title:Apache AND title:Solr) OR (text:Apache AND text:Solr)`
		- DisMax クエリパーサでは`q=Apache Solr&qf=title text&defType=dismax`
- Maximum Disjunction というスコア計算方式を使う
	1. （複数の）検索対象フィールドに対し、指定されたキーワードそれぞれでサブクエリを発行（Disjunction）
	2. 各サブクエリの最大値をキーワードのスコアとして採用（Maximum）
- Standard クエリパーサの場合、複数フィールドに同じキーワードが当たるとそのキーワードのスコアは合算される
- フィールドごとに異なる重みをかけられる

## Extended DisMax クエリパーサ

DisMax クエリパーサに加え、以下の機能をサポート

- Standard クエリパーサで利用可能な全ての構文
- 論理演算（AND, OR, NOT）
- 近傍検索によるブーストの改良
- 乗算によるスコアブースト

## ローカルパラメータ

**ローカルパラメータ**：`q={!key1=value1 key2=value2 ...}Apache`のようなパラメータ指定方式。

- defType は type というローカルパラメータで指定可能（`q={!type=dismax qf=title}Apache`）
- type は省略しても良い（`q={!dismax qf=title}Apache`）
- **v キー**という特殊なキーがあり、後続のクエリパラメータをローカルパラメータに含めることができる（`q={!dismax qf=title v=Apache}`）
- ローカルパラメータを変数にしておき、別のパラメータとしてローカルパラメータの外に出せる（`q={!dismax qf=title v=&qq}&qq=Apache`）


# 6.2 ハイライト

**ハイライト**：検索結果として表示されるドキュメントのどの部分が検索クエリにヒットしたのかを提示するための機能


```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?df=title&hl.fl=title&hl=on&indent=on&q=Apache%20AND%20Solr&wt=json"

{
	"responseHeader": {
		...
	}
	"response": {
		...
	}
	"highlighting":{
		"http://gihyo.jp/book/2010/978-4-7741-4175-6":{
			"title":["<em>Apache</em> <em>Solr</em>入門――オープンソース全文検索エンジン"]
		},
		"http://gihyo.jp/book/2014/978-4-7741-6163-1":{
			"title":["［改訂新版］<em>Apache</em> <em>Solr</em>入門――オープンソース全文検索エンジン"]
		}
	}
}
```

```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?df=title&hl.fl=title&hl=on&hl.simple.pre=<b>&hl.simple.post=</b>&indent=on&q=Apache%20AND%20Solr&wt=json"

{
	"responseHeader": {
		...
	}
	"response": {
		...
	}
	"highlighting":{
		"http://gihyo.jp/book/2010/978-4-7741-4175-6":{
			"title":["<b>Apache</b> <b>Solr</b>入門――オープンソース全文検索エンジン"]
		},
		"http://gihyo.jp/book/2014/978-4-7741-6163-1":{
			"title":["［改訂新版］<b>Apache</b> <b>Solr</b>入門――オープンソース全文検索エンジン"]
		}
	}
}
```

## ハイライタの種類

- Standard Highlighter: 標準のもの
- FastVector Highlighter, Posting Highlighter: インデックスに保存された文字や単語の場所の情報を利用し、効率よくハイライト対象となるスニペットを作成できる

## ハイライタの設定

solrconfig.xml に記述する（詳細略）
```xml
<config>
	<searchComponent class="solr.HighlightComponent" name="highlight">
		<highlighting>
			...
		</highlighting>
	</searchComponent>
</config>
```

## ハイライト用の検索パラメータ

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| hl | blank | true にするとハイライト機能を使う |
| hl.q | blank | 検索クエリではなくここに書いたクエリでハイライトする |
| hl.qparser | blank | hl.q に利用するクエリパーサ。なにも書かない場合 defType の値を使う |
| hl.fl | blank | ハイライト対象とするフィールド（カンマ区切り） |
| hl.snippets | 1 | 取得するスニペットの最大個数 |
| hl.fragsize | 100 | スニペット1つあたりの最大文字数 |
| hl.mergeContiguous | false | 隣接するスニペットを結合し、1つのスニペットとして返す |
| hl.requireFieldMatch | false | true にすると、ハイライト対象となるフィールドに対するクエリタームだけがハイライトされる。<br>ex. `q=title:検索 AND summary:Google&hl.fl=title`の場合、「検索」だけがハイライトされる |
| hl.maxAnalyzedChars | 51200 | スニペットを生成する際に処理対象となる最大文字数 |
| hl.maxMultiValuedToExamine | integer.MAX_VALUE | multiValued フィールドにおける最大参照エントリ数 |
| hl.maxMultiValuedToMatch | integer.MAX_VALUE | multiValued フィールドにおけるクエリタームの最大マッチ数 |
| hl.alternateField | blank | スニペットが取得できない場合に代わりに取得するフィールド名 |
| hl.maxAlternateFieldLength | unlimited | 上記の最大取得文字数 |
| hl.highlightAlternate | true | hl.alternateField が指定されている時、それをハイライトするかどうか |
| hl.formatter | simple | ハイライト文字列を生成するフォーマッター。simple のみ利用可能 |
| hl.simple.pre | `<em>` | ハイライトされる文字列の前に出力する文字列 |
| hl.simple.post | `</em>` | ハイライトされる文字列の後に出力する文字列 |
| hl.fragmenter | gap | フラグメンターの指定。regex も指定可能 |
| hl.usePhraseHighlighter | true | クエリにフレーズ検索が存在するときはフレーズだけをハイライト |
| hl.highlightMultiTerm | true | 範囲検索やワイルドカード検索のときもハイライト |
| hl.regex.slop | 0.6 | hl.fragmenter=regex の場合、hl.fragsize の値をどこまで厳密に守るかの割合。hl.fragsize に対して hl.regex.slop をかけた値がプラスマイナスで許容される |
| hl.regex.pattern | blank | フラグメント生成の正規表現 |
| hl.regex.maxAnalyzedChars | 10000 | regex フォーマッターを利用する場合に参照する最大文字数。大きなテキストフィールドに複雑な正規表現を適用した場合の負荷軽減策 |
| hl.preserveMulti | false | multiValued フィールドのテキストの保存順序を守るかどうか。false にすると、ハイライトの要求にマッチしたフラグメントとなる |
| hl.payloads | (automatic) | レアケースの負荷軽減策（略） |


# 6.3 ファセット

ファセット情報を取得するための機能は4つに分けられる。
いずれの機能を使う場合でも、`facet=true`パラメータを指定する。

## フィールド値によるファセット

指定したフィールドについて、インデクシングされている単語をもとにファセット情報を取得する。

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| facet.field |  | ファセット情報を生成する対象となるフィールド名 |
| facet.prefix |  | 指定した文字列から始まる単語のファセット情報のみを取得 |
| facet.contains |  | 指定した文字列を含む単語のファセット情報のみを取得 |
| facet.contains.ignoreCase |  | facet.contains を指定した場合に有効。大文字小文字を区別せずにマッチさせるかどうか |
| facet.sort |  | ファセット結果における並び順（count: カウント降順, index: 単語辞書順） |
| facet.limit | 100 | ファセットの最大取得数。ゼロより小さい値を指定した場合はすべて取得 |
| facet.offset | 0 | ファセットの取得を開始する位置。ファセット情報をページングして取得したい場合に使う |
| facet.mincount | 0 | 返却するファセット情報のカウントの最小値 |
| facet.missing | false | true にすると、通常のファセットに加えて、指定したフィールドの値を持たないドキュメントの数も出力される |
| facet.method | fc | ファセットの計算アルゴリズムの指定。enum, fc, fcs が選択できる |
| facet.exists | false | true の場合、ファセット情報の存在確認だけをして、カウントは1で固定される |

```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?q=*:*&facet=true&facet.field=genre&wt=json"
{
	"response":{
		...
	}
	"facet_counts":{
		...
		"facet_fields":{
			"genre":[
				"パソコン",639,
				"プログラミング・システム開発",339,
				"Excel",203,
				"サーバ・インフラ・ネットワーク",121,
				"ネットワーク・UNIX・データベース",121,
				"Word",115,
				"Windows",95,
				"JavaScript・Perl・Ruby・PHPなど",71,
				...
			]
		}
	}
}
```


## クエリによるファセット

任意のクエリを指定してファセット情報を取得する。

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| facet.query |  | ファセット情報を生成するクエリ。複数指定可能 |

```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?q=*:*&facet=true&facet.query=pages:\[0%20TO%20100\}&facet.query=pages:\[100%20TO%20200\}&facet.query=pages:\[200%20TO%20300\}&facet.query=pages:\[300%20TO%20*\}&wt=json"
{
	"response":{
		...
	}
	"facet_counts":{
		...
		"facet_queries":{
			"pages:[0 TO 100}":6,
			"pages:[100 TO 200}":322,
			"pages:[200 TO 300}":359,
			"pages:[300 TO *}":411
		},
		...
	}
}
```


## レンジファセット

日付型および数値型に特化して、範囲によるファセットを取得できる。

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| facet.range |  | **必須**。フィールド名 |
| facet.range.start |  | **必須**。レンジファセットの開始値 |
| facet.range.end |  | **必須**。レンジファセットの終了値 |
| facet.range.gap |  | **必須**。範囲を区切る間隔。日付型の場合は「+1MINUTE」などと指定できる |
| facet.range.hardend | false | facet.range.end を厳密に守るかどうか。false にしておくと facet.range.gap が優先され、end の値を超えることがある |
| facet range other | none | start から end までの範囲の**外**の範囲についてファセット除法を取得するためのパラメータ<br>・before: start 以前<br>・after: end 以降<br>・between: start と end の間の総合計<br>・none: 他の値は取得しない<br>・all: before, after, between 全てを取得 |
| facet.range.include |  | 範囲内の下限値・上限値の取り扱い（含める、含めない）を決める |

```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?&facet.range=pages&facet.range.start=0&facet.range.end=400&facet.range.gap=100&facet=on&indent=on&q=*:*&wt=json"
{
	"response":{
		...
	}
	"facet_counts":{
		...
		"facet_ranges":{
			"pages":{
				"counts":[
					"0",6,
					"100",322,
					"200",359,
					"300",251
				],
				"gap":100,
				"start":0,
				"end":400
			}
		},
		...
	}
}
```

## ピボットファセット

複数のフィールドを指定して階層的なファセットを取得

| パラメータ | デフォルト | 説明 |
| :-- | :-- | :-- |
| facet.pivot |  | ファセット情報を取得するフィールドをカンマ区切りで指定。親、子の順で指定する |
| facet.pivot.mincount | 1 | 返却するファセット情報のカウントの最小値 |

```
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?facet.pivot=genre,author,pages&facet=on&indent=on&q=*:*&wt=json"
{
	"response":{
		...
	}
	"facet_counts":{
		...
		"facet_pivot":{
			"genre,author,pages":[
				{
					"field":"genre",
					"value":"パソコン",
					"count":639,
					"pivot":[
						{
							"field":"author",
							"value":"技術評論社編集部",
							"count":117,
							"pivot":[
								{
									"field":"pages",
									"value":192,
									"count":39
								},
								...
							]
						},
						...
					]
				}
			]
		},
		...
	}
}
```


# 6.4 サーチコンポーネントとサーチハンドラ

- **サーチハンドラ**
	- クライアントからの検索リクエストを処理する
	- 複数のサーチコンポーネントが登録されている
- **サーチコンポーネント**
	- 通常の検索やハイライト、ファセット検索などもサーチコンポーネント
	- 互いに独立にリクエストを実行し、結果を JSON や XML として出力する

サーチコンポーネントの登録

```xml
<config>
	<searchComponent name="mycomponent" class="classname">
		...
	</searchComponent>
	<requestHandler name="/myhandler" class="solr.SearchHandler">
		<arr name="components">
			<str>mycomponent</str>
			<str>mycomponent2</str>
			...
		</arr>
	</requestHandler>
</config>
```

requestHandler タグでつけた name 属性を使い、`http://${HOSTNAME}:8983/solr/${COLLECTION}/<handler_name>`のようにしてリクエストハンドラにアクセスできる

## 検索キーワードのサジェスト

`solr.SuggestComponent`を使うと、検索キーワードのサジェスト（入力補完）機能を実現できる。

## 統計情報の表示

`solr.StatsComponent`を使うと、検索結果のドキュメントの集合について、最大値や最小値、平均値、標準偏差などの統計情報を検索結果に付与できる


# 6.5 Result Grouping と Collapse and Expand

検索結果を条件に従ってまとめる方法。

## Result Grouping

**グルーピング検索**ともいう。指定されたフィールドにおいて同じ値を持つものをまとめて表示する。

フィールド（group.field）によるグルーピング：

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=title:Apache&fl=title&wt=json&group=true&group.field=price&group.limit=100"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":1,
    "params":{
      "q":"title:Apache",
      "indent":"on",
      "fl":"title",
      "group.limit":"100",
      "wt":"json",
      "group.field":"price",
      "group":"true"}},
  "grouped":{
    "price":{
      "matches":5,
      "groups":[{
          "groupValue":3600,
          "doclist":{"numFound":3,"start":0,"docs":[
              {
                "title":"詳解 Apache Spark"},
              {
                "title":"Apache Solr入門――オープンソース全文検索エンジン"},
              {
                "title":"［改訂新版］Apache Solr入門――オープンソース全文検索エンジン"}]
          }},
        {
          "groupValue":2480,
          "doclist":{"numFound":1,"start":0,"docs":[
              {
                "title":"Apacheポケットリファレンス"}]
          }},
        {
          "groupValue":2980,
          "doclist":{"numFound":1,"start":0,"docs":[
              {
                "title":"サーバ構築の実際がわかる　Apache［実践］運用／管理"}]
          }}]}}}
```

クエリ（group.query）によるグルーピング：

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=*:*&fl=title,price&wt=json&group=true&group.query=price:\[0%20TO%202000\]&group.query=price:\{2000%20TO%203000\]&group.query=price:\{3000%20TO%204000\]&group.query=price:\{4000%20TO%20*\]&group.limit=2"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":6,
    "params":{
      "q":"*:*",
      "indent":"on",
      "fl":"title,price",
      "group.limit":"2",
      "group.query":["price:[0 TO 2000]",
        "price:{2000 TO 3000]",
        "price:{3000 TO 4000]",
        "price:{4000 TO *]"],
      "wt":"json",
      "group":"true"}},
  "grouped":{
    "price:[0 TO 2000]":{
      "matches":1100,
      "doclist":{"numFound":685,"start":0,"docs":[
          {
            "price":1780,
            "title":"Excelで作る　定型書類・ビジネス文書　匠の技100"},
          {
            "price":1880,
            "title":"30レッスンでしっかりマスター　Excel 2013 ［応用］ラーニングテキスト"}]
      }},
    "price:{2000 TO 3000]":{
      "matches":1100,
      "doclist":{"numFound":330,"start":0,"docs":[
          {
            "price":2880,
            "title":"自動計測システムのための Visual Basic 2005入門"},
          {
            "price":2280,
            "title":"もう迷わない！ Wordで作る長文ドキュメント【2007/2003/2002対応】"}]
      }},
    "price:{3000 TO 4000]":{
      "matches":1100,
      "doclist":{"numFound":78,"start":0,"docs":[
          {
            "price":3200,
            "title":"jQuery Mobile本格入門　～スマートフォンのデザイン・開発の効率化からWebアプリケーション構築まで"},
          {
            "price":3200,
            "title":"Nagios統合監視［実践］リファレンス"}]
      }},
    "price:{4000 TO *]":{
      "matches":1100,
      "doclist":{"numFound":5,"start":0,"docs":[
          {
            "price":4300,
            "title":"［改訂新版］パーフェクトC#"},
          {
            "price":4800,
            "title":"WebSphere Application Server構築・運用バイブル【WAS8.5／8.0／7.0対応】"}]
      }}}}
```


## Collapse and Expand

- Collapse と Expand
	- **Collapse**: 検索結果内のドキュメントをまとめて表示する機能で、`CollapsingQParser`というクエリパーサによって実現される
	- **Expand**: Collapse によってグルーピングされたドキュメントにアクセスするコンポーネント
- Collapse と Result Grouping とでは実装が異なるため、フォーマット・パフォーマンスに違いがある
	- `CollapsingQParser`はポストフィルタであり、検索結果のドキュメントセットに多くのグループが存在する場合に良いパフォーマンスを発揮する
	- これは、結果セットのドキュメントのグルーピングをまず行い、その結果をそれ以降のサーチコンポーネントに渡すので、ファセットやハイライトなどが Collapse されたドキュメントセットに対して実行されるため

price による Collapse:

各 price ごとに代表ドキュメントが表示されている。

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?"'indent=on&q=*:*&fl=title,pages,price&wt=json&fq=\{!collapse%20field=price%20max=pages\}'
```
※途中からシングルクオートに変更しているのは、`!`がダブルクオート中では展開されてしまって使えないため（エスケープしてもダメ）
```json
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "indent":"on",
      "fl":"title,pages,price",
      "fq":"{!collapse field=price max=pages}",
      "wt":"json"}},
  "response":{"numFound":64,"start":0,"docs":[
      {
        "pages":192,
        "price":762,
        "title":"今すぐ使えるかんたんmini Excel 2010 基本技"},
      {
        "pages":224,
        "price":980,
        "title":"今すぐ使えるかんたんmini　Excelグラフ 基本＆便利技［Excel 2016/2013/2010対応版］"},
      {
        "pages":192,
        "price":857,
        "title":"今すぐ使えるかんたんmini　Excel マクロ＆VBA 基本技"},
      {
        "pages":480,
        "price":3880,
        "title":"ネットワークエンジニアのための ヤマハルーター実践ガイド"},
      {
        "pages":192,
        "price":1080,
        "title":"Excel 2007 仕事で役立つ超便利【関数】技1"},
      {
        "pages":256,
        "price":680,
        "title":"今すぐ使えるかんたん文庫　エクセル文書作成　あっ！と驚く快速ワザ"},
      {
        "pages":320,
        "price":1429,
        "title":"今すぐ使えるかんたん パソコンの困った！を今すぐ解決する本［Windows 7対応］"},
      {
        "pages":624,
        "price":2880,
        "title":"オンラインゲームを支える技術 ―壮大なプレイ空間の舞台裏"},
      {
        "pages":352,
        "price":1380,
        "title":"今すぐ使えるかんたんPLUS+　Excel関数　組み合わせ　完全大事典"},
      {
        "pages":392,
        "price":2770,
        "title":"Chef実践入門――コードによるインフラ構成の自動化"}]
  }}
```

expand によるグループドキュメントの表示:

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?"'indent=on&q=*:*&fl=title,pages,price&wt=json&fq=\{!collapse%20field=price%20max=pages\}&expand=true'
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "expand":"true",
      "indent":"on",
      "fl":"title,pages,price",
      "fq":"{!collapse field=price max=pages}",
      "wt":"json"}},
  "response":{"numFound":64,"start":0,"docs":[
      {
        "pages":192,
        "price":762,
        "title":"今すぐ使えるかんたんmini Excel 2010 基本技"},
      {
        "pages":224,
        "price":980,
        "title":"今すぐ使えるかんたんmini　Excelグラフ 基本＆便利技［Excel 2016/2013/2010対応版］"},
      {
        "pages":192,
        "price":857,
        "title":"今すぐ使えるかんたんmini　Excel マクロ＆VBA 基本技"},
      {
        "pages":480,
        "price":3880,
        "title":"ネットワークエンジニアのための ヤマハルーター実践ガイド"},
      {
        "pages":192,
        "price":1080,
        "title":"Excel 2007 仕事で役立つ超便利【関数】技1"},
      {
        "pages":256,
        "price":680,
        "title":"今すぐ使えるかんたん文庫　エクセル文書作成　あっ！と驚く快速ワザ"},
      {
        "pages":320,
        "price":1429,
        "title":"今すぐ使えるかんたん パソコンの困った！を今すぐ解決する本［Windows 7対応］"},
      {
        "pages":624,
        "price":2880,
        "title":"オンラインゲームを支える技術 ―壮大なプレイ空間の舞台裏"},
      {
        "pages":352,
        "price":1380,
        "title":"今すぐ使えるかんたんPLUS+　Excel関数　組み合わせ　完全大事典"},
      {
        "pages":392,
        "price":2770,
        "title":"Chef実践入門――コードによるインフラ構成の自動化"}]
  },
  "expanded":{
    "1429":{"numFound":5,"start":0,"docs":[
        {
          "pages":320,
          "price":1429,
          "title":"［改訂新版］今すぐ使えるかんたんWord2007の困った！を今すぐ解決する本"},
        {
          "pages":320,
          "price":1429,
          "title":"今すぐ使えるかんたん Excel 2007の困った! を今すぐ解決する本"},
        {
          "pages":224,
          "price":1429,
          "title":"今すぐ使えるかんたん メール＆インターネットの困った！ を今すぐ解決する本"},
        {
          "pages":224,
          "price":1429,
          "title":"今すぐ使えるかんたん メール＆インターネットの困った！を今すぐ解決する本［Windows 7対応］"},
        {
          "pages":320,
          "price":1429,
          "title":"今すぐ使えるかんたん　Word 2007の困った！を今すぐ解決する本"}]
    },
    "857":{"numFound":26,"start":0,"docs":[
        {
          "pages":192,
          "price":857,
          "title":"今すぐ使えるかんたんmini Word 2013厳選便利技"},
        {
          "pages":192,
          "price":857,
          "title":"今すぐ使えるかんたんmini Windows Vista 基本技"},
        {
          "pages":192,
          "price":857,
          "title":"今すぐ使えるかんたんmini Access 2002/2003基本技"},
        {
          "pages":160,
          "price":857,
          "title":"今すぐ使えるかんたんmini　USBメモリー　徹底活用技"},
        {
          "pages":192,
          "price":857,
          "title":"今すぐ使えるかんたんmini Excel 2013 厳選便利技"}]
    },
    ...
    }}}
```


# 6.6 空間検索

## 空間検索とは

- 地図などの空間的な位置情報を使って検索するための機能
- 各ドキュメントが経度・緯度を保持する場合にそれを利用する
	- ex. 指定した座標から半径500 m以内の店舗（= ドキュメント）一覧を取得し、近い順に並べる
- 提供する機能
	- 　バウンディングボックスや円などの形状による検索及びフィルタリング
	- 緯度/経度などの地点と、検索するときの形状情報のインデクシング
	- 地点間や矩形間の距離によるソートやブースト

空間検索では以下のフィールドタイプが利用できる

| フィールドタイプ | 説明 |
| :-- | :-- |
| LatLonType<br>PointType | 緯度/経度などの地点情報 |
| SpatialRecursivePrefixTreeFieldType (RPT)<br>RptWithGeometrySpatialField (RPT 派生型) | 緯度/けいどなどの地点情報<br>マルチバリューをサポート |
| BBoxField | バウンディングボックスの情報を保持 |


## フィールド定義とインデックス

```xml
<schema>
	<fieldType name="location" class="solr.LatLonType" subFieldSuffix="_coordinate"/>
	<fields>
		<field name="geo_p" type="location" indexed="true" stored="true" />
		<dynamicField name="*_coordinate" type="tdouble" indexed="true" stored="false" />
	</fields>
</schema>
```

LatLonType フィールドへのインデックス時には、緯度・経度の順で debree 単位、カンマ区切りで指定する。

```xml
<doc>
	<field name="id">id001</field>
	<field name="geo_p">35.5,139.25</field>
</doc>
```

検索クエリには、以下の二種類のローカルパラメータを利用する
- `{!geofilt}`: 半径で検索
- `{!bbox}`: 矩形で検索

ローカルパラメータと同時に使えるパラメータ：

| パラメータ | 説明 |
| :-- | :-- |
| d | 中心からの km 単位の距離（bbox の場合は 2d x 2d の矩形内） |
| pt | 空間検索の起点となる中心点。LatLonType フィールドと同じ書式で指定 |
| sfield | 経度・緯度が設定されているフィールド名 |
| score | RPT と BBox フィールドタイプだけに利用でき、スコア生成のロジックを指定する |
| filter | RPT と BBox フィールドタイプだけに利用でき、false にするとフィルタではなく q パラメータによるメインクエリでのスコアだけを利用する |

パラメータ指定の例：
- geofilt: `q=shop_type:コンビニ&fq={!geofilt sfield=geo_p}&pt=35.12345,139.98765&d=1`
- bbox: `q=shop_type:コンビニ&fq={!bbox sfield=geo_p}&pt=35.12345,139.98765&d=1`


# 6.7 ファンクションクエリ

## ファンクションクエリとは

- フィールドの値を検索結果のスコアに反映させる際に利用できるクエリ
- 距離が近いデータや人気があるデータ、日付の新しいデータを優先したいときなどに使える
- 主なファンクション
	- 数学関数（四則演算・log・べき・最大最小）
	- 論理演算
	- 時刻の差分
	- フィールドに値が存在するかどうか
	- フィールドに指定した単語を含むドキュメント数
	- 条件分岐（if）
	- etc...
- ファンクションの利用方法
	- ファンクションの実行結果をフィールドとして取得
	- クエリパーサのパラメータとして利用し、結果をスコアに反映
	- ソート条件に利用

## ファンクションの実行結果をフィールドとして取得

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=*:*&fl=title,price,if(gt(price,2000),\"high\",\"low\")&wt=json"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "indent":"on",
      "fl":"title,price,if(gt(price,2000),\"high\",\"low\")",
      "wt":"json"}},
  "response":{"numFound":1100,"start":0,"docs":[
      {
        "price":2880,
        "title":"自動計測システムのための Visual Basic 2005入門",
        "if(gt(price,2000),\"high\",\"low\")":"high"},
      {
        "price":1780,
        "title":"Excelで作る　定型書類・ビジネス文書　匠の技100",
        "if(gt(price,2000),\"high\",\"low\")":"low"},
      {
        "price":1880,
        "title":"30レッスンでしっかりマスター　Excel 2013 ［応用］ラーニングテキスト",
        "if(gt(price,2000),\"high\",\"low\")":"low"},
      {
        "price":2280,
        "title":"もう迷わない！ Wordで作る長文ドキュメント【2007/2003/2002対応】",
        "if(gt(price,2000),\"high\",\"low\")":"high"},
      ...
      {
        "price":1880,
        "title":"Web開発の基礎徹底攻略",
        "if(gt(price,2000),\"high\",\"low\")":"low"}]
  }}
```

## クエリパーサのパラメータとして利用し、結果をスコアに反映

DisMax, eDisMax クエリパーサが持つ bf パラメータ（スコアのブーストに使うフィールド）にもファンクションクエリが使える。

まず、ファンクションクエリなしの場合：

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=*:*&fl=title,pages,score&wt=json&defType=edismax&bf=pages"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"*:*",
      "defType":"edismax",
      "bf":"pages",
      "indent":"on",
      "fl":"title,pages,score",
      "wt":"json"}},
  "response":{"numFound":1100,"start":0,"maxScore":849.0,"docs":[
      {
        "pages":848,
        "title":"［標準］ C言語重要用語解説 ＜ANSI C／ISO C99対応＞",
        "score":849.0},
      ...
      {
        "pages":752,
        "title":"知りたい操作がすぐわかる Word 2010 全機能Bible",
        "score":753.0}]
  }}
```

通常の検索スコアに pages の値がそのまま加算されている。

次にファンクションクエリを使う場合：

```bash
curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=*:*&fl=title,pages,score&wt=json&defType=edismax&bf=log(pages)"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":5,
    "params":{
      "q":"*:*",
      "defType":"edismax",
      "bf":"log(pages)",
      "indent":"on",
      "fl":"title,pages,score",
      "wt":"json"}},
  "response":{"numFound":1100,"start":0,"maxScore":3.9283957,"docs":[
      {
        "pages":848,
        "title":"［標準］ C言語重要用語解説 ＜ANSI C／ISO C99対応＞",
        "score":3.9283957},
      ...
      {
        "pages":752,
        "title":"知りたい操作がすぐわかる Word 2010 全機能Bible",
        "score":3.8762178}]
  }}
```


## ソート条件に利用

```bash
$ curl "http://${HOSTNAME}:8983/solr/${COLLECTION}/select?indent=on&q=*:*&fl=title,pages,price,sum(price,product(pages,2)),score&wt=json&defType=edismax&bf=log(pages)&sort=sum(price,product(pages,2))%20desc"
```

```json
{
  "responseHeader":{
    "status":0,
    "QTime":3,
    "params":{
      "q":"*:*",
      "defType":"edismax",
      "bf":"log(pages)",
      "indent":"on",
      "fl":"title,pages,price,sum(price,product(pages,2)),score",
      "sort":"sum(price,product(pages,2)) desc",
      "wt":"json"}},
  "response":{"numFound":1100,"start":0,"maxScore":3.9283957,"docs":[
      {
        "pages":656,
        "price":5200,
        "title":"Junos設定＆管理  完全Bible",
        "sum(price,product(pages,2))":6512.0,
        "score":3.8169038},
      {
        "pages":712,
        "price":4800,
        "title":"WebSphere Application Server構築・運用バイブル【WAS8.5／8.0／7.0対応】",
        "sum(price,product(pages,2))":6224.0,
        "score":3.85248},
      {
        "pages":800,
        "price":4300,
        "title":"［改訂新版］パーフェクトC#",
        "sum(price,product(pages,2))":5900.0,
        "score":3.90309},
      {
        "pages":528,
        "price":4800,
        "title":"Palo Alto Networks 構築実践ガイド　次世代ファイアウォールの機能を徹底活用",
        "sum(price,product(pages,2))":5856.0,
        "score":3.7226338},
      {
        "pages":592,
        "price":4200,
        "title":"Objective-C　プログラマーズバイブル",
        "sum(price,product(pages,2))":5384.0,
        "score":3.7723217},
      {
        "pages":704,
        "price":3900,
        "title":"Windows Server 2008実践ガイド",
        "sum(price,product(pages,2))":5308.0,
        "score":3.8475726},
      {
        "pages":608,
        "price":3800,
        "title":"はじめてのHadoop　～分散データ処理の基本から実践まで",
        "sum(price,product(pages,2))":5016.0,
        "score":3.7839036},
      {
        "pages":512,
        "price":3900,
        "title":"Spring3入門―Javaフレームワーク・より良い設計とアーキテクチャ",
        "sum(price,product(pages,2))":4924.0,
        "score":3.70927},
      {
        "pages":768,
        "price":3380,
        "title":"Windows8.1 全操作 Bible",
        "sum(price,product(pages,2))":4916.0,
        "score":3.8853612},
      {
        "pages":640,
        "price":3600,
        "title":"パーフェクトJava",
        "sum(price,product(pages,2))":4880.0,
        "score":3.80618}]
  }}
```


# 6.8 キャッシュ

Solr は以下のキャッシュ機能を備える。

- 検索結果キャッシュ
- フィルタキャッシュ
- ドキュメントキャッシュ
- フィールド値キャッシュ
- ユーザ定義キャッシュ

## キャッシュの種類

- **検索結果キャッシュ**
	- 個々の検索結果（= ドキュメント ID + 並び順）をキャッシュする
	- キャッシュのキー：
		- 検索式（q）
		- ソート条件（sort）
		- フィルタクエリ（fq）
	- 結果リストが保持されるため、順序も合わせて記憶される
	- ここでいう「ドキュメント ID」は Solr の内部的な管理用 ID であり、ユーザ定義のユニークキーとは別物
	- キャッシュ利用の流れ
		1. ユーザからの検索リクエスト
		2. 結果キャッシュにデータが存在するかチェック
		3. キャッシュデータがあれば、その中のドキュメント ID をもとに各フィールドの値をインデックスから取得（キャッシュに入っているのはドキュメント ID だけで、フィールドの値は含まれないため）

```xml
<config>
	<query>
		<queryResultCache class="solr.LRUCache" size="512" initialSize="512" autowarmCount="0" />
	</query>
<config>
```

- **フィルタキャッシュ**
	- フィルタクエリ（fq）の絞り込み条件と、条件にマッチするドキュメントの集合をキャッシュする
	- 検索結果キャッシュと異なり、順序は保持されない
	- リクエスト時 fq パラメータに`{!cache=false}`を指定すると、そのフィルタの結果はキャッシュされない

```xml
<config>
	<query>
		<filterCache class="solr.FastLRUCache" size="512" initialSize="512" autowarmCount="0" />
	</query>
<config>
```

- **ドキュメントキャッシュ**
	- 管理用 ID をキーに、ドキュメントそのものをキャッシュする

```xml
<config>
	<query>
		<documentCache class="solr.LRUCache" size="512" initialSize="512" autowarmCount="0" />
	</query>
<config>
```

- **フィールド値キャッシュ**
	- ファセット、グルーピングクエリ、ソートで使用されるキャッシュ
	- フィールドの docValues 設定が false の場合に利用される（true の場合は Doc Values が使われる）
	- このキャッシュに関しては、設定をコメントアウトしても Solr 内部で自動的に生成される

```xml
<config>
	<query>
		<fieldValueCache class="solr.FastLRUCache" size="512" autowarmCount="128" showItems="32" />
	</query>
<config>
```

- **ユーザ定義キャッシュ**
	- ユーザ独自のキャッシュを埋め込むこともできる
	- 詳細は公式ドキュメントや Javadoc を参照

```xml
<config>
	<query>
		<cache name="myUserCache" class="solr.LRUCache" size="4096" initialSize="1024" autowarmCount="1024" regenerator="org.mycompany.mypackage.MyRegenerator" />
	</query>
<config>
```


## キャッシュの設定

| 属性 | 説明 |
| :-- | :-- |
| class | キャッシュの実装。指定可能な実装は`solr.LRUCache`,`solr.FastLRUCache`,`solr.LFUCache`の3つ<br>※LRU: Least Recently Used（最後に参照してから最も長い時間が経っているデータを捨てる）<br>※LFU: Least Frequently Used（最も使用頻度が小さいデータを捨てる） |
| size | 保持できるキャッシュエントリの最大数 |
| initialSize | キャッシュの初期サイズ（エントリ数） |
| autowarmCount | 自動ウォームアップ（後述）で生成するキャッシュのサイズ。パーセンテージで指定することも可能 |
| maxRamMB | キャッシュで使用できるヒープサイズの上限値（queryResultCache のみ） |


## キャッシュの自動ウォームアップ

- Solr が持つ各種のキャッシュは、インデックスが更新されるタイミングで破棄される
	- これは、キャッシュが持つ内部管理用の ID が更新のタイミングでリセットされるため
- **キャッシュの自動ウォームアップ**：
	- キャッシュが破棄された直後にレスポンス性能が悪化することを防ぐための仕組み
	- インデックスを更新した後にも更新前のキャッシュキーを引き継いで利用し、キャッシュのヒット率を維持する
	- 実際の処理内容としては、更新前にキャッシュに使用されていたキーで新しいインデックスに対する検索が行われ、新しいキャッシュ値を生成する
	- ドキュメントキャッシュに対しては自動ウォームアップは利用できない

## キャッシュの統計情報

ヒット率やサイズなどの統計情報を管理画面（Solr コア選択 >「Plugins / Stats」> CACHE）から確認できる。

![Alt text](./20171015_solr_cache_stats.png)

| 項目 | 説明 |
| :-- | :-- |
| class | キャッシュの実装クラス名 |
| version | キャッシュの実装クラスのバージョン |
| description | キャッシュの説明 |
| lookups | キャッシュの検索回数 |
| hits | キャッシュのヒット回数 |
| hitratio | キャッシュのヒット率 |
| inserts | キャッシュの登録回数 |
| evictions | キャッシュからエントリが追い出された回数 |
| size | キャッシュのエントリ数 |
| warmupTime | ウォームアップにかかった時間 |
| cumulative_* | Solr を起動したときからの各値の累積値 |

「cumulative_」がついていない項目は、最後にキャッシュが破棄されて以降の統計情報。更新のコミットのたびにゼロにクリアされる
