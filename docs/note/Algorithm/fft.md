---
title: 高速フーリエ変換（FFT）
---

# 前提知識

## フーリエ変換

周期関数に限らず、任意の関数 $f(t)$ は、正弦波（$A \sin{\omega t}$ や $A \cos{\omega t}$。$A$, $\omega$ は定数）の和で表現できる（数学的な証明はここでは行わない）。  
$t$ を時間 [s] とすれば
- $\omega$ は波の角周波数 [rad/s]（周波数 $f$ [Hz] との関係は $\omega = 2\pi f$）
- $A$ は波の振幅

にあたる。

**フーリエ変換 = 関数 $f(t)$ を様々な周波数 $\omega$ の正弦波に分解する変換。各周波数の波がそれぞれどの程度の強さ（= 振幅 $A$）で混ざり合っているのかを求められる**

> **【公式】フーリエ変換**
> 
> フーリエ変換：
> 
> $$F(\omega) = \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt \tag{1}$$
> 
> フーリエ逆変換：
> 
> $$f(t) = \displaystyle \cfrac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} \,d\omega \tag{2}$$

> **【NOTE】逆変換の式の係数**
>
> フーリエ逆変換 $(2)$ の係数 $1/2\pi$ は、計算上の辻褄合わせ。  
> この係数なしで積分を行うと、$f(t)$ を変換した後に逆変換したとき、元の関数 $f(t)$ ではなく $2\pi f(t)$ になってしまうので、$1/2\pi$ をかけて元に戻るようにしてある。  
> つまり、変換の係数と逆変換の係数の積が $1/2\pi$ になっていれば何でも良く、書籍によっては以下のように定義されている：
> 
> $$
\begin{eqnarray}
    F(\omega) &=& \cfrac{1}{\sqrt{2\pi}} \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt
    \\
    f(t) &=& \cfrac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} \,d\omega
\end{eqnarray}
$$

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
→ 関数 $f(t)$ を、あらゆる（= 無限個の）周波数の波ではなく、有限個の異なる周波数 $\omega_i\,(i = 1, \cdots , N)$ の波に分解する。

- データサンプルの計測時間長 $T$
- サンプル総数 $N$
- 各サンプルの計測時刻 $t_n$、計測値 $f_n$（$n = 0, \cdots, N-1$）
  - サンプルは等間隔に取得：$t_n = n \Delta t$

に対して、DFT における周波数分解能は

$$\Delta f = \cfrac{1}{T}$$

また、時間間隔は

$$\Delta t = \cfrac{T}{N}$$

で与えられる。

$f(t)$ の DFT は

$$
F(\omega) = \displaystyle \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \,dt
 = \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \omega t_n} \Delta t
 = \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \omega \frac{nT}{N}}
$$

強度を求めたい周波数も等間隔に取り、

$$\omega = k \Delta \omega = 2 \pi k \Delta f = \cfrac{2 \pi k}{T}$$
$$k = 0, \cdots, N-1$$と置くと、

$$
F_k = F(\omega)
 = F(2 \pi k \Delta f)
 = \displaystyle \cfrac{T}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
$$

各周波数の強度（スペクトル密度）は、これを計測時間長 $T$ で割って

$$
\displaystyle \cfrac{1}{N} \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}
$$

これは複素数であり、

- 実部：波の偶関数成分（cos）
- 虚部：波の奇関数成分（sin）

という対応になっている。この複素数の絶対値を取ることでスペクトル密度が得られる。

1つの $k$ についてフーリエ係数を計算するのに $N$ 回の和を取るので、全ての $k$ について係数を得るための計算量は $O(N^2)$。

# 高速フーリエ変換（FFT）

**FFT = Fast Fourier Transform**

## 基本的な考え方

前提として、$N$ は2の冪乗となるように決める。

$F_k$ の和の部分

$$c_k \equiv \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk}$$

を高速に求めたい。

### 和を添字の偶数・奇数で分解

和の各要素を添字の偶数・奇数で分けると、

$$
\begin{eqnarray}
c_k &=& \displaystyle \sum_{n=0}^{N-1} f_n e^{-i \frac{2 \pi}{N} nk} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} e^{-i \frac{2 \pi}{N} 2nk} + \sum_{n=0}^{N/2-1} f_{2n+1} e^{-i \frac{2 \pi}{N} (2n+1)k} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_{2n} e^{-i \frac{2 \pi}{N/2} nk} + e^{-i \frac{2 \pi}{N} k} \sum_{n=0}^{N/2-1} f_{2n+1} e^{-i \frac{2 \pi}{N/2} nk}
\end{eqnarray}
$$

- 複素数空間の回転単位（回転子）$w_N \equiv e^{-i \frac{2 \pi}{N}}$
- 偶数添字・奇数添字成分 $f_n^{\rm e} \equiv f_{2n},\,\, f_n^{\rm o} \equiv f_{2n+1}$

と置くと、

$$
\begin{eqnarray}
c_k &=& \displaystyle \sum_{n=0}^{N-1} f_n w_N^{kn} \\
  &=& \displaystyle \sum_{n=0}^{N/2-1} f_n^{\rm e} w_{N/2}^{nk} + w_{N}^{k} \sum_{n=0}^{N/2-1} f_n^{\rm o} w_{N/2}^{nk}
\end{eqnarray}
$$

最後の式を見ると、

- 第1項：要素数 $N/2$ の DFT
- 第2項：要素数 $N/2$ の DFT に $w_N^k$ をかけたもの

となっている。  
即ち、**要素数 $N$ の DFT は、要素数 $N/2$ の DFT 2つに複素数 $w_N^k$ を掛けて和をとる処理に分解できる**。

分解された2つの DFT はそれぞれ計算量

$$
O\left(\left(\frac{N}{2}\right)^2\right) = O\left(\frac{N^2}{4}\right)
$$

となり、元の DFT の 1/4。

分かれた2つの DFT も再帰的に要素数半分の DFT の和に分解していくことができ、最終的には要素数1の DFT（要素の値をそのまま返却するだけ）になる。  


### $k \lt N/2$ かどうかで分けて考える

任意の $k$ について、

$$
\begin{eqnarray}
w_N^{k+N/2}     &=& e^{-i\frac{2 \pi}{N}(k + N/2)}   = e^{-i\frac{2 \pi}{N}k}e^{-i\pi}    = - w_N^k \\
w_{N/2}^{k+N/2} &=& e^{-i\frac{2 \pi}{N/2}(k + N/2)} = e^{-i\frac{2 \pi}{N/2}k}e^{-i2\pi} = w_{N/2}^k
\end{eqnarray}
$$

であるから、$k = 1, \cdots , \frac{N}{2}$ に対して

$$
\begin{eqnarray}
c_k       &=& \displaystyle \sum_{n=0}^{N/2-1} f_n^{\rm e} w_{N/2}^{nk} + w_N^k \sum_{n=0}^{N/2-1} f_n^{\rm o} w_{N/2}^{nk} \\
c_{k+N/2} &=& \displaystyle \sum_{n=0}^{N/2-1} f_n^{\rm e} w_{N/2}^{nk} - w_N^k \sum_{n=0}^{N/2-1} f_n^{\rm o} w_{N/2}^{nk}
\end{eqnarray}
$$

この式より、$c_k$ と $c_{k+N/2}$ の計算には同じ DFT、$w_N^k$ の値が使えることが分かる。  
即ち、$k = 1, \cdots , N$ のそれぞれに対して個別に DFT 2つと $w_N^k$ の計算が必要だったところを半分にできる。

> **【NOTE】**
> 
> 2つの DFT（$c_k$, $c_{k+N/2}$）を求める問題が、要素数半分の別の2つの DFT を求める問題に変換されている。


### 再計算を避けるための工夫

各 $k$ の DFT を個別に分解・計算すると、別の $k$ のときに一度計算したものを再計算してしまうことになり非効率。

例として、要素数8のデータサンプルの DFT を考える。  
各 $k$ に対応する DFT を要素数1の DFT（= そのまま要素を返すだけ）になるまで分解した結果を以下の図に示す。

- 矢印は実際に計算するときの流れ
  - 2本の矢印の合流点で、一方に $w_N^k$ や $-w_N^k$ をかけて足す
  - 矢印を逆にすれば、元の DFT が分解されていく過程になる
- `f_e`や`f_oeo`などは、添字の偶奇による DFT 分解の過程で作られた、元データの部分集合
  - `e`は偶数添字、`o`は奇数添字を抽出したことを示す
  - 例えば`f_oeo`は
    - `f = [f0, f1, f2, f3, f4, f5, f6, f7]`
    - 奇数添字を抽出：`f_o = [f1, f3, f5, f7]`
    - 偶数添字を抽出：`f_oe = [f1, f5]`
    - 奇数添字を抽出：`f_oeo = [f5]`

![fft_butterfly](https://user-images.githubusercontent.com/13412823/75625084-f5634a80-5bfd-11ea-90dc-68eef15b2739.png)

**この図が FFT の計算フロー**。図の形から、**バタフライ演算** と呼ばれる。

この計算フローには
- いずれのステップにおいても、2つの DFT の結果から、後のステップで使う新しい2つの DFT を計算
- 一度使った DFT は他の計算で再利用されないので捨てても困らない

という特徴があるため、長さ $N$ の配列（初期値はデータサンプル $f_n$）をステップごとに書き換えていくことで、空間計算量を節約できる（別配列を作る必要がない）。

（TODO: 続き。最終的な時間計算量）

## FFT の実装

{% gist 801c6ed6298b2d193ec7a5d7807ac5f7 20231014_fft.py %}

関数

$$
\begin{eqnarray}
    f(t) = A_1 \sin{2 \pi f_1 t} + A_2 \sin{2 \pi f_2 t}
    \\
    A_1 = 1.0,\, f_1 = 1.0 \mathrm{[Hz]}
    \\
    A_2 = 0.2,\, f_2 = 2.5 \mathrm{[Hz]}
\end{eqnarray}
$$ 
に対して、実装した FFT を適用してみる。  
また、numpy の fft 関数の結果と誤差がないか比較する。

{% gist 801c6ed6298b2d193ec7a5d7807ac5f7 ~adapt-fft.py %}

![fft](https://user-images.githubusercontent.com/13412823/275214863-39c153a6-fc1d-446d-844b-ccd5afe54cd1.png)

- いずれの実装も、numpy の fft 関数との誤差は極微小（正しく実装できていそう）
- $f(t)$ の定義通り、$f_1 = 1.0 \mathrm{[Hz]}$ と $f_1 = 2.5 \mathrm{[Hz]}$ のあたりにピークが観測される
- また、フーリエ変換で得られた振幅の比は定義した $A_1$ と $A_2$ の比（$1.0:0.2 = 5:1$）にだいたい一致


## 計算速度の比較

実装した各手法と `numpy.fft.fft` の速度を比較してみる：

{% gist 801c6ed6298b2d193ec7a5d7807ac5f7 ~compare-speed.py %}

![fft-speed](https://user-images.githubusercontent.com/13412823/275224596-41c6d2f9-255d-4006-b56b-cf9b72b49c7d.png)

DFT が圧倒的に遅いので、除外してデータ数を増やしてみる：

![fft-speed2](https://user-images.githubusercontent.com/13412823/275225513-16e34921-2004-4daa-b4b4-18416cd941fc.png)

- 愚直に和を取る離散フーリエ変換に比べて FFT が圧倒的に速い
- 同じ FFT の中でも、バタフライ演算に対応すればさらに大きく高速化（`fft` VS `fft_poor`）
- バタフライ演算対応版に比べても、numpy の `numpy.fft.fft` が速すぎる。実装どうなってるの...？

| 今回実装した FFT | `numpy.fft.fft` |
| :-- | :-- |
| ![fft-speed4](https://user-images.githubusercontent.com/13412823/275225515-93771393-4742-446d-925d-9d36b1a62ad6.png) | ![fft-speed3](https://user-images.githubusercontent.com/13412823/275225514-aa868cc7-fbb0-4be1-a596-4443b657d619.png) |

