import collections

# 解析したい3週間分の結果ファイル名リスト
files = [input(f"週{i + 1}の結果ファイル名を入力してください（拡張子含む）: ") for i in range(3)]

word_counts_total = collections.Counter()

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            word, count = line.split(':')
            word_counts_total[word.strip()] += int(count.strip())

# 合計を保存
with open("total_result.txt", "w", encoding="utf-8") as f:
    for word, count in word_counts_total.items():
        f.write(f"{word}: {count}\n")

print("3週間分の合計をtotal_result.txtに保存しました。")
