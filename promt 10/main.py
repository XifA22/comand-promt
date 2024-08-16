import streamlit as st
from diagram_lingkaran import show_pie_chart_page
from diagram_batang import show_bar_chart_page
from diagram_garis import show_line_chart_page

# Menambahkan logo di pojok kiri atas
st.image("logo.png", width=100, use_column_width=False)

# Judul utama
st.title("Visualisasi Data")

# Tombol navigasi
if st.button("Diagram Lingkaran"):
    show_pie_chart_page()
elif st.button("Diagram Batang"):
    show_bar_chart_page()
elif st.button("Diagram Garis"):
    show_line_chart_page()
