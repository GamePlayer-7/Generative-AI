import streamlit as st

st.title("Project 2: Text Input with Slider")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

if name:
    st.write(f"Hello, {name}! You are {age} years old.")