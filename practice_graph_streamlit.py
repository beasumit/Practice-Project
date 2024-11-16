import streamlit as st
import pandas as pd
st.title("Graph from CSV")


file_upload = st.file_uploader(label="Upload file Here.",type=[".csv",".xlsx"])
if file_upload:
    if file_upload.name.endswith(".csv"):
        data = pd.read_csv(file_upload)
        st.line_chart(data)
    elif file_upload.name.endswith(".xlsx"):
        data = pd.read_excel(file_upload)
        st.line_chart(data)