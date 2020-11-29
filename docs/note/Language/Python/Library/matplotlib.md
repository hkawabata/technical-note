---
title: matplotlib
---

# matplotlib とは

Python の画像処理ライブラリ。

![anatomy](https://user-images.githubusercontent.com/13412823/100397531-83853800-308d-11eb-993d-7a32700fbbb9.png)

（[Usage Guide](https://matplotlib.org/tutorials/introductory/usage.html) より）

# 使い方

```bash
$ pip install matplotlib
```

## 種々の描画

### 折れ線

```python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 1.4, 0.01)
y1 = x ** 2
y2 = x ** 3

# グラフのタイトル
plt.title('The Title')
# X軸, Y軸のラベル
plt.xlabel('value of $x$')
plt.ylabel('value of $y$')
# X軸, Y軸の描画範囲
plt.xlim(0, 2.0)
plt.ylim(0, 3.5)
# 目盛りの設定
plt.xticks([0.1, 0.2, 0.4, 0.8, 1.6])
plt.yticks(np.arange(0, 3.0, 0.15))
# 線の色, 線の太さ, 凡例
plt.plot(x, y1, color='blue', linewidth=1.0, label='$x^2$')
plt.plot(x, y2, color='red',  linewidth=2.0, label='$x^3$')
# 凡例を表示させる
plt.legend()
# グリッドを表示させる
plt.grid()

plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100530912-30e97e80-323b-11eb-9799-9ac22091d71a.png)


### 散布図


### ヒストグラム


## グラフの配置


## Tips

### 凡例の位置調整


### 塗りつぶし

```python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-4.0, 4.0, 0.01)
y1 = np.sin(x+1)
y2 = np.sin(x)
y3 = 0.2 * x

plt.plot(x, y1, color='black')
plt.plot(x, y2, color='black')
plt.plot(x, y3, color='black')
plt.fill_between(x, y1, y2, facecolor='red', alpha=0.3, label='foo')
plt.fill_between(x, y2, y3, facecolor='red', alpha=0.7, label='bar', where=(x>0)&(y3<y2))
plt.grid()
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100530930-82920900-323b-11eb-896e-a2726abd17db.png)

