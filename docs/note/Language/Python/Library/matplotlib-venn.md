---
title: matplotlib-venn
---

# matplotlib-venn とは

matplotlib においてベン図を書くためのライブラリ。

# 使い方

```python
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

venn2(subsets=(200, 100, 300), set_labels=('Condition A', 'Condition B'))
plt.title('Venn Diagram')
plt.show()
```

![](https://user-images.githubusercontent.com/13412823/167789370-fd30b9d1-7653-475d-81aa-fa50d9a9be31.png)


