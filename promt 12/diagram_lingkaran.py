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

        # Ekstraksi kolom pertama sebagai nama irisan
        labels = df.iloc[:, 0].values
        values = df.iloc[:, 1].values

        # Format angka pada sumbu Y
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        st.pyplot(fig)

    # Tombol Pengertian
    if st.button("Pengertian"):
        st.write("Pengertian Diagram Lingkaran...")

    # Tombol Panduan Penggunaan
    if st.button("Panduan Penggunaan"):
        st.write("Panduan Penggunaan Diagram Lingkaran...")
    
    # Gambar visualisasi
    if uploaded_file:
        st.image(fig, caption="Diagram Lingkaran")
