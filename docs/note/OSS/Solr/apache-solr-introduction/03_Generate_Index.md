---
title: 3. インデックスの作成
---

# 3.1 ドキュメントの登録

あらかじめ、

- コアの作成
- スキーマ定義

は実施しておく。

## JSON ファイルによる登録

JSON ファイルには2通りの書式がある。
- 単にフィールドに値を入れる書式
```json
[
  {
    "フィールド名": "値",
    "フィールド名": ["複数の値1", "複数の値2", ...],
    ...
  },
  ...
]
```
- ドキュメントごとに何らかのオプションを設定できる書式
```json
[
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
    }
  }
  ...
]
```

2つ目の方式では、ドキュメントやフィールドに対して`boost`というオプションも与えられる。

```json
{
  "add": {
    "doc": {
      "フィールド1": {"boost": 2.0, "value": "値1"},
      "フィールド2": "値2",
      ...
    },
    "boost": 2.5
    "オプション名": "値",
    ...
  }
}
```

この場合、以下のことを表す（ランキング用のスコアにブーストがかかる）。
- フィールド1は他の（boost されていない）フィールドに比べて2.0倍重要
- このドキュメントは他の（boost されていない）ドキュメントに比べて2.5倍重要

> フィールドに対して boost を使う場合は、omitNorms オプションが false である必要がある

Solr への登録：

- post ツール
```bash
$ ${SOLR}/bin/post -c <core_name> hoge.json
```
- curl コマンド
```bash
$ curl -H 'Content-type:text/json' --data-binary @hoge.json http://<hostname>:8983/solr/<core_name>/update?commit=true
```


## XML ファイルによる登録

以下のように記述する。JSON 同様、boost 値の設定もできる。

```xml
<add>
  <doc>
    <field name="フィールド名">値</field>
    <field name="フィールド名">値</field>
    ...
  </doc>
  <doc boost="2.5">
    <field name="フィールド名" boost="2.0">値</field>
    <field name="フィールド名">値</field>
    ...
  </doc>
  ...
</add>
```

> **【要確認】xml の書式だと、同じフィールドに対して別の boost 値を設定できそうだが、こうするとどうなる...？**
> ```xml
> <doc boost="2.5">
>   <field name="id" boost="2.0">0123</field>
>   <field name="author" boost="1.0">taro</field>
>   <field name="author" boost="2.0">jiro</field>
>   <field name="author" boost="3.0">saburo</field>
> </doc>
> ```

Solr への登録：

- post ツール
```bash
$ ${SOLR}/bin/post -c <core_name> hoge.xml
```
- curl コマンド
```bash
$ curl -H 'Content-type:text/xml' --data-binary @hoge.xml http://<hostname>:8983/solr/<core_name>/update?commit=true
```


## CSV ファイルによる登録

以下のような書式で、CSV ファイルも登録できる。
```bash
id,title,author,price
"http://sample.com/book?id=001","Apache Solr","田中太郎|山田花子","1234"
```
- この例では複数値を持つフィールドのセパレータを`|`としているが、これは登録時にオプションで指定する必要がある。
- CSV の場合、boost は使えない。


# 3.2 登録の確認

- Web UI でコアを選択すれば "Num Docs" などで正常にインデックスされたことが確認できる
- "query" から "\*:\*" で検索をかければドキュメント全文が見られる


# 3.3 インデックスディレクトリ

Solr がシングルのサーバで動作しているとき、インデックス情報はすべて1つのディレクトリ（**データディレクトリ**）に格納される。
通常は、コアディレクトリ内の data ディレクトリになる。

```bash
$ tree ${SOLR}/server/solr/<core_name>/data/
server/solr/<core_name>/data/
├── index  # 転置インデックスが格納されている
│   ├── _2.fdt
│   ├── _2.fdx
│   ├── _2.fnm
│   ├── _2.nvd
│   ├── _2.nvm
│   ├── _2.si
│   ├── _2_Lucene50_0.doc
│   ├── _2_Lucene50_0.pos
│   ├── _2_Lucene50_0.tim
│   ├── _2_Lucene50_0.tip
│   ├── _2_Lucene54_0.dvd
│   ├── _2_Lucene54_0.dvm
│   ├── segments_4
│   └── write.lock
├── snapshot_metadata
└── tlog
    └── tlog.0000000000000000002
```

データディレクトリの決定方式：
1. コアディレクトリの conf 以下にある solrconfig.xml に`<dataDir>...</dataDir>`が設定されていればそこ
2. 1を満たさない場合はコアディレクトリ内の data ディレクトリ


# 3.4 ドキュメントの更新

- スキーマ定義でユニークキーを指定していれば、登録済みのドキュメントを更新できる（ユニークキーがない場合、単なる追加となる）。
- 更新フォーマットは通常の登録時と全く同じであり、対象ドキュメントのユニークキーが登録済みならば更新、未登録ならば新規登録となる。

> 「更新」といっても、実際の処理においては上書きではなく、古いドキュメントを削除して新しく登録している。
> → つまり、**更新時には新規登録時と同様、ドキュメントを構成するすべてのフィールドを指定する必要がある**

## アトミックアップデート（部分更新）

- ドキュメントのすべてのフィールドが`stored=true`または`docValues=true`である場合に限り、更新対象のフィールドだけで部分更新が可能になる。
- これは、上記の場合であればすべてのフィールドを渡さなくても Solr 内部で他の値を補完できるため。

アトミックアップデートを行う場合、明示的にそれを示す記述をする。

```json
{
  "id": "001",
  "フィールド1": {"set": "hoge"},
  "フィールド2": {"add": ["fuga"]}
}
```
この例では、指定した id のドキュメントについて以下の変更を行っている。
- フィールド1を hoge で書き換え
- フィールド2の multiValued の値に fuga を追加
- 他のフィールド（フィールド3, フィールド4, ...）はそのまま

※**post ツールを使って更新する場合、アトミックアップデートのときには`-format solr`をつけないと正しく動作しない**。

使える修飾子：

| 修飾子 | 説明 |
| :-- | :-- |
| set | 指定された値で更新する。null が指定された場合、該当フィールド値を（multiValued=true のフィールドならすべての値を）インデックスから削除する|
| add | multiValued=true のフィールドにしか使えない。指定した値（複数指定可）を追加する |
| remove | multiValued=true のフィールドにしか使えない。指定した値（複数指定可）を削除する |
| removeregex | multiValued=true のフィールドにしか使えない。指定した正規表現（Java で扱えるものに準拠）にマッチする値を削除する |
| inc | 指定された値を数値フィールドの値に加算する |


# 3.5 ドキュメントの削除

ドキュメントの削除には2つの方法がある。json などの書式でリクエストを送るのは登録・更新と同じ。

- post ツール
```bash
$ ${SOLR}/bin/post -c <core_name> delete.json -format solr
```
- curl コマンド
```bash
$ curl -H 'Content-type:text/json' --data-binary @delete.json http://<hostname>:8983/solr/<core_name>/update?commit=true
```

※**post ツールを使って更新する場合、削除のときには`-format solr`をつけないと正しく動作しない**。

## ユニークキーを指定

```json
{"delete": {"id": "001"}}
```

**ここでいう "id" はフィールド名ではなく、「ユニークキーである」ことを意味する予約語。よって、ユニークキーを "url" などに自分で書き換えている場合でも "id" を指定する。**

## クエリで条件を指定

```json
{"delete": {"query": "author:田中 太郎"}}
```

> **正確には、この削除は論理削除（削除フラグを立てているだけで実データはまだ残っている）**。物理削除の方法は後述。


# 3.6 コミット/ロールバック

- ドキュメントの登録・更新・削除を確定し、検索結果に反映させるには**コミット**が必要
- コミット前であれば、操作を取り消す**ロールバック**が行える

※コミットを繰り返すとインデックスが物理的に複数のファイルに分かれてしまうことがあり、その分検索性能が悪化するため、オプティマイズ（5章）を行うとよいケースがある

## コミット

- リクエストパラメータによるコミット

```bash
$ curl http://<hostname>:8983/solr/<core_name>/update?commit=true
```

これまでの登録・更新・削除の例でも`commit=true`をつけていたのは、これらの操作とコミットを同時に行っていた。

- JSON, XML によるコミット

以下の内容の JSON, XML ファイルを Solr にポストすることでもコミットできる。

```json
{"commit": {}}
```

```xml
<commit/>
```

コミットで指定可能なオプション：

| オプション | デフォルト値 | 説明 |
| :-- | :-- | :-- |
| waitSearcher | true | true なら、新しいサーチャで検索が可能になるまで、コミットまたはオプティマイズを POST したクライアントに制御を戻さない |
| expungeDeletes | false | true なら、delete ときにドキュメントを完全にインデックスから削除する |

## ソフトコミット

- 通常のコミット（**ハードコミット**）ではインデックスファイルへの書き出しを行ってから検索が可能になる
- **ソフトコミット**では、ディスクへのインデックスの書き出しを行わないため、より早く検索可能になる（当然、サーバのクラッシュや障害で Solr がダウンするとデータは失われる）

```bash
$ curl http://<hostname>:8983/solr/<core_name>/update?softCommit=true
```


## 自動コミット
solrconfig.xml に以下の設定をしておけば、自動的なコミットの発行ができる。
```xml
<autoCommit>
  <!-- 未コミットのドキュメントがこの数を超えたらコミット -->
  <maxDocs>10000</maxDocs>
  <!-- 登録・更新・削除が行われてからこの時間（ミリ秒）が立ったらコミット -->
  <maxTime>1000</maxTime>
  <!-- コミット実行時に新しいサーチャを開くかどうか（true だとパフォーマンス劣化） -->
  <openSearcher>true</openSearcher>
</autoCommit>
```

## commitWithin
ドキュメントの追加・更新などの際に commitWithin を指定すると、指定時間（ミリ秒）以内にコミットを開始するよう Solr に指示できる。

```bash
$ curl -H 'Content-type:text/xml' --data-binary @hoge.xml http://<hostname>:8983/solr/<core_name>/update?commitWithin=1000
```

```json
[
  {
    "add": {
      "doc": {
        ...
      },
      "commitWithin": "1000"
    }
  }
]
```

```xml
<add commitWithin="1000">
  <doc>...</doc>
</add>
```

## ロールバック

コミット実行前、あるいはソフトコミットの実行後でも、ロールバックが行える。
```bash
$ curl http://<hostname>:8983/solr/<core_name>/update?rollback=true
```

```json
{"rollback": {}}
```

```xml
<rollback/>
```

> **【注意】**
> 複数のクライアントが同じ Solr に対して追加・更新・削除した場合、その後に誰かが1度コミットすると、コミットしたクライアントだけでなく、全クライアントの add したデータがまとめてコミットされる
