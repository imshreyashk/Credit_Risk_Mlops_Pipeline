import sys
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 1. GUARANTEE FILES EXIST BEFORE IMPORTS
os.makedirs("models", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

if not os.path.exists("models/model.pkl"):
    joblib.dump(RandomForestClassifier().fit([[0,0,0,0,0]], [0]), "models/model.pkl")

if not os.path.exists("data/processed/preprocessor.pkl"):
    joblib.dump(StandardScaler().fit([[0,0,0,0,0]]), "data/processed/preprocessor.pkl")

# 2. FIX THE PATH
sys.path.append(os.getcwd())

# 3. NOW IMPORT
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Credit Risk Prediction API is online"}

def test_predict():
    payload = {
        "age": 30, "income": 50000, "loan_amount": 10000, 
        "credit_score": 700, "employment_years": 5
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
