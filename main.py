import streamlit as st
import pandas as pd
import random

def generate_sample_data(n=5):
    titles = [
        "【プログラミング入門】Python基礎講座",
        "AIの最新トレンド2024年版",
        "データサイエンスで稼ぐ方法",
        "機械学習エンジニアになるためのロードマップ",
        "プログラミングで人生が変わった話",
        "初心者向けWebアプリ開発講座",
        "プログラマーの1日に密着",
        "コーディング面接対策講座"
    ]
    
    data = []
    for _ in range(n):
        title = random.choice(titles)
        url = f"https://www.youtube.com/watch?v={''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=11))}"
        views = random.randint(1000, 1000000)
        likes = random.randint(100, 10000)
        comments = random.randint(10, 1000)
        
        data.append({
            "タイトル": title,
            "URL": url,
            "再生回数": views,
            "高評価数": likes,
            "コメント数": comments
        })
    
    return pd.DataFrame(data)

def main():
    st.set_page_config(page_title="kamui Intelligence", layout="wide")

    # サイドバー
    with st.sidebar:
        st.header("設定")
        
        # テーマ選択
        theme = st.selectbox("テーマ", ["ライト", "ダーク"])
        
        # 言語選択
        language = st.selectbox("言語", ["日本語", "English"])
        
        # 通知設定
        notifications = st.checkbox("通知を受け取る")
        
        # バージョン情報
        st.text("Version: 1.0.0")

    st.title("kamui Intelligence")

    # CSVアップロードエリア
    st.header("CSVアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

    # フォーム
    st.header("フォーム")
    with st.form("input_form"):
        # 関連キーワード入力エリア
        keywords = st.text_input("関連キーワードを入力してください")

        # 参考動画数を決める部分
        video_count = st.number_input("参考動画数", min_value=1, max_value=100, value=10)

        # フリーのテキストボックス
        free_text = st.text_area("自由記述欄", height=200)

        # 送信ボタン
        submitted = st.form_submit_button("送信")

    if submitted:
        st.success("フォームが送信されました！")
        st.write("入力された内容:")
        st.write(f"関連キーワード: {keywords}")
        st.write(f"参考動画数: {video_count}")
        st.write(f"自由記述: {free_text}")

        # サンプルのYouTube動画データを生成
        df = generate_sample_data(video_count)

        # データフレームを表示
        st.subheader("関連YouTube動画 (サンプルデータ)")
        st.dataframe(df)

        # 詳細な統計情報
        st.subheader("動画統計")
        st.write(f"総再生回数: {df['再生回数'].sum():,}")
        st.write(f"平均再生回数: {df['再生回数'].mean():,.0f}")
        st.write(f"最も人気のある動画: {df.loc[df['再生回数'].idxmax(), 'タイトル']}")

if __name__ == "__main__":
    main()
