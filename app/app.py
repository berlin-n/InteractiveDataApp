import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeRegressor

st.set_page_config("Interactive Data App")
st.title("Interactive Data App")

tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Analyze", "Visualize", "Preprocess", "Feature Engineering", "Model Development", "Dashboard"])

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
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Data upoaded successfully! Navigate to the tabs to begin.")
        st.dataframe(df.head())
    else:
        st.info("Awaiting file upload...")

with tab1:
    st.subheader("Analysis")
    st.write("Number of Columns", len(df.columns))
    st.write("Number of rows", len(df))
    st.write("Columns:", df.columns.to_list())
    st.write(df.describe())
    
with tab2:
    st.subheader("Visualization")

with tab3:
    st.subheader("Preprocessing")
    cols = st.multiselect("Select columns to be dropped", df.columns)
    if st.button("Drop Columns"): # Need to add this button to trigger the column dropping functionality, or else... it won't work 
        df.drop(columns=cols)
        st.write(df.head())

with tab4:
    st.subheader("Feature Engineering")
    dependentVariable = st.selectbox("Select the column for your y-variable", df.columns)
    columns = st.multiselect("Select the columns for your X-variable", df.columns)
    y = df[dependentVariable]
    features = df[columns]

with tab5:
    st.subheader("Modelling")
    models = ["Linear Regression", "Logistic Regression", "Multi Regression", "Decision Trees"]
    model = st.selectbox("Select a Model to use", models)
    if model == "Linear Regression":
        X = st.selectbox("Select your X variable", features)
        linearRegressionModel = LinearRegression()
        linearRegressionModel.fit(X,y)
    elif model == "Multi Regression":
        X = st.multiselect("Select your X variable", features)
        linearRegressionModel = LinearRegression()
        linearRegressionModel.fit(X,y)
    elif model == "Logistic Regression":
        X = st.multiselect("Select your X variable", features)
        logisticRegressionModel = LogisticRegression()
        logisticRegressionModel.fit(X,y)
    elif model == "Decision Trees":
        X = st.multiselect("Select your X variable", features)
        decisionTreeRegressionModel = DecisionTreeRegressor()
        decisionTreeRegressionModel.fit(X,y)
    
with tab6:
    st.subheader("Generate a dashboard")
    

