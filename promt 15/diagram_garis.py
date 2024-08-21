import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def diagram_garis():
    st.title("Diagram Garis")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        if data.shape[1] < 2:
            st.error("CSV harus memiliki setidaknya dua kolom.")
        else:
            fig, ax = plt.subplots()
            for column in data.columns[1:]:
                ax.plot(data.iloc[:, 0], data[column], marker='o', label=column)

            ax.set_title("Diagram Garis")
            ax.set_xlabel("Waktu")
            ax.set_ylabel("Nilai")
            ax.grid(True)
            ax.legend()

            # Tambahkan angka detail di atas titik data
            for i in range(len(data)):
                for j in range(1, len(data.columns)):
                    ax.text(data.iloc[i, 0], data.iloc[i, j], str(data.iloc[i, j]), ha='center')

            st.pyplot(fig)

            if st.button("Syarat dan Ketentuan"):
                st.write("Dengan menggunakan aplikasi ini, Anda setuju untuk tidak menyalahgunakan data yang ditampilkan.")

if __name__ == "__main__":
    diagram_garis()
