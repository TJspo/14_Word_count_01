import MeCab
import collections
import os

# ユーザにファイル名を入力させる
filename = input("解析したいtxtファイルの名前を入力してください（拡張子含む）: ")

# テキストデータの読み込み
with open(filename, 'r', encoding="utf-8") as file:
    text = file.read()

m = MeCab.Tagger("-Owakati -r /opt/homebrew/etc/mecabrc")

# 形態素解析を実施
words = m.parse(text).split()

# 単語の出現回数をカウント
word_counts = collections.Counter(words)

# 結果をテキストファイルに保存（元のファイル名に「_result」という接尾辞を付けて保存）
result_filename = os.path.splitext(filename)[0] + "_result.txt"
with open(result_filename, "w", encoding="utf-8") as f:
    for word, count in word_counts.items():
        f.write(f"{word}: {count}\n")

print(f"結果を{result_filename}に保存しました。")
