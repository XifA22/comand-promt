import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_garis_page():
    st.header("Diagram Garis")

    # Tombol Upload
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        # Membaca file CSV
        df = pd.read_csv(uploaded_file)

        # Ekstraksi kolom data
        labels = df.iloc[:, 0]
        data = df.iloc[:, 1]

        # Membuat diagram garis
        fig, ax = plt.subplots()
        ax.plot(labels, data, marker='o')
        ax.set_title("Diagram Garis")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)

        # Menambahkan angka di atas data poin
        for i, v in enumerate(data):
            ax.text(i, v + 0.1, str(v), ha='center')

        st.pyplot(fig)

    # Tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        st.write("Teks syarat dan ketentuan di sini...")
