---
title: DTW
---
# DTW とは

= **Dynamic Time Warping, 動的時間伸縮**

時系列データの類似度を測る手法の1つ。  
2つの時系列に対して、データ点間の距離（誤差の絶対値）を総当たりで全て求めた上で２つの時系列が最短となるパスを探す。


# DTW の特徴

比較対象が同じ時刻のデータ点である必要はないため、時系列同士の長さや周期が違っても類似度を求めることができる。


# 定義

2つの時系列 $R=\{r_1,r_2,r_3,\cdots,r_M\}, S=\{s_1,s_2,s_3,\cdots,s_N\}$ があるとき、以下の条件を満たすように $R,S$ 上のデータ点をマッピングする。
- 全ての $R$ のデータ点 $r_i$ が $S$ のいずれか1つ以上のデータ点 $s_j$ にマッピングされる。逆も同様
- マッピングに対応するデータ点のペアを結ぶ線分は交差しない

このようなマッピングは複数考えられるが、対応する線分の長さの総和が最も小さくなるもの選び、その総和の値を DTW（動的時間伸縮）と呼ぶ。

| ユークリッド距離                                                                                           | DTW                                                                                              |
| :------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| ![euclidean](https://gist.github.com/user-attachments/assets/9db08bab-32a4-40e7-ba40-2a1c13b1f37c) | ![dtw](https://gist.github.com/user-attachments/assets/09a9bfaf-a313-4a86-8737-fbeaef3b0b89)<br> |


# 計算方法

## 理論

まず、全ての $r_i,s_j$ の組み合わせについて、コスト関数としてユークリッド距離 $d(r_i,s_j)$ を計算し（必要に応じて他のコスト関数を用いても良い）、これを並べたコスト行列を考える：

$$
\begin{pmatrix}
    d(r_1, s_1) & d(r_1, s_2) & \cdots & d(r_1, s_N) \\
    d(r_2, s_1) &  &  & \vdots \\
    \vdots \\
    d(r_M, s_1) & \cdots &  & d(r_M, s_N)
\end{pmatrix}
$$

この行列の一番左上 $d(r_1,s_1)$ から出発し、「右」「下」「右下」いずれかに1つ進みながら、通過した要素の $d(r_i,s_j)$ の値の和を取っていき、一番右下 $d(r_M,s_N)$ に到着したときの総和が最も小さくなるような経路を探す。  
このときの総和が求める DTW となる。

> **【NOTE】探索方向の制約の意味**
> 
> 「右」「下」「右下」いずれかにしか進めないという制約は、DTW の定義にある「データ点のペアを結ぶ線分が交差しない」という条件に対応している。  
> 左や上のように出発点へ戻る方向への探索をすると、例えば $d(r_2,s_2)\to d(r_2,s_1) \to d(r_3, s_1)$（左、下の順に探索）といった経路を通ったとき、ペア $(r_2, s_2)$ を結ぶ線分と $(r_3,s_1)$ は交差してしまう。

## アルゴリズム

以下のように動的計画法で求めることができる。
1. 「点 $d(r_i,s_j)$ から出発して右下 $d(r_M,s_N)$ まで行くときの距離の総和の最小値」を記録する行列 $DTW_{i,j}$ を作成
2. $DTW$ 行列の右下の値をセット：$DTW_{M,N} \gets d(r_M,s_N)$
3. $DTW$ 行列の最下行、最右列の値を計算
    1. 最下行：$i=M-1, M-2, M-3, \cdots, 1$ の順に $DTW_{i,N} \gets DTW_{i+1,N}+d(r_i,s_N)$
    2. 最左列：$j=N-1, N-2, N-3, \cdots, 1$ の順に $DTW_{M,j} \gets DTW_{M,j+1}+d(r_M,s_j)$
4. $DTW$ 行列の未計算の要素を右下から左上に向かって順に計算
    1. $DTW_{i,j} \gets \mathrm{min}(DTW_{i+1,j},DTW_{i,j+1},DTW_{i+1,j+1})+d(r_i,s_N)$
5. 4の計算の最後に得られる $DTW$ 行列の一番右上の要素 $DTW_{1,1}$ が求める DTW となる

## 実装・動作確認

以下の実装ではコードの読みやすさのため、上の解説とは逆に、右下の $d(r_M,s_N)$ を出発して「左」「上」「左上」の移動を繰り返しながら $d(r_1, s_1)$ を目指す方法で DTW を求めている。

```python
import numpy as np
import matplotlib.pyplot as plt

def calc_dtw(x1, y1, x2, y2, report=False):
    T1, T2 = len(x1), len(x2)
    d = np.zeros((T1, T2))
    for i1 in range(T1):
        for i2 in range(T2):
            d[i1][i2] = np.sqrt((x1[i1]-x2[i2])**2 + (y1[i1]-y2[i2])**2)
    dtw = np.zeros((T1, T2))
    dtw[0][0] = d[0][0]
    for i1 in range(1, T1):
        dtw[i1][0] = d[i1][0] + dtw[i1-1][0]
    for i2 in range(1, T2):
        dtw[0][i2] = d[0][i2] + dtw[0][i2-1]
    for i1 in range(1, T1):
        for i2 in range(1, T2):
            a, b, c = dtw[i1][i2-1], dtw[i1-1][i2], dtw[i1-1][i2-1]
            if min(a, b, c) == a:
                dtw[i1][i2] = d[i1][i2] + dtw[i1][i2-1]
            elif min(a, b, c) == b:
                dtw[i1][i2] = d[i1][i2] + dtw[i1-1][i2]
            else:
                dtw[i1][i2] = d[i1][i2] + dtw[i1-1][i2-1]
    if report:
        # どのデータ点どうしが紐づいたか可視化
        plt.title('Dinamic Time Warping: {:.4f}'.format(dtw[-1][-1]))
        plt.subplot().set_aspect('equal', 'datalim')
        plt.plot(x1, y1, color='orange')
        plt.scatter(x1, y1, color='orange')
        plt.plot(x2, y2, color='blue')
        plt.scatter(x2, y2, color='blue')
        i1, i2 = T1-1, T2-1
        plt.plot([x1[i1], x2[i2]], [y1[i1], y2[i2]], lw=1.0, color='black')
        while 0 < i1 or 0 < i2:
            if i1 == 0:
                i2 -= 1
            elif i2 == 0:
                i1 -= 1
            else:
                a, b, c = dtw[i1][i2-1], dtw[i1-1][i2], dtw[i1-1][i2-1]
                if min(a, b, c) == a:
                    i2 -= 1
                elif min(a, b, c) == b:
                    i1 -= 1
                else:
                    i1 -= 1
                    i2 -= 1
            plt.plot([x1[i1], x2[i2]], [y1[i1], y2[i2]], lw=1.0, color='black')
        #plt.axes().set_aspect('equal')
        plt.grid()
        plt.show()
    return dtw[-1][-1]


# トイデータ作成
T1 = 30
T2 = 34
T3 = 30
x1 = np.array(range(T1)) * 0.3
y1 = np.sin(x1) + np.random.rand(T1)*0.2-0.1
x2 = np.array(range(T2)) * 0.27
y2 = 0.7 + np.sin(x2/1.05) + np.random.rand(T2)*0.2-0.1
x3 = np.array(range(T3)) * 0.3 + 1.0
y3 = np.sin(x1-np.pi/6) + np.random.rand(T1)*0.2-0.1
# DTW を計算
calc_dtw(x1, y1, x2, y2, True)
calc_dtw(x1, y1, x3, y3, True)
```

| $\mathrm{dtw}(y_1,y_2)$                                                                           | $\mathrm{dtw}(y_1,y_3)$                                                                           |
| :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| ![Figure_1](https://gist.github.com/user-attachments/assets/46f9df01-70d0-4b4e-aee1-cb8253a8f3a2) | ![Figure_2](https://gist.github.com/user-attachments/assets/00bdfb32-4f59-4171-ada4-94d089f6779c) |

# 実験：ユークリッド距離との比較

```python
def f_sin(t, f=1.0, th=0):
    return np.sin(f*t+th)
```

## 平行移動

```python
amp = 5
t = np.linspace(0, np.pi*6, 100)
y0 = f_sin(t)*amp
ths = np.linspace(0, np.pi*2, 100)
d_dtw = []
d_euc = []
for th in ths:
    y = f_sin(t, th=th)*amp
    d_dtw.append(calc_dtw(t, y0, t, y))
    d_euc.append(np.sqrt((y-y0)**2).sum())

plt.title(r'$y={}\sin(t+\theta)$'.format(amp))
plt.xlabel(r'$\theta$')
plt.plot(ths, d_dtw, label='DTW')
plt.plot(ths, d_euc, label='Euclidean')
plt.legend()
plt.grid()
plt.show()
```

![dtw-vs-euc-th](https://gist.github.com/user-attachments/assets/91854208-f85e-4ea2-8370-5ff7a9a7f6be)



## 振動数変化

```python
amp = 5
t = np.linspace(0, np.pi*6, 100)
y0 = f_sin(t)*amp
fs = np.linspace(0.5, 2, 100)
d_dtw = []
d_euc = []
for f in fs:
    y = f_sin(t, f=f)*amp
    d_dtw.append(calc_dtw(t, y0, t, y))
    d_euc.append(np.sqrt((y-y0)**2).sum())

plt.title(r'$y={}\sin(ft)$'.format(amp))
plt.xlabel(r'$f$')
plt.plot(fs, d_dtw, label='DTW')
plt.plot(fs, d_euc, label='Euclidean')
plt.legend()
plt.grid()
plt.show()
```

![dtw-vs-euc-freq](https://gist.github.com/user-attachments/assets/2aa5255f-377a-4db3-80c3-32abf88aef95)
