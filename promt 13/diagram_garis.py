import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.sidebar.image("logo.png", use_column_width=True)  # Add your logo image
    st.title("Diagram Garis")

    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Line chart creation
        st.subheader("Line Chart")
        plt.figure(figsize=(10, 6))
        plt.plot(df[df.columns[0]], df[df.columns[1]], marker='o')
        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title('Line Chart')
        plt.grid(True)
        st.pyplot()

    # Additional buttons and text
    st.sidebar.button("Syarat dan Ketentuan")
