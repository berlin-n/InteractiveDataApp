import streamlit as st
import pandas as pd

st.subheader("Analysis")

if "df" in st.session_state:
    df = st.session_state["df"]
    st.write("Number of Columns", len(df.columns))
    st.write("Number of rows", len(df))
    st.write("Columns:", df.columns.to_list())
    st.write(df.describe())
else:
    st.info("Import your file from the Home Tab to begin")