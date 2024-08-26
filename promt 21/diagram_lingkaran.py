import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    st.title("Diagram Lingkaran")

    uploaded_file = st.file_uploader("Upload file CSV", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        first_column = df.columns[0]
        data = df[first_column].value_counts()
        
        # Create pie chart
        fig, ax = plt.subplots()
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        
        st.pyplot(fig)

    # Explanation button
    if st.button('Pengertian'):
        st.write("Diagram lingkaran digunakan untuk menunjukkan bagian-bagian dari keseluruhan.")

    # Usage guide button with image
    if st.button('Panduan Penggunaan'):
        st.write("Berikut adalah panduan penggunaan untuk mengupload dan melihat diagram lingkaran.")
        st.image('path_to_usage_image.png')  # Ganti dengan path gambar panduan penggunaan

if __name__ == "__main__":
    run()
