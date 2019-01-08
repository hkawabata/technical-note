---
title: Swagger
main_image: https://user-images.githubusercontent.com/13412823/48452739-c69c4780-e7f3-11e8-83ad-3454d0ce2c7d.png
---

# Swagger とは

Open API Initiative が推進する RESTful API インターフェース記述のための標準フォーマット。

利用のための色々な便利ツールがある。

| ツール | 説明 |
| :-- | :-- |
| Swagger Spec | Swagger 書式で記述した API 仕様書。JSON or YAML で記述。 |
| [Swagger Editor](https://editor.swagger.io/) | Swagger ファイルの生成・編集を行うためのツールで、ブラウザ上で動作する。リアルタイムで構文チェックしてくれる。 |
| Swagger UI | Swagger Spec を読み込み、HTML 形式でドキュメントを生成する。 |
| Swagger Codegen | Swagger Spec から、様々な言語の API クライアントを自動生成する。 |

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

# Swagger Codegen

## 使い方

### Mac にインストールする場合

```bash
$ brew install swagger-codegen

$ swagger-codegen generate -i /path/to/swagger.json -l ruby -o /tmp/ruby_api_client
```

### jar をダウンロードして使う場合

```bash
$ wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar

$ java -jar swagger-codegen-cli.jar generate \
     -i /path/to/swagger.json \
     -l php \
     -o /tmp/php_api_client
```

### リポジトリを clone して使う場合

```bash
$ git clone https://github.com/swagger-api/swagger-codegen
$ cd swagger-codegen
$ mvn clean package

$ java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
     -i /path/to/swagger.json \
     -l java \
     -o /tmp/java_api_client
```


## 設定

config.json に色々設定を記述できる

```json
{
    "modelPackage" : "jp.hkawabata.model",
    "apiPackage" : "jp.hkawabata.api"
}
```

使い方

```bash
$ java -jar swagger-codegen-cli.jar generate -i /path/to/swagger.json -l java -o /tmp/java_api_client -c /path/to/config.json
```

# Swagger の記法

