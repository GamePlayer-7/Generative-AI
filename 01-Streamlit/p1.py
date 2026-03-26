import streamlit as st

# Title
st.title("My First Streamlit App")

# Text display
st.write("Hello! Welcome to Streamlit.")

# User input
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.write(f"Hello, {name}!")