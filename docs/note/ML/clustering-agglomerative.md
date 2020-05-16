---
title: 凝集型クラスタリング
---

# 凝集型クラスタリングとは

階層的クラスタリングの種別。  
個々のデータ点をそれぞれ別のクラスタとみなすところからスタートして、最も近いクラスタのペアを順次マージしてクラスタを減らしていく。

# 主な手法

## 単連結法（最短距離法）

クラスタのペアに対し、クラスタ間をまたぐ **距離が最も近い** データサンプルのペアを見つけ、その距離をクラスタの近さとみなす。

![Single](https://user-images.githubusercontent.com/13412823/82132013-486c9700-9816-11ea-845c-15bc042f4de3.png)


## 完全連結法（最長距離法）

クラスタのペアに対し、クラスタ間をまたぐ **距離が最も遠い** データサンプルのペアを見つけ、その距離をクラスタの近さとみなす。

![Complete](https://user-images.githubusercontent.com/13412823/82132014-4acef100-9816-11ea-8fbe-0392d41054de.png)


## 群平均法

クラスタのペアに対し、クラスタ間をまたぐデータサンプルの **全ペアの組み合わせの平均距離** をクラスタの近さとみなす。

![Average](https://user-images.githubusercontent.com/13412823/82132015-4b678780-9816-11ea-84ad-5608600cc017.png)


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

![Ward](https://user-images.githubusercontent.com/13412823/82132017-4c001e00-9816-11ea-953f-990133f6ff5d.png)


# 実装

## コード

{%gist e32d290b91b87078f223023e1282f75f clustering-agglomerative.py %}

## 動作確認

{%gist e32d290b91b87078f223023e1282f75f ~fit.py %}

![凝集型階層クラスタリング](https://user-images.githubusercontent.com/13412823/82121870-387b9580-97cb-11ea-9ed9-e0ae6603fa3f.png)
