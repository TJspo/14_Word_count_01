import MeCab
import collections

# テキストデータ
text = """今日は夕方には晴れたが予報は雨だった！"""

# MeCabのインスタンスを作成
# m = MeCab.Tagger("-Owakati")
m = MeCab.Tagger("-Owakati -r /opt/homebrew/etc/mecabrc")


# 形態素解析を実施
words = m.parse(text).split()

# 単語の出現回数をカウント
word_counts = collections.Counter(words)

# 結果をテキストファイルに保存
with open("result_02.txt", "w", encoding="utf-8") as f:
    for word, count in word_counts.items():
        f.write(f"{word}: {count}\n")

print("結果をresult.txtに保存しました。")
