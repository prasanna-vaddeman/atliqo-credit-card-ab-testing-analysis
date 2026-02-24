import os
import pandas as pd

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"

def save_raw(df: pd.DataFrame, filename: str):
    os.makedirs(RAW_PATH, exist_ok=True)
    full_path = os.path.join(RAW_PATH, filename)
    df.to_csv(full_path, index=False)
    print(f"✔ Saved RAW file: {full_path}")


def save_processed(df: pd.DataFrame, filename: str):
    os.makedirs(PROCESSED_PATH, exist_ok=True)
    full_path = os.path.join(PROCESSED_PATH, filename)
    df.to_csv(full_path, index=False)
    print(f"✔ Saved PROCESSED file: {full_path}")