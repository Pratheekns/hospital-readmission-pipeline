# etl/load.py

import pandas as pd
import os

def load_data(df: pd.DataFrame, output_path: str):
    """
    Saves the cleaned DataFrame to a CSV file.

    Args:
        df (DataFrame): The cleaned data to be saved.
        output_path (str): Destination path to save the file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Cleaned data saved to {output_path}")
