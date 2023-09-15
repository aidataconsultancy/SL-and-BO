import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import data_preprocessing

# Title of the Streamlit app
st.title("Sales Forecasting and Budget Optimization")

# Upload datasets
st.sidebar.header("Upload your datasets")
uploaded_train = st.sidebar.file_uploader("Upload your train dataset", type=["csv"])
uploaded_test = st.sidebar.file_uploader("Upload your test dataset", type=["csv"])
uploaded_sample_submission = st.sidebar.file_uploader("Upload your sample submission dataset", type=["csv"])

if uploaded_train and uploaded_test and uploaded_sample_submission:
    train_data = pd.read_csv(uploaded_train)
    test_data = pd.read_csv(uploaded_test)
    sample_submission = pd.read_csv(uploaded_sample_submission)
    
    # Preprocess the datasets
    preprocessed_train, preprocessed_test, preprocessed_sample_submission = data_preprocessing.preprocess_data(train_data, test_data, sample_submission)
    
    # Data Insights
    st.subheader("Data Insights")
    highest_sales_day = preprocessed_train['sales'].idxmax()
    st.write(f"Highest Sales Day: {preprocessed_train.loc[highest_sales_day, 'date']} with {preprocessed_train.loc[highest_sales_day, 'sales']} sales.")
    
    lowest_sales_day = preprocessed_train['sales'].idxmin()
    st.write(f"Lowest Sales Day: {preprocessed_train.loc[lowest_sales_day, 'date']} with {preprocessed_train.loc[lowest_sales_day, 'sales']} sales.")
    
    average_sales = preprocessed_train['sales'].mean()
    st.write(f"Average Sales: {average_sales:.2f}")
    
    # Data Filtering
    st.subheader("Data Filtering")
    sales_threshold = st.slider("Filter data by sales threshold", float(preprocessed_train['sales'].min()), float(preprocessed_train['sales'].max()), (float(preprocessed_train['sales'].min()), float(preprocessed_train['sales'].max())))
    filtered_data = preprocessed_train[(preprocessed_train['sales'] >= sales_threshold[0]) & (preprocessed_train['sales'] <= sales_threshold[1])]
    st.write(filtered_data)
    
    # Feedback System
    st.subheader("Feedback System")
    feedback = st.text_area("Please provide your feedback or suggestions about the app:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")
        # In a real-world scenario, you'd store this feedback in a database or send it via email.

else:
    st.write("Please upload all the required datasets to proceed.")
