---
title: Chrome拡張
---
cf. [Chrome Extensions API Reference (Manifest V3)](https://developer.chrome.com/docs/extensions/reference/api?hl=ja)

# 概観

## manifest.json

拡張機能の名前やバージョン、使用する JavaScript プログラムのパスや必要とするパーミッション（権限）といった情報を記しておくファイル。

cf. https://developer.chrome.com/docs/extensions/reference/manifest?hl=ja

### 主なフィールド

| フィールド                      | 説明                                                         | 値の例   |
| :------------------------- | ---------------------------------------------------------- | ----- |
| `manifest_version`         | 拡張機能で使用するマニフェストファイル形式のバージョンを指定する整数。                        | `3`   |
| `name`                     | 拡張機能を識別する名称を表す文字列                                          |       |
| `version`                  | 拡張機能のバージョン番号を識別する文字列                                       | `0.1` |
| `description`              | 拡張機能を説明する文字列。最大で 132 文字                                    |       |
| `icons`                    | 拡張機能を表す 1 つ以上のアイコン                                         |       |
| `background`               | イベントハンドラとして機能する拡張機能の Service Worker を含む JavaScript ファイルを指定 |       |
| `web_accessible_resources` | ウェブページや他の拡張機能からアクセスできる拡張機能内のファイルを定義                        |       |
| `content_scripts`          | ユーザーが特定のウェブページを開いたときに使用する JavaScript ファイルまたは CSS ファイルを指定   |       |
| `permissions`              |                                                            |       |
| `commands`                 | 拡張機能内のキーボード ショートカットを定義                                     |       |


### content_scripts



### background


### web_accessible_resources


### permissions



## Content Script

ブラウザで開いたウェブページごとに動く JavaScript ファイル。  
名称は任意で、manifest.json の `content_scripts` フィールドで指定する。

- chrome.API のうち一部しか使えない
- ページ内で定義されている変数や関数にアクセスができない（DOMにはアクセスできる）
    - → つまり、**ページ自体のスクリプトからは隔離されたスコープで動く**

```json
"content_scripts": [
  {
    "matches": ["http://www.google.com/*"],
    "css": ["mystyles.css"],
    "js": ["jquery.js", "myscript.js"]
  }
]
```

## Background Page

ブラウザで開くウェブページとは別に、バックグラウンドで動く JavaScript プログラム。  
各ウェブページで動く `content_scripts.js` との間でメッセージをやり取りできる。  
名称は任意で、manifest.json の `background` フィールドで指定する。

常にバックグラウンドで動き続けるため、**メモリを常に占有してしまうという欠点がある。**

```json
"background": {
  "service_worker": "background.js"
}
```

## Event Page

Background Page と同じようにバックグラウンドで動作するが、常に動き続ける Background Page と違い、必要な時だけ立ち上がり、動作が完了すると閉じるという性質を持つ。


# タブの操作

`chrome.tabs` API により、タブ関連の操作を行うことができる。

必要に応じて、manifest.json の `permissions` で各タブの情報（`url`、`pendingUrl`、`title`、`favIconUrl`）へのアクセスを許可しておく：

```json
{
  ...
  "permissions": [
    "tabs"
  ],
  ...
}
```

## 新しくタブを開く

```javascript
chrome.tabs.create({url: "http://..."}, (tab) => { ... })
```

第2引数には、新しく開いたタブに対して行う処理を定義した callback 関数を記述する（任意）。

 第1引数に指定できる主なパラメータ：

| パラメータ      | 説明                       | デフォルト    |
| :--------- | ------------------------ | -------- |
| `url`      | タブで開くページの URL            |          |
| `windowId` | タブを開くウインドウの ID           | 現在のウインドウ |
| `active`   | そのウインドウ内で選択されたタブにするかどうか  | `true`   |
| `index`    | そのウインドウ内で何番目の位置にタブを作成するか |          |

## ID を指定してタブを取得

```javascript
chrome.tabs.get(tabId, (tab) => { ... })
```


## 条件を満たすタブの配列を取得

`chrome.tabs.query(queryInfo: object, callback?: function)` 関数により、条件を満たすタブオブジェクトの配列を取得する。

```javascript
// 全てのタブ
let tabs = chrome.tabs.query({});
// アクティブなタブ、かつ現在のウインドウに存在
let tabs = chrome.tabs.query({active: true, currentWindow: true});
```

第二引数にコールバック関数を与えることにより、条件にヒットしたタブに対して処理を行うこともできる：

```javascript
chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
  ...
});
```


| `queryInfo`のフィールド   | 型             | 説明                                                                             |
| :------------------ | ------------- | ------------------------------------------------------------------------------ |
| `active`            | boolean       | タブがアクティブかどうか                                                                   |
| `currentWindow`     | boolean       | タブが現在のウインドウにあるか                                                                |
| `lastFocusedWindow` | boolean       | タブが最後にフォーカスされたウインドウにあるか                                                        |
| `pinned`            | boolean       | タブが固定されているか                                                                    |
| `title`             | string        | ページタイトルが文字列パターンに一致するタブを抽出。<br>manifest.json の `permissions` に `tabs` の登録が必要    |
| `url`               | array(string) | URL が文字列パターン配列のいずれかに一致するタブを抽出<br>manifest.json の `permissions` に `tabs` の登録が必要 |


## 特定のタブにメッセージを送信

`chrome.tabs.sendMessage` 関数を利用する。詳細は次節を参照。


# ウインドウの操作

## 指定したウインドウを手前に移動

```javascript
chrome.windows.update(windowId, {focused: true});
```

# メッセージの送受信

ポイント：
- `chrome.runtime.sendMessage`, `chrome.tabs.sendMessage` で送信側の処理を記述
- `chrome.runtime.onMessage.addListener` で受信側の処理を記述

manifest.json：

```json
{
  "manifest_version": 3,
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content_script.js"]
    }
  ],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "matches": ["<all_urls>"],
    "default_popup": "popup.html"
  }
}
```

## ポップアップ, 各タブから background への送受信

送信側（popup.js, content_script.js）：
```javascript
const message = {from: "content_script", key: "value"};    // 任意のオブジェクト
chrome.runtime.sendMessage(message, function(response) {
  // background から返ってきたレスポンスに対する処理を記述
  // ここでは単にコンソールに出力
  console.log(response.n);
  console.log(response.s);
  console.log(response.l);
  console.log(response.d);
});
```

受信側（background.js）：
```javascript
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.from == "content_script") {
    console.log(request.key);
    const res = {n: 10, s: request.key+"-processed", l: [1,2,3,4,5], d: {key: "value"}};
    sendResponse(res);
  }
});
```

送信側のコンソールログ：
```
10
value-processed
[1, 2, 3, 4, 5]
{key: 'value'}
```

受信側のコンソールログ：
```
value
```

> **【NOTE】**
> 
> 正確には、`chrome.runtime.sendMessage` 関数は background だけでなく、Chrome 拡張全体へ向けてメッセージを送信している。  
> そのため、様々な種類のメッセージをやり取りする Chrome 拡張の場合、受信側で「どこから送られてきたのか」「自分宛てのメッセージかどうか」などを確認できるようにメッセージオブジェクトを設計しておくと良い。


## background, ポップアップからタブへの送受信

`chrome.tabs.query` で条件を満たすタブを抽出し、そこに向けてメッセージを送ってみる。

送信側（popup.js, background.js）：
```javascript
chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
  console.log({ tabs })
  const tab_id = tabs[0].id;
  const message = {from: "popup", foo: "bar"};
  // content_script へデータを送る.
  // content_script はタブごとに存在するのでタブの ID を引数で指定
  chrome.tabs.sendMessage(tab_id, message, function (response) {
    console.log(response);
  });
});
```

受信側（content_script.js）
```javascript
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.from == "popup") {
    console.log(request.foo);
    sendResponse("OK");
  }
});
```

送信側のコンソールログ：
```
OK
```

受信側のコンソールログ：
```
bar
```


# コンテキストメニュー

右クリックの際に表示されるメニューを追加する。  
コンテキストメニューの動作は、content script ではなく、background に記述する。

manifest.json：

```json
{
  "manifest_version": 3,
  "name": "Sample Chrome Extension",
  "background": {
    "service_worker": "background.js"
  },
  "permissions": [
    "contextMenus"
  ]
}
```

background.js：

```javascript
// メニューの作成
chrome.runtime.onInstalled.addListener(() => {
  // 親子構造のメニュー項目（ページ背景を右クリックしたとき）
  chrome.contextMenus.create({
    id: 'parent',
    title: '親メニューの例'
  });
  chrome.contextMenus.create({
    id: 'child1',
    parentId: 'parent',
    title: '子メニューの例1'
  });
  chrome.contextMenus.create({
    id: 'child2',
    parentId: 'parent',
    title: '子メニューの例2'
  });
  chrome.contextMenus.create({
    id: 'grandchild',
    parentId: 'child1',
    title: '孫メニューの例'
  });

  // ラジオボタンタイプの項目
  chrome.contextMenus.create({
    id: 'radio1',
    type: 'radio',
    title: 'ラジオタイプの例1'
  });
  chrome.contextMenus.create({
    id: 'radio2',
    type: 'radio',
    title: 'ラジオタイプの例2'
  });

  // チェックボックスタイプの項目
  chrome.contextMenus.create({
    id: 'checkbox1',
    type: 'checkbox',
    title: 'チェックボックスタイプの例1'
  });
  chrome.contextMenus.create({
    id: 'checkbox2',
    type: 'checkbox',
    title: 'チェックボックスタイプの例2'
  });

  // 文章選択時に出るメニュー項目
  chrome.contextMenus.create({
    id: 'str_selected',
    contexts: ['selection'],
    title: '文章選択時に出るメニューの例'
  });
});

// メニューがクリックされたときの挙動を定義
chrome.contextMenus.onClicked.addListener((info, tab) => {
  switch (info.menuItemId) {
    case 'parent':
      ...;
      break
    case 'child1':
      ...;
      break
    case 'child2':
      ...;
      break
    ...
  }
})
```

![メニューいろいろ](https://gist.github.com/user-attachments/assets/69e5f17d-48f4-4b95-8243-9a722d9cdd23)


![文章選択時に出るメニュー](https://gist.github.com/user-attachments/assets/28d73014-3a95-42f0-bdf5-9c7cd83a870e)

