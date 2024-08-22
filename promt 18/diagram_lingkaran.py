import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Lingkaran")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        slice_names = data.iloc[:, 0]
        values = data.iloc[:, 1]

        # Buat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(values, labels=slice_names, autopct='%1.1f%%')
        st.pyplot(fig)
        
        # Tombol pengertian
        if st.button("Pengertian"):
            st.text("Pengertian dari diagram lingkaran...")

        # Tombol panduan penggunaan
        if st.button("Panduan Penggunaan"):
            st.text("Panduan penggunaan untuk diagram lingkaran...")
            st.image('path_to_image.png')

