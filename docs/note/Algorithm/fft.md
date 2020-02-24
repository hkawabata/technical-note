---
title: 高速フーリエ変換（FFT）
---

# 前提

## フーリエ変換

数学的な証明は除く。

周期関数に限らず、任意の関数 $$f(t)$$ は、正弦波（$$A \sin {\omega t}$$や$$A cos {\omega t}$$。$$A$$, $$\omega$$ は定数）の和で表現できる。  
$$t$$ を時間 [s] とすれば
- $$\omega$$ は波の角周波数 [rad/s]（周波数 $$f$$ [Hz] との関係は $$\omega = 2\pi f$$）
- $$A$$ は波の振幅に当たる。

**フーリエ変換 = 関数 $$f(t)$$ を様々な周波数 $$\omega$$ の正弦波に分解したとき、各周波数の波がそれぞれどの程度の強さ（= 振幅 $$A$$）で混ざり合っているのかを求める変換**

**【フーリエ変換公式】**

フーリエ変換：  
$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt$$

フーリエ逆変換：  
$$f(t) = \cfrac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{-i\omega t} \,d\omega$$

**【例】**

元関数：  
![Unknown-8](https://user-images.githubusercontent.com/13412823/75129130-f16d8f00-570a-11ea-8ee4-2eaf3b77bda9.png)

フーリエ変換：  
![Unknown-9](https://user-images.githubusercontent.com/13412823/75129129-f0d4f880-570a-11ea-8cc1-388e2d361fb5.png)

フーリエ逆変換：  
![Unknown-11](https://user-images.githubusercontent.com/13412823/75129160-12ce7b00-570b-11ea-9300-3e9b341a6c6f.png)


## 離散フーリエ変換

（TODO）

# 高速フーリエ変換

（TODO）
