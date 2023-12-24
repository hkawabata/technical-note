---
title: オイラー法
title-en: Euler method
---
# 概要

常微分方程式

$$
\cfrac{dx(t)}{dt} = f(x, t)
$$

を解く手法の一つ。

# （前進）オイラー法

## 手順

- 刻み幅 $\Delta t$
- 初期値 $x(t_0) = x_0$

として、漸化式

$$
\begin{eqnarray}
    x(t_{n+1}) &=& x(t_n) + f(x_n, t_n) \Delta t \\ \\
    t_{n+1} &=& t_n + \Delta t
\end{eqnarray}
$$

により更新していく。

## 誤差

初期値 $x(t_0)$ から漸化式により数値的に求めた解 $x(t_n)$ は、

$$
\begin{eqnarray}
    x(t_n) &=& x(t_{n-1}) + f(x(t_{n-1}), t_{n-1}) \Delta t
    \\ &=&
    x(t_{n-2}) + f(x(t_{n-2}), t_{n-2}) \Delta t + f(x(t_{n-1}), t_{n-1}) \Delta t
    \\ &=&
    \cdots
    \\ &=&
    x(t_0) + \sum_{i=0}^{n-1} f(x(t_i), t_i) \Delta t
\end{eqnarray}
$$

また、解析的に求めた解 $x(t_n)$ は、

$$
\begin{eqnarray}
    x(t_n) &=& x(t_0) + \int_{t_0}^{t_n} \cfrac{dx(t)}{dt} dt
    \\ &=&
    x(t_0) + \int_{t_0}^{t_n} f(x(t), t) dt
\end{eqnarray}
$$

よって数値解と解析解の誤差は、

$$
x_\mathrm{error}(t_n) = \sum_{i=0}^{n-1} f(x(t_i), t_i) \Delta t - \int_{t_0}^{t_n} f(x(t), t) dt
$$

$\Delta t \to 0$ の極限を取れば、右辺第一項は和の極限による定積分の定義そのものであり、

$$
\lim_{\Delta t \to 0} \sum_{i=0}^{n-1} f(x(t_i), t_i) \Delta t
= \int_{t_0}^{t_n} f(x(t), t) dt
$$

したがって、

$$
\lim_{\Delta t \to 0} x_\mathrm{error}(t_n) = 0
$$

すなわち、$\Delta t$ を小さく取れば取るほど解析解と数値解の誤差は小さくなる。


## 具体例

### 例1

> $$
\cfrac{dx(t)}{dt} = 2t-1,\qquad x(0) = 0
$$

#### 解析解

微分方程式を解くと、積分定数を $C$ として

$$
x(t) = t^2-t + C
$$

初期値 $x(0) = 0$ より $C=0$ となるので、

$$
x(t) = t^2-t
$$

#### 数値解

漸化式は

$$
x(t_{n+1}) = x(t_n) + (2t_n-1) \Delta t
$$

{% gist 851d8195db96ecd26da5cbd7b2e99572 20231220_euler-method.py %}

```python
def x_poly(t):
    return t**2 - t

def dxdt_poly(t, x):
    return 2*t-1

x0 = 0
t1, t2 = 0, 1.0
draw_euler_result(x_poly, dxdt_poly, x0, t1, t2)
```

![euler-method](https://gist.github.com/assets/13412823/f07cb28a-52f7-43e3-8eca-14725e7f444f)

![euler-method-error](https://gist.github.com/assets/13412823/6daa7fe6-29a9-4811-a93d-9c5b8fbc400b)


### 例2

> $$
\cfrac{dx(t)}{dt} = 3t^2-6t+2,\qquad x(0) = -1
$$

#### 解析解

微分方程式を解くと、積分定数を $C$ として

$$
x(t) = t^3 - 3t^2 + 2t + C
$$

初期値 $x(0) = -1$ より $C=-1$ となるので、

$$
x(t) = t^3 - 3t^2 + 2t - 1
$$

#### 数値解

漸化式は

$$
x(t_{n+1}) = x(t_n) + (3t_n^2 - 6t_n + 2) \Delta t
$$

```python
def x_poly2(t):
    return t**3 - 3*t**2 + 2*t - 1

def dxdt_poly2(t, x):
    return 3*t**2 - 6*t + 2

x0 = - 1
t1, t2 = 0, 2.5
draw_euler_result(x_poly2, dxdt_poly2, x0, t1, t2)
```

![euler-method_3](https://gist.github.com/assets/13412823/8985cada-3e82-40e0-a679-0c7d474f5ee0)

![euler-method-error_3](https://gist.github.com/assets/13412823/bbb8a35b-3c3c-4552-a1a5-31b04e287e8a)



### 例3

> $$
\cfrac{dx(t)}{dt} = \sin t,\qquad x(0) = 0
$$

#### 解析解

微分方程式を解くと、積分定数を $C$ として

$$
x(t) = - \cos t + C
$$

初期値 $x(0) = 0$ より $C=1$ となるので、

$$
x(t) = - \cos t + 1
$$

#### 数値解

漸化式は

$$
x(t_{n+1}) = x(t_n) + \cos t_n \cdot \Delta t
$$

```python
def x_trig(t):
    return - np.cos(t) + 1

def dxdt_trig(t, x):
    return np.sin(t)

x0 = 0
t1, t2 = 0, np.pi*10
draw_euler_result(x_trig, dxdt_trig, x0, t1, t2)
```

![euler-method_2](https://gist.github.com/assets/13412823/a4ee02ae-d156-4b7f-b37b-b3e8ebde8629)

![euler-method-error_2](https://gist.github.com/assets/13412823/d7b9b458-8281-41d3-acbd-a73ff1a58d06)

