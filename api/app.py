from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
from api.schemas import LoanApplication

app = FastAPI(title="Credit Risk API")

model = joblib.load("models/model.pkl")
preprocesor = joblib.load("data/processed/preprocessor.pkl")


@app.get("/")
def home():
    return {"message": "Credit Risk Prediction API is online"}

@app.post("/predict")
def predict(data: LoanApplication):
    input_data = pd.DataFrame([data.model_dump()])
    transformed_data = preprocesor.transform(input_data)
    prediction = model.predict(transformed_data)


    result = "Default" if prediction[0] == 1 else "Safe"
    return {
        "status": "Success",
        "prediction": result,
        "default_probability": float(model.predict_proba(transformed_data)[0][1])
    }