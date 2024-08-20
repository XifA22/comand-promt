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
        values = df.iloc[:, 1].values

        # Buat diagram garis
        fig, ax = plt.subplots()
        ax.plot(labels, values, marker='o')
        ax.set_title("Diagram Garis")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        for i in range(len(values)):
            ax.text(i, values[i] + 1, str(values[i]), ha='center')
        st.pyplot(fig)

    # Tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        st.write("Syarat dan Ketentuan...")

    # Gambar visualisasi
    if uploaded_file:
        st.image(fig, caption="Diagram Garis")
