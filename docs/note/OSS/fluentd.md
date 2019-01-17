---
title: fluentd
main_image: https://user-images.githubusercontent.com/13412823/51295596-af7c0f00-1a5b-11e9-92ed-4e4c826ae66b.png
---


# fluentd とは

オープンソースのログ収集ミドルウェア。
ストリーミング処理に適する。
柔軟性のため Ruby で書かれ、パフォーマンスに関わる部分は C で書かれる。

# 特徴

## JSON 形式の構造化データ

ログデータを JSON として扱い、プログラムで利用しやすくしている。

## 全てはプラグイン

柔軟なプラグインアーキテクチャを持ち、Ruby を使って容易に実装・配布できる。

## 高い信頼性と性能

メモリ、ファイルベースの組み込みバッファリング機能、自動リトライ機能を持つ。

→ノード間のデータ欠損を防ぐ。


# アーキテクチャ

## データ構造

1つのイベントは**タグ**、**時間**、**レコード**という3要素の配列で管理される。

### タグ（文字列型）

データソースの識別子。要素をドット区切りで書き、\*（タグ要素1個）や\*\*（タグ要素0個以上）などのワイルドカードでマッチさせられる。

### 時間（整数型）

データの発生時刻を UNIX タイムスタンプで表現。

### レコード（オブジェクト型）

JSON。key-value 形式の連想配列を格納し、データそのものを表現。

## プラグインアーキテクチャ

fluentd のコア部分は小さなプログラムで、他のほとんどはプラグインで成り立つ。

### Input プラグイン

アプリケーションや他のサーバ、ファイルなど様々なソースからログを受け取る。

|プラグイン|意味|
|:-|:-|
|tail|ログファイルを読み込む|
|http|HTTP でデータを受け取る|
|forward|他の Fluentd からデータを受け付ける|

### Parser プラグイン

ログのパース処理を行う。

### Filter プラグイン

データ加工や集計を行う。

|プラグイン|意味|
|:-|:-|
|grep|正規表現でマッチするものだけを残す|
|record_transformer|メッセージの改変を行う|

### Formatter プラグイン

データのフォーマット処理を行う。

### Output プラグイン

ログをストレージに書き出したり他のサーバに送ったりする。

|プラグイン|意味|
|:-|:-|
|file|ファイルへ出力|
|forward|他の Fluentd にファイルを送る|

### Buffer プラグイン
ログをバッファリングして、スループットや信頼性を向上させる。

fluentd では以上のようなプラグインをパイプのように接続してデータを処理する。


## ディレクティブ

6つのディレクティブを持つ。

- **`<source>`ディレクティブ**

type パアラメータに Input プラグインを設定

- **`<match>`ディレクティブ**

引数は処理したいタグのマッチパターン。type パラメータに Output プラグインを設定

- **`<filter>`ディレクティブ**

引数は処理したいタグのマッチパターン。type パラメータに Filter プラグインを設定

- **`<system>`ディレクティブ**

Fluentd コアの動作を設定。ログレベルの決定や、連続する同一スタックトレースの抑制などを設定

- **`<label>`ディレクティブ**

ラベルによる処理のルーティングを行う

- **`@include`ディレクティブ**

分割された設定ファイルを読み込む。

```bash
# include user config
@include /path/to/config/1/application.conf
@include /path/to/config/2/*.conf
```

# 書式

|書式|意味|
|:-|:-|
|`#(半角スーペース)hoge`|コメント|
|`"hoge"`|内部に Ruby のコードを埋め込める|
|`'hoge'`|Ruby のコードは使えない|

# インストール・起動

Ruby のデーモンを操作したり、インストールするのに手間取りやすい。

→ stable なパッケージ（**td-agent**）が配布されている。

以後、バージョンは **fluentd 0.12** を想定する。

## 1. インストール準備

- NTP を立ち上げる（推奨）
- ファイルディスクリプタの上限を増やす：/etc/security/limits.conf を編集
- ネットワークパラメータを最適化：/etc/sysctl.conf を修正し、以下のパラメータを設定
	- `net.ipv4.tcp_tw_recycle = 1`
	- `net.ipv4.tcp_tw_reuse = 1`
	- `net.ipv4.ip_local_port_range = 10240 65535`

## 2. OS に対応する td-agent をインストール

OS ごとにスクリプトのアドレスが違う。

以後は ubuntu 16.04 の例。

```bash
$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS"
$ curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-xenial-td-agent2.sh | sh
```

```bash
$ /etc/init.d/td-agent start
$ /etc/init.d/td-agent stop
$ /etc/init.d/td-agent restart
$ /etc/init.d/td-agent status
```

※ パスが通っている`/usr/sbin/td-agent`とは違うっぽい。実行したら使い方が違うと言われた。

```
$ td-agent stop
Usage: td-agent [options]
    -s, --setup [DIR=/etc/td-agent]  install sample configuration file to the directory
    -c, --config PATH                config file path (default: /etc/td-agent/td-agent.conf)
        --dry-run                    Check fluentd setup is correct or not
        --show-plugin-config=PLUGIN  Show PLUGIN configuration and exit(ex: input:dummy)
    -p, --plugin DIR                 add plugin directory
    -I PATH                          add library path
    -r NAME                          load library
    -d, --daemon PIDFILE             daemonize fluent process
        --no-supervisor              run without fluent supervisor
        --user USER                  change user
        --group GROUP                change group
    -o, --log PATH                   log file path
    -i CONFIG_STRING,                inline config which is appended to the config file on-fly
        --inline-config
        --emit-error-log-interval SECONDS
                                     suppress interval seconds of emit error logs
        --suppress-repeated-stacktrace [VALUE]
                                     suppress repeated stacktrace
        --without-source             invoke a fluentd without input plugins
        --use-v1-config              Use v1 configuration format (default)
        --use-v0-config              Use v0 configuration format
    -v, --verbose                    increase verbose level (-v: debug, -vv: trace)
    -q, --quiet                      decrease verbose level (-q: warn, -qq: error)
        --suppress-config-dump       suppress config dumping when fluentd starts
    -g, --gemfile GEMFILE            Gemfile path
    -G, --gem-path GEM_INSTALL_PATH  Gemfile install path (default: $(dirname $gemfile)/vendor/bundle)
```

## 3. HTTP 経由でログを投げてみる

```bash
$ curl -X POST -d 'json={"json":"message"}' http://localhost:8888/debug.test
$ tail -n 3 /var/log/td-agent/td-agent.log
2017-02-27 16:23:56 +0900 [info]: listening fluent socket on 0.0.0.0:24224
2017-02-27 16:23:56 +0900 [info]: listening dRuby uri="druby://127.0.0.1:24230" object="Engine"
2017-02-27 16:24:47 +0900 debug.test: {"json":"message"}
```


# 基本的な設定

設定ファイル /etc/td-agent/td-agent.conf を編集する。

fluentd 起動中に設定を変更した場合、変更内容を反映させるために以下のようなコマンドで設定を再読み込みする（sudo 必要かも）。

```
/etc/init.d/td-agent reload
```

## 未編集の設定ファイル

```xml
$ cat /etc/td-agent/td-agent.conf
####
## Output descriptions:
##

# Treasure Data (http://www.treasure-data.com/) provides cloud based data
# analytics platform, which easily stores and processes data from td-agent.
# FREE plan is also provided.
# @see http://docs.fluentd.org/articles/http-to-td
#
# This section matches events whose tag is td.DATABASE.TABLE
<match td.*.*>
  @type tdlog
  apikey YOUR_API_KEY

  auto_create_table
  buffer_type file
  buffer_path /var/log/td-agent/buffer/td

  <secondary>
    @type file
    path /var/log/td-agent/failed_records
  </secondary>
</match>

## match tag=debug.** and dump to console
<match debug.**>
  @type stdout
</match>

####
## Source descriptions:
##

## built-in TCP input
## @see http://docs.fluentd.org/articles/in_forward
<source>
  @type forward
</source>

## built-in UNIX socket input
#<source>
#  @type unix
#</source>

# HTTP input
# POST http://localhost:8888/<tag>?json=<json>
# POST http://localhost:8888/td.myapp.login?json={"user"%3A"me"}
# @see http://docs.fluentd.org/articles/in_http
<source>
  @type http
  port 8888
</source>

## live debugging agent
<source>
  @type debug_agent
  bind 127.0.0.1
  port 24230
</source>

####
## Examples:
##

## File input
## read apache logs continuously and tags td.apache.access
#<source>
#  @type tail
#  format apache
#  path /var/log/httpd-access.log
#  tag td.apache.access
#</source>

## File output
## match tag=local.** and write to file
#<match local.**>
#  @type file
#  path /var/log/td-agent/access
#</match>

## Forwarding
## match tag=system.** and forward to another td-agent server
#<match system.**>
#  @type forward
#  host 192.168.0.11
#  # secondary host is optional
#  <secondary>
#    host 192.168.0.12
#  </secondary>
#</match>

## Multiple output
## match tag=td.*.* and output to Treasure Data AND file
#<match td.*.*>
#  @type copy
#  <store>
#    @type tdlog
#    apikey API_KEY
#    auto_create_table
#    buffer_type file
#    buffer_path /var/log/td-agent/buffer/td
#  </store>
#  <store>
#    @type file
#    path /var/log/td-agent/td-%Y-%m-%d/%H.log
#  </store>
#</match>
```

## ファイルから読み込んでそのままファイルに書き出す

```xml
<source>
  @type tail
  path /var/log/syslog
  pos_file /var/log/td-agent/syslog.pos
  tag syslog.line
  format syslog
</source>

<match syslog.line>
  @type file
  path /tmp/syslog_fluentd.output
</match>
```


# プラグインのインストール

cf. [Aggregate and Analyze Syslog with InfluxDB](http://www.fluentd.org/guides/recipes/syslog-influxdb)

以下は influxdb を使うためのプラグインを導入した例（sudo 必要かも）。

```bash
$ /usr/sbin/td-agent-gem install fluent-plugin-influxdb
```

使ってみる：

```xml
<source>
  ...
</source>

<match syslog.line>
  @type influxdb
  dbname test_db
  flush_interval 10s  # for testing.
</match>
```

※設定の再読み込み（`td-agent reload`）だけではプラグインが読まれなかった。デーモン自体の再起動（`td-agent restart`）でいけたっぽい。

接続できてるっぽい：

```bash
$ sudo tail /var/log/td-agent/td-agent.log
  <match syslog.line>
    @type influxdb
    dbname test_db
    flush_interval 10s
  </match>
</ROOT>
2017-04-23 12:47:46 +0900 [info]: Connecting to database: test_db, host: localhost, port: 8086, username: root, use_ssl = false, verify_ssl = true
2017-04-23 12:47:46 +0900 [info]: listening fluent socket on 0.0.0.0:24224
2017-04-23 12:47:46 +0900 [info]: listening dRuby uri="druby://127.0.0.1:24230" object="Engine"
2017-04-23 12:47:46 +0900 [info]: following tail of /var/log/syslog
```

# トラブルシューティング

## ファイルが読み込まれない

/var/log/syslog を読もうとして発生した問題。ログを見てみた。

```
$ sudo tail /var/log/td-agent/td-agent.log
2017-04-23 11:51:21 +0900 [error]: Permission denied @ rb_sysopen - /var/log/syslog
  2017-04-23 11:51:21 +0900 [error]: suppressed same stacktrace
2017-04-23 11:51:22 +0900 [error]: Permission denied @ rb_sysopen - /var/log/syslog
  2017-04-23 11:51:22 +0900 [error]: suppressed same stacktrace
2017-04-23 11:51:23 +0900 [error]: Permission denied @ rb_sysopen - /var/log/syslog
  2017-04-23 11:51:23 +0900 [error]: suppressed same stacktrace
...
```

read 権限の問題で読めてないっぽい。

```
$ ls -la
...
-rw-r-----  1 syslog            adm      207K  4月 23 12:01 syslog
...
```

**【解決】**

- `chmod`で読み込み権限付与

```bash
$ sudo chmod 644 /var/log/syslog
```

- ログローテートで今後生成されるファイルの権限も変えておく
	- /etc/rsyslog.conf の設定を修正
	- rsyslog 再起動（`/etc/init.d/rsyslog restart`）

```bash
$FileCreateMode 0644  # 0640 から修正
$DirCreateMode 0755
```

