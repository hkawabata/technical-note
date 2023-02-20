---
title: 行列の階数
title-en: Rank of Matrix
---

# 行列の階数 (rank) とは

行列 $A$ の rank については、複数の同値な定義が存在する。

1. $A$ の列ベクトルで、線形独立なものの最大数
2. $A$ の行ベクトルで、線形独立なものの最大数
3. $A$ を基本変形して得られる階段行列 $B$ について、行ベクトルのうちゼロベクトルでないものの個数
4. $A$ による線形写像の変換先の空間の次元

# rank の図形的な意味

定義の4より、rank が $r$ の行列 $A$ による線形写像の変換先の空間は $r$ 次元となる。  
以下に具体例を示す。

cf. [描画に使った Python コード](https://gist.github.com/hkawabata/533b3f374d8f938316a63ad502a07914#file-20230219_draw-rank-py)


## 例1：rank 2の2x2行列

2次元から2次元への変換。

$$
A = \begin{pmatrix}
	0.5 & 1.5 \\
	1 & -1
\end{pmatrix}
$$

![Figure_1](https://user-images.githubusercontent.com/13412823/219986083-8fbbc7b3-a6d7-4d0b-a9ba-9556e64fb538.png)

## 例2：rank 1の2x2行列

2次元から1次元への変換。

$$
A = \begin{pmatrix}
	1 & -0.5 \\
	-2 & 1
\end{pmatrix}
$$

![Figure_2](https://user-images.githubusercontent.com/13412823/219986086-886bcf14-7c5e-4fb7-b4e8-2d392cf94f0a.png)

## 例3：rank 3の3x3行列

3次元から3次元への変換。

$$
A = \begin{pmatrix}
	0.5 & 1 & 0 \\
	-0.6 & 0.9 & 0.3 \\
	1 & 0 & -2
\end{pmatrix}
$$

![Figure_3](https://user-images.githubusercontent.com/13412823/219952441-2fddb915-bb71-4e46-88f3-2a9145bb3b7d.png)

## 例4：rank 2の3x3行列

3次元から2次元への変換。

$$
A = \begin{pmatrix}
	-0.5 & 0 & 1 \\
	-1 & 1.5 & 0.5 \\
	0 & 1.5 & -1.5
\end{pmatrix}
$$

![Figure_4](https://user-images.githubusercontent.com/13412823/219982964-5db0a3c1-9486-4ee0-ac91-c650395aee71.png)

## 例5：rank 1の3x3行列

3次元から1次元への変換。

$$
A = \begin{pmatrix}
	-0.5 & 0.3 & 1 \\
	0.5 & -0.3 & -1 \\
	1 & -0.6 & -2
\end{pmatrix}
$$

![Figure_5](https://user-images.githubusercontent.com/13412823/219952450-beb2399b-e0be-48f0-918c-fe63a5a41b9b.png)

## 例6：rank 2の3x2行列

```python
A = np.array([
	[0.5, 1.8],
	[1.0, 1.5],
	[1.0, -0.6]
])
```

2次元から2次元への変換。  
※ $xy$ 座標系から $xyz$ 座標系への変換なので3次元への変換と勘違いしそうだが、変換先の空間は3次元空間の平面になる

$$
A = \begin{pmatrix}
	-0.5 & 0.3 \\
	1 & 1.5 \\
	1 & -0.6
\end{pmatrix}
$$

![Figure_6](https://user-images.githubusercontent.com/13412823/219985900-3c0b585f-791e-4ebb-abe7-ff9cb69e400e.png)
