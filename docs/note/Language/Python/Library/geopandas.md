# geopandas 概要

GIS（Geographic Information System, 地理情報システム）データを扱うためのライブラリ。


# 使い方

```sh
pip install geopandas
```


## 実データを使った例

### 例：日本地図

国土地理院が持つ日本地図を例にして geojson のデータを描画してみる。

[国土地理院のページ](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-v3_1.html)から N03-20230101_GML.zip（日本全国）をダウンロードして解凍すると N03-23_230101.geojson が得られる。


```python
import geopandas as gpd
from matplotlib import pyplot as plt

df_japan = gpd.read_file('N03-23_230101.geojson')
```

素直に描画（市区町村境を描画）：

```python
df_japan.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()

df = df_japan[df_japan['N03_001']=='大阪府']
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()

df = df_japan[(df_japan['N03_001']=='東京都')&(df_japan['N03_004']=='港区')]
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()

df = df_japan[(df_japan['N03_001']=='大阪府')&(df_japan['N03_004']=='大阪市中央区')]
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()
```

同じ都道府県は統合して都道府県境を描画：

```python
df = df_japan.dissolve(by='N03_001')
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()

df = df_japan[df_japan['N03_001']=='大阪府'].dissolve(by='N03_001')
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()
```

→ ゴミのような境界線が残る。小数点の微小なところで境界点に誤差があるため？

```python
from shapely.geometry import shape, mapping
from shapely import wkt

df = df_japan.dissolve(by='N03_001')
df['geometry'] = wkt.loads(wkt.dumps(df['geometry'], rounding_precision=5))
df.plot(edgecolor='black', facecolor='aliceblue', linewidth=0.5)
plt.show()
```


### 例：世界地図

同様に世界地図も描いてみる。

```python
df_world = gpd.read_file('https://datahub.io/@olayway/geo-countries/_r/-/data/countries.geojson')

df_world.plot(edgecolor='black', facecolor='yellow', linewidth=0.5)
plt.show()
```
