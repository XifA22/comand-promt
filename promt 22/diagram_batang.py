import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_batang():
    st.sidebar.title("Diagram Batang")
    st.sidebar.button("Kembali ke Halaman Utama", on_click=lambda: st.experimental_set_query_params())

    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        kolom_pertama = data.iloc[:, 0]

        tahun = st.selectbox("Pilih Tahun", data.columns[1:])
        if tahun:
            nilai = data[tahun]

            fig, ax = plt.subplots()
            ax.bar(kolom_pertama, nilai)
            ax.set_title(f"Diagram Batang Tahun {tahun}")
            ax.set_xlabel("Kategori")
            ax.set_ylabel("Nilai")
            for i, v in enumerate(nilai):
                ax.text(i, v + 1, str(v), ha='center')
            st.pyplot(fig)

if __name__ == "__main__":
    diagram_batang()
