---
title: Grafana
logo: https://user-images.githubusercontent.com/13412823/50382776-65b53880-06ea-11e9-97ab-07d993619f0c.jpg
---

# インストール・起動

```bash
$ wget https://grafanarel.s3.amazonaws.com/builds/grafana-4.1.2-1486989747.linux-x64.tar.gz
$ tar xvzf grafana-4.1.2-1486989747.linux-x64.tar.gz
$ cd grafana-4.1.2-1486989747
$ bin/grafana-server
INFO[12-23|13:59:51] Starting Grafana                         logger=main version=4.1.2 commit=v4.1.2 compiled=2017-02-13T21:13:31+0900
INFO[12-23|13:59:51] Config loaded from                       logger=settings file=/home/hkawabata/workspace/grafana/grafana-4.1.2-1486989747/conf/defaults.ini
INFO[12-23|13:59:51] Path Home                                logger=settings path=/home/hkawabata/workspace/grafana/grafana-4.1.2-1486989747
INFO[12-23|13:59:51] Path Data                                logger=settings path=/home/hkawabata/workspace/grafana/grafana-4.1.2-1486989747/data
INFO[12-23|13:59:51] Path Logs                                logger=settings path=/home/hkawabata/workspace/grafana/grafana-4.1.2-1486989747/data/log
...
```

http://hostname:3000 にアクセスしてログイン。初期ID/Password は admin/admin。

- 「Global Users」でユーザ設定を開き、admin ユーザのユーザ名・パスワードを変更する

![2018-12-23 19 13 03](https://user-images.githubusercontent.com/13412823/50382603-d9554680-06e6-11e9-9790-5d640879d1d9.png)

# データソースの設定

「Add data source」に飛び、InfluxDB などのデータベースをデータソースとして登録する。以下は予めローカルに立てておいた InfluxDB の例。

![2018-12-23 19 17 00](https://user-images.githubusercontent.com/13412823/50382625-5f718d00-06e7-11e9-9f96-fdb94e6778ed.png)

# ダッシュボード作成

1. 「New dashboard」>「Graph」で空のグラフパネルが追加される
2. パネルをクリック >「Edit」>「Metrics」で可視化したいデータの設定を行う
3. 「Back to dashboard」>「Save dashboard」

![2018-12-23 20 44 47](https://user-images.githubusercontent.com/13412823/50383279-a5cce900-06f3-11e9-8bd2-e9919d7d3e0e.png)

InfluxDB に適当にデータを入れてみた例：

```sql
> USE test_db
> INSERT serverstat,host=sample.com,region=us cpu=1.0,memory=0.7
> INSERT serverstat,host=node001.hkawabata.jp,region=jp cpu=0.3,memory=0.4
> INSERT serverstat,host=sample.com,region=us cpu=1.1,memory=0.5
> INSERT serverstat,host=node001.hkawabata.jp,region=jp cpu=0.2,memory=0.2
> INSERT serverstat,host=sample.com,region=us cpu=0.9,memory=0.8
> INSERT serverstat,host=node001.hkawabata.jp,region=jp cpu=0.9,memory=1.3
```

![2018-12-23 20 50 32](https://user-images.githubusercontent.com/13412823/50383315-6c48ad80-06f4-11e9-8645-c8aa6c6ce132.png)
