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

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📂 Project Structure

```text
Customer_Churn_Prediction/
│
├── data/
│   └── Churn_Modelling.csv
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_order.pkl
│
├── notebooks/
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

### Clone Repository

```bash
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