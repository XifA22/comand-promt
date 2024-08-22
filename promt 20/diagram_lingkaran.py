import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_lingkaran():
    st.header("Diagram Lingkaran")
    
    # Upload file CSV
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama sebagai nama irisan
        slice_names = df.iloc[:, 0]
        values = df.iloc[:, 1]
        
        # Membuat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(values, labels=slice_names, autopct='%1.1f%%')
        plt.axis('equal')
        st.pyplot(fig)
    
    # Tombol Pengertian
    if st.button("Pengertian"):
        st.write("Ini adalah diagram lingkaran yang menampilkan proporsi dari data yang diupload.")

    # Tombol Panduan Penggunaan
    if st.button("Panduan Penggunaan"):
        st.write("Panduan untuk menggunakan aplikasi ini:")
        st.image("panduan_gambar.png")

    # Visualisasi Gambar (misalnya gambar hasil visualisasi)
    st.image("visualisasi_diagram_lingkaran.png")
