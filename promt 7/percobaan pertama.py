import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan format angka pada sumbu y
def format_y_axis(ax):
    for label in ax.get_yticklabels():
        label.set_text(f'{int(float(label.get_text())):,}')

# Halaman Utama
def main():
    st.header('Visualisasi Data')

    if st.button('Lingkaran'):
        show_pie_chart_page()
    elif st.button('Batang'):
        show_bar_chart_page()
    elif st.button('Garis'):
        show_line_chart_page()

# Halaman Lingkaran
def show_pie_chart_page():
    st.title('Halaman Lingkaran')
    
    uploaded_file = st.file_uploader('Upload CSV', type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if not df.empty:
            slice_names = df.iloc[:, 0].tolist()
            values = df.iloc[:, 1].tolist()

            fig, ax = plt.subplots()
            ax.pie(values, labels=slice_names, autopct='%1.1f%%')
            st.pyplot(fig)

    if st.button('Pengertian'):
        st.write('Ini adalah penjelasan mengenai diagram lingkaran.')
    
    if st.button('Panduan Penggunaan'):
        st.write('Panduan penggunaan untuk halaman lingkaran.')

    st.image('https://via.placeholder.com/600x400', caption='Contoh Visualisasi Data')

# Halaman Batang
def show_bar_chart_page():
    st.title('Halaman Batang')

    uploaded_file = st.file_uploader('Upload CSV', type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if not df.empty:
            st.write('Daftar Tahun yang Tersedia:')
            st.write(df.columns[1:])
            selected_year = st.selectbox('Pilih Tahun:', df.columns[1:])
            population = df[selected_year].tolist()
            region_names = df.iloc[:, 0].tolist()

            fig, ax = plt.subplots()
            ax.barh(region_names, population, color='skyblue')
            ax.set_xlabel('Jumlah Penduduk')
            ax.set_ylabel('Kecamatan')
            ax.set_title('Jumlah Penduduk per Kecamatan')
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            for i, v in enumerate(population):
                ax.text(v + 10, i, f'{v:,}', va='center')
            format_y_axis(ax)
            st.pyplot(fig)

# Halaman Garis
def show_line_chart_page():
    st.title('Halaman Garis')

    uploaded_file = st.file_uploader('Upload CSV', type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if not df.empty:
            region_names = df.iloc[:, 0].tolist()
            selected_region = st.selectbox('Pilih Kecamatan:', region_names)
            population = df[df.iloc[:, 0] == selected_region].iloc[0, 1:].tolist()
            years = df.columns[1:]

            fig, ax = plt.subplots()
            ax.plot(years, population, marker='o', linestyle='-', color='skyblue')
            ax.set_xlabel('Tahun')
            ax.set_ylabel('Jumlah Penduduk')
            ax.set_title(f'Perkembangan Jumlah Penduduk di {selected_region}')
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            for i, v in enumerate(population):
                ax.text(i, v, f'{v:,}', ha='center', va='bottom')
            format_y_axis(ax)
            st.pyplot(fig)

    if st.button('Syarat dan Ketentuan'):
        st.write('Ini adalah syarat dan ketentuan penggunaan.')

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
