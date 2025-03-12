---
title: JavaScript の基本文法
---
# 変数の宣言


# ファイル入出力


# オブジェクト

## テキストからの読み込み

sample.json：
```json
{
  "team_id": 1,
  "team_name": "Tigers",
  "members": [
    {
      "name": "Taro",
      "age": 28
    },
    {
      "name": "Jiro",
      "age": 24
    }
  ]
}
```

```js
var obj = JSON.parse('path/to/sample.json');
console.log(obj.team_id);
console.log(obj['team_name']);
console.log(obj.members[0].name);
```


# 正規表現

```js
var r1 = new RegExp('[a-zA-Z]+');
var r2 = /^\d{3}-?\d{4}$/g;
```


# HTML 要素の操作

```html
<div>
  <p id="p1">
    <h1>paragraph 1</h1>
    This is contents of paragraph 1.
  </p>
  <p id="p2">
    <h1>paragraph 2</h1>
    This is contents of paragraph 2.
  </p>
</div>
```

## HTML 要素を取得

```javascript
let body = document.body
let p_elem = document.getElementById('p1');
let h1_elem = p_elem.getElementsByTagName('h1');
```

| メソッド                                            | 説明                                                                              |
| :---------------------------------------------- | ------------------------------------------------------------------------------- |
| `<elem>.getElementById("<id>")`                 | `id` プロパティが引数に指定した文字列と一致する要素を取得。<br>同じページには原則として同じ `id` を持つ要素は存在しないので、返り値は要素1つ。 |
| `<elem>.getElementsByClassName("<class_name>")` | `class`プロパティが引数に指定した文字列と一致する要素の配列を取得。                                           |
| `<elem>.getElementsByTagName("<tag_name>")`     | タグ名が引数に指定した文字列と一致する要素の配列を取得。                                                    |
| `document.body`                                 | `<body>` の取得                                                                    |


## HTML 要素の中身を書き換え

```javascript
p_elem.innerHTML = '<h1>paragraph 1 - rewritten</h1>This is rewritten contents.';
```

```javascript
h1_elem.textContent = 'Rewritten H1 Element'
```


## HTML 要素を削除

```javascript
// 全てのテーブルを削除する例
document.getElementsByTagName("TABLE").forEach(el => {
    el.remove();
});
```

## HTML 要素を新しく作成

```javascript
// テキストノード
let text = document.createTextNode("Plane text.");

// HTML タグ
let p = document.createElement("p");
p.id = "my_paragraph";
p.setAttribute();
```

## 指定した位置に要素を挿入

`appendChild, before, after, insertBefore`

```javascript
let parent = document.createElement("div");
let child1 = document.createElement("p");
child1.textContent = "aaaaa";
let child2 = document.createElement("p");
child2.textContent = "bbbbb";
parent.appendChild(child1);
```

```html
<div>
  <p>aaaaa</p>
  <p>bbbbb</p>
</div>
```


## HTML 要素の中身だけを残す

```html
<html>
  <body>
    <p id="my-p">
      <b>Bold text</b><br>
      This is sententce.
    </p>
    ...
  </body>
</html>
```

```javascript
function unwrap(elem) {
    // すべての子要素を取り出して前に置く
    while (elem.firstChild) {
        elem.parentNode.insertBefore(elem.firstChild, elem);
    }
    // 空になった親要素を削除する
    elem.remove();
}

let p = document.getElementById("my-p");
unwrap(p);
```

実行結果：

```html
<html>
  <body>
    <b>Bold text</b><br>
    "This is sententce."
  </body>
  ...
</html>
```