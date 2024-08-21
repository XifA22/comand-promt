import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_batang():
    st.title("Diagram Batang")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if data.shape[1] < 2:
            st.error("CSV harus memiliki setidaknya dua kolom.")
        else:
            # Ekstraksi kolom pertama dan tampilkan pilihan tahun
            options = st.selectbox("Pilih Tahun", data.columns[1:])
            selected_year = data[options]

            fig, ax = plt.subplots()
            ax.bar(data.iloc[:, 0], selected_year)
            ax.set_title("Diagram Batang")
            ax.set_xlabel("Kategori")
            ax.set_ylabel("Nilai")
            ax.grid(True)

            # Tambahkan angka detail di atas batang
            for i in range(len(selected_year)):
                ax.text(i, selected_year[i], str(selected_year[i]), ha='center')

            st.pyplot(fig)

if __name__ == "__main__":
    diagram_batang()
