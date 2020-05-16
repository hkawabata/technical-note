---
title: 凝集型クラスタリング
---

# 凝集型クラスタリングとは

階層的クラスタリングの種別。  
個々のデータ点をそれぞれ別のクラスタとみなすところからスタートして、最も近いクラスタのペアを順次マージしてクラスタを減らしていく。

# 主な手法

## 単連結法（最短距離法）

クラスタのペアに対し、クラスタ間をまたぐ **距離が最も近い** データサンプルのペアを見つけ、その距離をクラスタの近さとみなす。

![Single Linkage](https://user-images.githubusercontent.com/13412823/82131573-7f8c7980-9811-11ea-959e-d4d236a1c315.png)


## 完全連結法（最長距離法）

クラスタのペアに対し、クラスタ間をまたぐ **距離が最も遠い** データサンプルのペアを見つけ、その距離をクラスタの近さとみなす。

![Complete Linkage](https://user-images.githubusercontent.com/13412823/82131571-7ef3e300-9811-11ea-9640-dbc936b368df.png)


## 群平均法

クラスタのペアに対し、クラスタ間をまたぐデータサンプルの **全ペアの組み合わせの平均距離** をクラスタの近さとみなす。

![Average](https://user-images.githubusercontent.com/13412823/82131570-7dc2b600-9811-11ea-8781-ca26b7039f52.png)


## ウォード法

クラスタのペア $$C_1, C_2$$ に対し、クラスタをマージする前の偏差平方和

$$
\begin{eqnarray}
SSD(C_1) &=& \displaystyle \sum_{\boldsymbol{x}^{(i)} \in C_1} \left\| \boldsymbol{x}^{(i)} - \overline{\boldsymbol{x}}_{C_1} \right\|^2 \\
SSD(C_2) &=& \displaystyle \sum_{\boldsymbol{x}^{(i)} \in C_2} \left\| \boldsymbol{x}^{(i)} - \overline{\boldsymbol{x}}_{C_2} \right\|^2
\end{eqnarray}
$$

と、クラスタをマージした後の偏差平方和

$$
SSD(C_1 \cup C_2) = \displaystyle \sum_{\boldsymbol{x}^{(i)} \in C_1 \cup C_2} \left\| \boldsymbol{x}^{(i)} - \overline{\boldsymbol{x}}_{C_1 \cup C_2} \right\|^2
$$

を計算する。

マージの前後でクラスタの偏差平方和の変化が少ないほど近いとみなし、

$$
SSD(C_1 \cup C_2) - SSD(C_1) - SSD(C_2)
$$

をクラスタの近さとする。

![Ward](https://user-images.githubusercontent.com/13412823/82131569-7bf8f280-9811-11ea-8875-72ebbb4430db.png)


# 実装

## コード

{%gist e32d290b91b87078f223023e1282f75f clustering-agglomerative.py %}

## 動作確認

{%gist e32d290b91b87078f223023e1282f75f ~fit.py %}

![凝集型階層クラスタリング](https://user-images.githubusercontent.com/13412823/82121870-387b9580-97cb-11ea-9ed9-e0ae6603fa3f.png)
