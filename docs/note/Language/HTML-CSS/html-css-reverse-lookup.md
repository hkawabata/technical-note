---
title: HTML / CSS 逆引き
---
## マウスオーバー時にツールチップを表示

### 1. css を利用

```css
.balloon {
    display: none;               /* 初期値は非表示にしておく */
    position: absolute;          /* 絶対配置 */
    left: 50%;                   /* 親に対して中央配置 */
    transform: translateX(-50%); /* 親に対して中央配置 */
    bottom: -30px;               /* 親要素下からの位置 */
    padding: 5px;                /* 余白 */
    white-space: nowrap;         /* テキストを折り返さない */
    background: black;           /* 背景色 */
    color: white;                /* 文字色 */
    opacity: 0.5;                /* 背景の透過度 */
    border-radius: 5px;          /* 角丸 */
}

.balloon-parent {
    position: relative; /* ツールチップの位置の基準 */
    cursor: pointer;    /* カーソルを当てたときにポインターに */
}

.balloon-parent:hover .balloon {
    display: inline-block;
}
```

```html
<span class="balloon-parent">
    Please put cursor here.
    <div class="balloon">tooltip contents</div>
</span>
```

![css-balloon](https://gist.github.com/user-attachments/assets/6991dc49-2f05-4cf9-a28e-c7450bc66e08)


### 2. title 属性を使う

```html
<span title="tooltip contents">
    Please put cursor here.
</span>
```

![title-attribute](https://gist.github.com/user-attachments/assets/e9c0a3ce-6ec0-4f58-b1ae-c3ad312427ac)

マウスオーバーしてから表示されるまでに時間がかかる。（ブラウザ依存？調整は可能？）
