---
title: matplotlib-venn
---

# matplotlib-venn とは

matplotlib においてベン図を書くためのライブラリ。

# 使い方

```bash
pip install matplotlib-venn
```

## 基本機能

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted

venn2(
	subsets=(200, 100, 300),
	set_labels=('Group A', 'Group B')
)
plt.title('Venn Diagram')
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/167789370-fd30b9d1-7653-475d-81aa-fa50d9a9be31.png)

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted

venn3(
	subsets=(200, 100, 300, 50, 80, 100, 20),
	set_labels=('Group A', 'Group B', 'Group C')
)
plt.title('Venn Diagram')
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/238243010-69f2a4f4-722f-4230-9555-04a726738cf7.png)


## カスタマイズ

### 背景色・透過度

```python
venn2(
	subsets=(200, 100, 300),
	set_labels=('Group A', 'Group B'),
	set_colors=('blue', 'red'),  # 背景色
	alpha=0.7                    # 透過度
)
plt.title('Change colors & alpha')
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/238242035-90f40d8d-9b22-44cb-878c-e275921ce964.png)


### サイズによって円の大きさを変えない

```python
venn2_unweighted(
	subsets = (100, 10, 1),
	set_labels = ('Group A', 'Group B')
)
plt.title('venn2_unweighted')
plt.show()
```

![Figure_2](https://user-images.githubusercontent.com/13412823/238242040-62a1c1b2-9043-4fa1-ab66-1b05454dcc4f.png)


### 色を塗らず境界線だけを書く

```python
venn2_circles(
	subsets = (200, 100, 300),
	linestyle='dashed',         # 線の種類（デフォルトは実線）
	linewidth=2                 # 線の太さ
)
plt.title('venn2_circles')
plt.show()
```

![Figure_3](https://user-images.githubusercontent.com/13412823/238242043-ee2bd942-486f-4053-b87b-32ec8e40d845.png)


### 円ごとに境界線の太さを変える

```python
v = venn2_circles(
	subsets = (200, 100, 300)
)
v[0].set_lw(2)
v[1].set_lw(4)
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/13412823/238242713-c4226878-f771-47d0-9be2-697f87dd64b2.png)

