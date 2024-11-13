---
title: 質点の運動
title-en: Motion of Mass Point
---

# 基本的な定理・法則

## 座標・速度・加速度の関係

時刻 $t$ において
- 質点の座標を $\boldsymbol{x}(t)$
- 質点の速度を $\boldsymbol{v}(t)$
- 質点の加速度を $\boldsymbol{a}(t)$

とすると、

$$
\begin{eqnarray}
    \boldsymbol{v}(t) &=& \cfrac{d\boldsymbol{x}(t)}{dt} \\
    \boldsymbol{a}(t) &=& \cfrac{d\boldsymbol{v}(t)}{dt} = \cfrac{d^2\boldsymbol{x}(t)}{dt^2}
\end{eqnarray}
$$

これらの式を積分すると

$$
\begin{eqnarray}
    \boldsymbol{x}(t) = \boldsymbol{x}(0) + \int_0^t \boldsymbol{v}(t') dt'
    \\
    \boldsymbol{v}(t) = \boldsymbol{v}(0) + \int_0^t \boldsymbol{a}(t') dt'
\end{eqnarray}
$$

数値計算のため、微小な時間ステップ $\Delta t$ 刻みの漸化式で書くと、

$$
\begin{eqnarray}
    x(t+\Delta t) &=& x(t) + v(t) \Delta t
    \\
    v(t+\Delta t) &=& v(t) + a(t) \Delta t
\end{eqnarray}
$$


## 運動方程式

質点の質量を $m$、時刻 $t$ に質点にかかる力を $\boldsymbol{F}(t)$ とすると、

$$
m \boldsymbol{a}(t) = \boldsymbol{F}(t)
$$


# シミュレーション

## 放物運動

運動方程式 $m \boldsymbol{a} = \boldsymbol{F}$ を立てると、

$$
\begin{eqnarray}
	& m \boldsymbol{a} &=& m \boldsymbol{g}
	\\ \Longleftrightarrow \ &
	\boldsymbol{a} &=&\ \ \begin{pmatrix}0 \\ -g\end{pmatrix}
\end{eqnarray}
$$

{% gist 4bc7edbbbe33532104fe4c97743731ba ~parabolic-motion.py %}

空気抵抗なし：

![sample](https://user-images.githubusercontent.com/13412823/226670896-8e7de030-34cf-4a89-9b02-93fc385b7f8b.gif)

空気抵抗あり：

![sample](https://user-images.githubusercontent.com/13412823/226672700-756cebff-340f-41b8-a030-1ce62e5e9c37.gif)


## 振り子の運動

質量 $m$ の質点が速度 $v_\theta$、半径 $L$ の円運動を維持するために必要な半径方向の力（向心力）は $\cfrac{mv_\theta^2}{L}$  であり、これが張力 $S$ と重力の半径方向成分の和に等しいから、

$$
S - mg \cos \theta = \cfrac{mv_\theta^2}{L}
$$

よって $S$ を $v_\theta, \theta$ の式で表せる。運動方程式 $m \boldsymbol{a} = \boldsymbol{F}$ を立てると、

$$
\begin{eqnarray}
	& m \boldsymbol{a} &= m \boldsymbol{g} + \boldsymbol{S}
	\\ \Longleftrightarrow \ &
	\boldsymbol{a} &=
	\begin{pmatrix}0 \\ -g\end{pmatrix} +
	\cfrac{1}{m} \begin{pmatrix} -S \sin \theta \\ S \cos \theta \end{pmatrix}
	= \begin{pmatrix}
		- g \sin \theta \cos \theta - \cfrac{v_\theta^2}{L} \sin \theta \\
		\cfrac{v_\theta^2}{L} \cos \theta - g \sin^2 \theta
	\end{pmatrix}
\end{eqnarray}
$$

{% gist 4bc7edbbbe33532104fe4c97743731ba ~pendulum.py %}

![sample](https://user-images.githubusercontent.com/13412823/226149797-9eaa4041-61aa-4e08-95a4-4be3da704a09.gif)


## 連星の重力運動

$$
\boldsymbol{F} = m \boldsymbol{a} = G \cfrac{Mm}{r^2} \boldsymbol{\hat{r}}
$$

月と地球の連星運動をシミュレーションしてみる。

- $M_E$：地球の質量
- $M_M$：月の質量
- $v$：地球と月の相対速度
- $D_M$：地球と月の平均的な距離
- $G$：万有引力定数

とすると、

$$
\begin{eqnarray}
	M_E &=& 5.972 \times 10^{24}\ \mathrm{kg} \\
	M_M &=& 7.346 \times 10^{22}\ \mathrm{kg} \\
	G &=& 6.674 \times 10^{-11}\ \mathrm{m^3 kg^{−1}s^{−2}} \\
	D_M &=& 3.844 \times 10^{8}\ \mathrm{m} \\
	v &=& 1023\ \mathrm{ms^{-1}}
\end{eqnarray}
$$

ケタが大きくて計算しにくいので、単位系を $\mathrm{m, kg, s} \longrightarrow D_M, M_E, \mathrm{day}$ に変換する。

$$
\begin{eqnarray}
	1 \mathrm{m} = \cfrac{1}{3.844 \times 10^{8}} D_M \\
	1 \mathrm{kg} =  \cfrac{1}{5.972 \times 10^{24}} M_E \\
	1 \mathrm{s} = \cfrac{1}{60 \times 60 \times 24} \mathrm{day}
\end{eqnarray}
$$

なので、

$$
\begin{eqnarray}
	M_M &=& 1.230 \times 10^{-2} M_E \\
	G &=& 5.238 \times 10^{-2}\ D_M^3 M_E^{-1} \mathrm{day}^{-2} \\
	v &=& 2.299 \times 10^{-1} D_M \mathrm{day}^{-1}
\end{eqnarray}
$$

{% gist 4bc7edbbbe33532104fe4c97743731ba ~binary-star.py %}

![sample](https://user-images.githubusercontent.com/13412823/226108982-172feb4d-9ea3-427f-b208-04eabb46579e.gif)


地球が重すぎてあまり動きが分からないので、連星の質量比を5:1にしてみる。

![sample](https://user-images.githubusercontent.com/13412823/226109595-28273254-b2b2-45cd-a9bf-348ed0c92045.gif)



## 3連星の重力運動（三体問題）

3つの天体の重力相互作用を考える。

- $m_1,m_2,m_3$：3天体の質量
- $r_{ij}$：天体 $i,j$ の間の距離
- $\boldsymbol{\hat{r}}_{ij}$：天体 $i$ から $j$ に向かう方向の単位ベクトル

とすると、天体1,2,3に働く引力 $\boldsymbol{F}_1, \boldsymbol{F}_2, \boldsymbol{F}_3$ は、

$$
\begin{eqnarray}
    \boldsymbol{F}_1 =
    G \cfrac{m_1 m_2}{r_{12}^2} \boldsymbol{\hat{r}}_{12}
    + G \cfrac{m_3 m_1}{r_{31}^2} \boldsymbol{\hat{r}}_{13} \\
    \boldsymbol{F}_2 =
    G \cfrac{m_2 m_3}{r_{23}^2} \boldsymbol{\hat{r}}_{23}
    + G \cfrac{m_1 m_2}{r_{12}^2} \boldsymbol{\hat{r}}_{21} \\
    \boldsymbol{F}_3 =
    G \cfrac{m_3 m_1}{r_{31}^2} \boldsymbol{\hat{r}}_{31}
    + G \cfrac{m_2 m_3}{r_{23}^2} \boldsymbol{\hat{r}}_{32}
\end{eqnarray}
$$

運動方程式 $\boldsymbol{F} = m \boldsymbol{a}$ より、天体1,2,3の加速度は

$$
\begin{eqnarray}
    \boldsymbol{a}_1 =
    G \cfrac{m_2}{r_{12}^2} \boldsymbol{\hat{r}}_{12}
    + G \cfrac{m_3}{r_{31}^2} \boldsymbol{\hat{r}}_{13} \\
    \boldsymbol{a}_2 =
    G \cfrac{m_3}{r_{23}^2} \boldsymbol{\hat{r}}_{23}
    + G \cfrac{m_1}{r_{12}^2} \boldsymbol{\hat{r}}_{21} \\
    \boldsymbol{a}_3 =
    G \cfrac{m_1}{r_{31}^2} \boldsymbol{\hat{r}}_{31}
    + G \cfrac{m_2}{r_{23}^2} \boldsymbol{\hat{r}}_{32}
\end{eqnarray}
$$

3体問題の微分方程式は特別な場合を除いて解析解が得られないことが知られており、不規則な運動になる。

ここでは簡単のため、
- 平面上の3体問題
- 各質点は半径1の円周に沿って左回りの初速度を持つ

という状況を仮定する。

{% gist 4bc7edbbbe33532104fe4c97743731ba ~three-body-problem.py %}

質量が等しく、初期の速さも等しい場合：
- $M_1 = M_2 = M_3 = 1.0$
- $\vert v_1(0)\vert = \vert v_2(0)\vert = \vert v_3(0)\vert = 0.1$

![equal](https://gist.github.com/user-attachments/assets/24c1e8a9-412a-4700-8260-d2fa825e21e3)

質量が1%ずつ違い、初期の速さは同じ場合：
- $M_1 = 1.0, M_2 = 1.01, M_3 = 0.99$
- $\vert v_1(0)\vert = \vert v_2(0)\vert = \vert v_3(0)\vert = 0.1$

```python
M1, M2, M3 = 1, 1.01, 0.99
```

![mass1percent](https://gist.github.com/user-attachments/assets/52835139-b75e-4d7d-b945-f557d9f61251)

質量は同じだが、初期の速さが1%違う場合：
- $M_1 = M_2 = M_3 = 1.0$
- $\vert v_1(0)\vert = 0.101, \vert v_2(0)\vert = 0.099, \vert v_3(0)\vert = 0.100$

```python
v1 = np.array([0, 1.0]) * 0.101
v2 = np.array([-np.sqrt(3)/2.0, -0.5]) * 0.099
v3 = (-M1 * v1 - M2 * v2) / M3
```

![velocity1percent](https://gist.github.com/user-attachments/assets/d46c7467-ee68-454b-a4c3-9748368154cf)



