import streamlit as st

def main():
    st.sidebar.image("logo.png", use_column_width=True)  # Tambahkan logo di sidebar

    st.title("Visualisasi Data")

    # Tombol navigasi
    if st.button("Diagram Lingkaran"):
        st.experimental_set_query_params(page="lingkaran")
    if st.button("Diagram Batang"):
        st.experimental_set_query_params(page="batang")
    if st.button("Diagram Garis"):
        st.experimental_set_query_params(page="garis")

    # Penanganan query parameter untuk navigasi
    params = st.experimental_get_query_params()
    if params.get("page") == ["lingkaran"]:
        st.experimental_rerun()
    elif params.get("page") == ["batang"]:
        st.experimental_rerun()
    elif params.get("page") == ["garis"]:
        st.experimental_rerun()

if __name__ == "__main__":
    main()
