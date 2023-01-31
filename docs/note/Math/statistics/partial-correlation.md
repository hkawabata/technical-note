---
title: 偏相関
title-en: Partial Correlation
---

# 偏相関・擬似相関

**偏相関**：注目する2つの変数 $x, y$ の相関を考える時、単純に相関を調べるのではなく、別の変数 $z$ による影響を除外して考えたもの。

たとえば、「運動量が多いほど高血圧になりにくい」という仮説を検証したいとする。  
このとき、運動量 $x$ と血圧 $y$ の間に相関があったとしても、

- 年齢 $z$ が高いほど疲れやすいので運動しなくなる（運動量 $x$ が小さい）
- 年齢 $z$ が高いほど高血圧になりやすい（血圧 $y$ が高い）

という事情がある場合、運動量と高血圧の間に相関があっても、直接的な因果関係が存在するとは限らない（= **疑似相関**）。  
そのため、年齢 $z$ の影響を取り除いた運動量 $x$ と血圧 $y$ の相関を調べる必要がある。

この例のように、注目する2つの因子 $x, y$ 両方に対して影響を与える第三の因子 $z$ を **交絡因子** と呼ぶ。


# 偏相関係数

## 計算式

$z$ の影響を除いた $x, y$ の偏相関係数 $r_{xy,z}$ は、$r_{xy}$ を $x,y$ の相関係数（$r_{xz}, r_{yz}$ も同様）として、以下の式で計算できる。

$$
r_{xy,z} = \cfrac{r_{xy} - r_{xz} r_{yz}}{\displaystyle \sqrt{1-r_{xz}^2} \sqrt{1-r_{yz}^2}}
$$

## 計算式の導出

### 準備1：分散・共分散の公式

変数 $x$ の期待値・分散を $E(x)$・$V(x)$、変数 $x,y$ の共分散を $\mathrm{Cov}(x,y)$ で表すと、以下の公式が成り立つ。

$$
\begin{eqnarray}
	V(x) &=& E(x^2) - E(x)^2 \\
	\mathrm{Cov}(x, y) &=& E(xy) - E(x)E(y)
\end{eqnarray}
$$

### 準備2：回帰直線の係数

確率変数 $x, y$ の間の最小二乗法による回帰直線

$$
y = a x + b
$$

の係数は、

$$
\begin{eqnarray}
	a &=& \cfrac{\mathrm{Cov}(x, y)}{V(x)} \\
	b &=& E(y) - a E(x)
\end{eqnarray}
$$


### 偏相関係数の導出

$x$ と $z$、$y$ と $z$ の間に線形な関係があると仮定する。  
これらの関係性を示す回帰直線は、定数 $a, b, c, d$ を用いて以下の式で表現できる。

$$
\begin{eqnarray}
	x &=& az + b \\
	y &=& cz + d
\end{eqnarray}
$$

$x$ と $z$、$y$ と $z$ が完全に線形な関係にあれば、全てのサンプルデータに対してこの等式が成り立つ。  
よって、$z$ が与える影響を $x, y$ から除外した変数として、

$$
\begin{eqnarray}
	x' &\equiv& x - (az + b) \\
	y' &\equiv& y - (cz + d)
\end{eqnarray}
$$

を定義できる。

回帰直線の係数の式から、

$$
\begin{eqnarray}
	x' &=& x - (az + b)
	\\ &=&
	x - az - (E(x) - a E(z))
	\\ &=&
	(x-E(x)) - a(z-E(z))
	\\
	y' &=& y - (cz + d)
	\\ &=&
	y - cz - (E(y) - c E(z))
	\\ &=&
	(y-E(y)) - c(z-E(z))
\end{eqnarray}
$$
求める偏相関係数 $r_{xy,z}$ を $x', y'$ の相関係数 $r_{x'y'}$ で定義すると、相関係数の定義と分散・共分散の公式より

$$
\begin{eqnarray}
	r_{xy,z} \equiv r_{x'y'} &=& \cfrac{\mathrm{Cov}(x', y')}{\sqrt{V(x')}\sqrt{V(y')}}
	\\ &=&
	\cfrac{E(x'y') - E(x')E(y')}
	{\sqrt{E(x'^2)-E(x')^2}\sqrt{E(y'^2)-E(y')^2}}
\end{eqnarray}
$$

回帰直線の係数の式を用いて、$E(x'), E(y'), E(x'^2), E(y'^2), E(x'y')$ をそれぞれ計算する。

$$
\begin{eqnarray}
	E(x') &=& E( (x-E(x)) - a(z-E(z)) )
	\\ &=&
	E(x) - E(x) - a E(z) + a E(z)
	\\ &=&
	0
	\\
	\\
	E(y') &=& \cdots
	\\ &=&
	0
	\\
	\\
	E(x'^2) &=&
	E( (x-E(x))^2 - 2a (x-E(x)) (z-E(z)) + a^2 (z-E(z))^2 )
	\\ &=&
	E( (x-E(x))^2 ) - 2a E( (x-E(x)) (z-E(z)) ) + a^2 E( (z-E(z))^2 )
	\\ &=&
	V(x) - 2a \mathrm{Cov}(x, z) + a^2 V(z)
	\\ &=&
	V(x) -
	\cfrac{2 \mathrm{Cov}(x, z)^2}{V(z)} +
	\cfrac{\mathrm{Cov}(x, z)^2}{V(z)}
	\\ &=&
	V(x) -
	\cfrac{\mathrm{Cov}(x, z)^2}{V(z)}
	\\ &=&
	V(x) \left( 1 -
	\cfrac{\mathrm{Cov}(x, z)^2}{V(x) V(z)}
	\right)
	\\ &=&
	V(x) (1 - r_{xz}^2)
	\\
	\\
	E(y'^2) &=& \cdots
	\\ &=&
	V(y) (1 - r_{yz}^2)
	\\
	\\
	E(x'y') &=&
	E(
		( (x-E(x)) - a(z-E(z)) )
		( (y-E(y)) - c(z-E(z)) )
	)
	\\ &=&
	ac E \left( (z-E(z))^2 \right) -
	a E \left( (y-E(y)) (z-E(z)) \right) -
	c E \left( (x-E(x)) (z-E(z)) \right) +
	E \left( (x-E(x)) (y-E(y)) \right)
	\\ &=&
	ac V(z) -
	a \mathrm{Cov}(y, z) -
	c \mathrm{Cov}(x, z) +
	\mathrm{Cov}(x, y)
	\\ &=&
	\cfrac{\mathrm{Cov}(x, z) \mathrm{Cov}(y, z)}{V(z)^2} V(z) -
	\cfrac{\mathrm{Cov}(x, z)}{V(z)} \mathrm{Cov}(y, z) -
	\cfrac{\mathrm{Cov}(y, z)}{V(z)} \mathrm{Cov}(x, z) +
	\mathrm{Cov}(x, y)
	\\ &=&
	\mathrm{Cov}(x, y) -
	\cfrac{\mathrm{Cov}(x, z) \mathrm{Cov}(y, z)}{V(z)}
	\\ &=&
	\sqrt{V(x)}\sqrt{V(y)}
	\left(
		\cfrac{\mathrm{Cov}(x, y)}{\sqrt{V(x)}\sqrt{V(y)}} -
		\cfrac{\mathrm{Cov}(x, z)}{\sqrt{V(x)}\sqrt{V(z)}}
		\cfrac{\mathrm{Cov}(y, z)}{\sqrt{V(y)}\sqrt{V(z)}}
	\right)
	\\ &=&
	\sqrt{V(x)}\sqrt{V(y)} ( r_{xy} - r_{xz} r_{yz} )
\end{eqnarray}
$$

以上を相関係数の式に代入して、

$$
\begin{eqnarray}
	r_{xy,z}　&=&
	\cfrac{E(x'y') - E(x')E(y')}
	{\sqrt{E(x'^2)-E(x')^2}\sqrt{E(y'^2)-E(y')^2}}
	\\　&=&
	\cfrac{
		\sqrt{V(x)}\sqrt{V(y)} ( r_{xy} - r_{xz} r_{yz} ) -
		0 \cdot 0
	}{
		\displaystyle
		\sqrt{V(x) (1 - r_{xz}^2) - 0^2}
		\sqrt{V(y) (1 - r_{yz}^2) - 0^2}
	}
	\\ &=&
	\cfrac{r_{xy} - r_{xz} r_{yz}}{\displaystyle \sqrt{1-r_{xz}^2} \sqrt{1-r_{yz}^2}}
\end{eqnarray}
$$

## 例

Python で相関係数を計算 & 散布図を描画する関数

```python
from matplotlib import pyplot as plt
import numpy as np

def calc_corrcoef(x_, y_, z_):
	"""
	3つの確率変数 x_, y_, z_ の互いの相関係数・偏相関係数を計算する
	"""
	corrcoef = np.corrcoef([x_, y_, z_])
	r_xy = corrcoef[0][1]
	r_yz = corrcoef[1][2]
	r_zx = corrcoef[2][0]
	r_xy_z = (r_xy - r_yz * r_zx) / np.sqrt(1 - r_yz**2) / np.sqrt(1 - r_zx**2)
	r_yz_x = (r_yz - r_zx * r_xy) / np.sqrt(1 - r_zx**2) / np.sqrt(1 - r_xy**2)
	r_zx_y = (r_zx - r_xy * r_yz) / np.sqrt(1 - r_xy**2) / np.sqrt(1 - r_yz**2)
	return ([r_xy, r_yz, r_zx], [r_xy_z, r_yz_x, r_zx_y])

def draw_correlation_graph(x, y, z, x_name, y_name, z_name):
	"""
	相関係数・偏相関係数と合わせて散布図を描画
	"""
	data = [x, y, z]
	var_name = [x_name, y_name, z_name]
	corrcoef, p_corrcoef = calc_corrcoef(x, y, z)
	fig, ax = plt.subplots(1, 3, figsize=(12, 4))
	plt.subplots_adjust(wspace=0.4, hspace=0.4)
	for i in range(3):
		ax[i].scatter(data[i], data[(i+1)%3], marker='.')
		ax[i].set_xlabel(var_name[i], fontsize=10)
		ax[i].set_ylabel(var_name[(i+1)%3], fontsize=10)
		ax[i].set_title(r'$r_{{{0}{1}}} = {3:.4f}, \quad r_{{{0}{1},{2}}} = {4:.4f}$'.format(var_name[i], var_name[(i+1)%3], var_name[(i+2)%3], corrcoef[i], p_corrcoef[i]))
		ax[i].grid()
	plt.show()
```

### 手作りデータ

3変数 $x, y, z$ を、
- $x, y$ が $z$ と相関を持つ（線形の関係）
- $x, y$ は直接的な相関を持たない（$z$ を交絡因子とする疑似相関）

という条件で生成する。

```python
from matplotlib import pyplot as plt
import numpy as np

N = 500
z = np.random.normal(loc=10.0, scale=1.0, size=N)

# z と相関を持たせないインデックスをランダムに選ぶ
idx_x = np.array(range(N))
idx_y = np.array(range(N))
np.random.shuffle(idx_x)
np.random.shuffle(idx_y)
idx_x_rand = idx_x[:int(N*0.3)]
idx_y_rand = idx_y[:int(N*0.2)]

# ランダムに一定割合のサンプルが z と相関を持つように x, y を生成
x = 2.5 * z + 4.2 + np.random.normal(loc=0, scale=1.0, size=N)
y = -3.2 * z + 1.8 + np.random.normal(loc=0, scale=1.0, size=N)
x[idx_x_rand] = np.random.normal(loc=x.mean(), scale=x.std(), size=len(idx_x_rand))
y[idx_y_rand] = np.random.normal(loc=y.mean(), scale=y.std(), size=len(idx_y_rand))

draw_correlation_graph(x, y, z, 'x', 'y', 'z')
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215377569-b51f0572-b593-404c-83ef-fba3909733bd.png)

- 相関係数 $r_{xy}, r_{yz}, r_{zx}$ を見ると $x, y, z$ は相互に相関がある
- 注目していない変数の影響を除いた偏相関係数 $r_{xy,z}, r_{yz,x}, r_{zx,y}$ を見ると、$x$ と $z$、$y$ と $z$ の間には相関が見られるが、$x$ と $y$ の間には相関がなさそう

→ 期待通り、$x$ と $y$ の間に直接的な関係性がなさそうなことが示されている

### 実データ：ニューヨークの大気の状態

[rdatasets](https://vincentarelbundock.github.io/Rdatasets/articles/data.html) より、ニューヨークの大気状態のデータを利用。

```python
from matplotlib import pyplot as plt
import statsmodels.api as sm
import numpy as np

ds = sm.datasets.get_rdataset("airquality", "datasets")
df = ds.data.dropna()

keys = ['Ozone','Solar.R','Wind','Temp']
corr = np.corrcoef(df[keys].T)
"""
         Ozone        Solar.R      Wind         Temp
array([[ 1.        ,  0.34834169, -0.61249658,  0.69854141],    Ozone
       [ 0.34834169,  1.        , -0.12718345,  0.29408764],    Solar.R
       [-0.61249658, -0.12718345,  1.        , -0.49718972],    Wind
       [ 0.69854141,  0.29408764, -0.49718972,  1.        ]])   Temp
"""
```

単純な相関係数の計算では、Ozone, Wind, Temp の間に相関がありそう。  
これら3要素のうち1つの影響を取り除いた偏相関を求めてみる。

```python
x, y, z = df['Ozone'], df['Wind'], df['Temp']
draw_correlation_graph(x, y, z, 'O', 'W', 'T')
```

![Figure_1](https://user-images.githubusercontent.com/13412823/215378527-662a7f27-9660-4451-a892-1a12467f65fa.png)

- 気温の影響を除外した場合も、オゾンと風の間には相関がありそう
- 風の影響を除外した場合も、オゾンと気温の間には相関がありそう
- オゾンの影響を除外すると、気温と風の間には直接的な相関はなさそう