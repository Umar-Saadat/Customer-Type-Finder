import streamlit as st
import pickle as pkl
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('customer_Segmentation.csv')

mdoel = pkl.load(open('KNN.pkl','rb'))

st.header('Customer Type Predictor')

Age = st.slider('Select Age',10,100)

Annual_Income = st.slider('Select Annual Income(K)',10,230)

Spending_Score = st.slider('Select Spending Money',1,150)

user_Data = [[Age,Annual_Income,Spending_Score]]

if st.button('Predict'):
    prediction = mdoel.predict(user_Data)
    
    if prediction == 0:
        
        st.markdown(f"<h1 style='text-align : center'>Customer have Low Budget</h1>",unsafe_allow_html=True)
        
    elif prediction == 1:
        
        st.markdown(f"<h1 style='text-align : center'>Customer have Normal Budget</h1>",unsafe_allow_html=True)
        
    elif prediction == 2:
        
        st.markdown(f"<h1 style='text-align : center'>Customer have High Budget</h1>",unsafe_allow_html=True)