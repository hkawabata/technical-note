---
title: HDFS
---

（書きかけ）

# コマンド覚書

| コマンド | 説明 | 備考 |
| :-- | :-- | :-- |
| `hdfs dfs -ls` |  |  |
| `hdfs dfs -mv` |  |  |
| `hdfs dfs -cp` |  |  |
| `hdfs dfs -rm` |  |  |
| `hdfs dfs -count <path>` | ディレクトリ数,ファイル数,サイズを出力 |  |
| `hdfs dfs -count -q -h <path>` | QUOTA, REMAINING_QUOTA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, DIR_COUNT, FILE_COUNT, CONTENT_SIZE, FILE_NAME |  |
| `hdfs dfs -stat <format> <path>` | 指定パスの状態を指定したフォーマットで出力 | %n : 名前<br>%b : ファイルサイズ<br>%o : ブロックサイズ<br>%r : レプリケーション数<br>%y : 最終更新日時 |
| `hdfs dfs -test <option> <path>` | オプションに応じてパスの条件判定を行う<br>条件に該当すれば0、該当しなければ1が return される | オプション：<br>`-e`：パスが存在するか<br>`-d`：ディレクトリかどうか<br>`-z`：中身がゼロバイトかどうか（存在しないパスを指定するとエラー） |
|  |  |  |
|  |  |  |
