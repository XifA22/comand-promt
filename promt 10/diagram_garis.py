import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_line_chart_page():
    st.title("Diagram Garis")

    # Tombol upload file CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi data
        labels = df.iloc[:, 0].values
        data = df.iloc[:, 1:].values

        # Membuat diagram garis
        fig, ax = plt.subplots()
        for i in range(data.shape[1]):
            ax.plot(labels, data[:, i], marker='o', label=df.columns[i+1])
        
        ax.set_title("Diagram Garis")
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        ax.legend()
        
        # Menampilkan angka detail di atas titik data
        for i in range(len(labels)):
            for j in range(data.shape[1]):
                ax.text(labels[i], data[i, j], str(data[i, j]), ha='center', va='bottom')
        
        st.pyplot(fig)
    
    # Tombol Syarat dan Ketentuan
    st.button("Syarat dan Ketentuan")
