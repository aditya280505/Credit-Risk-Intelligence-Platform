
# 🏦 Credit Risk Intelligence Platform

🐍 Python &nbsp; ◈ &nbsp; 🤖 Machine Learning &nbsp; ◈ &nbsp; ⚖️ SMOTE &nbsp; ◈ &nbsp; 🔍 SHAP &nbsp; ◈ &nbsp; 🚀 Streamlit &nbsp; ◈ &nbsp; 🗄️ SQL

**An end-to-end machine learning and analytics platform for loan default risk analysis and data-driven credit-risk assessment.**

[![Live Demo](https://img.shields.io/badge/🚀-Live%20Demo-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)

---

# 🌐 Live Demo

### 🚀 Explore the Interactive Credit Risk Dashboard

**https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/**

The application provides:

- Executive Risk Dashboard
- Risk Analytics
- Model Performance Comparison
- SHAP Explainability
- Live Loan-Risk Prediction

---

# 📖 Overview

This project is an **end-to-end Credit Risk Intelligence Platform** built using **Python, SQL, Machine Learning, SHAP, SMOTE, and Streamlit**.

The platform analyzes historical LendingClub loan data to identify patterns associated with loan defaults, evaluate multiple machine learning models, explain model predictions, and provide interactive risk analytics through a Streamlit dashboard.

The project combines:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Business Analytics
- Feature Engineering
- Imbalanced Learning
- Machine Learning
- Model Evaluation
- Explainable AI
- Interactive Streamlit Dashboard
- Live Risk Prediction

into one complete credit-risk analytics solution.

> **Disclaimer:** This project is developed for educational and portfolio purposes. Model predictions should not be used as the sole basis for real-world lending or financial decisions.

---

# ✨ Key Highlights

- 📊 Portfolio-Level Credit Risk Analytics
- 🤖 Multiple Machine Learning Models
- ⚖️ SMOTE-Based Class Imbalance Handling
- 🔍 SHAP-Based Explainable AI
- 📈 Model Performance Comparison
- 🔮 Individual Loan-Risk Prediction
- 🗄️ SQL Business Analysis
- 🚀 Interactive Streamlit Application

---

# 🚀 Features

- Executive Risk Dashboard
- Loan Default Analysis
- Grade-Wise Risk Analysis
- Borrower Risk Analytics
- Feature Engineering
- SMOTE Class Balancing
- Logistic Regression
- Random Forest
- XGBoost
- Accuracy, F1 Score & ROC-AUC Evaluation
- SHAP Feature Importance
- SHAP Summary Analysis
- SHAP Waterfall Explanation
- Live Risk Prediction
- Interactive Visualizations

---

# 🛠 Tech Stack

## Programming

- Python
- SQL

## Data Analysis

- Pandas
- NumPy

## Machine Learning

- Scikit-Learn
- XGBoost
- imbalanced-learn
- SMOTE

## Explainable AI

- SHAP

## Visualization

- Plotly
- Matplotlib

## Dashboard

- Streamlit

## Model Persistence

- Joblib

## Development

- Jupyter Notebook
- VS Code

## Version Control

- Git
- GitHub

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
├── notebooks
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
````

---

# 📚 Dataset

The project uses a **LendingClub historical loan dataset** containing loan, borrower, employment, income, and credit-related information.

The processed modeling dataset contains approximately:

* **1,303,638 loan records**
* **93 modeling features**

### Target Variable

```text
default
```

```text
0 → Non-Default
1 → Default
```

---

# 📋 Important Dataset Features

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
| `inq_last_6mths`      | Credit inquiries                    |
| `open_acc`            | Number of open accounts             |
| `pub_rec`             | Public record count                 |
| `revol_bal`           | Revolving credit balance            |
| `revol_util`          | Revolving credit utilization        |
| `total_acc`           | Total credit accounts               |

---

# 📊 Dashboard Screenshots

## Executive Risk Dashboard

<img src="screenshots/executive_dashboard.png" width="100%" alt="Executive Risk Dashboard">

---

## Risk Analytics Dashboard

<img src="screenshots/risk_analytics.png" width="100%" alt="Risk Analytics Dashboard">

---

## Model Performance Dashboard

<img src="screenshots/model_performance.png" width="100%" alt="Model Performance Dashboard">

---

## Live Risk Prediction

<img src="screenshots/live_prediction.png" width="100%" alt="Live Risk Prediction">

---

# 📈 Workflow

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

# 🤖 Machine Learning Models

The project compares three classification algorithms.

## Logistic Regression

Used as an interpretable baseline classification model.

## Random Forest

Used to capture non-linear relationships and feature interactions in the loan dataset.

## XGBoost

Used as a gradient-boosting model for structured and tabular data.

---

# ⚖️ Class Imbalance Handling

Loan default prediction is an **imbalanced classification problem**, where non-default observations significantly outnumber default observations.

To improve minority-class representation during training, **SMOTE (Synthetic Minority Over-sampling Technique)** is applied to the training dataset.

```text
Original Training Data
        │
        ▼
Train / Test Split
        │
        ├──────────────► Test Data
        │                Untouched
        │
        ▼
Training Data
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

The test dataset remains untouched to provide a more reliable evaluation of model performance.

---

# 📈 Model Performance

The trained models were evaluated using the held-out test dataset.

| Model               |   Accuracy |   F1 Score |    ROC-AUC |
| ------------------- | ---------: | ---------: | ---------: |
| Logistic Regression | **66.10%** | **42.90%** | **70.84%** |
| Random Forest       | **66.06%** | **43.07%** | **71.24%** |
| XGBoost             | **80.32%** | **13.58%** | **71.94%** |

### Key Observation

XGBoost achieved the highest **Accuracy (80.32%)** and **ROC-AUC (71.94%)**.

However, its **F1 Score (13.58%)** is substantially lower than Logistic Regression and Random Forest under the evaluated classification threshold.

Therefore, **accuracy alone should not be used to select a credit-risk model**, especially when the target classes are imbalanced.

---

# 🔍 Explainable AI

The project uses **SHAP (SHapley Additive exPlanations)** to understand machine learning predictions.

SHAP helps identify:

* Which features influence model predictions
* Which variables contribute to higher predicted risk
* Which variables contribute to lower predicted risk
* Which features are globally most important
* Why a specific prediction was generated

This improves model transparency and makes the machine learning workflow easier to interpret.

---

# 📊 SHAP Visualizations

## SHAP Feature Importance

<img src="screenshots/shap_feature_importance.png" width="100%" alt="SHAP Feature Importance">

---

## SHAP Summary Plot

<img src="screenshots/shap_summary.png" width="100%" alt="SHAP Summary Plot">

---

## SHAP Waterfall Plot

<img src="screenshots/shap_waterfall.png" width="100%" alt="SHAP Waterfall Plot">

---

# 🗄️ SQL Business Analysis

SQL is used to perform business-oriented credit-risk analysis.

The analysis can answer questions such as:

* Which loan grades have the highest default rates?
* What is the average loan amount by grade?
* Which segments contain the most defaults?
* How does default rate vary across loan categories?
* Which borrower segments show higher risk?

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

This type of analysis connects machine learning outputs with practical business questions.

---

# 🔮 Live Risk Prediction

The Streamlit application allows users to enter applicant-level loan information and generate a model-based risk prediction.

### Prediction Workflow

```text
Applicant Information
        │
        ▼
Input Processing
        │
        ▼
Feature Engineering
        │
        ▼
Feature Scaling
        │
        ▼
Trained ML Model
        │
        ▼
Risk Prediction
```

The prediction pipeline processes the applicant information, applies the required transformations, loads the trained model, and generates the risk prediction.

---

# 💼 Business Problems Solved

✔ Identify loan segments with higher default risk

✔ Analyze borrower financial characteristics

✔ Monitor portfolio-level credit risk

✔ Compare machine learning models

✔ Explain model predictions

✔ Support data-driven credit-risk assessment

✔ Provide interactive risk analytics

---

# 🎯 Business Questions

The platform can help investigate questions such as:

* Which loan grades have higher default rates?
* How does loan amount relate to default risk?
* Does higher DTI correspond to higher risk?
* Which borrower characteristics influence predictions?
* Which features are most important to the model?
* Which model performs best under different evaluation metrics?
* How can an individual prediction be explained?

---

# 💾 Model Persistence

Trained machine learning models and preprocessing objects are persisted using **Joblib**.

```text
models
│
├── logistic.pkl
├── random_forest.pkl
├── xgboost.pkl
└── scaler.pkl
```

This allows the Streamlit application to load trained models without retraining them every time the application starts.

---

# ⚙️ Data Preprocessing

The preprocessing workflow includes:

* Selecting relevant variables
* Removing unnecessary columns
* Handling missing values
* Converting data types
* Encoding categorical variables
* Preparing numerical variables
* Separating target and predictor variables
* Preparing the final modeling dataset

---

# 🔧 Feature Engineering

The project creates additional financial-risk features to provide the machine learning models with more meaningful borrower information.

### Loan-to-Income Ratio

```text
loan_to_income = loan_amnt / annual_inc
```

Measures the size of the loan relative to annual income.

### Installment-to-Income Ratio

```text
installment_to_income = installment / annual_inc
```

Represents monthly payment burden relative to income.

### Open-to-Total Accounts Ratio

```text
open_to_total_accounts = open_acc / total_acc
```

Provides information about the proportion of currently open credit accounts.

### Revolving Balance-to-Income Ratio

```text
revol_bal_to_income = revol_bal / annual_inc
```

Provides an additional indicator of revolving credit burden relative to income.

---

# ⚠️ Current Limitations

The current implementation has several limitations:

* Models are trained on historical static data.
* Classification thresholds have not been specifically optimized for business risk tolerance.
* Probability calibration has not yet been implemented.
* Real-time data ingestion is not currently available.
* Automated model monitoring is not implemented.
* Automated data drift detection is not implemented.
* The platform is intended for educational and portfolio demonstration purposes.

> **Disclaimer:** The platform should not be used as the sole basis for real-world lending or financial decisions.

---

# 🔮 Future Improvements

* Classification Threshold Optimization
* Precision-Recall Optimization
* Probability Calibration
* Hyperparameter Tuning
* Cross-Validation
* Precision-Recall AUC Analysis
* Cost-Sensitive Learning
* Model Monitoring
* Data Drift Detection
* Automated Model Retraining
* Real-Time Prediction API
* Cloud Database Integration
* Advanced Risk Segmentation
* Model Governance
* Audit Logging
* Production-Grade Deployment

---

# 🚀 Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
cd Credit-Risk-Intelligence-Platform
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate Environment

### Windows

```bash
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

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python for Data Analytics
* Pandas and NumPy
* Data Preprocessing
* Exploratory Data Analysis
* Feature Engineering
* SQL Business Analytics
* Classification Algorithms
* Logistic Regression
* Random Forest
* XGBoost
* Imbalanced Learning
* SMOTE
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
* End-to-End ML Project Development

---

# 👨‍💻 Author

**Aditya Pravin Borgaonkar**

B.Tech Computer Science Engineering
**Artificial Intelligence & Analytics**
MIT Art, Design & Technology University

📧 **Email:** [borgaonkaraditya1@gmail.com](mailto:borgaonkaraditya1@gmail.com)

🔗 **GitHub:** [https://github.com/aditya280505](https://github.com/aditya280505)

🔗 **LinkedIn:** [https://linkedin.com/in/adityaborgaonkar280505/](https://linkedin.com/in/adityaborgaonkar280505/)

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star** on GitHub.

It helps others discover the project and supports continued development.

---

**Built with Python, SQL, Machine Learning, SHAP, SMOTE, and Streamlit.**

```
```
