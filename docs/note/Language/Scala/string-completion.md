---
title: 文字列補間
---

`s`, `f`, `raw` の3種類の補完子が提供されている。

```scala
val i: Int = 3
val d: Double = 1.5
val s: String = "answer"

// s補完子 -> 文字列に変数を埋め込み
val sStr = s"$s:\n$i x $d = ${i * d}"
/*
answer:
3 x 1.5 = 4.5
*/

// f補完子 -> 書式付き文字列を指定可能
val fStr = f"$s%s:\n$i%d x $d%.2f = ${i * d}%.3f"
/*
answer:
3 x 1.50 = 4.500
*/

// raw補完子 -> エスケープを実行しない
val rawStr = raw"$s:\n$i x $d = ${i * d}"
/*
answer:\n3 x 1.5 = 4.5
*/
```

