import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Diagram Batang")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Ekstraksi kolom pertama sebagai nama kategori
        categories = df.iloc[:, 0]
        years = df.columns[1:]  # Ambil tahun dari kolom

        # Pilih tahun untuk ditampilkan
        year = st.selectbox("Pilih Tahun", years)
        values = df[year]

        # Visualisasi bar chart
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title(f"Diagram Batang {year}")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)

        # Tambahkan angka detail di atas batang
        for i, v in enumerate(values):
            ax.text(i, v + 0.5, str(v), ha='center')

        st.pyplot(fig)
