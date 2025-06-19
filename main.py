# main.py

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import os

# Define file paths
RAW_FILE_PATH = "data/raw/train_df.csv"
CLEANED_FILE_PATH = "data/processed/cleaned_data.csv"

def main():
    print("Starting ETL pipeline...")

    # Step 1: Extract
    df_raw = extract_data(RAW_FILE_PATH)

    # Step 2: Transform
    df_cleaned = transform_data(df_raw)

    # Step 3: Load
    load_data(df_cleaned, CLEANED_FILE_PATH)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()
