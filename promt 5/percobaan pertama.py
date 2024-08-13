import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to create visualizations
def create_visualization(data, chart_type):
    fig, ax = plt.subplots()
    if chart_type == 'lingkaran':
        ax.pie(data.iloc[:, 1], labels=data.iloc[:, 0], autopct='%1.1f%%')
    elif chart_type == 'batang':
        ax.bar(data.iloc[:, 0], data.iloc[:, 1])
    elif chart_type == 'garis':
        ax.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o')

    st.pyplot(fig)

# Main page
st.title("Visualisasi Data")
st.header("Pilih Tipe Visualisasi")

if st.button("Lingkaran"):
    st.session_state.page = "lingkaran"
if st.button("Batang"):
    st.session_state.page = "batang"
if st.button("Garis"):
    st.session_state.page = "garis"

# Navigation
if "page" in st.session_state:
    if st.session_state.page in ["lingkaran", "batang", "garis"]:
        st.header(f"Visualisasi Data - {st.session_state.page.capitalize()}")
        
        # Buttons
        st.button("Pengertian")
        st.button("Panduan Penggunaan")

        # Upload CSV
        uploaded_file = st.file_uploader("Upload CSV", type="csv")

        if uploaded_file:
            data = pd.read_csv(uploaded_file)

            # Ensure first column as slice names and numbers on Y-axis
            st.write("Data Preview:")
            st.write(data.head())

            # Visualization
            create_visualization(data, st.session_state.page)
