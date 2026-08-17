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
'''
import streamlit as st, pandas as pd, numpy as np, joblib
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")
