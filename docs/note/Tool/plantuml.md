---
title: PlantUML
---

シーケンス図、ユースケース図、クラス図、アクティビティ図、コンポーネント図、ステート図、デプロイ図、オブジェクト図などイロイロ作れる java 製ツール

http://plantuml.com/

### インストール・実行

```bash
brew install graphviz
brew install plantuml
```

記法に従ってテキストに記述したファイル（hoge.pu）を作り、以下のコマンドを叩くとテキストと同じディレクトリに画像が生成される。

```bash
$ plantuml hoge.pu
```

### 描画

#### シーケンス図

![](https://user-images.githubusercontent.com/13412823/58454105-f9ad8500-810c-11e9-8efe-734c5e059a35.png)

```
@startuml
'分類子の宣言 (何も宣言しないと participant)
box
	participant Hoge
	participant "Named\nAs Fuga" as Fuga #cyan
end box
actor Actor #red
boundary Boundary #black
control Control #yellowgreen
entity Entity #purple
database Database #pink
collections Collections #yellow

'シーケンス
Hoge -> Fuga: to participant
Hoge -> Actor: to actor
Hoge -> Boundary: to boundary
Hoge -> Control: to control
Hoge -> Entity: to entity
Hoge -> Database: to database
Hoge -> Collections: to collections
Hoge -> Hoge: to myself
Actor --> Hoge: from actor
Hoge <-> Fuga
Hoge ->x Fuga
Hoge ->o Fuga
Hoge ->> Fuga
Hoge -\ Fuga
Hoge -\\ Fuga
Hoge --\\ Fuga
Hoge -/ Fuga
Hoge -// Fuga
Hoge --// Fuga
Hoge /- Fuga
Hoge //- Fuga
Hoge //-- Fuga
Hoge \- Fuga
Hoge \\- Fuga
Hoge \\-- Fuga
Hoge -[#red]> Fuga
Hoge -[#cyan]->o Fuga
Hoge <[#blue]-> Fuga

autonumber
Hoge -> Actor : 自動で
Actor <- Boundary : 番号が
Boundary <-> Control : 増える
Control --> Entity

autonumber 15 4
Hoge -> Actor
Hoge -> Boundary : 15 から
Hoge -> Control : 4 ずつ
Hoge -> Entity : 増える

autonumber 4 "<u>request-000</u>"
Fuga -> Boundary
Fuga -> Control : HTML タグ使用可
Fuga -> Entity : "000" のように桁数指定

'一時停止
autonumber stop
Hoge -> Fuga

'再開
autonumber resume
Fuga -> Database

autonumber stop


'ライフライン
activate Hoge
Hoge -> Actor
activate Actor #cyan
Actor -> Database
activate Database #blue
Actor <- Database
deactivate Database
Hoge <- Actor
destroy Actor

Hoge -> Boundary
activate Boundary #pink
Boundary -> Boundary
activate Boundary #salmon
deactivate Boundary
Hoge <- Boundary
deactivate Boundary

deactivate Hoge

'メッセージのグルーピング
group request and response
	group request
		Actor -> Boundary
		Boundary -> Control
		activate Control
	end
	group response
		Control -> Boundary
		deactivate Control
		Boundary -> Actor
	end
end

'メッセージの注釈
Hoge -> Fuga
note right #pink: right\ncomment
Hoge <- Fuga
note left
	<font color="red">left
	<b>comment
end note
note over Hoge: over Hoge
note over Hoge, Actor #yellowgreen: over Hoge, Actor
note right of Hoge: note right\nof Hoge
hnote left of Hoge: hnote left\nof Hoge\n(hexagon)
rnote over Hoge: rnote over Hoge\n(rectangle)

'遅延・コメント付き遅延
...
... <font size="30"><b>long delay ...
...
...
Hoge -> Entity
...
...

'境界線
== Initialization ==

'間隔（ピクセル数指定も可能）
Hoge -> Boundary
|||
Hoge -> Boundary
|||
|||
Hoge -> Boundary
|||
|||
|||
Hoge -> Boundary
||100||
Hoge -> Boundary

'分類子の生成
create Tom
Entity -> Tom
create database DB2 #red
Entity -> DB2

'インとアウト
Database ->] : out
Database <-] : in
[<- Actor : out
[-> Actor : in

'ステレオタイプとスポット
create Piyo << (C,#ADD1B2) Generated >>
Entity -> Piyo

'フッター削除
hide footbox

@enduml
```

こういうのも指定すると面白そう。

```
@startuml
skinparam backgroundColor #EEEBDC
skinparam handwritten true

skinparam sequence {
	ArrowColor DeepSkyBlue
	ActorBorderColor DeepSkyBlue
	LifeLineBorderColor blue
	LifeLineBackgroundColor #A9DCDF
	
	ParticipantBorderColor DeepSkyBlue
	ParticipantBackgroundColor DodgerBlue
	ParticipantFontName Impact
	ParticipantFontSize 17
	ParticipantFontColor #A9DCDF
	
	ActorBackgroundColor aqua
	ActorFontColor DeepSkyBlue
	ActorFontSize 17
	ActorFontName Aapex
}

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoWork
activate A

A -> B: Create Request
activate B

B -> C: DoWork
activate C
C --> B: WorkDone
destroy C

B --> A: Request Created
deactivate B

A --> User: Done
deactivate A

@enduml
```

### Atom との連携

- Atom > Preference > Install > "plantuml-viewer"
- 文法に従って何か記述
- `Ctrl + Opt + p`でプレビュー起動

よくわからないエラーが出てうまく preview されなかった。

出たメッセージによると既に報告済みのエラーとのことなので、[エラーメッセージに書かれていたリンク](https://github.com/atom/find-and-replace/issues/898)を見たところ、Atom 再起動で直ったとのことなのでやってみたところ、表示はマトモになったが別？のエラーが。

![](https://user-images.githubusercontent.com/13412823/58454106-fa461b80-810c-11e9-8b9e-8ba7b889a069.png)


```
Uncaught TypeError: Cannot read property 'getRelativeZoom' of undefined
/Users/hkawabat/.atom/packages/plantuml-viewer/node_modules/svg-pan-zoom/src/svg-pan-zoom.js:349
Hide Stack Trace
TypeError: Cannot read property 'getRelativeZoom' of undefined
    at SvgPanZoom.getRelativeZoom (/Users/hkawabat/.atom/packages/plantuml-viewer/node_modules/svg-pan-zoom/src/svg-pan-zoom.js:349:23)
    at Object.getZoom (/Users/hkawabat/.atom/packages/plantuml-viewer/node_modules/svg-pan-zoom/src/svg-pan-zoom.js:708:40)
    at updatePanZoom (/Users/hkawabat/.atom/packages/plantuml-viewer/lib/plantuml-viewer-view.js:134:32)
    at /Users/hkawabat/.atom/packages/plantuml-viewer/lib/plantuml-viewer-view.js:52:7
The error was thrown from the plantuml-viewer package. This issue has already been reported.
```

これも報告済みらしいが、[Issue](https://github.com/markushedvall/plantuml-viewer/issues/39)が閉じてない模様。
何度か Viewer を開いたり閉じたりしていると直った。


### IntelliJ との連携

- IntelliJ IDEA > Preference > Plugins > "PlantUML integration"
- プロジェクトを開き、適当なディレクトリを右クリック > New > UML xx
- エディタと同時にプレビューが開く
