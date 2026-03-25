import streamlit as st

st.title("Project 3: Interactive Dashboard")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25)

options = ["Python", "JavaScript", "Java", "C++"]

choice = st.selectbox("Select your favorite programming language:", options)

if name:
    st.write(f"Hello, {name}! You are {age} years old and your favorite programming language is {choice}.")