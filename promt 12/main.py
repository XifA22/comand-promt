import streamlit as st
from PIL import Image

# Logo di pojok kiri atas
logo = Image.open("path/to/logo.png")  # Ganti dengan path logo yang benar
st.sidebar.image(logo, use_column_width=True)

# Judul di halaman utama
st.title("Visualisasi Data")

# Tombol navigasi ke halaman diagram
if st.button("Diagram Lingkaran"):
    st.experimental_set_query_params(page="diagram_lingkaran")
if st.button("Diagram Batang"):
    st.experimental_set_query_params(page="diagram_batang")
if st.button("Diagram Garis"):
    st.experimental_set_query_params(page="diagram_garis")

# Navigasi ke halaman yang sesuai
query_params = st.experimental_get_query_params()
if query_params.get("page") == ["diagram_lingkaran"]:
    import diagram_lingkaran
    diagram_lingkaran.run()
elif query_params.get("page") == ["diagram_batang"]:
    import diagram_batang
    diagram_batang.run()
elif query_params.get("page") == ["diagram_garis"]:
    import diagram_garis
    diagram_garis.run()
