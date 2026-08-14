from imblearn.over_sampling import SMOTE


def apply_smote(X_train, y_train, random_state=42):
    """
    Balance the training data using SMOTE.

    SMOTE is applied only to training data
    to avoid data leakage.
    """

    smote = SMOTE(
        random_state=random_state
    )

    X_train_smote, y_train_smote = smote.fit_resample(
        X_train,
        y_train
    )

    return X_train_smote, y_train_smote