import streamlit as st

# Title for the app
st.title("Sample Streamlit App")

# Sidebar
st.sidebar.header("Sidebar Menu")
name = st.sidebar.text_input("Enter your name:", "User")
age = st.sidebar.slider("Select your age:", 0, 100, 25)

# Main area
st.header(f"Hello, {name}!")
st.write(f"Your age is {age}.")

# Adding an interactive button
if st.button("Click Me!"):
    st.success(f"Welcome, {name}! You clicked the button.")
else:
    st.info("Click the button to see a message.")

# Displaying a chart
st.subheader("Sample Chart")
import numpy as np
import pandas as pd
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)

# File uploader example
st.subheader("File Upload")
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write(uploaded_file.name)
