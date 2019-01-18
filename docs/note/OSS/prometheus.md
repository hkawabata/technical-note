---
title: Prometheus
main_image: https://user-images.githubusercontent.com/13412823/50383404-4fad7500-06f6-11e9-98b5-622b8b85f16b.png
---

https://prometheus.io/

# アーキテクチャ

Prometheus の役割は次の3つ：

- メトリクスデータの収集・格納
- クエリによるデータ整形
- アラート

![](https://camo.githubusercontent.com/78b3b29d22cea8eee673e34fd204818ea532c171/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f70726f6d6574686575732f70726f6d65746865757340633334323537643036396336333036383564613335626365663038343633326666643564363230392f646f63756d656e746174696f6e2f696d616765732f6172636869746563747572652e737667)

# 使ってみる

## バイナリのダウンロード・起動

### Prometheus

```bash
$ wget https://github.com/prometheus/prometheus/releases/download/v2.6.0/prometheus-2.6.0.linux-amd64.tar.gz
$ tar xvzf prometheus-2.6.0.linux-amd64.tar.gz
$ cd prometheus-2.6.0.linux-amd64/

$ ./prometheus --help
usage: prometheus [<flags>]

The Prometheus monitoring server

Flags:
  -h, --help                     Show context-sensitive help (also try --help-long and --help-man).
      --version                  Show application version.
      --config.file="prometheus.yml"  
                                 Prometheus configuration file path.
      ...

$ ./prometheus --config.file=prometheus.yml
...
level=info ts=2018-12-23T12:18:52.893777989Z caller=web.go:429 component=web msg="Start listening for connections" address=0.0.0.0:9090
```

http://hostname:9090 で Web UI にアクセスできる。

![2018-12-23 21 21 11](https://user-images.githubusercontent.com/13412823/50383520-b7fd5600-06f8-11e9-8372-18c802d9efd1.png)

![2018-12-24 18 28 19](https://user-images.githubusercontent.com/13412823/50395980-4b429400-07aa-11e9-9d8d-7f82a58248a6.png)


### Node Exporter

```bash
$ wget https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
$ tar xvzf node_exporter-0.17.0.linux-amd64.tar.gz
$ cd node_exporter-0.17.0.linux-amd64/
$ ./node_exporter
INFO[0000] Starting node_exporter (version=0.17.0, branch=HEAD, revision=f6f6194a436b9a63d0439abc585c76b19a206b21)  source="node_exporter.go:82"
INFO[0000] Build context (go=go1.11.2, user=root@322511e06ced, date=20181130-15:51:33)  source="node_exporter.go:83"
INFO[0000] Enabled collectors:                           source="node_exporter.go:90"
INFO[0000]  - arp                                        source="node_exporter.go:97"
INFO[0000]  - bcache                                     source="node_exporter.go:97"
INFO[0000]  - bonding                                    source="node_exporter.go:97"
INFO[0000]  - conntrack                                  source="node_exporter.go:97"
INFO[0000]  - cpu                                        source="node_exporter.go:97"
INFO[0000]  - diskstats                                  source="node_exporter.go:97"
INFO[0000]  - edac                                       source="node_exporter.go:97"
INFO[0000]  - entropy                                    source="node_exporter.go:97"
INFO[0000]  - filefd                                     source="node_exporter.go:97"
INFO[0000]  - filesystem                                 source="node_exporter.go:97"
INFO[0000]  - hwmon                                      source="node_exporter.go:97"
INFO[0000]  - infiniband                                 source="node_exporter.go:97"
INFO[0000]  - ipvs                                       source="node_exporter.go:97"
INFO[0000]  - loadavg                                    source="node_exporter.go:97"
INFO[0000]  - mdadm                                      source="node_exporter.go:97"
INFO[0000]  - meminfo                                    source="node_exporter.go:97"
INFO[0000]  - netclass                                   source="node_exporter.go:97"
INFO[0000]  - netdev                                     source="node_exporter.go:97"
INFO[0000]  - netstat                                    source="node_exporter.go:97"
INFO[0000]  - nfs                                        source="node_exporter.go:97"
INFO[0000]  - nfsd                                       source="node_exporter.go:97"
INFO[0000]  - sockstat                                   source="node_exporter.go:97"
INFO[0000]  - stat                                       source="node_exporter.go:97"
INFO[0000]  - textfile                                   source="node_exporter.go:97"
INFO[0000]  - time                                       source="node_exporter.go:97"
INFO[0000]  - timex                                      source="node_exporter.go:97"
INFO[0000]  - uname                                      source="node_exporter.go:97"
INFO[0000]  - vmstat                                     source="node_exporter.go:97"
INFO[0000]  - xfs                                        source="node_exporter.go:97"
INFO[0000]  - zfs                                        source="node_exporter.go:97"
INFO[0000] Listening on :9100                            source="node_exporter.go:111"
```

http://hostname:9100/metrics にアクセスするとメトリクス一覧が参照できる。


## Prometheus から exporter を監視

prometheus.yml を以下のように設定する。

```yaml
scrape_configs:
  ...
  - job_name: 'node'
    static_configs:
    - targets: ['node001.hkawabata.jp:9100']
```

Prometheus Web UI でクエリを投げればグラフが見られる。

ex. 1分ごとの平均受信データ量[Bytes]：`rate(node_network_receive_bytes_total[1m])`

![2018-12-23 22 53 48](https://user-images.githubusercontent.com/13412823/50384239-b25a3d00-0705-11e9-8821-19cc5346d73b.png)

## Graphana で可視化

データソース追加：

![2018-12-23 23 06 38](https://user-images.githubusercontent.com/13412823/50384376-6e683780-0707-11e9-98cd-ea4f9ff9051d.png)

グラフ作成：

![2018-12-23 23 04 33](https://user-images.githubusercontent.com/13412823/50384359-382ab800-0707-11e9-9229-519df9867e3b.png)

「Legend Format」欄には、`{{instance}} ({{device}})`のように Prometheus のラベルを埋め込める。

# PromQL

Prometheus 独自のクエリを使ってデータを整形できる。

## データ型

| データ型 | 説明 | 例 |
| :-- | :-- | :-- |
| Instant Vector | 各時点の単一の値を並べたベクトル | `node_filesystem_files` |
| Range Vector | 各時点について、そこから指定した期間だけ前までさかのぼった値のリストを並べたベクトル | `node_memory_MemFree_bytes[1m]` |
| Scalar | 単一の数値 |  |
| String | 単一の文字列 (ver 2.6 現在未使用) |  |

Instant Vector のイメージ:

```json
{
  "14:56": 0.98,
  "14:57": 0.98,
  "14:58": 0.99,
  "14:59": 0.50,
  "15:00": 0.52
}
```

Range Vector のイメージ:

```json
{
  "14:58": {
    "14:56": 0.98,
    "14:57": 0.98,
    "14:58": 0.99,
  },
  "14:59": {
    "14:57": 0.98,
    "14:58": 0.99,
    "14:59": 0.50,
  },
  "15:00": {
    "14:58": 0.99,
    "14:59": 0.50,
    "15:00": 0.52
  }
}
```

## 演算子・関数

| 演算子・関数 | 説明 | クエリの例 | 備考 |
| :-- | :-- | :-- | :-- |
| `+`,`-`,`*`,`/`,`%` | 四則演算、剰余計算 | `( node_memory_MemTotal_bytes - node_memory_MemFree_bytes ) / node_memory_MemTotal_bytes * 100`<br>（メモリ使用率 [%]） |
| `rate` | 指定した期間の始点と終点から求まる、1秒あたりの増加量 | `rate(node_cpu_seconds_total{mode!="idle"}[1m]) * 100`<br>（CPU 使用率 [%]） | `mode!="idle"`により、idle 状態を除外している |
| `delta` | 期間の始点と終点の差分（終点-始点） | `delta(node_memory_MemFree_bytes[1h])`<br>（空きメモリの変化） |
| `changes` | 期間中に値の変化が何回起こったかをカウント |  |
| `max`,`min`,`sum`,`avg` |  |  |


# Exporter

## node_exporter

## jmx_exporter

### jmx_prometheus_httpserver

exporter 専用のプロセスを立ち上げる。

```bash
$ git clone git@github.com:prometheus/jmx_exporter.git
$ cd jmx_exporter
$ mvn package
...
```

必要なファイルは、
- ビルド生成物の`jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-${version}-jar-with-dependencies.jar`
- 設定ファイル`example_configs/httpserver_sample_config.yml`

httpserver_sample_config.yml の`hostPort`設定はデフォルトで`localhost:5555`となっている（これは jmx_prometheus_httpserver プロセス自身の jmx ポート）。

これを監視したいプロセスの情報に書き換える。

例：

```
---
hostPort: localhost:1099
username: 
password: 

rules:
- pattern: ".*"
```

jmx_prometheus_httpserver 起動：

```bash
$ version=$(sed -n -e 's#.*<version>\(.*-SNAPSHOT\)</version>#\1#p' pom.xml)
$ jar_file=jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-${version}-jar-with-dependencies.jar
$ exporter_jmx_port=5555     # jmx_prometheus_httpserver プロセス自身の jmx ポート
$ exporter_port=5556         # prometheus からのリクエストを待ち受けるポート
$ config_file=example_configs/httpserver_sample_config.yml

$ java -Dcom.sun.management.jmxremote.ssl=false \
    -Dcom.sun.management.jmxremote.authenticate=false \
    -Dcom.sun.management.jmxremote.port=${exporter_jmx_port} \
    -jar ${jar_file} \
    ${exporter_port} \
    ${config_file}
```

以下は監視対象プロセス（jetty, jmx を1099ポートで有効化）と jmx_prometheus_httpserver を同じサーバで動かし、jconsole で眺めた様子。

![2018-12-24 18 10 07](https://user-images.githubusercontent.com/13412823/50395423-37496300-07a7-11e9-8590-a8f337395a27.png)

prometheus.yml に以下のように追記して Prometheus を再起動。

```yaml
scrape_configs:
  ...
  - job_name: 'jmx_jetty'
    static_configs:
    - targets: ['localhost:5556']
```

Graphana で可視化：

![2018-12-24 18 27 07](https://user-images.githubusercontent.com/13412823/50395864-c48db700-07a9-11e9-92d3-60ebbcb15e92.png)



### jmx_prometheus_javaagent


## Java クライアントで exporter を自作（雑多なメモ、整理中）

### quantile の計算

99%ile などの計算に関して、`Summary`は監視対象のアプリケーション側で計算コストがかかるが正確、`Histoguram`は Prometheus サーバ側で計算するためコストは低いが正確性が犠牲になる。

[ここ](https://prometheus.github.io/client_java/src-html/io/prometheus/client/Summary.Builder.html)に`Summary`を使うときに役立ちそうな説明がある。

> maxAgeSeconds(long): Set the duration of the time window is, i.e. how long observations are kept before they are discarded.
  Default is 10 minutes.

この保持期間は`Summary`のビルダーで設定可能で、これを過ぎると以下のような表記になる。

```
# HELP requests_latency_seconds_summary Request latency in seconds (Summary).
# TYPE requests_latency_seconds_summary summary
requests_latency_seconds_summary{quantile="0.1",} NaN
requests_latency_seconds_summary{quantile="0.3",} NaN
requests_latency_seconds_summary{quantile="0.5",} NaN
requests_latency_seconds_summary{quantile="0.7",} NaN
requests_latency_seconds_summary{quantile="0.9",} NaN
requests_latency_seconds_summary_count 125.0
requests_latency_seconds_summary_sum 61.848624543999996
```

> ageBuckets(int): Set the number of buckets used to implement the sliding time window. If your time window is 10 minutes, and you have ageBuckets=5,
  buckets will be switched every 2 minutes. The value is a trade-off between resources (memory and cpu for maintaining the bucket)
  and how smooth the time window is moved. Default value is 5.


### その他メモ

（メモ）この辺りを参考にした：

- https://github.com/prometheus/client_java
- https://povilasv.me/prometheus-tracking-request-duration/
- https://prometheus.io/docs/practices/histograms/
- http://sylnsr.blogspot.com/2015/12/using-prometheus-with-java-in-jersey.html

サンプルコード：

https://github.com/hkawabata/WebApp/blob/master/jersey-practice/src/main/java/jp/hkawabata/webapp/sample/jersey/prometheus/MonitoredResource.java
