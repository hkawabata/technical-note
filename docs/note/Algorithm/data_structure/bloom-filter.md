---
title: ブルームフィルタ
title-en: Bloom Filter
---

# 概要

あるデータが集合の要素である（集合に含まれている）かどうかの判定に使われる確率的データ構造。
空間効率が非常に良いが、**偽陽性**（= 実際には含まれていないのに含まれていると判定）を示す可能性がある。

# 仕組み

(ToDo)

<img width="600" alt="スクリーンショット 2023-09-07 23 26 40" src="https://user-images.githubusercontent.com/13412823/266348832-e40f367f-820e-47d5-baab-95ad7e37e932.png">


memo: [なぜ複数のハッシュ関数で1つの配列を使って良いのか？](https://stackoverflow.com/questions/49139960/why-bloom-filters-use-the-same-array-for-all-k-hashing-algorithms)
→ ハッシュ関数の個数が配列長より十分に小さければ問題にならない、らしい。別に複数配列を使ってもそれほど問題にならない気もするけど。

# 実装

{% gist 099780657962f1a7205d4b5259734a3c 20230907_bloom-filter.py %}

# 実験

## BloomFilter に登録済みの検索単語の割合を変える

![Figure_1](https://user-images.githubusercontent.com/13412823/266193182-747763e9-22fd-4f0d-979c-e79eff43eaa1.png)

- 確率的にハッシュ関数の衝突が起こり、偽陽性（BloomFilter に登録されたことがない単語に対して「存在する」と判定）を示す
- 登録済み単語が非常に少ない時：BloomFIlter は非常に疎であり、ハッシュ値の衝突が起こる頻度が非常に少ないため偽陽性率は低い
- 登録済み単語が非常に多い時：実際に登録済みの単語がほとんどであり、未登録単語が検索される回数自体が非常に少なく偽陽性率が低い

実験コード：

{% gist 099780657962f1a7205d4b5259734a3c ~1_word-add-rate.py %}


## フィルタのサイズを変える

![Figure_2](https://user-images.githubusercontent.com/13412823/266193191-07527904-c323-41bd-9171-76a25e57d4e2.png)

- フィルタのサイズが大きいほど、ハッシュ値がとりうる値が多いので、ハッシュ値の衝突が発生しにくくなって偽陽性率が下がる

実験コード：

{% gist 099780657962f1a7205d4b5259734a3c ~2_filter-size.py %}


## ハッシュ関数の個数を変える

![Figure_3](https://user-images.githubusercontent.com/13412823/266193197-563ee24f-51a4-4527-8620-9a0c2060003d.png)

- 偽陽性となるのは、「別単語に複数のハッシュ関数を適用した時、ハッシュ値が全て衝突する」とき
- なので使用するハッシュ関数を多くすると、BloomFilter がそれなりに疎（実験では全単語のうち2割を登録）であっても、急激に偽陽性率が下がる

実験コード：

{% gist 099780657962f1a7205d4b5259734a3c ~3_num-of-hash.py %}