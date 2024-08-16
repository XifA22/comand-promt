import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_pie_chart_page():
    st.title("Diagram Lingkaran")

    # Tombol upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama sebagai nama irisan
        labels = df.iloc[:, 0].values
        
        # Membuat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(df.iloc[:, 1], labels=labels, autopct='%1.1f%%')
        st.pyplot(fig)
        
    # Tombol Pengertian dan Panduan Penggunaan
    st.button("Pengertian")
    st.button("Panduan Penggunaan")
    
    # Gambar visualisasi (placeholder untuk gambar)
    st.image("visualization_image.png", caption="Gambar Visualisasi")

