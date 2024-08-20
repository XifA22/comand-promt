import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.sidebar.image("logo.png", use_column_width=True)  # Add your logo image
    st.title("Diagram Batang")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        years = df[df.columns[0]].unique()
        
        # Year selection
        year = st.selectbox("Pilih Tahun", options=years)
        data = df[df[df.columns[0]] == year]

        # Bar chart creation
        st.subheader("Bar Chart")
        plt.figure(figsize=(10, 6))
        plt.bar(data.index, data[data.columns[1]])
        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title(f'Bar Chart for {year}')
        plt.grid(True)
        st.pyplot()

    # Additional buttons and text
    st.sidebar.button("Pengertian")
    st.sidebar.button("Panduan Penggunaan")
