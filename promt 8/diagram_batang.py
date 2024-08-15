import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_batang():
    st.title("Diagram Batang")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview Data:", df.head())

        column_name = df.columns[0]
        years = df.columns[1:]

        selected_year = st.selectbox("Pilih Tahun:", years)
        population = df[selected_year]

        fig, ax = plt.subplots()
        ax.bar(df[column_name], population)

        ax.set_xlabel(column_name)
        ax.set_ylabel("Jumlah Penduduk")
        ax.set_title(f"Diagram Batang untuk Tahun {selected_year}")
        ax.grid(True)
        
        for i, v in enumerate(population):
            ax.text(i, v, str(v), ha='center', va='bottom')

        st.pyplot(fig)

if __name__ == "__main__":
    diagram_batang()
