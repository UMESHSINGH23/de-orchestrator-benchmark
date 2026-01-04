# Feature engineering logic
import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features and aggregations.
    """

    # Example: total revenue
    if {"price", "quantity"}.issubset(df.columns):
        df["total_revenue"] = df["price"] * df["quantity"]

    # Example: aggregation for RQ
    agg_df = df.groupby("category", as_index=False)["total_revenue"].sum()

    return agg_df