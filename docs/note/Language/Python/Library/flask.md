---
title: Flask
---

# リクエストを送信

クエリの受け取りなど？
```python
from flask import Flask, request
# アクセス元で指定されたパラメータ（ここでは'query'）を取得
query  = request.arg.get('query', '')
 
# アクセス元の情報を取得（OS, ブラウザなど）
ua = request.headers.get('User-Agent')
 
# アクセス元が求める返り値の型を取得
accept = request.headers.get('Accept')
```

# REST API サーバ

```
#!/usr/bin/env python2.7

from flask import Flask, jsonify

# インスタンス生成
app = Flask(__name__)

@app.route('/')
def return_json():
    result = {
        "a": "aiueo",
        "b": 12345
    }
    return jsonify(ResultSet=result)

if __name__ == '__main__':
	# デバッグを有効にして起動
	# コードが修正された時、自動でコードをリロードしてくれる
    app.run(debug=True)
    
    # 上の起動ではネットワークの他のホストからはアクセスできない仕様になっている
    # デバッグモードだと元ファイルを編集するだけで任意のコードを実行できて危険
    # 以下のように host を設定すると外部からも接続可能に
    # デバッグは無効にすることを推奨
    #app.run(host='0.0.0.0')

	# デフォルトの5000以外のポートを指定することもできる
	#app.run(port='1234')
```


# ルーティング

叩く URL によって挙動を変える

```python
# http://localhost:5000/hi
@app.route('/hi')
def say_hi():
    return 'Hi World'

# http://localhost:5000/hello
@app.route('/hello')
def say_hello():
    return 'Hello World'
```

# 変数ルール

URL に変数をあてることもできる。

```python
@app.route('/user/<username>')
def show_user_profile(username):
	return "User {0}".format(username)

# 引数型指定
@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "post {0}".format(post_id)
```
引数型指定は
- int: 整数
- float: 浮動小数点
- path: スラッシュも受け取る

# クエリパラメータを受け取る

サーバ側のコード(server_template.py)：

```
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/hoge', methods=['GET'])
def application_get():
    """GET リクエストを受け取った時"""
    p_int = request.args.get("param1", type=int)
    p_str = request.args.get("param2", type=str)
    if p_int == None or p_str == None:
        res_error = {"msg": "invalid parameter(s)."}
        return jsonify(ResultSet=res_error)
    else:
        # 処理を記述

        # json を返す
        res_sample = {"p1": p_int + 1, "p2": p_str + "a"}
        return jsonify(ResultSet=res_sample)


@app.route('/fuga', methods=['POST'])
def application_post():
    """POST リクエストを受け取った時"""
    parameters = json.loads(request.get_data())
    if not parameters.has_key("param1") or not parameters.has_key("param2"):
        res_error = {"msg": "invalid parameter(s)."}
        return jsonify(ResultSet=res_error)
    else:
        p_int = parameters["param1"]
        p_str = parameters["param2"]

        # 処理を記述

        # json を返す
        res_sample = {"p1": p_int + 1, "p2": p_str + "a"}
        return jsonify(ResultSet=res_sample)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
```

リクエストする側のコード(request_template.py)：

```
# -*- coding: utf-8 -*-
"""
使い方

server_template.py を起動し、別ウインドウでこのスクリプトを叩く

[window 1]
$ python server_template.py

[window 2]
$ python request_template.py
GET リクエスト実行結果：
{u'ResultSet': {u'p2': u'abcda', u'p1': 1235}}
POST リクエスト実行結果：
{u'ResultSet': {u'p2': u'abcda', u'p1': 1235}}
"""


import requests, json

request_parameters = {"param1": 1234, "param2": "abcd"}


def get_request():
    """GET リクエストを投げる"""
    s = requests.Session()
    url = "http://localhost:5000/hoge"
    result = s.get(url, params=request_parameters).json()
    print "GET リクエスト実行結果："
    print result


def post_request():
    """POST リクエストを投げる"""
    s = requests.Session()
    url = "http://localhost:5000/fuga"
    result = s.post(url, data=json.dumps(request_parameters)).json()
    print "POST リクエスト実行結果："
    print result


if __name__ == '__main__':
    get_request()
    post_request()
```

**デフォルトでは POST は許可されていないっぽい**。POST でリクエストを投げると 405 エラーが返ってくる。GET は大丈夫。
そこで、以下のように明示的に POST を許可する。

```python
@app.route('/hoge', methods=['GET', 'POST'])
def application():
	...
```

あとは GET のときと同様。


# パスパラメータを受け取る

```python
@app.route('/hoge/<int:status>')
def return_status(status):
    result = {
        "status": status
    }
    return jsonify(ResultSet=result)
```
