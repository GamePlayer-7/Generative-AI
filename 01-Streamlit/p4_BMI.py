import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, value=50.0)
height = st.number_input("Enter your height (meters):", min_value=0.1, value=1.6)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.info("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")