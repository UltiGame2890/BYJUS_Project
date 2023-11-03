from diabetes_main import load_data
import streamlit as st
st.set_page_config(page_title = 'Early Diabetes Prediction Web App',
                    page_icon = 'random',
                    layout = 'wide',
                    initial_sidebar_state = 'auto'
                    )
st.title("Early Diabetes Prediction Web App")
st.sidebar.title("Navigation")
st.sidebar.success("Select a page above.")
st.markdown("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes. This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.")
diabetes_df = load_data()
st.header("View Data")
expander = st.expander("View Data")
expander.dataframe(diabetes_df)
col1, col2, col3 = st.columns(3)
with col1:
	if st.checkbox("Show all column names"):
		st.write(diabetes_df.columns)

with col2:
	if st.checkbox("View column data-type"):
		st.write(diabetes_df.dtypes)

with col3:
	if st.checkbox("View column data"):
		selectbox = st.selectbox("Select column", list(diabetes_df.columns))
		st.dataframe(diabetes_df[selectbox])