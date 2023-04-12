---
title: 質点の運動
title-en: Motion of Mass Point
---

# 基本的な定理・法則

$$
\boldsymbol{F}(t) = m \boldsymbol{a}(t)
$$

$$
\boldsymbol{v}(t) = \boldsymbol{v}(0) + \int_0^t \boldsymbol{a}(t') dt'
$$

$$
\boldsymbol{x}(t) = \boldsymbol{x}(0) + \int_0^t \boldsymbol{v}(t') dt'
$$

# シミュレーション

## 放物運動

運動方程式 $m \boldsymbol{a} = \boldsymbol{F}$ を立てると、

$$
\begin{eqnarray}
	& m \boldsymbol{a} &=& m \boldsymbol{g}
	\\ \Longleftrightarrow \ &
	\boldsymbol{a} &=& \begin{pmatrix}0 \\ -g\end{pmatrix}
\end{eqnarray}
$$

```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

np.seterr(all='raise')

class PointMass:
	def __init__(self, name, m, x0, v0):
		self.name = name
		self.m = m
		self.x = [x0]
		self.v = [v0]
		self.a = None
	
	def update(self, x, v, a):
		self.x.append(x)
		self.v.append(v)
		self.a.append(a)


class MotionSystem:
	def __init__(self, point_masses):
		self.point_masses = []
		for pm in point_masses:
			pm.a = [self.calc_a(pm)]
			self.point_masses.append(pm)
	
	def exec_simulation(self, dt, T):
		self.t = [0]
		for i in range(1, T+1):
			self.t.append(dt * i)
			for pm in self.point_masses:
				x_new = pm.x[-1] + pm.v[-1] * dt
				v_new = pm.v[-1] + pm.a[-1] * dt
				a_new = self.calc_a(pm)
				pm.update(x_new, v_new, a_new)
	
	def calc_a(self, pm):
		pass
	
	def draw_simulation(self, path_length=5, slice_size=1):
		x_max, y_max = np.max([np.max(pm.x, axis=0) for pm in system.point_masses], axis=0)
		x_min, y_min = np.min([np.min(pm.x, axis=0) for pm in system.point_masses], axis=0)
		xs_plot = [np.array(pm.x)[::slice_size] for pm in self.point_masses]
		names = [pm.name for pm in self.point_masses]
		fig, ax = plt.subplots()
		def update(i):
			ax.clear()
			ax.set_aspect('equal')
			ax.set_xlim([x_min, x_max])
			ax.set_ylim([y_min, y_max])
			i_start = max(0, i-path_length)
			for j in range(len(names)):
				x_plot = xs_plot[j]
				name = names[j]
				ax.plot(x_plot[i_start:i+1,0], x_plot[i_start:i+1,1], lw=0.3, color='black')
				ax.scatter(x_plot[i,0], x_plot[i,1], s=30.0, color="C{}".format(j), marker='o', label=name)
			ax.legend(loc='upper right')
			ax.grid()
		ani = animation.FuncAnimation(fig, update, frames=len(xs_plot[0]), interval=100)
		ani.save("sample.gif", writer="pillow", fps=60)
		plt.close()


class ParaboricMotionSystem(MotionSystem):
	g = 9.8
	def __init__(self, point_masses, k):
		self.k = k
		super().__init__(point_masses)
	
	def calc_a(self, pm):
		a_gravity = np.array([0, -self.g])
		a_air = -pm.v[-1] * self.k / pm.m
		return a_gravity + a_air


v = 10.0
v1, v2, v3 = [v*np.array([np.cos(theta), np.sin(theta)]) for theta in [np.pi/3, np.pi/4, np.pi/6]]
m1, m2, m3 = 1.0e-6, 1.0e-5, 1.0e-4

# 空気抵抗なし
point_masses = [
	# 初速度の向きを変える
	PointMass(r'$\theta_0=\pi/3$', m=m1, x0=np.zeros(2), v0=v1),
	PointMass(r'$\theta_0=\pi/4$', m=m1, x0=np.zeros(2), v0=v2),
	PointMass(r'$\theta_0=\pi/6$', m=m1, x0=np.zeros(2), v0=v3)
]
system = ParaboricMotionSystem(point_masses, k=0.)
system.exec_simulation(dt=0.01, T=150)
system.draw_simulation(path_length=7, slice_size=5)
# 空気抵抗あり
point_masses = [
	# 初速度の向きを変える
	PointMass(r'$\theta_0=\pi/3, m=10^{-6} \mathrm{kg}$', m=m1, x0=np.zeros(2), v0=v1),
	PointMass(r'$\theta_0=\pi/4, m=10^{-6} \mathrm{kg}$', m=m1, x0=np.zeros(2), v0=v2),
	PointMass(r'$\theta_0=\pi/6, m=10^{-6} \mathrm{kg}$', m=m1, x0=np.zeros(2), v0=v3),
	# 質量を変える
	PointMass(r'$\theta_0=\pi/4, m=10^{-5} \mathrm{kg}$', m=m2, x0=np.zeros(2), v0=v2),
	PointMass(r'$\theta_0=\pi/4, m=10^{-4} \mathrm{kg}$', m=m3, x0=np.zeros(2), v0=v2)
]
system = ParaboricMotionSystem(point_masses, k=1.0e-6)
system.exec_simulation(dt=0.01, T=150)
system.draw_simulation(path_length=7, slice_size=5)
```

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

```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

np.seterr(all='raise')

class PendulumMotion:
	g = 9.8
	
	def __init__(self, r, theta0):
		self.__r = r
		self.__theta = theta0
		self.__x = r * np.array([np.sin(theta0), -np.cos(theta0)])
		self.__v = np.zeros(2)
		self.__a = self.__calc_a()
	
	def exec_simulation(self, T, dt):
		self.__dt = dt
		self.X = [self.__x.copy()]
		self.V = [self.__v.copy()]
		self.A = [self.__a.copy()]
		for i in range(T):
			self.__update()
			self.X.append(self.__x.copy())
			self.V.append(self.__v.copy())
			self.A.append(self.__a.copy())
		self.X = np.array(self.X)
		self.V = np.array(self.V)
		self.A = np.array(self.A)
	
	def __update(self):
		self.__v += self.__a * self.__dt
		x_tmp = self.__x + self.__v * self.__dt
		self.__theta = np.arctan(-x_tmp[0]/x_tmp[1])
		# 運動半径 r が一定になるよう x を調整
		self.__x = self.__r * np.array([np.sin(self.__theta), -np.cos(self.__theta)])
		self.__a = self.__calc_a()
	
	def __calc_a(self):
		r_unit_vec = np.array([
			-np.sin(self.__theta),
			np.cos(self.__theta)
		])
		v_norm = np.linalg.norm(self.__v)
		a_tention = (self.g * np.cos(self.__theta) + v_norm**2 / self.__r) * r_unit_vec
		a_gravity = np.array([0, -self.g])
		return a_gravity + a_tention
	
	def draw_result(self, path_length=5, slice_size=1):
		x_min, y_min = self.X[:,0].min(), self.X[:,1].min()
		x_max, y_max = self.X[:,0].max(), self.X[:,1].max()
		X_plot = self.X[::slice_size]
		fig, ax = plt.subplots()
		def update(i):
			ax.clear()
			ax.set_aspect('equal')
			ax.set_xlim([x_min, x_max])
			ax.set_ylim([y_min, 0])
			i_start = max(0, i-path_length)
			ax.plot(X_plot[i_start:i+1,0], X_plot[i_start:i+1,1], lw=0.3, color='black')
			ax.scatter(X_plot[i,0], X_plot[i,1], s=30.0, color='blue', marker='o')
			ax.plot([0, X_plot[i,0]], [0, X_plot[i,1]], lw=0.5, color='black')
			ax.grid()
		ani = animation.FuncAnimation(fig, update, frames=len(X_plot), interval=100)
		ani.save("sample.gif", writer="pillow", fps=60)
		plt.close()

model = PendulumMotion(r=0.3, theta0=np.pi*2/5)
model.exec_simulation(T=300, dt=0.01)
model.draw_result(path_length=5, slice_size=2)
```

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


```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

T = 24*90  # 90日間
dt = 1.0/24  # 1時間

M1 = 1.0
M2 = 1.23e-2
G = 5.238e-2

def binary_star_motion(x1_0, x2_0, v1_0, v2_0):
	x1, x2 = np.array(x1_0), np.array(x2_0)
	v1, v2 = np.array(v1_0), np.array(v2_0)
	def calc_a(x1, x2):
		r_vec = x1 - x2
		r_square = (r_vec**2).sum()
		r_dir_vec = r_vec / np.sqrt(r_square)
		a1 = - r_dir_vec * G * M2 / r_square
		a2 = r_dir_vec * G * M1 / r_square
		return a1, a2
	a1, a2 = calc_a(x1, x2)
	X1, X2 = [x1.copy()], [x2.copy()]
	V1, V2 = [v1.copy()], [v2.copy()]
	A1, A2 = [a1.copy()], [a2.copy()]
	for i in range(T):
		v1 += a1 * dt
		v2 += a2 * dt
		x1 += v1 * dt
		x2 += v2 * dt
		a1, a2 = calc_a(x1, x2)
		A1.append(a1.copy())
		A2.append(a2.copy())
		V1.append(v1.copy())
		V2.append(v2.copy())
		X1.append(x1.copy())
		X2.append(x2.copy())
	return np.array(X1), np.array(X2), np.array(V1), np.array(V2), np.array(A1), np.array(A2)

# 連星の重心が原点、系の総運動量がゼロとなるように初期値を設定
x1_0 = np.array([-M2/(M1+M2), 0.0])
x2_0 = np.array([M1/(M1+M2), 0.0])
v1_0 = np.array([0.0, -0.2299*M2/(M1+M2)])
v2_0 = np.array([0.0, 0.2299*M1/(M1+M2)])
X1, X2, V1, V2, A1, A2 = binary_star_motion(x1_0, x2_0, v1_0, v2_0)


x_min, y_min = min(X1[:,0].min(), X2[:,0].min()), min(X1[:,1].min(), X2[:,1].min())
x_max, y_max = max(X1[:,0].max(), X2[:,0].max()), max(X1[:,1].max(), X2[:,1].max())

# gif 動画のサイズを抑えるためデータを圧縮
X1 = X1[::4]
X2 = X2[::4]

fig, ax = plt.subplots()
def update(i):
	ax.clear()
	ax.set_aspect('equal')
	ax.set_xlim([x_min, x_max])
	ax.set_ylim([y_min, y_max])
	l = 24
	i_start = max(0, i-l)
	ax.plot(X1[i_start:i+1,0], X1[i_start:i+1,1], lw=0.3, color='black')
	ax.scatter(X1[i,0], X1[i,1], s=30.0, color='blue', marker='o')
	ax.plot(X2[i_start:i+1,0], X2[i_start:i+1,1], lw=0.3, color='black')
	ax.scatter(X2[i,0], X2[i,1], s=30.0, color='blue', marker='o')
	ax.grid()

ani = animation.FuncAnimation(fig, update, frames=len(X1), interval=100)
ani.save("sample.gif", writer="pillow", fps=int(1.0//dt))
plt.close()
```

![sample](https://user-images.githubusercontent.com/13412823/226108982-172feb4d-9ea3-427f-b208-04eabb46579e.gif)


地球が重すぎてあまり動きが分からないので、連星の質量比を5:1にしてみる。

![sample](https://user-images.githubusercontent.com/13412823/226109595-28273254-b2b2-45cd-a9bf-348ed0c92045.gif)


