---
title: screen
---

工事中。

# 概要

1つの端末で複数の仮想端末を開いて利用できる。

リモートサーバにログインし、時間のかかる処理をさせている最中にサーバとの接続が切れると通常は処理が中断されるが、screen セッション中で実行中の処理は（そのセッションからデタッチ済みであれば）サーバとの接続が切れても処理が継続する。

| 用語 | 説明 |
| :-- | :-- |
| ウィンドウ | 各仮想端末のこと。 |
| セッション | screen コマンドで取り扱う、ウインドウのひとまとまり。 |
| デタッチ | アクティブなセッションから離脱すること。プロセスは生存し続ける。 |
| アタッチ | デタッチしたセッションに再接続すること。 |
|  |  |

# 使い方

## コマンド

| コマンド | 説明 |
| :-- | :-- |
| `screen` | 新しいセッションを開始 |
| `screen -S ${SESSION_NAME}` | 名前をつけて新しいセッションを開始 |
| `screen -ls` | セッション一覧を表示 |
| `screen -r ${PID}` | 指定したセッションにアタッチ |
| `screen -d` | セッションからデタッチする |
| `rm -rf /var/run/screen/S-${USERNAME}/*` | セッションの一括削除 |

## screen セッション内の操作

| 操作 | 説明 |
| :-- | :-- |
| Ctrl+a d | セッションからデタッチする |
| Ctrl+a c | セッションに新しいウインドウを作る |
| Ctrl+a space | 昇順にウインドウを切り替え |
| Ctrl+a  |  |
| Ctrl+a  |  |
|  |  |