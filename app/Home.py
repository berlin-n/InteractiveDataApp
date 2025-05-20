import streamlit as st
import pandas as pd

st.set_page_config("Interactive Data App")
st.title("Interactive Data App")
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

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.success("Data upoaded successfully! Navigate to the tabs to begin.")
    st.dataframe(df.head())
else:
    st.info("Awaiting file upload...")


 