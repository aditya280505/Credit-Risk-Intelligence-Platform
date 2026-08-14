
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("🤖 Model Performance")
st.caption(
    "Comparison and evaluation of machine learning models "
    "for credit risk prediction"
)


# ==================================================
# PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_DIR = BASE_DIR / "models"


# ==================================================
# LOAD MODELS
# ==================================================

@st.cache_resource
def load_model(path):
    return joblib.load(path)


logistic_model = None
random_forest_model = None
xgb_model = None


# Logistic Regression
logistic_path = MODEL_DIR / "logistic.pkl"

if logistic_path.exists():
    try:
        logistic_model = load_model(logistic_path)
    except Exception:
        logistic_model = None


# Random Forest
random_forest_path = MODEL_DIR / "random_forest.pkl"

if random_forest_path.exists():
    try:
        random_forest_model = load_model(random_forest_path)
    except Exception:
        random_forest_model = None


# XGBoost
xgb_path = MODEL_DIR / "xgboost.pkl"

if xgb_path.exists():
    try:
        xgb_model = load_model(xgb_path)
    except Exception:
        xgb_model = None


# ==================================================
# MODEL STATUS
# ==================================================

st.divider()

st.subheader("📦 Model Status")

col1, col2, col3 = st.columns(3)


with col1:

    if logistic_model is not None:
        st.success("✅ Logistic Regression Loaded")
    else:
        st.error("❌ Logistic Regression Not Found")


with col2:

    if random_forest_model is not None:
        st.success("✅ Random Forest Loaded")
    else:
        st.error("❌ Random Forest Not Found")


with col3:

    if xgb_model is not None:
        st.success("✅ XGBoost Loaded")
    else:
        st.error("❌ XGBoost Not Found")


# ==================================================
# ACTUAL MODEL METRICS
# ==================================================

metrics = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        0.6610,
        0.6606,
        0.8032
    ],

    "F1 Score": [
        0.4290,
        0.4307,
        0.1358
    ],

    "ROC-AUC": [
        0.7084,
        0.7124,
        0.7194
    ]
})


# ==================================================
# KPI CARDS
# ==================================================

st.divider()

st.subheader("📊 Best Performance")


best_accuracy_model = metrics.loc[
    metrics["Accuracy"].idxmax(),
    "Model"
]

best_accuracy = metrics["Accuracy"].max()


best_f1_model = metrics.loc[
    metrics["F1 Score"].idxmax(),
    "Model"
]

best_f1 = metrics["F1 Score"].max()


best_auc_model = metrics.loc[
    metrics["ROC-AUC"].idxmax(),
    "Model"
]

best_auc = metrics["ROC-AUC"].max()


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🏆 Best Accuracy",
        f"{best_accuracy:.2%}",
        best_accuracy_model
    )


with col2:

    st.metric(
        "🎯 Best F1 Score",
        f"{best_f1:.2%}",
        best_f1_model
    )


with col3:

    st.metric(
        "📈 Best ROC-AUC",
        f"{best_auc:.2%}",
        best_auc_model
    )


# ==================================================
# PERFORMANCE TABLE
# ==================================================

st.divider()

st.subheader("📋 Performance Summary")


display_metrics = metrics.copy()

display_metrics["Accuracy"] = (
    display_metrics["Accuracy"] * 100
).round(2).astype(str) + "%"


display_metrics["F1 Score"] = (
    display_metrics["F1 Score"] * 100
).round(2).astype(str) + "%"


display_metrics["ROC-AUC"] = (
    display_metrics["ROC-AUC"] * 100
).round(2).astype(str) + "%"


st.dataframe(
    display_metrics,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# MODEL COMPARISON CHART
# ==================================================

st.divider()

st.subheader("📈 Model Performance Comparison")


chart_data = metrics.melt(
    id_vars="Model",
    var_name="Metric",
    value_name="Score"
)


fig = px.bar(
    chart_data,
    x="Model",
    y="Score",
    color="Metric",
    barmode="group",
    title="Accuracy vs F1 Score vs ROC-AUC",
    range_y=[0, 1]
)


fig.update_layout(
    yaxis_title="Score",
    xaxis_title="Model",
    legend_title="Metric"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ==================================================
# ROC-AUC COMPARISON
# ==================================================

st.subheader("📊 ROC-AUC Comparison")


auc_data = metrics.sort_values(
    "ROC-AUC",
    ascending=False
)


fig_auc = px.bar(
    auc_data,
    x="Model",
    y="ROC-AUC",
    text="ROC-AUC",
    title="ROC-AUC Score by Model",
    range_y=[0, 1]
)


fig_auc.update_traces(
    texttemplate="%{text:.2%}",
    textposition="outside"
)


fig_auc.update_layout(
    yaxis_title="ROC-AUC",
    xaxis_title="Model"
)


st.plotly_chart(
    fig_auc,
    use_container_width=True
)


# ==================================================
# BEST MODEL
# ==================================================

st.divider()

st.subheader("🏆 Model Selection")


st.success(
    f"""
**Best ROC-AUC Model: XGBoost**

ROC-AUC: **{best_auc:.2%}**

XGBoost achieved the highest ROC-AUC among the three
evaluated models.
"""
)


# ==================================================
# IMPORTANT OBSERVATION
# ==================================================

st.warning(
    """
⚠️ **Important Observation**

XGBoost has the highest Accuracy (80.32%) and ROC-AUC (71.94%),
but its F1 Score is only 13.58%.

This indicates that accuracy alone is not sufficient for
evaluating the credit-risk classification problem.
"""
)


# ==================================================
# MODEL DETAILS
# ==================================================

st.divider()

st.subheader("🔍 Model Details")


model_info = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Type": [
        "Linear Classification",
        "Bagging Ensemble",
        "Gradient Boosting"
    ],

    "Role": [
        "Baseline Model",
        "Non-linear Ensemble",
        "Advanced Boosting Model"
    ]
})


st.dataframe(
    model_info,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Metrics calculated on the held-out test dataset "
    "(20% test split, random_state=42)."
)

