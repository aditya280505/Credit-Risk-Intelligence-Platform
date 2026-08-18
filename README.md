Haan bhai. **Ab same old format hi rakhenge**, bas usko thoda **modern, clean, user-friendly aur 8.5–9/10 portfolio-level** bana dete hain.
Emoji overload nahi, repeated links nahi, sections unnecessarily huge nahi, aur important evidence/screenshots proper jagah par.

**Ek hi box — upar Copy button se poora `README.md` copy karna.**

````markdown
# 🏦 Credit Risk Intelligence Platform

🐍 Python &nbsp; ◈ &nbsp; 🤖 Machine Learning &nbsp; ◈ &nbsp; ⚖️ SMOTE &nbsp; ◈ &nbsp; 🔍 SHAP &nbsp; ◈ &nbsp; 🚀 Streamlit &nbsp; ◈ &nbsp; 🗄️ SQL

**An end-to-end machine learning and analytics platform for loan default risk analysis, model evaluation, explainable AI, and interactive credit-risk decision support.**

[![Live Demo](https://img.shields.io/badge/🚀-Live%20Demo-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

---

# 🌐 Live Demo

### 🚀 Explore the Interactive Credit Risk Platform

**Live Application:**  
https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/

The deployed application provides:

- Portfolio-level credit-risk overview
- Default-rate analysis
- Borrower risk analytics
- Machine learning model comparison
- SHAP explainability
- Individual loan-risk prediction

---

# 📖 Overview

**Credit Risk Intelligence Platform** is an end-to-end machine learning and analytics project designed to analyze loan default risk and generate actionable credit-risk insights.

The platform transforms historical LendingClub loan data into an interactive risk-analysis system using:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- SQL Business Analytics
- Financial Feature Engineering
- Imbalanced Learning
- Machine Learning Classification
- Model Evaluation
- Explainable AI
- Interactive Streamlit Dashboards
- Applicant-Level Risk Prediction

The project demonstrates the complete workflow from **raw financial data → analytics → machine learning → explainability → interactive risk prediction**.

> **Disclaimer:** This project is developed for educational and portfolio purposes. Model predictions should not be used as the sole basis for real-world lending or financial decisions.

---

# ✨ Key Highlights

- 📊 Portfolio-level Credit Risk Dashboard
- ⚠️ Loan Default Risk Analytics
- 🤖 Logistic Regression, Random Forest & XGBoost
- ⚖️ SMOTE for Class Imbalance
- 🔍 SHAP-based Model Explainability
- 🗄️ SQL Business Analysis
- 🔮 Applicant-Level Risk Prediction
- 🚀 Multi-page Streamlit Application
- 📈 Model Performance Comparison

---

# 🚀 Features

### 📊 Executive Risk Dashboard

Provides a high-level view of the loan portfolio through:

- Total Loans
- Defaulted Loans
- Default Rate
- Average Loan Amount
- Default Distribution
- Grade-wise Default Analysis
- Loan Amount Distribution
- Portfolio Risk Indicators

### ⚠️ Risk Analytics

Explores borrower and loan characteristics associated with credit risk:

- Loan Amount
- Interest Rate
- Annual Income
- Debt-to-Income Ratio
- Credit Inquiries
- Delinquencies
- Revolving Utilization
- Credit Accounts
- Loan Grades
- Borrower Financial Characteristics

### 🤖 Model Performance

Compares three classification models:

- Logistic Regression
- Random Forest
- XGBoost

Evaluation metrics:

- Accuracy
- F1 Score
- ROC-AUC

### 🔍 Explainable AI

SHAP is used to understand model behavior through:

- SHAP Feature Importance
- SHAP Summary Plot
- SHAP Waterfall Plot

### 🔮 Live Risk Prediction

Users can enter applicant-level loan information through the Streamlit application and generate a model-based risk prediction.

The prediction pipeline performs:

```text
Applicant Input
      ↓
Input Processing
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Trained Model
      ↓
Risk Prediction
````

---

# 🛠 Tech Stack

| Category            | Technologies              |
| ------------------- | ------------------------- |
| Programming         | Python, SQL               |
| Data Analysis       | Pandas, NumPy             |
| Machine Learning    | Scikit-learn, XGBoost     |
| Imbalanced Learning | imbalanced-learn, SMOTE   |
| Explainable AI      | SHAP                      |
| Visualization       | Plotly, Matplotlib        |
| Dashboard           | Streamlit                 |
| Model Persistence   | Joblib                    |
| Development         | Jupyter Notebook, VS Code |
| Version Control     | Git, GitHub               |

---

# 📂 Project Structure

```text
Credit-Risk-Intelligence-Platform
│
├── app
│   ├── Home.py
│   └── pages
│       ├── 1_Executive_Dashboard.py
│       ├── 2_Risk_Analytics.py
│       ├── 3_Model_Performance.py
│       └── 4_Live_Prediction.py
│
├── data
│   ├── raw
│   ├── processed
│   └── external
│
├── models
│   ├── logistic.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── scaler.pkl
│
├── notebook
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_sql_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_shap_explainability.ipynb
│
├── screenshots
│   ├── executive_dashboard.png
│   ├── risk_analytics.png
│   ├── model_performance.png
│   ├── live_prediction.png
│   ├── shap_feature_importance.png
│   ├── shap_summary.png
│   └── shap_waterfall.png
│
├── sql
│
├── src
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── imbalance_handling.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│   └── shap
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📚 Dataset

The project uses a **LendingClub historical loan dataset** containing loan, borrower, employment, financial, and credit-related information.

### Dataset Scale

| Metric            |            Value |
| ----------------- | ---------------: |
| Processed Records |    **1,303,638** |
| Modeling Features |           **93** |
| Target            | **Loan Default** |

### Target Variable

```text
default

0 → Non-Default
1 → Default
```

---

# 📋 Important Dataset Features

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
| `addr_state`          | Borrower's state                        |
| `dti`                 | Debt-to-income ratio                    |
| `delinq_2yrs`         | Delinquencies during previous two years |
| `inq_last_6mths`      | Credit inquiries                        |
| `open_acc`            | Number of open credit accounts          |
| `pub_rec`             | Public record count                     |
| `revol_bal`           | Revolving credit balance                |
| `revol_util`          | Revolving credit utilization            |
| `total_acc`           | Total credit accounts                   |
| `application_type`    | Loan application type                   |

---

# 🧹 Data Cleaning & Preprocessing

The raw LendingClub dataset contains a large number of records and variables.

The preprocessing workflow includes:

* Selecting relevant variables
* Removing unnecessary columns
* Handling missing values
* Converting data types
* Encoding categorical variables
* Preparing numerical variables
* Creating the modeling dataset
* Separating target and predictor variables

This produces a structured dataset suitable for analytics and machine learning.

---

# 🔍 Exploratory Data Analysis

EDA was performed to understand loan characteristics and identify patterns associated with default risk.

Key analysis areas include:

* Loan Amount Distribution
* Interest Rate Distribution
* Annual Income
* Debt-to-Income Ratio
* Loan Grade
* Default Distribution
* Employment Length
* Home Ownership
* Loan Purpose
* Revolving Utilization
* Credit Inquiries
* Delinquencies
* Credit Account Characteristics

---

# ⚙️ Feature Engineering

Additional financial-risk features were created to provide meaningful signals to the machine learning models.

### Loan-to-Income Ratio

```text
loan_to_income = loan_amnt / annual_inc
```

Measures the loan size relative to annual income.

### Installment-to-Income Ratio

```text
installment_to_income = installment / annual_inc
```

Measures monthly payment burden relative to income.

### Open-to-Total Accounts Ratio

```text
open_to_total_accounts = open_acc / total_acc
```

Represents the proportion of currently open credit accounts.

### Revolving Balance-to-Income Ratio

```text
revol_bal_to_income = revol_bal / annual_inc
```

Measures revolving credit balance relative to annual income.

### Credit Issue Count

A composite indicator based on negative credit-related signals such as:

* Delinquencies
* Public records
* Recent credit inquiries

---

# 🗄️ SQL Business Analysis

SQL is used to connect the machine learning workflow with practical business analysis.

The analysis investigates questions such as:

* Which loan grades have higher default rates?
* What is the average loan amount by grade?
* Which categories contain more defaults?
* Which states show higher default rates?
* How does income vary across risk segments?

### Example SQL Query

```sql
SELECT
    grade,
    COUNT(*) AS total_loans,
    SUM(default) AS defaulted_loans,
    ROUND(AVG(default) * 100, 2) AS default_rate
FROM loans
GROUP BY grade
ORDER BY default_rate DESC;
```

This provides a grade-level view of portfolio default risk.

---

# ⚖️ Class Imbalance Handling

Loan-default prediction is an **imbalanced classification problem** because non-default loans significantly outnumber default loans.

To improve minority-class representation during training, **SMOTE (Synthetic Minority Over-sampling Technique)** was used.

### Training Process

```text
Original Dataset
       │
       ▼
Train / Test Split
       │
       ├──────────────► Test Dataset
       │                 (Untouched)
       │
       ▼
Training Dataset
       │
       ▼
SMOTE
       │
       ▼
Balanced Training Dataset
       │
       ▼
Model Training
```

SMOTE is applied **only to the training data**.

The test dataset remains untouched for a more reliable evaluation.

---

# 🤖 Machine Learning Models

## 1. Logistic Regression

Used as an interpretable baseline classification model.

**Key characteristics:**

* Simple
* Fast
* Interpretable
* Useful for benchmarking

## 2. Random Forest

An ensemble tree-based model capable of learning non-linear relationships and feature interactions.

**Key characteristics:**

* Handles non-linear patterns
* Captures feature interactions
* Works well with structured data
* Provides feature importance

## 3. XGBoost

A gradient-boosting algorithm designed for high-performance classification on structured datasets.

**Key characteristics:**

* Strong predictive capability
* Captures complex relationships
* Handles non-linear patterns
* Effective for tabular data

---

# 📈 Model Performance

The models were evaluated using a held-out test dataset.

| Model               |   Accuracy |   F1 Score |    ROC-AUC |
| ------------------- | ---------: | ---------: | ---------: |
| Logistic Regression | **66.10%** | **42.90%** | **70.84%** |
| Random Forest       | **66.06%** | **43.07%** | **71.24%** |
| XGBoost             | **80.32%** | **13.58%** | **71.94%** |

### Performance Summary

| Metric   | Best Model    |      Score |
| -------- | ------------- | ---------: |
| Accuracy | XGBoost       | **80.32%** |
| F1 Score | Random Forest | **43.07%** |
| ROC-AUC  | XGBoost       | **71.94%** |

---

# 🔎 Model Performance Interpretation

### XGBoost

XGBoost achieved the:

* **Highest Accuracy:** 80.32%
* **Highest ROC-AUC:** 71.94%

However, its **F1 Score of 13.58%** indicates weak minority-class performance at the evaluated classification threshold.

### Random Forest

Random Forest achieved:

* **Accuracy:** 66.06%
* **F1 Score:** 43.07%
* **ROC-AUC:** 71.24%

It provides a stronger balance between default-class identification and overall discrimination among the evaluated models.

### Logistic Regression

Logistic Regression achieved:

* **Accuracy:** 66.10%
* **F1 Score:** 42.90%
* **ROC-AUC:** 70.84%

It serves as a useful interpretable baseline.

> **Important:** Accuracy alone should not be used to select a credit-risk model when the target classes are imbalanced. Precision, Recall, F1 Score, ROC-AUC, Precision-Recall AUC, and threshold analysis should also be considered.

---

# 🔍 Explainable AI with SHAP

**SHAP (SHapley Additive exPlanations)** is used to interpret machine learning predictions.

It helps answer:

* Which features influence model predictions?
* Which variables contribute to higher risk?
* Which variables contribute to lower risk?
* Which features are globally important?
* Why did the model make a specific prediction?

---

# 📊 SHAP Visualizations

### SHAP Feature Importance

Shows the features with the greatest overall influence on model predictions.

### SHAP Summary Plot

Provides a global view of feature importance, impact direction, and feature contribution.

### SHAP Waterfall Plot

Explains how individual features contribute to a specific prediction.

---

# 📊 Dashboard Screenshots

## Executive Risk Dashboard

![Executive Risk Dashboard](screenshots/executive_dashboard.png)

---

## Risk Analytics Dashboard

![Risk Analytics Dashboard](screenshots/risk_analytics.png)

---

## Model Performance Dashboard

![Model Performance Dashboard](screenshots/model_performance.png)

---

## Live Risk Prediction

![Live Risk Prediction](screenshots/live_prediction.png)

---

## SHAP Feature Importance

![SHAP Feature Importance](screenshots/shap_feature_importance.png)

---

## SHAP Summary Plot

![SHAP Summary Plot](screenshots/shap_summary.png)

---

## SHAP Waterfall Plot

![SHAP Waterfall Plot](screenshots/shap_waterfall.png)

---

# 📈 End-to-End Workflow

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
SQL Business Analysis
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
        ├── Logistic Regression
        ├── Random Forest
        └── XGBoost
        │
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
```

---

# 🖥️ Streamlit Application

The platform is deployed as a multi-page Streamlit application.

```text
Home
 │
 ├── Executive Dashboard
 │
 ├── Risk Analytics
 │
 ├── Model Performance
 │
 └── Live Prediction
```

The application provides an interactive interface for exploring portfolio risk, analyzing borrower characteristics, comparing models, understanding predictions, and generating applicant-level risk predictions.

---

# 🎯 Business Problems Solved

✔ Identify loan characteristics associated with higher default risk

✔ Analyze borrower financial characteristics

✔ Monitor portfolio-level default rates

✔ Compare multiple machine learning models

✔ Identify important risk-driving features

✔ Explain individual model predictions

✔ Support credit-risk analysis

✔ Automate parts of the risk-analysis workflow

---

# 💼 Business Questions Answered

The platform can help investigate:

* Which loan grades have higher default rates?
* How does loan amount relate to default risk?
* Does higher DTI correspond to higher risk?
* Which borrower characteristics influence predictions?
* Which features are most important to the model?
* Which model performs best under different evaluation metrics?
* Why did the model make a specific prediction?
* What patterns exist across different risk segments?

---

# 💾 Model Persistence

Trained models and preprocessing objects are stored using **Joblib**.

```text
models
│
├── logistic.pkl
├── random_forest.pkl
├── xgboost.pkl
└── scaler.pkl
```

This allows the Streamlit application to load trained models without retraining them each time.

---

# 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
cd Credit-Risk-Intelligence-Platform
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**Windows PowerShell**

```bash
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app/Home.py
```

---

# ⚠️ Current Limitations

The current implementation has several limitations:

* Models are trained on a historical static dataset.
* XGBoost achieves high accuracy but has a lower F1 Score under the evaluated threshold.
* Classification thresholds have not been optimized for a specific business risk tolerance.
* Probability calibration has not yet been implemented.
* Real-time data ingestion is not available.
* Automated model monitoring is not implemented.
* Data-drift detection is not implemented.
* The project is intended for educational and portfolio demonstration rather than production lending decisions.

---

# 🔮 Future Improvements

* Minority-Class Recall Optimization
* Precision-Recall Optimization
* Classification Threshold Tuning
* Probability Calibration
* Hyperparameter Optimization
* Cross-Validation
* Precision-Recall AUC Analysis
* Cost-Sensitive Learning
* Model Monitoring
* Data Drift Detection
* Automated Model Retraining
* Real-Time Prediction API
* Cloud Database Integration
* Real-Time Loan Data Integration
* Advanced Risk Segmentation
* Model Governance
* Audit Logging
* Production-Grade Deployment

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python for Data Analytics
* Pandas & NumPy
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* SQL Business Analytics
* Classification Algorithms
* Logistic Regression
* Random Forest
* XGBoost
* SMOTE
* Imbalanced Learning
* Model Evaluation
* Accuracy
* F1 Score
* ROC-AUC
* Explainable AI
* SHAP
* Streamlit
* Joblib
* Git & GitHub
* Machine Learning Deployment
* End-to-End ML Development

---

# 🧠 Skills Demonstrated

```text
Data Analytics
│
├── Python
├── Pandas
├── NumPy
├── Data Cleaning
└── Exploratory Data Analysis
        │
        ▼
Machine Learning
│
├── Logistic Regression
├── Random Forest
├── XGBoost
├── SMOTE
└── Model Evaluation
        │
        ▼
Explainable AI
│
└── SHAP
        │
        ▼
Business Analytics
│
└── SQL
        │
        ▼
Visualization & Deployment
│
├── Plotly
├── Matplotlib
└── Streamlit
        │
        ▼
Version Control
│
└── Git + GitHub
```

---

# 👨‍💻 Author

**Aditya Pravin Borgaonkar**

B.Tech Computer Science Engineering
**Artificial Intelligence & Analytics**
MIT Art, Design & Technology University

📧 Email: [borgaonkaraditya1@gmail.com](mailto:borgaonkaraditya1@gmail.com)

🔗 GitHub: [https://github.com/aditya280505](https://github.com/aditya280505)

🔗 LinkedIn: [https://linkedin.com/in/adityaborgaonkar280505/](https://linkedin.com/in/adityaborgaonkar280505/)

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star** on GitHub.

It helps others discover the project and supports continued development.

---

# 🎯 Project Goal

The goal of this project is to demonstrate an **end-to-end Credit Risk Intelligence Platform** combining:

**Data Analytics + SQL + Machine Learning + SMOTE + Explainable AI + Interactive Dashboards**

The project demonstrates how historical loan data can be transformed into meaningful credit-risk insights, machine learning predictions, and explainable decision-support information through a complete analytics pipeline.

---

**Built with Python, SQL, Machine Learning, SMOTE, SHAP, and Streamlit.**

```
```
