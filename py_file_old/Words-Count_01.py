import MeCab
import collections

# テキストデータ
text = """今日は晴れた！"""

# MeCabのインスタンスを作成
m = MeCab.Tagger("-Owakati")

# 形態素解析を実施
words = m.parse(text).split()
m = MeCab.Tagger("-r /opt/homebrew/etc/mecabrc -Owakati")

# 単語の出現回数をカウント
word_counts = collections.Counter(words)

print(word_counts)
