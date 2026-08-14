import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Risk Analytics",
    page_icon="⚠️",
    layout="wide"
)


# ==================================================
# CUSTOM KPI CARD STYLE
# ==================================================

st.markdown(
    """
    <style>

    .risk-kpi-card {
        padding: 24px 20px;
        border-radius: 14px;
        border: 1px solid #3a3d45;
        background-color: #16191f;
        text-align: center;
        min-height: 145px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-sizing: border-box;
    }

    .risk-kpi-title {
        font-size: 16px;
        color: #b8b8b8;
        margin-bottom: 12px;
    }

    .risk-kpi-value {
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.title("⚠️ Risk Analytics")
st.caption("Detailed analysis of borrower and loan risk factors")


# ==================================================
# LOAD DATA
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "dashboard_data.csv"
)


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()


# ==================================================
# RISK FILTERS
# ==================================================

st.sidebar.header("🔎 Risk Filters")


# ==================================================
# GRADE FILTER
# ==================================================

if "grade" in df.columns:

    grades = sorted(
        df["grade"].dropna().unique()
    )

    selected_grades = st.sidebar.multiselect(
        "Loan Grade",
        grades,
        default=grades
    )

else:

    selected_grades = []


# ==================================================
# APPLY FILTER
# ==================================================

filtered_df = df.copy()

if "grade" in df.columns and selected_grades:

    filtered_df = filtered_df[
        filtered_df["grade"].isin(selected_grades)
    ]


# ==================================================
# KPI CALCULATIONS
# ==================================================

total_filtered = len(filtered_df)

defaulted_filtered = int(
    filtered_df["default"].sum()
)


if total_filtered > 0:

    filtered_default_rate = (
        defaulted_filtered /
        total_filtered
    ) * 100

else:

    filtered_default_rate = 0


if "annual_inc" in filtered_df.columns:

    avg_income = filtered_df["annual_inc"].mean()

else:

    avg_income = 0


# ==================================================
# KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="risk-kpi-card">
            <div class="risk-kpi-title">
                Filtered Loans
            </div>
            <div class="risk-kpi-value">
                {total_filtered:,}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="risk-kpi-card">
            <div class="risk-kpi-title">
                Defaulted Loans
            </div>
            <div class="risk-kpi-value">
                {defaulted_filtered:,}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="risk-kpi-card">
            <div class="risk-kpi-title">
                Default Rate
            </div>
            <div class="risk-kpi-value">
                {filtered_default_rate:.2f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="risk-kpi-card">
            <div class="risk-kpi-title">
                Average Annual Income
            </div>
            <div class="risk-kpi-value">
                ${avg_income:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# DIVIDER
# ==================================================

st.divider()


# ==================================================
# GRADE-WISE DEFAULT RATE
# ==================================================

if "grade" in filtered_df.columns:

    st.subheader("📊 Default Rate by Loan Grade")

    grade_analysis = (
        filtered_df
        .groupby("grade")
        .agg(
            total_loans=("default", "count"),
            defaults=("default", "sum")
        )
        .reset_index()
    )

    grade_analysis["default_rate"] = (
        grade_analysis["defaults"]
        / grade_analysis["total_loans"]
    ) * 100

    fig = px.bar(
        grade_analysis,
        x="grade",
        y="default_rate",
        title="Loan Grade vs Default Risk",
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
# INTEREST RATE VS DEFAULT
# ==================================================

if "int_rate" in filtered_df.columns:

    st.subheader("💰 Interest Rate vs Default Risk")

    fig = px.box(
        filtered_df,
        x="default",
        y="int_rate",
        points=False,
        title="Interest Rate Distribution by Default Status",
        labels={
            "default": "Default Status",
            "int_rate": "Interest Rate (%)"
        }
    )

    fig.update_xaxes(
        tickvals=[0, 1],
        ticktext=[
            "Non-Default",
            "Default"
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==================================================
# LOAN AMOUNT VS DEFAULT
# ==================================================

if "loan_amnt" in filtered_df.columns:

    st.subheader("💵 Loan Amount vs Default Risk")

    fig = px.box(
        filtered_df,
        x="default",
        y="loan_amnt",
        points=False,
        title="Loan Amount Distribution by Default Status",
        labels={
            "default": "Default Status",
            "loan_amnt": "Loan Amount"
        }
    )

    fig.update_xaxes(
        tickvals=[0, 1],
        ticktext=[
            "Non-Default",
            "Default"
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==================================================
# DTI VS DEFAULT
# ==================================================

if "dti" in filtered_df.columns:

    st.subheader("📈 Debt-to-Income Ratio vs Default Risk")

    fig = px.box(
        filtered_df,
        x="default",
        y="dti",
        points=False,
        title="DTI Distribution by Default Status",
        labels={
            "default": "Default Status",
            "dti": "Debt-to-Income Ratio"
        }
    )

    fig.update_xaxes(
        tickvals=[0, 1],
        ticktext=[
            "Non-Default",
            "Default"
        ]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==================================================
# DATA SUMMARY
# ==================================================

st.divider()

st.subheader("📋 Risk Dataset Summary")

summary_columns = [
    col for col in [
        "loan_amnt",
        "int_rate",
        "annual_inc",
        "dti",
        "grade",
        "default"
    ]
    if col in filtered_df.columns
]

st.dataframe(
    filtered_df[summary_columns].head(100),
    use_container_width=True,
    hide_index=True
)
