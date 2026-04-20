import streamlit as st
import pandas as pd

st.title("Smart Electricity Bill Analyzer")

uploaded_file = st.file_uploader("Upload your electricity data (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Data Preview:")
    st.dataframe(df)

    if df.shape[1] >= 2:
        st.write("Simple Visualization:")
        st.line_chart(df.select_dtypes(include='number'))
