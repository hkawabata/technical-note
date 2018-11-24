---
title: (WIP) 実行時オプション
---

[このページ](https://docs.oracle.com/javase/jp/8/docs/technotes/tools/windows/java.html)が詳しい。

# 標準オプション

# 非標準オプション

## -Xms${size}

ヒープの初期サイズ(バイト単位)。
- 条件
  - 1024の倍数
  - 設定値 > 1M
- k/K,m/M,g/G が使える（ex.`-Xms12m`）

## -Xmx${size}

メモリー割当てプールの最大サイズ(バイト単位)。
- 条件
  - 1024の倍数
  - 設定値 > 2M
- `-XX:MaxHeapSize`と同等

# 拡張ランタイム・オプション

# 拡張 JIT コンパイラオプション

# 拡張保守性オプション

# 拡張ガベージ・コレクション・オプション
