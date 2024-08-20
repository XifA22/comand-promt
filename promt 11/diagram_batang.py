# diagram_batang.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Batang")
    
    # Upload file CSV
    uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama
        labels = df.iloc[:, 0].tolist()
        values = df.iloc[:, 1].tolist()  # Asumsikan kolom kedua adalah nilai
        
        # Format angka pada sumbu Y
        st.write("Format angka pada sumbu Y")
        
        # Tombol Pengertian dan Panduan Penggunaan
        if st.button("Pengertian"):
            st.write("Penjelasan tentang Diagram Batang")
        
        if st.button("Panduan Penggunaan"):
            st.write("Panduan penggunaan untuk Diagram Batang")
        
        # Membuat diagram batang
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_xlabel('Tahun')
        ax.set_ylabel('Nilai')
        ax.set_title('Diagram Batang')
        ax.grid(True)
        
        # Menampilkan angka detail di atas batang
        for i, value in enumerate(values):
            ax.text(i, value + 0.1, str(value), ha='center')
        
        st.pyplot(fig)

if __name__ == "__main__":
    main()
