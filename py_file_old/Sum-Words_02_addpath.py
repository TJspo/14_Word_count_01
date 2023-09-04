import os
import collections

# ユーザーに結果ファイルが保存されているフォルダ名を入力してもらう
folder_path = input("結果ファイルが保存されているフォルダ名を入力してください: ")

# 指定したフォルダ内のファイル一覧を取得
files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

word_count_sum = collections.Counter()

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            word, count = line.strip().split(': ')
            word_count_sum[word] += int(count)

sorted_word_counts = word_count_sum.most_common()

# 合計結果をテキストファイルに保存
output_file_name = "combined_result.txt"
with open(output_file_name, "w", encoding="utf-8") as f:
    for word, count in sorted_word_counts:
        f.write(f"{word}: {count}\n")

print(f"結果を{output_file_name}に保存しました。")
