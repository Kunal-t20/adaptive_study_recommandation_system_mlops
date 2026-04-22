# Adaptive Learning Recommendation System (MLOps)

## Overview

This project is an end-to-end MLOps system that predicts student performance and continuously improves using real-world feedback.

Unlike traditional machine learning projects, this system is **adaptive** — it collects user feedback, retrains the model, and deploys updated versions automatically.

---

## Key Features

- Student performance prediction using ML model
- User-friendly Streamlit frontend
- FastAPI backend for inference
- Feedback collection for continuous learning
- Automated retraining pipeline
- MLflow for experiment tracking and model versioning
- CI/CD pipeline using GitHub Actions
- Dockerized deployment

---

## System Architecture
```
User → Streamlit UI → FastAPI API → ML Model → Prediction
                ↓
            Feedback Collection → Retraining → MLflow → Updated Model
```


---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- MLflow
- Docker
- GitHub Actions (CI/CD)

---

## Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │
│   ├── services/
│   │   └── prediction_service.py
│   │
│   ├── ml/
│   │   ├── preprocessing.py
│   │   ├── training.py
│   │   └── retrain.py
│   │
│   ├── data/
│   │   ├── student_performance.csv
│   │   ├── feedback.csv
│   │   └── predictions.csv
│   │
│   ├── tests/
│   │   ├── test_api.py
│   │   └── conftest.py
│   │
│   ├── mlruns/        # MLflow artifacts
│   ├── notebook/
│   │   └── notebook.ipynb
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── mlflow.db
│
├── frontend/
│   └── app.py
│
├── .github/workflows/
│   └── ci_cd.yml
│
└── README.md

```


---

## How It Works

1. User enters input via Streamlit UI  
2. FastAPI processes the request and returns prediction  
3. User can submit actual results as feedback  
4. Feedback is stored and used for retraining  
5. New model is trained and logged using MLflow  
6. Best model is promoted to production  
7. CI/CD pipeline builds and deploys updated system  

---

## Running the Project

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```
### frontend

```bash
cd frontend
streamlit run app.py
```

### MLFlow

```bash
mlflow ui
```

### Docker
- build image:
```bash
docker build -t yourusername/app:latest backend/

- run container:
docker run -p 8000:8000 yourusername/app:latest
```

### CI/CD Pipeline
1. Runs tests using pytest
2. Builds Docker image
3. Pushes image to Docker Hub

### API Endpoints
- POST /predict → Get prediction
- POST /feedback → Store feedback
- GET /metrics → View performance
- POST /retrain → Retrain model

### Benefits
1. Continuous model improvement using feedback
2. Production-ready architecture
3. Automated testing and deployment
4. Scalable system design

### Future Improvements
1. Cloud deployment (AWS / GCP)
2. Authentication system
3. Better UI/UX
4. Scheduled retraining

### Conclusion

This project demonstrates how to build a complete MLOps pipeline where models are not static but continuously evolve using real-world data.

