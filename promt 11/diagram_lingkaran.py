# diagram_lingkaran.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Diagram Lingkaran")
    
    # Upload file CSV
    uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Ekstraksi kolom pertama sebagai nama irisan
        labels = df.iloc[:, 0].tolist()
        sizes = [1] * len(labels)  # Dummy sizes for demonstration, replace with actual data
        
        # Format angka pada sumbu Y
        st.write("Format angka pada sumbu Y")
        
        # Tombol Pengertian dan Panduan Penggunaan
        if st.button("Pengertian"):
            st.write("Penjelasan tentang Diagram Lingkaran")
        
        if st.button("Panduan Penggunaan"):
            st.write("Panduan penggunaan untuk Diagram Lingkaran")
        
        # Membuat diagram lingkaran
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        st.pyplot(fig)

if __name__ == "__main__":
    main()
