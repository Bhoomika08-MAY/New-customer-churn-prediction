<<<<<<< HEAD
# 📊 Customer Churn Prediction

A Machine Learning web application that predicts whether a bank customer is likely to churn (leave the bank) based on customer demographics, account information, and banking behavior.

The project includes data preprocessing, feature engineering, model training, evaluation, model persistence using pickle files, and deployment through a Streamlit web application.

---

## 🚀 Features

- Predicts customer churn likelihood
- Interactive Streamlit web interface
- Data preprocessing and feature engineering
- Feature scaling using StandardScaler
- Trained Machine Learning model
- Real-time predictions
- Model and preprocessing artifacts stored using Pickle
=======
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
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997

---

## 🛠️ Tech Stack

<<<<<<< HEAD
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
=======
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
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997

---

## 📂 Project Structure

```text
<<<<<<< HEAD
Customer_Churn_Prediction/
│
├── data/
│   └── Churn_Modelling.csv
│
=======
New-customer-churn-prediction/
│
├── app.py
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_order.pkl
│
├── notebooks/
<<<<<<< HEAD
│   └── churn_training.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📈 Machine Learning Pipeline

### 1. Data Collection

- Bank Customer Churn Dataset

### 2. Data Preprocessing

- Removed non-predictive columns:
  - RowNumber
  - CustomerId
  - Surname

### 3. Feature Engineering

- Encoded categorical variables:
  - Geography
  - Gender

### 4. Train-Test Split

- Split dataset into training and testing sets

### 5. Feature Scaling

- Applied StandardScaler to numerical features

### 6. Model Training

- Trained a Machine Learning classification model to predict customer churn

### 7. Model Evaluation

- Evaluated model performance using:
  - Accuracy Score
  - Classification Report
  - Confusion Matrix

### 8. Model Persistence

Saved the following artifacts:

#### churn_model.pkl

Stores the trained machine learning model.

#### scaler.pkl

Stores the fitted StandardScaler used during preprocessing.

#### feature_order.pkl

Stores the feature order used during training to ensure consistency during prediction.

---

## 🎯 Prediction Output

The application predicts:

- **Churn** → Customer is likely to leave the bank.
- **No Churn** → Customer is likely to stay with the bank.

---

## ▶️ Run Locally
=======
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
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997

### Clone Repository

```bash
<<<<<<< HEAD
git clone https://github.com/Bhoomika08-MAY/customer-churn-prediction.git
```

### Navigate to Project Folder

```bash
cd customer-churn-prediction
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
=======
git clone https://github.com/Bhoomika08-MAY/New-customer-churn-prediction.git
cd New-customer-churn-prediction
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997
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

<<<<<<< HEAD
## 💡 Skills Demonstrated

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Machine Learning
- Feature Scaling
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- Git & GitHub

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Building an end-to-end machine learning workflow
- Handling customer churn prediction problems
- Preparing data for machine learning models
- Saving and loading trained models
- Deploying machine learning applications using Streamlit

---

## 👩‍💻 Developer

**Bhoomika Maleyur**

GitHub: https://github.com/Bhoomika08-MAY
=======
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
>>>>>>> 6bcff2982bc0170b1ad3c6d1597477a5c903e997
