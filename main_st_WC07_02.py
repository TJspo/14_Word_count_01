import streamlit as st
import os
import MeCab
import collections

def process_files(folder_path):
    # フォルダ内の全てのファイルを取得
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    results = []
    
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

        results.append(f"{file_name} の結果を {output_file_name} に保存しました。")
        # st.write(sorted_word_counts)  # 結果を表示

    return results

# Streamlitアプリの作成
st.title("フォルダ内のテキストファイル解析アプリ")

# ユーザー入力の取得
folder_path = st.text_input("フォルダのパスを入力してください：")

# ボタンがクリックされたら、ファイルの処理を実行
if st.button("ファイルを処理"):
    if folder_path:
        results = process_files(folder_path)
        for result in results:
            st.write(result)
    else:
        st.write("フォルダのパスを正しく入力してください。")
