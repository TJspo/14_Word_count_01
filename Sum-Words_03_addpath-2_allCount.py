import os
import collections

# ユーザーにフォルダ名を入力させる
folder_path = input("結果ファイルが保存されているフォルダのパスを入力してください: ")

# フォルダ内の全てのファイルをリストアップ（拡張子が無くても対応）
# この部分が変更されました
txt_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 空のカウンタを作成
total_counts = collections.Counter()

# 各ファイルに対して処理を行う
for file in txt_files:
    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
        for line in f:
            word, count = line.split(": ")
            total_counts[word] += int(count)

# 結果を'combined_result.txt'という名前のファイルに保存
with open("combined_result.txt", "w", encoding="utf-8") as f:
    for word, count in total_counts.most_common():
        f.write(f"{word}: {count}\n")

print("合計結果をcombined_result.txtに保存しました。")
