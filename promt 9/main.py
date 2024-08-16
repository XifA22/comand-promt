import streamlit as st
from diagram_lingkaran import show_diagram_lingkaran_page
from diagram_batang import show_diagram_batang_page
from diagram_garis import show_diagram_garis_page

# Header
st.title("Visualisasi Data")

# Tombol untuk navigasi
option = st.selectbox(
    'Pilih jenis diagram',
    ('Halaman Utama', 'Diagram Lingkaran', 'Diagram Batang', 'Diagram Garis')
)

if option == 'Diagram Lingkaran':
    show_diagram_lingkaran_page()
elif option == 'Diagram Batang':
    show_diagram_batang_page()
elif option == 'Diagram Garis':
    show_diagram_garis_page()
