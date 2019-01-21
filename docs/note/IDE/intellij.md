---
title: IntelliJ
---

参考にしたページ：
- [IntelliJ IDEA クイックスタート](http://samuraism.com/products/jetbrains/intellij-idea/quickstart)

# IntelliJ について

Java, Scala の IDE... と思いきや、Web 開発に必要な環境も整っている。


# インストール・初期設定

## インストール

[公式サイト](http://www.jetbrains.com/idea/download/index.html)から dmg パッケージをダウンロードして開き、アプリケーションフォルダに IntelliJ をドラッグ&ドロップ

## 初期設定

### 初回起動時の設定

Featured plugins の画面で Scala をインストール（後で設定することも可能）。

### 初期設定

- **【必須】JDK の指定**
スタート画面で `Configure > Project defaults > Project structure` としてから JDK を指定。
- **行番号の表示**
`Configure > Preference > Editor > General > Appearance`で show line numbers をチェック
- 色・フォントの設定
  1. まず自分用の設定を作る。
     `Configure > Preference > Editor > Colors & Fonts`の上部で`Save As`を選択すると、デフォルトの色・フォント設定のコピーを自分用設定として保存できる。
  2. これを好きにカスタマイズして Apply すれば完了。
     シンタックスチェックの色などはデフォルトが目立たないので設定しておくべき。


## プロジェクト作成

プロジェクト名を選ぶ画面で Use auto-import にチェックを入れると…？

## build.sbt を変更したら・・・

build.sbt の編集画面右上に出る refresh project をクリックする。これでライブラリ依存性が解決される。
※ オートでリフレッシュする設定もある。プロジェクト作成時にチェックをつけるか、refresh project ではなく enable auto-import をクリックする。

## Git との連携
生成したプロジェクトのルートディレクトリに Git の設定ファイルがあれば勝手に検知してくれる。



# 設定もろもろ

Preference からイロイロ設定できる。

## ファイル末尾に改行を入れる

Preference > Editor > General > Other > Ensure line feed at file end on Save


# ショートカットキー

## 編集関係

|ショートカット|説明|備考|
|:-|:-|:-|
|Alt + Enter|エラーや警告の箇所でクイックフィックス|
|Cmd + Shift + V|コピー履歴から選択して貼り付け|
|Cmd + V|貼り付け|
|Ctrl + K|カーソル位置から行末まで切り取り|
|Shift + カーソルキー|部分選択（ドラッグと同じ）|
|Alt + Shift + ↑/↓|カーソルのある行を上下に移動（インデントはそのまま）|
|Cmd + Shift + ↑/↓|カーソルのある行（メソッドなどが複数行にわたってくっついているときはその終わりまで）を上下に移動（新しい位置での適切なインデントに変更）|
|（文字列を選択してから）<br>Ctrl + G|同じ文字列に対するマルチカーソル。一度押すごとに、選択文字列と同じ文字列のうち後方直近のものの位置にカーソルが出る。<br>→ 同時に同じ文字列を編集するときに使える。|同じ変数ではなく、同じ文字列。つまり、同じパターンを含む別の変数やコメント内の文字列にも適用される。|
|Alt + ドラッグ|複数行にわたるマルチカーソル。ドラッグした範囲の各行にカーソルが出る。|
|Cmd + Alt + L|コードをフォーマットする（インデントを直す）|
|Cmd + Alt + T|選択箇所を if や while, for, try/catch などで囲む|
|Cmd + Alt + M|選択部分をメソッドとして切り出す|選択範囲で使われている変数の中に、範囲外で宣言されたものがあった場合は、それを引数として受け取るメソッドが切り出される|
|Cmd + Alt + F|カーソル位置にある値をフィールドとして宣言に切り出す|
|Cmd + Shift + R|文字列の一斉置換||


## 画面の表示

|ショートカット|説明|備考|
|:-|:-|:-|
|Cmd + E|最近開いたファイルを表示|
|Cmd + =|カーソル位置にある import 文、複数行に渡る関数引数、クラスや関数の実装部分、制御文の中身、コメントなどを畳んで`...`で表示する|
|Cmd + Shift + =|コード全体の畳める箇所を全て畳む|
|Cmd + num|num 番のウインドウ（1ならプロジェクト、7ならストラクチャ、など）の表示/非表示を切り替え|

## 検索・移動

|ショートカット|説明|備考|
|:-|:-|:-|
|Alt + →/←|単語単位のカーソル移動|
|Cmd + →/←|行末/行頭へのカーソル移動|
|Cmd + F|文字列検索|
|Cmd + Shift + F|ファイル横断文字列検索|
|Shift 2回|どこでも検索（クラス名や関数名、ファイル名）|選択するとそこへジャンプできる。依存ライブラリの中へも飛べるので、**ライブラリにあるクラスや関数の実装を見たいときなどにも使える**。|
|Ctrl + Alt + H|メソッド（フィールドも？）の呼び出し先を調べる|
|Cmd + B|変数やクラス、関数の宣言へ飛ぶ|**外部の依存ライブラリの中へも飛べる**。|
|Cmd + Alt + B|Scala のトレイトや Java のインターフェースの実装クラスへ飛ぶ|複数ある場合は選択できる|
|Ctrl + h|型の継承階層を表示|
|Cmd + B|変数やクラス、関数の宣言へ飛ぶ|**外部の依存ライブラリの中へも飛べる**。|
|Alt + Space||
|Cmd + Alt + B|Scala のトレイトや Java のインターフェースの実装クラスへ飛ぶ|複数ある場合は選択できる|


# Tips

## 困ったら Option + Enter

## postfix コード補完

= ***postfix code complition***

- 式の最後に`.var`をつけることで変数宣言を補完できる。
- Boolean の後に`.if`で if 文補完
- イテレータの後に`.for`で要素による for 文補完
- 例外の後に`.throw`で throw 文補完

## 定型文の短縮表現

- `psvm` = `public static void main`
- `fori`

## IntelliJ で Web 開発

IntelliJ は HTML, CSS, JavaScript, PHP をサポートする。
Live Edit というリアルタイムビューアがあるが、**有料版限定？**

### Live Edit

- Chrome に機能拡張（JetBrains IDE Support）をインストール

![](https://user-images.githubusercontent.com/13412823/48967305-bf5e1080-f021-11e8-8819-20e1ababde72.png)

- プラグインを有効化

![](https://user-images.githubusercontent.com/13412823/48967307-bf5e1080-f021-11e8-8e50-c71dfd410127.png)

- IntelliJ 上で対象ファイルを右クリック >「Debug <ファイル名>」
	- これで自動で Chrome が立ち上がる

![](https://user-images.githubusercontent.com/13412823/48967308-bff6a700-f021-11e8-9c3f-aeec79d8aaa5.png)


### JS ライブラリのダウンロード

Preference > Languages & Frameworks > JavaScript > Libraries > Download

![](https://user-images.githubusercontent.com/13412823/48967310-bff6a700-f021-11e8-92d2-8c9000afabee.png)


# トラブルシューティング

## Error:Cannot determine Java VM executable in selected JDK（プロジェクト作成時）

JDK が指定されていないのが原因。
- スタート画面で `Configure > Project defaults > Project structure` としてから JDK を指定。
- または、そのプロジェクトを右クリックして `Open Module Settings > Project > Project SDK` として JDK を指定する。


## FAILED DOWNLOADS（プロジェクト作成時）


```
11:47:07 SBT project import
         [warn]  [FAILED     ] org.scala-sbt#compiler-interface;0.13.8!compiler-interface.jar(src):  (0ms)
         [warn] ==== typesafe-ivy-releases: tried
         [warn]   https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/compiler-interface/0.13.8/srcs/compiler-interface-sources.jar
         [warn] ==== sbt-plugin-releases: tried
         [warn]   https://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/org.scala-sbt/compiler-interface/0.13.8/srcs/compiler-interface-sources.jar
         [warn] ==== local: tried
         [warn]   C:\Users\hogehoge\.ivy2\local\org.scala-sbt\compiler-interface\0.13.8\srcs\compiler-interface-sources.jar
         [warn] ==== public: tried
         [warn]   https://repo1.maven.org/maven2/org/scala-sbt/compiler-interface/0.13.8/compiler-interface-0.13.8-sources.jar
         [warn]  ::::::::::::::::::::::::::::::::::::::::::::::
         [warn]  ::              FAILED DOWNLOADS            ::
         [warn]  :: ^ see resolution messages for details  ^ ::
         [warn]  ::::::::::::::::::::::::::::::::::::::::::::::
         [warn]  :: org.scala-sbt#compiler... (show balloon)
```

compiler-interface.jar は、sbt コマンド実行時に作成されるらしいので、とりあえず無視してOK。

## import 時に "cannot resolve symbol"

pom.xml の dependencies に追加したライブラリをインポートすると IntelliJ 上で "cannot resolve symbol" と出て import できない。無視してコンパイルすると通る。
→ IntelliJ が認識できていない

**【解決】**

まず、調べて出てきた File > Invalidate Caches/Restart を実行。

これでは解決しなかったが、restart した直後のフローティングウィンドウに **"unmanaged pom.xml"** という文言が。pom.xml が認識されない状態になってた？ そこの "add project" を押すと解決した。

これでもダメだったときは、.idea ディレクトリを削除してから Invalidate Caches/Restart で解決した。


## src/test ディレクトリが作られない

maven プロジェクトを開いた際、src/test ディレクトリが作られない。手動で作っても test ディレクトリとは認識されないのか、「new package」がメニューから選択できない。

**【解決】**

File > Project Structure > Modules の Sources タブで、「このディレクトリがテストディレクトリだ」と登録できる。src/test ディレクトリ自体は自分で作る必要があるっぽい。
