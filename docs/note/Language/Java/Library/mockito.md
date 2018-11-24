---
title: Mockito
---

# pom.xml の設定

```xml
<dependency>
	<groupId>org.mockito</groupId>
	<artifactId>mockito-all</artifactId>
	<version>1.10.19</version>
	<scope>test</scope>
</dependency>
```

# 使い方

## インスタンスのモックを作成

### インスタンス全体をモック化

`mock`を用いると、ハリボテインスタンスを作り、その一部のメソッドに対して任意の返り値を設定できる。
> **【注意】**
> インスタンス自体はハリボテなので、挙動を定義しなかったメソッドは null などを返す。


```java
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class MockTest() {
	@Test
	public void mockTest() {
		// モックオブジェクト生成
		MyDBConnector con = mock(MyDBConnector.class);
		// 返り値を登録
		String[] records = {"Taro,20,male", "Hanako,18,female", ...};
		when(con.getAllRecords()).thenReturn(records);
		assertThat(con.getAllRecords(), is(records))
	}
}
```

### インスタンスの一部をモック化

完全なハリボテを作る`mock`と異なり、`spy`を使えば、インスタンスの他のメソッドの挙動は実装のままで、特定メソッドの返り値だけを指定することもできる。
> 使い方の例：
> - 以下のようなメソッドを持つクラスを想定
>   - 外部データベースへアクセスするメソッドA
>   - メソッドAで取得したデータを加工して返すメソッドB
> - メソッドAをモック化すれば、外部へのアクセスを伴わずメソッドBのテストができる

```java
import static org.mockito.Mockito.*;

public class HogeFuga() {
	public String hoge() { return "hoge"; }
	public String hogeFuga() { return hoge() + "-fuga" }
}

public class MockTest() {
	@Test
	public void spyMockitoTest() {
		HogeFuga hf = spy(HogeFuga.class);
		assertThat(hf.hogeFuga(), is("hoge-fuga"));
		doReturn("hoge-spy").when(hf).hoge();
		assertThat(hf.hogeFuga(), is("hoge-spy-fuga"));
	}
}
```

`doReturn`と`thenReturn`は記述スタイルだけの違いらしい。

## 種々の使い方

### 引数なしメソッドの返り値として任意の値を返す

```java
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class MockTest() {
	@Test
	public void mockTest() {
		// モックオブジェクト生成
		MyDBConnector con = mock(MyDBConnector.class);
		// 返り値を登録
		String[] records = {"Taro,20,male", "Hanako,18,female", ...};
		when(con.getAllRecords()).thenReturn(records);
		assertThat(con.getAllRecords(), is(records))
	}
}
```

### 引数ありメソッドの返り値として任意の値を返す

引数ありのメソッドでは、引数に応じて返り値を変えることもできる。

```
import static org.mockito.Matchers.anyString;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

public class MockTest() {
	@Test
	public void mockTest() {
		MyDBConnector con = mock(MyDBConnector.class);
		when(con.getAgeOf(anyString())).thenReturn("Unknown");
		when(con.getAgeOf("Taro")).thenReturn("20");
		when(con.getAgeOf("Hanako")).thenReturn("18");
		assertThat(con.getAgeOf("Jiro"), is("Unknown"));
		assertThat(con.getAgeOf("Taro"), is("20"));
		assertThat(con.getAgeOf("Hanako"), is("18"));
	}
}
```

> **【注意】**
> `anyString`,`anyInt`など任意引数を指すメソッドを使う場合は、具体的な引数の戻り値を定義するよりも先に使う。
> 例えば以下のように使った場合、`con.getAgeOf("Taro")`の値は "Unknown" になってしまう。
> ```java
> when(con.getAgeOf("Taro")).thenReturn("20");
> when(con.getAgeOf(anyString())).thenReturn("Unknown");
> when(con.getAgeOf("Hanako")).thenReturn("18");
> ```

### ネストしたオブジェクトのモック

モックオブジェクトの生成時に、第2引数として`RETURNS_DEEP_STUBS`を指定しておくと、モックオブジェクトのメソッドの返り値だけでなく、更にその返り値のメソッドにも任意の返り値を指定できる。

```
@Test
public class MockTest() {
	public void nestMockitoTest() {
		MyDBConnector con = mock(MyDBConnector.class, RETURNS_DEEP_STUBS);
		when(con.getLogs().indexOf(anyString())).thenReturn(0);
		when(con.getLogs().indexOf("A")).thenReturn(1);
		when(con.getLogs().indexOf("B")).thenReturn(2);
		assertThat(con.getLogs().indexOf("A"), is(1));
		assertThat(con.getLogs().indexOf("B"), is(2));
		assertThat(con.getLogs().indexOf("C"), is(0));
	}
}
```

### 返り値をコールバック形式で設定

`Answer`インターフェースを実装し、`thenAnswer`や`doAnswer`を使う。

```java
import org.mockito.invocation.InvocationOnMock;
import org.mockito.stubbing.Answer;

public class MockitoTest {
	@Test
	public void callbackAnswerMockitoTest() {
		MyDBConnector conMock = mock(MyDBConnector.class);
		doAnswer(new Answer() {
			public Object answer(InvocationOnMock invocation) {
				Object args[] = invocation.getArguments();
				return "record-" + args[0];
			}
		}).when(conMock).getMySQLRecord(anyString());
		assertThat(conMock.getMySQLRecord("hoge"), is("record-hoge"));
	}
}
```


### Mock 呼び出しごとに戻り値を変える

```java
public class MockitoTest {
	@Test(expected = NoSuchElementException.class)
	public void iteratorMockitoTest() {
		MyDBConnector conMock = mock(MyDBConnector.class);
		when(conMock.getMySQLRecord(anyString()))
				.thenReturn("1")
				.thenReturn("2")
				.thenReturn("3")
				.thenThrow(new NoSuchElementException());
		assertThat(conMock.getMySQLRecord("hoge"), is("1"));
		assertThat(conMock.getMySQLRecord("hoge"), is("2"));
		assertThat(conMock.getMySQLRecord("hoge"), is("3"));
		conMock.getMySQLRecord("hoge");
	}
}
```

### 一部のメソッドだけ実際のものを使う

```
public class MockitoTest() {
	@Test
	public void callRealMethodMockitoTest() {
		MyDBConnector conMock = mock(MyDBConnector.class);
		assertThat(conMock.hoge(), nullValue());
		when(conMock.hoge()).thenCallRealMethod();
		assertThat(conMock.hoge(), is("hoge"));
	}
}
```
