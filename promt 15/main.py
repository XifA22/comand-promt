import streamlit as st
from PIL import Image

def main():
    # Tambahkan logo di pojok kiri atas
    logo = Image.open("logo.png")  # Gantilah "logo.png" dengan nama file logomu
    st.image(logo, width=100)

    # Teks di atas tombol
    st.title("Visualisasi Data")

    # Tombol navigasi
    if st.button("Diagram Lingkaran"):
        st.experimental_rerun("diagram_lingkaran")
    if st.button("Diagram Batang"):
        st.experimental_rerun("diagram_batang")
    if st.button("Diagram Garis"):
        st.experimental_rerun("diagram_garis")

if __name__ == "__main__":
    main()
