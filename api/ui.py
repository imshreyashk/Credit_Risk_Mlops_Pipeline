import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(page_title="Credit Guard AI", page_icon="🛡️", layout="wide")

# Custom CSS for "Wild" UI
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #00ffcc; color: black; font-weight: bold; }
    .stMetric { background-color: #1a1c24; padding: 15px; border-radius: 15px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Credit Guard AI")
st.subheader("Autonomous Risk Assessment Protocol")

with st.sidebar:
    st.image("https://flaticon.com", width=100)
    st.header("Control Panel")
    st.info("This AI uses a Random Forest Classifier to detect default probability in real-time.")

# 1. Inputs
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Applicant Age", 18, 100, 30)
    income = st.number_input("Annual Income ($)", 0, 1000000, 55000)
with col2:
    loan_amount = st.number_input("Requested Loan ($)", 0, 500000, 15000)
    credit_score = st.slider("Credit Score", 300, 850, 680)
with col3:
    employment = st.number_input("Employment (Years)", 0, 50, 4)
    purpose = st.selectbox("Loan Purpose", ["Education", "Medical", "Venture", "Personal"])

# 2. Prediction Logic
if st.button("EXECUTE RISK ANALYSIS"):
    payload = {
        "age": age, "income": income, "loan_amount": loan_amount,
        "credit_score": credit_score, "employment_years": employment
    }
    
    try:
        # Use localhost for internal Docker communication
        response = requests.post("http://localhost:8080/predict", json=payload)
        res = response.json()
        
        prob = res["default_probability"]
        
        # 3. ADVANCED UI OUTPUTS
        st.divider()
        m1, m2, m3 = st.columns(3)
        
        with m1:
            st.metric("Risk Status", res["prediction"])
        with m2:
            # Color coding the probability
            color = "green" if prob < 0.3 else "orange" if prob < 0.6 else "red"
            st.markdown(f"**Default Probability**")
            st.title(f":{color}[{prob:.2%}]")
        with m3:
            decision = "APPROVED" if prob < 0.4 else "MANUAL REVIEW" if prob < 0.7 else "REJECTED"
            st.metric("System Decision", decision)

        if res["prediction"] == "Safe":
            st.balloons()
            st.success("Protocol Cleared: Applicant meets safety threshold.")
        else:
            st.error("Protocol Breach: High Default Risk Detected.")

    except Exception as e:
        st.error(f"System Offline: {e}")
