---
title: ガウスの発散定理
title-en: divergence theorem
---
# 定理

$n$ 次元空間において
- $\boldsymbol{v}(\boldsymbol{x})$：滑らかなベクトル関数
- $S$：滑らかな閉曲面
- $V$：閉曲面 $S$ 内部の閉空間
- $\boldsymbol{n}(\boldsymbol{x})$：閉曲面 $S$ 上の点 $\boldsymbol{x}$ において、$S$ の外側に向かう向きの法線ベクトル（$\vert \boldsymbol{n} \vert = 1$）

を考える。

![divergence-1](https://gist.github.com/assets/13412823/e6c7e951-2227-4f32-8a81-0516f4d6fdde)


このとき、以下の2つは等しい。
- $\boldsymbol{v}(\boldsymbol{x})$ の発散 $\nabla \cdot \boldsymbol{v}(\boldsymbol{x})$ を $V$ 全体で空間積分した値
- $\boldsymbol{v}(\boldsymbol{x})$ と $S$ の法線ベクトル $\boldsymbol{n}(\boldsymbol{x})$ の内積 $\boldsymbol{v}(\boldsymbol{x}) \cdot \boldsymbol{n}(\boldsymbol{x})$ を $S$ 全体で面積分した値

すなわち、

$$
\int_V \nabla \cdot \boldsymbol{v}(\boldsymbol{x}) dV
=
\int_S \boldsymbol{v}(\boldsymbol{x}) \cdot \boldsymbol{n}(\boldsymbol{x}) dS
\tag{1}
$$

※ $\nabla$ 演算子やベクトル場の発散については[ナブラ演算子](nabla.md)を参照

「**閉空間内の発散（= 流出・湧き出し）を全て足し合わせると、その表面から出ていく値の合計に等しくなる**」と言い換えることもできる。


# 雑な証明

ベクトル場の発散は、その点における流出・湧き出し（流入・吸い込み）を表す（cf. [ナブラ演算子](nabla.md)）。

簡単のため2次元空間で考えて、下図のように閉空間 $V$ を微小間隔 $\Delta$ の格子状に分割する。

![divergence-2](https://gist.github.com/assets/13412823/26bf46e0-7cbf-4784-af57-50cd04e2b510)

格子点 $\boldsymbol{x}=(x,y)$ における発散 $\nabla \cdot \boldsymbol{v}(\boldsymbol{x})$ は、以下の4つの和と考えることができる。
- 点 $(x,y)$ から右側の格子点 $(x+\Delta,y)$ への流出量 $d_\mathrm{right}(x,y)$
- 点 $(x,y)$ から左側の格子点 $(x-\Delta,y)$ への流出量 $d_\mathrm{left}(x,y)$
- 点 $(x,y)$ から上側の格子点 $(x,y+\Delta)$ への流出量 $d_\mathrm{upper}(x,y)$
- 点 $(x,y)$ から下側の格子点 $(x,y-\Delta)$ への流出量 $d_\mathrm{lower}(x,y)$

したがって、発散の体積積分は以下のように書き換えられる。

$$
\int_V \nabla \cdot \boldsymbol{v}(\boldsymbol{x}) dV \simeq
\sum_{\boldsymbol{x} \in V} (
    d_\mathrm{right}(\boldsymbol{x}) +
    d_\mathrm{left}(\boldsymbol{x}) +
    d_\mathrm{top}(\boldsymbol{x}) +
    d_\mathrm{lower}(\boldsymbol{x})
)
\tag{2}
$$

ここで、$(x,y)$ から上側の格子点 $(x,y+\Delta)$ への流出量 $d_\mathrm{upper}(x,y)$ は、上側の格子点 $(x,y+\Delta)$ から見ると流出ではなく流入なので、**絶対値が等しく符号が逆**。  
下側・右側・左側についても同じことが言えるので、

$$
\begin{eqnarray}
    d_\mathrm{upper}(x,y) &=& - d_\mathrm{lower}(x,y+\Delta)
    \\
    d_\mathrm{lower}(x,y) &=& - d_\mathrm{upper}(x,y-\Delta)
    \\
    d_\mathrm{right}(x,y) &=& - d_\mathrm{left}(x+\Delta,y)
    \\
    d_\mathrm{left}(x,y) &=& - d_\mathrm{right}(x-\Delta,y)
\end{eqnarray}
$$

よって $(2)$ の右辺の和を取ると、**閉空間 $V$ 内の隣接格子点どうしでは流出・流入が打ち消しあってゼロになる**（上図の赤矢印。破線は隣接格子点からの流出）。

しかし、閉曲面 $S$ と接する格子点の場合、その隣接格子点には $S$ 外部のものが存在する。  
**$S$ 外部の格子点は積分範囲 $V$ に含まれないため、この打ち消しが発生しない**（上図のオレンジ矢印）。

したがって、**$(2)$ 右辺の和を取ると、$S$ 外部への流出量だけが打ち消されずに残る**。
これはまさに、ベクトル場 $\boldsymbol{v}(\boldsymbol{x})$ の $S$ 上の面積分そのものである。すなわち、

$$
\int_V \nabla \cdot \boldsymbol{v}(\boldsymbol{x}) dV
=
\int_S \boldsymbol{v}(\boldsymbol{x}) \cdot \boldsymbol{n}(\boldsymbol{x}) dS
$$

