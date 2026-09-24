# 📊 Customer Churn Prediction System

A Machine Learning-based web application that predicts customer churn risk and provides insights into the factors influencing customer retention. Built using Python, Scikit-learn, and Streamlit.

## 🚀 Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave their services. By predicting churn early, companies can take proactive measures to improve customer retention and reduce revenue loss.

This project uses a **Random Forest Classifier** trained on customer banking data to predict whether a customer is likely to churn.

---

## ✨ Features

* Predict customer churn probability
* Interactive Streamlit web interface
* Customer risk categorization:

  * 🟢 Low Risk
  * 🟡 Medium Risk
  * 🔴 High Risk
* Feature Importance Visualization
* Customer Summary Dashboard
* Credit Score Sensitivity Analysis
* Real-time prediction using trained model

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Streamlit
* NumPy
* Pandas
* Scikit-learn
* Pickle
* Matplotlib

### Machine Learning

* Random Forest Classifier

---

## 📂 Project Structure

```text
New-customer-churn-prediction/
│
├── app.py
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_order.pkl
│
├── notebooks/
│   └── train_model.ipynb
│
├── requirements.txt
├── README.md
└── dataset/
```

## 📈 Input Features

The model uses the following customer attributes:

* Credit Score
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary
* Geography (Germany, Spain)

---

## 🎯 Model Performance

* Algorithm: Random Forest Classifier
* Accuracy: **86.65%**
* Output: Churn Probability (%)
* Classification:

  * Low Risk: < 20%
  * Medium Risk: 20% – 50%
  * High Risk: > 50%

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Bhoomika08-MAY/New-customer-churn-prediction.git
cd New-customer-churn-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Workflow

1. Enter customer information.
2. Click **Predict Churn**.
3. View churn probability.
4. Analyze risk level.
5. Review feature importance and insights.

---

## 🔍 Future Improvements

* SHAP Explainability Integration
* Model Hyperparameter Optimization
* Deployment on Cloud Platform
* Customer Retention Recommendations
* Advanced Dashboard Analytics

---

## 👩‍💻 Author

**Bhoomika M**

 B.E (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/Bhoomika08-MAY

---

## 📜 License

This project is developed for educational and learning purposes.
