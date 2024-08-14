import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Halaman utama
def main():
    st.header('Visualisasi Data')
    
    if st.button('Lingkaran'):
        halaman_lingkaran()
    if st.button('Batang'):
        halaman_batang()
    if st.button('Garis'):
        halaman_garis()

# Halaman Lingkaran
def halaman_lingkaran():
    st.title('Visualisasi Lingkaran')

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        column_name = df.columns[0]
        values = df[column_name].value_counts()

        fig, ax = plt.subplots()
        values.plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_ylabel('')
        st.pyplot(fig)

    if st.button('Pengertian'):
        st.info('Visualisasi lingkaran digunakan untuk menggambarkan proporsi data dalam bentuk irisan lingkaran.')

    if st.button('Panduan Penggunaan'):
        st.info('Panduan untuk menggunakan aplikasi ini.')

    st.image('visualisasi_data_lingkaran.png', caption='Visualisasi Data')

# Halaman Batang
def halaman_batang():
    st.title('Visualisasi Batang')

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        column_name = df.columns[0]
        values = df[column_name].value_counts()
        years = df['Year'].unique()

        selected_year = st.selectbox('Pilih Tahun', years)
        population = df[df['Year'] == selected_year][column_name].sum()

        fig, ax = plt.subplots()
        ax.bar(values.index, values.values)
        ax.set_title('Diagram Batang Vertikal')
        ax.set_xlabel('Kategori')
        ax.set_ylabel('Jumlah')
        ax.grid(True)

        for i, v in enumerate(values.values):
            ax.text(i, v + 0.2, str(v), ha='center')

        st.pyplot(fig)

# Halaman Garis
def halaman_garis():
    st.title('Visualisasi Garis')

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        column_name = df.columns[0]
        values = df.groupby('Year')[column_name].sum()

        fig, ax = plt.subplots()
        ax.plot(values.index, values.values, marker='o')
        ax.set_title('Diagram Garis')
        ax.set_xlabel('Tahun')
        ax.set_ylabel('Jumlah')
        ax.grid(True)

        for i, v in enumerate(values.values):
            ax.text(i, v + 0.2, str(v), ha='center')

        st.pyplot(fig)

if __name__ == '__main__':
    main()
