---
title: Piecewise Aggregate Approximation (PAA)
---
# 概要

**Piecewise Aggregate Approximation (PAA)** は、時系列データを次元圧縮する手法の1つ。

# 手法

長さ $N$ の時系列 $R=\{r_1, r_2, \cdots, r_N\}$ の次元数を $N \to M\ (M \lt N)$ に圧縮することを考える。  
時系列の全区間（$t=1,2,\cdots,N$）を $M$ 個の区間に等分割し、この各区間でデータ点の平均値を取り、それを区間の代表値とする。

# 実装・動作確認

```python
import matplotlib.pyplot as plt
import numpy as np

def paa(t, r, m):
    """
    Piecewise Aggregate Approximation により次元削減
    t : 時刻の配列
    r : 時刻 t に対応する時系列データ
    m : 削減後の次元
    """
    n = len(r)   # 削減前の次元
    if n <= m:
        raise ValueError('m should be smaller than len(r)')
    # dt を極微小な値だけ大きくすることで int(max(t)/dt) が
    # list index out of range を引き起こすのを防ぐ
    dt = (max(t)-min(t)) / m * (1.0+1e-10)
    cnt = np.zeros(m)
    acc = np.zeros(m)
    for i in range(n):
        k = int(t[i]//dt)
        cnt[k] += 1
        acc[k] += r[i]
    r_new = acc / cnt
    t_new = (np.arange(m)+0.5)*dt + min(t)
    return t_new, r_new


N = 100
M = 20
t = np.linspace(0, np.pi*4, N)
r = np.sin(t) + np.random.rand(N)*0.4-0.2
t_new, r_new = paa(t, r, M)

plt.plot(t, r, label='$R$')
plt.scatter(t, r)
plt.plot(t_new, r_new, label='$R\'$')
plt.scatter(t_new, r_new)
for x in (t_new[1:]+t_new[:-1])/2:
    plt.axvline(x, 0, 1.0, lw=1.0, color='black', linestyle='dashed')

plt.legend()
plt.show()
```

![paa](https://gist.github.com/user-attachments/assets/21615051-fae5-4817-b979-fc1c14e4c6ea)


