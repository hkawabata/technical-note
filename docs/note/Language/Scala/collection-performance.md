---
title: コレクションの性能
---

cf. [Scalaのコレクションたち〜imutable.Seq編〜](https://qiita.com/louvre2489/items/f16db1e9d7f88fdeb04c)

- データ取得（先頭・末尾・任意）
- 追加（先頭・末尾・任意）
- 削除（先頭・末尾・任意）

- `Array`, `List`, `Set`

```scala
import collection.{immutable, mutable}

val N = 100000
val keys = 0 until N
val values = keys.map(n => "v" + n.toString)

val imList = immutable.List(keys: _*)
val 

def benchmark(): Unit = {
  a
}
```


```

```