---
title: Prometheus
logo: https://user-images.githubusercontent.com/13412823/50383404-4fad7500-06f6-11e9-98b5-622b8b85f16b.png
---

https://prometheus.io/


# バイナリのダウンロード・起動

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



# アーキテクチャ

![](https://camo.githubusercontent.com/78b3b29d22cea8eee673e34fd204818ea532c171/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f70726f6d6574686575732f70726f6d65746865757340633334323537643036396336333036383564613335626365663038343633326666643564363230392f646f63756d656e746174696f6e2f696d616765732f6172636869746563747572652e737667)
