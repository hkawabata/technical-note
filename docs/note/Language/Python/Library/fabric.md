---
title: Fabric
---

# メタ設定

## env

# アノテーション

## task

## parallel

# task 内部で使える関数

## upload_template

jinja2 と連携し、テンプレートファイルに変数を埋め込んでリモートサーバに追加する

テンプレートファイルの例：

```
master={{ master_host }}
user={{ user }}
threshold={{ score_threshold }}
```

```python
from fabric.api import task
from fabric.contrib.files import upload_template

@task
def hoge():
    settings = {"master_host": "hoge.co.jp", "user": "Taro", "score_threshold": 2.5}
    upload_template("/local/path/settings.txt.template", "/remote/path/settings.txt", context=settings, use_jinja=True)
```

## run


## sudo


## cd

```python
with cd('/path/to/dir'):
    run('./hoge.sh')
```

## execute
