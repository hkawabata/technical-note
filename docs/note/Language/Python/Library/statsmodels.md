---
title: statsmodels
---

statsmodels 0.13.5 時点の情報。

# 概要

統計モデルを使って推定・検定・探索ができるライブラリ。

# インストール

```bash
$ pip install statsmodels
```

# 使い方

```python
import statsmodels.api as sm
```

## R データセット取得


```python
ds = sm.datasets.get_rdataset("Guerry", "HistData")
# <class 'statsmodels.datasets.utils.Dataset'>
df = ds.data
# <class 'pandas.core.frame.DataFrame'>
```

参照：https://vincentarelbundock.github.io/Rdatasets/articles/data.html

| Package | Item | 内容 |
| :-- | :-- | :-- |
| HistData | Guerry |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


## 線形回帰モデルの適用

```python
df_part = df[['Lottery', 'Wealth']]
df_part = df_part.dropna()  # 無効なデータのある行を削除
y = df_part['Lottery']
x = df_part['Wealth']

x1 = sm.add_constant(x)  # 定数項 (1.0) を加えて原点を通らない直線への回帰に対応
model = sm.OLS(y, x1)  # 線形回帰モデルを定義
results = model.fit()

print(results.params)
"""
const     22.592339
Wealth     0.480636
"""

from matplotlib import pyplot as plt
plt.xlabel('Wealth')
plt.ylabel('Lottery')
plt.scatter(x, y, label='real')
plt.plot(x, results.predict(x1), label='predicted')
plt.legend()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215259704-99b32b7d-6d97-46a3-9e2f-1e4f7412097f.png)


## グラフの描画

### Q-Q プロット

正規分布の Q-Q プロットを行う例。

```python
from scipy import stats

# 使用するデータ（ナイル川の年間流量の推移）の読み込み
ds = sm.datasets.get_rdataset("Nile", "datasets")
df = ds.data
mu = df['value'].mean()
sigma = df['value'].std()

fig = sm.qqplot(df['value'], dist=stats.norm, loc=mu, scale=sigma, marker='.', line='45')
plt.grid()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215302607-43a52268-b6f2-429e-8d1a-c3a8a90c6e26.png)


### 時系列データ

```python
# 使用するデータ（ナイル川の年間流量の推移）の読み込み
ds = sm.datasets.get_rdataset("Nile", "datasets")
df = ds.data
print(df)
"""
    time  value
0   1871   1120
1   1872   1160
2   1873    963
3   1874   1210
4   1875   1160
..   ...    ...
95  1966    746
96  1967    919
97  1968    718
98  1969    714
99  1970    740
"""

# 描画してみる
from matplotlib import pyplot as plt
plt.xlabel('year')
plt.ylabel('flow [$10^8 m^3$]')
plt.plot(df['time'], df['value'])
plt.grid()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215260654-d5335e4a-1812-48d9-b200-a238604dfdbd.png)

```python
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
# 自己相関係数の描画
sm.graphics.tsa.plot_acf(df['value'], ax=ax[0], lags=49, marker='.')
ax[0].grid()
# 偏自己相関係数の描画
sm.graphics.tsa.plot_pacf(df['value'], ax=ax[1], lags=49, marker='.')
ax[1].grid()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215261322-7b2c4421-d06e-423f-b101-6cb8b11710d3.png)
