---
title: 複素解析の基礎
---
# 用語の定義

## 実部・虚部

複素数

$$
z = x+iy\qquad(x, y \in \mathbb{R})
$$

に関して $x,y$ をそれぞれ **実部、虚部** といい、

$$
\begin{eqnarray}
    x &=& \mathrm{Re}\ z
    \\
    y &=& \mathrm{Im}\ z
\end{eqnarray}
$$

とも書く。

## 共役複素数

虚部の符号だけが異なる2つの複素数

$$
\begin{eqnarray}
    z = x + iy
    \\
    \bar{z} = x - iy
\end{eqnarray}
$$

を互いに **共役である** といい、$z$ を $\bar{z}$ の、$\bar{z}$ を $z$ の **共役複素数** という。

## 絶対値

複素数の絶対値 $\vert z \vert$ は以下のように計算され、0以上の実数値になる。

$$
\vert z \vert^2 = z \bar{z} = (x + iy)(x - iy) = x^2 + y^2
$$

## 複素平面

複素数 $z = x + iy$ の実部 $x$ を横軸、虚部 $y$ を縦軸にとって平面座標上で表したものを **複素平面** という。図の $\theta$ は $-1+2i$ の偏角（後述）。

![complex-plane](https://user-images.githubusercontent.com/13412823/284117156-ee5ec573-8a2a-469c-9e0c-6fee528a7566.png)

```python
plt.xlabel('Re')
plt.ylabel('Im')
plt.scatter(0,0,color='black')
plt.plot([0,-1], [0,2], color='black', lw=2)
plt.plot([0,2], [0,0], color='black', lw=2)
for x, y in [(-1, 2), (2,1), (4,0), (0,3), (-2, -2)]:
    plt.scatter(x,y,label='${}+{}i$'.format(x,y))

plt.text(0, 0.1, r'$\theta$', size=20)
plt.legend()
plt.grid()
plt.show()
```


## 複素数の極形式

複素数 $z$ を複素平面上にプロットした時、ベクトル $\vec{z} = (x, y)$ が横軸となす角 $\theta$ （横軸から左回りを正として定義）を **偏角** といい、$\theta = \mathrm{arg}\,z$ とも書く。

たとえば $z = -1+2i$ に関して

$$
\begin{eqnarray}
    \sin \theta &=& \cfrac{2}{\sqrt{(-1)^2+2^2}} = \cfrac{2}{\sqrt{5}}
    \\
    \cos \theta &=& \cfrac{-1}{\sqrt{(-1)^2+2^2}} = -\cfrac{1}{\sqrt{5}}
\end{eqnarray}
$$

この偏角 $\theta$ と絶対値 $r := \vert z \vert$ を用いて、$z$ を

$$
z = r (\cos \theta + i \sin \theta) = re^{i\theta}
$$

と表すことができる。これを **極形式** という。  
ここで、最後の変形では **オイラーの公式**

$$
e^{i\theta} = \cos \theta + i \sin \theta
$$

を用いた。