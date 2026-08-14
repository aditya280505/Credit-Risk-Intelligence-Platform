import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Credit Risk Intelligence Platform",
    page_icon="🏦",
    layout="wide"
)


# ==================================================
# CUSTOM KPI CARD STYLE
# ==================================================

st.markdown(
    """
    <style>

    .home-kpi-card {
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

    .home-kpi-title {
        font-size: 16px;
        color: #b8b8b8;
        margin-bottom: 12px;
    }

    .home-kpi-value {
        font-size: 30px;
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

st.title("🏦 Credit Risk Intelligence Platform")

st.subheader("AI-Powered Loan Default Risk Analysis")

st.write(
    """
    This platform uses machine learning and analytics to assess
    loan default risk and support data-driven credit decisions.
    """
)

st.divider()


# ==================================================
# PLATFORM KPI CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class="home-kpi-card">
            <div class="home-kpi-title">
                Loan Records
            </div>
            <div class="home-kpi-value">
                1.3M+
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="home-kpi-card">
            <div class="home-kpi-title">
                ML Models
            </div>
            <div class="home-kpi-value">
                3
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="home-kpi-card">
            <div class="home-kpi-title">
                Risk Analysis
            </div>
            <div class="home-kpi-value">
                Enabled
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        """
        <div class="home-kpi-card">
            <div class="home-kpi-title">
                Explainability
            </div>
            <div class="home-kpi-value">
                SHAP
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# PLATFORM FEATURES
# ==================================================

st.divider()

st.subheader("Platform Features")

st.markdown(
    """
    - 📊 **Executive Dashboard** — Overall portfolio risk overview
    - ⚠️ **Risk Analytics** — Default rates and risk segmentation
    - 🤖 **Model Performance** — Compare ML models
    - 🔮 **Live Prediction** — Predict individual loan default risk
    """
)


# ==================================================
# NAVIGATION INFO
# ==================================================

st.info(
    "Use the sidebar to navigate through the platform."
)

#python -m streamlit run app/Home.py   
