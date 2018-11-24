---
title: Vue.js
---

<img src="https://user-images.githubusercontent.com/13412823/48967150-98064400-f01f-11e8-9ffe-5fbd1c8a5af9.png" width="200">

# 基本的な使い方

## Vue インスタンスの作成

`Vue`インスタンスを作成し、セレクタで対象要素を設定する。

```javascript
new Vue ({
  // Vue インスタンスをマウントするセレクタ
  el: '#app',
  // Vue で管理するデータ
  data: {
    count: 0
  },
  // data を操作する関数
  methods: {
    countup: function(){
      this.count++;
    }
  }
})
```

html に **Mustache** 構文（二重中括弧）を利用してテキストに変数を展開できる。

```html
<div id="app">
  カウント: {{ count }}
</div>
```

#### Vue インスタンスのライフサイクル

インスタンスのライフサイクルごとに任意の処理を実行させることができる。

例：
```javascript
var sampleVue = new Vue ({
  // インスタンス作成後に呼ばれる処理を記述
  created: function() {
    console.log('Vue instance created');
  }
})
```

![](https://user-images.githubusercontent.com/13412823/48967189-195dd680-f020-11e8-8c29-dd6894b03ff4.png)

`data:`プロパティに記述した全てのプロパティはリアクティブで、更新するとビューに新しい値が反映される。

```javascript
sampleVue.$data.count++
```

## ディレクティブ

タグに Vue.js 専用の特別な（`v-`から始まる）属性を付加できる。

| ディレクティブ | 説明 |
| :-- | :-- |
| v-if, v-else | 条件を満たせば要素を表示し、満たさなければ表示しない。<br>表示しない場合、要素を DOM から消す（描画しない）。 |
| v-show | 条件を満たせば要素を表示し、満たさなければ表示しない。<br>表示しない場合も要素を DOM に残し、style の display 属性を none にする（描画はされている）。 |
| v-for | 繰り返し |
| v-on | イベントリスナをアタッチ |
| v-model | フォームをリアクティブにする |
|  |  |

### v-if, v-else, v-show

```html
<div id="app">
    <button>{{ message }}</button>
    <span v-if="message === 'ON'">ボタンが ON のときだけ表示される（v-if）</span>
    <span v-else>ボタンが OFF のときだけ表示される</span>
    <span v-show="message === 'ON'">ボタンが ON のときだけ表示される（v-show）</span>
</div>
<script>
    var app2 = new Vue({
        el: '#app',
        data: {
            message: 'OFF'
        }
    });
</script>
<script>
    document.getElementById("app2").onclick = function() {
        if (app2.message === "ON") {
            app2.message = "OFF";
        } else {
            app2.message = "ON";
        }
    }
</script>
```

### v-for

```html
<div id="app">
    <!-- リストから値を順に取り出す -->
    <ul>
        <li v-for="item in list">
            {{ item.key }}
        </li>
    </ul>
    <!-- リストからインデックス付きで値を順に取り出す -->
    <ul>
        <li v-for="(item, index) in list">
            {{ index + 1 }} - {{ item.key }}
        </li>
    </ul>
    <!-- 辞書からインデックス・キー・値を順に取り出す -->
    <ul>
        <li v-for="(val, key, index) in object">
            {{ index + 1 }} - {{ key }} - {{ val }}
        </li>
    </ul>
    <!-- 文字列から1文字ずつ取り出す -->
    <ul>
        <li v-for="(char, index) in string">
            {{ index + 1 }} - {{ char }}
        </li>
    </ul>
    <!-- 整数を1から順に取り出す -->
    <ul>
        <li v-for="(num, index) in number">
            {{ index + 1 }} - {{ num }}
        </li>
    </ul>
</div>
<script>
    new Vue({
        el: "#app",
        data: {
            list: [
                { key: "value1" },
                { key: "value2" },
                { key: "value3" }
            ],
            object: {
                key1: "value1",
                key2: "value2",
                key3: "value3"
            },
            string: "abcdefg",
            number: 7
        }
    })
</script>
```


### v-on

クリックやテキストなどのイベントに対して実行する処理を設定する。
- `v-on:click="javascript のコード"`のように属性を指定する
- `v-on:click`→`@click`のように略記もできる
- `Vue`インスタンスで`methods`を定義しておけば、メソッド名だけによる呼び出しも可能

```html
<div id="app">
    <p>{{ message }}</p>
    <input type="text" v-on:input="changeMessage">
    <button v-on:click="reverseMessage">Reverse Message</button>
</div>
<script>
    new Vue({
        el: "#app",
        data: {
            message: ""
        },
        methods: {
            reverseMessage: function() {
                this.message = this.message.split('').reverse().join('');
            },
            changeMessage: function (event) {
                this.message = event.target.value;
            }
        }
    })
</script>
```


### v-bind

タグ内のテキストには`{{  }}`を使って変数を展開可能だが、タグの属性にはこの文法は使えない。
属性に変数を展開するには`v-bind`を用いる。

```html
<div id="app">
  <p v-bind:id="dynamicId">
    {{ dynamicText }}
  </p>
</div>
<script>
    new Vue({
        el: "#app",
        data: {
            dynamicId: "A001",
            dynamicText: "太郎"
        }
    })
</script>
```


### v-model

フォームに入力した値をリアクティブにする場合、`v-on`でキー入力を検知しても良いが、`v-model`で双方向のデータバインドを実装することもできる。
※input 要素 or textarea 要素で使用可能
※textarea の改行は`<br>`に変換する処理を入れないと1行につながってしまうので注意

```html
<div id="app">
    <p>
        textarea 要素：{{ model.messageTextarea }}<br/>
        <textarea v-model:value="model.messageTextarea"></textarea>
    </p>
    <p>
        input 要素（入力フォーム）：{{ model.messageInput }}<br/>
        <input v-model:value="model.messageInput">
    </p>
    <p>
        input 要素（チェックボックス・単数）：{{ model.checkBoxSelected }}<br/>
        <input type="checkbox" v-model="model.checkBoxSelected">
    </p>
    <p>
        input 要素（チェックボックス・複数）：{{ model.checkedWords.sort() }}<br/>
        <label><input type="checkbox" value="apple" v-model="model.checkedWords">りんご</label>
        <label><input type="checkbox" value="orange" v-model="model.checkedWords">みかん</label>
        <label><input type="checkbox" value="grape" v-model="model.checkedWords">ぶどう</label>
    </p>
    <p>
        input 要素（ラジオボタン）：{{ model.radioModuration }}<br/>
        <label><input type="radio" value="AM" v-model="model.radioModuration">午前</label>
        <label><input type="radio" value="PM" v-model="model.radioModuration">午後</label>
    </p>
    <p>
        セレクトボックス・単数：{{ model.selectBoxSelected }}<br/>
        <select v-model="model.selectBoxSelected">
            <option disabled value="">元号を選択して下さい</option>
            <option>明治</option>
            <option>大正</option>
            <option>昭和</option>
            <option>平成</option>
        </select>
    </p>
    <p>
        セレクトボックス・複数：{{ model.selectedWords }}<br/>
        <select v-model="model.selectedWords" multiple>
            <option disabled value="">好きなジャンルを選択して下さい（複数可）</option>
            <option>歴史</option>
            <option>SF</option>
            <option>ミステリー</option>
            <option>恋愛</option>
        </select>
    </p>
</div>
<script>
    new Vue({
        el: "#app",
        data: {
            model: {
                messageInput: "",
                messageTextarea: "",
                checkBoxSelected: false,
                checkedWords: [],
                radioModuration: "",
                selectBoxSelected: false,
                selectedWords: []
            }
        }
    })
</script>
```

結果：

![](https://user-images.githubusercontent.com/13412823/48967205-4ca06580-f020-11e8-9920-df06684497df.png)


## 算出プロパティ

ある条件を満たす値だけを表示するときなどに使う。

```
<div id="app">
    奇数：{{ odd }}<br/>
    偶数：{{ even }}<br/>
    <ul v-for="num in odd">
        <li>奇数：{{ num }}</li>
    </ul>
    <ul v-for="num in even">
        <li>偶数：{{ num }}</li>
    </ul>
</div>
<script>
    new Vue({
        el: '#app',
        data: {
            numArray: [0, 1, 2, 3, 4, 5]
        },
        computed: {
            odd(){
                return this.numArray.filter(n => {return n % 2 !== 0})
            },
            even(){
                return this.numArray.filter(n => {return n % 2 === 0})
            }
        }
    })
</script>
```

結果：

![](https://user-images.githubusercontent.com/13412823/48967216-79547d00-f020-11e8-8c6b-bdf45adbb67d.png)


## コンポーネント

UI をコンポーネントツリーとして抽象化して表現する。
カスタムタグのように使える。

![](https://user-images.githubusercontent.com/13412823/48967217-7c4f6d80-f020-11e8-85be-456ee5dc48dd.png)

```html
<div id="app">
    <ol>
        <sample-item v-for="item in tasks" v-bind:todo="item"></sample-item>
    </ol>
</div>
<script>
    // コンポーネント sample-item の定義
    Vue.component('sample-item', {
        props: ['todo'],
        template: '<li>{{ todo.text }}</li>'
    });

    new Vue({
        el: "#app",
        data: {
            title: "ToDo List",
            tasks: [
                { id: 0, text: "Task A" },
                { id: 1, text: "Task B" },
                { id: 2, text: "Task C" }
            ]
        }
    })
</script>
```

結果：

![](https://user-images.githubusercontent.com/13412823/48967223-9f7a1d00-f020-11e8-8ef0-669a3d778aa9.png)


# 単一ファイルコンポーネント

ビュー・ロジック・スタイルを1つのソースコード（.vue）にまとめる仕組み。
**コンパイルが必要**。

- MyMessage.vue

```
<template>
    <div>{{ msg }}</div>
</template>

<script>
    export default {
        name: 'MyMessage',
        data () {
            return {
                msg: 'Hello world!'
            }
        }
    }
</script>

<style>
</style>
```

- index.html

```html
<div id="app">
    <mymessage></mymessage>
</div>
<script>
    import MyMessage from './MyMessage';
    new Vue({
        el: '#app',
        components: { 'mymessage': MyMessage }
    })
</script>
```

（動作未確認）


# Vuex


# vue-router
