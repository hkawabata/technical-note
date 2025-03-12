# gensim とは

最新の統計的機械学習を使用した、教師なしトピックモデリングと自然言語処理のためのライブラリ。

# 使い方

```bash
pip install gensim
```

## モデルの学習

### Word2Vec

```python
from gensim.test.utils import common_texts
from gensim.models import Word2Vec

sample_texts = [
    ['I', 'say', 'hello', 'to', 'him' '.'],
    ['You', 'say', 'goodbye', 'to', 'her', '.']
]
model = Word2Vec(sentences=sample_texts, vector_size=2, window=2, min_count=1)

model.wv['hello']
# array([-0.24300802, -0.09080088], dtype=float32)
model.wv.index_to_key
# ['to', 'say', '.', 'her', 'goodbye', 'You', 'him.', 'hello', 'I']
model.wv.vectors
"""
array([[-0.02681136,  0.01182157],
       [ 0.25516748,  0.45046365],
       [-0.4651475 , -0.35584044],
       [ 0.32294363,  0.4486494 ],
       [-0.2507714 , -0.18816859],
       [ 0.36902523, -0.07667357],
       [-0.22683066,  0.32770258],
       [-0.24300802, -0.09080088],
       [ 0.14382899,  0.04959369]], dtype=float32)
"""

for w in model.wv.index_to_key:
    print(model.wv[w], w)

"""
[-0.02681136  0.01182157] to
[0.25516748 0.45046365] say
[-0.4651475  -0.35584044] .
[0.32294363 0.4486494 ] her
[-0.2507714  -0.18816859] goodbye
[ 0.36902523 -0.07667357] You
[-0.22683066  0.32770258] him.
[-0.24300802 -0.09080088] hello
"""
```