from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)


def evaluate_model(model, X_test, y_test):
    """Evaluate a binary classification model."""

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    metrics = {
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(y_test, predictions),
        "Recall": recall_score(y_test, predictions),
        "F1 Score": f1_score(y_test, predictions),
        "ROC-AUC": roc_auc_score(y_test, probabilities)
    }

    return metrics


def get_confusion_matrix(model, X_test, y_test):
    """Return confusion matrix."""

    predictions = model.predict(X_test)

    return confusion_matrix(y_test, predictions)


def get_classification_report(model, X_test, y_test):
    """Return classification report."""

    predictions = model.predict(X_test)

    return classification_report(
        y_test,
        predictions
    )