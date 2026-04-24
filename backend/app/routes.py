from fastapi import APIRouter
from app.schemas import StudentInput, FeedbackInput
import os
import pandas as pd
from services.prediction_service import PredictionService

service = PredictionService()
router = APIRouter()

# ------------------ PREDICT ------------------
@router.post('/predict')
def predict(data: StudentInput):
    input_data = data.model_dump()

    result = service.predict(input_data)

    prediction = int(result[0])   

    log_path = os.path.join("data", "predictions.csv")
    os.makedirs("data", exist_ok=True)

    row = input_data.copy()
    row["prediction"] = prediction 

    df = pd.DataFrame([row])

    if not os.path.exists(log_path):
        df.to_csv(log_path, index=False)
    else:
        df.to_csv(log_path, mode="a", header=False, index=False)

    return {"prediction": prediction}   # <-- FIX


# ------------------ FEEDBACK ------------------
@router.post("/feedback")
def feedback(data: FeedbackInput):

    file_path = os.path.join("data", "feedback.csv")

    df = pd.DataFrame([data.model_dump()])

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    return {"message": "feedback stored successfully"}


# ------------------ METRICS ------------------
@router.get("/metrics")
def metrics():

    file_path = os.path.join("data", "feedback.csv")

    if not os.path.exists(file_path):
        return {"message": "No feedback data yet"}

    df = pd.read_csv(file_path)

    accuracy = (df["predicted"] == df["actual"]).mean()

    return {
        "total_samples": len(df),
        "accuracy": float(accuracy)
    }

@router.post("/retrain")
def retrain():
    from ml.retrain import retrain_model

    result = retrain_model()

    return {
        "message": "Model retrained",
        "details": result
    }