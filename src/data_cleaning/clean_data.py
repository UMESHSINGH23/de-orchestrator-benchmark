# Data cleaning logic
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw data:
    - handle missing values
    - fix data types
    - remove duplicates
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna(subset=df.columns, how="any")

    # Example: convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df