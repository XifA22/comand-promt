import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Logo di pojok kanan atas
    logo = Image.open("path/to/logo.png")
    st.image(logo, use_column_width=True)

    # Uploader CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data:")
        st.write(df)

        # Ekstraksi kolom pertama
        labels = df.iloc[:, 0].values
        years = df.columns[1:].tolist()

        # Tampilkan dropdown untuk memilih tahun
        selected_year = st.selectbox("Pilih Tahun", years)
        values = df[selected_year].values

        # Buat diagram batang vertikal
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title(f"Diagram Batang {selected_year}")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        for i in range(len(values)):
            ax.text(i, values[i] + 1, str(values[i]), ha='center')
        st.pyplot(fig)

    # Tombol Pengertian
    if st.button("Pengertian"):
        st.write("Pengertian Diagram Batang...")

    # Tombol Panduan Penggunaan
    if st.button("Panduan Penggunaan"):
        st.write("Panduan Penggunaan Diagram Batang...")

    # Gambar visualisasi
    if uploaded_file:
        st.image(fig, caption="Diagram Batang")
