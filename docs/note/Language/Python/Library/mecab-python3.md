---
title: mecab-python3
---

# mecab-python3 とは

形態素解析エンジン MeCab を Python で利用するためのパッケージ。

# 使い方

1. MeCab 本体のインストール
	1. [MeCab のノート](../../../NLP/morphological-analysis/mecab.md)を参照
2. mecab-python3 のインストール

```bash
pip install mecab-python3
```

## デフォルト

```python
import MeCab

text = "私は東京に住み、東京大学の情報学研究科で形態素解析の研究をしています。"

m1 = MeCab.Tagger()
print(m1.parse(text))
"""
私	名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
東京	名詞,固有名詞,地域,一般,*,*,東京,トウキョウ,トーキョー
に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
住み	動詞,自立,*,*,五段・マ行,連用形,住む,スミ,スミ
、	記号,読点,*,*,*,*,、,、,、
東京大学	名詞,固有名詞,組織,*,*,*,東京大学,トウキョウダイガク,トーキョーダイガク
の	助詞,連体化,*,*,*,*,の,ノ,ノ
情報	名詞,一般,*,*,*,*,情報,ジョウホウ,ジョーホー
学	名詞,接尾,一般,*,*,*,学,ガク,ガク
研究	名詞,サ変接続,*,*,*,*,研究,ケンキュウ,ケンキュー
科	名詞,接尾,一般,*,*,*,科,カ,カ
で	助詞,格助詞,一般,*,*,*,で,デ,デ
形態素	名詞,一般,*,*,*,*,形態素,ケイタイソ,ケイタイソ
解析	名詞,サ変接続,*,*,*,*,解析,カイセキ,カイセキ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
研究	名詞,サ変接続,*,*,*,*,研究,ケンキュウ,ケンキュー
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
て	助詞,接続助詞,*,*,*,*,て,テ,テ
い	動詞,非自立,*,*,一段,連用形,いる,イ,イ
ます	助動詞,*,*,*,特殊・マス,基本形,ます,マス,マス
。	記号,句点,*,*,*,*,。,。,。
EOS
"""
```

## 単語分かち書き

```python
m2 = MeCab.Tagger('-Owakati')
print(m2.parse(text))
# 私 は 東京 に 住み 、 東京大学 の 情報 学 研究 科 で 形態素 解析 の 研究 を し て い ます 。
print(m2.parse(text).split())
# ['私', 'は', '東京', 'に', '住み', '、', '東京大学', 'の', '情報', '学', '研究', '科', 'で', '形態素', '解析', 'の', '研究', 'を', 'し', 'て', 'い', 'ます', '。']
```

## 読み

```python
m3 = MeCab.Tagger('-Oyomi')
print(m3.parse(text))
# ワタシハトウキョウニスミ、トウキョウダイガクノジョウホウガクケンキュウカデケイタイソカイセキノケンキュウヲシテイマス。
```

## 表層文字列、読み、基本形、素性

```python
m4 = MeCab.Tagger("-Ochasen")
print(m4.parse(text).split())
# ['私', 'ワタシ', '私', '名詞-代名詞-一般', 'は', 'ハ', 'は', '助詞-係助詞', '東京', 'トウキョウ', '東京', '名詞-固有名詞-地域-一般', 'に', 'ニ', 'に', '助詞-格助詞-一般', '住み', 'スミ', '住む', '動詞-自立', '五段・マ行', '連用形', '、', '、', '、', '記号-読点', '東京大学', 'トウキョウダイガク', '東京大学', '名詞-固有名詞-組織', 'の', 'ノ', 'の', '助詞-連体化', '情報', 'ジョウホウ', '情報', '名詞-一般', '学', 'ガク', '学', '名詞-接尾-一般', '研究', 'ケンキュウ', '研究', '名詞-サ変接続', '科', 'カ', '科', '名詞-接尾-一般', 'で', 'デ', 'で', '助詞-格助詞-一般', '形態素', 'ケイタイソ', '形態素', '名詞-一般', '解析', 'カイセキ', '解析', '名詞-サ変接続', 'の', 'ノ', 'の', '助詞-連体化', '研究', 'ケンキュウ', '研究', '名詞-サ変接続', 'を', 'ヲ', 'を', '助詞-格助詞-一般', 'し', 'シ', 'する', '動詞-自立', 'サ変・スル', '連用形', 'て', 'テ', 'て', '助詞-接続助詞', 'い', 'イ', 'いる', '動詞-非自立', '一段', '連用形', 'ます', 'マス', 'ます', '助動詞', '特殊・マス', '基本形', '。', '。', '。', '記号-句点', 'EOS']
```


# トラブルシューティング

## ImportError: Symbol not found

MeCab を import する際に以下のようなエラーが出る場合の対応。

```python
>>> import MeCab

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.11/site-packages/MeCab/__init__.py", line 10, in <module>
    from . import _MeCab
ImportError: dlopen(/usr/local/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so, 2): Symbol not found: __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
  Referenced from: /usr/local/lib/python3.11/site-packages/MeCab/../mecab-python3.dylibs/libmecab.2.dylib (which was built for Mac OS X 12.0)
  Expected in: /usr/lib/libc++.1.dylib
```

`otool -L` コマンドを実行し、依存している共有ライブラリの名前とバージョンを確認：

```bash
$ otool -L /usr/local/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so

/usr/local/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so:
	@loader_path/../mecab-python3.dylibs/libmecab.2.dylib (compatibility version 3.0.0, current version 3.0.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 1300.23.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1311.100.3)
```

`ls /usr/lib | grep .dylib` で調べると、これら3つの `dylib` ファイルは存在しない。

→ `find / -name 'libmecab.dylib'` などのコマンドで場所を探す。

```bash
$ find / -name 'libmecab.dylib'
/usr/local/lib/libmecab.dylib
/usr/local/Cellar/mecab/0.996/lib/libmecab.dylib

$ find / -name 'libc++.1.dylib'
...

$ find / -name 'libSystem.B.dylib'
...
```

`install_name_tool` コマンドで正しいパスに置換：

```bash
install_name_tool -change "@loader_path/../mecab-python3.dylibs/libmecab.2.dylib" \
    /usr/local/lib/libmecab.dylib \
    /usr/local/lib/python3.11/site-packages/MeCab/_MeCab.cpython-311-darwin.so
```

※ 今回実際に起きたエラーでは `libc++.1.dylib`, `libSystem.B.dylib` は見つからなかったが、`libmecab.dylib` の書き換えだけで import できる & 使えるようになった。
