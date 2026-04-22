from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Adaptive Learning Recommendation System",
    description="MLOps-based system with MLflow, feedback loop, retraining and monitoring",
    version="1.0.0"
)

app.include_router(router, tags=["API"])


@app.get("/", tags=["Health"])
def home():
    return {"message": "app is running"}