---
title: kSar
---

sar の可視化ツール

# 使い方

1. [ダウンロード](ttps://sourceforge.net/projects/ksar/)
2. 解凍ディレクトリに入り、GUI 起動
```bash
$ java -jar kSar.jar
```
3. sar を実行して結果をファイル出力 & バイナリファイルをテキストに書き出し
```bash
$ sar 1 -o sa00
...
$ sar -A -f sa00 > sa00.txt
```
4. GUI から Data > Load from text file

# （必読）注意

バージョン5.0.6時点で、グラフの単位が間違っている。`rxbyt/s`,`txbyt/s`はそれぞれ毎秒の受信**キロバイト**、送信**キロバイト**になっている。3ケタずれているので注意。

# TIPS

## 数日分の sa ファイルをまとめて kSar で見たい

ムリらしい。"kSar multiple days" とかで検索。

# トラブルシューティング

## ファイルを読み込んでもグラフが出ない

```
java.lang.NumberFormatException: For input string: "all"
	at sun.misc.FloatingDecimal.readJavaFormatString(FloatingDecimal.java:2043)
	at sun.misc.FloatingDecimal.parseFloat(FloatingDecimal.java:122)
	at java.lang.Float.parseFloat(Float.java:451)
	at java.lang.Float.<init>(Float.java:532)
	at net.atomique.ksar.Linux.Parser.parse(Parser.java:624)
	at net.atomique.ksar.kSar.parse(kSar.java:750)
	at net.atomique.ksar.FileRead.run(FileRead.java:62)
```

環境変数を変えてからテキストに書き出すと解決した。

```
$ export LC_ALL=C && export S_TIME_FORMAT=ISO
$ sar -A -f sa00 > sa00.txt
```

mac でやると変なことになった。サーバ側でテキスト書き出しまでやった方が良さそう。

```
$ sar -A -f sa00 > sa00.txt
sar: drivepath sync code error -4
```
