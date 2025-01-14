---
title: Shape-Based Distance (SBD)
---
# 概要

**Shape-based Distance (SBD)** は、2つの時系列データの類似性を評価するための指標の1つ。  
時間方向・振幅方向のシフトを許容して形状を比較することが可能。

# 計算方法

前処理段階で2つの時系列データ $R=\{r_1,r_2,\cdots,r_T\},\ S=\{s_1,s_2,\cdots,s_T\}$ は標準化されているものとする：

$$
E(r_i) = E(s_j) = 0,\ V(r_i) = E(s_j) = 1
$$

ここで $E$ は期待値、$V$ は分散を表す。

時系列データ $R$ と、$S$ に時間ステップのシフト $\tau = 0,1,2,\cdots,T-1$ を施したものとの相関係数 $NCC(\tau)$ を計算する：

$$
NCC(\tau) := \cfrac{
    \sum_{i=1}^T r_i s_{i+\tau}
}{
    \sqrt{\sum_{i=1}^T r_i^2} \sqrt{\sum_{i=1}^T s_{i+\tau}^2}
}
$$

ここで、$r_i,s_j$ はともに標準化されている想定のため、相関係数の計算式には平均値が出てこない。

この中で、最も $NCC(\tau)$ の値が大きくなるような $\tau$ を $\tau^*$ とすると、shape-based distance $SBD(R,S)$ は以下の式で計算される。

$$
SBD(R, S) = 1-NCC(\tau^*)
$$

# 実装・動作確認

```python
import numpy as np

def sbd(r, s, report=False):
    T = len(r)
    r_norm = (r - r.mean()) / r.std()
    s_norm = (s - s.mean()) / s.std()
    ncc_max = -np.inf
    tau_best = 0
    for tau in range(T):
        s_shift = np.concatenate([s[T-tau:], s[:T-tau]])
        ncc = np.corrcoef(r_norm, s_shift)[0,1]
        if ncc_max < ncc:
            ncc_max = ncc
            tau_best = tau
    ret = 1 - ncc_max
    if report:
        plt.title(r'$SBD = {:.4f}, \tau^* = {}$'.format(ret, tau_best))
        plt.plot(r, label=r'$R(t)$')
        plt.plot(s, label=r'$S(t)$')
        plt.plot(np.concatenate([s[T-tau_best:], s[:T-tau_best]]), label=r'$S(t-\tau^*)$')
        plt.grid()
        plt.legend()
        plt.show()
    return ret


T = 100
t = np.linspace(0, np.pi*4, T)
x0 = np.sin(t) + np.random.rand(T)*0.4-0.2
x1a = np.sin(t-np.pi/4) + np.random.rand(T)*0.4-0.2
x1b = np.sin(t-np.pi/2) + np.random.rand(T)*0.4-0.2
x2a = np.sin(t) + 1.0 + np.random.rand(T)*0.4-0.2
x2b = np.sin(t) + 2.0 + np.random.rand(T)*0.4-0.2
x3a = np.sin(0.8*t) + np.random.rand(T)*0.4-0.2
x3b = np.sin(1.2*t) + np.random.rand(T)*0.4-0.2
x4a = 0.5*np.sin(t) + np.random.rand(T)*0.4-0.2
x4b = 2.0*np.sin(t) + np.random.rand(T)*0.4-0.2
sbd(x0, x1a, True)
sbd(x0, x1b, True)
sbd(x0, x2a, True)
sbd(x0, x2b, True)
sbd(x0, x3a, True)
sbd(x0, x3b, True)
sbd(x0, x4a, True)
sbd(x0, x4b, True)
```

| 操作          | 例1                                                                                          | 例2                                                                                          | SBD | 考察                      |
| :---------- | :------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------ | --- | ----------------------- |
| 平行移動（時間方向）  | ![1a](https://gist.github.com/user-attachments/assets/f8b56640-fd0b-4a77-bc43-9809916b2c40) | ![1b](https://gist.github.com/user-attachments/assets/bf250b01-201b-4a4d-9599-34120d1cd45d) | 小   | 最適な時間シフト $\tau^*$ 選択の効果 |
| 平行移動（振幅方向）  | ![2a](https://gist.github.com/user-attachments/assets/d3818b61-16cd-41d8-b67d-c5413c7e4484) | ![2b](https://gist.github.com/user-attachments/assets/d8a6b8ee-3a7c-4a64-b5c9-267a580340cb) | 小   | 標準化の効果                  |
| 拡大・縮小（時間方向） | ![3a](https://gist.github.com/user-attachments/assets/893d5c93-0b9b-41ff-9fe6-534bdb086cb2) | ![3b](https://gist.github.com/user-attachments/assets/0e896931-277a-4e3f-9038-71fe3092ef2f) | 大   | 時間シフトや標準化では違いを吸収できない    |
| 拡大・縮小（振幅方向） | ![4a](https://gist.github.com/user-attachments/assets/916e03de-ac72-4d60-8cb7-3320dfc72269) | ![4b](https://gist.github.com/user-attachments/assets/41783424-5d8e-4a85-8083-52c2e26336ed) | 小   | 標準化の効果                  |
