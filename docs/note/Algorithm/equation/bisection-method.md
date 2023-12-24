---
title: 二分法
title-en: bisection method
---
# 概要

方程式を解く数値的手法の1つ。  
変数が1つの方程式に使える。

# 基本的な考え方

連続関数 $f(x)$ に関して

$$
f(x_1)f(x_2) \lt 0
\qquad (x_1 \lt x_2)
$$

となる $x_1, x_2$ があれば、方程式 $f(x)=0$ の解は $x_1 \lt x \lt x_2$ の範囲に少なくとも1つ存在する。  
$x_1, x_2$ を両端とする区間を、二分探索で小さく狭めていくことで解を求める。

![bisection-method](https://gist.github.com/assets/13412823/60baafe3-3d61-442f-81b1-d58888325db6)

```python
from matplotlib import pyplot as plt

x1, x2, x3 = -1.234, 0.345, 2.345
def f(x):
    return (x-x1) * (x-x2) * (x-x3)

x = np.arange(-2, 3, 0.01)
y = f(x)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(x, y, label=r'$y=f(x)$')
plt.plot(x, np.full(x.size, 0), color='black')
plt.scatter([x1, x2, x3], [0,0,0], color='red', label=r'$f(x)=0$')
plt.text(x1-0.8, 0.5, r'$f(x) < 0$')
plt.text(x2-1.1, 0.5, r'$f(x) > 0$')
plt.text(x3-1.3, 0.5, r'$f(x) < 0$')
plt.text(x3+0.3, 0.5, r'$f(x) > 0$')
plt.plot([-0.1, -0.1], [0, f(-0.1)], color='orange', lw=2, linestyle='dotted')
plt.scatter(-0.1, f(-0.1), color='orange')
plt.text(-0.1, -0.5, r'$x_1$')
plt.plot([1.2, 1.2], [0, f(1.2)], color='orange', lw=2, linestyle='dotted')
plt.scatter(1.2, f(1.2), color='orange')
plt.text(1.2, -0.5, r'$x_2$')
plt.legend()
plt.grid()
plt.show()
```

# 手順

> **【問題設定】**
> 
> 以下の方程式の解を求める。
> 
> $$
f(x) = 0
$$

計算手順

1. 収束条件を決める：$\vert f(x) \vert \lt \varepsilon$ 
2. $f(x_1)$ と $f(x_2)$ が異符号、すなわち $f(x_1)f(x_2) \lt 0$ となるような $x_1, x_2$ を1組見つける
3. 平均値 $x_3 = (x_1+x_2)/2$ を計算
4. $\vert f(x_3) \vert \lt \varepsilon$ なら計算終了
5. $f(x_1), f(x_2)$ のうち $f(x_3)$ と異符号である方の引数 $x_i (i=1,2)$ を $x_3$ に置き換える：$x_i \gets x_3$
6. 3に戻る


# 実装

```python
import numpy as np

def bisection(f, x1, x2, eps=1e-8):
    """
    f(x1)f(x2) < 0 のとき x1, x2 の間に存在する f(x)=0 の解を1つ求める
    """
    f_x1, f_x2 = f(x1), f(x2)
    if f_x1 * f_x2 >= 0:
        raise Exception('f(x1)*f(x2) must be < 0')
    while True:
        x3 = (x1+x2)/2.0
        f_x3 = f(x3)
        if np.abs(f_x3) < eps:
            return x3
        elif f_x1 * f_x3 < 0:
            x2 = x3
            f_x2 = f_x3
        else:
            x1 = x3
            f_x1 = f_x3

def bisection_all(f, x_min, x_max, dx=0.1):
    """
    指定した区間の f(x)=0 の解を全て求める
    """
    res = []
    for x1 in np.arange(x_min, x_max, dx):
        x2 = x1 + dx
        if f(x1) * f(x2) < 0:
            res.append(bisection(f, x1, x2))
        if f(x1) == 0:
            res.append(x1)
        if f(x2) == 0:
            res.append(x2)
    return res

def f1(x):
    return (x-2.345)*(x-1.234)*(x+3.21)

def f2(x):
    return np.sin(x*2)

bisection_all(f1, -10, 10)
```

```python
>>> bisection_all(f1, -5, 5)
[-3.2100000001490194, 1.234000000357606, 2.34499999880788]

>>> bisection_all(f2, -5, 5)
[-4.712388980388643, -3.1415926575660773, -1.570796322822583, 2.9802144752011374e-09, 1.5707963228225479, 3.141592657566042, 4.712388980388607]
```