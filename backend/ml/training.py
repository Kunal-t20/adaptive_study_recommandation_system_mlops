import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from ml.preprocessing import preprocess

mlflow.set_experiment("adaptive_recommendation")

def train_model(data_path):

    with mlflow.start_run():

        X, y = preprocess(data_path)

        X_train, X_test, y_train, y_test = train_test_split(X, y)

        model = RandomForestClassifier(n_estimators=100, max_depth=10)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        # logs
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 10)
        mlflow.log_metric("accuracy", acc)

        mlflow.sklearn.log_model(model, "model")

        print("Run ID:", mlflow.active_run().info.run_id)

        return model

if __name__ == "__main__":
    train_model("data/student_performance.csv")