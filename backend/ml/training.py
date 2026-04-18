from ml.preprocessing import preprocess
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


def train_model(data_path):

    X,y = preprocess(data_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model=RandomForestClassifier()

    model.fit(X_train, y_train)

    y_pred=model.predict(X_test)

    acc=accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc}")

    path=joblib.dump(model, "models/model.pkl")
    print("Saved at:", path)

    return model


if __name__ == "__main__":
    train_model("data/student_performance.csv")