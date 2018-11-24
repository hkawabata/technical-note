---
title: Swagger
---

![swagger_logo2](https://user-images.githubusercontent.com/13412823/48452739-c69c4780-e7f3-11e8-83ad-3454d0ce2c7d.png)

# Swagger とは

Open API Initiative が推進する RESTful API インターフェース記述のための標準フォーマット。

利用のための色々な便利ツールがある。

| ツール | 説明 |
| :-- | :-- |
| Swagger Spec | Swagger 書式で記述した API 仕様書。JSON or YAML で記述。 |
| [Swagger Editor](https://editor.swagger.io/) | Swagger ファイルの生成・編集を行うためのツールで、ブラウザ上で動作する。リアルタイムで構文チェックしてくれる。 |
| Swagger UI | Swagger Spec を読み込み、HTML 形式でドキュメントを生成する。 |
| Swagger Codegen |  |

# Swagger Editor

## Web UI

https://editor.swagger.io/ にアクセスすれば使える。

## インストールしてローカルで動かす

```bash
$ brew install npm
$ git clone https://github.com/swagger-api/swagger-editor.git
$ cd swagger-editor
$ npm start  # 自動でブラウザ上で Editor が開く
```

# Swagger の記法

