---
title: Pillow
---

# Pillow とは

Python の画像処理ライブラリ。

# 使い方

```bash
$ pip install Pillow
```

## 読み書き

```python
from PIL import Image

# 読み込み
img = Image.open('path/to/sample.png')

# 何らかの処理
img2 = ...

# 書き込み
img2.save('path/to/sample_new.png')
```


## 情報の取得

```python
# サイズ
img.size   # (1830, 806)
# フォーマット
img.format   # PNG
# モード
img.mode   # RGBA
# 指定したピクセルの色
getpixel((501, 420))   # (154, 180, 121, 255)
```


## リサイズ

```python
img_resized = img.resize((256, 128), Image.LANCZOS)
```


## 回転

```python
# 左回りに90度
img_rotated = img.rotate(90)
```

- 画像サイズは変化しない
- 縦横比が異なる画像を回転させる場合、180の倍数を指定しなければ空白ができる


## フィルタ

```python
from PIL import Image, ImageFilter

img.filter(ImageFilter.GaussianBlur())
```



## モード変換

```python
img_rgba = Image.open('path/to/sample.png')
img_rgb = img_png.convert('RGB')
```


## 画像を重ねる

```python
# 画像1の上に画像2を貼り付け
# 上書きされるため元画像を残す場合は copy した画像を使う
img1.paste(img2)
# 貼り付け位置を指定
img1.paste(img2, (100, 40))
# マスク画像を利用して任意の形で貼り付け
img1.paste(img2, (100, 40), img_mask)
```


