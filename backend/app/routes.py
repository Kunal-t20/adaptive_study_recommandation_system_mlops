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
    result = service.predict(data.dict())
    return {"Prediction": result}


# ------------------ FEEDBACK ------------------
@router.post("/feedback")
def feedback(data: FeedbackInput):

    # correct path (important)
    file_path = os.path.join("data", "feedback.csv")

    # convert to dataframe
    df = pd.DataFrame([data.dict()])

    # ensure folder exists
    os.makedirs("data", exist_ok=True)

    # save data
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    return {"message": "feedback stored successfully"}