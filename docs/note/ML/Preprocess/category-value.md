---
title: カテゴリデータの変換
---

# カテゴリデータ

現実のデータセットの特徴量およびクラスラベルには、数値だけでなくカテゴリ値がしばしば含まれる。  
機会的に扱うには、特徴量は数値であることが望ましい。

| サンプル番号 | クラスラベル | サイズ | 色 | 価格 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | A | S | blue | 100 |
| 2 | B | S | red | 200 |
| 3 | C | M | green | 300 |
| 4 | C | L | red | 400 |
| 5 | B | M | red | 500 |

- **順序特徴量**: S < M < L のように順序付けが可能なカテゴリ値
- **名義特徴量**: blue, red, green のように順序付けができないカテゴリ値

## クラスラベルのエンコーディング

適当に A = 1, B = 2, C = 3 などと置き換える。  
**ラベルを区別さえできれば良く、数値の大小に意味はない**。

| サンプル番号 | クラスラベル | サイズ | 色 | 価格 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 1 | S | blue | 100 |
| 2 | 2 | S | red | 200 |
| 3 | 3 | M | green | 300 |
| 4 | 3 | L | red | 400 |
| 5 | 2 | M | red | 500 |

## 順序特徴量のマッピング

S = 1, M = 2, L = 3 のように順序を守って置き換えれば良い。

| サンプル番号 | クラスラベル | サイズ | 色 | 価格 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 1 | 1 | blue | 100 |
| 2 | 2 | 1 | red | 200 |
| 3 | 3 | 2 | green | 300 |
| 4 | 3 | 3 | red | 400 |
| 5 | 2 | 2 | red | 500 |

## 名義特徴量のエンコーディング

クラスラベルと同様に、適当に blue = 1, red = 2, green = 3 などと置き換えるのはダメ。  
**実際には blue, red, green は等価であるにも関わらず、学習において「blue < red < green」という大小関係を前提としてモデルを学習してしまう**。

→ **one-hot エンコーディング**：特徴量のユニークな値1つごとに **ダミー特徴量** を作り、その値を取るときに1、取らないときに0を付与

| サンプル番号 | クラスラベル | サイズ | 色-blue | 色-red | 色-green | 価格 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 1 | 1 | 1 | 0 | 0 | 100 |
| 2 | 2 | 1 | 0 | 1 | 0 | 200 |
| 3 | 3 | 2 | 0 | 0 | 1 | 300 |
| 4 | 3 | 3 | 0 | 1 | 0 | 400 |
| 5 | 2 | 2 | 0 | 1 | 0 | 500 |