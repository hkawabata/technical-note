---
title: 決定木（作成中）
---

# 決定木とは


# 実装

## コード

{% gist f48fc2b0f1adb9adc10ad8badecf1254 decision-tree.py %}


## 動作確認

{% gist f48fc2b0f1adb9adc10ad8badecf1254 fit1.py %}

![過学習](https://user-images.githubusercontent.com/13412823/79865383-0a967180-8416-11ea-9329-bf1107272cb7.png)

![過学習回避](https://user-images.githubusercontent.com/13412823/79865392-0d916200-8416-11ea-97a3-9171a5c84e3f.png)

→ 葉を構成するサンプル数の最小値による制約で過学習が抑えられている

![決定木](https://user-images.githubusercontent.com/13412823/79865497-39ace300-8416-11ea-9bbe-0fdaeaddee73.png)


{% gist f48fc2b0f1adb9adc10ad8badecf1254 fit2.py %}

![過学習回避・同心円](https://user-images.githubusercontent.com/13412823/79865396-0e29f880-8416-11ea-85a2-88c18628face.png)

![決定木・同心円](https://user-images.githubusercontent.com/13412823/79865503-3c0f3d00-8416-11ea-97f6-8e252d56cd25.png)

