import os
import collections

# ユーザーにフォルダ名を入力させる
folder_path = input("結果ファイルが保存されているフォルダのパスを入力してください: ")

# フォルダ内の全てのファイルをリストアップ
txt_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 空のカウンタを作成
appearance_counts = collections.Counter()

# 各ファイルに対して処理を行う
for file in txt_files:
    # この単語がこのファイルに現れたかを記録するセットを初期化
    appeared_in_file = set()

    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
        for line in f:
            word = line.split(": ")[0]
            appeared_in_file.add(word)
            
    for word in appeared_in_file:
        appearance_counts[word] += 1

# 結果を'combined_appearance.txt'という名前のファイルに保存
with open("combined_appearance.txt", "w", encoding="utf-8") as f:
    for word, count in appearance_counts.most_common():
        f.write(f"{word}: {count}\n")

print("出現ファイル数をcombined_appearance.txtに保存しました。")
