import pandas as pd

def preprocess(data):

    df=pd.read_csv(data)

    df=df.drop(columns=["ExamScore", "Gender"])

    X=df.drop("FinalGrade",axis=1)
    y=df[["FinalGrade"]]

    return X,y



