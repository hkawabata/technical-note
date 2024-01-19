---
title: ストークスの定理
title-en: Stokes’ theorem
---
# 定理

3次元空間において
- $\boldsymbol{v}(\boldsymbol{x})$：滑らかなベクトル関数
- $C$：空間内の閉曲線
- $S$：閉曲線 $C$ を境界とする任意の曲面
- $\boldsymbol{n}(\boldsymbol{x})$：曲面 $S$ 上の点 $\boldsymbol{x}$ における法線ベクトル（$\vert \boldsymbol{n} \vert = 1$）

を考える。

![stokes-1](https://gist.github.com/assets/13412823/20d2d870-1224-4f2a-a06f-bd4c7879ff99)

このとき、以下の2つは等しい。
- $\boldsymbol{v}(\boldsymbol{x})$ の回転 $\nabla \times \boldsymbol{v}$ と $S$ の法線ベクトル $\boldsymbol{n}(\boldsymbol{x})$ の内積 $(\nabla \times \boldsymbol{v}) \cdot \boldsymbol{n}$ を $S$ 全体で面積分した値
- $\boldsymbol{v}(\boldsymbol{x})$ の $S$ の境界線 $C$ に沿って1周線積分した値

すなわち、

$$
\int_S (\nabla \times \boldsymbol{v}) \cdot \boldsymbol{n} dS
=
\oint_C \boldsymbol{v} \cdot d\boldsymbol{l}
\tag{1}
$$

※ $\nabla$ 演算子やベクトル場の回転については[ナブラ演算子](nabla.md)を参照


# 雑な証明

ベクトル場の回転は、その点におけるベクトル場のトルクを表す（cf. [ナブラ演算子](nabla.md)）。

下図のように、曲面 $S$ を1辺 $\Delta$ の微小な正方形の集合に分割する。

![stokes-2](https://gist.github.com/assets/13412823/fbaed217-df81-4359-b454-14833fdffd32)

点 $\boldsymbol{x}=(x,y,z)$ を中心とする正方形の4辺に沿った $\boldsymbol{v}$ の線積分 $\Delta s(\boldsymbol{x})$ を考える。  
$S$ 内で $\Delta s$ 全ての和を取ると、ほとんどの辺の線積分は、隣接する正方形の辺の線積分と打ち消し合う（上図の赤矢印）。  
打ち消されないのは閉曲線 $C$ と接する辺のみ（上図のオレンジ矢印）であるから、残るのは $C$ に沿った線積分：

$$
\sum_{\boldsymbol{x} \in S} \Delta s(\boldsymbol{x}) = \oint_C \boldsymbol{v}\cdot d\boldsymbol{l}
\tag{2}
$$

次に、実際に $\Delta s(\boldsymbol{x})$ を計算してみる。  
厳密な計算は大変なので、簡単のため、曲面 $S$ が $xy$ 平面に平行な場合を考える。  
このとき、注目する正方形は
- 重心：$\boldsymbol{x}=(x,y,z)$
- 頂点：$(x+\Delta/2,y,z),(x-\Delta/2,y,z),(x,y+\Delta/2,z),(x,y-\Delta/2,z)$

よって

$$
\begin{eqnarray}
    \Delta s(\boldsymbol{x})
    &=&
    \int_{x-\Delta/2}^{x+\Delta/2} v_x(x,y-\Delta/2,z) dx +
    \int_{y-\Delta/2}^{y+\Delta/2} v_y(x+\Delta/2,y,z) dy +
    \\ &&
    \int_{x+\Delta/2}^{x-\Delta/2} v_x(x,y+\Delta/2,z) dx +
    \int_{y+\Delta/2}^{y-\Delta/2} v_y(x-\Delta/2,y,z) dy
    \\ &=&
    v_x(x,y-\Delta/2,z) \int_{x-\Delta/2}^{x+\Delta/2} dx +
    v_y(x+\Delta/2,y,z) \int_{y-\Delta/2}^{y+\Delta/2} dy +
    \\ &&
    v_x(x,y+\Delta/2,z) \int_{x+\Delta/2}^{x-\Delta/2} dx +
    v_y(x-\Delta/2,y,z) \int_{y+\Delta/2}^{y-\Delta/2} dy
    \\ &=&
    \left\{
        v_x(x,y-\Delta/2,z) + v_y(x+\Delta/2,y,z) -
        v_x(x,y+\Delta/2,z) - v_y(x-\Delta/2,y,z)
    \right\} \Delta
\end{eqnarray}
$$

途中、正方形が十分小さいことから $v_x,v_y$ は一定と見なして積分の外に出した。

テイラー展開により

$$
\begin{cases}
    v_x(x,y-\Delta/2,z) &\simeq& v_x(x,y,z) - \cfrac{\partial v_x}{\partial y} \cfrac{\Delta}{2}
    \\
    v_y(x,y+\Delta/2,z) &\simeq& v_y(x,y,z) + \cfrac{\partial v_y}{\partial x} \cfrac{\Delta}{2}
    \\
    v_x(x,y+\Delta/2,z) &\simeq& v_x(x,y,z) + \cfrac{\partial v_x}{\partial y} \cfrac{\Delta}{2}
    \\
    v_y(x,y-\Delta/2,z) &\simeq& v_y(x,y,z) - \cfrac{\partial v_y}{\partial x} \cfrac{\Delta}{2}
\end{cases}
$$

なので、

$$
\begin{eqnarray}
    \Delta s(\boldsymbol{x})
    &=&
    \left\{
        - \cfrac{\partial v_x}{\partial y} \cfrac{\Delta}{2} +
        \cfrac{\partial v_y}{\partial x} \cfrac{\Delta}{2} -
        \cfrac{\partial v_x}{\partial y} \cfrac{\Delta}{2} -
        \left( - \cfrac{\partial v_y}{\partial x} \cfrac{\Delta}{2} \right)
    \right\} \Delta
    \\ &=&
    \left(
        \cfrac{\partial v_y}{\partial x} - \cfrac{\partial v_x}{\partial y}
    \right) \Delta^2
    \\ &=&
    (\nabla \times \boldsymbol{v})_z \Delta^2
\end{eqnarray}
$$

曲面 $S$ 全体で和を取れば、

$$
\sum_{\boldsymbol{x} \in S} \Delta s(\boldsymbol{x})
=
\sum_{\boldsymbol{x} \in S} (\nabla \times \boldsymbol{v})_z \Delta^2
\simeq
\int_S (\nabla \times \boldsymbol{v})_z dS
$$

最後の変形では、正方形の面積 $\Delta^2 \to dS$ として和を積分に書き換えた。

ここでは $xy$ 平面に並行な曲面 $S$ を想定しているので、$S$ 上の任意の点で $\boldsymbol{n} = (0,0,1)$。
したがって、

$$
\sum_{\boldsymbol{x} \in S} \Delta s(\boldsymbol{x})
\simeq
\int_S (\nabla \times \boldsymbol{v})_z dS
=
\int_S (\nabla \times \boldsymbol{v}) \cdot \boldsymbol{n} dS
\tag{3}
$$

$(2)(3)$ より、

$$
\int_S (\nabla \times \boldsymbol{v}) \cdot \boldsymbol{n} dS
=
\oint_C \boldsymbol{v}\cdot d\boldsymbol{l}
$$

