---
title: HttpFS
---

（書きかけの項目）

# とりあえず動かしてみる

## Hadoop を動かす

スタンドアローンで動かす場合も自分への ssh ログインが必要なようなので、`-A`オプション付きでログイン

```bash
$ ssh -A dev001.hkawabata.jp
```

```bash
$ sudo yum install java-1.8.0-openjdk
$ sudo yum install java-1.8.0-openjdk-devel

$ wget http://ftp.jaist.ac.jp/pub/apache/hadoop/common/hadoop-2.9.2/hadoop-2.9.2.tar.gz
$ tar xvzf hadoop-2.9.2.tar.gz
$ cd hadoop-2.9.2
```

etc/hadoop/core-site.xml を編集：

```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000/</value>
  </property>
</configuration>
```

```bash
$ bin/hdfs namenode -format
$ sbin/start-dfs.sh
$ jps
9428 SecondaryNameNode
9239 DataNode
9096 NameNode
9561 Jps

$ bin/hdfs dfs -mkdir /user
$ bin/hdfs dfs -mkdir /user/hkawabata
$ bin/hdfs dfs -mkdir /user/hkawabata2
$ bin/hdfs dfs -chown hkawabata2:hkawabata2 /user/hkawabata2

$ bin/hdfs dfs -ls /user
Found 2 items
drwxr-xr-x   - hkawabata  supergroup          0 2019-12-03 17:46 /user/hkawabata
drwxr-xr-x   - hkawabata2 hkawabata2          0 2019-12-03 17:48 /user/hkawabata2
```

## HttpFS を動かす

HDFS を停止：

```bash
$ sbin/stop-dfs.sh
```

etc/hadoop/core-site.xml を編集：

```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000/</value>
  </property>
  <property>
    <name>hadoop.proxyuser.hkawabata.hosts</name>
    <value>*</value>
  </property>
  <property>
    <name>hadoop.proxyuser.hkawabata.groups</name>
    <value>*</value>
  </property>
</configuration>
```

HDFS, HttpFS を起動：

```bash
$ sbin/start-dfs.sh
$ sbin/httpfs.sh start
```

READ: `hdfs dfs -ls`相当の操作：

```
$ curl -sS 'http://localhost:14000/webhdfs/v1/user?op=liststatus&user.name=hkawabata' | python -m json.tool
```

```json
{
    "FileStatuses": {
        "FileStatus": [
            {
                "accessTime": 0,
                "blockSize": 0,
                "group": "supergroup",
                "length": 0,
                "modificationTime": 1575362809838,
                "owner": "hkawabata",
                "pathSuffix": "hkawabata",
                "permission": "755",
                "replication": 0,
                "type": "DIRECTORY"
            },
            {
                "accessTime": 0,
                "blockSize": 0,
                "group": "hkawabata2",
                "length": 0,
                "modificationTime": 1575362882647,
                "owner": "hkawabata2",
                "pathSuffix": "hkawabata2",
                "permission": "755",
                "replication": 0,
                "type": "DIRECTORY"
            }
        ]
    }
}
```

WRITE: `hdfs dfs -mkdir`相当の操作：

```bash
$ curl -X PUT "http://localhost:14000/webhdfs/v1/user/hkawabata/tmp?op=mkdirs&permission=1777&user.name=hkawabata"
{"boolean":true}
$ bin/hdfs dfs -ls /user/hkawabata
drwxrwxrwx   - hkawabata hkawabata          0 2019-12-03 18:42 /user/hkawabata/tmp
```


# 設定

| パラメータ | 説明 |
| :-- | :-- |
| `hadoop.proxyuser.XXX.hosts` | `XXX`には HttpFS プロセスの起動ユーザを指定 |
| `hadoop.proxyuser.XXX.groups` |  |
