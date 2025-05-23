---
title: Trino (Presto)
main_image: https://user-images.githubusercontent.com/13412823/255066907-23ea48b2-c633-4a80-b7a6-f29960a5a3ff.png
---

# Trino (Presto) とは

- Presto：[Hive](hive.md) クエリ処理の遅さを解決するために Facebook で開発された OSS
- Trino：Presto から名称変更


# Hive と Trino の違い

## アーキテクチャ


## Quely Language


# Trino SQL

## 予約語と同じ名前のフィールドにアクセス

例えば `ORDER BY` 句で使う `order` という名前のフィールドが `data` に含まれる場合：

```sql
SELECT
  data."order"
FROM
  db.my_table
```


## 値の操作

### 別の型にキャスト

```sql
SELECT
  *
FROM
  db.my_table
ORDER BY
  CAST(sales_priority AS INTEGER)
```

この書き方だと、整数型にキャストしたいフィールドに null や数字以外の文字列が含まれている場合、エラーになる。

エラーを避け、このような場合に null を返すには `TRY_CAST` を使う：

```sql
TRY_CAST(sales_priority AS INTEGER)
```


## 配列操作

### 配列の長さ

```sql
SELECT
  cardinality(my_array)
FROM
  db.my_table
```

### 配列を flatten

```sql
SELECT
  r.record_id
FROM
  db.my_table
  CROSS JOIN UNNEST(records) AS r
```

複数の配列型フィールド `records`, `records2` があり、
- `records` と `records2` の長さが同じ
- `records` と `records2` の要素のフィールド名が重複しない
という条件を満たす時、複数の配列をまとめて flatten できる。

```sql
SELECT
  r.record_id,
  r.record2_id
FROM
  db.my_table
  CROSS JOIN UNNEST(records, records2) AS r
```


## 集約関数

`GROUP BY` 句でまとめたレコードに対する集約関数。


### COUNT

指定したフィールドの件数を集計。`DISTINCT`をつけることで重複を排除して集計。

```sql
SELECT
  category,
  COUNT(record_id),
  COUNT(DISTINCT record_id)  -- 値の重複を排除して集計する場合
FROM
  db.my_table
GROUP BY
  category
```

### ARRAY_AGG

指定したフィールドを配列として取得。

- `ORDER BY` 句でソート済み配列にできる
- `DISTINCT` で重複を除いて配列にできる

```sql
SELECT
  category,
  COUNT(record_id),
  COUNT(record_id ORDER BY record_id),  -- ソート済み配列として取得
  COUNT(DISTINCT record_id ORDER BY record_id)  -- ソート済み重複なし配列として取得
FROM
  db.my_table
GROUP BY
  category
```