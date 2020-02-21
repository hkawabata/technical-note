---
title: "[Python] スクレイピング"
---

Python3 を想定。

# 基本的な動作

## URL から HTML を取得

```python
from urllib import request

target_url = 'http://example.hkawabata.jp'

with request.urlopen(target_url) as response:
    html = response.read().decode('utf-8')
    # html 文字列を処理
    pass
```

## URL からファイルを取得

```python3
from urllib import request

file_url = 'http://example.hkawabata.jp/path/to/hoge.png'
save_as = './path/to/local/dir/hoge_local.png'

request.urlretrieve(file_url, save_as)
```

## HTML をパース

標準の`HTMLParser`を使う。

タグの開始 / 終了、及び本文データを見つけた際の挙動を定義しておく。

```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs_str = '' if len(attrs) == 0 else ', '.join(['({}: {})'.format(a[0], a[1]) for a in attrs])
        print('[Encountered a start tag] {}'.format(tag if len(attrs) == 0 else tag + ', attributes = ' + attrs_str))

    def handle_endtag(self, tag):
        print('[Encountered a end tag] {}'.format(tag))

    def handle_data(self, data):
        print('[Encountered a data] {}'.format(data))

html = """
<html>
  <head>
    <title>タイトル</title>
  </head>
  <body>
    <h1 class="c1">見出し</h1>
    body本文1
    <img src="http://example.hkawabata.jp/img.png" alt="画像">
    <ul>
      <li>箇条書き（テキスト）</li>
      <li><a href="http://example.hkawabata.jp">箇条書き（リンク）</a></li>
    </ul>
    body本文2
  </body>
</html>
"""

my_parser = MyHTMLParser()
my_parser.feed(html)

my_parser.close()
```

出力結果：

```
[Encountered a data] 

[Encountered a start tag] html
[Encountered a data] 
  
[Encountered a start tag] head
[Encountered a data] 
    
[Encountered a start tag] title
[Encountered a data] タイトル
[Encountered a end tag] title
[Encountered a data] 
  
[Encountered a end tag] head
[Encountered a data] 
  
[Encountered a start tag] body
[Encountered a data] 
    
[Encountered a start tag] h1, attributes = (class: c1)
[Encountered a data] 見出し
[Encountered a end tag] h1
[Encountered a data] 
    body本文1
    
[Encountered a start tag] img, attributes = (src: http://example.hkawabata.jp/img.png), (alt: 画像)
[Encountered a data] 
    
[Encountered a start tag] ul
[Encountered a data] 
      
[Encountered a start tag] li
[Encountered a data] 箇条書き（テキスト）
[Encountered a end tag] li
[Encountered a data] 
      
[Encountered a start tag] li
[Encountered a start tag] a, attributes = (href: http://example.hkawabata.jp)
[Encountered a data] 箇条書き（リンク）
[Encountered a end tag] a
[Encountered a end tag] li
[Encountered a data] 
    
[Encountered a end tag] ul
[Encountered a data] 
    body本文2
  
[Encountered a end tag] body
[Encountered a data] 

[Encountered a end tag] html
[Encountered a data] 

```
