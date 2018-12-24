---
title: Prometheus
logo: https://user-images.githubusercontent.com/13412823/50383404-4fad7500-06f6-11e9-98b5-622b8b85f16b.png
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


# PromQL

Prometheus 独自のクエリを使ってデータを整形できる。

| 演算子・関数 | 説明 | クエリの例 | 備考 |
| :-- | :-- | :-- | :-- |
| `+`,`-`,`*`,`/`,`%` | 四則演算、剰余計算 | `( node_memory_MemTotal_bytes - node_memory_MemFree_bytes ) / node_memory_MemTotal_bytes * 100`<br>（メモリ使用率 [%]） |
| `rate` | 指定した期間の始点と終点から求まる、1秒あたりの増加量 | `rate(node_cpu_seconds_total{mode!="idle"}[1m]) * 100`<br>（CPU 使用率 [%]） | `mode!="idle"`により、idle 状態を除外している |
| `delta` | 期間の始点と終点の差分（終点-始点） | `delta(node_memory_MemFree_bytes[1h])`<br>（空きメモリの変化） |
| `changes` | 期間中に値の変化が何回起こったかをカウント |  |
| `max`,`min`,`sum`,`avg` |  |  |
