import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Diagram Batang")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Ekstraksi kolom pertama dan tampilkan tahun
    years = data.iloc[:, 0]
    
    # Pilih tahun
    selected_year = st.selectbox("Pilih Tahun", years)
    
    # Plotting diagram batang vertikal
    fig, ax = plt.subplots()
    ax.bar(years, data[selected_year])
    ax.set_title("Judul Diagram Batang")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Populasi")
    ax.grid(True)
    st.pyplot(fig)

# Tombol Pengertian
if st.button("Pengertian"):
    st.text("Diagram batang digunakan untuk...")

# Tombol Panduan Penggunaan
if st.button("Panduan Penggunaan"):
    st.text("Panduan untuk menggunakan aplikasi ini...")
    st.image("path/to/image.png")  # Ganti path dengan lokasi gambar
