import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.set_page_config("Interactive Data App")
st.title("Interactive Data App")

tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Analyze", "Visualize", "Preprocess", "Feature Engineering", "Predict", "Dashboard"])

with tab0:
    st.title("Welcome to the Data Interaction App")
    st.markdown("""
    This interactive tool allows you to:
    - **Explore and analyze** your datasets
    - **Clean and preprocess** your data
    - **Engineer Features** for machine learning
    - **Build and test predictive models**
    - **Visulaize** your insights
    - And generate **dashboards** for reporting

    Upload a CSV file to get started.
    """)

    st.markdown("---")
    uploaded_file = st.file_uploader("Upload your CSV file")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
    else:
        st.info("Awaiting file upload...")

with tab1:
    st.subheader("Analyze your data")

with tab2:
    st.subheader("Visualize your data")

with tab3:
    st.subheader("Preprocess your data")

with tab4:
    st.subheader("Create features")

with tab5:
    st.subheader("Make predictions")

with tab6:
    st.subheader("Generate a dashboard")
    

