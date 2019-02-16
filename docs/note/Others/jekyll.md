---
title: Jekyll
main_image: https://user-images.githubusercontent.com/13412823/52898457-a4b2c680-3221-11e9-9051-615440342bec.png
---

# Jekyll とは

静的サイトジェネレータ。

- Markdown や HTML/CSS を利用してウェブサイトを生成
- ブログのような形態を意識しており、テンプレートを用いて簡単にウェブページが作成できる
- 

# 基本的な使い方

(TODO)

# GitHub Pages における利用

(TODO)

# 便利プラグイン

## jekyll-redirect-from

https://github.com/jekyll/jekyll-redirect-from

リダイレクトの設定をする。

**リダイレクト先** ページに対応する .md ファイルの YAML Front-matter で以下のような設定を行う。

```
---
redirect_from: /foo/
---
```

複数指定したいとき：

```
---
redirect_from:
  - /foo/
  - /foo/bar/
---
```

## jekyll-gist

https://github.com/jekyll/jekyll-gist

gist のコードスニペットを埋め込める。

a

`{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}`

b

```
{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}
```

c

{% raw %}`{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}`{% endraw %}

d

{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}




# Tips

## 404

## Liquid タグのエスケープ

```
{% raw %}
この中身はそのまま出力される
{% endraw %}
```


