---
title: nslookup
---

# 概要

以下の用途で利用されるコマンド。
-   ドメイン名から IP アドレスを確認
-   IP アドレスからドメイン名を確認
-   特定の DNS レコードの確認


# 使い方

## ドメイン名から IP アドレスを確認

```bash
$ nslookup google.com

Server:		172.xxx.xxx.xxx    # 問い合わせ先のDNSサーバの情報
Address:	172.xxx.xxx.xxx    # 問い合わせ先のDNSサーバの情報

Non-authoritative answer:      # 問い合わせを行ったDNSサーバではなく、別のDNSサーバに登録されている情報であることを表す
Name:	google.com             # 問い合わせ結果: ホスト名
Address: 216.58.220.110        # 問い合わせ結果: IPアドレス
```

## IP アドレスからドメイン名を確認

```bash
$ nslookup 216.58.220.110

Server:		172.xxx.xxx.xxx
Address:	172.xxx.xxx.xxx

Non-authoritative answer:
110.220.58.216.in-addr.arpa	name = syd10s01-in-f110.1e100.net.
110.220.58.216.in-addr.arpa	name = nrt12s30-in-f14.1e100.net.

Authoritative answers can be found from:
```


# オプション

# Tips