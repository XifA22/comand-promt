import streamlit as st
from PIL import Image

# Set the page title and layout
st.set_page_config(page_title="Visualisasi Data", layout="wide")

# Add logo in the top right corner
logo = Image.open('path_to_your_logo.png')  # Ganti dengan path logo yang kamu miliki
st.image(logo, width=100)

# Add title text
st.markdown("<h1 style='text-align: center;'>Visualisasi Data</h1>", unsafe_allow_html=True)

# Add buttons for different diagrams
if st.button('Diagram Lingkaran'):
    st.experimental_set_query_params(page='lingkaran')

if st.button('Diagram Batang'):
    st.experimental_set_query_params(page='batang')

if st.button('Diagram Garis'):
    st.experimental_set_query_params(page='garis')

# Check for page parameter and redirect accordingly
query_params = st.experimental_get_query_params()
page = query_params.get('page', [''])[0]

if page == 'lingkaran':
    import diagram_lingkaran
    diagram_lingkaran.run()
elif page == 'batang':
    import diagram_batang
    diagram_batang.run()
elif page == 'garis':
    import diagram_garis
    diagram_garis.run()
