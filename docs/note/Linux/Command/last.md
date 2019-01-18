---
title: last
---

# 概要

ユーザーのログイン履歴を参照する。
- telnet や ftp によるアクセスも含む
- シャットダウン情報も取得できる

# 使い方

```bash
$ last
hkawabata pts/4        xxx.xxx.xxx.xxx Fri Jan 18 12:58   still logged in   
xxxxxx    pts/3        xxx.xxx.xxx.xxx Fri Jan 18 12:18   still logged in   
yyyyyyyy  pts/0        xxx.xxx.xxx.xxx Fri Jan 18 09:38   still logged in   
hkawabata pts/5        :pts/0:S.0      Thu Jan 17 13:03 - 14:17  (01:13) 
xxxxxx    pts/3        :pts/0:S.0      Thu Jan 17 11:36 - 14:55  (03:18)

$ last <username>
```

# オプション

# Tips
