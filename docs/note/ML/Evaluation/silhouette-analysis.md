---
title: シルエット分析
---

# シルエット分析とは

クラスタリングの性能の評価手法の1つ。  
以下の基準に従って、クラスタリングの性能を可視化する。
- **クラスタ内は密に凝集されているほど良い**
- **異なるクラスタは遠く離れているほど良い**

## 方法

各データサンプル $$\boldsymbol{x}^{(i)}$$ に関して、以下の手順で **シルエット係数（silhouette coefficient）** を計算する。

### 1. シルエット係数の計算

クラスタ内の **凝集度** として、$$\boldsymbol{x}^{(i)}$$ が属するクラスタ $$C_{\rm in}$$ の他の点までの平均距離を計算：

$$
a^{(i)} = \cfrac{1}{|C_{\rm in}|-1} \displaystyle \sum_{\boldsymbol{x}^{(j)} \in C_{\rm in}} \left\| \boldsymbol{x}^{(i)} - \boldsymbol{x}^{(j)} \right\|
$$

別クラスタからの **乖離度** として、$$\boldsymbol{x}^{(i)}$$ に最も近い別クラスタ $$C_{\rm near}$$ に属する点までの平均距離を計算：

$$
b^{(i)} = \cfrac{1}{|C_{\rm near}|} \displaystyle \sum_{\boldsymbol{x}^{(j)} \in C_{\rm near}} \left\| \boldsymbol{x}^{(i)} - \boldsymbol{x}^{(j)} \right\|
$$

$$a^{(i)}, b^{(i)}$$ のうち大きい方で $$b^{(i)} - a^{(i)}$$ を割って **シルエット係数** を計算：

$$
s^{(i)} = \cfrac{b^{(i)} - a^{(i)}}{\max(a^{(i)}, b^{(i)})}
$$

### 2. シルエット係数の解釈

その定義から、シルエット係数は $$[-1, 1]$$ の区間に収まる。

- 値が1に近いほど性能が高い
- 値が負になると、所属クラスタの判別が間違っている可能性がある

全データサンプルでシルエット係数の平均値を取り、1に近いほどクラスタリングの性能が良いと言える。

### 3. 可視化

得られたシルエット係数を以下のルールでソートする。
- 所属クラスタ番号でソート
- 同じクラスタ内ではシルエット係数の値でソート

これを棒グラフにすると、クラスタリング全体の性能、およびクラスタごとの性能が可視化できる。


## コード・動作確認

{% gist 6f47dc1ad4e5874e2d7d9d88673d794f silhouette.py %}

乖離度・凝集度が低くシルエット係数が小さい

![normal](https://user-images.githubusercontent.com/13412823/82108359-e7d35080-9768-11ea-96cb-60f888f84e66.png)

乖離度・凝集度が高くシルエット係数が大きい

![good](https://user-images.githubusercontent.com/13412823/82108355-e6a22380-9768-11ea-8ce0-6482cd5805ed.png)

クラスタが重なり、シルエット係数が負の値を取る（所属クラスタの判定が誤っている恐れ）

![bad](https://user-images.githubusercontent.com/13412823/82108356-e73aba00-9768-11ea-8860-8e90ca1282da.png)

クラスタ数が適切ではなく、シルエット係数が小さい

![2-clusters](https://user-images.githubusercontent.com/13412823/82108354-e43fc980-9768-11ea-9e72-84a29fd1a87d.png)
