import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def train_logistic_regression(X_train, y_train):
    """Train Logistic Regression model."""

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def train_random_forest(X_train, y_train):
    """Train Random Forest model."""

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        min_samples_leaf=5,
        class_weight="balanced",
        random_state=42,
        n_jobs=2
    )

    model.fit(X_train, y_train)

    return model


def train_xgboost(X_train, y_train):
    """Train XGBoost model."""

    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        eval_metric="logloss",
        tree_method="hist",
        random_state=42,
        n_jobs=2
    )

    model.fit(X_train, y_train)

    return model


def save_model(model, path):
    """Save trained model."""
    joblib.dump(model, path)
    print(f"Model saved: {path}")