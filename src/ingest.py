import pandas as pd
from sklearn.model_selection import train_test_split
import os
import numpy as np

def ingest_data():
    print("Generating synthetic credit data...")
    np.random.seed(42)
    n_samples = 1000

    data = {
        'age': np.random.randint(18, 70, n_samples),
        'income': np.random.randint(20000, 150000, n_samples),
        'loan_amount': np.random.randint(1000, 50000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'employment_years': np.random.randint(0, 40, n_samples),
        'target': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
    }

    df = pd.DataFrame(data)

    # Use makedirs here to avoid errors
    os.makedirs("data/raw", exist_ok=True)
    raw_path = "data/raw/credit_risk.csv"
    df.to_csv(raw_path, index=False)
    print(f"Raw data saved to {raw_path}")

    # Standard split: 80% train, 20% test
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    os.makedirs("data/processed", exist_ok=True)
    train_df.to_parquet("data/processed/train.parquet")
    test_df.to_parquet("data/processed/test.parquet")

    print("Ingestion complete: train.parquet and test.parquet created.")

if __name__ == "__main__":
    ingest_data()
