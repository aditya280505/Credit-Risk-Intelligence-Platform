import os
import joblib


def save_object(obj, path):
    """Save any Python object using joblib."""

    directory = os.path.dirname(path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    joblib.dump(obj, path)

    print(f"Saved successfully: {path}")


def load_object(path):
    """Load a saved Python object."""

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"File not found: {path}"
        )

    return joblib.load(path)


def ensure_directory(path):
    """Create directory if it does not exist."""

    os.makedirs(path, exist_ok=True)