---
title: 剛体の運動
title-en: Motion of Rigid Body
---

# 基本的な定理・法則

角運動量保存


# シミュレーション

## 剛体の回転

難航中...

```python
import numpy as np
from matplotlib import pyplot as plt

M = 1.0              # 剛体全体の質量
lx, ly, lz = 3, 5, 7 # 直方体型の剛体のサイズ
dx = 1.0             # 格子点の間隔
dt = 0.01            # 時間間隔 [秒]

nx, ny, nz = int(lx//dx+1), int(ly//dx+1), int(lz//dx+1)
dm = M / (nx*ny*nz)

XX, YY, ZZ = np.meshgrid(
    np.array(range(nx)),
    np.array(range(ny)),
    np.array(range(nz))
)
X = np.array([XX.flatten(), YY.flatten(), ZZ.flatten()]).T
x_g = X.mean(axis=0)  # 重心


# 回転軸ベクトル
# - 軸の左回りに回転
# - ベクトルの長さが角速度 [rad/s] を表す
rotate_axis = np.array([0, 0, np.pi])

F = np.zeros(X.shape)




fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X[:,0], X[:,1], X[:,2])
plt.show()










# 直方体の格子点に質点を配置し、全体を剛体とみなす
XX, YY, ZZ = np.meshgrid(
	np.array(range(-1, 1+1)),
	np.array(range(-2, 2+1)),
	np.array(range(-3, 3+1))
)
X = np.array([XX.flatten(), YY.flatten(), ZZ.flatten()]).T

# 回転軸を表す方向ベクトル
rotate_axis_vec = np.array([0, 0, 1])
# 角速度 rad/s
omega = 2 * np.pi

def calc_v_of_point(r):
	r_norm = np.linalg.norm(r)
	cos = rotate_axis_vec.dot(r) / r_norm
	sin = 0 if 1 < cos**2 else np.sqrt(1 - cos**2)
	v_dir_vec = np.cross(rotate_axis_vec, r)
	v_dir_vec /= np.linalg.norm(v_dir_vec)
	return r_norm * sin * v_dir_vec

def calc_v(X):
	V = []
	for x in X:
		v.append(calc_v_of_point(x))
	return np.array(v)

T = 400
dt = np.pi / 50
for i in range(T):
	v = calc_v(X)
	
```