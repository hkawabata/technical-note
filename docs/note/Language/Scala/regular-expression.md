---
title: 正規表現
---

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

### マッチした文字列の抽出

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
