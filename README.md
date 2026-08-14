Credit Risk Intelligence Platform

An end-to-end machine learning and analytics platform for analyzing loan default risk and supporting credit-risk decisions.

The project combines Python, SQL, machine learning, explainable AI, and Streamlit to transform loan-level data into actionable risk insights.

📌 Project Overview

Credit-risk teams need to identify potentially risky loan applications while reducing unnecessary manual review.

This project analyzes historical loan data, engineers financial and credit-risk features, trains multiple classification models, evaluates their performance, and presents the results through an interactive Streamlit dashboard.

Main Objectives

Analyze historical loan and borrower information

Identify patterns associated with loan defaults

Engineer meaningful financial-risk features

Handle class imbalance during model training

Compare multiple classification algorithms

Explain model predictions using SHAP

Provide an interactive credit-risk analytics dashboard

Support individual loan-risk prediction

🎯 Problem Statement

Financial institutions process a large number of loan applications and need reliable ways to identify applicants with higher default risk.

Manual assessment can be time-consuming and may not scale efficiently.

The objective of this project is to build a data-driven credit-risk intelligence platform that can:

Analyze borrower and loan characteristics

Identify high-risk patterns

Predict default risk using machine learning

Compare different classification models

Explain important factors behind predictions

Present risk insights through an interactive dashboard

💡 Proposed Solution

The platform follows an end-to-end machine learning workflow:

Raw Loan Data
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Class Imbalance Handling
      ↓
Train ML Models
      ↓
Model Evaluation
      ↓
SHAP Explainability
      ↓
Streamlit Risk Dashboard
      ↓
Live Risk Prediction

✨ Key Features

📊 Executive Risk Dashboard

Provides a high-level overview of the loan portfolio:

Total loans

Defaulted loans

Default rate

Average loan amount

Default distribution

Grade-wise default rate

Loan amount distribution

⚠️ Risk Analytics

Provides detailed analysis of borrower and loan risk factors, including financial indicators and credit-related patterns.

🤖 Model Performance

Compares:

Logistic Regression

Random Forest

XGBoost

Metrics include:

Accuracy

F1 Score

ROC-AUC

🔍 Explainable AI

SHAP is used to understand model behavior and identify important features contributing to predictions.

🔮 Live Prediction

Allows users to enter applicant information and obtain a model-based credit-risk prediction.

🛠️ Tech Stack

Category

Technologies

Programming

Python

Data Analysis

Pandas, NumPy

Machine Learning

Scikit-learn, XGBoost

Imbalanced Learning

imbalanced-learn / SMOTE

Explainable AI

SHAP

Visualization

Plotly, Matplotlib

Dashboard

Streamlit

Model Persistence

Joblib

Database / Analysis

SQL

Development

Jupyter Notebook, VS Code

Version Control

Git, GitHub

📂 Project Structure

Credit-Risk-Intelligence-Platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── sql/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_sql_analysis.ipynb
│   ├── 04_rfm_segmentation.ipynb
│   └── 05_sales_forecasting.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── imbalance_handling.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│   └── shap/
│
├── models/
│   ├── logistic.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── scaler.pkl
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Executive_Dashboard.py
│       ├── 2_Risk_Analytics.py
│       ├── 3_Model_Performance.py
│       └── 4_Live_Prediction.py
│
├── screenshots/
│   ├── executive_dashboard.png
│   ├── risk_analytics.png
│   ├── model_performance.png
│   ├── live_prediction.png
│   ├── shap_summary.png
│   ├── shap_feature_importance.png
│   └── shap_waterfall.png
│
├── requirements.txt
├── .gitignore
└── README.md

Update the notebook filenames above if your actual notebook names differ.

📚 Dataset

The project uses a LendingClub loan dataset containing historical loan and borrower information.

The processed modeling dataset contains approximately:

1,303,638 records
93 modeling features

Important variables include:

Loan amount

Interest rate

Installment

Loan grade

Sub-grade

Employment length

Annual income

Debt-to-income ratio

Delinquencies

Credit inquiries

Open accounts

Revolving balance

Revolving utilization

Total accounts

Loan-to-income ratio

Installment-to-income ratio

Credit issue count

Revolving-balance-to-income ratio

The target variable is:

default

where:

0 → Non-Default
1 → Default

⚙️ Feature Engineering

Additional risk-oriented features were created from the available financial variables.

Examples:

loan_to_income
installment_to_income
open_to_total_accounts
credit_issue_count
revol_bal_to_income

These features provide additional information about an applicant's financial burden and credit profile.

⚖️ Class Imbalance Handling

Loan-default prediction is an imbalanced classification problem.

SMOTE (Synthetic Minority Over-sampling Technique) was used during model training to improve the representation of the minority class.

The test dataset was kept separate for unbiased evaluation.

🤖 Machine Learning Models

Three classification algorithms were trained and compared:

1. Logistic Regression

Used as a baseline linear classification model.

2. Random Forest

An ensemble tree-based model capable of capturing nonlinear relationships.

3. XGBoost

A gradient-boosting model designed for strong predictive performance on structured/tabular data.

📈 Model Performance

Evaluation was performed on the held-out test dataset.

Model

Accuracy

F1 Score

ROC-AUC

Logistic Regression

66.10%

42.90%

70.84%

Random Forest

66.06%

43.07%

71.24%

XGBoost

80.32%

13.58%

71.94%

Important Observation

XGBoost achieved the highest accuracy and ROC-AUC among the evaluated models.

However, its F1 score was considerably lower than the other models. This highlights why accuracy alone should not be used to judge a credit-risk classification model, particularly when the classes are imbalanced.

🔍 SHAP Explainability

SHAP (SHapley Additive exPlanations) was used to interpret model predictions.

Generated visualizations include:

SHAP feature importance

SHAP summary plot

SHAP waterfall plot

These visualizations help explain which features have the greatest influence on model predictions.

🖥️ Streamlit Dashboard

The application contains four main sections:

Home
 │
 ├── Executive Dashboard
 ├── Risk Analytics
 ├── Model Performance
 └── Live Prediction

Executive Dashboard

Portfolio-level KPIs and default-risk trends.

Risk Analytics

Detailed borrower and loan-risk analysis.

Model Performance

Model comparison and evaluation metrics.

Live Prediction

Interactive applicant-level risk prediction.

📸 Screenshots

Executive Risk Dashboard



Risk Analytics



Model Performance



Live Prediction



SHAP Feature Importance



SHAP Summary



SHAP Waterfall



🚀 How to Run Locally

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Credit-Risk-Intelligence-Platform

2. Create a virtual environment

python -m venv .venv

3. Activate the environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

5. Run the Streamlit application

streamlit run app/Home.py

The application will open in your browser.

📊 Project Workflow

Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Train/Test Split
      ↓
SMOTE
      ↓
Model Training
      ↓
Model Evaluation
      ↓
SHAP Analysis
      ↓
Streamlit Dashboard
      ↓
Live Risk Prediction

🔮 Future Improvements

Improve minority-class recall and F1 score

Hyperparameter optimization

Probability calibration

Threshold optimization for risk classification

Additional credit-risk metrics

Model monitoring

Data drift detection

Automated model retraining

Cloud deployment

Real-time prediction API

More advanced risk segmentation

👨‍💻 Author

Aditya Borgaonkar

B.Tech Computer Science Engineering
Artificial Intelligence and Analytics

Interested in:

Artificial Intelligence

Data Analytics

Machine Learning

Credit Risk Analytics

Business Intelligence

⭐ Project Goal

The goal of this project is to demonstrate an end-to-end Credit Risk Intelligence Platform combining data analytics, machine learning, explainable AI, and interactive business dashboards.