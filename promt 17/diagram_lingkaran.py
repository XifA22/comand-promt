import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Diagram Lingkaran")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Ekstraksi kolom pertama sebagai nama irisan
    names = data.iloc[:, 0]
    
    # Plotting diagram lingkaran
    fig, ax = plt.subplots()
    ax.pie(data.iloc[:, 1], labels=names, autopct='%1.1f%%')
    st.pyplot(fig)

# Tombol Pengertian
if st.button("Pengertian"):
    st.text("Diagram lingkaran digunakan untuk...")

# Tombol Panduan Penggunaan
if st.button("Panduan Penggunaan"):
    st.text("Panduan untuk menggunakan aplikasi ini...")
    st.image("path/to/image.png")  # Ganti path dengan lokasi gambar

# Visualisasi
st.image("path/to/visualisasi.png")  # Ganti path dengan lokasi gambar visualisasi
