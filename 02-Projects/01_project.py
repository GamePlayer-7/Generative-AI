import streamlit as st

st.title("Project 1: Streamlit Text Input")

name= st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")