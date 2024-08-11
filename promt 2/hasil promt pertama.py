import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Pie Chart Data Visualization")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show the uploaded data as a table
    st.write("Data Preview:")
    st.write(df)
    
    # Check if the DataFrame is not empty
    if not df.empty:
        # Select the columns for the pie chart
        st.write("Select the column for the pie chart:")
        column = st.selectbox("Column", df.columns)
        
        # Prepare data for the pie chart
        data = df[column].value_counts()
        
        # Create a pie chart
        fig, ax = plt.subplots()
        ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        # Display the pie chart
        st.pyplot(fig)
