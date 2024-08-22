import streamlit as st
from diagram_lingkaran import show_diagram_lingkaran
from diagram_batang import show_diagram_batang
from diagram_garis import show_diagram_garis

# Menampilkan logo di pojok kanan atas
st.sidebar.image("logo.png", use_column_width=True)

# Teks "Visualisasi Data" di atas tombol
st.title("Visualisasi Data")

# Tombol navigasi
option = st.selectbox("Pilih diagram:", ["Pilih diagram", "Diagram Lingkaran", "Diagram Batang", "Diagram Garis"])

if option == "Diagram Lingkaran":
    show_diagram_lingkaran()
elif option == "Diagram Batang":
    show_diagram_batang()
elif option == "Diagram Garis":
    show_diagram_garis()
