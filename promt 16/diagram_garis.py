import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Diagram Garis")

    # Tombol Syarat dan Ketentuan
    if st.button("Syarat dan Ketentuan"):
        st.write("Syarat dan Ketentuan untuk penggunaan aplikasi ini...")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Ekstraksi data
        categories = df.iloc[:, 0]
        values = df.iloc[:, 1]

        # Visualisasi line chart
        fig, ax = plt.subplots()
        ax.plot(categories, values, marker='o')
        ax.set_title("Diagram Garis")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Jumlah")
        ax.grid(True)

        # Tambahkan angka detail di atas titik data
        for i, v in enumerate(values):
            ax.text(i, v + 0.5, str(v), ha='center')

        st.pyplot(fig)
