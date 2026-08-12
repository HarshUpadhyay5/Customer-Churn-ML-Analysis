# Customer Churn Predictor
 
A Streamlit app that predicts the probability a telecom customer will churn, based on their account details, contract type, and services subscribed.
 
**Live app:** https://customer-churn-ml-analysis-e7nketpm9fzerymiwefk99.streamlit.app/
 
## How it works
Enter a customer's tenure, charges, contract, payment method, and service subscriptions, and the app returns a churn probability along with a risk flag (high/low risk).
 
## Files
- `app.py` — Streamlit app
- `churn_model.pkl` — trained XGBoost classification pipeline (preprocessing + model)
- `requirements.txt` — pinned dependencies
## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
