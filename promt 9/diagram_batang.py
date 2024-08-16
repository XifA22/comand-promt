import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_batang_page():
    st.header("Diagram Batang")

    # Tombol Upload
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        # Membaca file CSV
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama sebagai nama batang
        labels = df.iloc[:, 0]
        years = df.columns[1:]  # Kolom tahun

        selected_year = st.selectbox('Pilih Tahun', years)
        data = df[selected_year]

        # Membuat diagram batang vertikal
        fig, ax = plt.subplots()
        ax.bar(labels, data)
        ax.set_title(f"Diagram Batang untuk Tahun {selected_year}")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)

        # Menambahkan angka di atas batang
        for i, v in enumerate(data):
            ax.text(i, v + 0.1, str(v), ha='center')

        st.pyplot(fig)
