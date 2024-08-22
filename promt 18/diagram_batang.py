import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Batang")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        
        years = st.selectbox("Pilih Tahun", data.columns[1:])
        values = data[years]
        labels = data.iloc[:, 0]

        # Buat diagram batang
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Diagram Batang")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        st.pyplot(fig)
        
        # Tombol pengertian
        if st.button("Pengertian"):
            st.text("Pengertian dari diagram batang...")

        # Tombol panduan penggunaan
        if st.button("Panduan Penggunaan"):
            st.text("Panduan penggunaan untuk diagram batang...")
            st.image('path_to_image.png')

