import streamlit as st
import os
import MeCab
import collections
import io

def process_uploaded_files(uploaded_files):
    results = []
    
    # MeCabのインスタンスを作成
    m = MeCab.Tagger("-Owakati")
    
    for uploaded_file in uploaded_files:
        # ファイルの内容を読み込む
        text = uploaded_file.read().decode('utf-8')

        # 形態素解析を実施
        words = m.parse(text).split()

        # 単語の出現回数をカウント
        word_counts = collections.Counter(words)

        # カウント数の多い順に並べ替え
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        results.append((uploaded_file.name, sorted_word_counts))

    return results

# Streamlitアプリの作成
st.title("テキストファイル解析アプリ")

# ユーザーにファイルをアップロードしてもらう
uploaded_files = st.file_uploader("ファイルをアップロードしてください", type="txt", accept_multiple_files=True)

# ボタンがクリックされたら、ファイルの処理を実行
if st.button("ファイルを処理"):
    if uploaded_files:
        results = process_uploaded_files(uploaded_files)
        for file_name, word_counts in results:
            st.write(f"{file_name} の結果:")
            for word, count in word_counts:
                st.write(f"{word}: {count}")
    else:
        st.write("ファイルをアップロードしてください。")
