---
title: 正定値行列
title-en: Positive Definite Matrix
---

# 正定値行列・半正定値行列の定義

$A$ が $n$ 次の実対称行列またはエルミート行列であるとき、任意の $n$ 次元列ベクトル $\boldsymbol{x}$ が

$$
A \boldsymbol{x} \cdot \boldsymbol{x} \gt 0
$$

を満たすとき、$A$ を **正定値行列** という。  
少しだけ条件を緩めて、

$$
A \boldsymbol{x} \cdot \boldsymbol{x} \ge 0
$$

を満たすとき、$A$ を **半正定値行列** という。  

> **【NOTE】**
> 
> 実空間の場合
> 
> $$
A \boldsymbol{x} \cdot \boldsymbol{x} = (A \boldsymbol{x})^T \boldsymbol{x} = \boldsymbol{x}^T A \boldsymbol{x}
$$
> 
> であるから、正定値行列の定義は
> 
> $$
\boldsymbol{x}^T A \boldsymbol{x} \gt 0
$$
> 
> とも書ける。複素数空間でも同様に
> 
> $$
\boldsymbol{x}^* A \boldsymbol{x} \gt 0
$$

# 正定値行列・半正定値行列の性質

## （半）正定値行列となるための必要十分条件

> **【定理】**
> 
> - $P$：行列 $A$ が（半）正定値行列である
> - $Q$：$A$ の固有値が全て正（非負）の実数である
> 
> とすると、$P \Longleftrightarrow Q$ 

以後、証明は正定値行列の場合について行う。半正定値行列の場合も同様に証明できる。

**【$P \Longrightarrow Q$ の証明】**

$A$ の固有値を $\lambda$、それに対応する固有ベクトルを $\boldsymbol{u}$ とすると、

$$
A \boldsymbol{u} \cdot \boldsymbol{u} = \lambda \boldsymbol{u} \cdot \boldsymbol{u} = \lambda | \boldsymbol{u} |^2
$$

$A$ は正定値行列なので、

$$
A \boldsymbol{u} \cdot \boldsymbol{u} \gt 0
$$

よって

$$
\lambda | \boldsymbol{u} |^2 \gt 0
$$

$| \boldsymbol{u} |^2 \gt 0$ なので、$\lambda \gt 0$

**【$Q \Longrightarrow P$ の証明】**

$A$ の固有値を $\lambda_1, \cdots, \lambda_n \gt 0$ とする。

https://mathlandscape.com/positive-definite-matrix/

ToDo：ユニタリー行列、正規行列