---
title: 高速フーリエ変換（FFT）
---

# 前提知識

## フーリエ変換

数学的な証明は除く。

周期関数に限らず、任意の関数 $$f(t)$$ は、正弦波（$$A \sin{\omega t}$$や$$A \cos{\omega t}$$。$$A$$, $$\omega$$ は定数）の和で表現できる。  
$$t$$ を時間 [s] とすれば
- $$\omega$$ は波の角周波数 [rad/s]（周波数 $$f$$ [Hz] との関係は $$\omega = 2\pi f$$）
- $$A$$ は波の振幅に当たる。

**フーリエ変換 = 関数 $$f(t)$$ を様々な周波数 $$\omega$$ の正弦波に分解する変換。各周波数の波がそれぞれどの程度の強さ（= 振幅 $$A$$）で混ざり合っているのかを求められる**

**【フーリエ変換公式】**

フーリエ変換：  
$$F(\omega) = \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt$$

フーリエ逆変換：  
$$f(t) = \displaystyle \cfrac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} \,d\omega$$

**【例】**

元関数：  
![Unknown-8](https://user-images.githubusercontent.com/13412823/75129130-f16d8f00-570a-11ea-8ee4-2eaf3b77bda9.png)

フーリエ変換：  
![Unknown-9](https://user-images.githubusercontent.com/13412823/75129129-f0d4f880-570a-11ea-8cc1-388e2d361fb5.png)

フーリエ逆変換：  
![Unknown-11](https://user-images.githubusercontent.com/13412823/75129160-12ce7b00-570b-11ea-9300-3e9b341a6c6f.png)


## 離散フーリエ変換（DFT）

**DFT = Discrete Fourier Transform**

コンピュータで扱うデータとしての波は連続値ではなく離散値であり、無限個の処理はできない。  
→ 関数 $$f(t)$$ を、あらゆる（= 無限個の）周波数の波ではなく、有限個の異なる周波数 $$\omega_i\,(i = 1, \cdots , N)$$ の波に分解する。

- データサンプルの計測時間長 $$T$$
- サンプル総数 $$N$$
- 各サンプルの計測時刻 $$t_n$$、計測値 $$f_n$$（$$n = 0, \cdots, N-1$$）
  - サンプルは等間隔に取得：$$t_n = n \Delta t$$

に対して、DFT における周波数分解能は

$$\Delta f = \cfrac{1}{T}$$

また、時間間隔は

$$\Delta t = \cfrac{T}{N}$$

で与えられる。

$$f(t)$$ の DFT は

$$
F(\omega) = \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt
 = \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \omega t_n} \Delta t
 = \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \omega \frac{nT}{N}}
$$

強度を求めたい周波数も等間隔に取り、$$\omega = k \Delta \omega = 2 \pi k \Delta f = \cfrac{2 \pi k}{T}$$（$$k = 0, \cdots, N-1$$）と置くと、

$$
F_k = F(\omega)
 = F(2 \pi k \Delta f)
 = \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
$$

各周波数の強度（スペクトル密度）は、これを計測時間長 $$T$$ で割って

$$
\displaystyle \cfrac{1}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
$$

これは複素数であり、

- 実部：波の偶関数成分（cos）
- 虚部：波の奇関数成分（sin）

という対応になっている。この複素数の絶対値を取ることでスペクトル密度が得られる。

1つの $$k$$ についてフーリエ係数を計算するのに $$N$$ 回の和を取るので、全ての $$k$$ について係数を得るための計算量は $$O(N^2)$$。

# 高速フーリエ変換（FFT）

**FFT = Fast Fourier Transform**

## 基本的な考え方

前提として、$$N$$ は2の冪乗となるように決める。

$$F_k$$ の和の部分

$$c_k \equiv \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}$$

を高速に求めたい。

### 和を偶数番目と奇数番目に分解

和の各要素を偶数番目と奇数番目に分けると、

$$
\begin{eqnarray}
c_k &=& \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} e^{-i \frac{2 \pi}{N} 2nk} + \sum_{n=0}^{N/2-1} f_{2n+1} e^{-i \frac{2 \pi}{N} (2n+1)k} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} e^{-i \frac{2 \pi}{N/2} nk} + e^{-i \frac{2 \pi}{N} k} \sum_{n=0}^{N/2-1} f_{2n+1} e^{-i \frac{2 \pi}{N/2} nk}
\end{eqnarray}
$$

$$w_N \equiv e^{-i \frac{2 \pi}{N}}$$ と置くと、

$$
\begin{eqnarray}
c_k &=& \displaystyle \sum_{n=0}^{N-1} f_n w_N^{kn} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} w_{N/2}^{nk} + w_{N}^{k} \sum_{n=0}^{N/2-1} f_{2n+1} w_{N/2}^{nk}
\end{eqnarray}
$$

最後の式を見ると、

- 第1項：要素数 $$N/2$$ の DFT
- 第2項：要素数 $$N/2$$ の DFT に $$w_N^k$$ をかけたもの

となっている。  
即ち、**要素数 $$N$$ の DFT は、要素数 $$N/2$$ の DFT 2つに複素数 $$w_N^k$$ を掛けて和をとる処理に分解できる**。

2つの DFT はそれぞれ計算量 $$O\left(\left(\frac{N}{2}\right)^2\right) = O\left(\frac{N^2}{4}\right)$$ なので、この式変形により元の DFT の計算量は $$O\left(2 \cdot \frac{N^2}{4}\right) = O\left(\frac{N^2}{2}\right)$$ に下がる。

再帰的に、分かれた2つの DFT もそれぞれ要素数半分の DFT の和に分解していけるので、最終的な計算量は $$O(N \log2{N})$$ になる。


### $$k \lt N/2$$ かどうかで分解

任意の $$k$$ について、

$$
\begin{eqnarray}
w_N^{k+N/2}     &=& e^{-i\frac{2 \pi}{N}(k + N/2)}   = e^{-i\frac{2 \pi}{N}k}e^{-i\pi}    = - w_N^k \\
w_{N/2}^{k+N/2} &=& e^{-i\frac{2 \pi}{N/2}(k + N/2)} = e^{-i\frac{2 \pi}{N/2}k}e^{-i2\pi} = w_{N/2}^k
\end{eqnarray}
$$

であるから、$$k = 1, \cdots , \frac{N}{2}$$ に対して

$$
\begin{eqnarray}
c_k       &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} w_{N/2}^{nk} + w_N^{k} \sum_{n=0}^{N/2-1} f_{2n+1} w_{N/2}^{nk} \\
c_{k+N/2} &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} w_{N/2}^{nk} - w_N^{k} \sum_{n=0}^{N/2-1} f_{2n+1} w_{N/2}^{nk}
\end{eqnarray}
$$

この式より、$$c_k$$ と $$c_{k+N/2}$$ の計算には同じ DFT、$$w_N^k$$ の値が使えることが分かる。  
即ち、$$k = 1, \cdots , N$$ のそれぞれに対して個別に DFT 2つと $$w_N^k$$ の計算が必要だったところを半分にできる。

（TODO: 続き）

## サンプルコード

```python
import numpy as np

def dft(f_):
    """
    愚直に和を取る
    """
    N_ = len(f_)
    F_ = np.full(N_, 0j)
    x = -1j*2*np.pi/N_
    for k in range(N_):
        for n in range(N_):
            F_[k] += f_[n] * np.exp(x*k*n)
    return F_

def fft_poor(f_, start=0, d=1):
    """
    各kのDFTを再帰的に2分割して高速化
    - バタフライ演算非対応
    - 配列を何度も作るのでコストがかかっていそう
    """
    N_ = len(f_) / d
    if 1 < N_:
        return fft_poor(f_, start, d*2) + fft_poor(f_, start+d, d*2) * np.exp(-1j*2*np.pi*np.arange(len(f_))/N_)
    else:
        return np.array([f_[start]])

def fft(f_):
    """
    Cooley-Tukey アルゴリズム
    """
    N_ = len(f_)
    b = int(np.log2(N_))
    F_ = []
    for i in range(N_):
        F_.append(f_[reverse_bit(i, b)])
    window = 1
    while window < N_:
        window <<= 1
        j = 0
        for i in range(N_):
            if i%window < window/2:
                k = int(i + window/2)
                wi = np.exp(-1j * 2 * np.pi * (i%window) / window)
                wk = np.exp(-1j * 2 * np.pi * (k%window) / window)
                F_[i], F_[k] = F_[i] + wi * F_[k], F_[i] + wk * F_[k]
    return F_

def reverse_bit(num, b):
    """
    bビットの数値numのビットを逆順に変換
    - ex. num=2, b=4 の場合、0010 => 0100 => 4
    - ex. num=20, b=6 の場合、010100 => 001010 => 10
    """
    tmp = num
    res = tmp & 1
    for _ in range(b-1):
        tmp >>= 1
        res = (res << 1) | (tmp & 1)
    return res
```

関数 $$f(t) = \sin{60 \pi t} + 0.1 \sin{600 \pi t}$$ に FFT を適用：

![Unknown-6](https://user-images.githubusercontent.com/13412823/75610477-c218b100-5b54-11ea-9539-7fddce19666e.png)

## 速度の比較

![Unknown-1](https://user-images.githubusercontent.com/13412823/75618487-5f560280-5bb2-11ea-8769-e15b84a92315.png)


