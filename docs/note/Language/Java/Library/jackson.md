---
title: Jackson
---

# Jackson とは

JSON のパースを行う Java ライブラリ。

# 使用するための設定

## pom.xml

```xml
<dependency>
	<groupId>com.fasterxml.jackson.core</groupId>
	<artifactId>jackson-databind</artifactId>
	<version>2.6.5</version>
</dependency>
<dependency>
	<groupId>com.fasterxml.jackson.core</groupId>
	<artifactId>jackson-core</artifactId>
	<version>2.6.5</version>
</dependency>
<dependency>
	<groupId>com.fasterxml.jackson.core</groupId>
	<artifactId>jackson-annotations</artifactId>
	<version>2.6.5</version>
</dependency>
```

## build.sbt の設定

```scala
libraryDependencies ++= Seq(
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.6.5",
  "com.fasterxml.jackson.core" % "jackson-core" % "2.6.5",
  "com.fasterxml.jackson.core" % "jackson-annotations" % "2.6.5"
)
```

# 簡単なサンプル

```json
{
    "group_name": "GLAY",
    "member": [
        {"name": "TERU", "age": 46},
        {"name": "TAKURO", "age": 46},
        {"name": "HISASHI", "age": 45},
        {"name": "JIRO", "age": 44}
    ]
}
```

```java
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;

public class Main {
	public static void main (String args[]) {
		ObjectMapper mapper = new ObjectMapper();
		JsonNode root = mapper.readTree(new File("test.json"));
		// member -> 2番目の要素 -> name
		String name = root.get("member").get(2).get("name");
	}
}
```

## JSON → Java のオブジェクト

- JsonNode オブジェクト（木構造）に変換
```java
String filename = "hogehoge.json";
ObjectMapper mapper = new ObjectMapper();
JsonNode root = mapper.readTree(new FIle(filename));
```

- 指定したクラスにマップして変換

```java
mapper.readValue(String str, Hoge.class)
mapper.readValue(File file, Hoge.class)
```

第二引数は`String.class`などを指定する。
配列であれば`String[].class`、List や Map など型引数を持つクラスであれば`new TypeReference<List<String>>(){}`のようにする。

## Java のオブジェクト → JSON

```java
mapper.writeValueAsString(Object object)
```

# Tips

## 値が null のフィールドは JSON 文字列に含めない

```java
ObjectMapper mapper = new ObjectMapper().setSerializationInclusion(JsonInclude.Include.NON_NULL)
```

## JSON フィールドとは関係のないクラス変数を定義する

JSON ⇔ Java オブジェクトの変換において、変換対象とは見做さない変数を定義できる。

```java
@JsonIgnore
public int ignored;
```

クラス宣言の前に`@JsonIgnoreProperties`アノテーションをつければ複数まとめて無視できる。

```java
@JsonIgnoreProperties({"id", "age"})
public class Hoge {
    public int id;
    public String name;
    public int age;
}
```



## JSON フィールドのうち特定のものだけをオブジェクトにマッピングする

```java
public class Person {
	public static int id;
	puclic static String name;
}
```

```json
{
	"id": 1,
	"name": "Taro",
	"age": 18
}
```

JSON に存在するフィールドのうち一部だけを Java のクラスにマッピングしたいとき、適切に設定をしないと`org.codehaus.jackson.map.exc.UnrecognizedPropertyException`が発生する。
以下の設定をしておけば回避できる。

```java
objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

## setter, getter を定義する

JSON をマッピングするクラスに setter, getter を定義すると、Jackson はエラーを吐く。
`@JsonIgnore`アノテーションをつければ問題は起こらない。

```java
@JsonIgnore
public void setHoge(String hoge) { ... }

@JsonIgnore
public String getHoge(String hoge) { ... }
```

## Scala で使うとき

以下のような処理をしようとすると、`foreach is not ***` というエラー。

```scala
for (node <- root) {
	...
}
```


## JSON を比較する

JSON が途中に配列を含む時、順番に関わらず等価性を判定したい場合は、

```
// Scala の場合
mapper.readValue("[1,3,2,5,4]", classOf[Set[Int]])
```

のように Set として読み込んで比較すれば良い。


## JSON フィールド名とは異なるオブジェクトフィールド名を使う

以下のようにフィールドを定義すれば良い。
この例では、JSON フィールド名は "sex", Java オブジェクトとしてのフィールド名は "gender" になる。

```java
@JsonProperty("sex")
public String gender;
```

## デシリアライズ時に使われるコンストラクタやファクトリーメソッドを定義する

JSON を Java オブジェクトにデシリアライズする際、通常はデフォルトコンストラクタが利用される。
`@JsonCreator`を使うことで、デシリアライズ時に利用するコンストラクタやファクトリーメソッドを定義・指定できる。

```java
public class Hoge {
    public int id;
    public String name;
    public char initial;

    @JsonCreator
    Hoge(@JsonProperty("id") int id, @JsonProperty("name") String name) {
        this.id = id;
        this.name = name;
        this.initial = name.charAt(0);
    }
}
```

```java
public class Hoge {
    public int id;
    public String name;
    public char initial;

    @JsonCreator
    public static Hoge create(@JsonProperty("id") int id, @JsonProperty("name") String name) {
        return new Hoge(id, name);
    }

    private Hoge (int id, String name) {
        this.id = id;
        this.name = name;
        this.initial = name.charAt(0);
    }
}
```

## 型情報を JSON に出力する

クラスのフィールドだけでなく、そのクラスの型情報を合わせて JSON に含めることができる。
この情報はデシリアライズ時に必要になることがある。

```java
@JsonTypeInfo(use=JsonTypeInfo.Id.CLASS)
public class Hoge {
    public int id;
    public String name;
}
```

このクラスのインスタンスを JSON として書き出すと以下のようになる

```json
{"@class":"sample.jackson.Hoge","id":10,"name":"hoge"}
```

`use=JsonTypeInfo.Id.NAME`とすれば、FQCN ではなくクラスの単純名が書き込まれる

```json
{"@class":"Hoge","id":10,"name":"hoge"}
```

## Map 型のフィールドをフラットに展開する

```java
public class Hoge {
    private String name;

    private Map<String, String> props = new HashMap<>();
    
    private Map<String, String> props2 = new HashMap<>();

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Map<String, String> getProps() {
        return props;
    }

    public void setProps(Map<String, String> props) {
        this.props = props;
    }

    @JsonAnyGetter
    public Map<String, String> getProps2() {
        return props2;
    }

    public void setProps2(Map<String, String> props2) {
        this.props2 = props2;
    }
}
```

```java
Hoge h = new Hoge();
h.setName("bean");
h.getProps().put("key1", "value1");
h.getProps().put("key2", "value2");
h.getProps2().put("key3", "value3");
h.getProps2().put("key4", "value4");

ObjectMapper objectMapper = new ObjectMapper().enable(SerializationFeature.INDENT_OUTPUT);
String json = objectMapper.writeValueAsString(h);
System.out.println(json);
```

```json
{
  "name" : "hoge",
  "props" : {
    "key1" : "value1",
    "key2" : "value2"
  },
  "key3": "value3",
  "key4": "value4"
}
```

Scala の case class では動かないらしく、通常のクラスを使う必要がある（2019/9/10時点）。

https://github.com/FasterXML/jackson-module-scala/issues/308
