# Data ingestion logic
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load raw dataset from CSV and verify ingestion.
    """
    df = pd.read_csv('data/sample/pakistan_data.csv')

    # Verification checks
    assert not df.empty, "ERROR: Loaded DataFrame is empty"
    assert df.shape[1] > 1, "ERROR: Dataset has only one column"

    print("✅ Data ingestion successful")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Column names:", df.columns.tolist())

    return df