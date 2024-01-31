---
title: 三重積
title-en: triple product
---
# スカラー三重積

## 定義

3つの3次元ベクトル $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$ に関して、

$$
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
$$

で表される計算のこと。


## 性質

> 行列式での表現：
> 
> $$
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
=
\mathrm{det}
\begin{pmatrix}
    a_x & a_y & a_z \\
    b_x & b_y & b_z \\
    c_x & c_y & c_z
\end{pmatrix}
\tag{1.1}
$$

外積 $\boldsymbol{b} \times \boldsymbol{c}$ を計算すると

$$
\boldsymbol{b} \times \boldsymbol{c}
=
\mathrm{det}
\begin{pmatrix}
    \hat{x} & \hat{y} & \hat{z} \\
    b_x & b_y & b_z \\
    c_x & c_y & c_z
\end{pmatrix}
=
\begin{pmatrix}
    b_y c_z - b_z c_y \\
    b_z c_x - b_x c_z \\
    b_x c_y - b_y c_x
\end{pmatrix}
$$

であるから、

$$
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
=
(a_x, a_y, a_z)
\begin{pmatrix}
    b_y c_z - b_z c_y \\
    b_z c_x - b_x c_z \\
    b_x c_y - b_y c_x
\end{pmatrix}
=
a_x(b_y c_z - b_z c_y) +
a_y(b_z c_x - b_x c_z) +
a_z(b_x c_y - b_y c_x)
$$

また、

$$
\mathrm{det}
\begin{pmatrix}
    a_x & a_y & a_z \\
    b_x & b_y & b_z \\
    c_x & c_y & c_z
\end{pmatrix}
= a_x b_y c_z + a_y b_z c_x + a_z b_x c_y - a_x b_z c_y - a_y b_x c_z - a_z b_y c_x
$$

以上により、$(1.1)$ が成り立つ。


> 循環性：
> 
> $$
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
= \boldsymbol{b} \cdot (\boldsymbol{c} \times \boldsymbol{a})
= \boldsymbol{c} \cdot (\boldsymbol{a} \times \boldsymbol{b})
\tag{1.2}
$$

$(1.1)$ の証明で計算した $\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})$ の成分表示の式を $b_x,b_y,b_z$ でくくると、

$$
\begin{eqnarray}
    \boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
    &=&
    b_x(c_y a_z - c_z a_y) + b_y(c_z a_x - c_x a_z) + b_z(c_x a_y - c_y a_x)
    \\ &=&
    (b_x, b_y, b_z)
    \begin{pmatrix}
        c_y a_z - c_z a_y \\
        c_z a_x - c_x a_z \\
        c_x a_y - c_y a_x
    \end{pmatrix}
    \\ &=&
    \boldsymbol{b} \cdot (\boldsymbol{c} \times \boldsymbol{a})
\end{eqnarray}
$$

同様に $c_x,c_y,c_z$ でくくると、

$$
\begin{eqnarray}
    \boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
    &=&
    c_x(a_y b_z - a_z b_y) + c_y(a_z b_x - a_x b_z) + c_z(a_x b_y - a_y b_x)
    \\ &=&
    (c_x, c_y, c_z)
    \begin{pmatrix}
        a_y b_z - a_z b_y \\
        a_z b_x - a_x b_z \\
        a_x b_y - a_y b_x
    \end{pmatrix}
    \\ &=&
    \boldsymbol{c} \cdot (\boldsymbol{a} \times \boldsymbol{b})
\end{eqnarray}
$$

以上により、$(1.2)$ が成り立つ。


> スカラー三重積は、3つのベクトル $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$ を3辺とする平行六面体の体積 $V$ に一致する：
> 
> $$
V = \boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
\tag{1.3}
$$

まず、$\boldsymbol{b} \times \boldsymbol{c}$ の長さが $\boldsymbol{b}, \boldsymbol{c}$ を2辺とする平行四辺形の面積 $S$ と一致することを示す。

$$
\vert \boldsymbol{b} \times \boldsymbol{c} \vert
=
\sqrt{
    (b_y c_z - b_z c_y)^2 +
    (b_z c_x - b_x c_z)^2 +
    (b_x c_y - b_y c_x)^2
}
$$

$\boldsymbol{b}, \boldsymbol{c}$ の間の角を $\theta$ とすると、$\boldsymbol{b}, \boldsymbol{c}$ の内積は

$$
\boldsymbol{b} \cdot \boldsymbol{c} = \vert\boldsymbol{b}\vert \vert\boldsymbol{c}\vert \cos\theta
$$

であるから、

$$
\begin{eqnarray}
    S &=& \vert\boldsymbol{b}\vert \vert\boldsymbol{c}\vert \sin\theta
    \\ &=&
    \vert\boldsymbol{b}\vert \vert\boldsymbol{c}\vert
    \sqrt{1-\cos^2\theta}
    \\ &=&
    \vert\boldsymbol{b}\vert \vert\boldsymbol{c}\vert
    \sqrt{
        1 - \cfrac{
            (\boldsymbol{b} \cdot \boldsymbol{c})^2
        }{
            \vert\boldsymbol{b}\vert^2 \vert\boldsymbol{c}\vert^2
        }
    }
    \\ &=&
    \sqrt{
        \vert\boldsymbol{b}\vert^2 \vert\boldsymbol{c}\vert^2 -
        (\boldsymbol{b} \cdot \boldsymbol{c})^2
    }
    \\ &=&
    \sqrt{
        (b_x^2+b_y^2+b_z^2)(c_x^2+c_y^2+c_z^2) -
        (b_x c_x + b_y c_y + b_z c_z)^2
    }
    \\ &=&
    \sqrt{
        (b_x^2c_y^2+b_y^2c_x^2-2b_xb_yc_xc_y) +
        (b_y^2c_z^2+b_z^2c_y^2-2b_yb_zc_yc_z) +
        (b_z^2c_x^2+b_x^2c_z^2-2b_zb_xc_zc_x)
    }
    \\ &=&
    \sqrt{
        (b_xc_y-b_yc_x)^2 +
        (b_yc_z-b_zc_y)^2 +
        (b_zc_x-b_xc_z)^2
    }
    \\ &=&
    \vert \boldsymbol{b} \times \boldsymbol{c} \vert
\end{eqnarray}
$$

次に、$\boldsymbol{b}, \boldsymbol{c}$ で定まる平行四辺形を底面と見て、平行六面体の高さ $h$ を求める。

外積の性質から、ベクトル $\boldsymbol{b} \times \boldsymbol{c}$ は $\boldsymbol{b}, \boldsymbol{c}$ 両方に垂直。  
よって、$\boldsymbol{b} \times \boldsymbol{c}$ は平行六面体の高さ方向のベクトルである。

したがって、$\boldsymbol{a}$ と $\boldsymbol{b} \times \boldsymbol{c}$ がなす角を $\phi$ とすると、$h$ は $\boldsymbol{a}$ の高さ方向の成分であるから、

$$
h = \vert \boldsymbol{a} \vert \cos \phi
$$

$\boldsymbol{a}$ と $\boldsymbol{b} \times \boldsymbol{c}$ の内積を計算すると

$$
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
=
\vert \boldsymbol{a} \vert
\vert \boldsymbol{b} \times \boldsymbol{c} \vert
\cos \phi
$$

なので、

$$
h = \vert \boldsymbol{a} \vert \cos \phi
=
\cfrac{\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})}{\vert \boldsymbol{b} \times \boldsymbol{c} \vert}
$$

以上により、平行六面体の体積 $V$ は、

$$
V = Sh
=
\vert \boldsymbol{b} \times \boldsymbol{c} \vert
\cfrac{\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})}{\vert \boldsymbol{b} \times \boldsymbol{c} \vert}
=
\boldsymbol{a} \cdot (\boldsymbol{b} \times \boldsymbol{c})
$$

以上により、$(1.3)$ が成り立つ。


# ベクトル三重積

3つの3次元ベクトル $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$ に関して、

$$
\boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c})
$$

で表される計算のこと。


## 性質

> $$
\boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c})
=
(\boldsymbol{a} \cdot \boldsymbol{c}) \boldsymbol{b} - (\boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c}
\tag{2.1}
$$

$$
\begin{eqnarray}
    \boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c})
    &=&
    \mathrm{det}
    \begin{pmatrix}
        \hat{x} & \hat{y} & \hat{z} \\
        a_x & a_y & a_z \\
        (\boldsymbol{b} \times \boldsymbol{c})_x &
        (\boldsymbol{b} \times \boldsymbol{c})_y &
        (\boldsymbol{b} \times \boldsymbol{c})_z
    \end{pmatrix}
    \\ &=&
    \det
    \begin{pmatrix}
        \hat{x} & \hat{y} & \hat{z} \\
        a_x & a_y & a_z \\
        b_y c_z - b_z c_y &
        b_z c_x - b_x c_z &
        b_x c_y - b_y c_x
    \end{pmatrix}
    \\ &=&
    \begin{pmatrix}
        a_y(b_x c_y - b_y c_x) - a_z(b_z c_x - b_x c_z) \\
        a_z(b_y c_z - b_z c_y) - a_x(b_x c_y - b_y c_x) \\
        a_x(b_z c_x - b_x c_z) - a_y(b_y c_z - b_z c_y)
    \end{pmatrix}
    \\ &=&
    \begin{pmatrix}
        (a_y c_y + a_z c_z) b_x - (a_y b_y + a_z b_z) c_x \\
        (a_x c_x + a_z c_z) b_y - (a_x b_x + a_z b_z) c_y \\
        (a_x c_x + a_y c_y) b_z - (a_x b_x + a_y b_y) c_z
    \end{pmatrix}
    \\ &=&
    \begin{pmatrix}
        (a_x c_x + a_y c_y + a_z c_z) b_x - (a_x b_x + a_y b_y + a_z b_z) c_x \\
        (a_x c_x + a_y c_y + a_z c_z) b_y - (a_x b_x + a_y b_y + a_z b_z) c_y \\
        (a_x c_x + a_y c_y + a_z c_z) b_z - (a_x b_x + a_y b_y + a_z b_z) c_z
    \end{pmatrix}
    \\ &=&
    \begin{pmatrix}
        (\boldsymbol{a} \cdot \boldsymbol{c}) b_x - (\boldsymbol{a} \cdot \boldsymbol{b}) c_x \\
        (\boldsymbol{a} \cdot \boldsymbol{c}) b_y - (\boldsymbol{a} \cdot \boldsymbol{b}) c_y \\
        (\boldsymbol{a} \cdot \boldsymbol{c}) b_z - (\boldsymbol{a} \cdot \boldsymbol{b}) c_z
    \end{pmatrix}
    =
    (\boldsymbol{a} \cdot \boldsymbol{c}) \boldsymbol{b} - (\boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c}
\end{eqnarray}
$$


> $$
\boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c}) +
\boldsymbol{b} \times (\boldsymbol{c} \times \boldsymbol{a}) +
\boldsymbol{c} \times (\boldsymbol{a} \times \boldsymbol{b})
=
\boldsymbol{0}
\tag{2.2}
$$

$(2.1)$ より

$$
\begin{eqnarray}
    \boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c}) +
    \boldsymbol{b} \times (\boldsymbol{c} \times \boldsymbol{a}) +
    \boldsymbol{c} \times (\boldsymbol{a} \times \boldsymbol{b})
    &=&
    \{(\boldsymbol{a} \cdot \boldsymbol{c}) \boldsymbol{b} -
    (\boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c}\} +
    \{(\boldsymbol{b} \cdot \boldsymbol{a}) \boldsymbol{c} -
    (\boldsymbol{b} \cdot \boldsymbol{c}) \boldsymbol{a}\} +
    \{(\boldsymbol{c} \cdot \boldsymbol{b}) \boldsymbol{a} -
    (\boldsymbol{c} \cdot \boldsymbol{a}) \boldsymbol{b}\}
    \\ &=&
    (\boldsymbol{c} \cdot \boldsymbol{b} - \boldsymbol{b} \cdot \boldsymbol{c}) \boldsymbol{a} +
    (\boldsymbol{a} \cdot \boldsymbol{c} - \boldsymbol{c} \cdot \boldsymbol{a}) \boldsymbol{b} +
    (\boldsymbol{b} \cdot \boldsymbol{a} - \boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c}
    \\ &=&
    \boldsymbol{0}
\end{eqnarray}
$$

最後の計算では、内積の交換可能性（$\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{b} \cdot \boldsymbol{a}$）を用いた。