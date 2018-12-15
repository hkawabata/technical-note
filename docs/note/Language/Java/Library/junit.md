---
title: JUnit
---

# JUnit の特徴

## 実装方法
テストクラスにテスト用のメソッドを実装する。テストしたい対象とテストプログラムを分離できるため、テスト対象への影響がなくなる。

## テストプログラム管理

複数のテストプログラムをまとめることができ、まとめたテストを一度に実行することもできる。

## テストの評価と結果

テスト結果が瞬時に表示されるので、テストを評価する負荷がなくなる。

## IDE との連携

JUnit 単体でも利用できるが、Eclipse などと連携することも可能。**最近の Eclipse は JUnit 同梱**。

# 基本的なアノテーション

|アノテーション|説明|
|:--|:--|
|`@BeforeClass`|テストクラスの static イニシャライザの後に呼ばれる。|
|`@Before`|テストクラスのコンストラクタの後に呼ばれる。**各テストメソッドの前に実行される**。フィールドへのアクセスも可能。|
|`@Test`|テストメソッドに付与する。|
|`@Ignore("...")`|テストメソッドに付与する。これを付与したテストメソッドは実行されない。|
|`@After`|テストメソッド実行後に実行したいメソッドに付与する。**各テストメソッドの後に実行される**。フィールドへのアクセスも可能。|
|`@AfterClass`|テストクラス実行後に実行したいメソッドに付与する。|

- `@Before`,`@After`,`@BeforeClass`,`@AfterClass`をつけたメソッドは public, void である必要がある。
- `@BeforeClass`,`@AfterClass`をつけたメソッドは、static である必要がある。

# テストの書き方

## テストクラスのルール

- src/test/java 以下のパッケージに作成する。
- テストクラスは`*Test`という名前でないと`mvn test`を叩いても実行されない。
- テストメソッドには`@Test`アノテーションをつける（JUnit 4）。

```java
import org.junit.Test

public class SampleTest {
	@Test
	public void testHogeHoge() {
		...
		assert(...)
	}
}
```

> `@Test`不要の方法として、`junit.framework.TestCase`をテストクラスに継承させても良い（JUnit 3）。
> 内部の全メソッド（public かどうかとか、特別のアノテーションがついてるとかで例外あるかも）がテストメソッドとみなされる。


## アサーション
以下のメソッドを使う。

```java
import junit.framework.Assert.*;

// expected（期待値）と actual（実行結果）が等しければテスト成功。
// 任意の型でテスト可能だが、boolean・byte・char・short・int・long 以外の
// クラスのインスタンスを比較する場合、そのクラスの equals メソッドで比較している。
static void assertEquals(型 expected, 型 actual);

// expected と actual の差の絶対値が delta より小さければテスト成功。
// float もある。
static void assertEquals(double expected, double actual, double delta);

// 配列の要素が一致していればテスト成功。
static void assertArrayEquals(配列 expected, 配列 actual)

// 中身が Null でなければテスト成功。
static void assertNotNull(Object obj)

// 中身が Null ならテスト成功。
static void assertNull(Object obj)

// expected と actual が同じ参照先かどうかを比較（== による比較）。
// 同値比較（equals による比較）が true でも、別のインスタンスだと通らない。
static void assertSame(Object expected, Object actual)

// assertSame の逆。
static void assertNotSame(Object expected, Object actual)

// 中身が True ならテスト成功。
static void assertTrue(boolean cond)

// 中身が True ならテスト成功。
static void assertFalse(boolean cond)

// 必ずテスト失敗。
// 「ここにくるハズがない」「ここにきたらテスト失敗」という箇所に記述する
static void fail()
```
上記の各メソッドについて、第1引数としてテスト失敗時のメッセージを記述できる。

## 例外のテスト

```java
import static org.hamcrest.Matchers.*;
import org.junit.rules.ExpectedException;

ExpectedException expectedException = ExpectedException.none();

// 期待する例外クラス
expectedException.expect(RuntimeException.class);
expectedException.expectCause(
	allOf(
		// 期待する Caused By の例外クラス
		instanceOf(NullPointerException.class),
		// 期待する Caused By の例外メッセージ
		hasProperty("message", is("ぬるぽ"))
	)
);
```

# メモ

## 複数のテストメソッドを実行する時に起こること

```
@BeforeClass >
	インスタンス生成・コンストラクタ実行 > @Before > @Test test1() > @After >
	インスタンス生成・コンストラクタ実行 > @Before > @Test test2() > @After >
	インスタンス生成・コンストラクタ実行 > @Before > @Test test3() > @After >
	...
@AfterClass
```

のような流れで動いているっぽい。なので、
- @Before でフィールドの値をいじるとその効果はその回のテストメソッドに反映される
- @After でフィールドの値をいじっても、次の回のテストメソッドは新しいインスタンス上で動くため、効果が反映されない
