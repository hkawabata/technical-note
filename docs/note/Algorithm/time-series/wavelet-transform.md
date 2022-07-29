---
title: ウェーブレット変換
---

# ウェーブレット変換とは

wavelet transform

時系列データに対して、信号の時間と周波数の関係を同時に解析するための手法。

同じく時系列データを解析する手法としてフーリエ変換があるが、フーリエ変換によるスペクトル解析では、時間方向の情報が失われてしまうため、例えば「時間が後ろになるほど周波数が高くなる」ような状況を解析することが難しい。

<img src="https://user-images.githubusercontent.com/13412823/181401297-0dd45ece-355e-4831-b176-c418c5f44c24.png" alt="" width="500">

ウェーブレット変換ではその欠点を補い、時間とともにデータの周期性が変化していく様子を捉えることができる。

# 基本的な考え方

## ウェーブレットの導入

信号の周波数成分を解析するための物差しとして導入する、「波の断片」。
基準となる**マザーウェーブレット**をメキシカンハット関数

$$
\psi(t) = \left(1 - t^2 \right) \exp{ \left( - \cfrac{t^2}{2} \right)}
$$

などで定義する。

<img src="https://user-images.githubusercontent.com/13412823/181408870-68f10e7e-dfa2-4ef5-8b79-e28e51acec71.png" alt="" width="500">

これを拡大・縮小 / 平行移動して、色々な形のウェーブレットを生成して用いる：

$$
\psi_{\sigma, t_0}(t) = \left(1 - \cfrac{(t-t_0)^2}{\sigma^2} \right) \exp{ \left( - \cfrac{(t-t_0)^2}{2\sigma^2} \right)}
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/181471261-eed5ff18-6383-434f-89c6-3b197816c98d.png)

<details>
<summary>（作図に使ったコード）</summary>
{% gist 3bd481ef29271e88d567126aa0efb1b2 wavelet.py %}
</details>


## 時間・周波数的な特徴の計算

用意した色々なウェーブレット $\psi_{\sigma, t_0}(t)$ と元の時系列データ $f(t)$ とで、同じ時刻の成分どうしの積 $\psi_{\sigma, t_0}(t) f(t)$ を取り、全区間で積分することを考える。

$$
I(\sigma, t_0) = \int_{-\infty}^{\infty} \psi_{\sigma, t_0}(t) f(t) dt
$$

ウェーブレット $\psi_{\sigma, t_0}(t)$ は、以下の特徴を持つ波であると考えることができる。
- 特定の時刻 $t_0$ 付近だけに高い振幅を持つ
- 周期が $\sigma$ に比例する

なので、
- 積 $\psi_{\sigma, t_0}(t) f(t)$ の値は、時刻 $t_0$ 付近以外ではゼロに近い値になる
- その積分である $I(\sigma, t_0)$ の値は、時刻 $t_0$ 付近に同じ周期・同じ位相の波が存在すると大きな値になる


$$
\int_{-\infty}^{\infty} \psi_{\sigma, t_0}(t) f(t) dt
$$

<details>
<summary>（作図に使ったコード）</summary>

```python
from matplotlib import pyplot as plt
import numpy as np

def mexican_hat(t, sigma, t0):
    tmp = ((t - t0) / sigma)**2
    return (1 - tmp) * np.exp(-tmp/2)

t = np.arange(2000) / 100

t0_list = [5.0, 10.0, 15.0]
sigma_list = [0.5, 1.0, 2.0]

fig = plt.figure(figsize=(9,9))
c = 0
for t0 in t0_list:
    for sigma in sigma_list:
        c += 1
        y = mexican_hat(t, sigma, t0)
        ax = fig.add_subplot(3, 3, c)
        ax.set_title('$\sigma = ' + str(sigma) + ', t_0 = ' + str(t0) + '$')
        ax.plot(t, y)
        ax.grid()

plt.tight_layout()
plt.show()
```

</details>