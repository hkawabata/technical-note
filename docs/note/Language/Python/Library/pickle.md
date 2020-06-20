---
title: pickle
---

# pickle とは

Python オブジェクトをファイルとして保存するライブラリ。

# 使い方

```python
import pickle

l = [1,2,3]
with open('sample.pkl', 'wb') as f:
    pickle.dump(l, f)
```

```python
import pickle

l = [1,2,3]
with open('sample.pkl', 'rb') as f:
    l = pickle.load(f)
print(l)
# [1, 2, 3]
```

# 注意

## 読み書きモード

- バイナリモード書き込み（`open(file, 'wb')`）したファイルはバイナリモードで読み込む（`open(file, 'rb')`）必要がある
- テキストモード（'r', 'w'）も同様

## プロトコルバージョン

pickle の処理のバージョン。  

- 書き込み時と異なるバージョンで読み込もうとするとエラーになる
- `pickle.load()`メソッドがバージョンを自動判別してくれるため、新しい Python バージョンで作成したファイルを古い Python で読むときに意外は問題がない

保存時にプロトコルバージョンを指定する方法：

```python
pickle.dump(obj, file, protocol=2)
```



