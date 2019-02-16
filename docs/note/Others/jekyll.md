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

{% raw %}
```
{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}
```
{% endraw %}

{% gist hkawabata/84464b4853dfdce81214f102746b0011 %}


## jekyll-sitemap

https://github.com/jekyll/jekyll-sitemap

サイトのルートに sitemap.xml を自動生成する。


## jekyll-seo-tag

https://github.com/jekyll/jekyll-seo-tag

検索エンジン向けのメタタグを生成する。

`_config.yml`:

```yaml
plugins:
  - jekyll-seo-tag

webmaster_verifications:
  google: ...
```

`_layouts/default.html`:

{% raw %}
```html
<html>
  <head>
    {% seo %}
    <title>{{ page.title }}</title>
    ...
  </head>
  <body>
    ...
  </body>
</html>
```
{% endraw %}


# Tips

## 404

ルートディレクトリに 404.html または 404.md を配置する。

※ 404.md の場合、デフォルトでは _layouts/default.html が適用される（変更する場合は 404.md の Front-matter で`layout`の設定を行う）


## Liquid タグのエスケープ

`{{ "{% raw "}} %}`と`{{ "{% endraw " }} %}`で挟む。

```
{{ "{% raw "}} %}
この中身がエスケープされる。
{{ "{% endraw " }} %}
```

本ページのように`{{ "{% raw "}} %}`,`{{ "{% endraw " }} %}`自体を表示させる方法については[変換元のマークダウンファイル](https://github.com/hkawabata/technical-note/blob/master/docs/note/Others/jekyll.md)を参照。


