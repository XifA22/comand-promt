import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("Diagram Garis")

    uploaded_file = st.file_uploader("Upload file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        first_column = df.columns[0]
        data = df.set_index(first_column).T
        
        # Create line chart
        fig, ax = plt.subplots()
        data.plot(ax=ax)
        ax.set_title('Tren Data')
        ax.set_xlabel('Tahun')
        ax.set_ylabel('Jumlah')
        ax.grid(True)

        for column in data.columns:
            for x, y in enumerate(data[column]):
                ax.text(x, y, str(y), ha='center', va='bottom')

        st.pyplot(fig)

    # Terms and conditions button
    if st.button('Syarat dan Ketentuan'):
        st.write("Berikut adalah syarat dan ketentuan untuk menggunakan aplikasi ini.")

if __name__ == "__main__":
    run()
