---
title: DBSCAN
---

# DBSCAN とは

クラスタリングの手法の1つ。  
**Density-Based Spacial Clustering of Applications with Noise**.

## 手順

ハイパーパラメータ $$\varepsilon, n_{\rm min-pts}$$

1. データ点 $$\boldsymbol{x}^{(i)}$$ を、以下のルールに従って全データ点をラベル付けする
    - **コア点（Core Point）**：距離 $$\varepsilon$$ 以内に他のデータ点が $$n_{\rm min-pts}$$ 個以上存在する
    - **ボーダー点（Border Point）**：コア点の条件は満たさないが、距離 $$\varepsilon$$ 以内にコア点が1つ以上存在する
    - **ノイズ点（Noise Point）**：コア点・ボーダー点いずれの条件も満たさない
2. コア点同士の距離が $$\varepsilon$$ 以内である場合、それらのコア点を接続する
3. 接続されたコア点とそれらから距離 $$\varepsilon$$ 以内のボーダー点の集合を1つのクラスタとする
    - ノイズ点はどのクラスタにも含めない

![DBSCAN イメージ](https://user-images.githubusercontent.com/13412823/82140439-e047a080-9869-11ea-8614-63bf920374e6.png)


## 実装

### コード

{% gist 17927e3a697abc42ee52c270e0fe78aa dbscan.py %}

### 動作確認

{% gist 17927e3a697abc42ee52c270e0fe78aa ~fit.py %}

![DBSCAN](https://user-images.githubusercontent.com/13412823/82139141-cbb2da80-9860-11ea-8ff0-9994661c1a26.png)
