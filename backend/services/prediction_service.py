import mlflow.pyfunc
import pandas as pd
import os


class PredictionService:

    def __init__(self):

        try:
            if os.getenv("TESTING") == "1":
                self.model = None

            elif os.getenv("DOCKER") == "1":
                self.model = mlflow.pyfunc.load_model("model")

            else:
                self.model = mlflow.pyfunc.load_model(
                    "models:/adaptive_model@production"
                )

        except Exception as e:
            print("Model loading failed:", e)
            self.model = None

    def predict(self, data):

        df = pd.DataFrame([data])

        df = df[[
            "StudyHours", "Attendance", "Resources", "Extracurricular",
            "Motivation", "Internet", "Age", "LearningStyle",
            "OnlineCourses", "Discussions", "AssignmentCompletion",
            "EduTech", "StressLevel"
        ]]

        if self.model is None:
            return [1]

        prediction = self.model.predict(df)

        return list(prediction)