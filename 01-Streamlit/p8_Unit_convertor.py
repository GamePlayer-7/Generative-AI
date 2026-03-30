import streamlit as st

st.title("Unit Converter")

conversion_type = st.selectbox(
    "Select conversion type:",
    ["Kilometers to Meters", "Meters to Kilometers", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]
)

value = st.number_input("Enter value:", value=0.0)

if st.button("Convert"):
    if conversion_type == "Kilometers to Meters":
        result = value * 1000
        st.success(f"{value} km = {result} meters")

    elif conversion_type == "Meters to Kilometers":
        result = value / 1000
        st.success(f"{value} meters = {result} km")

    elif conversion_type == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result:.2f}°F")

    elif conversion_type == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result:.2f}°C")