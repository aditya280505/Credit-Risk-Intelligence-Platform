import streamlit as st

st.set_page_config(
    page_title="Credit Risk Intelligence Platform",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Credit Risk Intelligence Platform")

st.subheader("AI-Powered Loan Default Risk Analysis")

st.write(
    """
    This platform uses machine learning and analytics to assess
    loan default risk and support data-driven credit decisions.
    """
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Loan Records", "1.3M+")

with col2:
    st.metric("ML Models", "3")

with col3:
    st.metric("Risk Analysis", "Enabled")

with col4:
    st.metric("Explainability", "SHAP")

st.divider()

st.subheader("Platform Features")

st.markdown("""
- 📊 **Executive Dashboard** — Overall portfolio risk overview
- ⚠️ **Risk Analytics** — Default rates and risk segmentation
- 🤖 **Model Performance** — Compare ML models
- 🔮 **Live Prediction** — Predict individual loan default risk
""")

st.info(
    "Use the sidebar to navigate through the platform."
)


#python -m streamlit run app/Home.py   