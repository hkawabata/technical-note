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

```python
from matplotlib import pyplot as plt
import numpy as np

N = 1000
x = np.random.randn(N)
plt.hist(x, bins=20, label='hoge')
plt.legend()
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100531045-321bab00-323d-11eb-8c21-e875ebda5cb7.png)


## グラフの配置


## Tips

### 線・点のスタイル

線のスタイル：

```python
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 10.0+1, 1.0)
y = x * 0.2
linestyles = [
    'solid', 'dashed', 'dotted', 'dashdot',
    (0, (1, 10)),
    (0, (5, 10)),
    (0, (5, 1)),
    (0, (3, 10, 1, 10)),
    (0, (3, 1, 1, 1)),
    (0, (3, 5, 1, 5, 1, 5)),
    (0, (3, 10, 1, 10, 1, 10)),
    (0, (3, 1, 1, 1, 1, 1))
]
for style in linestyles:
    plt.plot(x, y, linestyle=style, label='{}'.format(style))
    y += 1.0
plt.legend(ncol=1, bbox_to_anchor=(1.05, 0.93, 0.5, .100))
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100531139-ecabad80-323d-11eb-978e-b26d87617ed3.png)

点のスタイル：

```python
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

x, y = np.array([0]), np.array([0])
cnt = 0
for k, v in Line2D.markers.items():
    if cnt%10 == 0:
        x = 0
        y += 1
    x += 1
    plt.scatter(x, y, marker=k, label='{} {}'.format(k, v))
    cnt += 1
plt.legend(ncol=3, bbox_to_anchor=(1.05, 0.93, 0.5, .100))
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/100531141-ee757100-323d-11eb-89cb-623394b8d6da.png)


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

