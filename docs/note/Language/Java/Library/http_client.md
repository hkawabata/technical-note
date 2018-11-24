---
title: HttpClient
---

# 資料

- [HttpClient Tutorial](https://hc.apache.org/httpcomponents-client-ga/tutorial/pdf/httpclient-tutorial.pdf)

# 使い方

HTTP/1.1 が定義する各リクエストメソッドに対応する下記のインスタンスを作成し、クライアントオブジェクトからリクエストを実行する。

- `HttpGet`
- `HttpHead`
- `HttpPost`
- `HttpPut`
- `HttpDelete`
- `HttpTrace`
- `HttpOptions`

```java
CloseableHttpClient httpclient = HttpClients.createDefault();
HttpGet httpget = new HttpGet("http://localhost/");
CloseableHttpResponse response = httpclient.execute(httpget);
try {
	<...>
} finally {
	response.close();
}
```

URI のビルダーも備える。

```java
URI uri = new URIBuilder()
        .setScheme("http")
        .setHost("www.google.com")
        .setPath("/search")
        .setParameter("q", "httpclient")
        .setParameter("btnG", "Google Search")
        .setParameter("aq", "f")
        .setParameter("oq", "")
        .build();
HttpGet httpget = new HttpGet(uri);
```
