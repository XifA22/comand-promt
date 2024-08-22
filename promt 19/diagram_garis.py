import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def halaman_diagram_garis():
    st.header("Diagram Garis")

    # Fitur upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # Ekstraksi kolom-kolom untuk membuat diagram garis
        categories = data.iloc[:, 0]
        values = data.iloc[:, 1]
        
        # Membuat diagram garis
        fig, ax = plt.subplots()
        ax.plot(categories, values, marker='o')
        ax.set_title("Judul Diagram Garis")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Nilai")
        ax.grid(True)
        
        # Menambahkan angka detail di atas data points
        for i, v in enumerate(values):
            ax.text(i, v + 0.1, str(v), ha='center')
        
        # Menampilkan visualisasi
        st.pyplot(fig)
    
    # Tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        st.write("Syarat dan Ketentuan...")
