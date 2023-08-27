---
title: LightGBM
---

# LightGBM とは

= Light Gradient Boosting Machine

[XGBoost](xgboost.md) と同じく、[GBDT (勾配ブースティング決定木)](gbdt.md)の実装の1つ。  
学習高速化のためにいろいろな工夫が為されている。


# 例

```bash
brew install cmake libomp
pip install wheel
pip install lightgbm
```

分類問題：

```python
import lightgbm as lgb
from sklearn import datasets, model_selection
from matplotlib import pyplot as plt

ds = datasets.load_iris()
#ds = datasets.load_wine()
X = ds.data
y = ds.target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, shuffle=True)

model = lgb.LGBMClassifier(max_depth=3)
model.fit(X_train, y_train)
acc_train = (model.predict(X_train) == y_train).sum() / float(y_train.size)
acc_test = (model.predict(X_test) == y_test).sum() / float(y_test.size)
print(acc_train, acc_test)
# iris: 1.0 0.9777777777777777
# wine: 1.0 0.9259259259259259

# 特徴量の重要度を可視化
lgb.plot_importance(model)
plt.show()
```

wine データセットの特徴量の重要度：

![lightgbm-feature-importance](https://user-images.githubusercontent.com/13412823/263511283-17c65d3b-d61e-4cde-8323-86cadb39b0de.png)
