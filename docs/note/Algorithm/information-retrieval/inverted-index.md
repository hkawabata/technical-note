---
title: 転置インデックス
title-en: inverted index
---
# 概要

**転置インデックス** は、全文検索において、対象となる文書群から単語の位置情報を格納するための索引構造。

# 理論

$N$ 個の文章の集合 $D = \{d_1,d_2,d_3,\cdots,d_N\}$ と、それらに含まれる単語全ての集合 $W = \{w_1,w_2,w_3,\cdots,w_M\}$ を考える。

各文章ごとに含まれる単語を並べていくと、以下のような表が得られる（同じ単語が複数回現れる場合は省略している）。

```
d1: [w1, w2, w3, w4, w5]
d2: [w1, w2, w6, w7]
d3: [w4, w6, w8]
d4: [w2, w3, w4, w6, w8]
```

これは文章 ID をキーとして、その文章に含まれる単語一覧のリストを得る Map 構造になっている。  
ここで逆に単語に注目して、単語 ID をキーとして、その単語を含む文章一覧（**ポスティングリスト**）を並べたものを **転置インデックス** と呼ぶ：

```
w1: [d1, d2]
w2: [d1, d2, d4]
w3: [d1, d4]
w4: [d1, d3, d4]
w5: [d1]
w6: [d2, d3, d4]
w7: [d2]
w8: [d3, d4]
```

転置インデックスの実態は Map 構造であり、これを用いることで、指定された単語を含む文章の一覧をすぐに検索することができる。

例えば上の転置インデックスでクエリが $w_2, w_6$ の AND 検索（指定された全ての単語が存在するドキュメントを探す）を行う場合、以下の手順で検索結果を求められる。
1. $w_2$ のポスティングリスト $d_1,d_2,d_4$
2. $w_2$ のポスティングリスト $d_2,d_3,d_4$
3. 1,2の積集合を取って、検索結果は $d_2, d_4$


# 実装

```python
import re
import sklearn.datasets
import time
import numpy as np


class InvertedIndex:
    def __init__(self, articles):
        self.word2id = {}
        self.posting_list = []
        id_next = 0
        for id_article, a in enumerate(articles):
            words_added = set()
            words = self.preprocess_text(a)
            for w in words:
                if w not in self.word2id:
                    self.word2id[w] = id_next
                    self.posting_list.append([])
                    id_next += 1
                id_word = self.word2id[w]
                if id_word not in words_added:
                    self.posting_list[id_word].append(id_article)
                    words_added.add(id_word)
    def preprocess_text(self, text):
        """記号を削除して単語区切りにする"""
        words = re.sub(r'[,.!?:;\']', '', text).lower().split()
        return [w for w in words if re.fullmatch(r'[a-zA-Z]+', w)]
    def search_and(self, words, is_sort=True):
        """複数単語による AND 検索"""
        s = None
        for w in words:
            if w not in self.word2id:
                return []
            i = self.word2id[w]
            s2 = set(self.posting_list[i])
            s = s2 if s is None else s.intersection(s2)
        s = list(s)
        if is_sort:
            sort(s)
        return s
    def search_or(self, words, is_sort=True):
        """複数単語による OR 検索"""
        s = set()
        for w in words:
            if w in self.word2id:
                i = self.word2id[w]
                s2 = set(self.posting_list[i])
                s = s.union(s2)
        s = list(s)
        if is_sort:
            sort(s)
        return s
    def test_time(self, mode, n_query_max=10, T=100):
        t_ave = []
        t_std = []
        n_query = list(range(1, n_query_max+1))
        words_uniq = [w for w in self.word2id.keys()]
        for n in n_query:
            buff = []
            for _ in range(T):
                queries = []
                for i in np.random.choice(len(words_uniq), n, replace=False):
                    queries.append(words_uniq[i])
                start = time.time()
                if mode == 'AND':
                    self.search_and(queries, is_sort=False)
                elif mode == 'OR':
                    self.search_or(queries, is_sort=False)
                else:
                    raise ValueError('unknown mode: {}'.format(mode))
                end = time.time()
                buff.append(end-start)
            buff.sort()
            t_ave.append(np.mean(buff[T//10:-T//10]))
            t_std.append(np.std(buff[T//10:-T//10]))
        plt.plot(n_query, t_ave)
        plt.plot(n_query, t_std)
        plt.grid()
        plt.show()


data = sklearn.datasets.fetch_20newsgroups(subset='all')['data']
len(data)  # 18846
ii = InvertedIndex(data)

"""処理時間の計測"""
ii.test_time(mode='AND', T=500)
ii.test_time(mode='OR', T=500)

"""検索結果のテスト"""
res_and = ii.search_and(['soccer', 'baseball'])
res_or = ii.search_or(['soccer', 'baseball'])
res_soccer = ii.search_and(['soccer'])
res_baseball = ii.search_and(['baseball'])
print('A. AND(soccer) == OR(soccer):', ii.search_and(['soccer']) == ii.search_or(['soccer']))
print('B. AND(baseball) == OR(baseball):', ii.search_and(['baseball']) == ii.search_or(['baseball']))
print('A({}) + B({}) - A^B({}) == AvB({}): {}'.format(len(res_soccer), len(res_baseball), len(res_and), len(res_or), len(res_soccer)+len(res_baseball)-len(res_and)==len(res_or)))
"""
A. AND(soccer) == OR(soccer): True
B. AND(baseball) == OR(baseball): True
A(26) + B(414) - A^B(3) == AvB(437): True
"""
```
