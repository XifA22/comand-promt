import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_lingkaran():
    st.title("Diagram Lingkaran")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if data.shape[1] < 2:
            st.error("CSV harus memiliki setidaknya dua kolom.")
        else:
            # Ekstraksi kolom pertama
            slice_names = data.iloc[:, 0]
            values = data.iloc[:, 1]

            fig, ax = plt.subplots()
            ax.pie(values, labels=slice_names, autopct='%1.1f%%')
            plt.axis('equal')  # Untuk membuat lingkaran proporsional
            st.pyplot(fig)

            if st.button("Pengertian"):
                st.write("Diagram lingkaran adalah representasi grafis dari data dalam bentuk lingkaran yang dibagi menjadi beberapa bagian.")

            if st.button("Panduan Penggunaan"):
                st.write("Panduan penggunaan: Upload file CSV yang berisi nama irisan dan nilai yang ingin divisualisasikan.")

            # Gambar visualisasi (jika ada)
            st.image("visualisasi_lingkaran.png")  # Gantilah dengan gambar visualisasimu

if __name__ == "__main__":
    diagram_lingkaran()
