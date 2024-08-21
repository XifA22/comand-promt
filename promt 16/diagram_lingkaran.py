import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Diagram Lingkaran")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Ekstraksi kolom pertama sebagai nama irisan
        slice_names = df.iloc[:, 0]
        values = df.iloc[:, 1]

        # Visualisasi pie chart
        fig, ax = plt.subplots()
        ax.pie(values, labels=slice_names, autopct='%1.1f%%')
        st.pyplot(fig)

        # Tombol Pengertian
        if st.button("Pengertian"):
            st.write("Pengertian tentang diagram lingkaran...")

        # Tombol Panduan Penggunaan
        if st.button("Panduan Penggunaan"):
            st.write("Panduan tentang cara menggunakan aplikasi ini...")
            st.image("panduan.png")  # Gambar panduan penggunaan

