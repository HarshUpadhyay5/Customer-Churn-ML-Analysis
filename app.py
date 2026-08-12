import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Predictor")

col1, col2 = st.columns(2)
with col1:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.slider("Monthly Charges ($)", 18.0, 120.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, float(tenure * monthly_charges))
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col2:
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    contract_extras = st.multiselect(
        "Other Services",
        ["OnlineBackup", "DeviceProtection", "StreamingTV", "StreamingMovies", "MultipleLines"],
    )
    senior = st.checkbox("Senior Citizen")
    partner = st.checkbox("Has Partner")
    dependents = st.checkbox("Has Dependents")

customer = pd.DataFrame([{
    "gender": "Female", "SeniorCitizen": int(senior), "Partner": "Yes" if partner else "No",
    "Dependents": "Yes" if dependents else "No", "tenure": tenure,
    "PhoneService": "Yes", "MultipleLines": "Yes" if "MultipleLines" in contract_extras else "No",
    "InternetService": internet_service, "OnlineSecurity": online_security,
    "OnlineBackup": "Yes" if "OnlineBackup" in contract_extras else "No",
    "DeviceProtection": "Yes" if "DeviceProtection" in contract_extras else "No",
    "TechSupport": tech_support,
    "StreamingTV": "Yes" if "StreamingTV" in contract_extras else "No",
    "StreamingMovies": "Yes" if "StreamingMovies" in contract_extras else "No",
    "Contract": contract, "PaperlessBilling": "Yes", "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges, "TotalCharges": total_charges,
}])

if st.button("Predict Churn Risk"):
    probability = model.predict_proba(customer)[0, 1]
    st.metric("Churn Probability", f"{probability:.1%}")
    if probability >= 0.5:
        st.error("High risk of churn — consider a retention offer.")
    else:
        st.success("Low risk of churn.")
