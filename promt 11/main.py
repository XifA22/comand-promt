# main.py
import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Visualisasi Data", layout="wide")
    
    # Menampilkan logo di pojok kiri atas
    image = Image.open('logo.png')  # Ganti dengan path ke logo Anda
    st.sidebar.image(image, use_column_width=True)
    
    st.title("Visualisasi Data")
    
    # Tombol navigasi
    st.sidebar.title("Pilih Jenis Visualisasi")
    selection = st.sidebar.radio("Pilih Jenis Diagram", ["Diagram Lingkaran", "Diagram Batang", "Diagram Garis"])
    
    if selection == "Diagram Lingkaran":
        st.write("Anda memilih Diagram Lingkaran")
        st.write("Klik tombol di samping untuk beralih ke Diagram Lingkaran.")
        if st.button("Diagram Lingkaran"):
            st.experimental_rerun()
    
    elif selection == "Diagram Batang":
        st.write("Anda memilih Diagram Batang")
        st.write("Klik tombol di samping untuk beralih ke Diagram Batang.")
        if st.button("Diagram Batang"):
            st.experimental_rerun()
    
    elif selection == "Diagram Garis":
        st.write("Anda memilih Diagram Garis")
        st.write("Klik tombol di samping untuk beralih ke Diagram Garis.")
        if st.button("Diagram Garis"):
            st.experimental_rerun()
    
    # Rerun jika tombol ditekan
    if st.session_state.get('rerun'):
        st.session_state.rerun = False
        if selection == "Diagram Lingkaran":
            import diagram_lingkaran
        elif selection == "Diagram Batang":
            import diagram_batang
        elif selection == "Diagram Garis":
            import diagram_garis

if __name__ == "__main__":
    main()
