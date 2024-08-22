import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_garis():
    st.header("Diagram Garis")

    # Tampilkan uploader
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")

    # Tombol syarat dan ketentuan
    if st.button("Syarat dan Ketentuan"):
        st.write("Syarat dan ketentuan penggunaan aplikasi ini...")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi data dari CSV
        categories = df.iloc[:, 0]
        values = df.iloc[:, 1]
        
        # Membuat diagram garis
        fig, ax = plt.subplots()
        ax.plot(categories, values, marker='o')
        ax.set_title('Judul Diagram Garis')
        ax.set_xlabel('Kategori')
        ax.set_ylabel('Nilai')
        ax.grid(True)
        
        # Menampilkan angka detail di atas titik data
        for i, v in enumerate(values):
            ax.text(i, v + 0.5, str(v), ha='center')
        
        st.pyplot(fig)
