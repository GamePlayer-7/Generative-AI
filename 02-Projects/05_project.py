import streamlit as st
import pandas as pd

#Data Cleaning Tool

st.set_page_config(page_title="Data Cleaning Tool", page_icon="🧹", layout="wide")

st.title("Data Cleaning Tool")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Original Data")
    st.dataframe(df)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.success("Duplicates removed!")

    fill_option = st.selectbox(
        "Fill Missing Values With",
        ["Do Nothing", "0", "Mean (numeric columns only)"]
    )

    if fill_option == "0":
        df = df.fillna(0)
    elif fill_option == "Mean (numeric columns only)":
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())

    st.subheader("Cleaned Data")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload a CSV file.")