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

1つの周波数 $$\omega_i$$ の波は、振幅を $$A_i$$、位相ズレ（時間方向の平行移動）を $$\phi_i$$ として

$$A_i \sin{(\omega_i t + \phi_i)} = A_i \cos{\phi_i} \sin{\omega_i t} + A_i \sin{\phi_i} \cos{\omega_i t} = a_i \sin{\omega_i t} + b_i \cos{\omega_i t}$$

$$a_i \equiv A_i \cos{\phi_i}, b_i \equiv A_i \sin{\phi_i}$$

と表現できる。  

よって、$$f(t)$$ を $$N$$ 個の周波数の波に分解すると

$$f(t) = \displaystyle \sum_{i=1}^N (a_i \sin{\omega_i t} + b_i \cos{\omega_i t})$$

波の決定のためには、$$2N$$ 個の定数 $$(a_1, \cdots , a_N, b_1, \cdots , b_N)$$ が求まれば良い。  
以下の $$2N$$ 元1次連立方程式を解くことになるので、異なる $$2N$$ 個の時刻 $$t_j\,(j = 1, \cdots , 2N)$$ に対する $$f(t)$$ のデータサンプルが必要。

$$
\begin{pmatrix}
\sin{\omega_1 t_1} & \cdots & \sin{\omega_N t_1} & \cos{\omega_1 t_1} & \cdots & \cos{\omega_N t_1}\\
\vdots & & & & & \vdots \\
\sin{\omega_1 t_N} & \cdots & \sin{\omega_N t_N} & \cos{\omega_1 t_N} & \cdots & \cos{\omega_N t_N}\\
\sin{\omega_1 t_{N+1}} & \cdots & \sin{\omega_N t_{N+1}} & \cos{\omega_1 t_{N+1}} & \cdots & \cos{\omega_N t_{N+1}}
\vdots & & & & & \vdots \\
\sin{\omega_1 t_{2N}} & \cdots & \sin{\omega_N t_{2N}} & \cos{\omega_1 t_{2N}} & \cdots & \cos{\omega_N t_{2N}}
\end{pmatrix}
\left( \begin{array}
{c} a_1 \\ \vdots \\ a_N \\ b_1 \\ \vdots \\ b_N
\end{array} \right)
=
\left( \begin{array}
{c} f(t_1) \\ \vdots \\ f(t_{N}) \\ f(t_{N+1}) \\ \vdots \\ f(t_{2N})
\end{array} \right)
$$

**【問題点】**  
素直に方程式を解くと、データの規模が大きくなるにつれて時間計算量・空間計算量が飛躍的に増大
- 時間計算量 $$O(N^3)$$
- 空間計算量 $$O(N^2)$$


# 高速フーリエ変換

（TODO）
