![](https://img.shields.io/github/repo-size/hkawabata/technical-note.svg)

# technical-note

https://hkawabata.github.io/technical-note/

## ドキュメントツリーの生成

目次生成のため、以下のコマンドを叩く。

```
$ bin/path_tree_generator.py > docs/_includes/toc-technical-notes.xml
```

参考：生成される XML

```
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
