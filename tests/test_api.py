import sys
import os
from fastapi.testclient import TestClient

# 1. FIX THE PATH FIRST
sys.path.append(os.getcwd())

# 2. NOW IMPORT YOUR APP
from api.app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Credit Risk Prediction API is online"}

def test_predict_safe():
    payload = {
        "age": 40,
        "income": 80000,
        "loan_amount": 5000,
        "credit_score": 750,
        "employment_years": 10
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
