import streamlit as st

def main():
    st.title("Visualisasi Data")

    if st.button('Lingkaran'):
        st.experimental_set_query_params(page='lingkaran')

    if st.button('Batang'):
        st.experimental_set_query_params(page='batang')

    if st.button('Garis'):
        st.experimental_set_query_params(page='garis')

if __name__ == "__main__":
    main()
