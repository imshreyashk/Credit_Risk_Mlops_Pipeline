import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import yaml
import mlflow
import mlflow.sklearn
import json


def train_model():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    X_train = np.load("data/processed/X_train.npy")
    y_train = np.load("data/processed/y_train.npy")

    mlflow.set_experiment("Credit_Risk_Training")

    with mlflow.start_run():
        rf = RandomForestClassifier(
            n_estimators=params['model']['n_estimators'],
            max_depth=params['model']['max_depth'],
            random_state=42
        )
        rf.fit(X_train, y_train)

        mlflow.log_params(params['model'])
        mlflow.sklearn.log_model(rf, "model")

        os.makedirs("models", exist_ok=True)
        joblib.dump(rf, "models/model.pkl")

        train_score = rf.score(X_train, y_train)
        metrics = {"train_accuracy": train_score}
        
        os.makedirs("metrics", exist_ok=True)
        with open("metrics/scores.json", "w") as f:
            json.dump(metrics, f)

        mlflow.log_metrics(metrics)


        print("Training complete. Model saved to models/model.pkl")

if __name__ == "__main__":
    train_model()