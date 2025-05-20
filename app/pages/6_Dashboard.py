import streamlit as st

st.subheader("Dashboard")

if "df" in st.session_state:
    df = st.session_state["df"]
else:
    st.info("Import your file from the Home Tab to begin")