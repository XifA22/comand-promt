import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Garis")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

        # Buat diagram garis
        fig, ax = plt.subplots()
        for column in data.columns[1:]:
            ax.plot(data.iloc[:, 0], data[column], marker='o', label=column)
        ax.set_title("Diagram Garis")
        ax.set_xlabel("Waktu")
        ax.set_ylabel("Jumlah")
        ax.grid(True)
        st.pyplot(fig)
        
        # Tombol pengertian
        if st.button("Pengertian"):
            st.text("Pengertian dari diagram garis...")

        # Tombol panduan penggunaan
        if st.button("Panduan Penggunaan"):
            st.text("Panduan penggunaan untuk diagram garis...")
            st.image('path_to_image.png')
