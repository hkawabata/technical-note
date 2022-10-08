---
title: Parser Combinator
---

# 使用するための設定

build.sbt
```scala
libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "2.1.1"
```

# 簡単なサンプル

```scala
object MyApp {  
  def main(args: Array[String]): Unit = {  
    MyTokenParser("I LOVE MUSIC")  
    MyTokenParser("I LIKE MUSIC")  
    println(MyRegexParser("Xx1234"))  
    println(MyRegexParser("1234Xx"))  
  }  
}  
  
object MyTokenParser extends JavaTokenParsers {  
  def third = s ~ v ~ o ^^ { case subj ~ verb ~ obj => println(s"$subj + $verb + $obj") }  
  def s = "I" | "WE"  
  def v = "LOVE"  
  def o = "YOU" | "MUSIC"  
  
  def apply(s : String) : Unit = {  
    parseAll(third, s) match {  
      case Success(_, _) => println("Success")  
      case x => println("Failure: " + x)  
    }  
  }  
}  
  
object MyRegexParser extends RegexParsers {  
  def p1 = """[a-zA-Z]+""".r  
  def p2 = """\d+""".r  
  
  def word: Parser[String] = p1 ~ p2 ^^ { case x ~ y =>  x + ":" + y }  
  
  def apply(s: String): String = {  
    parseAll(word, s) match {  
      case Success(x, y) => x  
      case x => "Failure: " + x  
    }  
  }  
}
```

```
I + LOVE + MUSIC
Success
Failure: [1.3] failure: 'LOVE' expected but 'L' found

I LIKE MUSIC
  ^
Xx:1234
Failure: [1.1] failure: string matching regex '[a-zA-Z]+' expected but '1' found

1234Xx
^
```

