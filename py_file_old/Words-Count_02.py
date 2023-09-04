import MeCab
import collections

# テキストデータ
text = """今日は晴れた！"""

# MeCabのインスタンスを作成（mecabrcの場所を指定）
m = MeCab.Tagger("-Owakati -r /opt/homebrew/etc/mecabrc")

# 形態素解析を実施
words = m.parse(text).split()

# 単語の出現回数をカウント
word_counts = collections.Counter(words)

print(word_counts)

