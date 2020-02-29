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


## 離散フーリエ変換

コンピュータで扱うデータとしての波は連続値ではなく離散値であり、無限個の処理はできない。  
→ 関数 $$f(t)$$ を、あらゆる（= 無限個の）周波数の波ではなく、有限個の異なる周波数 $$\omega_i\,(i = 1, \cdots , N)$$ の波に分解する。

- データサンプルの計測時間長 $$T$$
- サンプル総数 $$N$$
- 各サンプルの計測時刻 $$t_n$$、計測値 $$f_n$$（$$n = 0, \cdots, N-1$$）
  - サンプルは等間隔に取得：$$t_n = n \Delta t$$

に対して、離散フーリエ変換における周波数分解能は

$$\Delta f = \cfrac{1}{T}$$

また、時間間隔は

$$\Delta t = \cfrac{T}{N}$$

で与えられる。

$$f(t)$$ のフーリエ変換は

$$
\begin{eqnarray}
F(\omega) &=& \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt \\
 &=& \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \omega t_n} \Delta t \\
 &=& \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \omega \frac{nT}{N}}
\end{eqnarray}
$$

強度を求めたい周波数も等間隔に取り、$$\omega = k \Delta \omega = 2 \pi k \Delta f = \cfrac{2 \pi k}{T}$$（$$k = 0, \cdots, N-1$$）と置くと、

$$
\begin{eqnarray}
F_k &=& F(\omega) = F(2 \pi k \Delta f) \\
 &=& \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
\end{eqnarray}
$$

各周波数の強度（スペクトル密度）は、これを計測時間長 $$T$$ で割って

$$
\displaystyle \cfrac{1}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
$$

これは複素数であり、

- 実部：波の偶関数成分（cos）
- 虚部：波の奇関数成分（sin）

という対応になっている。この複素数の絶対値を取ることでスペクトル密度が得られる。


# 高速フーリエ変換

（TODO）
