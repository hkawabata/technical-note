---
title: 正規表現
---

## 使い方いろいろ

### マッチするかどうか (Boolean)

```scala
"1234".matches("""\d{4}""")
```

### マッチする最初の文字列 (Option[String])

```scala
val regex = """\d{4}""".r
// regex: scala.util.matching.Regex = \d{4}
regex.findFirstIn("1234")
// res0: Option[String] = Some(1234)
```

### マッチした文字列の部分抽出

```scala
val regexYMD = """(\d{4})-(\d{2})-(\d{2})""".r
"1990-12-31" match {
  case regexYMD(y, m, d) => println(s"${y}年${m}月${d}日")
  case _ => throw new Exception
}
// 1990年12月31日
```

```scala
val regexYMD = """(\d{4})-(\d{2})-(\d{2})""".r
val regexYMD(year, month, day) = "2000-01-23"
// year: String = 2000
// month: String = 01
// day: String = 23
```

```scala
val regex = """(\d{4})-(\d{2})-(\d{2})""".r
regex.findAllIn("1990-12-31").matchData.foreach {
  m =>
    println(m.group(0))
    println(m.group(1))
    println(m.group(2))
    println(m.group(3))
}
// 1990-12-31
// 1990
// 12
// 31
```

```scala
val regex = new scala.util.matching.Regex("""(\d{4})-(\d{2})-(\d{2})""", "year", "month", "day")
regex.findAllIn("1990-12-31").matchData.foreach {
  m =>
    println(m.group("year"))
    println(m.group("month"))
    println(m.group("day"))
}
// 1990
// 12
// 31
regex.findAllIn("1990-12-31, 2000-01-23").matchData.foreach {
  m =>
    println(m.group("year"))
    println(m.group("month"))
    println(m.group("day"))
}
// 1990
// 12
// 31
// 2000
// 01
// 23
```

## Tips

### 括弧でグループ化するが、インデックスは割り当てない

```scala
val regexYMD1 = """((紀元前)?[0-9]+)年([0-9]+)月([0-9]+)日""".r
val regexYMD2 = """((?:紀元前)?[0-9]+)年([0-9]+)月([0-9]+)日""".r

regexYMD1.findAllIn("紀元前1000年12月31日").matchData.foreach {
  m =>
    println(m.group(0))
    println(m.group(1))
    println(m.group(2))
    println(m.group(3))
    println(m.group(4))
}
/*
紀元前1000年12月31日
紀元前1000
紀元前
12
31
*/
regexYMD2.findAllIn("紀元前1000年12月31日").matchData.foreach {
  m =>
    println(m.group(0))
    println(m.group(1))
    println(m.group(2))
    println(m.group(3))
}
/*
紀元前1000年12月31日
紀元前1000
12
31
*/
```
