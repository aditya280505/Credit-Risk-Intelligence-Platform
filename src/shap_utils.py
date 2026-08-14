import shap


def create_explainer(model):
    """Create SHAP TreeExplainer for tree-based model."""
    return shap.TreeExplainer(model)


def calculate_shap_values(explainer, X):
    """Calculate SHAP values."""
    return explainer.shap_values(X)


def get_feature_importance(shap_values, feature_names):
    """Calculate mean absolute SHAP feature importance."""

    importance = abs(shap_values).mean(axis=0)

    result = sorted(
        zip(feature_names, importance),
        key=lambda x: x[1],
        reverse=True
    )

    return result


def explain_prediction(
    explainer,
    X,
    feature_names,
    max_display=15
):
    """Create SHAP waterfall explanation for one prediction."""

    shap_values = explainer.shap_values(X)

    explanation = shap.Explanation(
        values=shap_values[0],
        base_values=explainer.expected_value,
        data=X[0],
        feature_names=feature_names
    )

    shap.plots.waterfall(
        explanation,
        max_display=max_display
    )

    return explanation