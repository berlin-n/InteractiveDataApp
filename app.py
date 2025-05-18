import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Explorer")
st.title("Interative Data App")

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
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file and "data_loaded" not in st.session_state:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df
        st.session_state["data_loaded"] = True
        st.success("Data upoaded successfully! Navigate to the tabs to begin.")
        st.dataframe(df.head())
    
    if uploaded_file and st.session_state.get("data_loaded"):
        if st.button("Reset and Reload File"):
            df = pd.read_csv(uploaded_file)
            st.session_state["df"] = df
            st.success("Data reset to original upload")

    else:
        st.info("Awaiting file upload...")


with tab1:
    st.subheader("Analyze Your Data")

    if "df" in st.session_state:
        df = st.session_state["df"]
        st.write("Original Data Preview")
        st.dataframe(df.head())
        
        st.write("Number of Rows", df.size)
        st.write("Number of Columns", len(df.columns))
        st.write("Column names:", df.columns.tolist())
        st.subheader("Summary Statistics")
        st.write(df.describe())
    else:
        st.warning("Please upload a dataset in the 'Home' tab first.")



with tab2:
    st.subheader("Visualize Your Data")

    if "df" in st.session_state:
        df = st.session_state["df"]
        st.write("Original Data Preview")
        st.dataframe(df.head())
        
        col = st.selectbox("Select a column to visualize", df.columns)
        if pd.api.types.is_numeric_dtype(df[col]):
            st.subheader(f"Distribution of {col}")
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
            st.pyplot(fig)
        else:
            st.subheader(f"Value Counts for {col}")
            st.write(df[col].value_counts())
    else:
        st.warning("Please upload a dataset in the 'Home' tab first.")



with tab3:
    st.subheader("Preprocessing")

    if "df" not in st.session_state:
        st.warning("Please upload a dataset in the 'Home' tab first.")
    else:
        df = st.session_state["df"]
        st.write("Current Data Preview")
        st.dataframe(df.head())

        st.markdown('### Handle Missing Values')
        missing_cols = df.columns[df.isnull().any().tolist()]
        if missing_cols is not None:
            selected_col = st.selectbox("Select column to fix", missing_cols)
            option = st.radio("Choose a method:", [
                "Drop rows",
                "Fill with mean", 
                "Fill with median", 
                "Fill with mode", 
                "Fill with custom value"
            ], key="fill_method")
                
            if option == "Fill with custom value":
                custom_val = st.text_input("Enter custom value")

            if st.button("Apply Missing Value Treatment"):
                try:
                    if option == "Drop rows":
                        df = df.dropna(subset=[selected_col])
                    elif option == "Fill with mean":
                        df[selected_col] = df[selected_col].fillna(df[selected_col].mean())
                    elif option == "Fill with median":
                        df[selected_col] = df[selected_col].fillna(df[selected_col].median())
                    elif option == "Fill with mode":
                        df[selected_col] = df[selected_col].fillna(df[selected_col].mode([0]))
                    elif option == "Fill with custom value":
                        df[selected_col] = df[selected_col].fillna(custom_val)

                    st.session_state["df"] = df
                    st.success(f"Missing Values in {selected_col} handled")
                except Exception as e:
                    st.Error(f"Error: {e}")
        else:
            st.info("No column with missing values.")
        
        st.markdown("---")

        st.markdown("### Drop Columns")
        drop_cols = st.multiselect("Select columns to drop", df.columns, key="drop_cols")
        if st.button("Drop selected columns"):
            df = df.drop(columns=drop_cols)
            st.session_state["df"] = df
            st.success(f"Dropped Columns {drop_cols}")

        st.markdown("---")

        st.markdown("### Change Column Data Type")
        dtype_col = st.selectbox("Select column to change type", df.columns, key="change_dtype")
        dtype = st.selectbox("Convert to type:", ["int", "float", "str", "datetime"])
        if st.button("Convert data type"):
            try:
                if dtype == "datetime":
                    df[dtype_col] = pd.to_datetime(df[dtype_col])
                else:
                    df[dtype_col] = df[dtype_col].astype(dtype)
                st.session_state["df"] = df
                st.success(f"Converted '{dtype_col}' to '{dtype}'")
            except Exception as e:
                st.error(f"Converion failed: {e}")

        st.markdown("---")

        st.markdown("### Rename Columns")
        col_to_rename = st.selectbox("Select a column to rename", df.columns, key="rename_col")
        new_col_name = st.text_input("Enter new column name")
        if st.button("Rename column") and new_col_name:
            df = df.rename(columns={col_to_rename: new_col_name})
            st.session_state["df"] = df
            st.success(f"Renamed '{col_to_rename}' to '{new_col_name}'")
        
    

with tab4:
    st.subheader("Create Features")

    if "df" in st.session_state:
        df = st.session_state["df"]
        st.write("Original Data Preview")
        st.dataframe(df.head())
        
    else:
        st.warning("Please upload a dataset in the 'Home' tab first.")

    

with tab5:
    st.subheader("Make a Prediction")

    if "df" in st.session_state:
        df = st.session_state["df"]
        st.write("Original Data Preview")
        st.dataframe(df.head())
        
    else:
        st.warning("Please upload a dataset in the 'Home' tab first.")

with tab6:
    st.subheader("Generate a Dashboard")

    if "df" in st.session_state:
        df = st.session_state["df"]
        st.write("Original Data Preview")
        st.dataframe(df.head())
        
    else:
        st.warning("Please upload a dataset in the 'Home' tab first.")
        
