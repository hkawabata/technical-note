---
title: サーバのボトルネック調査
---

# サーバのボトルネックになり得るリソース

- CPU 使用率
- メモリ使用量
- ディスク I/O
- ネットワークコネクション数

# まずはロードアベレージを確認

`uptime`を使う。
- システム稼働時間
- 現在時刻
- ログインユーザ数
- 直近1分・5分・15分で計測したロードアベレージ

```bash
$ uptime 
 09:50:20 up 85 days, 19:56,  1 user,  load average: 0.00, 0.00, 0.00
```

## ロードアベレージが高い場合

以下のいずれかがボトルネックになっている可能性がある。

- CPU 使用率
- メモリ使用量
- ディスク I/O

## ロードアベレージが低い場合

ネットワークコネクション数、または該当サーバではなく接続先の別サーバがボトルネックになっている可能性がある。

# 各リソースの調査方法

## CPU 使用率

## メモリ使用率

## ディスク I/O

## ネットワークコネクション数

### Too many open files

- ファイルディスクリプタの不足
- `cat /proc/1234/limits`のようにプロセスが開けるファイル数上限を調べられる

### Ephemeral port の不足

```bash
$ cat /proc/sys/net/ipv4/ip_local_port_range
32768	60999
```

→ 32768〜60999の約28,000のポートが通信に使えるという意味。

```
$ netstat | grep tcp | wc -l
27194
```

→ 枯渇しかけてる？

このうち、`TIME_WAIT`（= 接続終了の最終信号を送った後、待機しているポート）が多数を占めるのであれば`tcp_tw_reuse`のフラグを設定することで回避できる可能性あり。

```bash
$ netstat | grep tcp
...
tcp        0      0 example.client.:49334 example.server.:2379 TIME_WAIT
...
```

```
$ cat /proc/sys/net/ipv4/tcp_tw_reuse
0
```


### SYNs to LISTEN sockets dropped

- 接続が多すぎて受けきれていない
- `netstat -s`で確認できる


