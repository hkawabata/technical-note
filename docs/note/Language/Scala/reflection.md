---
title: リフレクション（書きかけ）
---

## メンバ一覧

```scala
import scala.reflect.runtime.{universe => ru}

case class MyBean(s: String, n: Int, d: Double, var sVar: String)

val members = ru.typeOf[MyBean].members
members.foreach(println)
/*
method equals
method toString
method hashCode
method productElementName
method canEqual
method productIterator
method productElement
method productArity
method productPrefix
method copy$default$4
method copy$default$3
method copy$default$2
method copy$default$1
method copy
constructor MyBean
variable sVar
variable sVar
variable sVar
value d
value d
value n
value n
value s
value s
method productElementNames
method $init$
method $asInstanceOf
method $isInstanceOf
method synchronized
method ##
method !=
method ==
method ne
method eq
method notifyAll
method notify
method clone
method getClass
method wait
method wait
method wait
method finalize
method asInstanceOf
method isInstanceOf
*/

members.filter(_.asTerm.isVal).foreach(println)
/*
value d
value n
value s
*/

members.filter(_.asTerm.isVar).foreach(println)
// variable sVar
```

## 値の set / get

➔ `val`でも値を変更できる？

```scala
val x = MyBean("a", 1, 0.1, "aVar")

val m: ru.Mirror = ru.runtimeMirror(classOf[MyBean].getClassLoader)
val im: ru.InstanceMirror = m.reflect(x)

members.map(_.asTerm).filter(term => term.isVar || term.isVal).foreach{
  term => println(s"$term:\t${im.reflectField(term).get}")
}
/*
variable sVar:	aVar
value d:	0.1
value n:	1
value s:	a
*/

val fieldTermSymb: ru.TermSymbol = ru.typeOf[MyBean].decl(ru.TermName("sVar")).asTerm
im.reflectField(fieldTermSymb).set("bVar")
println(im.reflectField(fieldTermSymb).get)
// bVar

val fieldTermSymb: ru.TermSymbol = ru.typeOf[MyBean].decl(ru.TermName("s")).asTerm
im.reflectField(fieldTermSymb).set("b")
println(im.reflectField(fieldTermSymb).get)
// b
```
