import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def halaman_diagram_lingkaran():
    st.header("Diagram Lingkaran")

    # Fitur upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # Ekstraksi kolom pertama sebagai nama irisan
        names = data.iloc[:, 0]
        values = data.iloc[:, 1]
        
        # Membuat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(values, labels=names, autopct='%1.1f%%')
        ax.axis('equal')
        
        # Menampilkan visualisasi
        st.pyplot(fig)
    
    # Tombol Pengertian
    if st.button("Pengertian"):
        st.write("Pengertian dari diagram lingkaran...")
    
    # Tombol Panduan Penggunaan
    if st.button("Panduan Penggunaan"):
        st.write("Panduan penggunaan dari diagram lingkaran...")
        st.image("path_to_guide_image.png", width=300)
