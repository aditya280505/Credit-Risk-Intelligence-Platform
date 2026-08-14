import pandas as pd


def create_features(df):
    """Create credit-risk features."""

    df = df.copy()

    df["int_rate_decimal"] = df["int_rate"] / 100

    df["loan_income_ratio"] = (
        df["loan_amnt"] / (df["annual_inc"] + 1)
    )

    df["installment_income_ratio"] = (
        df["installment"] / ((df["annual_inc"] / 12) + 1)
    )

    df["revol_util_decimal"] = df["revol_util"] / 100

    df["credit_usage"] = (
        df["revol_bal"] * df["revol_util_decimal"]
    )

    return df