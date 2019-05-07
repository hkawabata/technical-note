---
title: カリー化・部分適用
---

# カリー化

複数の引数を取る関数を、1つの引数を取る関数のチェーンとして扱う。

```scala
def func(x: Int)(y: Int)(z: Int) = 100 * x + 10 * y + z
// func: (x: Int)(y: Int)(z: Int)Int

val funcCurried = func _
// funcCurried: Int => (Int => (Int => Int)) = $$Lambda$1077/483635512@151bf776

val funcCurried2 = funcCurried(1)   // val funcCurried2 = func(1) _
// funcCurried2: Int => (Int => Int) = $$Lambda$1079/1807896178@724aefc3

val funcCurried3 = funcCurried2(2)  // val funcCurried3 = func(1)(2) _
// funcCurried3: Int => Int = $$Lambda$1080/441683672@78910096

funcCurried(1)(2)(3)
// res0: Int = 123

funcCurried2(4)(5)
// res1: Int = 145

funcCurried3(6)
// res2: Int = 126
```

引数をまとめてカリー化するメソッドもある。

```scala
val func = {(x:Int, y:Int, z:Int) => 100 * x + 10 * y + z}
// func: (Int, Int, Int) => Int = $$Lambda$1116/1443000737@4b9c411

val funcCurried = func.curried
// funcCurried: Int => (Int => (Int => Int)) = scala.Function3$$Lambda$1062/1389984438@685d7ba5

val funcCurried2 = funcCurried(1)
// funcCurried2: Int => (Int => Int) = scala.Function3$$Lambda$1114/670959005@5ec25b61

val funcCurried3 = funcCurried(1)(2)
// funcCurried3: Int => Int = scala.Function3$$Lambda$1115/1986679541@3fecdd00

func(1, 2, 3)
// res0: Int = 123

funcCurried(1)(2)(3)
// res1: Int = 123

funcCurried2(4)(5)
// res2: Int = 145

funcCurried3(6)
// res3: Int = 126

val funcCurried3_2 = funcCurried2(2)
// funcCurried3_2: Int => Int = scala.Function3$$Lambda$1070/1273012861@792b9dd3
```

# 部分適用

複数の引数を取る関数に対して、一部の引数に値を束縛した関数を返す。

```scala
def func(x: Int, y: Int, z: Int) = 100 * x + 10 * y + z
// func: (x: Int, y: Int, z: Int)Int

val funcPartialApplied1 = func(_, _, 3)
// funcPartialApplied1: (Int, Int) => Int = $$Lambda$1051/662409124@6cd64ee8

val funcPartialApplied2 = func(1, _, 3)
// funcPartialApplied2: Int => Int = $$Lambda$1052/1223213866@20a7953c

val funcPartialApplied3 = func _
// funcPartialApplied3: (Int, Int, Int) => Int = $$Lambda$1074/1947378744@1e3ff233

funcPartialApplied1(4, 5)
// res0: Int = 453

funcPartialApplied2(6)
// res1: Int = 163

funcPartialApplied3(7, 8, 9)
// res2: Int = 789
```
