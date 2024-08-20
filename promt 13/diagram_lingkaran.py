import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.sidebar.image("logo.png", use_column_width=True)  # Add your logo image
    st.title("Diagram Lingkaran")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        slice_names = df.iloc[:, 0].tolist()
        
        # Example pie chart creation
        st.subheader("Pie Chart")
        plt.figure(figsize=(10, 6))
        plt.pie(df[df.columns[0]], labels=slice_names, autopct='%1.1f%%')
        st.pyplot()
    
    # Additional buttons and text
    st.sidebar.button("Pengertian")
    st.sidebar.button("Panduan Penggunaan")
