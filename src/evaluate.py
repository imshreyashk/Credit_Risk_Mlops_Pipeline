import pandas as pd
import numpy as np
import joblib
import json
import os
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model():

    model = joblib.load("models/model.pkl")
    X_test = np.load("data/processed/X_test.npy")
    y_test = np.load("data/processed/y_test.npy")

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1_score": f1_score(y_test, predictions)
    }

    os.makedirs("metrics", exist_ok=True)
    with open("metrics/evaluation.json", "w") as f:
        json.dump(metrics, f)

    mlflow.set_experiment("Credit_Risk_Training")
    with mlflow.start_run(run_name="Evaluation_Run"):
        mlflow.log_metrics(metrics)

    print(f"Evaluation complete. Accuracy: {metrics['accuracy']:.4f}")

if __name__ == "__main__":
    evaluate_model()