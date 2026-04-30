import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
import os

def transform_data():
    # 1. Load data
    train_df = pd.read_parquet("data/processed/train.parquet")
    test_df = pd.read_parquet("data/processed/test.parquet")
    
    # 2. Separate Features and Target
    X_train = train_df.drop("target", axis=1)
    y_train = train_df["target"].values
    X_test = test_df.drop("target", axis=1)
    y_test = test_df["target"].values

    # 3. Simple Transformation (Since our synthetic data is all numbers)
    # We use a basic imputer and scaler for all feature columns
    preprocessor = StandardScaler()

    # 4. Fit and Transform
    X_train_transformed = preprocessor.fit_transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)
    
    # 5. Save arrays
    os.makedirs("data/processed", exist_ok=True)
    np.save("data/processed/X_train.npy", X_train_transformed)
    np.save("data/processed/X_test.npy", X_test_transformed)
    np.save("data/processed/y_train.npy", y_train)
    np.save("data/processed/y_test.npy", y_test)
    
    # 6. Save preprocessor
    joblib.dump(preprocessor, "data/processed/preprocessor.pkl")
    
    # This print will help us debug if it happens again
    print(f"Transformation complete. Features detected: {X_train.columns.tolist()}")
    print(f"New Shape: {X_train_transformed.shape}")

if __name__ == "__main__":
    transform_data()
