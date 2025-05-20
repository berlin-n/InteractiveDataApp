import streamlit as st
import pandas as pd


st.subheader("Modelling")

if "df" in st.session_state:
    df = st.session_state["df"]
    models = ["Linear Regression", "Logistic Regression", "Multi Regression", "Decision Trees"]
    model = st.selectbox("Select a Model to use", models)
else:
    st.info("Import your file from the Home Tab to begin")


# if model == "Linear Regression":
#     X = st.selectbox("Select your X variable", features)
#     linearRegressionModel = LinearRegression()
#     linearRegressionModel.fit(X,y)
# elif model == "Multi Regression":
#     X = st.multiselect("Select your X variable", features)
#     linearRegressionModel = LinearRegression()
#     linearRegressionModel.fit(X,y)
# elif model == "Logistic Regression":
#     X = st.multiselect("Select your X variable", features)
#     logisticRegressionModel = LogisticRegression()
#     logisticRegressionModel.fit(X,y)
# elif model == "Decision Trees":
#     X = st.multiselect("Select your X variable", features)
#     decisionTreeRegressionModel = DecisionTreeRegressor()
#     decisionTreeRegressionModel.fit(X,y)