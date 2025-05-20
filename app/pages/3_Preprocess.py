import streamlit as st
import pandas as pd

st.subheader("Preprocessing")

if "df" in st.session_state:
    df = st.session_state["df"]
    dropped_cols = st.multiselect("Select columns to be dropped", df.columns)
    if st.button("Drop Columns"): # Need to add this button to trigger the column dropping functionality, or else... it won't work 
        df = df.drop(columns=dropped_cols)
        st.session_state["df"] = df
        st.write(df.head())
else:
    st.info("Import your file from the Home Tab to begin")

