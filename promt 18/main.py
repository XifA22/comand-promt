import streamlit as st
from PIL import Image
import diagram_lingkaran
import diagram_batang
import diagram_garis

# Memuat logo
logo = Image.open('path_to_logo.png')

# Menampilkan logo di pojok kiri atas
st.image(logo, width=100, use_column_width=False)

# Teks di atas tombol
st.title("Visualisasi Data")

# Tombol navigasi
if st.button("Diagram Lingkaran"):
    diagram_lingkaran.main()
elif st.button("Diagram Batang"):
    diagram_batang.main()
elif st.button("Diagram Garis"):
    diagram_garis.main()
