import streamlit as st
import pandas as pd

st.subheader("Visualization")

if "df" in st.session_state:
    st.info("Coming Soon")
else:
    st.info("Import your file from the Home Tab to begin")