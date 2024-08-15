import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_lingkaran():
    st.title("Diagram Lingkaran")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    st.button("Pengertian")
    st.button("Panduan Penggunaan")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview Data:", df.head())

        column_name = df.columns[0]
        values = df[column_name].value_counts()

        fig, ax = plt.subplots()
        ax.pie(values, labels=values.index, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

    st.image("path/to/your/visualization_image.png")

if __name__ == "__main__":
    diagram_lingkaran()
