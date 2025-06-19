# etl/transform.py

import pandas as pd
import os

def transform_data(df):
    """
    Cleans and transforms the raw hospital data.

    Args:
        df (pd.DataFrame): Raw DataFrame.

    Returns:
        pd.DataFrame: Cleaned and transformed DataFrame.
    """
    # Rename columns for readability
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Encode gender: Male=1, Female=0
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Encode discharge_to and primary_diagnosis using one-hot encoding
    df = pd.get_dummies(df, columns=["discharge_to", "primary_diagnosis"], drop_first=True)

    # Return cleaned DataFrame
    return df


if __name__ == "__main__":
    raw_file = "data/raw/train_df.csv"
    output_file = "data/processed/cleaned_data.csv"

    # Load raw
    df_raw = pd.read_csv(raw_file)

    # Transform
    df_clean = transform_data(df_raw)

    # Save
    os.makedirs("data/processed", exist_ok=True)
    df_clean.to_csv(output_file, index=False)

    print(f"[INFO] Cleaned data saved to {output_file}")
    print(df_clean.head())
