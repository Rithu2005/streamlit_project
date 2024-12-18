import streamlit as st

# Title of the app
st.title("Interactive Greeting App")

# Add a text input widget
name = st.text_input("Enter your name:")

# Add a slider widget
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)

# Add a button to display the output
if st.button("Submit"):
    # Display a message using the inputs
    st.write(f"Hello, {name}! You are {age} years old.")
