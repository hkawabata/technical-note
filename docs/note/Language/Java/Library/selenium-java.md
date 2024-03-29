---
title: Selenium
---

# 概要

スクレイピングを行うためのライブラリ。

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

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class App {
    public static void main(String[] args) {
        // WebDriver 生成
        System.setProperty("webdriver.chrome.driver", "./exe/chromedriver-v101-mac64");
        WebDriver driver = new ChromeDriver();

        // ウェブページへアクセス
        driver.get("https://ja.wikipedia.org/?curid=4105812");

        // ページの要素を取得
        WebElement toc = driver.findElement(By.id("toc"));
        List<WebElement> aTags = driver.findElements(By.className("contentslist"));

        // ページの要素から情報を抽出
        for (WebElement aTag : aTags) {
            String href = aTag.getAttribute("href");
            System.out.println(href);
        }
  }
}
```

## 条件を満たす html タグを探す

### メソッド

| メソッド | 説明 |
| :-- | :-- |
| `driver.findElement(By by)` | 条件を満たす `WebElement` を1つ探す<br>1つも存在しない場合は例外発生？（要確認） |
| `driver.findElements(By by)` | 条件を満たす `WebElement` を全て探す<br>1つも存在しない場合は空コレクション？（要確認） |

### 条件指定

`By` クラスのメソッドを使う。

| メソッド | 説明 |
| :-- | :-- |
| `By.id("xxx")` | タグの id を指定 |
| `By.className("xxx")` | タグの class を指定 |
| `By.tagName("xxx")` | html タグ名を指定 |
| `By.linkText("xxx")` | リンクテキストの文字列を指定（完全一致） |
| `By.partialLinkText("xxx")` | リンクテキストの文字列を指定（部分一致） |

## html タグからの情報抽出

| メソッド | 説明 |
| :-- | :-- |
| `webElement.getAttribute("xxx")` | 属性名から属性値を取得 |
| `webElement.getTagName()` | 要素のタグ名を取得 |
| `webElement.getText()` | タグに囲まれた内部テキストを取得 |
| `webElement.getCssValue("xxx")` | CSS プロパティ名から CSS プロパティ値を取得 |



# TIPS
ヘッドレスブラウザを使う

```java
ChromeOptions options = new ChromeOptions();
options.addArguments("--headless");
System.setProperty("webdriver.chrome.driver", "./exe/chromedriver-v101-mac64");
WebDriver driver = new ChromeDriver(options);
```

# トラブルシューティング

## エラー

### element is not attached to the page document

`WebElement`をクリックしようとしたときに発生。

```
org.openqa.selenium.StaleElementReferenceException: stale element reference: element is not attached to the page document
```

このときは、ページ遷移前に取得した`WebElement`をそのまま遷移後も使い回そうとしたことが原因？（遷移前後が同一ページなので使い回そうとした）
毎回新しく取得するようにすると解消した。

### element is not clickable at point ...

`WebElement`をクリックしようとしたときに発生（Chrome で確認）。

```java
WebElement elem = driver.findElement(By.id("hoge"));
elem.click();
```

```
java.lang.Exception: org.openqa.selenium.WebDriverException: unknown error: Element <a name="..." id="...">...</a> is not clickable at point (382, 572). Other element would receive the click: <div id="..."></div>
```

【原因】

クリック対象の要素が、ブラウザの表示領域に入っていない。

【対策】

`org.openqa.selenium.interactions.Actions`のインスタンスを作るだけで OK。

```java
Actions action = new Actions(driver);
WebElement elem = driver.findElement(By.id("hoge"));
elem.click();
```

こうすると表示対象の要素がある場所までスクロールしてくれるようになる。

### session not created exception

もう一度実行すると成功した。セッションがちゃんと張られるまで待つ必要がある？

```
Exception in thread "main" java.lang.ExceptionInInitializerError
Caused by: org.openqa.selenium.SessionNotCreatedException: session not created exception
from disconnected: received Inspector.detached event
```
