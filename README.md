````markdown
# 🏦 Credit Risk Intelligence Platform

🐍 **Python** &nbsp; ◈ &nbsp; 🤖 **Machine Learning** &nbsp; ◈ &nbsp; ⚖️ **SMOTE** &nbsp; ◈ &nbsp; 🔍 **SHAP** &nbsp; ◈ &nbsp; 🚀 **Streamlit** &nbsp; ◈ &nbsp; 🗄️ **SQL**

**An end-to-end machine learning and analytics platform for analyzing loan default risk and supporting data-driven credit-risk decisions.**

[![Live Demo](https://img.shields.io/badge/🚀-Live%20Demo-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

---

# 🚀 Live Demo

### Explore the Interactive Credit Risk Dashboard

**Live Application:**

[https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)

The application provides interactive credit-risk analytics, portfolio insights, model-performance comparison, explainable AI visualizations, and individual loan-risk prediction.

---

# 📖 Overview

**Credit Risk Intelligence Platform** is an end-to-end machine learning and analytics solution designed to analyze loan default risk and support data-driven credit-risk decisions.

The platform combines:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- SQL Business Analysis
- Imbalanced Learning
- Machine Learning Classification
- Model Evaluation
- Explainable AI using SHAP
- Interactive Streamlit Dashboards
- Individual Loan-Risk Prediction

The system transforms historical loan-level data into meaningful risk insights and demonstrates how machine learning can support automated credit-risk assessment.

> **Important:** This project is an educational and portfolio demonstration. Predictions should not be used as the sole basis for real-world lending decisions.

---

# 🎯 Problem Statement

Financial institutions process large numbers of loan applications and need reliable methods to identify applicants who may have a higher probability of default.

Traditional manual assessment can be:

- Time-consuming
- Difficult to scale
- Dependent on manual analysis
- Challenging when working with large datasets
- Difficult to standardize consistently

The objective of this project is to build a **Credit Risk Intelligence Platform** capable of:

- Analyzing borrower and loan characteristics
- Identifying risky patterns
- Predicting loan default risk
- Comparing multiple machine learning models
- Explaining model predictions
- Providing portfolio-level risk insights
- Supporting data-driven credit-risk analysis

---

# 💡 Proposed Solution

The platform follows a complete end-to-end credit-risk analytics workflow:

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
````

---

# ✨ Key Features

## 📊 Executive Risk Dashboard

Provides a high-level overview of the loan portfolio through:

* Total Loans
* Defaulted Loans
* Default Rate
* Average Loan Amount
* Default Distribution
* Grade-wise Default Analysis
* Loan Amount Distribution

---

## ⚠️ Risk Analytics

Provides detailed analysis of borrower and loan characteristics associated with credit risk.

Key areas include:

* Loan characteristics
* Interest rates
* Borrower income
* Debt-to-income ratio
* Credit inquiries
* Delinquencies
* Revolving credit utilization
* Credit account information
* Risk patterns across loan grades

---

## 🤖 Model Performance

Compares three classification algorithms:

* Logistic Regression
* Random Forest
* XGBoost

Performance is evaluated using:

* Accuracy
* F1 Score
* ROC-AUC

---

## 🔍 Explainable AI

**SHAP (SHapley Additive exPlanations)** is used to understand model behavior and interpret predictions.

The project includes:

* SHAP Feature Importance
* SHAP Summary Plot
* SHAP Waterfall Plot

---

## 🔮 Live Risk Prediction

Users can enter applicant-level loan information through the Streamlit application and generate a model-based credit-risk prediction.

The prediction pipeline processes the applicant information, applies the required preprocessing and scaling, and generates a model prediction.

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

The project uses a **LendingClub historical loan dataset** containing loan and borrower information.

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

The analysis uses loan, borrower, financial, and credit-related variables.

| Feature               | Description                         |
| --------------------- | ----------------------------------- |
| `loan_amnt`           | Loan amount                         |
| `term`                | Loan repayment term                 |
| `int_rate`            | Interest rate                       |
| `installment`         | Monthly installment                 |
| `grade`               | Loan grade                          |
| `sub_grade`           | Loan sub-grade                      |
| `emp_length`          | Employment length                   |
| `home_ownership`      | Home ownership status               |
| `annual_inc`          | Annual income                       |
| `verification_status` | Income verification status          |
| `purpose`             | Loan purpose                        |
| `dti`                 | Debt-to-income ratio                |
| `delinq_2yrs`         | Delinquencies in previous two years |
| `inq_last_6mths`      | Recent credit inquiries             |
| `open_acc`            | Number of open accounts             |
| `pub_rec`             | Public record count                 |
| `revol_bal`           | Revolving credit balance            |
| `revol_util`          | Revolving credit utilization        |
| `total_acc`           | Total credit accounts               |

---

# ⚙️ Data Preprocessing

The LendingClub dataset contains a large number of records and variables.

The preprocessing pipeline includes:

1. Selecting relevant variables
2. Removing unnecessary columns
3. Handling missing values
4. Converting categorical variables
5. Encoding categorical features
6. Preparing numerical features
7. Creating the final modeling dataset
8. Separating target and predictor variables

The processed dataset is then used for machine learning model development.

---

# 🔧 Feature Engineering

Additional risk-oriented financial features were created to provide the models with more meaningful information about borrower financial behavior.

## Loan-to-Income Ratio

```text
loan_to_income = loan_amnt / annual_inc
```

Measures the size of the requested loan relative to the borrower's annual income.

---

## Installment-to-Income Ratio

```text
installment_to_income = installment / annual_inc
```

Represents the monthly payment burden relative to annual income.

---

## Open-to-Total Accounts Ratio

```text
open_to_total_accounts = open_acc / total_acc
```

Provides information about the proportion of currently open credit accounts.

---

## Credit Issue Count

A composite indicator based on credit-related risk signals such as:

* Delinquencies
* Public records
* Recent credit inquiries

---

## Revolving Balance-to-Income Ratio

```text
revol_bal_to_income = revol_bal / annual_inc
```

Provides an additional indicator of revolving credit burden relative to income.

---

# ⚖️ Class Imbalance Handling

Loan-default prediction is an **imbalanced classification problem** because non-default observations significantly outnumber default observations.

To improve representation of the minority class during training, the project uses:

## SMOTE

**SMOTE — Synthetic Minority Over-sampling Technique**

SMOTE generates synthetic minority-class observations rather than simply duplicating existing records.

The workflow is:

```text
Original Dataset
      │
      ▼
Train / Test Split
      │
      ├──────────────► Test Data
      │                 (Untouched)
      │
      ▼
    SMOTE
      │
      ▼
Balanced Training Data
      │
      ▼
Machine Learning Models
```

The test dataset remains untouched so that final evaluation provides a more unbiased estimate of model performance.

---

# 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated.

## 1. Logistic Regression

Logistic Regression was used as a baseline classification model.

Advantages:

* Simple
* Interpretable
* Fast
* Useful as a benchmark

---

## 2. Random Forest

Random Forest is an ensemble learning algorithm based on multiple decision trees.

It can capture:

* Non-linear relationships
* Feature interactions
* Complex patterns
* Structured tabular-data relationships

---

## 3. XGBoost

XGBoost is a gradient-boosting algorithm designed for high-performance classification and regression on structured datasets.

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

The results demonstrate why multiple evaluation metrics are important for credit-risk classification.

### XGBoost

XGBoost achieved:

* Highest Accuracy: **80.32%**
* Highest ROC-AUC: **71.94%**

However, its F1 Score was only **13.58%**.

This indicates that its high accuracy does not necessarily translate into strong minority-class detection.

### Random Forest

Random Forest achieved:

* Accuracy: **66.06%**
* F1 Score: **43.07%**
* ROC-AUC: **71.24%**

Among the evaluated models, Random Forest provides the strongest F1 score.

### Logistic Regression

Logistic Regression achieved:

* Accuracy: **66.10%**
* F1 Score: **42.90%**
* ROC-AUC: **70.84%**

It provides a useful interpretable baseline for comparison.

### Important Observation

Accuracy alone should not be used to select a credit-risk model when the target classes are imbalanced.

Metrics such as:

* Precision
* Recall
* F1 Score
* ROC-AUC
* Precision-Recall analysis
* Decision-threshold performance

should also be considered.

For a real-world credit-risk system, the model and decision threshold would require additional validation, calibration, fairness analysis, and domain-specific risk evaluation.

---

# 🔍 Explainable AI with SHAP

**SHAP — SHapley Additive exPlanations** is used to interpret machine learning predictions.

SHAP helps answer:

* Which features influence predictions?
* Which variables contribute toward higher predicted risk?
* Which variables contribute toward lower predicted risk?
* Which features are globally most important?
* How do individual features influence a specific prediction?

---

# 📊 SHAP Visualizations

The project includes three major SHAP visualizations.

### SHAP Feature Importance

Shows the most influential features used by the model.

### SHAP Summary Plot

Provides a global overview of feature importance and feature impact across observations.

### SHAP Waterfall Plot

Explains how individual features contribute to a specific model prediction.

---

# 🖥️ Streamlit Dashboard

The platform is deployed as an interactive multi-page Streamlit web application.

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

### Dashboard Preview

![Executive Risk Dashboard](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/executive_dashboard.png?raw=true)

---

# ⚠️ Risk Analytics

The Risk Analytics section provides deeper analysis of borrower and loan characteristics.

It helps investigate relationships between:

* Loan amount
* Interest rate
* Income
* DTI
* Credit utilization
* Delinquencies
* Credit inquiries
* Loan grades

### Dashboard Preview

![Risk Analytics Dashboard](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/risk_analytics.png?raw=true)

---

# 🤖 Model Performance Dashboard

The Model Performance page compares the trained classification models using key evaluation metrics.

### Dashboard Preview

![Model Performance Dashboard](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/model_performance.png?raw=true)

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

### Dashboard Preview

![Live Prediction Dashboard](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/live_prediction.png?raw=true)

---

# 🔍 SHAP Feature Importance

The SHAP feature-importance visualization highlights the variables that have the greatest influence on model predictions.

![SHAP Feature Importance](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_feature_importance.png?raw=true)

---

# 📈 SHAP Summary Plot

The SHAP summary plot provides a global explanation of model behavior across observations.

![SHAP Summary Plot](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_summary.png?raw=true)

---

# 🧩 SHAP Waterfall Plot

The SHAP waterfall visualization explains the contribution of individual features for a specific model prediction.

![SHAP Waterfall Plot](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_waterfall.png?raw=true)

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

The platform demonstrates how machine learning and analytics can support several credit-risk use cases.

### Risk Identification

Identify loan and borrower characteristics associated with higher default risk.

### Portfolio Monitoring

Monitor default rates and risk patterns across different loan segments.

### Borrower Assessment

Analyze borrower financial and credit characteristics.

### Decision Support

Provide data-driven insights that can support credit-risk assessment.

### Explainability

Help analysts understand the factors influencing model predictions.

### Scalability

Automate parts of the risk-analysis process for large loan datasets.

---

# 📊 Key Business Questions

The platform can be used to investigate questions such as:

* Which loan grades have higher default rates?
* How does loan amount relate to default risk?
* Does a higher debt-to-income ratio correspond to higher risk?
* Which borrower characteristics influence predictions?
* Which features are most important to the model?
* How do different classification algorithms perform?
* How can individual model predictions be explained?
* Which risk indicators deserve further investigation?

---

# 🗄️ SQL Analysis

SQL is incorporated into the project for business-oriented analysis of loan data.

Example analytical use cases include:

* Default analysis by loan grade
* Loan portfolio aggregation
* Average loan amount analysis
* Default counts
* Risk segmentation
* Borrower-level aggregation
* Financial metric analysis

SQL helps bridge the gap between raw loan data and business-oriented credit-risk insights.

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

This allows the Streamlit application to load trained models and preprocessing objects without retraining them whenever the application starts.

---

# 🚀 How to Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
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

### macOS / Linux

```bash
source .venv/bin/activate
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

# 🌐 Project Links

| Resource             | Link                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 🚀 Live Demo         | [Open Streamlit Application](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/) |
| 💻 GitHub Repository | [View Source Code](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)                              |
| 🐛 Issues            | [Report an Issue](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/issues)                        |

---

# 🔮 Future Improvements

The current platform provides a strong foundation for credit-risk analysis. Future improvements could include:

* Minority-class recall optimization
* F1-score optimization
* Hyperparameter tuning
* Probability calibration
* Optimal classification threshold selection
* Precision-Recall analysis
* Cost-sensitive learning
* Additional credit-risk metrics
* Model monitoring
* Data drift detection
* Automated model retraining
* Real-time prediction API
* Cloud database integration
* Real-time loan data integration
* Advanced risk segmentation
* Model governance and audit logging
* Fairness and bias analysis

---

# ⚠️ Current Limitations

The current project is a portfolio and educational implementation rather than a production lending system.

Key limitations include:

* Model performance has not been validated on live production data.
* XGBoost currently shows a significantly lower F1 score despite higher accuracy.
* Classification thresholds have not been extensively optimized.
* Probability calibration has not been implemented.
* Real-time data ingestion is not currently implemented.
* Production-level model monitoring is not implemented.
* Fairness and regulatory validation would be required before real-world deployment.

These limitations also provide clear directions for future development.

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python for data analytics
* Pandas and NumPy
* Data preprocessing
* Exploratory data analysis
* Feature engineering
* SQL analytics
* Logistic Regression
* Random Forest
* XGBoost
* Imbalanced classification
* SMOTE
* Model evaluation
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Explainable AI
* SHAP
* Streamlit
* Model persistence
* Git and GitHub
* End-to-end machine learning deployment

---

# 🧠 Skills Demonstrated

```text
Python
   │
   ├── Data Cleaning
   ├── Exploratory Data Analysis
   ├── Feature Engineering
   └── Machine Learning
           │
           ├── Logistic Regression
           ├── Random Forest
           └── XGBoost

SQL
   │
   └── Business Analytics

Imbalanced Learning
   │
   └── SMOTE

Explainable AI
   │
   └── SHAP

Visualization
   │
   ├── Plotly
   └── Matplotlib

Deployment
   │
   └── Streamlit

Model Persistence
   │
   └── Joblib

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

[https://github.com/aditya280505](https://github.com/aditya280505)

### LinkedIn

[https://linkedin.com/in/adityaborgaonkar280505/](https://linkedin.com/in/adityaborgaonkar280505/)

### Email

[borgaonkaraditya1@gmail.com](mailto:borgaonkaraditya1@gmail.com)

---

# ⭐ Project Goal

The goal of this project is to demonstrate an **end-to-end Credit Risk Intelligence Platform** that combines:

**Data Analytics + SQL + Machine Learning + Imbalanced Learning + Explainable AI + Interactive Dashboards**

The project demonstrates how historical loan data can be transformed into meaningful credit-risk insights and machine learning predictions through a complete analytics pipeline.

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star** on GitHub.

It helps others discover the project and supports continued development.

---

<div align="center">

### 🚀 Explore the Project

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Credit_Risk_Dashboard-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)

[![GitHub](https://img.shields.io/badge/💻_GitHub-Credit_Risk_Intelligence_Platform-black?style=for-the-badge\&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)

<br>

**Built with Python, Machine Learning, SQL, SHAP, and Streamlit.**

</div>
```
