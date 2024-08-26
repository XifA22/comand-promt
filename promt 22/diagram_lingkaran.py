import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_lingkaran():
    st.sidebar.title("Diagram Lingkaran")
    st.sidebar.button("Kembali ke Halaman Utama", on_click=lambda: st.experimental_set_query_params())

    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        kolom_pertama = data.iloc[:, 0]

        fig, ax = plt.subplots()
        ax.pie(data.iloc[:, 1], labels=kolom_pertama, autopct='%1.1f%%')
        st.pyplot(fig)

        st.button("Pengertian", on_click=lambda: st.write("Pengertian diagram lingkaran..."))
        st.button("Panduan Penggunaan", on_click=lambda: st.write("Panduan penggunaan..."))
        st.image("visualisasi.png", caption="Visualisasi Diagram Lingkaran")

if __name__ == "__main__":
    diagram_lingkaran()
