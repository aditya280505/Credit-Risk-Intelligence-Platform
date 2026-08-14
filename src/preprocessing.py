import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path):
    """Load processed loan dataset."""
    return pd.read_csv(path)


def prepare_data(df):
    """Separate features and target."""
    X = df.drop(columns=["default"])
    y = df["default"]

    return X, y


def split_data(X, y, test_size=0.20, random_state=42):
    """Split data into training and testing sets."""
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )


def scale_data(X_train, X_test):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler