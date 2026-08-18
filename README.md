# 🏦 Credit Risk Intelligence Platform

🐍 **Python**   ◈   🤖 **Machine Learning**   ◈   ⚖️ **SMOTE**   ◈   🔍 **SHAP**   ◈   🚀 **Streamlit**   ◈   🗄️ **SQL**

**An end-to-end machine learning and analytics platform for analyzing loan default risk and supporting data-driven credit-risk decisions.**

[![Live Demo](https://img.shields.io/badge/🚀-Live%20Demo-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)](https://streamlit.io/)

---

# 🚀 Live Demo

### Explore the Interactive Credit Risk Dashboard

**Live Application:**
https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/

The application provides interactive credit-risk analytics, model performance comparison, explainable AI visualizations, and individual loan-risk prediction.

---

# 📖 Overview

**Credit Risk Intelligence Platform** is an end-to-end machine learning and analytics solution designed to analyze loan default risk and support data-driven credit decisions.

The platform combines:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* SQL Business Analysis
* Imbalanced Learning
* Machine Learning Classification
* Model Evaluation
* Explainable AI using SHAP
* Interactive Streamlit Dashboards
* Individual Loan-Risk Prediction

The system transforms historical loan-level data into actionable credit-risk insights and demonstrates how machine learning can support automated risk assessment.

---

# 🎯 Problem Statement

Financial institutions process a large number of loan applications and need reliable methods to identify applicants who may have a higher probability of default.

Traditional manual assessment can be:

* Time-consuming
* Difficult to scale
* Dependent on manual analysis
* Challenging when dealing with large datasets

The objective of this project is to build a **Credit Risk Intelligence Platform** capable of analyzing borrower and loan characteristics, identifying risky patterns, predicting default risk, comparing machine learning models, and explaining model predictions.

---

# 💡 Proposed Solution

The platform follows an end-to-end credit-risk analytics workflow:

```text
Raw Loan Data
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Train / Test Split
      │
      ▼
SMOTE Class Balancing
      │
      ▼
Machine Learning Models
      │
      ▼
Model Evaluation
      │
      ▼
SHAP Explainability
      │
      ▼
Streamlit Risk Dashboard
      │
      ▼
Live Loan-Risk Prediction
```

---

# ✨ Key Features

### 📊 Executive Risk Dashboard

Provides a portfolio-level overview of credit risk through:

* Total Loans
* Defaulted Loans
* Default Rate
* Average Loan Amount
* Default Distribution
* Grade-wise Default Analysis
* Loan Amount Distribution

### ⚠️ Risk Analytics

Provides detailed analysis of borrower and loan characteristics associated with credit risk.

Key areas include:

* Loan characteristics
* Interest rates
* Borrower income
* Debt-to-income ratio
* Credit inquiries
* Delinquencies
* Revolving utilization
* Credit account information
* Risk patterns across loan grades

### 🤖 Model Performance

Compares multiple classification algorithms:

* Logistic Regression
* Random Forest
* XGBoost

Performance is evaluated using:

* Accuracy
* F1 Score
* ROC-AUC

### 🔍 Explainable AI

SHAP is used to interpret machine learning predictions and understand the factors influencing model output.

The project includes:

* SHAP Feature Importance
* SHAP Summary Plot
* SHAP Waterfall Plot

### 🔮 Live Risk Prediction

Users can enter loan and borrower information through the Streamlit application and obtain a model-based credit-risk prediction.

---

# 🛠️ Tech Stack

| Category            | Technologies              |
| ------------------- | ------------------------- |
| Programming         | Python                    |
| Data Analysis       | Pandas, NumPy             |
| Machine Learning    | Scikit-learn, XGBoost     |
| Imbalanced Learning | imbalanced-learn, SMOTE   |
| Explainable AI      | SHAP                      |
| Visualization       | Plotly, Matplotlib        |
| Dashboard           | Streamlit                 |
| Model Persistence   | Joblib                    |
| Database / Analysis | SQL                       |
| Development         | Jupyter Notebook, VS Code |
| Version Control     | Git, GitHub               |

---

# 📂 Project Structure

```text
Credit-Risk-Intelligence-Platform/
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 1_Executive_Dashboard.py
│       ├── 2_Risk_Analytics.py
│       ├── 3_Model_Performance.py
│       └── 4_Live_Prediction.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│   ├── logistic.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── scaler.pkl
│
├── notebook/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_sql_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_shap_explainability.ipynb
│
├── screenshots/
│   ├── executive_dashboard.png
│   ├── risk_analytics.png
│   ├── model_performance.png
│   ├── live_prediction.png
│   ├── shap_feature_importance.png
│   ├── shap_summary.png
│   └── shap_waterfall.png
│
├── sql/
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
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📚 Dataset

The project uses a **LendingClub loan dataset** containing historical loan and borrower information.

The processed modeling dataset contains approximately:

* **1,303,638 records**
* **93 modeling features**

The target variable is:

```text
default
```

Where:

```text
0 → Non-Default
1 → Default
```

---

# 📋 Important Dataset Features

The analysis uses important loan, borrower, financial, and credit-related variables.

Examples include:

| Feature               | Description                             |
| --------------------- | --------------------------------------- |
| `loan_amnt`           | Loan amount                             |
| `term`                | Loan repayment term                     |
| `int_rate`            | Interest rate                           |
| `installment`         | Monthly installment                     |
| `grade`               | Loan grade                              |
| `sub_grade`           | Loan sub-grade                          |
| `emp_length`          | Employment length                       |
| `home_ownership`      | Home ownership status                   |
| `annual_inc`          | Annual income                           |
| `verification_status` | Income verification status              |
| `purpose`             | Loan purpose                            |
| `dti`                 | Debt-to-income ratio                    |
| `delinq_2yrs`         | Delinquencies in the previous two years |
| `inq_last_6mths`      | Credit inquiries                        |
| `open_acc`            | Number of open accounts                 |
| `pub_rec`             | Public record count                     |
| `revol_bal`           | Revolving credit balance                |
| `revol_util`          | Revolving credit utilization            |
| `total_acc`           | Total credit accounts                   |

---

# ⚙️ Data Preprocessing

The raw LendingClub dataset contains a large number of columns and records.

The preprocessing pipeline includes:

1. Selecting relevant variables
2. Removing unnecessary columns
3. Handling missing values
4. Converting categorical variables
5. Encoding categorical features
6. Preparing numerical features
7. Creating the final modeling dataset
8. Separating target and predictor variables

The processed data is then used for machine learning model development.

---

# 🔧 Feature Engineering

Additional risk-oriented financial features were created to provide the models with more meaningful information about borrower financial behavior.

### Loan-to-Income Ratio

```text
loan_to_income = loan_amnt / annual_inc
```

Measures the size of the loan relative to the borrower's annual income.

### Installment-to-Income Ratio

```text
installment_to_income = installment / annual_inc
```

Represents the monthly loan payment burden relative to income.

### Open-to-Total Accounts Ratio

```text
open_to_total_accounts = open_acc / total_acc
```

Provides information about the proportion of currently open credit accounts.

### Credit Issue Count

A combined indicator based on credit-related negative signals such as:

* Delinquencies
* Public records
* Recent inquiries

### Revolving Balance-to-Income Ratio

```text
revol_bal_to_income = revol_bal / annual_inc
```

Provides an additional indicator of revolving credit burden relative to income.

---

# ⚖️ Class Imbalance Handling

Loan-default prediction is an **imbalanced classification problem**.

The dataset contains significantly more non-default observations than default observations.

To improve the representation of the minority class during model training, the project uses:

### SMOTE

**SMOTE — Synthetic Minority Over-sampling Technique**

SMOTE generates synthetic minority-class observations instead of simply duplicating existing records.

The workflow is:

```text
Original Training Data
        │
        ▼
Train / Test Split
        │
        ├──────────────► Test Data
        │                 (Untouched)
        ▼
      SMOTE
        │
        ▼
Balanced Training Data
        │
        ▼
Machine Learning
```

The test dataset remains separate to provide an unbiased evaluation of model performance.

---

# 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated.

## 1. Logistic Regression

Logistic Regression was used as a baseline classification model.

Advantages:

* Simple
* Interpretable
* Fast
* Useful as a benchmark model

---

## 2. Random Forest

Random Forest is an ensemble learning algorithm based on multiple decision trees.

It can capture:

* Non-linear relationships
* Feature interactions
* Complex patterns in structured data

---

## 3. XGBoost

XGBoost is a gradient-boosting algorithm designed for high-performance classification and regression on structured/tabular datasets.

It is particularly useful for:

* Complex relationships
* Non-linear patterns
* Feature interactions
* Large tabular datasets

---

# 📈 Model Performance

The models were evaluated on the held-out test dataset.

| Model               |   Accuracy |   F1 Score |    ROC-AUC |
| ------------------- | ---------: | ---------: | ---------: |
| Logistic Regression | **66.10%** | **42.90%** | **70.84%** |
| Random Forest       | **66.06%** | **43.07%** | **71.24%** |
| XGBoost             | **80.32%** | **13.58%** | **71.94%** |

---

# 🔎 Model Performance Interpretation

The results demonstrate why multiple evaluation metrics are important in credit-risk classification.

### XGBoost

XGBoost achieved:

* Highest Accuracy: **80.32%**
* Highest ROC-AUC: **71.94%**

However, its F1 Score was only **13.58%**.

### Random Forest

Random Forest achieved:

* Accuracy: **66.06%**
* F1 Score: **43.07%**
* ROC-AUC: **71.24%**

### Logistic Regression

Logistic Regression achieved:

* Accuracy: **66.10%**
* F1 Score: **42.90%**
* ROC-AUC: **70.84%**

### Important Observation

Accuracy alone is not sufficient for evaluating a credit-risk model, especially when the target classes are imbalanced.

A model can achieve high accuracy while still performing poorly at identifying actual defaults.

Therefore, **F1 Score, ROC-AUC, recall, precision, and threshold analysis** should also be considered when selecting a production credit-risk model.

---

# 🔍 Explainable AI with SHAP

**SHAP — SHapley Additive exPlanations** is used to interpret machine learning predictions.

The purpose of SHAP analysis is to understand:

* Which features influence predictions
* Which variables contribute to higher risk
* Which variables contribute to lower risk
* How individual predictions are formed
* Overall feature importance

---

# 📊 SHAP Visualizations

The project includes three major SHAP visualizations.

### SHAP Feature Importance

Shows the most influential features used by the model.

### SHAP Summary Plot

Provides a global overview of feature importance and the direction of feature influence.

### SHAP Waterfall Plot

Explains how individual features contribute to a specific prediction.

---

# 🖥️ Streamlit Dashboard

The platform is deployed as an interactive Streamlit web application.

### Application Structure

```text
Home
 │
 ├── 📊 Executive Dashboard
 │
 ├── ⚠️ Risk Analytics
 │
 ├── 🤖 Model Performance
 │
 └── 🔮 Live Prediction
```

---

# 📊 Executive Risk Dashboard

The Executive Dashboard provides a high-level view of the loan portfolio.

It includes:

* Total loan applications
* Defaulted loans
* Default rate
* Average loan amount
* Default distribution
* Grade-wise risk analysis
* Portfolio-level visualizations

![Executive Risk Dashboard](screenshots/executive_dashboard.png)

---

# ⚠️ Risk Analytics

The Risk Analytics section provides deeper analysis of borrower and loan characteristics.

It helps identify relationships between:

* Loan amount
* Interest rate
* Income
* DTI
* Credit utilization
* Delinquencies
* Credit inquiries
* Loan grades

![Risk Analytics Dashboard](screenshots/risk_analytics.png)

---

# 🤖 Model Performance Dashboard

The Model Performance page compares the trained classification models using key evaluation metrics.

![Model Performance Dashboard](screenshots/model_performance.png)

---

# 🔮 Live Risk Prediction

The Live Prediction page allows users to enter applicant-level loan information and generate a model-based risk prediction.

The workflow is:

```text
Applicant Information
        ↓
Feature Processing
        ↓
Feature Scaling
        ↓
Trained ML Model
        ↓
Risk Prediction
```

![Live Prediction Dashboard](screenshots/live_prediction.png)

---

# 🔍 SHAP Feature Importance

The SHAP feature-importance visualization highlights the variables that have the greatest influence on the model.

![SHAP Feature Importance](screenshots/shap_feature_importance.png)

---

# 📈 SHAP Summary Plot

The SHAP summary plot provides a global explanation of model behavior across observations.

![SHAP Summary Plot](screenshots/shap_summary.png)

---

# 🧩 SHAP Waterfall Plot

The SHAP waterfall visualization explains the contribution of individual features for a specific model prediction.

![SHAP Waterfall Plot](screenshots/shap_waterfall.png)

---

# 🔄 End-to-End Project Workflow

```text
                 ┌──────────────────┐
                 │   LendingClub    │
                 │    Loan Data     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Data Cleaning &  │
                 │ Preprocessing    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Exploratory Data │
                 │     Analysis     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Feature          │
                 │ Engineering      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Train / Test     │
                 │     Split        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │      SMOTE       │
                 │ Training Data    │
                 └────────┬─────────┘
                          │
                          ▼
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        Logistic      Random       XGBoost
        Regression    Forest
              │           │           │
              └───────────┼───────────┘
                          ▼
                 ┌──────────────────┐
                 │ Model Evaluation │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ SHAP             │
                 │ Explainability   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Streamlit        │
                 │ Dashboard        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Live Risk        │
                 │ Prediction       │
                 └──────────────────┘
```

---

# 💼 Business Problems Addressed

The platform demonstrates how machine learning and analytics can help address several credit-risk problems.

### Risk Identification

Identify applicants and loan characteristics associated with higher default risk.

### Portfolio Monitoring

Monitor default rates and risk patterns across different loan segments.

### Customer Assessment

Analyze borrower financial and credit characteristics.

### Decision Support

Provide data-driven information that can support credit-risk assessment.

### Explainability

Help analysts understand why a model produces a particular prediction.

### Scalability

Automate parts of the risk-analysis process for large loan datasets.

---

# 📊 Key Business Insights

The platform can be used to investigate questions such as:

* Which loan grades have higher default rates?
* How does loan amount relate to default risk?
* Does higher debt-to-income ratio correspond to higher risk?
* Which borrower financial characteristics influence predictions?
* Which features are most important to the machine learning model?
* How do different classification algorithms perform?
* How can model predictions be explained to analysts?

---

# 🗄️ SQL Analysis

SQL is incorporated into the project for business-oriented analysis of loan data.

Example analytical use cases include:

* Default analysis by loan grade
* Loan portfolio aggregation
* Average loan amount
* Default counts
* Risk segmentation
* Borrower-level aggregation
* Financial metric analysis

SQL helps bridge the gap between raw data and business decision-making.

---

# 💾 Model Persistence

Trained machine learning models and preprocessing objects are saved using **Joblib**.

Stored model artifacts include:

```text
models/
│
├── logistic.pkl
├── random_forest.pkl
├── xgboost.pkl
└── scaler.pkl
```

This allows the Streamlit application to load trained models without retraining them every time the application starts.

---

# 🚀 How to Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
```

```bash
cd Credit-Risk-Intelligence-Platform
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the Streamlit Application

```bash
streamlit run app/Home.py
```

The application will open in your default web browser.

---

# 🌐 Online Application

The project is deployed using Streamlit.

### 🚀 Live Demo

https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/

### 💻 GitHub Repository

https://github.com/aditya280505/Credit-Risk-Intelligence-Platform

---

# 🔮 Future Improvements

The platform can be further improved with:

* Minority-class recall optimization
* F1-score optimization
* Hyperparameter tuning
* Probability calibration
* Optimal classification threshold selection
* Precision-Recall analysis
* Additional credit-risk metrics
* Model monitoring
* Data drift detection
* Automated model retraining
* Real-time prediction API
* Cloud database integration
* Real-time loan data integration
* Advanced risk segmentation
* Customer churn/default prediction
* Model governance and audit logging

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python for data analytics
* Pandas and NumPy
* Data preprocessing
* Exploratory data analysis
* Feature engineering
* SQL analytics
* Classification algorithms
* Random Forest
* XGBoost
* Logistic Regression
* Imbalanced learning
* SMOTE
* Model evaluation
* ROC-AUC
* F1 Score
* Explainable AI
* SHAP
* Streamlit
* Git and GitHub
* Machine learning deployment

---

# 🧠 Skills Demonstrated

```text
Python
   │
   ├── Data Cleaning
   ├── EDA
   ├── Feature Engineering
   └── Machine Learning
           │
           ├── Logistic Regression
           ├── Random Forest
           └── XGBoost

SQL
   │
   └── Business Analytics

Explainable AI
   │
   └── SHAP

Deployment
   │
   └── Streamlit

Version Control
   │
   └── Git + GitHub
```

---

# 👨‍💻 Author

## Aditya Pravin Borgaonkar

**B.Tech Computer Science Engineering**
**Artificial Intelligence and Analytics**
**MIT Art, Design & Technology University**

### Areas of Interest

* Artificial Intelligence
* Data Analytics
* Machine Learning
* Credit Risk Analytics
* Business Intelligence
* Explainable AI

### GitHub

https://github.com/aditya280505

### LinkedIn

https://linkedin.com/in/adityaborgaonkar280505/

### Email

[borgaonkaraditya1@gmail.com](mailto:borgaonkaraditya1@gmail.com)

---

# ⭐ Project Goal

The goal of this project is to demonstrate an **end-to-end Credit Risk Intelligence Platform** that combines:

**Data Analytics + SQL + Machine Learning + Imbalanced Learning + Explainable AI + Interactive Dashboards**

The project demonstrates how historical loan data can be transformed into meaningful risk insights and machine learning predictions through a complete analytics pipeline.

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star** on GitHub.

It helps others discover the project and supports continued development.

---

## 🚀 Explore the Project

[![🚀 Open Live Dashboard](https://img.shields.io/badge/🚀%20OPEN%20LIVE%20DASHBOARD-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)

[![💻 View on GitHub](https://img.shields.io/badge/💻%20VIEW%20ON%20GITHUB-black?style=for-the-badge\&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)

---

**Built with Python, Machine Learning, SQL, SHAP, and Streamlit.**
