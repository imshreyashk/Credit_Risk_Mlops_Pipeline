from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
from api.schemas import LoanApplication

app = FastAPI(title="Credit Risk API")

model = joblib.load("models/model.pkl")
preprocessor = joblib.load("data/processed/preprocessor.pkl")


@app.get("/")
def home():
    return {"message": "Credit Risk Prediction API is online"}

@app.post("/predict")
def predict(data: LoanApplication):
    # 1. Convert to DataFrame
    input_data = pd.DataFrame([data.model_dump()])
    
    # 2. Transform and Predict
    transformed_data = preprocessor.transform(input_data)
    prediction = model.predict(transformed_data)
    
    # 3. Safely get probability
    try:
        prob = float(model.predict_proba(transformed_data)[0][1])
    except (IndexError, AttributeError):
        # Fallback if model only has 1 class (like in our CI test)
        prob = 1.0 if prediction[0] == 1 else 0.0
        
    result = "Default" if prediction[0] == 1 else "Safe"
    
    return {
        "status": "Success",
        "prediction": result,
        "default_probability": prob
    }
