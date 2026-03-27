import streamlit as st

st.title("Student Marks Calculator")

name = st.text_input("Enter student name:")
sub1 = st.number_input("Enter marks of Subject 1:", 0, 100, 0)
sub2 = st.number_input("Enter marks of Subject 2:", 0, 100, 0)
sub3 = st.number_input("Enter marks of Subject 3:", 0, 100, 0)

if st.button("Calculate"):
    total = sub1 + sub2 + sub3
    percentage = total / 3

    st.write(f"Student Name: {name}")
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")