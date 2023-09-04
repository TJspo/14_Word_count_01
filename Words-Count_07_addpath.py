import MeCab
import collections
import os

# ユーザーにフォルダのパスを入力してもらう
folder_path = input("フォルダのパスを入力してください（例: ./articles/）: ")

# 指定されたフォルダ内の全てのファイルを取得
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# MeCabのインスタンスを作成
m = MeCab.Tagger("-Owakati -r /opt/homebrew/etc/mecabrc")

for file_name in files:
    # ファイルの内容を読み込む
    with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
        text = f.read()

    # 形態素解析を実施
    words = m.parse(text).split()

    # 単語の出現回数をカウント
    word_counts = collections.Counter(words)

    # カウント数の多い順に並べ替え
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # 結果をテキストファイルに保存
    output_file_name = os.path.join(folder_path, "result_" + file_name)
    with open(output_file_name, "w", encoding="utf-8") as f:
        for word, count in sorted_word_counts:
            f.write(f"{word}: {count}\n")

    print(f"{file_name} の結果を {output_file_name} に保存しました。")
