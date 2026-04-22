import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlflow.tracking import MlflowClient


def retrain_model():

    df_original = pd.read_csv("data/student_performance.csv")

    try:
        df_feedback = pd.read_csv("data/feedback.csv")
        df_feedback = df_feedback.drop(columns=["predicted"])
        df_feedback = df_feedback.rename(columns={"actual": "Performance"})
        df = pd.concat([df_original, df_feedback], ignore_index=True)
    except:
        df = df_original

    X = df.drop(columns=["Performance"])
    y = df["Performance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print("New Accuracy:", acc)

    mlflow.set_experiment("adaptive_recommendation")

    with mlflow.start_run():

        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 10)
        mlflow.log_metric("accuracy", acc)

        mlflow.sklearn.log_model(model, "model")

        run_id = mlflow.active_run().info.run_id

    model_uri = f"runs:/{run_id}/model"
    result = mlflow.register_model(model_uri, "adaptive_model")

    print("Registered model version:", result.version)

    # ------------------ AUTO PROMOTION ------------------

    client = MlflowClient()
    model_name = "adaptive_model"

    versions = client.search_model_versions(f"name='{model_name}'")

    best_acc = 0
    best_version = None

    for v in versions:
        run_id = v.run_id
        metrics = client.get_run(run_id).data.metrics
        acc_metric = metrics.get("accuracy", 0)

        if acc_metric > best_acc:
            best_acc = acc_metric
            best_version = v.version

    if best_version is not None:
        client.set_registered_model_alias(
            name=model_name,
            alias="production",
            version=best_version
        )

        print(f"Production model set to version {best_version} with accuracy {best_acc}")

    return {
        "new_accuracy": acc,
        "production_version": best_version
    }