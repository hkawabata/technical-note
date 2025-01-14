# streamlit とは

Python で Web アプリケーションを作成できるオープンソースのライブラリ。


# インストール〜アプリ起動

ライブラリのインストール：

```bash
$ pip install streamlit
```

サンプルアプリの実装：

```python
# sample.py
import streamlit as st

st.title('streamlit Tutorial')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('Hello World!')

input_num = st.number_input('Input a number', value=0)
result = input_num ** 2
st.write('Result: ', result)
```

アプリの起動：

```bash
$ streamlit run sample.py
```

→ http://localhost:8501 にアクセス

![スクリーンショット 2025-01-14 11 52 08](https://gist.github.com/user-attachments/assets/16356bef-2cb3-4cf6-b688-4cc82016c7f2)


# 使い方

## st.write の色々

Markdown 表記にも対応：

```python
st.write('# This is h1')
st.write('## This is h2')
st.write('### This is h3')
st.write('**太字の例**')
st.write('~~取消線の例~~')
```

![スクリーンショット 2025-01-14 11 52 16](https://gist.github.com/user-attachments/assets/0fbb0841-2175-4654-99f9-0d975da7ac06)

リスト・辞書の表示：

```python
st.write(['apple', 'orange', 'banana'])
st.write({'apple': 100, 'orange': 50, 'banana': 200})
```

![スクリーンショット 2025-01-14 11 52 23](https://gist.github.com/user-attachments/assets/6b0d716a-62b7-4cb9-a5cd-48de9d6e14d4)

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Tom', 'John'],
    'age': [19, 22],
    'birthPlace': ['U.K.', 'Australia']
})
st.write(df)
```


![スクリーンショット 2025-01-14 11 52 29](https://gist.github.com/user-attachments/assets/7a4c4376-c8db-46a5-bf98-b3f1d9cf7cbe)


## 入力フォーム

```python
# 数値入力を受け取るボックスとデフォルト値を設定
n_input = st.number_input('Input a number', value=0)
st.write('Result: ', n_input**2)

# テキスト入力ボックス
text_input = st.text_input('Input', 'Input some text here.')
# テキストエリア
text_area = st.text_area('Text Area', 'Input some text here.')
```


## ファイルのアップロード

```python
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file)
    # アップロードされたファイルを読み込んで操作
    data = pd.read_csv(uploaded_file)
    st.write(data)
```

![スクリーンショット 2025-01-14 12 32 34](https://gist.github.com/user-attachments/assets/e28a0649-955a-46e9-9b5e-ec22be2f3873)


## ボタン・チェックボックス

```python
if st.button('My Button'):
    st.write('Hello World!')

if st.checkbox('My Checkbox'):
    st.write('Task 1 is done.')

opt_radio = st.radio(
    'My Radio Button', 
    ['A', 'B', 'C'],
    default='B'
)

opt_select = st.selectbox(
    'My Select Box', 
    ['A', 'B', 'C'],
    default='B'
)

opt_multiselect = st.multiselect(
    'My Multi Select Box',
    ['A', 'B', 'C', 'D'],
    default=['A', 'C'] # デフォルトの設定
)

# スライダー
value = st.slider('Select a value', 0, 100, 50) # min, max, default
if value < 30:
    # 値が30以下になったらテキストを表示
    st.write('value = {} < 30'.format(value))

# 両側スライダー、日付型
import datetime
d_min = datetime.date(1900, 1, 1)
d_max = datetime.date(2000, 12, 31)
d_lower = datetime.date(1930, 1, 1)
d_upper = datetime.date(1970, 12, 31)
values = st.slider('期間を指定してください', d_min, d_max, (d_lower, d_upper), format='YYYY-MM-DD (ddd)')
st.write('values: left = {}, right = {}'.format(values[0], values[1]))
```

![スクリーンショット 2025-01-14 15 52 09](https://gist.github.com/user-attachments/assets/60748867-59c1-41ad-8186-df908f5837d1)


## グラフの描画

[matplotlib](matplotlib.md) を利用してグラフを描画できる。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = x**2
y2 = x*7
fig, ax = plt.subplots()
ax.plot(x, y1, label=r'$y=x^2$')
ax.plot(x, y2, label=r'$y=7x$')
plt.legend()
plt.grid()
st.pyplot(fig)
```

![スクリーンショット 2025-01-14 15 16 54](https://gist.github.com/user-attachments/assets/78be530f-35b9-4e2c-bccb-c9025011d0b3)


## データの保持

streamlit はボタンを押したときなどのタイミングで全てのデータがリセットされるため、通常の変数の値は保持されない。  
→ 例えば「ボタンを押すたびにカウンタを1大きくする」といったことができない。

これを解決するには `session_state` の機能を使う：

```python
import streamlit as st

# 変数の定義（ボタンが押された回数）
count = 0
if 'count' not in st.session_state:
    st.session_state.count = 0

# ボタンを表示し、クリックされた回数を表示する
if st.button('クリックしてください'):
    count += 1
    st.session_state.count += 1

st.write(f'クリック回数: {count}（通常の変数）')
st.write(f'クリック回数: {st.session_state.count}（session_state）')
```

![スクリーンショット 2025-01-14 15 25 10](https://gist.github.com/user-attachments/assets/b889c80e-f9f5-47f7-9dd2-50380537bf29)


## コンテナ

```python
with st.container(height=100):
    st.write('Inside container')
    for i in range(10):
        st.write(i)

st.write('Outside container')
```

![スクリーンショット 2025-01-14 23 06 10](https://gist.github.com/user-attachments/assets/1ef6365d-a436-410f-87fc-4c6cac05fc83)


## 展開

```python
with st.expander('中身を見る'):
    st.write('expander の中身')
```

![スクリーンショット 2025-01-14 23 06 51](https://gist.github.com/user-attachments/assets/64dcd154-8287-4eb6-a5a9-26489aaab533)


## カラム分割

```python
col1, col2, col3, empty = st.columns([1,2,1,6])  # 比率を指定して分割
col1.write('カラム1に文字列を表示します')
col2.write(['カ', 'ラ', 'ム', '2'])
if col3.button('ボタン'):
    col3.write('ボタンがクリックされました')
```

![スクリーンショット 2025-01-14 22 22 23](https://gist.github.com/user-attachments/assets/4df3c7a6-777b-4020-9ed5-fda311086f35)


## サイドバー

```python
st.sidebar.write('サイドバー')
side_slider = st.sidebar.slider('width', 0, 100, 30)
```

![スクリーンショット 2025-01-14 22 50 58](https://gist.github.com/user-attachments/assets/d944d5b7-ffc4-426a-8556-59178b14e206)


## タブ

```python
tab_a, tab_b, tab_c = st.tabs(['A', 'B', 'C'])

with tab_a:
    st.write('This tab is A')

with tab_b:
    st.write('This tab is B')

with tab_c:
    st.write('This tab is C')
```

![スクリーンショット 2025-01-14 22 54 31](https://gist.github.com/user-attachments/assets/c5f4a34d-2964-4e93-a3cb-b10723b49e04)


## 処理が長引く場合の wait 表示

```python
import time

if st.button('Slow process'):
    with st.spinner('処理中です。しばらくお待ち下さい'):
        st.write('Processing...')
        time.sleep(3)
        st.write('Done!')
```

![スクリーンショット 2025-01-14 23 01 25](https://gist.github.com/user-attachments/assets/0e74499c-159b-410d-bb99-99453db47172)


## 空のウィジット

- 空っぽのウィジットを生成して場所を確保しておき、ボタン押下などのユーザ行動をトリガーにその位置に表示させる
- 作ってあったウィジットを画面から消す

といったことができる。

例えば以下の例では、
- 初期状態：数値を入力するフォームと「submit」ボタン
- ボタンを押下したとき：フォームの数値のみが画面に表示され、フォームとボタンは消失

```python
widget_out = st.empty()
widget_in = st.empty()
btn = st.empty()
num = widget_in.number_input('Input a number', value=0)
if btn.button('submit'):
    widget_in.empty()
    widget_out.write(num)
    btn.empty()
```
