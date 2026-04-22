from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict():
    payload = {
        "StudyHours": 5,
        "Attendance": 80,
        "Resources": 6,
        "Extracurricular": 1,
        "Motivation": 7,
        "Internet": 1,
        "Age": 20,
        "LearningStyle": 2,
        "OnlineCourses": 2,
        "Discussions": 4,
        "AssignmentCompletion": 8,
        "EduTech": 5,
        "StressLevel": 3
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "Prediction" in response.json()


def test_feedback():
    payload = {
        "StudyHours": 5,
        "Attendance": 80,
        "Resources": 6,
        "Extracurricular": 1,
        "Motivation": 7,
        "Internet": 1,
        "Age": 20,
        "LearningStyle": 2,
        "OnlineCourses": 2,
        "Discussions": 4,
        "AssignmentCompletion": 8,
        "EduTech": 5,
        "StressLevel": 3,
        "predicted": 1,
        "actual": 0
    }

    response = client.post("/feedback", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "feedback stored successfully"


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200