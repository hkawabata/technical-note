---
title: selenium-java
---

# pom.xml の設定

```xml
<!-- https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java -->
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>3.14.0</version>
</dependency>
<!-- https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-chrome-driver -->
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-chrome-driver</artifactId>
    <version>3.14.0</version>
</dependency>
```

# 使い方

(TODO)

# トラブルシューティング

## エラー

### element is not attached to the page document

```
org.openqa.selenium.StaleElementReferenceException: stale element reference: element is not attached to the page document
```

このときは、ページ遷移前に取得した`WebElement`をそのまま遷移後も使い回そうとしたことが原因？（遷移前後が同一ページなので使い回そうとした）
毎回新しく取得するようにすると解消した。

### element is not clickable at point ...

```
java.lang.Exception: org.openqa.selenium.WebDriverException: unknown error: Element <a name="..." id="...">...</a> is not clickable at point (382, 572). Other element would receive the click: <div id="..."></div>
```
