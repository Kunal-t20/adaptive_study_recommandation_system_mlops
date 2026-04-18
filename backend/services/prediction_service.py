import joblib
import numpy as np

model=joblib.load("models/model.pkl")

def predict_student(data_dict):
    values = list(data_dict.values())
    arr = np.array(values).reshape(1, -1)
    prediction = model.predict(arr)
    return int(prediction[0])