---
title: 自己相関
title-en: Autocorrelation
---

# 自己相関

自己相関 = 過去と現在の相関。  
時系列データ $S = \{r_1, \cdots, r_n\}$ に対して、そこから一定時間をずらしたデータとの相関係数を計算する。

## 自己相関係数の計算

- **ラグ** $h$：元データからずらす時間
- 時系列データ
	- $S = \{r_1, \cdots, r_n\}$：元の時系列データ
	- $S_0 = \{r_1, \cdots, r_{n-h}\}$：計算の都合上 $S_h$ と同じ長さにするため、ラグ $h$ だけ末尾を削った時系列データ
	- $S_h = \{r_{h+1}, \cdots, r_n\}$：$S_0$ からラグ $h$ だけ後ろにずらした時系列データ

**自己相関係数** $\rho$ は $S_0$ と $S_h$ の相関係数で表される。  
ただし後述の通り、単純な相関係数とは計算式が少し異なる。

まず、分散・共分散それぞれを計算する際に用いる標本平均は、ラグを取った $S_0, S_h$ それぞれの平均値 $\bar{r_0}, \bar{r_h}$ ではなく、元データ $S$ 全体の平均値 $\bar{r}$ を用いる：

$$
\bar{r} := \cfrac{1}{n} \sum_{t=1}^n r_t
$$

次に、分母に出てくる標本標準偏差の計算には、$S_0, S_h$ それぞれの分散 $V(S_0), V(S_h)$ ではなく、元データ $S$ 全体の分散 $V(S)$ を用いる：

$$
V(S) :=
\cfrac{1}{n}
\sum_{t=1}^n (r_t - \bar{r})^2
$$

最後に、分子である標本共分散の計算においては、$S_0, S_h$ の素直な共分散 $\mathrm{Cov}(S_0, S_h)$ と違って、平均に $\bar{r}$ を使い、和を取る件数 $n-h$ ではなく $n$ で割った **自己共分散** $\mathrm{Cov}_{\mathrm{auto}}(S_0, S_h)$ を用いる：

$$
\mathrm{Cov}_{\mathrm{auto}}(S_0, S_h) :=
\cfrac{1}{n}
\sum_{t=1}^{n-h} (r_t - \bar{r})(r_{t+h}-\bar{r})
$$

以上により、自己相関係数 $\rho$ の計算式は

$$
\rho :=
\cfrac{\mathrm{Cov}_{\mathrm{auto}}(S_0, S_h)}
{\sqrt{V(S)}\sqrt{V(S)}}
=
\cfrac{
	\displaystyle
	\sum_{t=1}^{n-h} (r_t - \bar{r})(r_{t+h}-\bar{r})
}{
	\displaystyle
	\sum_{t=1}^n (r_t - \bar{r})^2
}
\qquad
\left(
	\bar{r} := \cfrac{1}{n} \sum_{t=1}^n r_t
\right)
\tag{1}
$$

> **【NOTE】素直に $S_0, S_h$ の相関係数を計算した場合との差異**
> 
> - $S_0 = \{r_1, \cdots, r_{n-h}\}$
> - $S_h = \{r_{h+1}, \cdots, r_n\}$
> 
> の単純な相関係数 $\rho'$ を計算すると、
> 
> $$
\begin{eqnarray}
	V(S_0) &=& \cfrac{1}{n-h} \sum_{t=1}^{n-h} (r_t-\bar{r_0})^2
	\qquad
	\left( \bar{r_0} := \cfrac{1}{n-h} \sum_{t=1}^{n-h} r_t \right)
	\\
	\\
	V(S_h) &=& \cfrac{1}{n-h} \sum_{t=h+1}^{n} (r_t-\bar{r_h})^2
	\qquad
	\left( \bar{r_h} := \cfrac{1}{n-h} \sum_{t=h+1}^{n} r_t \right)
	\\
	\\
	\mathrm{Cov}(S_0, S_h) &=& \cfrac{1}{n-h} \sum_{t=1}^{n-h} (r_t - \bar{r_0})(r_{t+h}-\bar{r_h})
	\\
	\\
	\rho' &:=& \cfrac{\mathrm{Cov}(S_0, S_h)}{\sqrt{V(S_0)}\sqrt{V(S_h)}}
	=
	\cfrac{
		\displaystyle
		\sum_{t=1}^{n-h} (r_t - \bar{r_0})(r_{t+h}-\bar{r_h})
	}{
		\displaystyle
		\sqrt{ \sum_{t=1}^{n-h} (r_t-\bar{r_0})^2 }
		\sqrt{ \sum_{t=h+1}^{n} (r_t-\bar{r_h})^2 }
	}
\end{eqnarray}
$$
> 
> $\rho$ と $\rho'$ は以下の点で異なっている。
> 
> - 標本平均
> 	- $\rho$：全時系列 $S$ の標本平均 $\bar{r}$
> 	- $\rho'$：$S_0, S_h$ それぞれの標本平均 $\bar{r_0}, \bar{r_h}$
> - 標本分散
> 	- $\rho$：全時系列 $S$ の標本分散 $V(S)$
> 	- $\rho'$：$S_0, S_h$ それぞれの標本分散 $V(S_0), V(S_h)$
> - 標本共分散の分母
> 	- $\rho$：和を取る件数（$S_0,S_h$ の長さ）$n-h$ で割らず、全時系列 $S$ のデータ数 $n$ で割る
> 	- $\rho'$：和を取る件数（$S_0,S_h$ の長さ）$n-h$ で割る
> 
> → **（要調査）共分散の計算では、なぜ和を取る件数 $n-h$ ではなく $n$ で割るのか？ 同じくらいの相関があっても、ラグが大きいほど相関係数が小さくなってしまうのでは？**
> 
> ※ Python 言語の statsmodels や R 言語の acf 関数といった一般的なライブラリで計算してみると、$\rho'$ ではなく $\rho$ の計算式が使われていることが分かる
> 
> 【実験】完全に周期的なデータ（周期7）にノイズを乗せたデータについて $\rho, \rho'$ を計算・プロットしてみる：
> 
> ![Figure_1](https://user-images.githubusercontent.com/13412823/243217166-f3ff3d6b-591a-4abf-9bf4-d40a19d8615b.png)
> 
> cf. [実験に用いたコード](https://gist.github.com/hkawabata/fb0b6e86ba7e6bdbfbff115d73dafa57#file-20230602_autocorrelation-py)
> 
> - lag=7の倍数のところに大きな自己相関
> - 予想通り、同じ7の倍数でも、14, 21, 28, 35, ... とラグが大きくなるにつれて自己相関係数 $\rho$ は小さくなる
>   - $\rho'$ はラグが大きくなっても自己相関係数が変わらない
> 
> （仮説）ラグが大きくなるほど $S_0, S_h$ の長さは短くなり、自己相関係数の計算精度も落ちる（誤差が大きくなる）ので、それに補正をかけている？  
> ※ 同じ確率分布から標本抽出して平均を取る場合、分散は標本数に反比例
> 
> 【実験】ランダムなノイズを乗せたデータに対して $\rho, \rho'$ を計算する、という操作を1000回繰り返し、$\rho, \rho'$ の分散を計算してみる（ノイズは毎回新しく計算）：
> 
> ![Figure_2](https://user-images.githubusercontent.com/13412823/243217190-a4260efb-8ddb-4333-a429-a2a88875631b.png)
> 
> cf. [実験に用いたコード](https://gist.github.com/hkawabata/fb0b6e86ba7e6bdbfbff115d73dafa57#file-var-autocorrelation-py)
> 
> - ラグが大きくなるほど、$\rho$ の分散は小さくなり、$\rho'$ の分散は大きくなっている
> - $\rho'$ の分散は、共分散の計算において和を取る標本数 $n-h$ に反比例していそう


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

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/fb0b6e86ba7e6bdbfbff115d73dafa57#file-yakushima-temperature-py)


## 例：いろいろな手作りデータ

（ToDo：周期性のあるもの、一定のラグに大きな依存があるもの）

```python
T = 2000
x = np.array(range(T)) / 25
y1 = np.random.normal(1.0, 0.25, T)
y2 = np.sin(x) + np.random.normal(0, 0.2, T)
y3 = np.sin(x**1.3) + np.random.normal(0, 0.2, T)
y4 = np.sin(x) + 0.5 * x + np.random.normal(0, 0.2, T)
y5 = np.sin(x) + (x-30)**2/400 + np.random.normal(0, 0.2, T)
```


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

前提として、弱定常性（cf. [定常性](../../../DataMining/time-series/stationary-process)）を仮定する：

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

$\phi_1, \cdots, \phi_h$ が

$$
r_{t+h} - \mu = \phi_1 (r_{t+h-1} - \mu) + \phi_2 (r_{t+h-2} - \mu) + \cdots + \phi_h (r_t - \mu) \qquad \qquad (2)
$$

を満たせば、$(1)$ が成り立つ。

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
	\\ \Longrightarrow \quad
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

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/fb0b6e86ba7e6bdbfbff115d73dafa57#file-yakushima-temperature-partial-py)

おまけ：以上の実装が正しいか、`statsmodels` ライブラリの計算結果も確認

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

| No | 式 | データの特徴 | 自己相関 | 偏自己相関 |
| :-- | :-- | :-- | :-- | :-- |
| 1 | $y_t = \sin(t)$ | サインカーブ | 期待通り、「ラグ = 周期の倍数」のところに高い相関が出ている | バラバラ。若干期待する周期のところの偏自己相関は大きいかも |
| 2 | - | 一定周期で鋭いスパイク | 同上 | ・期待する周期（ラグ = 5）のところに相関が見られる<br>・「ラグ = 30〜50」のあたりに大きな相関が観測されているのはなぜ？ |
| 3 | $y_t \sim N(0, 1)$ | 完全ランダム（正規分布） | 期待通り自己相関は見られない | 期待通り自己相関は見られない |
| 4 | $y_t = 1.1y_{t-1}$ | 1つ前の成分だけに依存 | ラグが大きくなるほど自己相関が低下 | 1つ前の成分のみに相関が見られる |
| 5 | $y_t = 1.1y_{t-1} - 0.9y_{t-2} + 0.8y_{t-3}$ | 1つ前〜3つ前の成分に依存 | 概ね同上、1つ前の成分だけに依存する場合よりは自己相関はばらつく | ・「ラグ = 1〜3」のあたりの偏自己相関は高い<br>・しかし、「ラグ = 40〜」のあたりでも偏自己相関が高くなっているのが謎 |
