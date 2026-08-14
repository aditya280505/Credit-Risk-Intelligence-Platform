import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==================================================
# PAGE HEADER
# ==================================================

st.title("📊 Executive Risk Dashboard")
st.caption("Overview of loan portfolio and default risk")


# ==================================================
# LOAD DATA
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "loan_feature_engineered.csv"
)


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()


# ==================================================
# KPI CALCULATIONS
# ==================================================

total_loans = len(df)

defaulted_loans = int(df["default"].sum())

default_rate = (
    defaulted_loans / total_loans
) * 100

avg_loan_amount = df["loan_amnt"].mean()


# ==================================================
# CUSTOM KPI CARD STYLE
# ==================================================

st.markdown(
    """
    <style>

    .kpi-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #444;
        background-color: #16191f;
        text-align: center;
        min-height: 130px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .kpi-title {
        font-size: 16px;
        color: #b8b8b8;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Loans</div>
            <div class="kpi-value">{total_loans:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Defaulted Loans</div>
            <div class="kpi-value">{defaulted_loans:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Default Rate</div>
            <div class="kpi-value">{default_rate:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Avg Loan Amount</div>
            <div class="kpi-value">${avg_loan_amount:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# DIVIDER
# ==================================================

st.divider()


# ==================================================
# DEFAULT DISTRIBUTION
# ==================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("Loan Default Distribution")

    default_data = (
        df["default"]
        .value_counts()
        .reset_index()
    )

    default_data.columns = [
        "default",
        "count"
    ]

    default_data["status"] = default_data["default"].map({
        0: "Non-Default",
        1: "Default"
    })

    fig = px.pie(
        default_data,
        names="status",
        values="count",
        hole=0.45,
        title="Default vs Non-Default"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==================================================
# GRADE-WISE DEFAULT RATE
# ==================================================

with col2:

    st.subheader("Default Rate by Loan Grade")

    grade_analysis = (
        df.groupby("grade")
        .agg(
            total_loans=("default", "count"),
            defaulted_loans=("default", "sum")
        )
        .reset_index()
    )

    grade_analysis["default_rate"] = (
        grade_analysis["defaulted_loans"]
        / grade_analysis["total_loans"]
    ) * 100

    fig = px.bar(
        grade_analysis,
        x="grade",
        y="default_rate",
        title="Default Rate by Grade",
        labels={
            "grade": "Loan Grade",
            "default_rate": "Default Rate (%)"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==================================================
# LOAN AMOUNT DISTRIBUTION
# ==================================================

st.subheader("Loan Amount Distribution")


fig = px.histogram(
    df,
    x="loan_amnt",
    nbins=40,
    title="Distribution of Loan Amounts",
    labels={
        "loan_amnt": "Loan Amount"
    }
)


st.plotly_chart(
    fig,
    use_container_width=True
)