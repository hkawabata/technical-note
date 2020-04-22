---
title: 決定木（作成中）
---

# 決定木とは


# 実装

## コード

{% gist f48fc2b0f1adb9adc10ad8badecf1254 decision-tree.py %}


```python
# python3

import numpy as np

class MyNode:
    def __init__(self, label, i_feature=None, threshold=None):
        """
        Parameters
        ----------
        label : ノードの代表ラベル
        i_feature : 判定に用いる特徴量のインデックス
        threshold : 判別閾値
        """
        self.left = None
        self.right = None
        self.i_feature = i_feature
        self.threshold = threshold
        self.label = label
    
    def is_leaf(self):
        return self.threshold is None

class DecisionTree:
    def __init__(self, min_sample_leaf=1):
        self.root = None
        self.min_sample_leaf = min_sample_leaf

    def predict(self, x):
        """
        Parameters
        ----------
        x : 分類したいデータ（d次元ベクトル）
        """
        stack = [self.root]
        while len(stack) > 0:
            node = stack.pop()
            if node.left is None:
                return node.label
            if x[node.i_feature] < node.threshold:
                stack.append(node.left)
            else:
                stack.append(node.right)
    
    def fit(self, data, labels):
        self.root = self.dfs(data, labels)
    
    def dfs(self, data, labels):
        best_data_left, best_data_right = [], []
        best_labels_left, best_labels_right = [], []
        best_threshold = None
        best_i_feature = None
        best_gain = - float('inf')
        for i_f in range(len(data[0])):
            data_f = np.unique(data[:, i_f])  # 重複削除 & ソート
            th_arr = (data_f[:-1] + data_f[1:]) / 2.0  # 閾値候補として中間の値を取る
            for i_th in range(len(th_arr)):
                d_l, d_r = [], []
                l_l, l_r = [], []
                for j in range(len(data)):
                    if data[j][i_f] < th_arr[i_th]:
                        d_l.append(data[j])
                        l_l.append(labels[j])
                    else:
                        d_r.append(data[j])
                        l_r.append(labels[j])
                inpurity_l = self.inpurity(l_l)
                inpurity_r = self.inpurity(l_r)
                gain = - inpurity_l*len(d_l)/len(data) - inpurity_r*len(d_r)/len(data)
                if gain > best_gain and len(d_l) >= self.min_sample_leaf and len(d_r) >= self.min_sample_leaf:
                    best_gain = gain
                    best_inpurity_left, best_inpurity_right = inpurity_l, inpurity_r
                    best_threshold = th_arr[i_th]
                    best_i_feature = i_f
                    best_data_left, best_data_right = d_l, d_r
                    best_labels_left, best_labels_right = l_l, l_r

        node_label = self.__representative_label(labels)
        # 一度も gain が更新されなかった
        if best_i_feature is None:
            return MyNode(node_label)
        
        node = MyNode(node_label, best_i_feature, best_threshold)
        if best_inpurity_left == 0:
            node.left = MyNode(best_labels_left[0])
        else:
            node.left = self.dfs(np.array(best_data_left), np.array(best_labels_left))
        if best_inpurity_right == 0:
            node.right = MyNode(best_labels_right[0])
        else:
            node.right = self.dfs(np.array(best_data_right), np.array(best_labels_right))
        
        # 左と右が共に葉で同じラベルなら枝刈りして自分を葉にする
        if node.left.is_leaf() and node.right.is_leaf() and node.left.label == node.right.label:
            node = MyNode(node_label)

        return node
    
    def inpurity(self, labels):
        """
        与えられたラベルの集合の不純度（ジニ不純度）を計算
        """
        inp = 1.0
        rate_label1 = labels.count(1) / len(labels)
        inp -= rate_label1**2
        inp -= (1-rate_label1)**2
        return inp
    
    def __representative_label(self, labels):
        """
        多数決で代表ラベルを決める
        """
        num_label1 = np.count_nonzero(labels == 1, axis=0)
        return 1 if num_label1*2 >= len(labels) else -1
```

## 動作確認

```python
# 学習データ作成
N = 300
A = 6
B = 2
x = np.random.rand(N) * A
y = np.random.rand(N) * B
data = np.array([x, y]).T
def get_label(d_):
    tmp_ = (d_[0] // (A/3) + d_[1] // (B/2)) % 2
    return 1 if tmp_ == 1 else -1
labels = np.array([get_label(data[i]) for i in range(N)])
# 外れ値を入れる
for i in range(N//50):
    labels[i] = -1 if labels[i] == 1 else 1

# 学習
tree = DecisionTree(1)
tree.fit(data, labels)
# 決定領域の描画
pass

# 学習（過学習回避）
tree = DecisionTree(10)
tree.fit(data, labels)
# 決定領域・決定木の描画
pass
```

![過学習](https://user-images.githubusercontent.com/13412823/79865383-0a967180-8416-11ea-9329-bf1107272cb7.png)

![過学習回避](https://user-images.githubusercontent.com/13412823/79865392-0d916200-8416-11ea-97a3-9171a5c84e3f.png)

→ 葉を構成するサンプル数の最小値による制約で過学習が抑えられている

![決定木](https://user-images.githubusercontent.com/13412823/79865497-39ace300-8416-11ea-9bbe-0fdaeaddee73.png)


```python
# 学習データ作成
R1 = 2
R2 = 4
R_MARGIN = 0.3
C = (1,1)

N = 300
r1 = R1*np.random.rand(N//2)
r2 = (R2-R1-R_MARGIN)*np.random.rand(N//2) + R1 + R_MARGIN
theta1 = np.random.rand(N//2) * 2 * np.pi
theta2 = np.random.rand(N//2) * 2 * np.pi
data1 = np.array([r1 * np.sin(theta1) + C[0], r1 * np.cos(theta1) + C[1]]).T
data2 = np.array([r2 * np.sin(theta2) + C[0], r2 * np.cos(theta2) + C[1]]).T
data = np.concatenate([data1, data2])
labels = np.array([1 if i < N//2 else -1 for i in range(N)])

# 学習
tree = DecisionTree(10)
tree.fit(data, labels)

# 決定領域・決定木の描画
pass
```

![過学習回避・同心円](https://user-images.githubusercontent.com/13412823/79865396-0e29f880-8416-11ea-85a2-88c18628face.png)

![決定木・同心円](https://user-images.githubusercontent.com/13412823/79865503-3c0f3d00-8416-11ea-97f6-8e252d56cd25.png)

