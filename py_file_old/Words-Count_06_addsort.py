import MeCab
import collections

# ユーザーにテキストファイルの名前を入力してもらう
file_name = input("テキストファイルの名前を入力してください（例: asahi.txt）: ")

# テキストファイルの内容を読み込む
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# MeCabのインスタンスを作成
m = MeCab.Tagger("-Owakati -r /opt/homebrew/etc/mecabrc")

# 形態素解析を実施
words = m.parse(text).split()

# 単語の出現回数をカウント
word_counts = collections.Counter(words)

# カウント数の多い順に並べ替え
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# 結果をテキストファイルに保存
output_file_name = "result_" + file_name
with open(output_file_name, "w", encoding="utf-8") as f:
    for word, count in sorted_word_counts:
        f.write(f"{word}: {count}\n")

print(f"結果を{output_file_name}に保存しました。")
