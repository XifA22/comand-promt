import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Bar Chart Data Visualization")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write("Data Preview:")
    st.write(df)
    
    # Select columns for x and y axes
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)
    
    # Generate the bar chart
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"Bar Chart of {y_col} vs {x_col}")
    
    # Display the chart
    st.pyplot(fig)
