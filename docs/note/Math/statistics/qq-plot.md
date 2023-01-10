---
title: Q-Q プロット
---

# Q-Q プロットとは

「調査対象の実測データの分布が、期待する分布にどれだけ近いか？」を視覚的に確認するための手法。

# 仕組み

以下の2つを縦軸・横軸にとってプロットする。
- 実測値：実際に測定されたデータを小さい順に並べたもの
- 理論値：期待する分布の $N+1$ 分位点（$N$：実測データのサンプル数）の値を並べたもの

実測データが期待する分布に完全に従っていれば、実測値 = 理論値となり、Q-Q プロットのグラフは直線を描く。

→ **Q-Q プロットが直線に近いほど、期待する分布に近い**

# 実装

種々のデータが正規分布

$$
f(x) =
\cfrac{1}{\sqrt{2\pi}\sigma}
\exp{
  \left(
    - \cfrac{(x-\mu)^2}{2\sigma^2}
  \right)
}
$$

に従うと仮定して Q-Q プロットを試してみる。

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

def qqplot_norm(v):
	v_measured = v.copy()
	# 正規分布を仮定した場合の理論値を生成（乱数を使っているのでブレあり）
	N = v_measured.size
	sigma = np.std(v_measured)
	mu = np.average(v_measured)
	v_theoretical = np.random.normal(loc=mu, scale=sigma, size=N)
	# 実測値・理論値それぞれをソート
	v_measured.sort()
	v_theoretical.sort()
	# Q-Q plot
	plt.xlabel('theoretical')
	plt.ylabel('measured')
	plt.plot(v_theoretical, v_measured, marker='.')
	# 補助線 y=x
	v_min = np.min([np.min(v_measured), np.min(v_theoretical)])
	v_max = np.max([np.max(v_measured), np.max(v_theoretical)])
	plt.plot([v_min, v_max], [v_min, v_max])
	plt.title('Q-Q plot (Normal Dist.)')
	plt.grid()
	plt.show()
```

# 動作確認

## アイリスデータセット

```python
iris = load_iris().data
print(load_iris().DESCR)
"""
...
:Attribute Information:
    - sepal length in cm
    - sepal width in cm
    - petal length in cm
    - petal width in cm
...
"""

for i in range(4):
	v = load_iris().data[:, i]
	qqplot_norm(v)
```

| 素性 | Q-Q plot |
| :-- | :-- |
| sepal length | <img src="https://user-images.githubusercontent.com/13412823/211126949-1898aef6-e10e-4541-9d45-3d897184108a.png" width="400"> |
| sepal width | <img src="https://user-images.githubusercontent.com/13412823/211126948-773fc4a2-4c84-4613-96f4-33bb8cb0c477.png" width="400"> |
| petal length | <img src="https://user-images.githubusercontent.com/13412823/211126947-7bfe8aaa-3564-4b4d-b333-3261c7707ddb.png" width="400"> |
| petal width | <img src="https://user-images.githubusercontent.com/13412823/211126941-0a59a3af-e9e8-4474-bef1-f6457bda4dd8.png" width="400"> |

※ 主に分類タスクに利用されるアイリスデータセットでは、3つのクラスのサンプルが混在しており、正規分布に従わない素性があっても自然（クラス分類に効く素性であれば、クラス間で値に飛びが存在）。同じクラスに分類されるものだけに絞ってプロットすれば結果は変わりそう

## 乱数生成した正規分布

```python
v = np.random.normal(loc=10, scale=0.1, size=1000)
qqplot_norm(v)
```

<img src="https://user-images.githubusercontent.com/13412823/211128037-c0fbf2cb-27d3-4994-a804-a4a9b0a31516.png" width="500">


## 乱数生成したカイ二乗分布

```python
for f in [3, 10, 100]:
	v = np.random.chisquare(f, 1000)  # 自由度fのカイ二乗分布
	qqplot_norm(v)
```

| 自由度3 | 自由度10 | 自由度100 |
| :-- | :-- | :-- |
| ![Figure_1](https://user-images.githubusercontent.com/13412823/211128401-29a4b0ee-8243-416a-a666-61c2d338a8fd.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/211128619-79335f2d-641f-408f-bdc2-6edb2f0f16bc.png) | ![Figure_2](https://user-images.githubusercontent.com/13412823/211128398-89b6ad42-c504-4327-bf14-159deee4f1d3.png) |

※ カイ二乗分布は自由度が大きくなるほど正規分布に近づくことが知られている