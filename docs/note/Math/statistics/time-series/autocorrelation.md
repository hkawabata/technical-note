---
title: 自己相関
title-en: Autocorrelation
---

# 自己相関

自己相関 = 過去と現在の相関。  
時系列データ $S_0 = \{r_1, \cdots, r_n\}$ と、そこから一定時間をずらしたデータ $S_h = \{r_{1+h}, \cdots, r_{n+h}\}$ との相関を取る。

- **ラグ**：元データからずらす時間
- **自己相関係数**：時系列データとそこからラグ $h$ だけずらしたデータとの相関係数

## 例：屋久島の2020年6月の気象データ

[気温・降水量・気圧・湿度](https://gist.github.com/hkawabata/5e0e7cbbb142125643acb663b3c11559)（気象庁からダウンロードしたデータを整形）を利用。

### 元となる気象データの描画

- 横軸：6/1 0:00 からの経過時間（hours）
- 縦軸：その時刻の気象データ

![Figure_1](https://user-images.githubusercontent.com/13412823/212796591-05976887-9074-4401-91e2-c5c9fafb646e.png)

### 自己相関係数の描画

- 横軸：ラグ
- 縦軸：自己相関係数

![Figure_2](https://user-images.githubusercontent.com/13412823/212796601-c8321832-9b1f-4549-89bc-319fa360f5e4.png)

（描画に使った Python コード）
```python
import numpy as np
from matplotlib import pyplot as plt
from urllib import request

unit = {
	'temperature': 'degree',
	'rain-fall': 'mm',
	'pressure': 'hPa',
	'humidity': '%'
}

# データ読み込み・格納
csv_url = 'https://gist.githubusercontent.com/hkawabata/5e0e7cbbb142125643acb663b3c11559/raw/af638f0b4193a9adb4d1f3d069e389a196146daa/20220116_Yakushima_weather.csv'
response = request.urlopen(csv_url)
lines = response.read().decode().split('\n')
response.close()
t = []
data = {}
for k in unit:
	data[k] = []

for line in lines[1:]:
	arr = line.split(',')
	t.append(arr[0])
	data['temperature'].append(float(arr[1]))
	data['rain-fall'].append(float(arr[4]))
	data['pressure'].append(float(arr[8]))
	data['humidity'].append(float(arr[11]))

# 自己共分散を計算
acf = {}
for k in unit:
	acf[k] = []

for k, vs in data.items():
	for lag in range(1, len(vs)//2):
		acf[k].append(np.corrcoef(vs[:len(vs)-lag], vs[lag:])[0][1])

# 元データの描画
days = 15
plt.figure(figsize=(8, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt_cnt = 1
for k, vs in data.items():
	plt.subplot(4, 1, plt_cnt)
	plt.xticks(np.arange(0, 24*days + 1, 24))
	plt.plot(range(24*days), vs[:24*days])
	plt.grid()
	plt.title('{} [{}]'.format(k, unit[k]))
	plt_cnt += 1

plt.show()

# 自己相関係数の描画
days = 5
plt.figure(figsize=(8, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt_cnt = 1
for k, vs in acf.items():
	plt.subplot(4, 1, plt_cnt)
	plt.xticks(np.arange(0, 24*days + 1, 24))
	plt.ylim([-1.0, 1.0])
	plt.stem(range(1, 24*days+1), vs[:24*days], markerfmt='C0.')
	plt.grid()
	plt.title(k)
	plt_cnt += 1

plt.show()
```

## 例：いろいろな手作りデータ

（ToDo：周期性のあるもの、一定のラグに大きな依存があるもの）


# 偏自己相関

$r_t$ と $r_{t+h}$ の間の自己相関を考える時、純粋な $r_t$ と $r_{t+h}$ の間の相関だけではなく、その間の $r_{t+1}, \cdots, r_{t+h-1}$ の情報が含まれている可能性がある。

たとえば

$$
r_{t+1} = a r_t + \epsilon
$$

という関係性があるとき、直接的に $r_{t+1}$ の値に関与するのは直前の $r_t$ だけだが、

$$
\begin{eqnarray}
	r_{t+2} &=& a r_{t+1} + \epsilon = a^2 r_t + (a+1) \epsilon \\
	r_{t+3} &=& a r_{t+2} + \epsilon = a^3 r_t + (a^2+a+1) \epsilon \\
	\cdots
\end{eqnarray}
$$

となるので、単純に相関係数を計算すると、ラグが2以上の $r_{t+2}, r_{t+3}, \cdots$ と $r_t$ の間にも高い相関があるような計算結果が得られる。

なので、$r_{t+h}$ と $r_t$ の間の相関から、間にある $r_{t+1}, \cdots, r_{t+h-1}$ の影響を取り除いた純粋な相関（= **偏自己相関**）を求めたい。

## 偏自己相関係数の計算

### 問題設定

前提として、弱定常性を仮定する：

- $r_t$ の期待値・分散が時刻によらず一定
- $r_{t+h}$ と $r_t$ 自己共分散 $\mathrm{Cov} (r_{t+h}, r_t)$ が時刻には寄らず、ラグ $h$ にのみ依存

$$
\begin{eqnarray}
	E(r_t) &=& \mu \\
	V(r_t) &=& \gamma_0 \\
	\mathrm{Cov} (r_{t+h}, r_t) &=& \gamma_h
\end{eqnarray}
$$

この前提の下、$\mathrm{Cov} (r_{t+h}, r_t)$ を

$$
\begin{eqnarray}
	\mathrm{Cov} (r_{t+h}, r_t) &=&
	\phi_1 \mathrm{Cov} (r_{t+h-1}, r_t) +
	\phi_2 \mathrm{Cov} (r_{t+h-2}, r_t) +
	\cdots +
	\phi_h \mathrm{Cov} (r_t, r_t)
	\qquad \qquad (1)
	\\ &=&
	\phi_1 \gamma_{h-1} + \phi_2 \gamma_{h-2} + \cdots \phi_h \gamma_0
\end{eqnarray}
$$

のように、

- $r_{t+h-1}, r_{t+h-2}, \cdots, r_{t+1}$  と $r_t$ との相関を表す共分散 $\mathrm{Cov} (r_{t+h-1}, r_t), \cdots, \mathrm{Cov} (r_{t+1}, r_t)$
- 純粋な $r_{t+h}$ と $r_t$ の相関を表す成分 $\phi_h \mathrm{Cov} (r_t, r_t)$

の線形和で表し、$\phi_h$ を求める。

### $\phi_h$ の計算

$$
r_{t+h} - \mu = \phi_1 (r_{t+h-1} - \mu) + \phi_2 (r_{t+h-2} - \mu) + \cdots + \phi_h (r_t - \mu) \qquad \qquad (2)
$$

が成り立つような $\phi_1, \cdots, \phi_h$ を求めれば良い。

※ $(2)$ の両辺に $(r_t - \mu)$ をかけて期待値を取れば、$\mathrm{Cov}(r_s, r_t) = E((r_s-\mu)(r_t-\mu))$ より $(1)$ が成り立つ。

$(2)$ の両辺に $(r_{t+1} - \mu)$ をかけて期待値を取ると、

$$
\begin{eqnarray}
	\mathrm{Cov}(r_{t+h}, r_{t+1}) &=&
	\phi_1 \mathrm{Cov}(r_{t+h-1}, r_{t+1}) +
	\phi_2 \mathrm{Cov}(r_{t+h-2}, r_{t+1}) +
	\cdots +
	\phi_{h-1} \mathrm{Cov}(r_{t+1}, r_{t+1}) +
	\phi_h \mathrm{Cov}(r_{t}, r_{t+1})
	\\
	\gamma_{h-1} &=&
	\phi_1 \gamma_{h-2} +
	\phi_2 \gamma_{h-3} +
	\cdots +
	\phi_{h-1} \gamma_{0} +
	\phi_h \gamma_{1}
\end{eqnarray}
$$

同様に $(2)$ の両辺に $(r_{t+2} - \mu), (r_{t+3} - \mu), \cdots, (r_{t+h-1} - \mu)$ をかけて期待値を取ると、

$$
\begin{eqnarray}
	\gamma_{h-2} &=&
	\phi_1 \gamma_{h-3} +
	\phi_2 \gamma_{h-4} +
	\cdots +
	\phi_{h-1} \gamma_{1} +
	\phi_h \gamma_{2}
	\\
	\gamma_{h-3} &=&
	\phi_1 \gamma_{h-4} +
	\phi_2 \gamma_{h-5} +
	\cdots +
	\phi_{h-1} \gamma_{2} +
	\phi_h \gamma_{3}
	\\
	\cdots
	\\
	\gamma_{1} &=&
	\phi_1 \gamma_0 +
	\phi_2 \gamma_1 +
	\cdots +
	\phi_{h-1} \gamma_{h-2} +
	\phi_h \gamma_{h-1}
\end{eqnarray}
$$

以上の式を行列で表現すると、

$$
\begin{pmatrix}
	\gamma_1 \\
	\gamma_2 \\
	\vdots \\
	\gamma_{h-1} \\
	\gamma_h
\end{pmatrix}
=
\begin{pmatrix}
	\gamma_0 & \gamma_1 & \gamma_2 & \cdots & \gamma_{h-1} \\
	\gamma_1 & \gamma_0 & \gamma_1 & \cdots & \gamma_{h-2} \\
	\gamma_2 & \gamma_1 & \gamma_0 & \cdots & \gamma_{h-3} \\
	\vdots & \vdots & \vdots & \ddots & \vdots \\
	\gamma_{h-1} & \gamma_{h-2} & \gamma_{h-3} & \cdots & \gamma_0
\end{pmatrix}
\begin{pmatrix}
	\phi_1 \\
	\phi_2 \\
	\vdots \\
	\phi_{h-1} \\
	\phi_h
\end{pmatrix}
$$

よって $\phi_h$ は以下の式で求まる。

$$
\begin{pmatrix}
	\phi_1 \\
	\phi_2 \\
	\vdots \\
	\phi_{h-1} \\
	\phi_h
\end{pmatrix}
=
\begin{pmatrix}
	\gamma_0 & \gamma_1 & \gamma_2 & \cdots & \gamma_{h-1} \\
	\gamma_1 & \gamma_0 & \gamma_1 & \cdots & \gamma_{h-2} \\
	\gamma_2 & \gamma_1 & \gamma_0 & \cdots & \gamma_{h-3} \\
	\vdots & \vdots & \vdots & \ddots & \vdots \\
	\gamma_{h-1} & \gamma_{h-2} & \gamma_{h-3} & \cdots & \gamma_0
\end{pmatrix}^{-1}
\begin{pmatrix}
	\gamma_1 \\
	\gamma_2 \\
	\vdots \\
	\gamma_{h-1} \\
	\gamma_h
\end{pmatrix}
$$


## 例：屋久島の2020年6月の気象データ

いずれの気象データも、ほぼ直前のタイムステップだけで値が決まっていることが分かる。

![Figure_1](https://user-images.githubusercontent.com/13412823/213010136-59400a88-9be4-4c1d-9feb-327708ddb7d1.png)

（描画に使った Python コード）
```python
# 偏自己相関係数の計算
pacf = {}
for k, vs in data.items():
	# 各ラグに対する自己共分散
	cov_all = []
	for lag in range(len(vs)//2):
		cov_all.append(np.cov(vs[:len(vs)-lag], vs[lag:])[0][1])
	cov_all = np.array(cov_all)
	# 自己共分散を並べた行列
	cov_matrix_all = np.empty((len(cov_all), len(cov_all)))
	for i in range(len(cov_all)):
		for j in range(len(cov_all)):
			cov_matrix_all[i][j] = cov_all[np.abs(i-j)]
	# 偏自己共分散
	pacf[k] = []
	for lag in range(1, len(vs)//2):
		cov_matrix = cov_matrix_all[:lag, :lag]
		cov = cov_all[1:lag+1]
		phi = np.linalg.inv(cov_matrix).dot(np.matrix(cov).T)[-1,0]
		pacf[k].append(phi)

days = 5
plt.figure(figsize=(8, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt_cnt = 1
for k, vs in pacf.items():
	plt.subplot(4, 1, plt_cnt)
	plt.xticks(np.arange(0, 24*days + 1, 24))
	plt.ylim([-1.0, 1.0])
	plt.stem(range(1, 24*days+1), vs[:24*days], markerfmt='C0.')
	plt.grid()
	plt.title(k)
	plt_cnt += 1

plt.show()
```

（おまけ：以上の実装が正しいか、`statsmodels` ライブラリの計算結果も確認）
```python
import statsmodels.api as sm

days = 5
fig, ax = plt.subplots(4, 2, figsize=(10, 8))
plt_cnt = 0
for k, vs in data.items():
	# 自己相関係数
	sm.graphics.tsa.plot_acf(vs, lags=120, ax=ax[plt_cnt,0], marker='.')
	ax[plt_cnt,0].set_xticks(np.arange(0, 24*days+1, 24))
	ax[plt_cnt,0].grid()
	ax[plt_cnt,0].set_title('Autocorrelation' if plt_cnt==0 else '')
	ax[plt_cnt,0].set_ylabel(k, fontsize=12)
	# 偏自己相関係数
	sm.graphics.tsa.plot_pacf(vs, lags=120, ax=ax[plt_cnt,1], marker='.')
	ax[plt_cnt,1].set_xticks(np.arange(0, 24*days+1, 24))
	ax[plt_cnt,1].grid()
	ax[plt_cnt,1].set_title('Partial Autocorrelation' if plt_cnt==0 else '')
	plt_cnt += 1

plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/213066335-0ee026a0-3200-4b1f-aa3e-3121d011d5b5.png)

## 例：いろいろな手作りデータ

```python
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm

def noise(sigma, n):
	rand = np.random.normal(loc=0, scale=sigma, size=n)
	if n == 1:
		return rand[0]
	else:
		return rand

N = 100

# 周期性あり：サインカーブ
y_sin = np.sin(np.linspace(0, 10*np.pi, N)) + noise(0.1, N)

# 周期性あり：一定期間ごとに大きなピーク
y_peak = noise(0.1, N)
y_peak[::5] += 1.0

# 完全ランダム
y_rand_norm = noise(1.0, N)

s = 0.01
# 1つ前の成分だけに依存
y_1 = [1.0]
for _ in range(N-1):
	y_1.append((1.1+noise(s,1))*y_1[-1])

# 1つ前〜3つ前までの成分に依存
y_123 = [1.0] * 3
for _ in range(N-3):
	y_123.append((1.1+noise(s,1))*y_123[-1] - (0.9+noise(s,1))*y_123[-2] + (0.8+noise(s,1))*y_123[-3])

ys = [
	('$\sin (t)$', y_sin),
	('peak', y_peak),
	('random normal', y_rand_norm),
	('$y_t = 1.1 y_{t-1}$', y_1),
	('$y_t = 1.1 y_{t-1} - 0.9 y_{t-2} + 0.8 y_{t-3}$', y_123)
]
fig, ax = plt.subplots(len(ys), 3, figsize=(10, 2.3*len(ys)))
plt_cnt = 0
for title, y in ys:
	# 元データ
	ax[plt_cnt,0].plot(range(N), y)
	ax[plt_cnt,0].grid()
	ax[plt_cnt,0].set_title('Raw Data' if plt_cnt==0 else '')
	ax[plt_cnt,0].set_ylabel(title, fontsize=8)
	# 自己相関係数
	sm.graphics.tsa.plot_acf(y, lags=N//2-1, ax=ax[plt_cnt,1], marker='.')
	#ax[plt_cnt,0].set_xticks(np.arange(0, 24*days+1, 24))
	ax[plt_cnt,1].grid()
	ax[plt_cnt,1].set_title('Autocorrelation' if plt_cnt==0 else '')
	# 偏自己相関係数
	sm.graphics.tsa.plot_pacf(y, lags=N//2-1, ax=ax[plt_cnt,2], marker='.')
	#ax[plt_cnt,1].set_xticks(np.arange(0, 24*days+1, 24))
	ax[plt_cnt,2].grid()
	ax[plt_cnt,2].set_title('Partial Autocorrelation' if plt_cnt==0 else '')
	plt_cnt += 1

plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/213912338-f66c4e43-adec-4fb5-a199-e0735d0e7249.png)

| データ | 自己相関 | 偏自己相関 |
| :-- | :-- | :-- |
| サインカーブ | 期待通り、「ラグ = 周期の倍数」のところに高い相関が出ている | バラバラ。若干期待する周期のところの偏自己相関は大きいかも |
| 一定期間ごとにピーク | 同上 | 期待する周期（ラグ = 5）のところに相関が見られる。「ラグ = 30〜50」のあたりに大きな相関が観測されているのはなぜ？ |
| 完全ランダム（正規分布） | 期待通り自己相関は見られない | 期待通り自己相関は見られない |
| 1つ前の成分だけに依存 | ラグが大きくなるほど自己相関が低下 | 1つ前の成分のみに相関が見られる |
| 1つ前〜3つ前の成分に依存 | 概ね同上、1つ前の成分だけに依存する場合よりは自己相関はばらつく | 「ラグ = 1〜3」のあたりの偏自己相関は高い。しかし、「ラグ = 40〜」のあたりでも偏自己相関が高くなっているのが謎 |
