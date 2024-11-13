---
title: GeoJSON
---
# GeoJSON とは

JSON を元にした、ウェブマップで利用する代表的なデータフォーマット。


# 書式

## 点データ

### 1地点

```json
{
  "type": "Point",
  "crs": {
    "type": "name",
    "properties": {
      "name": "xxxx"
    }
  },
  "coordinates": [139.691722, 35.689501]
}
```

### 2地点

```json
{
  "type": "MultiPoint",
  "crs": {
    "type": "name",
    "properties": {
      "name": "xxxx"
    }
  },
  "coordinates": [
    [139.691722, 35.689501],
    [135.520037, 34.686344]
  ]
}
```


## 線データ

```json
{ "type": "LineString",
  "crs": {
    "type": "name",
    "properties": {
      "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
    }
  },
  "coordinates": [
    [139.691722, 35.689501],
    [135.520037, 34.686344]
  ]
}
```

## 面データの作成

- 始点（配列の最初の座標）と終点（配列の最後の画像）の座標を同じにする必要あり
- 配列が3重になっている点に注意（なぜ？複数の面を記述できる仕様？）

```json
{
  "type": "Polygon",
  "crs": { "type": "name",
    "properties": {
      "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
    }
  },
  "coordinates": [
    [
      [139.691722, 35.689501],
      [140.123154, 35.604560],
      [139.642537, 35.447734],
      [139.691722, 35.689501]
    ]
  ]
}
```


## 複数の要素を作成

`FeatureCollection` を使う。

- `Point`：東京
- `LineString`：東京 - 大阪
- `Polygon`：東京 - 千葉 - 神奈川

の3つを1つのファイルで表現。

```json
{
  "type": "FeatureCollection",
  "crs": {
    "type": "name",
    "properties": {
      "name": "xxx"
    }
  },
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Point",
        "coordinates": [
          [139.691722, 35.689501]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [139.691722, 35.689501],
          [135.520037, 34.686344]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [139.691722, 35.689501],
            [140.123154, 35.604560],
            [139.642537, 35.447734],
            [139.691722, 35.689501]
          ]
        ]
      }
    }
  ]
}
```

<img width="500" alt="スクリーンショット 2024-09-08 22 15 11" src="https://gist.github.com/user-attachments/assets/22c2df84-31d9-4456-998e-46b50e1f93ae">


# GeoJSON の描画

GeoJSON を Python で扱う例は [geopandas](../../Language/Python/Library/geopandas.md) を参照。
