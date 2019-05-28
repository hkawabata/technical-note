---
title: gnuplot
---

参考：
http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/average.html

## 1. インストール

XQuartz（X11を利用するソフトウェアをMacOSXで動作させるために必要なソフト）をあらかじめ[公式ページ](https://xquartz.macosforge.org)からダウンロード・インストールしておく（そうでないとグラフを画面出力できない）。

**※一度PCを再起動しないとgnuplotとうまく連携しないかも。**

```bash
brew install gnuplot --with-x11
```


## 2. 文法

### 各フィールドの名称

![](https://user-images.githubusercontent.com/13412823/58454521-4180dc00-810e-11e9-96e3-519d4a5ac279.png)

### プロット時に指定できるオプション

```
plot x with line lw 2 lc 4 title "aaa"
```

| 内容 | 表記 | 備考 |
| :--- | :--- | :--- |
| 線の種類 | `with line`,<br>`with point`,<br>`with linespoints` | それぞれ線のみ、点のみ、点・線両方で描画。 |
| 線の太さ | `lw 2` |
| 点のサイズ | `ps 1` |
| 点の種類 | `pt 3` | 番号ごとに決まった形がある |
| 凡例(key) | `title "hoge"`,<br>`notitle` |
| 線の色 | `lc 3` | 番号ごとに決まった色がある |

### ファイルから読み込んだ数値のプロット

タブやスペース区切りのデータを読み込んでプロットする。

```
plot "filename"
```

ファイルのデータが3列以上ある場合、指定しなければ1,2列目が


### 軸のラベル

```
set xlabel "xlabel"
set ylabel "ylabel"
```

### 任意の箇所のラベル

```
set label 1 at graph 0.5,0.5 "label 1"
```

### 凡例

#### 凡例の位置

```
# 座標で指定
set key <x>,<y>
# オプションで指定（上下左右）
set key <{left|right} {top|bottom}>
# オプションで指定（図の右側の外）
set key outside
# オプションで指定（図の下側の外）
set key below
```

### multiplot

### グラフの出力先を設定

```
set terminal <outputformat>
set output "<filename>"
```

### 文字サイズ・フォント

```
set <parameter> font "<font>,<size>"
```

のように指定する。以下の例のように、他の項目と同時にセットしても良い。

```
# x軸のラベル文字列とフォント・サイズを同時に設定
set xlabel "sample_x" font "Helvetica,12"
```

フォントを指定可能なパラメータ

- 軸のラベル (xlabel, ylabel etc.)
- 軸の数値 (xtics, ytics, etc.)
- 凡例 (key)
- グラフのタイトル (title)

指定可能なフォント

- Helvetica
- Times-Roman
- ...

### 描画範囲の指定

```
# 上限・下限を指定
set xrange [<bottom>:<top>]
# 上限のみを指定
set xrange [:<top>]
# 下限のみを指定
set xrange [<bottom>:]
```

### 目盛りの刻み幅

#### 大目盛

```
# 大目盛の刻み幅を2に
set xtics 2
```

#### 小目盛

### グリッド

```
set grid [options]
```

指定できるオプション：

|オプション|意味|
|:-|:-|
|`linetype / lt`|線の種類|
|`linewidth / lw`|線の太さ|
|`{x\|y\|z}tics`|指定軸のみグリッドを表示|
|`m{x\|y\|z}tics`|指定軸のみグリッドを表示|


### 左右（上下）で別の軸を使用

```
set
```

### 変数や関数を定義

### 3次元プロット

### パラメータ fitting

### エラーバー

## 3. Tips

### 表記の省略

gnuplot では、予約語文字列がただ1つに特定できるまで書けばそれ以降は必要ない。以下の２つのコマンドは同じ。

- 元のコード

```
set terminal jpeg
set output "image.jpg"
set xlabel "sample_x"
plot x**3 with line
```

- 省略コード

```
se term jpeg
se ou "image.jpg"
se xl "sample_x"
p x**3 w l
```

### コマンドファイルを読み込む

gnuplot のコマンドを記述した sample.plt を

- ターミナルから読み込んで実行

```bash
$ gnuplot sample.plt
```

- gnuplot コンソールから読み込んで実行

```bash
gnuplot> load "sample.plt"
```

### 複数の命令を1行に記述

`;`で複数の命令を区切れる。

```
set xl "x_label"; set yl "y_label"; plot x**2
```

### 複数行の命令を記述

行末に`\`をつければ、複数行にわたる命令を記述できる。

```
plot x w l lc 1 title "x",\
x**2 w l lc 2 title "x^2",\
x**3 w l lc 3 title "x^3"
```

### 同じ x の値で平均をとる

```
plot "hogehoge.txt" u 1:2 smooth unique
```

x が離散値をとる場合はこれで良いが、連続値をとる場合には先に値を丸めておく必要がある。

```
# 一番近い整数に丸める関数
nearint(x)=(x - floor(x) <= 0.5 ? floor(x) : floor(x)+1)
# yの整数倍に丸める関数
filter(x,y)=nearint(x/y)*y
# 0.05 区切りで平均を取ってプロット
plot "hogehgoe.txt" u (filter($1,0.05)):2 smooth unique
```

### 時刻表記のデータを読み込む

以下のようなデータを使い、軸が日付になるようなグラフが描きたい

```
2017/03/23 18:55:18	995	8.993358
2017/03/23 18:55:19	1037	8.598015
2017/03/23 18:55:20	1018	8.774249
2017/03/23 18:55:21	1041	8.555087
2017/03/23 18:55:22	1045	8.546441
2017/03/23 18:55:23	1050	8.495757
2017/03/23 18:55:24	1050	8.489656
2017/03/23 18:55:25	1037	8.560051
2017/03/23 18:55:26	1046	8.521292
```

方法：

```
set xdata time

# 読み込み形式
set datafile separator '\t'
set timefmt "%Y/%m/%d %H:%M:%S"

# 書き込み形式
set format x "%H:%M:%S"

plot ["2017/01/01 00:00:00":"2017/01/02 00:00:00"] "hoge.dat" w l
```

`set xtics 30`などとすれば目盛り間隔を秒数で指定できる

### 背景に色をつける（長方形型）

長方形のオブジェクトを裏側（back）に置くことで実現できる

```
set object 1 rect from 0, -5 to 4, 5 back fillcolor rgb "cyan" fill solid 0.5
p [][-5:5] x, x**2, cos(x)
```

![](https://user-images.githubusercontent.com/13412823/58454523-4180dc00-810e-11e9-9b15-288d3e4efc0e.png)


範囲に限らず、グラフ全体の背景を変えたい場合は絶対座標ではなくグラフ内の相対座標（graph x, graph y）を使って (graph 0, graph 0), (graph 1, graph 1) を始点・終点に指定する

```
set object 1 rect from graph 0, graph 0 to graph 1, graph 1 back fillcolor rgb "red" fill solid 0.3
p [][-5:5] x, x**2, cos(x)
```

![](https://user-images.githubusercontent.com/13412823/58454524-4180dc00-810e-11e9-9861-4b60c0dd235f.png)


### 累積グラフ

`smooth cumulative`を使う。

```bash
# sample.dat
0 3
1 12
2 145
3 128
4 64
5 4
6 2
7 80
8 174
9 31
10 5
```

```
plot "sample.dat" w p ps 2, "sample.dat" smooth cumulative
```

![](https://user-images.githubusercontent.com/13412823/58454525-42197280-810e-11e9-95a6-f34475d24d04.png)


## トラブルシューティング
### plot してもエラーじゃないのに何も出ない
と思ったら、グラフのウインドウが画面の外に行ってしまっていた。Gnuplot が、x11 の画面を出す原点の位置を画面外に設定してしまっているために起こるとのこと。


ミッションコントロールをいじる。システム環境設定の "Mission Control" で「ディスプレイごとに個別の操作スペース」のチェックを外すと解決。

> You can work around this by turning off "Displays have different spaces" in Mission Control preferences, but the fix will require a change in OS X.
