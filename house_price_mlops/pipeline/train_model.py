import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from pipeline.preprocessing import preprocess_data, build_preprocessing_pipeline
import os

def train():
    df = pd.read_csv("/opt/airflow/data/house_data.csv")
    X = preprocess_data(df)
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessing_pipeline = build_preprocessing_pipeline()
    X_train_prepared = preprocessing_pipeline.fit_transform(X_train)

    model = LinearRegression()
    model.fit(X_train_prepared, y_train)

    from sklearn.pipeline import make_pipeline
    full_pipeline = make_pipeline(preprocessing_pipeline, model)

    joblib.dump(full_pipeline, "/opt/airflow/models/house_price_model.pkl")
    print("✅ Modèle entraîné et sauvegardé dans /opt/airflow/models/")

if __name__ == "__main__":
    train()
    print("✅ Modèle entraîné et sauvegardé dans /opt/airflow/models/")