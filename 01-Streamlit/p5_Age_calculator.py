import streamlit as st
from datetime import date

st.title("Age Calculator")

birth_date = st.date_input("Select your birth date:")

if st.button("Calculate Age"):
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    st.success(f"Your age is: {age} years")