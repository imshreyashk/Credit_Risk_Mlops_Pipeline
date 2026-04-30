from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_read_main():
    # Tests if the API home page is up
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Credit Risk Prediction API is online"}

def test_predict_safe():
    # Tests a 'Safe' applicant scenario
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
    assert "default_probability" in response.json()
