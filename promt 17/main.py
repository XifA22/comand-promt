import streamlit as st
from PIL import Image

# Load logo image
logo = Image.open("path/to/logo.png")  # Ganti path dengan lokasi logo

# Halaman utama
st.image(logo, width=100)
st.title("Visualisasi Data")

# Tombol navigasi
if st.button("Diagram Lingkaran"):
    st.experimental_rerun()
    st.session_state['page'] = 'diagram_lingkaran'
elif st.button("Diagram Batang"):
    st.experimental_rerun()
    st.session_state['page'] = 'diagram_batang'
elif st.button("Diagram Garis"):
    st.experimental_rerun()
    st.session_state['page'] = 'diagram_garis'

# Navigasi halaman
if 'page' in st.session_state:
    if st.session_state['page'] == 'diagram_lingkaran':
        import diagram_lingkaran
    elif st.session_state['page'] == 'diagram_batang':
        import diagram_batang
    elif st.session_state['page'] == 'diagram_garis':
        import diagram_garis
