---
title: Flask
---

# Flask 概要

Python 用のウェブアプリケーションフレームワーク。


# ディレクトリ構成

単純な例。

```
/
+-- myapp.py
+-- static/
      +-- ...
      +-- ...
+-- templates/
      +-- ...
      +-- ...
```

# 基本的な使い方

## 単純な REST API

```python
#!/usr/bin/env python3

from flask import Flask, jsonify

# インスタンス生成
app = Flask(__name__)

# http://localhost:5000/
@app.route('/')
def hello():
    """
    単純な文字列を返す
    """
    return 'Hello, world!'

# http://localhost:5000/json
@app.route('/json')
def json():
    """
    JSON を返す
    """
    result = {
        'a': 'aiueo',
        'b': 12345
    }
    return jsonify(ResultSet=result)

if __name__ == '__main__':
    # リモートからのアクセスを許可して起動
    app.run(host='0.0.0.0')
```

## パラメータの受け取り

### クエリパラメータ

```python
from flask import jsonify, request

@app.route('/user')
def func():
    user_id = request.args.get("id", type=int)
    user_name = request.args.get("name", type=str)
    result = {
        'name': user_name,
        'id': user_id
    }
    return jsonify(ResultSet=result)
```

### パスパラメータ

#### 任意のフォーマットのパラメータを受け取る

（`/`を含まない）任意のパスパラメータを変数として受け付ける。

```python
@app.route('/user/<username>')
def func(username):
    return 'your user-name is ' + username
```

#### ルールでフォーマットを制限する

```python
@app.route('/user/<int:user_id>')
def func(user_id):
    return 'your user-id is ' + user_id
```

`<コンバータ:変数名>`という記法で変数書式に制限をかけられる

| コンバータ | 説明 | 備考 |
| :-- | :-- | :-- |
| `int` | 整数 |  |
| `float` | 浮動小数 | `int`とは排他で整数は受け付けない模様（`3.0`は OK だが`3`はダメだった） |
| `path` | `/`を含んでも OK |  |


## 静的ファイル・テンプレートファイルの使用

### 静的ファイルをそのまま返す

静的ファイルを static/ に配置（ここでは static/index.html）

```html
<html>
  <body>
    This is static file.
  </body>
</html>
```

```python
@app.route('/staticfile')
def static_file():
    return app.send_static_file('index.html')
```

```html
$ curl http://127.0.0.1:5000/staticfile
<html>
  <body>
    This is static file.
  </body>
</html>
```

### テンプレートファイルを変数の値でレンダリングして返す

テンプレートファイルを templates/ に配置（ここでは templates/index.html）

```html
<html>
  <body>
    {{ message }}
    <ul>
      {% for user in users %}
      <li><a href="/user/{{ users[user] }}">{{ user }}</a></li>
      {% endfor %}
    </ul>
  </body>
</html>
```

```python
from flask import render_template

users = {'Taro': 1, 'Jiro': 2, 'Saburo': 3}

@app.route('/userinfo')
def render():
    message = 'There are {} users.'.format(len(users))
    return render_template('index.html', message=message, users=users)
```

```html
$ curl http://localhost:5000/userinfo
<html>
  <body>
    There are 3 users.
    <ul>
      <li><a href="/user/1">Taro</a></li>
      <li><a href="/user/2">Jiro</a></li>
      <li><a href="/user/3">Saburo</a></li>
    </ul>
  </body>
</html>
```


# Tips

## app.run() の引数

### 待ち受けポート指定

```python
app.run(port=80)
```

### デバッグモード

```python
app.run(debug=True)
```

- 元のコードに変更があると自動でリロード
- エラー時のデバッガー機能


### リモートからのアクセスを許可

```python
app.run(host='0.0.0.0')
```

デフォルトでは`127.0.0.1`（ローカルループバックアドレス）で待ち受けており、外からのアクセスを受け付けない。


## GET 以外のメソッドを受け付ける

```python
@app.route('/path', methods=['POST'])
def func():
    pass
```


## ルーティング URL が重複したときの優先順位

実験してみた。

- 直接 URL を指定 > コンバータ付きパスパラメータ > コンバータなしパスパラメータ
- パス、コンバータが重複する複数のルートが定義されている場合、先に定義した方が優先

```python
@app.route('/hello')
def func1a():
    return 'route 1a'

@app.route('/hello')
def func1b():
    return 'route 1b'

@app.route('/<int:param>')
def func2a(param):
    return 'route 2a'

@app.route('/<int:param>')
def func2b(param):
    return 'route 2b'

@app.route('/<param>')
def func4a(param):
    return 'route 4a'

@app.route('/<param>')
def func4b(param):
    return 'route 4b'

@app.route('/<float:param>')
def func3(param):
    return 'route 3'
```

```bash
$ curl http://localhost:5000/hello
route 1
$ curl http://localhost:5000/helloworld
route 4a
$ curl http://localhost:5000/3
route 2a
$ curl http://localhost:5000/3.1
route 3
$ curl http://localhost:5000/3.0
route 3
$ curl http://localhost:5000/
# 404 Not Found
```


## URL 末尾のスラッシュの有無

| \ | 末尾に`/`をつけてリクエスト | 末尾に`/`をつけずリクエスト |
| :-- | :-- | :-- |
| URL 定義末尾に`/`あり | `200 OK` | `308 PERMANENT REDIRECT` |
| URL 定義末尾に`/`なし | `404 NOT FOUND` | `200 OK` |

```python
@app.route('/hello')
def no_slash():
    return 'slash not in definition'

@app.route('/hi/')
def slash():
    return 'slash in definition'
```

```
$ curl http://localhost:5000/hello
slash not in definition

$ curl http://localhost:5000/hello/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

$ curl http://localhost:5000/hi
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="http://localhost:5000/hi/">http://localhost:5000/hi/</a>.  If not click the link.

$ curl http://localhost:5000/hi/
slash in definition
```
