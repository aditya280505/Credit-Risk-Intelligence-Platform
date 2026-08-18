# 🏦 Credit Risk Intelligence Platform

🐍 **Python**   ◈   🤖 **Machine Learning**   ◈   ⚖️ **SMOTE**   ◈   🔍 **SHAP**   ◈   📊 **Analytics**   ◈   🚀 **Streamlit**   ◈   🗄️ **SQL**

### An End-to-End Machine Learning & Analytics Platform for Credit-Risk Intelligence

The **Credit Risk Intelligence Platform** analyzes historical loan and borrower data, engineers financial-risk features, handles class imbalance, trains multiple classification models, evaluates their performance, explains predictions using SHAP, and delivers interactive credit-risk insights through Streamlit.

[![🚀 Live Demo](https://img.shields.io/badge/🚀%20LIVE%20DEMO-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)
[![💻 GitHub](https://img.shields.io/badge/💻%20GITHUB-Repository-black?style=for-the-badge\&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge\&logo=streamlit)](https://streamlit.io/)

---

# 📌 Project Highlights

|                           | Highlight                                   |
| ------------------------- | ------------------------------------------- |
| 📚 **Dataset**            | ~1.3M processed loan records                |
| 🔢 **Features**           | 93 modeling features                        |
| 🎯 **Task**               | Binary loan-default classification          |
| 🤖 **Models**             | Logistic Regression, Random Forest, XGBoost |
| ⚖️ **Imbalance Handling** | SMOTE                                       |
| 🔍 **Explainability**     | SHAP                                        |
| 📊 **Dashboard**          | 4 interactive Streamlit sections            |
| 🔮 **Prediction**         | Individual loan-risk prediction             |
| 🗄️ **Analytics**         | SQL-based business analysis                 |
| 🚀 **Deployment**         | Streamlit                                   |

---

# 🚀 Live Demo

## Explore the Interactive Credit-Risk Dashboard

**Live Application:**
https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/

The application provides:

* Portfolio-level risk monitoring
* Loan and borrower risk analytics
* Machine-learning model comparison
* SHAP-based explainability
* Individual loan-risk prediction

---

# 💻 Repository

**GitHub:**
https://github.com/aditya280505/Credit-Risk-Intelligence-Platform

---

# 📖 Overview

Financial institutions process large volumes of loan applications and need effective methods to identify borrowers who may have a higher probability of default.

This project demonstrates an **end-to-end Credit Risk Intelligence Platform** that combines:

* Data Analytics
* SQL
* Feature Engineering
* Machine Learning
* Imbalanced Learning
* Model Evaluation
* Explainable AI
* Interactive Visualization
* Streamlit Deployment

The platform transforms historical loan-level data into meaningful risk insights and machine-learning-based predictions.

---

# 🎯 Problem Statement

Traditional credit-risk assessment can require significant manual analysis and may become difficult to scale as the number of applications increases.

The objective of this project is to develop a data-driven system capable of:

* Analyzing borrower and loan characteristics
* Identifying patterns associated with loan defaults
* Engineering meaningful financial-risk indicators
* Handling imbalanced default classes
* Training and comparing multiple ML models
* Explaining model predictions
* Providing portfolio-level risk analytics
* Supporting individual loan-risk prediction

---

# 💡 Proposed Solution

The platform follows a complete machine-learning and analytics pipeline:

```text
                    ┌─────────────────────┐
                    │   LendingClub Data  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Exploratory Data    │
                    │ Analysis            │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Train / Test Split  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SMOTE on Training   │
                    │ Data                │
                    └──────────┬──────────┘
                               │
                  ┌────────────┼────────────┐
                  ▼            ▼            ▼
             Logistic       Random        XGBoost
             Regression      Forest
                  │            │            │
                  └────────────┼────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Model Evaluation    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SHAP Explainability │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Streamlit Dashboard │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Live Risk Prediction│
                    └─────────────────────┘
```

---

# ✨ Key Features

## 📊 Executive Risk Dashboard

Provides a portfolio-level overview of credit risk.

Key KPIs include:

* Total loans
* Defaulted loans
* Default rate
* Average loan amount
* Default distribution
* Grade-wise default rate
* Loan amount distribution

---

## ⚠️ Risk Analytics

Provides deeper analysis of borrower and loan characteristics.

The dashboard can be used to investigate relationships involving:

* Loan amount
* Interest rate
* Annual income
* Debt-to-income ratio
* Credit inquiries
* Delinquencies
* Revolving balance
* Revolving utilization
* Credit accounts
* Loan grades

---

## 🤖 Model Performance

Compares three classification algorithms:

1. Logistic Regression
2. Random Forest
3. XGBoost

Evaluation metrics include:

* Accuracy
* F1 Score
* ROC-AUC

---

## 🔍 Explainable AI

SHAP is used to understand the behavior of the machine-learning model.

The project includes:

* SHAP Feature Importance
* SHAP Summary Plot
* SHAP Waterfall Plot

---

## 🔮 Live Risk Prediction

The Streamlit application allows users to enter loan and borrower information and generate a model-based prediction.

The prediction workflow is:

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

---

# 🛠️ Tech Stack

| Category             | Technologies              |
| -------------------- | ------------------------- |
| Programming          | Python                    |
| Data Analysis        | Pandas, NumPy             |
| Machine Learning     | Scikit-learn, XGBoost     |
| Imbalanced Learning  | imbalanced-learn, SMOTE   |
| Explainable AI       | SHAP                      |
| Visualization        | Plotly, Matplotlib        |
| Dashboard            | Streamlit                 |
| Model Persistence    | Joblib                    |
| Database / Analytics | SQL                       |
| Development          | Jupyter Notebook, VS Code |
| Version Control      | Git, GitHub               |

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

Target encoding:

```text
0 → Non-Default
1 → Default
```

---

# 📋 Important Features

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
| `open_acc`            | Open credit accounts                |
| `pub_rec`             | Public record count                 |
| `revol_bal`           | Revolving balance                   |
| `revol_util`          | Revolving utilization               |
| `total_acc`           | Total credit accounts               |

---

# ⚙️ Data Preprocessing

The raw dataset contains a large number of columns and observations.

The preprocessing pipeline includes:

1. Selecting relevant variables
2. Removing unnecessary columns
3. Handling missing values
4. Converting data types
5. Encoding categorical variables
6. Preparing numerical features
7. Creating the final modeling dataset
8. Separating predictors and target

The processed dataset is then used for model development and analytics.

---

# 🔧 Feature Engineering

Financial-risk features were engineered from existing variables to provide additional information about borrower financial burden and credit behavior.

### Loan-to-Income Ratio

```python
loan_to_income = loan_amnt / annual_inc
```

Measures the loan size relative to annual income.

### Installment-to-Income Ratio

```python
installment_to_income = installment / annual_inc
```

Represents monthly payment burden relative to income.

### Open-to-Total Accounts Ratio

```python
open_to_total_accounts = open_acc / total_acc
```

Represents the proportion of currently open credit accounts.

### Credit Issue Count

Combines selected negative credit indicators such as:

* Delinquencies
* Public records
* Recent credit inquiries

### Revolving Balance-to-Income Ratio

```python
revol_bal_to_income = revol_bal / annual_inc
```

Provides an additional measure of revolving-credit burden relative to income.

---

# ⚖️ Handling Class Imbalance

Loan-default prediction is an **imbalanced binary classification problem**.

The minority class represents defaulted loans, while the majority class represents non-default loans.

To improve minority-class representation during training, the project uses:

## SMOTE

**SMOTE — Synthetic Minority Over-sampling Technique**

SMOTE creates synthetic examples of the minority class rather than simply duplicating existing observations.

```text
Original Dataset
       │
       ▼
Train / Test Split
       │
       ├──────────────► Test Set
       │                Untouched
       ▼
     SMOTE
       │
       ▼
Balanced Training Set
       │
       ▼
Machine Learning
```

**Important:** SMOTE is applied only to the training data so that the test set remains representative of unseen data.

---

# 🤖 Machine Learning Models

## 1. Logistic Regression

Used as a baseline linear classification model.

**Strengths:**

* Simple
* Fast
* Interpretable
* Useful benchmark

---

## 2. Random Forest

An ensemble of decision trees designed to capture nonlinear relationships and feature interactions.

**Strengths:**

* Handles nonlinear patterns
* Captures feature interactions
* Works well with structured data

---

## 3. XGBoost

A gradient-boosting algorithm designed for strong performance on structured/tabular datasets.

**Strengths:**

* Captures complex relationships
* Handles nonlinear patterns
* Effective on tabular data
* Provides strong predictive performance

---

# 📈 Model Performance

Models were evaluated on the held-out test dataset.

| Model               |   Accuracy |   F1 Score |    ROC-AUC |
| ------------------- | ---------: | ---------: | ---------: |
| Logistic Regression | **66.10%** | **42.90%** | **70.84%** |
| Random Forest       | **66.06%** | **43.07%** | **71.24%** |
| XGBoost             | **80.32%** | **13.58%** | **71.94%** |

---

# 🧠 Model Selection Analysis

The model results demonstrate an important lesson in credit-risk classification.

### XGBoost

XGBoost achieved:

* **Highest Accuracy:** 80.32%
* **Highest ROC-AUC:** 71.94%

However:

* **F1 Score:** 13.58%

The high accuracy combined with low F1 score indicates that accuracy alone does not adequately represent minority-class performance in this imbalanced problem.

### Random Forest

Random Forest achieved:

* Accuracy: 66.06%
* **F1 Score: 43.07%**
* ROC-AUC: 71.24%

### Logistic Regression

Logistic Regression achieved:

* Accuracy: 66.10%
* F1 Score: 42.90%
* ROC-AUC: 70.84%

### Key Takeaway

For a credit-risk application, model selection should not rely only on accuracy.

Metrics such as:

* Precision
* Recall
* F1 Score
* ROC-AUC
* Precision-Recall AUC
* Classification threshold

should be considered together with the business cost of false positives and false negatives.

This project therefore treats the model comparison as an analytical exercise rather than claiming that the highest-accuracy model is automatically the best production model.

---

# 🔍 Explainable AI with SHAP

**SHAP (SHapley Additive exPlanations)** is used to interpret machine-learning predictions.

SHAP helps answer questions such as:

* Which features influence model predictions?
* Which features contribute toward higher predicted risk?
* Which features contribute toward lower predicted risk?
* Which variables are globally important?
* Why did a specific observation receive a particular prediction?

---

# 📊 SHAP Visualizations

## SHAP Feature Importance

Displays the relative importance of features used by the model.

![SHAP Feature Importance](screenshots/shap_feature_importance.png)

---

## SHAP Summary Plot

Provides a global view of feature importance and feature impact across observations.

![SHAP Summary](screenshots/shap_summary.png)

---

## SHAP Waterfall Plot

Explains how individual features contribute to a specific prediction.

![SHAP Waterfall](screenshots/shap_waterfall.png)

---

# 🖥️ Streamlit Application

The platform contains four main application sections:

```text
🏠 Home
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

The Executive Dashboard provides portfolio-level KPIs and risk insights.

![Executive Dashboard](screenshots/executive_dashboard.png)

---

# ⚠️ Risk Analytics

The Risk Analytics page provides detailed analysis of loan and borrower characteristics.

![Risk Analytics](screenshots/risk_analytics.png)

---

# 🤖 Model Performance

The Model Performance dashboard presents comparative model evaluation metrics.

![Model Performance](screenshots/model_performance.png)

---

# 🔮 Live Risk Prediction

The Live Prediction dashboard provides applicant-level risk prediction using the trained machine-learning pipeline.

![Live Prediction](screenshots/live_prediction.png)

---

# 🗄️ SQL Business Analytics

SQL is used as part of the analytics workflow to perform business-oriented analysis.

Example use cases include:

* Default analysis by loan grade
* Average loan amount
* Default counts
* Portfolio aggregation
* Risk segmentation
* Borrower-level analysis
* Financial metric analysis

SQL provides an additional analytical layer between raw data and business insights.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │   LendingClub Data   │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │ Data Cleaning & Preprocessing │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │ Exploratory Data Analysis     │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │ Feature Engineering           │
                    └───────────────┬───────────────┘
                                    │
              ┌─────────────────────▼─────────────────────┐
              │             Train / Test Split            │
              └─────────────────────┬─────────────────────┘
                                    │
                              ┌─────▼─────┐
                              │   SMOTE   │
                              └─────┬─────┘
                                    │
              ┌─────────────────────▼─────────────────────┐
              │              ML Model Layer               │
              │                                            │
              │ Logistic Regression | Random Forest       │
              │ XGBoost                                      │
              └─────────────────────┬─────────────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │ Model Evaluation              │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │ SHAP Explainability            │
                    └───────────────┬───────────────┘
                                    │
              ┌─────────────────────▼─────────────────────┐
              │          Streamlit Application            │
              │                                             │
              │ Executive | Risk | Models | Prediction    │
              └─────────────────────┬─────────────────────┘
                                    │
                                    ▼
                          Credit-Risk Insights
```

---

# 🔄 End-to-End Workflow

```text
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
SHAP Explainability
      ↓
Streamlit Dashboard
      ↓
Live Risk Prediction
```

---

# 💼 Business Use Cases

The platform demonstrates potential applications in:

### Credit-Risk Assessment

Identify loan applications that may require additional review.

### Portfolio Monitoring

Monitor default rates and risk patterns across loan segments.

### Risk Segmentation

Analyze risk according to borrower and loan characteristics.

### Decision Support

Provide analytical information that can assist credit-risk teams.

### Explainable Decision Support

Use SHAP to understand factors influencing model predictions.

### Large-Scale Analysis

Automate analysis across large historical loan datasets.

---

# 📊 Questions the Platform Can Help Answer

* Which loan grades have higher default rates?
* How does loan amount relate to default risk?
* How does debt-to-income ratio relate to risk?
* Which financial variables are most influential?
* Which model performs better under different metrics?
* What factors contribute to a particular prediction?
* How does borrower credit behavior relate to default risk?

---

# 💾 Model Persistence

Trained models and preprocessing objects are persisted using **Joblib**.

```text
models/
│
├── logistic.pkl
├── random_forest.pkl
├── xgboost.pkl
└── scaler.pkl
```

This allows the deployed Streamlit application to load trained artifacts without retraining the models each time.

---

# 🚀 Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/Credit-Risk-Intelligence-Platform.git
```

## 2. Navigate to the Project

```bash
cd Credit-Risk-Intelligence-Platform
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Application

```bash
streamlit run app/Home.py
```

The application will open in your browser.

---

# 📸 Dashboard Gallery

### Executive Dashboard

![Executive Dashboard](screenshots/executive_dashboard.png)

### Risk Analytics

![Risk Analytics](screenshots/risk_analytics.png)

### Model Performance

![Model Performance](screenshots/model_performance.png)

### Live Prediction

![Live Prediction](screenshots/live_prediction.png)

### SHAP Feature Importance

![SHAP Feature Importance](screenshots/shap_feature_importance.png)

### SHAP Summary

![SHAP Summary](screenshots/shap_summary.png)

### SHAP Waterfall

![SHAP Waterfall](screenshots/shap_waterfall.png)

---

# ⚠️ Limitations

This project is an educational and portfolio demonstration.

Current limitations include:

* The dataset is historical rather than real-time.
* Model performance depends on the available features and data quality.
* Accuracy can be misleading for imbalanced classification.
* The current evaluation does not represent production credit underwriting validation.
* Classification thresholds have not been fully optimized for a specific business cost matrix.
* Production deployment would require extensive model validation and monitoring.
* Real-world lending systems require regulatory, fairness, privacy, security, and governance controls.

---

# 🔐 Disclaimer

> **This project is developed for educational, analytical, and portfolio demonstration purposes. Predictions generated by this application should not be used as the sole basis for real-world lending, financial, or credit decisions.**

---

# 🔮 Future Improvements

Planned improvements include:

* Hyperparameter optimization
* Minority-class recall optimization
* F1-score optimization
* Probability calibration
* Classification threshold optimization
* Precision-Recall AUC analysis
* Cost-sensitive learning
* Model monitoring
* Data drift detection
* Automated model retraining
* Real-time prediction API
* Cloud database integration
* Real-time loan-data integration
* Advanced risk segmentation
* Model governance and audit logging
* Fairness and bias evaluation
* Production-grade authentication and authorization

---

# 🎓 Learning Outcomes

This project demonstrates hands-on experience with:

* Python
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* SQL
* Logistic Regression
* Random Forest
* XGBoost
* SMOTE
* Imbalanced Classification
* Model Evaluation
* F1 Score
* ROC-AUC
* Explainable AI
* SHAP
* Streamlit
* Joblib
* Git
* GitHub
* Machine Learning Deployment

---

# 🧠 Skills Demonstrated

```text
                    CREDIT RISK INTELLIGENCE
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
     DATA ANALYTICS      MACHINE LEARNING     EXPLAINABLE AI
          │                   │                   │
      Pandas/NumPy       Logistic Regression      SHAP
      EDA                Random Forest
      Feature Eng.       XGBoost
          │                   │
          ▼                   ▼
        SQL               SMOTE
          │                   │
          └──────────┬────────┘
                     ▼
             STREAMLIT DASHBOARD
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Analytics   Evaluation  Prediction
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

The goal of this project is to demonstrate how **data analytics, SQL, machine learning, imbalanced learning, explainable AI, and interactive dashboards** can be integrated into a single credit-risk intelligence platform.

The project focuses on the complete journey from:

```text
Raw Data
   ↓
Analytics
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Explainability
   ↓
Interactive Dashboard
   ↓
Risk Prediction
```

---

# 🚀 Explore the Project

[![🚀 Open Live Dashboard](https://img.shields.io/badge/🚀%20OPEN%20LIVE%20DASHBOARD-success?style=for-the-badge)](https://aditya280505-credit-risk-intelligence-platform-apphome-gqpygr.streamlit.app/)

[![💻 View GitHub Repository](https://img.shields.io/badge/💻%20VIEW%20GITHUB%20REPOSITORY-black?style=for-the-badge\&logo=github)](https://github.com/aditya280505/Credit-Risk-Intelligence-Platform)

---

### ⭐ If you found this project useful, consider giving the repository a Star!

**Built with Python • SQL • Machine Learning • SMOTE • SHAP • Streamlit**
