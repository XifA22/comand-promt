import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Visualisasi Data: Diagram Garis')

# Tombol upload file CSV
uploaded_file = st.file_uploader("Unggah file CSV Anda", type=["csv"])

if uploaded_file is not None:
    # Membaca file CSV
    data = pd.read_csv(uploaded_file)
    
    # Menampilkan beberapa baris data
    st.write("Data yang diunggah:")
    st.write(data.head())

    # Membuat diagram garis
    st.write("Diagram Garis:")
    plt.figure(figsize=(10, 6))
    
    for column in data.columns[1:]:
        plt.plot(data[data.columns[0]], data[column], label=column)

    plt.xlabel(data.columns[0])
    plt.ylabel('Nilai')
    plt.title('Diagram Garis')
    plt.legend(loc="upper left")
    plt.grid(True)
    
    # Menampilkan diagram garis
    st.pyplot(plt)
