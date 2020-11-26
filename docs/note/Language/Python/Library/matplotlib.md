---
title: matplotlib
---

# matplotlib とは

Python の画像処理ライブラリ。

# 使い方

```bash
$ pip install matplotlib
```

## 単純なグラフ描画

```python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.01)
y1 = x ** 2
y2 = x ** 3

plt.plot(x, y1)
plt.plot(x, y2)
```

![](https://user-images.githubusercontent.com/13412823/100396806-e2e14900-3089-11eb-9494-7fb92890c1d7.png)

## 種々の描画設定

```python
# グラフのタイトル
plt.title('The Title')
# X軸, Y軸のラベル
plt.xlabel('value of $x$')
plt.ylabel('value of $y$')
# X軸, Y軸の描画範囲
plt.xlim(0, 1.4)
plt.ylim(0, 1.2)
# 目盛りの設定
plt.xticks([0.1, 0.2, 0.4, 0.8])
plt.yticks(np.arange(0, 1.0, 0.05))
# 線の色, 線の太さ, 凡例
plt.plot(x, y1, color='blue', linewidth=1.0, label='$x^2$')
plt.plot(x, y2, color='red',  linewidth=2.0, label='$x^3$')
# 凡例を表示させる
plt.legend()
# グリッドを表示させる
plt.grid()

plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100397384-b844bf80-308c-11eb-812e-87053e797f80.png)


## グラフの配置


## Tips

### 凡例の位置調整


