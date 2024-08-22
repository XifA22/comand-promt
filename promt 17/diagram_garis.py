import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Diagram Garis")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Format angka pada sumbu Y dan buat diagram garis
    fig, ax = plt.subplots()
    ax.plot(data.iloc[:, 0], data.iloc[:, 1])
    ax.set_title("Judul Diagram Garis")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Populasi")
    ax.grid(True)
    st.pyplot(fig)

# Tombol Syarat dan Ketentuan
if st.button("Syarat dan Ketentuan"):
    st.text("Syarat dan ketentuan untuk aplikasi ini...")
