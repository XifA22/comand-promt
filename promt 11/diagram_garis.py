# diagram_garis.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Garis")
    
    # Upload file CSV
    uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Membaca data dari CSV
        x = df.iloc[:, 0].tolist()  # Asumsikan kolom pertama adalah sumbu X
        y = df.iloc[:, 1].tolist()  # Asumsikan kolom kedua adalah sumbu Y
        
        # Format angka pada sumbu Y
        st.write("Format angka pada sumbu Y")
        
        # Tombol Syarat dan Ketentuan
        if st.button("Syarat dan Ketentuan"):
            st.write("Syarat dan ketentuan penggunaan aplikasi")
        
        # Membuat diagram garis
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_xlabel('Sumbu X')
        ax.set_ylabel('Sumbu Y')
        ax.set_title('Diagram Garis')
        ax.grid(True)
        
        # Menampilkan angka detail di titik-titik
        for i, txt in enumerate(y):
            ax.annotate(txt, (x[i], y[i]))
        
        st.pyplot(fig)

if __name__ == "__main__":
    main()
