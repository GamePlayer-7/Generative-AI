import streamlit as st

st.title("Student Marksheet")

name = st.text_input("Enter student name:")

sub1 = st.number_input("Enter marks for Subject 1:", min_value=0, max_value=100, value=0)
sub2 = st.number_input("Enter marks for Subject 2:", min_value=0, max_value=100, value=0)
sub3 = st.number_input("Enter marks for Subject 3:", min_value=0, max_value=100, value=0)
sub4 = st.number_input("Enter marks for Subject 4:", min_value=0, max_value=100, value=0)
sub5 = st.number_input("Enter marks for Subject 5:", min_value=0, max_value=100, value=0)

if st.button("Generate Marksheet"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    st.write(f"Student Name: {name}")
    st.write(f"Total Marks: {total}/500")
    st.write(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    st.write(f"Grade: {grade}")