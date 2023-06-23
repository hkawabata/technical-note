---
title: ニュートン法
title-en: Newton's method
---

# 概要

方程式を解く数値的手法の1つ。

適用するためには、解きたい方程式を

$$
f(x_1, \cdots, x_n) = 0
$$

で表した時、解の近傍で $f$ が微分可能である必要がある。

# 理論

## 1変数の場合

> **【問題設定】**
> 
> 以下の方程式の解を求める。
> 
> $$
f(x) = 0
$$

計算手順は次の通り。

1. 適当な方法で真の解の近傍の点 $x^{(0)}$ を求め、初期値とする
2. $x=x^{(0)}$ における $y = f(x)$ の接線 $l^{(0)}$ を求める
3. $l^{(0)}$ と $x$ 軸との交点を $x^{(1)}$ とする
4. $x=x^{(1)}$ における $y = f(x)$ の接線 $l^{(1)}$ を求める
5. 3,4と同様の手順を、$x^{(k)}$ と $x^{(k-1)}$ の差が収束判定値 $\varepsilon$ より小さくなるまで繰り返し、最後の $x^{(k)}$ を解とする

曲線 $y = f(x)$ の $x=x^{(i)}$ における接線 $l^{(i)}$ の方程式は

$$
y - f(x^{(i)}) = f'(x^{(i)}) (x-x^{(i)})
\tag{1}
$$

$l^{(i)}$ と $x$ 軸の交点 $x^{(i+1)}$ は、$l^{(i)}$ の方程式に $y=0$ を代入すれば求まり、

$$
x^{(i+1)} = x^{(i)} - \cfrac{f(x^{(i)})}{f'(x^{(i)})}
\tag{2}
$$

実際の計算手順としては、この漸化式により $x^{(i+1)}$ を計算して、$x^{(i)}$ との差が収束するか調べる操作を繰り返していく。


## 2変数の場合

> **【問題設定】**
> 
> 以下の方程式の解を求める。
> 
> $$
\begin{eqnarray}
	f(x,y) &=& 0 \\
	g(x,y) &=& 0
\end{eqnarray}
$$

1変数の場合、

- 曲線 $y = f(x)$ の $x=x^{(i)}$ における接線
- $x$ 軸 ($y=0$)

の2直線の交点を求め、それを次ステップの $x^{(i+1)}$ とした。

2変数の場合も考え方は同じで、

- 曲面 $z = f(x,y)$ の $(x,y)=(x^{(i)},y^{(i)})$ における接平面 
- 曲面 $z = g(x,y)$ の $(x,y)=(x^{(i)},y^{(i)})$ における接平面 
- $xy$ 平面 ($z=0$)

の3平面の交点を求め、それを次ステップの $(x^{(i+1)}, y^{(i+1)})$ として用いる。

曲面 $z = f(x,y)$ の $(x^{(i)}, y^{(i)})$ における接平面の方程式は、

$$
z - f^{(i)}
=
f_x^{(i)} (x-x^{(i)}) +
f_y^{(i)} (y-y^{(i)})
\tag{3}
$$

ただし、

$$
f^{(i)} = f(x^{(i)}, y^{(i)}), \quad
f_x^{(i)} = \cfrac{\partial f}{\partial x}
(x^{(i)}, y^{(i)}, f^{(i)}), \quad
f_y^{(i)} = \cfrac{\partial f}{\partial y}
(x^{(i)}, y^{(i)}, f^{(i)})
$$

この平面と $xy$ 平面の交線の方程式は $z=0$ とおけば求まり、

$$
- f^{(i)}
=
f_x^{(i)} (x-x^{(i)}) +
f_y^{(i)} (y-y^{(i)})
\tag{4}
$$

同様に議論して、曲面 $z = g(x,y)$ の接平面と $xy$ 平面の交線の方程式は、

$$
- g^{(i)}
=
g_x^{(i)} (x-x^{(i)}) +
g_y^{(i)} (y-y^{(i)})
\tag{5}
$$

以上の2式を整理すると、

$$
\begin{cases}
	f_x^{(i)} x +
	f_y^{(i)} y
	=
	f_x^{(i)} x^{(i)} +
	f_y^{(i)} y^{(i)} -
	f^{(i)}
	\\ \\
	g_x^{(i)} x +
	g_y^{(i)} y
	=
	g_x^{(i)} x^{(i)} +
	g_y^{(i)} y^{(i)} -
	g^{(i)}
\end{cases}
\tag{6}
$$

行列形式で書けば、

$$
\begin{eqnarray}
	& J^{(i)}
	\begin{pmatrix}
		x \\ y
	\end{pmatrix}
	=
	J^{(i)}
	\begin{pmatrix}
		x^{(i)} \\ y^{(i)}
	\end{pmatrix}
	-
	\begin{pmatrix}
		f^{(i)} \\ g^{(i)}
	\end{pmatrix}
	\\ \\
	\Longrightarrow \quad &
	\begin{pmatrix}
		x \\ y
	\end{pmatrix}
	=
	\begin{pmatrix}
		x^{(i)} \\ y^{(i)}
	\end{pmatrix}
	-
	\left(J^{(i)}\right)^{-1}
	\begin{pmatrix}
		f^{(i)} \\ g^{(i)}
	\end{pmatrix}
	\tag{7}
\end{eqnarray}
$$

ただし、$J^{(i)}$ はヤコビ行列：

$$
J^{(i)} = \begin{pmatrix}
f_x^{(i)} & f_y^{(i)} \\
g_x^{(i)} & g_y^{(i)}
\end{pmatrix}
$$

この方程式の解が次ステップの $(x^{(i+1)}, y^{(i+1)})$ となる。

この漸化式を用いて、2つのベクトル

$$
\begin{eqnarray}
	\boldsymbol{x}^{(k)} &=& (x^{(k)}, y^{(k)})
	\\ \\
	\boldsymbol{x}^{(k-1)} &=& (x^{(k-1)}, y^{(k-1)})
\end{eqnarray}
$$

の差の絶対値が収束判定値 $\varepsilon$ より小さくなる、すなわち

$$
| \boldsymbol{x}^{(k)} - \boldsymbol{x}^{(k-1)} |
= \sqrt{
	\left(x^{(k)}-x^{(k-1)}\right)^2 +
	\left(y^{(k)}-y^{(k-1)}\right)^2
}
\lt \varepsilon
$$

となるまで順に $x^{(i)}, y^{(i)}$ を計算していき、最後の $(x^{(k)}, y^{(k)})$ を解とすれば良い。


> **【NOTE】**
> 
> 実用上は、$(7)$ にように逆行列を用いて計算するのではなく、$(6)$ にガウスの消去法を使うなど、低コストで連立方程式を解くことが多い。


## 多変数の場合


> **【問題設定】**
> 
> $n$ 個の変数 $x_1, \cdots, x_n$ に関する $n$ 個の連立方程式の解を求める。
> 
> $$
\begin{eqnarray}
	f_1(x_1, \cdots, x_n) &=& 0 \\
	f_2(x_1, \cdots, x_n) &=& 0 \\
	\vdots \\
	f_n(x_1, \cdots, x_n) &=& 0
\end{eqnarray}
$$

2変数の場合と同様、

- $(n+1)$ 次元空間の超曲面 $z = f_1(x_1, \cdots, x_n)$ に $(x_1, \cdots, x_n, z)=(x_1^{(i)}, \cdots, x_n^{(i)}, f_1^{(i)})$ で接する超平面
- $(n+1)$ 次元空間の超曲面 $z = f_2(x_1, \cdots, x_n)$ に $(x_1, \cdots, x_n, z)=(x_1^{(i)}, \cdots, x_n^{(i)}, f_2^{(i)})$ で接する超平面
- $\cdots$
- $(n+1)$ 次元空間の超曲面 $z = f_n(x_1, \cdots, x_n)$ に $(x_1, \cdots, x_n, z)=(x_1^{(i)}, \cdots, x_n^{(i)}, f_n^{(i)})$ で接する超平面
- $x_1 x_2 \cdots x_n$ 超平面 ($z=0$)

の $(n+1)$ 個の平面の交点を次ステップの $(x_1^{(i+1)}, \cdots, x_n^{(i+1)})$ として用いれば良い。

この交点を求めるための方程式は、2変数の場合と同様に計算すれば得られる：

$$
J^{(i)}
	\begin{pmatrix}
		x_1 \\ \vdots \\ x_n
	\end{pmatrix}
	=
	J^{(i)}
	\begin{pmatrix}
		x_1^{(i)} \\ \vdots \\ x_n^{(i)}
	\end{pmatrix}
	-
	\begin{pmatrix}
		f_1^{(i)} \\ \vdots \\ f_n^{(i)}
\end{pmatrix}
\tag{8}
$$

ただし、

$$
J^{(i)} = \begin{pmatrix}
	\cfrac{\partial f_1}{\partial x_1}(x_1^{(i)},\cdots,x_n^{(i)}) & \cdots & \cfrac{\partial f_1}{\partial x_n}(x_1^{(i)},\cdots,x_n^{(i)}) \\
	\vdots & \ddots & \vdots \\
	\cfrac{\partial f_n}{\partial x_1}(x_1^{(i)},\cdots,x_n^{(i)}) & \cdots & \cfrac{\partial f_n}{\partial x_n}(x_1^{(i)},\cdots,x_n^{(i)})
\end{pmatrix}
$$

計算の収束判定についても2変数と同様、ベクトルの差の絶対値を用いれば良い。


# 実装

## 1変数

方程式

$$
f(x) := (x+2) (x+1)^2 (x-3) = 0
$$

をニュートン法で解いてみる。解析解は

$$
x = -2, -1, 3
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/248159694-2948dd60-619e-4b46-a2b2-3b91e7a7bbdb.png)


{% gist a6d18ea3cd6461f49078be9398a1ff31 20230623_newton-method-1.py %}


## 2変数

方程式

$$
\begin{cases}
	f(x,y) := x^2 + 4y^2 - 4 = 0
	\\ \\
	g(x,y) := x^2 - y - \cfrac{5}{2} = 0
\end{cases}
$$

を2変数のニュートン法で解いてみる。

解析解は

$$
\begin{eqnarray}
	(x,y) &=&
	\left( \pm \cfrac{\sqrt{7}}{2}, -\cfrac{3}{4} \right),\ 
	\left( \pm \sqrt{3}, \cfrac{1}{2} \right)
	\\ \\ &\simeq&
	(\pm 1.32287566, -0.75),\quad (\pm 1.73205081, 0.5)
\end{eqnarray}
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/248220432-edc32f72-dc16-4030-b73d-f87bf42244fc.png)


{% gist a6d18ea3cd6461f49078be9398a1ff31 20230623_newton-method-2.py %}
