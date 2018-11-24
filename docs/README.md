# GitHub Pages
https://hkawabata.github.io

## ドキュメントツリーの生成

技術ノートの目次生成のため、以下のコマンドを叩く。

```bash
$ bin/path_tree_generator.py technical-notes > _includes/toc-technical-notes.xml
```

参考：生成される XML
```xml
<?xml version="1.0" ?>
<ul>
  <li>
    <a href="https://hkawabata.github.io/technical-notes">technical-notes</a>
    <ul>
      <li>
        oss
        <ul>
          <li>
            <a href="https://hkawabata.github.io/technical-notes/oss/gatling">gatling</a>
          </li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
```
