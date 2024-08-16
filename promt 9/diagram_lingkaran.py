import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_lingkaran_page():
    st.header("Diagram Lingkaran")

    # Tombol Upload
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file:
        # Membaca file CSV
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama sebagai nama irisan
        labels = df.iloc[:, 0]
        sizes = df.iloc[:, 1]

        # Membuat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')

        st.pyplot(fig)

    # Tombol Pengertian dan Panduan Penggunaan
    st.button("Pengertian")
    st.button("Panduan Penggunaan")

    # Gambar visualisasi
    st.image("visualisasi.png", caption="Contoh Visualisasi Diagram Lingkaran")

