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

![](https://user-images.githubusercontent.com/13412823/100397768-dca19b80-308e-11eb-8084-041393a1a115.png)


### 散布図


### ヒストグラム


## グラフの配置


## Tips

### 凡例の位置調整


