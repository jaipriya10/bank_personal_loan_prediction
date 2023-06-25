import streamlit as st
import numpy as np
import pickle
import plotly.express as px
import pandas as pd
from streamlit import components
import webbrowser

st.set_page_config(page_title="Bank Loan Approval Prediction App",layout="wide")
title  = "Bank Loan Approval Prediction App"
container = st.container()

with container:
    st.markdown("<h1 style='text-align:center;font-weight:bold;'>Bank Loan Approval Prediction App</h1>",unsafe_allow_html=True)
cols = container.columns([1,2])
left_col = cols[0]
right_col = cols[1]
model = pickle.load(open('model.pkl', 'rb'))

def predict_loan_approval(values):
    prediction = model.predict(values)
    return prediction






def main():
    df = pd.DataFrame({'Income': [0], 'cc_avg': [0.0]}) # Define df before the if block
    left_col.write("Enter the following details to get the loan approval status")
    with left_col:
        age = st.slider("Age", min_value=1, max_value=90, step=1)
        experience = st.slider("Experience", min_value=0, max_value=25, step=1)
        income = st.slider("Income", min_value=0, max_value=1000, step=1)
        zip_code = st.number_input("ZIP Code", min_value=0)
        family = st.slider("Family Size", min_value=0, max_value=10, step=1)
        cc_avg = st.slider("CCAvg", min_value=0.0, max_value=20.0, format="%.2f")
        education = st.selectbox("Education", options=["Undergrad", "Graduate", "Advanced/Professional"])
        mortgage = st.selectbox("Mortgage", options=["No Mortgage", "Have Mortgage"])
        securities_account = st.selectbox("Securities Account", options=["No account with us", "Have account with us"])
        cd_account = st.selectbox("CD Account", options=["No CD account with us", "Have CD account with us"])
        online = st.selectbox("Online Banking", options=["No online banking", "Online banking"])
        credit_card = st.selectbox("Credit Card", options=["No credit card", "Have credit card"])
        prediction = None
        if st.button("Predict"):
            educ_dict = {"Undergrad": 1, "Graduate": 2, "Advanced/Professional": 3}
            education_val = educ_dict[education]

            values = np.array([[age, experience, income, zip_code, family, cc_avg, education_val,                                
                                1 if mortgage == "Have Mortgage" else 0,                                
                                1 if securities_account == "Have account with us" else 0,                                
                                1 if cd_account == "Have CD account with us" else 0,                               
                                1 if online == "Online banking" else 0,                                
                                1 if credit_card == "Have credit card" else 0]])
            prediction = predict_loan_approval(values)
            df = pd.DataFrame({'Income': [income], 'cc_avg': [cc_avg]}) # Update df if the button is pressed
        else:
            df = pd.DataFrame({'Income': [0], 'cc_avg': [0.0]}) # Use default values for df
    with right_col:
        if prediction is not None:
            st.subheader("Prediction")
            if prediction == 1:
                image = "approve.jpg"
                st.image(image)
                st.subheader("Tableau Dashboard")
                tableau_dashboard_url = "http://localhost:8080/tab.html"

                st.markdown(f'<a href="{tableau_dashboard_url}" target="_blank">Open Tableau Dashboard</a>', unsafe_allow_html=True)

            else:
                image = "rejected.jpg"
                st.image(image)
                st.subheader("Tableau Dashboard")
                tableau_dashboard_url = "http://localhost:8080/tab.html"

                st.markdown(f'<a href="{tableau_dashboard_url}" target="_blank">Open Tableau Dashboard</a>', unsafe_allow_html=True)


           

                

            
 


        
    
        
       

if __name__ == "__main__":
    main()