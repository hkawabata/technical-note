---
title: jQuery
---


`$(function(){ ... });`は`$(document).ready(function(){ ... });`の略であり、
**DOMが全てロードされてDOMにアクセスできる準備が出来た段階で実行させたい処理を関数で指定する。**

なので、

```javascript
$(function(){
　　console.log('jQuery');
});
console.log('java script');
```

のコンソールログは

```
java script
jQuery
```

となる。

