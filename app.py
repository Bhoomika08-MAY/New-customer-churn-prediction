import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

# ---------------- LOAD FILES ----------------

with open("models/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/feature_order.pkl", "rb") as f:
    feature_order = pickle.load(f)

# ---------------- TITLE ----------------

st.title("📊 Customer Churn Prediction System")

st.markdown(
    "Predict whether a customer is likely to churn based on customer details."
)

# ---------------- SIDEBAR ----------------

st.sidebar.header("Customer Information")

credit_score = st.sidebar.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

geography = st.sidebar.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.sidebar.radio(
    "Gender",
    ["Male", "Female"]
)

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure = st.sidebar.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.sidebar.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_products = st.sidebar.selectbox(
    "Number of Products",
    [1, 2, 3, 4]
)

has_card = st.sidebar.radio(
    "Has Credit Card",
    ["Yes", "No"]
)

active_member = st.sidebar.radio(
    "Active Member",
    ["Yes", "No"]
)

salary = st.sidebar.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=60000.0
)

# ---------------- PREDICTION ----------------

if st.button("🔍 Predict Churn"):

    input_data = np.array([[
        credit_score,
        1 if gender == "Male" else 0,
        age,
        tenure,
        balance,
        num_products,
        1 if has_card == "Yes" else 0,
        1 if active_member == "Yes" else 0,
        salary,
        1 if geography == "Germany" else 0,
        1 if geography == "Spain" else 0
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    st.write(f"### Churn Probability: {probability*100:.2f}%")

    st.progress(int(probability * 100))

    # ---------------- RISK LEVEL ----------------

    st.subheader("Risk Assessment")

    risk_percent = probability * 100

    if risk_percent < 40:
       st.success("🟢 Low Risk")

    elif risk_percent < 65:
       st.warning("🟡 Medium Risk")

    elif risk_percent < 75:
       st.error("🔴 Edge of High Risk")

    else:
       st.error("🚨 Critical Churn Risk")
    # ---------------- CUSTOMER SUMMARY ----------------

    st.subheader("Customer Summary")

    st.write(f"Credit Score: {credit_score}")
    st.write(f"Age: {age}")
    st.write(f"Tenure: {tenure}")
    st.write(f"Balance: {balance}")
    st.write(f"Products: {num_products}")
    st.write(f"Active Member: {active_member}")
    st.write(f"Estimated Salary: {salary}")
        # ---------------- WHY THIS PREDICTION ----------------

    st.subheader("🧠 Why This Prediction?")

    risk_factors = []
    positive_factors = []

    if age > 60:
        risk_factors.append("Higher age may increase churn risk")
    else:
        positive_factors.append("Younger customer profile")

    if credit_score < 500:
        risk_factors.append("Low credit score")
    elif credit_score > 700:
        positive_factors.append("Strong credit score")

    if tenure <= 2:
        risk_factors.append("Short relationship with bank")
    elif tenure >= 7:
        positive_factors.append("Long relationship with bank")

    if num_products == 1:
        risk_factors.append("Only one banking product")
    elif num_products == 2:
        positive_factors.append("Uses multiple banking products")

    if active_member == "No":
        risk_factors.append("Inactive customer")
    else:
        positive_factors.append("Active customer")

    if balance > 100000:
        risk_factors.append("High balance customer")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔺 Factors Increasing Risk")

        if risk_factors:
            for factor in risk_factors:
                st.markdown(f"- {factor}")
        else:
            st.success("No major risk factors detected")

    with col2:
        st.markdown("### 🔻 Factors Reducing Risk")

        if positive_factors:
            for factor in positive_factors:
                st.markdown(f"- {factor}")
        else:
            st.success("No major positive factors detected")

    # ---------------- SHAP STYLE EXPLANATION ----------------

    st.subheader("🔍 Feature Impact Analysis")

    impact_df = pd.DataFrame({
        "Feature": [
            "Age",
            "CreditScore",
            "Tenure",
            "NumProducts",
            "Balance"
        ],
        "Value": [
            age,
            credit_score,
            tenure,
            num_products,
            balance
        ]
    })

    st.dataframe(impact_df)

    # ---------------- FEATURE IMPORTANCE ----------------

    st.subheader("📊 Feature Importance")

    feature_df = pd.DataFrame({
        "Feature": feature_order,
        "Importance": model.feature_importances_
    })

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False
    )

    st.bar_chart(
        feature_df.set_index("Feature")
    )

    # ---------------- MOST IMPORTANT FEATURE ----------------

    st.subheader("🏆 Most Influential Feature")

    st.success(
        f"Most important feature: {feature_df.iloc[0]['Feature']}"
    )

    # ---------------- CREDIT SCORE ANALYSIS ----------------

    st.subheader("📈 Credit Score Sensitivity Analysis")

    credit_scores = []
    churn_probs = []

    for score in range(300, 901, 50):

        temp_input = np.array([[
            score,
            1 if gender == "Male" else 0,
            age,
            tenure,
            balance,
            num_products,
            1 if has_card == "Yes" else 0,
            1 if active_member == "Yes" else 0,
            salary,
            1 if geography == "Germany" else 0,
            1 if geography == "Spain" else 0
        ]])

        temp_scaled = scaler.transform(temp_input)

        prob = model.predict_proba(
            temp_scaled
        )[0][1]

        credit_scores.append(score)
        churn_probs.append(prob)

    sensitivity_df = pd.DataFrame({
        "Credit Score": credit_scores,
        "Churn Probability": churn_probs
    })

    st.line_chart(
        sensitivity_df.set_index("Credit Score")
    )

    st.info(
        "Only Credit Score changes in this graph. All other customer details remain fixed."
    )    