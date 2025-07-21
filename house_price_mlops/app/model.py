import pandas as pd
import joblib
from app.preprocess import build_pipeline

def train_and_save_model():
    df = pd.read_csv("data/house_data.csv")

    selected_columns = [
    "bedrooms", "bathrooms", "sqft_living", "sqft_lot",
    "floors", "waterfront", "view", "condition",
    "sqft_above", "sqft_basement", "yr_built", "yr_renovated"
    ]


    y = df["price"]
    X = df[selected_columns]

    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = X.select_dtypes(include="object").columns.tolist()

    pipeline = build_pipeline(numeric, categorical)
    model = pipeline.fit(X, y)

    joblib.dump(model, "model/model.pkl")

if __name__ == "__main__":
    train_and_save_model()
