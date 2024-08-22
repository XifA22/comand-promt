import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def halaman_diagram_batang():
    st.header("Diagram Batang")

    # Fitur upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # Ekstraksi kolom pertama sebagai nama kategori
        categories = data.iloc[:, 0]
        values = data.iloc[:, 1]
        
        # Membuat diagram batang vertikal
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title("Judul Diagram Batang")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Nilai")
        ax.grid(True)
        
        # Menambahkan angka detail di atas batang
        for i, v in enumerate(values):
            ax.text(i, v + 0.1, str(v), ha='center')
        
        # Menampilkan visualisasi
        st.pyplot(fig)
