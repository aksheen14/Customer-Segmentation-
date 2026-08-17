'''
// ============================================
// PART 2: Streamlit Web App (segmentation.py)
// ============================================

// 17. App Setup
IMPORT streamlit as st, pandas, numpy, joblib
LOAD kmeans = joblib.load('kmeans_model.pkl')
LOAD scaler = joblib.load('scaler.pkl')
SET st.title("Customer Segmentation App")
SET st.write("Enter customer details to predict the segment.")

// 18. Create Input Fields (matching training features)
age = st.number_input("Age", min=18, max=100, default=35)
income = st.number_input("Income", min=0, max=200000, default=50000)
total_spending = st.number_input("Total Spending", min=0, max=5000, default=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min=0, max=100, default=10)
num_store_purchases = st.number_input("Number of Store Purchases", min=0, max=100, default=10)
num_web_visits = st.number_input("Number of Web Visits per Month", min=0, max=50, default=3)

// 19. Build Input DataFrame
CREATE input_data = pandas.DataFrame with columns matching 'features' list,
    using the values collected above (SAME ORDER as training features)

// 20. Scale Input & Predict
COMPUTE input_scaled = scaler.transform(input_data)

IF st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)
    DISPLAY st.success(f"Predicted segment is Cluster {cluster}")
    // Optionally map cluster number -> human-readable label here

// 21. Run App
// Command line: streamlit run segmentation.py
'''
import streamlit as st, pandas as pd, numpy as np, joblib
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")


age = st.number_input("Age", min=18, max=100, default=35)
income = st.number_input("Income", min=0, max=200000, default=50000)
total_spending = st.number_input("Total Spending", min=0, max=5000, default=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min=0, max=100, default=10)
num_store_purchases = st.number_input("Number of Store Purchases", min=0, max=100, default=10)
num_web_visits = st.number_input("Number of Web Visits per Month", min=0, max=50, default=3)

input_data = pd.DataFrame({
    'Age': [age],
    'Income': [income],
    'Total_Spending': [total_spending],
    'NumWebPurchases': [num_web_purchases], 
    'NumStorePurchases': [num_store_purchases], 
    'NumWebVisits': [num_web_visits]
    })

input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)
    st.success(f"Predicted segment is Cluster {cluster}")