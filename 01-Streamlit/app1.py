import streamlit as st
import pandas as pd
import numpy as np


# Title of the application
st.title("Hello Streamlit.")

# Create a simple DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]
})
# Display the DataFrame in the Streamlit app
st.write("Here is a simple DataFrame:")
st.write(df)