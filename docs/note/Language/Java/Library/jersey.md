---
title: Jersey
---


User Guide：
https://jersey.github.io/documentation/latest/user-guide.html

# 登場人物

## pom.xml

```xml
<dependency>
    <groupId>org.glassfish.jersey.containers</groupId>
    <artifactId>jersey-container-servlet</artifactId>
    <version>2.27</version>
    <scope>provided</scope>
</dependency>
```

アプリケーションサーバとして GlassFish を使う場合は、サーバ側の jar に含まれているため`<scope>provided</scope>`として良い

## javax.ws.rs.core.Application のサブクラス

アプリケーションのルート？

```java
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;

@ApplicationPath("/")
public class MyApp extends Application {}
```

中身は空でも良い。その場合、定義したサーブレットクラスが全て読み込まれる。

`javax.ws.rs.core.Application`を拡張した`org.glassfish.jersey.server.ResourceConfig`を使うと Dependency Injection とかできて便利？



## サーブレットクラス

```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/")
public class MyAppResource {
    @GET
    @Produces(MediaType.TEXT_HTML)
    public String rootPage() {
        return "<html><body><h1>Root Page</h1></body></html>";
    }

    @GET
    @Path("/xml")
    @Produces(MediaType.APPLICATION_XML)
    public String xml() {
        return "<tag>sample xml</tag>";
    }

    @GET
    @Path("/json")
    @Produces(MediaType.APPLICATION_JSON)
    public String json() {
        return "{\"num\": 100}";
    }
}
```

### @Path

- URI の相対パスを表す
- クラスにもメソッドにも付与できる
- パスの一部を`{}`で囲むと、`@PathParam`アノテーションで変数として取り出すことができる

```java
@Path("/users/{username}")
public class UserResource {
    @GET
    @Produces("text/xml")
    public String getUser(@PathParam("username") String userName) {
        ...
    }
}
```

### @GET, @PUT, @POST, @DELETE, ...

- Java のメソッドを HTTP メソッドに対応させる


### @Produces

- リソースが返却する MIME タイプ（text/plain など）を表す
- クラスにもメソッドにも付与できる

```java
@Path("/")
public class SomeResource {
    @GET
    @Path("/acceptTypeTest")
    @Produces(MediaType.APPLICATION_JSON)
    public String acceptTypeTestOnlyJSON() {
        return "{\"result\": \"JSON が要求されたため JSON 形式で返却します。\"}";
    }
    @GET
    @Path("/acceptTypeTest")
    @Produces({MediaType.APPLICATION_XML, MediaType.TEXT_XML})
    public String acceptTypeTestOnlyXML() {
        return "<result>XML が要求されたため XML 形式で返却します</result>";
    }
    @GET
    @Path("/acceptTypeTest")
    public String acceptTypeTestAny() {
        return "JSON/XML ともに Accept ヘッダに含まれなかったため、plain/text を返却します";
    }
}
```

```bash
$ curl --dump-header - -H 'Accept:text/xml' http://localhost:8080/acceptTypeTest
...
Content-Type: text/xml
...
<result>XML が要求されたため XML 形式で返却します</result>

$ curl --dump-header - -H 'Accept:application/xml' http://localhost:8080/acceptTypeTest
...
Content-Type: application/xml
...
<result>XML が要求されたため XML 形式で返却します</result>

$ curl --dump-header - -H 'Accept:application/json' http://localhost:8080/acceptTypeTest
...
Content-Type: application/json
...
{"result": "JSON が要求されたため JSON 形式で返却します。"}

$ curl --dump-header - -H 'Accept:plain/text' http://localhost:8080/acceptTypeTest
...
Content-Type: plain/text
...
JSON/XML ともに Accept ヘッダに含まれなかったため、plain/text を返却します
```


### @Consumes

- リソースが受け付ける MIME タイプを表す


### @*Param

- リソースメソッドの引数としてリソースのパスやリクエストパラメータなどから値を取ってくる

| アノテーション | 説明 |
| :-- | :-- |
| `@MatrixParam` |  |
| `@HeaderParam` |  |
| `@CookieParam` |  |
| `@FormParam` |  |
| `@QueryParam` |  |
| `@PathParam` |  |

```java
@Path("/")
public class SomeResource {
	@GET
	@path("/search/user/{username}")
	public String func(
		@DefaultValue("10") @QueryParam("max-response") int maxResponse,
		@PathParam("username") String userName
	) {
		...
	}
}
```

**String 1つを引数とするコンストラクタを持てば**、ユーザ定義のクラスへマッピングすることもできる。

```java
public class MyObject {
	public String str;
	public MyObject(String s) {
		this.str = s;
	}
}

@Path("/")
public class SomeResource {
	@GET
	public String func(
		@DefaultValue("default") @QueryParam("s") MyObject myObj
	) {
		...
	}
}
```



## web.xml



# Dependency Injection

`javax.ws.rs.core.Application`を拡張した`org.glassfish.jersey.server.ResourceConfig`を使う。

## サンプルコード

```java
public interface IMyString {
	String s();
}
```

```java
public class MyString implements IMyString {
	public long instanceCreatedTimeNano;

    public MyString() {
        this.instanceCreatedTimeNano = System.nanoTime();
    }
    
	String s() {
		return "created: " + instanceCreatedTimeNano;
	}
}
```

```java
import org.glassfish.hk2.utilities.binding.AbstractBinder;
import org.glassfish.jersey.server.ResourceConfig;

import javax.inject.Singleton;
import javax.ws.rs.ApplicationPath;

@ApplicationPath("/")
public class MyApplication extends ResourceConfig {
    public MyApplication() {
        packages(getClass().getPackage().getName());
        register(new AbstractBinder() {
            @Override
            protected void configure() {
            bind(MyString.class).to(IMyString.class);
            //bind(MyString.class).to(IMyString.class).in(Singleton.class);
            }
        });
    }
}
```

```java
import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/")
public class MyAppResource {
	@Inject
	IMyString myStr;
	
	@GET
	public String get() {
		return myStr.s();
	}
}
```

## Singleton

`ResourceConfig`において

1. `.in(Singleton.class)`をつけないで bind した場合、アクセスの都度インスタンスが作られるため毎回結果が変わる：
```
// curl http://${app_server}:${port}
created: 4651889700541
created: 4654055891730
created: 4655392680232
created: 4656127701837
created: 4656978541467
created: 4657311692444
...
```
2. `.in(Singleton.class)`をつけて bind した場合、**最初のアクセス時（アプリケーションサーバの起動時ではない※）**にしかインスタンスが作られないため何度叩いても結果は変わらない：
```
// curl http://${app_server}:${port}
created: 4782770088054
created: 4782770088054
created: 4782770088054
created: 4782770088054
created: 4782770088054
created: 4782770088054
...
```

※ Singleton インスタンスの生成が起動時ではないことを確認するため、上の例の`MyString`のコンストラクタを以下のように書き換え、アプリケーションサーバ起動から数十秒待ってから curl で複数回叩く実験を実施。

```java
public MyString() throws InterruptedException {
	this.instanceCreatedTimeNano = System.nanoTime();
	Thread.sleep(2000L);
}
```

```bash
$ time curl http://${app_server}:${port}
created: 6900775283199
real	0m2.191s
user	0m0.007s
sys	0m0.010s
# 初回はレスポンスに2秒以上かかっている

$ time curl http://${app_server}:${port}
real	0m0.024s
user	0m0.007s
sys	0m0.008s
# 2回目以降はすぐにレスポンスが返る
```


# TIPS

## javax.ws.rs.core.Application と web.xml の関係

| Application クラスのサブクラス | web.xml |
| :-- | :-- |
| サブクラスが定義されていない | web.xml に servlet-mapping が必要 |
| サブクラスが定義され、`@ApplicationPath`アノテーションがついている | web.xml 不要 |
| サブクラスが定義され、`@ApplicationPath`アノテーションが定義されていない | web.xml に servlet-mapping が必要 |
