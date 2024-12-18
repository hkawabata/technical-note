# 自然言語処理

## 長い文章

### Project Gutenberg

著作権切れ？の書籍データ。

```python
from urllib import request

url = 'https://www.gutenberg.org/cache/epub/74913/pg74913.txt'
books = {
    'alice': 'https://www.gutenberg.org/cache/epub/11/pg11.txt',
    'gulliver': 'https://www.gutenberg.org/cache/epub/829/pg829.txt'
}


def read_raw_novel(url):
    with request.urlopen(request.Request(url)) as res:
        body = res.read()
        words = body.decode('utf-8').split()
        words_norm = [w.lower() for w in words if re.fullmatch(r'[a-zA-Z]+', w)]
        cnt = {}
        for w in words_norm:
            cnt[w] = cnt.get(w, 0) + 1
        cnt_sorted = sorted([(w, n) for w, n in cnt.items()], key=lambda x: x[1])
        print(cnt_sorted[-100:])


read_raw_novel(books['alice'])
read_raw_novel(books['gulliver'])
```

## ニュース記事分類の学習データセット

### News classification dataset for NLP

https://www.kaggle.com/datasets/alessandrolobello/guardian

### sklearn.datasets.fetch_20newsgroups

```python
import sklearn.datasets

data = sklearn.datasets.fetch_20newsgroups(subset='train')['data']
data_words = [text.split() for text in data]
plt.xlabel('Words')
plt.ylabel('Articles')
plt.hist([len(words) for words in data_words], bins=500)
plt.xlim((0,2000))
plt.show()
```

![Figure_1](https://gist.github.com/user-attachments/assets/8256059e-23b5-44e9-95f3-de44844250a7)
