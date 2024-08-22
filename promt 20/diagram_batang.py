import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_diagram_batang():
    st.header("Diagram Batang")

    # Upload file CSV
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama
        categories = df.iloc[:, 0]
        values = df.iloc[:, 1]
        
        # Membuat diagram batang vertikal
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_title('Judul Diagram Batang')
        ax.set_xlabel('Kategori')
        ax.set_ylabel('Nilai')
        ax.grid(True)
        
        # Menampilkan angka detail di atas batang
        for i, v in enumerate(values):
            ax.text(i, v + 0.5, str(v), ha='center')
        
        st.pyplot(fig)
