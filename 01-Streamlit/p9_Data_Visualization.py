# Creating a Data Visualization Application
import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Visualization App: Random Data")

st.subheader("Line Chart")
# Generate some random data for a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.subheader("Map of San Francisco Area")
# Generate random data points (latitude and longitude) for a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)
