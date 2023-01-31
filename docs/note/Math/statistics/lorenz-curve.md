---
title: ローレンツ曲線
title-en: Lorenz curve
---

# ローレンツ曲線とは

事象や資源の集中度合いを示す曲線。
所得や貯蓄の格差などを視覚的に示すのに有用。

# 書き方と解釈

データサンプルの値を階級分けし、

- 横軸：各階級の度数の累積相対度数
- 縦軸：各階級に属する値の合計の累積相対度数

をプロットする。

例えば以下のように、ある労働者グループの年収の階級別度数分布表において、横軸に「累積人数（相対）」、縦軸に「累積年収（相対）」を取る。

| 階級 | 階級値（万円） | 人数 | 階級内合計年収 | 累積人数（実数） | 累積人数（相対） | 累積年収（実数） | 累積年収（相対） |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 100 | 11 | 1100 | 11 | 0.0924 | 1100 | 0.0154 |
| 2 | 200 | 15 | 3000 | 26 | 0.2185 | 4100 | 0.0575 |
| 3 | 300 | 18 | 5400 | 44 | 0.3697 | 9500 | 0.1332 |
| 4 | 400 | 24 | 9600 | 68 | 0.5714 | 19100 | 0.2679 |
| 5 | 500 | 18 | 9000 | 86 | 0.7227 | 28100 | 0.3941 |
| 6 | 600 | 11 | 6600 | 97 | 0.8151 | 34700 | 0.4867 |
| 7 | 700 | 6 | 4200 | 103 | 0.8655 | 38900 | 0.5456 |
| 8 | 800 | 3 | 2400 | 106 | 0.8908 | 41300 | 0.5792 |
| 9 | 900 | 4 | 3600 | 110 | 0.9244 | 44900 | 0.6297 |
| 10 | 1000 | 1 | 1000 | 111 | 0.9328 | 45900 | 0.6438 |
| 11 | 1100 | 0 | 0 | 111 | 0.9328 | 45900 | 0.6438 |
| 12 | 1200 | 2 | 2400 | 113 | 0.9496 | 48300 | 0.6774 |
| 13 | 1300 | 0 | 0 | 113 | 0.9496 | 48300 | 0.6774 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 35 | 3500 | 0 | 0 | 113 | 0.9496 | 48300 | 0.6774 |
| 36 | 3600 | 0 | 0 | 113 | 0.9496 | 48300 | 0.6774 |
| 37 | 3700 | 3 | 11100 | 116 | 0.9748 | 59400 | 0.8331 |
| 38 | 3800 | 0 | 0 | 116 | 0.9748 | 59400 | 0.8331 |
| 39 | 3900 | 1 | 3900 | 117 | 0.9832 | 63300 | 0.8878 |
| 40 | 4000 | 2 | 8000 | 119 | 1.0000 | 71300 | 1.0000 |

![Figure_1](https://user-images.githubusercontent.com/13412823/215793605-6958525c-5d8d-4d25-9b0a-5c83943f123a.png)

これを見れば、例えば「ローレンツ曲線が (0.8, 0.5) よりも下を通る」→「低所得な順に労働者の8割の年収を足しても、全労働者の年収合計の半分に満たない」といったことが分かる。

このように、(0, 0) と (1, 1) を結ぶ直線（**完全平等線**）と比べてローレンツ曲線の膨らみが大きいほど、偏りの大きい分布であると言うことができる。

（描画に使った Python コード）

```python
from matplotlib import pyplot as plt
import numpy as np

def calc_cum_rel(vs, dv):
	"""
	累積相対度数を計算する
	vs : 値のリスト（全て正の値を想定）
	dv : 階級幅
	"""
	hist_size = int(max(vs)//dv+1)
	cnt_v = [0] * hist_size
	sum_v = [0] * hist_size
	for v in vs:
		i = int(v//dv)
		cnt_v[i] += 1
		sum_v[i] += v
	# 累積度数の計算
	cnt_v_cum = [0, cnt_v[0]]
	sum_v_cum = [0, sum_v[0]]
	for i in range(1, hist_size):
		cnt_v_cum.append(cnt_v_cum[-1] + cnt_v[i])
		sum_v_cum.append(sum_v_cum[-1] + sum_v[i])
	# 累積相対度数の計算
	cnt_v_cum_rel = np.array(cnt_v_cum) / cnt_v_cum[-1]
	sum_v_cum_rel = np.array(sum_v_cum) / sum_v_cum[-1]
	return (cnt_v_cum_rel, sum_v_cum_rel)

def calc_gini(cnt_v_cum_rel, sum_v_cum_rel):
	"""
	ジニ係数を計算
	cnt_v_cum_rel : 度数の累積相対度数
	sum_v_cum_rel : 値の累積相対度数
	"""
	gini = 0
	for i in range(len(cnt_v_cum_rel)-1):
		h = cnt_v_cum_rel[i+1] - cnt_v_cum_rel[i]
		a_top = cnt_v_cum_rel[i] - sum_v_cum_rel[i]
		a_bottom = cnt_v_cum_rel[i+1] - sum_v_cum_rel[i+1]
		gini += h * (a_top + a_bottom) * 0.5
	gini /= 0.5
	return gini

def draw_lorenz_curve(vs, dv, n_label, v_label):
	"""
	ローレンツ曲線を描画
	vs      : 値のリスト（全て正の値を想定）
	dv      : 階級幅
	n_label :
	v_label :
	"""
	cnt_v_cum_rel, sum_v_cum_rel = calc_cum_rel(vs, dv)
	hist_size = len(cnt_v_cum_rel) - 1
	gini = calc_gini(cnt_v_cum_rel, sum_v_cum_rel)
	# 描画
	fig, ax = plt.subplots(1, 2, figsize=(10, 4))
	plt.subplots_adjust(wspace=0.4)
	ax[0].set_title('Histogram')
	ax[0].hist(vs, bins=hist_size)
	ax[0].set_xlabel(v_label)
	ax[0].set_ylabel(n_label)
	ax[1].set_title('Lorenz Curve')
	ax[1].plot(cnt_v_cum_rel, sum_v_cum_rel, marker='.', label='Lorenz curve ($G = {:.4f}$)'.format(gini))
	ax[1].plot([0,1], [0,1], label='complete equality line')
	ax[1].set_xlabel('Cumulative relative frequency ({})'.format(n_label))
	ax[1].set_ylabel('Cumulative relative frequency ({})'.format(v_label))
	ax[1].legend()
	ax[1].grid()
	plt.show()

vs = [100]*11+[200]*15+[300]*18+[400]*24+[500]*18+[600]*11+[700]*6+[800]*3+[900]*4+[1000]*1+[1200]*2+[3700]*3+[3900]*1+[4000]*2
draw_lorenz_curve(vs, dv=100, n_label='worker', v_label='salary')
```

# ジニ係数

= Gini index

## 定義

ローレンツ曲線の偏り・不平等の程度を数値化した指数。

- $S_1$：完全平等線と実際のデータのローレンツ曲線とで囲まれた面積
- $S_2$：完全平等線と完全に不平等なときのローレンツ曲線とで囲まれた面積

として、ジニ係数 $G$ は

$$
G = \cfrac{S_1}{S_2}
$$

で計算される。  
偏りが大きいほどローレンツ曲線は右に膨らむので、$S_1$ が大きくなり、ジニ係数 $G$ も大きくなる。

## データからの計算方法

データサンプル数 $n$ が十分に大きい時、$S_2$ は底辺・高さがともに長さ1の直角二等辺三角形に近づいていくから、$S_2 = 0.5$ と近似できる。

$S_1$ は以下の図より、

- 台形 $A_0A_1B_1B_0$（三角形）の面積
- 台形 $A_1A_2B_2B_1$ の面積
- 台形 $A_2A_3B_3B_2$ の面積
- ...

を足し上げることで計算できる。

![Figure_1](https://user-images.githubusercontent.com/13412823/215807592-422ace67-735a-42e1-805f-6122bb12471a.png)


# 実データの例

## 2010年のメジャーリーグ年俸

[rdatasets](https://vincentarelbundock.github.io/Rdatasets/articles/data.html) より、2010年のメジャーリーグの年俸データを利用。

![Lorenz curve](https://user-images.githubusercontent.com/13412823/215761434-1f8796d1-5028-4fc7-8483-56164a641280.png)

（描画に使った Python コード）

```python
import statsmodels.api as sm

# 2010年のメジャーリーグ選手の年俸データを読み込み
ds = sm.datasets.get_rdataset("mlb", "openintro")
df = ds.data.dropna()
"""
               player                  team       position  salary
0        Brandon Webb  Arizona Diamondbacks        Pitcher  8500.0
1         Danny Haren  Arizona Diamondbacks        Pitcher  8250.0
2        Chris Snyder  Arizona Diamondbacks        Catcher  5250.0
..                ...                   ...            ...     ...
825     Ross Detwiler  Washington Nationals        Pitcher   400.0
826     Jesse English  Washington Nationals        Pitcher   400.0
827     Willy Taveras  Washington Nationals     Outfielder   400.0
"""

draw_lorenz_curve(df['salary'], dv=1000, v_label='salary', n_label='player')
```

