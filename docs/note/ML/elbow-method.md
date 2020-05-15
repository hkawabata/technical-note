---
title: エルボー法
---

# エルボー法とは

クラスタリングにおいて、最適なクラスタ数を求めるための手法。  

## 直感的な理解

- クラスタ数が多いほど、個々のクラスタサイズは小さく、同じクラスタのデータは近くに集まる = **クラスタの歪みが小さい**
- クラスタ数をどんどん増やしていき、「これ以上増やしても歪みがあまり改善しない」ようなところを探す

## 方法

### 1. 様々なクラスタ数で学習

様々なクラスタ数でクラスタリングを行い、それぞれモデルの **歪み（distortion）** を計算する。  
k-means や FCM では SSE（クラスタ内誤差平方和）を歪みとして用いると良い。

### 2. クラスタ数と歪みの関係を描画

![Distortion](https://user-images.githubusercontent.com/13412823/82035340-5917f280-96da-11ea-92c3-d50e1a017375.png)

この例だと、クラスタ数 = 4 あたりを超えるとクラスタ数を増やしても歪みがほとんど改善しない。  
→ 最適なクラスタ数として4を選ぶ

## コード・動作確認

{% gist 205917c3a344ee1aaeb82ef37847bc97 ~elbow-method.py %}

※ k-means, FCM のコードは以下を参照。  
https://gist.github.com/hkawabata/205917c3a344ee1aaeb82ef37847bc97

![data](https://user-images.githubusercontent.com/13412823/82034350-0ab62400-96d9-11ea-837d-9557dd6efe1c.png)

![elbow-kmeans](https://user-images.githubusercontent.com/13412823/82034361-0d187e00-96d9-11ea-90d3-eb6b34c432ba.png)

![elbow-fcm](https://user-images.githubusercontent.com/13412823/82034356-0be75100-96d9-11ea-8f20-87dcdb968fff.png)
