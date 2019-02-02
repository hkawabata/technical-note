---
title: mat - Eclipse Memory Analyzer
---

# ダウンロード

https://eclipse.org/mat/ から mat.app がダウンロードできる。

# ヒープダンプとは

JVM が JVM Heap を使い切った時や JVM がクラッシュしたとき、あるいはユーザが明示的に命令を送った時に生成されるダンプファイル。

## 得られる情報

- JVM Heap 内のオブジェクトのアドレス、サイズ、タイプ
- そのオブジェクトが参照するオブジェクトのアドレス

## 生成のタイミング

- 障害時の自動生成
	- JVM の異常終了
	- OutOfMemoryError
- ユーザの命令
	- SIGQUIT
		- `kill -3 <pid>`
		- `kill -QUIT <pid>`
	- アプリケーション内から明示的に出力させる API（`com.ibm.jvm.Dump.JavaDump()`）

## 出力先

Linux の場合は /tmp？

# ヒープダンプの取得

## OutOfMemoryError 発生時のヒープダンプ

JVM の起動オプションに`-XX:-HeapDumpOnOutOfMemoryError`を指定すると、OutOfMemoryError 発生時に java_pid9999.hprof のような形式のヒープダンプファイルを自動生成してくれる。

## 実行中アプリケーションのヒープダンプ

1. `jps -v`とか`ps aux | grep java`とかでアプリケーションのプロセス ID を取得
2. `jmap`でヒープダンプ出力（アプリケーションにも依るのかもしれないが、Spark のヒストリーサーバのプロセスで試した時は終わるまで数分かかった）

```bash
$ ps aux | grep java
hoge   15632  0.2  0.4 2977968 611336 ?      Sl   Jul03   5:59 /usr/lib/jvm/default-java/bin/java ...

$ jmap -F -dump:format=b,file=heapdump.hprof 15632
Attaching to process ID 15632, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.131-b11
Dumping heap to heapdump.hprof ...
Heap dump file created
```

**【注1】**`jps`コマンドは実行ユーザとして（`sudo -u <user> jps ...`）叩く必要がある。

**【注2】**`jmap`に`-F`をつけないと`well-known file is not secure`とか言われて失敗した。

**【注3】** アプリケーションの実行ユーザ（上の例では hoge）で実行しないと`cannot open binary file`とか言われて失敗した。`sudo -u hoge`をつけると通った。


# ダンプの解析

- 「File」>「Open Heap Dump」でダンプファイルを開くだけ
※ ダンプファイルと同じディレクトリに多数の解析ファイルが生成されるので注意

![20170707_mat_overview](https://user-images.githubusercontent.com/13412823/44305237-a3592c00-a3ad-11e8-9c6e-1b5e6795dcda.png)

- メモリリークが疑われる場合は、ダンプを開くと出てくるウインドウで「Leak Suspects Report」をチェックして「finish」とするとメモリリークが疑われる箇所の解析もしてくれる

![20170703_mat01](https://user-images.githubusercontent.com/13412823/44305230-a227ff00-a3ad-11e8-93fa-61df66f1616b.png)

![20170707_mat_leak_suspect](https://user-images.githubusercontent.com/13412823/44305236-a2c09580-a3ad-11e8-9ac4-d47be93a31c4.png)

画像下部「See stacktrace」から、OutOfMemoryError が発生しているのが確認できる。

```bash
qtp322830747-143373
  at java.lang.OutOfMemoryError.<init>()V (OutOfMemoryError.java:48)
  at scala.collection.mutable.ListBuffer.$plus$eq(Ljava/lang/Object;)Lscala/collection/mutable/ListBuffer; (ListBuffer.scala:164)
  at scala.collection.mutable.ListBuffer.$plus$eq(Ljava/lang/Object;)Lscala/collection/generic/Growable; (ListBuffer.scala:45)
  ...
```

# メモリリーク問題の調査戦略

## 1. ヒープ中を占める割合が大きいオブジェクトを見つける

ヒープダンプを1度取得して中身を見る。
ただし、キャッシュなど必要があって確保している場合もある。

- **Dominator Tree** を使うと、メモリ上のインスタンスのツリーの画面が開き、これを辿っていくとオブジェクトが保有するフィールドやその値などが確認できる。

![20170707_mat_dominator_tree](https://user-images.githubusercontent.com/13412823/44305234-a2c09580-a3ad-11e8-9bd3-06417ebf6dc4.jpg)

![20170707_mat_dominator_tree2](https://user-images.githubusercontent.com/13412823/44305235-a2c09580-a3ad-11e8-9226-2ae28910e9bf.png)

右クリックで、オブジェクトの中身をファイルに保存することもできる。

![20170707_mat_dominator_tree_save_object](https://user-images.githubusercontent.com/13412823/44305233-a2c09580-a3ad-11e8-95cd-05da3f54e550.png)

以下は aaa.txt という名前でホームディレクトリに保存したファイルの中身。

```bash
$ cat ~/aaa.txt
/var/run/cloudera-scm-agent/process/18780-spark_on_yarn-SPARK_YARN_HISTORY_SERVER/spark-conf/:/opt/cloudera/parcels/CDH-5.8.2-1.cdh5.8.2.p0.3/lib/spark/lib/spark-assembly-1.6.0-cdh5.8.2-hadoop2.6.0-cdh5.8.2.jar:/var/run/cloudera-scm-agent/process/18780-spark_on_yarn-SPARK_YARN_HISTORY_SERVER/yarn-conf/:/etc/hive/conf/:...
```

オブジェクトを保存した場合、`org.apache.spark.ui.scope.RDDOperationGraphListener @ 0xe72b9ba8`のような内容が保存される（`toString`を実装しているかどうかの違い？）。


## 2. アプリケーションの動作過程で単調増加し続けるオブジェクトを見つける

時間を置いて複数回ヒープダンプを取得し、オブジェクトのインスタンス数や使用メモリの差分を見る。

1. 比較したいダンプファイル2つを開く
2. どちらか一方のタブで、Overview かツールバーのアイコンから Histogram を開く
3. ツールバーの「Compare to another Heap Dump」をクリックし、比較対象のダンプを選択。

![20170707_mat_compare_two_dumps](https://user-images.githubusercontent.com/13412823/44305231-a227ff00-a3ad-11e8-8314-d8a4020f6bf1.png)

![20170707_mat_compare_two_dumps2](https://user-images.githubusercontent.com/13412823/44305232-a227ff00-a3ad-11e8-90ed-b49227f7c39e.png)

# 参考ページ

- 公式サイト：https://eclipse.org/mat/

