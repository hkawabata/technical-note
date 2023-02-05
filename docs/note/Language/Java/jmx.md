---
title: JMX
---

# JMX とは

Java Management Extensions の略。
Java アプリケーションやデバイス、サービス、JVM の管理・モニタリングを行う API。

# 有効化

起動時に以下のパラメータを渡す必要あり

```java
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=1234
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.authenticate=false
```

# アプリケーションの任意の値をモニタリング

http://blog.cybozu.io/entry/2018/02/05/080000
https://github.com/jersey/jersey/tree/master/examples/monitoring-webapp
https://docs.oracle.com/javase/jp/8/docs/technotes/guides/jmx/tutorial/tutorialTOC.html
https://www.eclipse.org/jetty/documentation/9.3.x/jmx-chapter.html#custom-monitor-applcation
https://docs.oracle.com/javase/jp/7/api/java/lang/management/ManagementFactory.html
