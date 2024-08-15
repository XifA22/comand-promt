import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_garis():
    st.title("Diagram Garis")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview Data:", df.head())

        x = df.iloc[:, 0]
        y = df.iloc[:, 1]

        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')

        ax.set_xlabel(df.columns[0])
        ax.set_ylabel("Jumlah Penduduk")
        ax.set_title("Diagram Garis")
        ax.grid(True)
        
        for i, v in enumerate(y):
            ax.text(i, v, str(v), ha='center', va='bottom')

        st.pyplot(fig)

    if st.button('Syarat dan Ketentuan'):
        st.write("Syarat dan Ketentuan: ...")

if __name__ == "__main__":
    diagram_garis()
