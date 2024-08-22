import streamlit as st
from diagram_lingkaran import halaman_diagram_lingkaran
from diagram_batang import halaman_diagram_batang
from diagram_garis import halaman_diagram_garis

# Halaman Utama
def main():
    st.set_page_config(page_title="Visualisasi Data", layout="wide")
    
    # Logo di pojok kanan atas
    st.image("path_to_logo_image.png", width=100)
    
    # Teks "Visualisasi Data" di atas tombol
    st.title("Visualisasi Data")
    
    # Tombol navigasi ke halaman lain
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Diagram Lingkaran"):
            halaman_diagram_lingkaran()
    
    with col2:
        if st.button("Diagram Batang"):
            halaman_diagram_batang()
    
    with col3:
        if st.button("Diagram Garis"):
            halaman_diagram_garis()

if __name__ == "__main__":
    main()
