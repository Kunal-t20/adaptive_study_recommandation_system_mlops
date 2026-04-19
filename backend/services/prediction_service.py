import mlflow.pyfunc
import pandas as pd

class PredictionService:

    def __init__(self):
        self.model = mlflow.pyfunc.load_model(
            "models:/adaptive_model@production"
        )

    def predict(self, data):
        # dict → DataFrame
        df = pd.DataFrame([data])

        # enforce correct column order (VERY IMPORTANT)
        df = df[[
            "StudyHours", "Attendance", "Resources", "Extracurricular",
            "Motivation", "Internet", "Age", "LearningStyle",
            "OnlineCourses", "Discussions", "AssignmentCompletion",
            "EduTech", "StressLevel"
        ]]

        # prediction
        prediction = self.model.predict(df)

        return prediction.tolist()  # make it JSON serializable