import streamlit as st
import requests

st.set_page_config(page_title="Credit Risk AI", page_icon="🏦")

st.title("🏦 Loan Default Predictor")
st.markdown("Enter applicant details to assess credit risk.")

# 1. Create the Input Form
with st.form("loan_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        income = st.number_input("Annual Income ($)", min_value=0, value=50000)
        employment = st.number_input("Years of Employment", min_value=0, value=5)
        
    with col2:
        loan_amount = st.number_input("Loan Amount requested ($)", min_value=0, value=10000)
        credit_score = st.slider("Credit Score", 300, 850, 700)
    
    submit = st.form_submit_button("Analyze Risk")

# 2. Handle the Prediction
if submit:
    payload = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "credit_score": credit_score,
        "employment_years": employment
    }
    
    # Point this to your Render URL!
    API_URL = "https://onrender.com" 
    
    with st.spinner("Calculating risk..."):
        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()
            
            if result["prediction"] == "Safe":
                st.success(f"✅ Prediction: {result['prediction']}")
                st.balloons()
            else:
                st.error(f"⚠️ Prediction: {result['prediction']}")
                
            st.info(f"Default Probability: {result['default_probability']:.2%}")
            
        except Exception as e:
            st.error("Could not connect to the API. Make sure it's awake!")
