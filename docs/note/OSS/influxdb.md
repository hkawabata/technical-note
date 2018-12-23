---
title: InfluxDB
logo: https://user-images.githubusercontent.com/13412823/50383336-e11be780-06f4-11e9-9b0a-68aa96eb0ee0.png
---

# インストール・起動

```bash
$ wget https://dl.influxdata.com/influxdb/releases/influxdb-1.2.0_linux_amd64.tar.gz
$ tar xvzf influxdb-1.2.0_linux_amd64.tar.gz
$ cd influxdb-1.2.0-1/
$ usr/bin/influxd run
```


# アクセス・基本操作

## CLI

```bash
$ usr/bin/influx
```

```sql
> SHOW DATABASES
name: databases
name
----
_internal

> 
> CREATE DATABASE test_db
> SHOW DATABASES
name: databases
name
----
_internal
test_db

> USE test_db
Using database test_db

> INSERT serverstat,host=node001.hkawabata.jp,region=jp cpu=0.3,memory=0.4
> INSERT serverstat,host=node001.hkawabata.jp,region=jp cpu=0.4,memory=0.8
> INSERT serverstat,host=sample.com,region=us cpu=1.0,memory=0.7

> SHOW MEASUREMENTS
name: measurements
name
----
serverstat

> SELECT * FROM serverstat
name: serverstat
time                cpu host                 memory region
----                --- ----                 ------ ------
1545561850303234279 0.3 node001.hkawabata.jp 0.4    jp
1545562024137251309 0.4 node001.hkawabata.jp 0.8    jp
1545562065544289591 1   sample.com           0.7    us

> DELETE FROM serverstat
> DELETE FROM serverstat WHERE region = 'jp'
> DELETE WHERE time < '2017-02-25 09:10:00'
```

- テーブルを作る必要がないっぽい。
- INSERT 文の構文は、`INSERT <measurement>,<tag_key1>=<tag_value1>,...,<tag_keyN>=<tag_valueN> <field_key1>=<field_value1>,...,<field_keyN>=<field_valueN> [タイムスタンプ]`
- time は世界標準時で指定する必要がある

## REST API

```bash
$ curl http://localhost:8086/query --data-urlencode "q=CREATE DATABASE test_db"
{"results":[{"statement_id":0}]}

$ curl -i -XPOST 'http://localhost:8086/write?db=test_db' --data-binary 'serverstat,host=node001.hkawabata.jp,region=jp cpu=0.6,memory=1.2 1545562127000000000'
HTTP/1.1 204 No Content
Content-Type: application/json
Request-Id: 3c1a1ec5-06a1-11e9-8025-000000000000
X-Influxdb-Version: 1.2.0
Date: Sun, 23 Dec 2018 10:55:17 GMT

$ curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=test_db" --data-urlencode "q=SELECT cpu FROM serverstat WHERE region='jp'"
{
    "results": [
        {
            "statement_id": 0,
            "series": [
                {
                    "name": "serverstat",
                    "columns": [
                        "time",
                        "cpu"
                    ],
                    "values": [
                        [
                            "2018-12-23T10:44:10.303234279Z",
                            0.3
                        ],
                        [
                            "2018-12-23T10:47:04.137251309Z",
                            0.4
                        ],
                        [
                            "2018-12-23T10:48:47Z",
                            0.6
                        ]
                    ]
                }
            ]
        }
    ]
}
```

# Retention Policy

書き込んだデータを何日で削除するか、などの設定

```sql
> CREATE RETENTION POLICY <retention_policy_name> ON <database_name> DURATION <duration> REPLICATION <n> [SHARD DURATION <duration>] [DEFAULT]
```

| 指定項目 | 説明 |
| :-- | :-- |
| `DURATION` | 登録されてからデータが削除されるまでの時間（TTL）。ver1.2の時点では1h以上でないといけない。最大は INF |
| `REPLICATION` | レプリケーション数 |
| `SHARD DURATION` |  |
| `DEFAULT` | 引数を取らない。このポリシーをデフォルトにする（使用する） |

例：
```sql
> USE test_db

> SHOW RETENTION POLICIES
name    duration shardGroupDuration replicaN default
----    -------- ------------------ -------- -------
autogen 0s       168h0m0s           1        true

> CREATE RETENTION POLICY hour_delete ON test_db DURATION 1h REPLICATION 1
> CREATE RETENTION POLICY day_delete ON test_db DURATION 1d REPLICATION 1
> CREATE RETENTION POLICY week_delete ON test_db DURATION 7d REPLICATION 1

> SHOW RETENTION POLICIES
name        duration shardGroupDuration replicaN default
----        -------- ------------------ -------- -------
autogen     0s       168h0m0s           1        true
hour_delete 1h0m0s   1h0m0s             1        false
day_delete  24h0m0s  1h0m0s             1        false
week_delete 168h0m0s 24h0m0s            1        false
```

`autogen`が default になっているので、作成したポリシーを有効化。

```
> ALTER RETENTION POLICY hour_delete ON test_db DEFAULT
> SHOW RETENTION POLICIES
name        duration shardGroupDuration replicaN default
----        -------- ------------------ -------- -------
autogen     0s       168h0m0s           1        false
hour_delete 1h0m0s   1h0m0s             1        true
day_delete  24h0m0s  1h0m0s             1        false
week_delete 168h0m0s 24h0m0s            1        false
```

- 削除：`DROP RETENTION POLICY <policy_name> ON <db_name>`
- 変更：`ALTER RETENTION POLICY <policy_name> ON <db_name> ...`

# トラブルシューティング

## 有限の DURATION を設定したのにデータが消えない

RETENTION POLICY を変更して有限の DURATION を設定したにもかかわらず、その時間を過ぎてもデータが消えない。
設定変更前に作成したデータを壊さないように、以下のどちらかの機能が備わっている可能性が考えられる。
1. 設定変更前に挿入されたレコードには効かない
2. 設定変更前に作られた measurement のレコードには効かない

と思ったが、もうしばらく待つとちゃんと消えた。定期的に寿命かどうかチェックしており、そのサイクルが結構遅い（/10minutesとか）らしい。
