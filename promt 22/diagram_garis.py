import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_garis():
    st.sidebar.title("Diagram Garis")
    st.sidebar.button("Kembali ke Halaman Utama", on_click=lambda: st.experimental_set_query_params())

    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        
        st.button("Syarat dan Ketentuan", on_click=lambda: st.write("Syarat dan ketentuan..."))

        fig, ax = plt.subplots()
        for i in range(1, len(data.columns)):
            ax.plot(data.iloc[:, 0], data.iloc[:, i], marker='o', label=data.columns[i])
            for j, v in enumerate(data.iloc[:, i]):
                ax.text(j, v + 0.2, str(v), ha='center')

        ax.set_title("Diagram Garis")
        ax.set_xlabel("Kategori")
        ax.set_ylabel("Nilai")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

if __name__ == "__main__":
    diagram_garis()
