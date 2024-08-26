import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("Diagram Batang")

    uploaded_file = st.file_uploader("Upload file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        first_column = df.columns[0]
        year_column = st.selectbox('Pilih Tahun', df.columns[1:])  # Assuming the years are in subsequent columns
        
        data = df.groupby(first_column)[year_column].sum()
        
        # Create bar chart
        fig, ax = plt.subplots()
        data.plot(kind='bar', ax=ax)
        ax.set_title('Jumlah Populasi Berdasarkan Kategori')
        ax.set_xlabel(first_column)
        ax.set_ylabel('Jumlah')
        ax.grid(True)

        for index, value in enumerate(data):
            ax.text(index, value, str(value), ha='center', va='bottom')

        st.pyplot(fig)

if __name__ == "__main__":
    run()
