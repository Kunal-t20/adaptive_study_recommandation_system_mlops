import mlflow.pyfunc
import pandas as pd
import os


class PredictionService:

    def __init__(self):

        if os.getenv("TESTING") == "1":
            self.model = None
        else:
            self.model = mlflow.pyfunc.load_model(
                "models:/adaptive_model@production"
            )

    def predict(self, data):

        # dict → DataFrame
        df = pd.DataFrame([data])

        # enforce correct column order
        df = df[[
            "StudyHours", "Attendance", "Resources", "Extracurricular",
            "Motivation", "Internet", "Age", "LearningStyle",
            "OnlineCourses", "Discussions", "AssignmentCompletion",
            "EduTech", "StressLevel"
        ]]

        # if testing → return dummy output
        if self.model is None:
            return [1]

        prediction = self.model.predict(df)

        return prediction.tolist()