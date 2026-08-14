import numpy as np


def predict_risk(model, scaler, input_data):
    """
    Predict loan default probability and risk level.
    """

    # Convert input to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Apply saved scaler
    input_scaled = scaler.transform(input_array)

    # Default probability
    default_probability = model.predict_proba(input_scaled)[0][1]

    # Risk classification
    if default_probability < 0.20:
        risk_level = "Low Risk"
    elif default_probability < 0.50:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    return {
        "default_probability": default_probability,
        "risk_level": risk_level
    }