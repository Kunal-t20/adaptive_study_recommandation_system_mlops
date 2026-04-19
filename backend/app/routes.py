from fastapi import APIRouter
from app.schemas import StudentInput,FeedbackInput
import os
from services.prediction_service import PredictionService

service = PredictionService()

router=APIRouter()

@router.post('/predict')
def predict(data:StudentInput):
    result=service.predict(data.dict())

    return {"Prediction":result}


@router.post("/feedback")
def feedback(data: FeedbackInput):
    file_path = "data/feedback.csv"

    df = pd.DataFrame([data.dict()])

    # Check if file exists
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    return {"message": "feedback stored successfully"}
