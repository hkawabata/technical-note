---
title: Log4J
---

# pom.xml の設定

```xml
<!-- https://mvnrepository.com/artifact/log4j/log4j -->
<dependency>
  <groupId>log4j</groupId>
  <artifactId>log4j</artifactId>
  <version>1.2.17</version>
</dependency>
```

# log4j.xml

クラスパスの通ったところ（src/main/resources とか）に置く。このファイルではなく、**コード内部で設定しても良い**。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE log4j:configuration SYSTEM "log4j.dtd">
<log4j:configuration xmlns:log4j="http://jakarta.apache.org/log4j/" >

    <appender name="stdout" class="org.apache.log4j.ConsoleAppender">
        <param name="Target" value="System.out" />
        <layout class="org.apache.log4j.PatternLayout">
            <param name="ConversionPattern" value="%m%n" />
        </layout>
    </appender>

    <root>
        <appender-ref ref="stdout"/>
    </root>
</log4j:configuration>
```


# 使い方

## Logger

## Appender

ログの出力先（標準出力、ファイル、メール、リモートサーバ、etc...）を決定するインターフェース。これを実装したクラスの中から使いたいものを`Logger`にセットする。

```java
Appender appender = new ConsoleAppender();
logger.addAppender(appender);
```

### ConsoleAppender


**【注意】**
`ConsoleAppender`の実装は以下のようになっている。そのため、引数なしでコンストラクタを呼び出し（`new ConsoleAppender()`）、かつレイアウトを設定する場合、`setLayout()`だけでなく`setTarget()`, `activateOptions()`も呼び出す必要がある。

```java
public ConsoleAppender(Layout layout) {
    this(layout, SYSTEM_OUT);
}

public ConsoleAppender(Layout layout, String target) {
    setLayout(layout);
    setTarget(target);
    activateOptions();
}
```

### FileAppender

### RollingFileAppender

### DailyRollingFileAppender

### AsyncAppender


## Layout

出力フォーマットを決定するインターフェース。
単純なもの以外にもユーザが指定できるフォーマット、HTML のテーブルに即したフォーマットなどがある。

```java
PatternLayout layout = new PatternLayout();
layout.setConversionPattern("%-4r [%t] %-5p %c %x - %m%n");
```

# log4j.properties を使う方法

src/main/resources などに log4j.properties ファイルを置いておくと、特にプログラム内部で明示的に読み込まなくても設定を反映してくれる。

```
# logger
log4j.rootLogger=INFO, file

# file appender
log4j.appender.file=org.apache.log4j.DailyRollingFileAppender
log4j.appender.file.File=/path/to/log/file.log
log4j.appender.file.DatePattern='.'yyyyMMdd
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=%d{yyyy/mm/dd HH:mm:ss} %-5p %m%n
log4j.appender.file.encoding=UTF-8
```
