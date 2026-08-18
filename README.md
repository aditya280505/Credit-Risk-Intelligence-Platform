````markdown
# Credit Risk Intelligence Platform

### End-to-End Machine Learning & Analytics Platform for Loan Default Risk

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-success?style=for-the-badge&logo=streamlit)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

**[Live Demo](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/) · [GitHub Repository](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform) · [Report an Issue](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/issues)**

---

## Table of Contents

- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Class Imbalance Handling](#class-imbalance-handling)
- [Machine Learning Models](#machine-learning-models)
- [Model Performance](#model-performance)
- [Explainable AI with SHAP](#explainable-ai-with-shap)
- [Dashboard](#dashboard)
- [Dashboard Screenshots](#dashboard-screenshots)
- [SQL Business Analytics](#sql-business-analytics)
- [Model Persistence](#model-persistence)
- [Business Use Cases](#business-use-cases)
- [Getting Started](#getting-started)
- [Live Application](#live-application)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## Overview

The **Credit Risk Intelligence Platform** is an end-to-end machine learning and analytics solution for analyzing loan default risk and supporting data-driven credit-risk decisions.

The project combines data analytics, SQL, financial feature engineering, machine learning, imbalanced classification, explainable AI, and interactive Streamlit dashboards into a single workflow.

The platform transforms historical LendingClub loan data into actionable portfolio insights and model-based risk predictions.

### Core Capabilities

- Loan portfolio analysis
- Borrower risk analysis
- Financial feature engineering
- Default-risk classification
- Imbalanced learning using SMOTE
- Machine learning model comparison
- SHAP-based model explainability
- Interactive risk dashboards
- Individual loan-risk prediction

---

## Project Objectives

The main objectives of the project are to:

- Analyze historical loan and borrower information
- Identify patterns associated with loan defaults
- Engineer meaningful financial-risk features
- Handle class imbalance during model training
- Train and compare multiple classification models
- Evaluate models using appropriate classification metrics
- Explain model predictions using SHAP
- Build an interactive credit-risk analytics dashboard
- Provide individual applicant-level risk prediction

---

## Key Features

| Module | Description |
|---|---|
| **Executive Dashboard** | Portfolio KPIs, total loans, default rate, average loan amount, and grade-wise risk analysis |
| **Risk Analytics** | Detailed analysis of borrower, loan, income, DTI, utilization, delinquency, and credit characteristics |
| **Model Performance** | Comparison of Logistic Regression, Random Forest, and XGBoost |
| **Explainable AI** | SHAP feature importance, summary plots, and individual prediction explanations |
| **Live Prediction** | Interactive applicant input and model-based loan-risk prediction |

---

## Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Imbalanced Learning | imbalanced-learn, SMOTE |
| Explainable AI | SHAP |
| Visualization | Plotly, Matplotlib |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| Business Analytics | SQL |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

---

## Project Architecture

```text
LendingClub Loan Data
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
SMOTE on Training Data
        │
        ├──────────────┬──────────────┐
        ▼              ▼              ▼
 Logistic Regression  Random Forest  XGBoost
        │              │              │
        └──────────────┼──────────────┘
                       ▼
               Model Evaluation
                       │
                       ▼
              SHAP Explainability
                       │
                       ▼
              Streamlit Dashboard
                       │
                       ▼
              Live Risk Prediction
````

---

## Project Structure

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

> Update the notebook filenames above if your actual repository uses different names.

---

## Dataset

The project uses a historical **LendingClub loan dataset** containing loan-level and borrower-related information.

### Dataset Scale

* Approximately **1,303,638 processed records**
* **93 modeling features**
* Binary target variable: `default`

```text
default = 0 → Non-Default
default = 1 → Default
```

### Important Variables

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
| `delinq_2yrs`         | Delinquencies during previous two years |
| `inq_last_6mths`      | Recent credit inquiries                 |
| `open_acc`            | Open credit accounts                    |
| `pub_rec`             | Public record count                     |
| `revol_bal`           | Revolving credit balance                |
| `revol_util`          | Revolving credit utilization            |
| `total_acc`           | Total credit accounts                   |

---

## Data Preprocessing

The preprocessing pipeline includes:

1. Selecting relevant variables
2. Removing unnecessary columns
3. Handling missing values
4. Cleaning data types
5. Encoding categorical variables
6. Preparing numerical features
7. Creating the final modeling dataset
8. Separating predictors and target

---

## Feature Engineering

Additional financial-risk features were engineered to capture borrower financial burden and credit behavior.

### Loan-to-Income Ratio

```python
loan_to_income = loan_amnt / annual_inc
```

Measures the loan amount relative to annual income.

### Installment-to-Income Ratio

```python
installment_to_income = installment / annual_inc
```

Represents the installment burden relative to income.

### Open-to-Total Accounts Ratio

```python
open_to_total_accounts = open_acc / total_acc
```

Represents the proportion of currently open credit accounts.

### Revolving Balance-to-Income Ratio

```python
revol_bal_to_income = revol_bal / annual_inc
```

Provides an additional measure of revolving-credit burden relative to income.

### Credit Issue Count

A composite risk indicator based on selected credit-related signals such as:

* Delinquencies
* Public records
* Recent credit inquiries

These engineered features provide additional information beyond the original raw variables.

---

## Class Imbalance Handling

Loan-default prediction is an imbalanced classification problem because non-default observations significantly outnumber default observations.

**SMOTE (Synthetic Minority Over-sampling Technique)** was used to improve minority-class representation during model training.

The workflow is:

```text
Original Dataset
       │
       ▼
Train / Test Split
       │
       ├──────────────► Test Set
       │                Untouched
       │
       ▼
Training Set
       │
       ▼
     SMOTE
       │
       ▼
Balanced Training Data
       │
       ▼
Model Training
```

SMOTE is applied **only to the training dataset**. The test dataset remains untouched to provide an unbiased evaluation of model performance.

---

## Machine Learning Models

Three classification models were trained and compared.

### 1. Logistic Regression

Used as a baseline linear classification model.

### 2. Random Forest

An ensemble tree-based model capable of capturing nonlinear relationships and feature interactions.

### 3. XGBoost

A gradient-boosting model designed for strong predictive performance on structured/tabular datasets.

---

## Model Performance

The models were evaluated using the held-out test dataset.

| Model               |   Accuracy | F1 Score |    ROC-AUC |
| ------------------- | ---------: | -------: | ---------: |
| Logistic Regression |     66.10% |   42.90% |     70.84% |
| Random Forest       |     66.06% |   43.07% |     71.24% |
| XGBoost             | **80.32%** |   13.58% | **71.94%** |

---

## Model Performance Analysis

The results highlight an important issue in imbalanced credit-risk classification: **accuracy alone can be misleading**.

### XGBoost

XGBoost achieved:

* Highest Accuracy: **80.32%**
* Highest ROC-AUC: **71.94%**
* F1 Score: **13.58%**

Although XGBoost achieved the highest accuracy and ROC-AUC, its much lower F1 score indicates weaker minority-class performance under the current classification threshold.

### Random Forest

Random Forest achieved:

* Accuracy: **66.06%**
* F1 Score: **43.07%**
* ROC-AUC: **71.24%**

It provides a more balanced F1/ROC-AUC profile than XGBoost under the current configuration.

### Logistic Regression

Logistic Regression achieved:

* Accuracy: **66.10%**
* F1 Score: **42.90%**
* ROC-AUC: **70.84%**

It provides a useful baseline for comparing the more complex models.

### Key Takeaway

For credit-risk classification, model evaluation should consider multiple metrics rather than accuracy alone.

Important metrics include:

* Precision
* Recall
* F1 Score
* ROC-AUC
* Precision-Recall AUC
* Classification threshold

The appropriate model ultimately depends on the business cost associated with false positives and false negatives.

---

## Explainable AI with SHAP

**SHAP (SHapley Additive exPlanations)** is used to interpret model behavior and understand the factors influencing predictions.

The project includes:

* Global feature importance
* SHAP summary analysis
* Individual prediction explanations using waterfall plots

SHAP helps answer questions such as:

* Which features influence risk predictions?
* Which variables have the greatest impact?
* Which factors push a prediction toward higher risk?
* Which factors contribute toward lower risk?
* Why did a particular applicant receive a specific prediction?

---

## Dashboard

The Streamlit application contains four main sections:

```text
Home
 │
 ├── Executive Dashboard
 ├── Risk Analytics
 ├── Model Performance
 └── Live Prediction
```

### Executive Dashboard

Provides portfolio-level insights including:

* Total loans
* Defaulted loans
* Default rate
* Average loan amount
* Grade-wise default analysis
* Loan distribution

### Risk Analytics

Provides detailed analysis of:

* Income
* Loan amount
* Interest rate
* DTI
* Credit utilization
* Delinquencies
* Credit inquiries
* Other borrower and loan characteristics

### Model Performance

Provides side-by-side comparison of:

* Logistic Regression
* Random Forest
* XGBoost

### Live Prediction

Allows users to enter applicant information and generate an individual model-based loan-risk prediction.

---

## Dashboard Screenshots

### Executive Dashboard

![Executive Dashboard](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/executive_dashboard.png)

### Risk Analytics

![Risk Analytics](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/risk_analytics.png)

### Model Performance

![Model Performance](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/model_performance.png)

### Live Prediction

![Live Prediction](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/live_prediction.png)

### SHAP Feature Importance

![SHAP Feature Importance](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_feature_importance.png)

### SHAP Summary

![SHAP Summary](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_summary.png)

### SHAP Waterfall

![SHAP Waterfall](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform/blob/main/screenshots/shap_waterfall.png)

---

## SQL Business Analytics

SQL is used as an additional analytical layer for business-oriented loan analysis.

Example analyses include:

* Default rates by loan grade
* Default counts
* Average loan amount
* Portfolio-level aggregations
* Risk segmentation
* Borrower-level analysis
* Financial metric analysis

SQL complements the machine-learning workflow by converting loan-level data into business-oriented insights.

---

## Model Persistence

Trained models and preprocessing artifacts are persisted using Joblib.

```text
models/
├── logistic.pkl
├── random_forest.pkl
├── xgboost.pkl
└── scaler.pkl
```

These artifacts allow the deployed application to load trained models and preprocessing components without retraining them each time the application starts.

---

## Business Use Cases

The platform demonstrates potential applications in:

### Credit-Risk Assessment

Identify loan applications that may require additional review.

### Portfolio Monitoring

Analyze default patterns across different loan segments.

### Risk Segmentation

Compare risk across borrower and loan characteristics.

### Decision Support

Provide analytical information to support credit-risk assessment.

### Explainable Risk Analysis

Understand which factors contribute to model predictions.

### Large-Scale Loan Analytics

Analyze large historical loan portfolios using automated data pipelines and machine learning.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
cd Credit-Risk-Intelligence-Platform
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app/Home.py
```

The application will open in your browser.

---

## Live Application

The project is deployed using Streamlit.

**Live Demo:**
[https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)

**GitHub Repository:**
[https://github.com/aditya280505/Credit-Risk-Intelligence-Platform](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)

---

## Limitations

The current implementation has several limitations:

* The dataset is historical rather than real-time.
* Model performance depends on the quality and availability of input features.
* Accuracy can be misleading for imbalanced classification.
* XGBoost currently has a substantially lower F1 score than Logistic Regression and Random Forest.
* Classification thresholds have not been fully optimized for a specific business cost matrix.
* Probability calibration has not yet been implemented.
* Production deployment would require additional validation and monitoring.
* Real-world credit-risk systems require appropriate privacy, security, fairness, governance, and regulatory controls.

---

## Future Improvements

Planned improvements include:

* Classification threshold optimization
* Precision-Recall optimization
* Probability calibration
* Hyperparameter tuning
* Improved minority-class recall
* Additional credit-risk metrics
* Model monitoring
* Data drift detection
* Automated model retraining
* Real-time prediction API
* Cloud database integration
* Advanced risk segmentation
* Authentication and role-based access
* Model governance and audit logging
* Fairness and bias evaluation

---

## Learning Outcomes

This project provided hands-on experience with:

* Python data pipelines
* Pandas and NumPy
* Data cleaning
* Exploratory Data Analysis
* Feature engineering
* SQL business analytics
* Binary classification
* Logistic Regression
* Random Forest
* XGBoost
* SMOTE and imbalanced learning
* Model evaluation
* F1 Score and ROC-AUC
* Explainable AI with SHAP
* Streamlit development
* Model persistence with Joblib
* Git and GitHub
* End-to-end ML project development

---

## Disclaimer

> **This project is developed for educational, analytical, and portfolio demonstration purposes. Predictions generated by the application should not be used as the sole basis for real-world lending, financial, or credit decisions.**

Real-world credit-risk systems require appropriate model validation, governance, fairness assessment, privacy controls, security measures, regulatory compliance, and human oversight.

---

## Author

**Aditya Pravin Borgaonkar**

B.Tech Computer Science Engineering
Artificial Intelligence and Analytics
MIT Art, Design & Technology University

### Areas of Interest

* Artificial Intelligence
* Data Analytics
* Machine Learning
* Credit Risk Analytics
* Business Intelligence
* Explainable AI

**GitHub:**
[https://github.com/aditya280505](https://github.com/aditya280505)

**LinkedIn:**
[https://linkedin.com/in/adityaborgaonkar280505/](https://linkedin.com/in/adityaborgaonkar280505/)

**Email:**
[borgaonkaraditya1@gmail.com](mailto:borgaonkaraditya1@gmail.com)

---

## Project Goal

The goal of this project is to demonstrate an end-to-end **Credit Risk Intelligence Platform** integrating:

```text
Data Analytics
      +
SQL
      +
Feature Engineering
      +
Machine Learning
      +
Imbalanced Learning
      +
Model Evaluation
      +
Explainable AI
      +
Interactive Dashboard
      +
Loan-Risk Prediction
```

The project demonstrates the complete journey from raw loan data to analytical insights, explainable machine-learning predictions, and an interactive credit-risk dashboard.

---

### If you find this project useful, consider giving the repository a Star.

**Built with Python, SQL, Machine Learning, SMOTE, SHAP, and Streamlit.**

```
```
