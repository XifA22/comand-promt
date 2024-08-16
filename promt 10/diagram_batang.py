import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_bar_chart_page():
    st.title("Diagram Batang")

    # Tombol upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama
        labels = df.iloc[:, 0].values
        years = df.columns[1:]

        # Pilih tahun
        selected_year = st.selectbox("Pilih Tahun", years)
        data = df[selected_year].values
        
        # Membuat diagram batang vertikal
        fig, ax = plt.subplots()
        ax.bar(labels, data)
        ax.set_title("Diagram Batang Vertikal")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        
        # Menampilkan angka detail di atas batang
        for i, v in enumerate(data):
            ax.text(i, v + 0.5, str(v), ha='center')
        
        st.pyplot(fig)
