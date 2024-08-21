import streamlit as st
from PIL import Image

def main():
    # Memuat logo
    logo = Image.open("logo.png")
    st.image(logo, width=100)  # Tampilkan logo di pojok kiri atas

    # Judul halaman utama
    st.title("Visualisasi Data")

    # Tombol navigasi
    if st.button("Diagram Lingkaran"):
        st.experimental_rerun()  # Navigasi ke halaman diagram lingkaran
        import diagram_lingkaran
        diagram_lingkaran.show()

    if st.button("Diagram Batang"):
        st.experimental_rerun()  # Navigasi ke halaman diagram batang
        import diagram_batang
        diagram_batang.show()

    if st.button("Diagram Garis"):
        st.experimental_rerun()  # Navigasi ke halaman diagram garis
        import diagram_garis
        diagram_garis.show()

if __name__ == "__main__":
    main()
