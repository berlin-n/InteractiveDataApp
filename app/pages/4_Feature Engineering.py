import streamlit as st
import pandas as pd

st.subheader("Feature Engineering")

if "df" in st.session_state:
    df = st.session_state["df"]
    dependentVariable = st.selectbox("Select the column for your y-variable", df.columns)
    columns = st.multiselect("Select the columns for your X-variable", df.columns)
    y = df[dependentVariable]
    features = df[columns]
else:
    st.info("Import your file from the Home Tab to begin")