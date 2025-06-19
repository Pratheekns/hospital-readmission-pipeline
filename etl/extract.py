# etl/extract.py

import pandas as pd
import os

def extract_data(file_path):
    """
    Extracts raw hospital readmission data from CSV file.

    Args:
        file_path (str): Path to the raw data CSV file.

    Returns:
        pd.DataFrame: Extracted data as a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    print(f"[INFO] Loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df


if __name__ == "__main__":
    raw_file = "data/raw/train_df.csv"  
    df = extract_data(raw_file)
    print(df.head())
