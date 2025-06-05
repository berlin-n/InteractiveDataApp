import streamlit as st
import pandas as pd

st.subheader("Preprocessing")

if "df" in st.session_state:
    df = st.session_state["df"]
    if st.button("View Data"):
        st.write(df.head())

    st.markdown("##### Drop Columns")
    dropped_cols = st.multiselect("Select columns to be dropped", df.columns)
    if dropped_cols:
        if st.button("Drop"): # Need to add this button to trigger the column dropping functionality, or else... it won't work 
            df = df.drop(columns=dropped_cols)
            st.session_state["df"] = df
            st.success("Columns successfully dropped")

    st.markdown("##### Drop columns with missing values")    
    if st.button("Drop Columns"):
        df = df.dropna(axis=0)
        st.session_state["df"] = df
        st.success("Columns successfully dropped")

    st.markdown("##### Drop rows with missing values")   
    if st.button("Drop Rows"):
        df = df.dropna(axis=1)
        st.session_state["df"] = df
        st.success("Columns successfully dropped")

    # st.markdown("##### Convert datatype")

else:
    st.info("Import your file from the Home Tab to begin")

