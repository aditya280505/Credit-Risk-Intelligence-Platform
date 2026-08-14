import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Live Prediction",
    page_icon="🔮",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("🔮 Live Credit Risk Prediction")

st.caption(
    "Enter applicant and loan information to estimate "
    "default risk using the trained XGBoost model."
)


# ==================================================
# PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_DIR = BASE_DIR / "models"


# ==================================================
# LOAD MODEL + SCALER
# ==================================================

@st.cache_resource
def load_model(path):
    return joblib.load(path)


try:

    xgb_model = load_model(
        MODEL_DIR / "xgboost.pkl"
    )

    scaler = load_model(
        MODEL_DIR / "scaler.pkl"
    )

except Exception as e:

    st.error("❌ Could not load model or scaler.")

    st.code(str(e))

    st.stop()


# ==================================================
# GET TRAINING FEATURE NAMES
# ==================================================

if hasattr(scaler, "feature_names_in_"):

    FEATURE_COLUMNS = list(
        scaler.feature_names_in_
    )

elif hasattr(xgb_model, "feature_names_in_"):

    FEATURE_COLUMNS = list(
        xgb_model.feature_names_in_
    )

elif hasattr(xgb_model, "get_booster"):

    booster_features = (
        xgb_model
        .get_booster()
        .feature_names
    )

    if booster_features:

        FEATURE_COLUMNS = list(
            booster_features
        )

    else:

        st.error(
            "❌ Training feature names are not available "
            "inside the saved model."
        )

        st.stop()

else:

    st.error(
        "❌ Could not determine training feature names."
    )

    st.stop()


# ==================================================
# INPUT SECTION
# ==================================================

st.divider()

st.subheader("👤 Applicant Information")


col1, col2, col3 = st.columns(3)


with col1:

    loan_amnt = st.number_input(
        "Loan Amount ($)",
        min_value=500.0,
        max_value=50000.0,
        value=15000.0,
        step=500.0
    )


with col2:

    annual_inc = st.number_input(
        "Annual Income ($)",
        min_value=1000.0,
        max_value=1000000.0,
        value=60000.0,
        step=1000.0
    )


with col3:

    int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=1.0,
        max_value=30.0,
        value=12.0,
        step=0.1
    )


# ==================================================
# FINANCIAL INFORMATION
# ==================================================

col1, col2, col3 = st.columns(3)


with col1:

    dti = st.number_input(
        "Debt-to-Income Ratio",
        min_value=0.0,
        max_value=100.0,
        value=15.0,
        step=0.5
    )


with col2:

    installment = st.number_input(
        "Monthly Installment ($)",
        min_value=10.0,
        max_value=5000.0,
        value=450.0,
        step=10.0
    )


with col3:

    emp_length = st.number_input(
        "Employment Length (Years)",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        step=1.0
    )


# ==================================================
# LOAN INFORMATION
# ==================================================

st.divider()

st.subheader("🏦 Loan Information")


col1, col2, col3 = st.columns(3)


with col1:

    grade = st.selectbox(
        "Loan Grade",
        [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
        ]
    )


with col2:

    term = st.selectbox(
        "Loan Term",
        [
            "36 months",
            "60 months"
        ]
    )


with col3:

    sub_grade = st.selectbox(
        "Sub Grade",
        [
            "A1", "A2", "A3", "A4", "A5",
            "B1", "B2", "B3", "B4", "B5",
            "C1", "C2", "C3", "C4", "C5",
            "D1", "D2", "D3", "D4", "D5",
            "E1", "E2", "E3", "E4", "E5",
            "F1", "F2", "F3", "F4", "F5",
            "G1", "G2", "G3", "G4", "G5"
        ]
    )


# ==================================================
# BORROWER INFORMATION
# ==================================================

col1, col2, col3 = st.columns(3)


with col1:

    home_ownership = st.selectbox(
        "Home Ownership",
        [
            "MORTGAGE",
            "NONE",
            "OTHER",
            "OWN",
            "RENT"
        ]
    )


with col2:

    verification_status = st.selectbox(
        "Verification Status",
        [
            "Not Verified",
            "Source Verified",
            "Verified"
        ]
    )


with col3:

    application_type = st.selectbox(
        "Application Type",
        [
            "Individual",
            "Joint App"
        ]
    )


# ==================================================
# LOAN PURPOSE
# ==================================================

purpose = st.selectbox(
    "Loan Purpose",
    [
        "credit_card",
        "debt_consolidation",
        "educational",
        "home_improvement",
        "house",
        "major_purchase",
        "medical",
        "moving",
        "other",
        "renewable_energy",
        "small_business",
        "vacation",
        "wedding"
    ]
)


# ==================================================
# CREDIT PROFILE
# ==================================================

st.divider()

st.subheader("💳 Credit Profile")


col1, col2, col3 = st.columns(3)


with col1:

    delinq_2yrs = st.number_input(
        "Delinquencies (2 Years)",
        min_value=0,
        max_value=20,
        value=0
    )


with col2:

    inq_last_6mths = st.number_input(
        "Credit Inquiries (6 Months)",
        min_value=0,
        max_value=20,
        value=1
    )


with col3:

    open_acc = st.number_input(
        "Open Accounts",
        min_value=0,
        max_value=100,
        value=8
    )


col1, col2, col3 = st.columns(3)


with col1:

    pub_rec = st.number_input(
        "Public Records",
        min_value=0,
        max_value=20,
        value=0
    )


with col2:

    revol_bal = st.number_input(
        "Revolving Balance ($)",
        min_value=0.0,
        max_value=500000.0,
        value=10000.0,
        step=500.0
    )


with col3:

    revol_util = st.number_input(
        "Revolving Utilization (%)",
        min_value=0.0,
        max_value=150.0,
        value=40.0,
        step=1.0
    )


total_acc = st.number_input(
    "Total Credit Accounts",
    min_value=0,
    max_value=150,
    value=20
)


# ==================================================
# PREDICTION BUTTON
# ==================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Credit Risk",
    type="primary",
    use_container_width=True
)


# ==================================================
# CREATE FEATURE VECTOR
# ==================================================

if predict_button:

    input_data = {}


    # ------------------------------------------------
    # Numerical Features
    # ------------------------------------------------

    input_data["loan_amnt"] = loan_amnt

    input_data["int_rate"] = int_rate

    input_data["installment"] = installment

    input_data["emp_length"] = emp_length

    input_data["annual_inc"] = annual_inc

    input_data["dti"] = dti

    input_data["delinq_2yrs"] = delinq_2yrs

    input_data["inq_last_6mths"] = inq_last_6mths

    input_data["open_acc"] = open_acc

    input_data["pub_rec"] = pub_rec

    input_data["revol_bal"] = revol_bal

    input_data["revol_util"] = revol_util

    input_data["total_acc"] = total_acc


    # ------------------------------------------------
    # Term
    # ------------------------------------------------

    input_data["term"] = (
        36
        if term == "36 months"
        else 60
    )


    # ------------------------------------------------
    # Grade
    # ------------------------------------------------

    grade_map = {

        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7

    }

    input_data["grade"] = grade_map[grade]


    # ------------------------------------------------
    # Sub Grade
    # ------------------------------------------------

    sub_grade_map = {

        "A1": 1, "A2": 2, "A3": 3,
        "A4": 4, "A5": 5,

        "B1": 6, "B2": 7, "B3": 8,
        "B4": 9, "B5": 10,

        "C1": 11, "C2": 12, "C3": 13,
        "C4": 14, "C5": 15,

        "D1": 16, "D2": 17, "D3": 18,
        "D4": 19, "D5": 20,

        "E1": 21, "E2": 22, "E3": 23,
        "E4": 24, "E5": 25,

        "F1": 26, "F2": 27, "F3": 28,
        "F4": 29, "F5": 30,

        "G1": 31, "G2": 32, "G3": 33,
        "G4": 34, "G5": 35

    }

    input_data["sub_grade"] = (
        sub_grade_map[sub_grade]
    )


    # ------------------------------------------------
    # Initialize all training features
    # ------------------------------------------------

    for column in FEATURE_COLUMNS:

        if column not in input_data:

            input_data[column] = 0


    # ------------------------------------------------
    # Home Ownership
    # ------------------------------------------------

    home_column = (
        "home_ownership_"
        + home_ownership
    )

    if home_column in input_data:

        input_data[home_column] = 1


    # ------------------------------------------------
    # Verification Status
    # ------------------------------------------------

    if verification_status == "Source Verified":

        column = (
            "verification_status_Source Verified"
        )

        if column in input_data:

            input_data[column] = 1


    elif verification_status == "Verified":

        column = (
            "verification_status_Verified"
        )

        if column in input_data:

            input_data[column] = 1


    # ------------------------------------------------
    # Purpose
    # ------------------------------------------------

    purpose_column = (
        "purpose_"
        + purpose
    )

    if purpose_column in input_data:

        input_data[purpose_column] = 1


    # ------------------------------------------------
    # Application Type
    # ------------------------------------------------

    if application_type == "Joint App":

        column = (
            "application_type_Joint App"
        )

        if column in input_data:

            input_data[column] = 1


    # ------------------------------------------------
    # Feature Engineering
    # ------------------------------------------------

    input_data["loan_to_income"] = (
        loan_amnt /
        max(annual_inc, 1)
    )


    input_data["installment_to_income"] = (
        installment /
        max(annual_inc / 12, 1)
    )


    input_data["open_to_total_accounts"] = (
        open_acc /
        max(total_acc, 1)
    )


    input_data["credit_issue_count"] = (
        delinq_2yrs
        + inq_last_6mths
        + pub_rec
    )


    input_data["revol_bal_to_income"] = (
        revol_bal /
        max(annual_inc, 1)
    )


    # ------------------------------------------------
    # Create DataFrame
    # ------------------------------------------------

    input_df = pd.DataFrame(
        [input_data]
    )


    # ------------------------------------------------
    # Ensure exact feature order
    # ------------------------------------------------

    input_df = input_df.reindex(
        columns=FEATURE_COLUMNS,
        fill_value=0
    )


    # ------------------------------------------------
    # Scale
    # ------------------------------------------------

    try:

        input_scaled = scaler.transform(
            input_df
        )

    except Exception as e:

        st.error(
            "❌ Feature scaling failed."
        )

        st.code(str(e))

        st.stop()


    # ------------------------------------------------
    # Prediction
    # ------------------------------------------------

    try:

        probability = (
            xgb_model
            .predict_proba(input_scaled)[0][1]
        )

    except Exception as e:

        st.error(
            "❌ Model prediction failed."
        )

        st.code(str(e))

        st.stop()


    probability_percent = (
        probability * 100
    )


    # ==================================================
    # RISK CLASSIFICATION
    # ==================================================

    if probability < 0.30:

        risk_level = "LOW RISK"

        recommendation = (
            "Applicant shows relatively low "
            "probability of default."
        )


    elif probability < 0.60:

        risk_level = "MEDIUM RISK"

        recommendation = (
            "Applicant requires additional "
            "credit review."
        )


    else:

        risk_level = "HIGH RISK"

        recommendation = (
            "Applicant shows high probability "
            "of default and requires careful review."
        )


    # ==================================================
    # RESULT
    # ==================================================

    st.divider()

    st.subheader(
        "🎯 Prediction Result"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Default Probability",
            f"{probability_percent:.2f}%"
        )


    with col2:

        st.metric(
            "Risk Level",
            risk_level
        )


    if risk_level == "LOW RISK":

        st.success(
            f"🟢 **{risk_level}**\n\n"
            + recommendation
        )


    elif risk_level == "MEDIUM RISK":

        st.warning(
            f"🟡 **{risk_level}**\n\n"
            + recommendation
        )


    else:

        st.error(
            f"🔴 **{risk_level}**\n\n"
            + recommendation
        )


    # ==================================================
    # PROBABILITY BAR
    # ==================================================

    st.subheader(
        "📊 Default Probability"
    )


    st.progress(
        float(probability)
    )


    st.caption(
        "Probability estimated by the trained XGBoost model."
    )
