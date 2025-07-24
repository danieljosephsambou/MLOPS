import joblib
import os
import numpy as np

def load_model(model_path: str = "models/house_price_model.pkl"):
    return joblib.load(model_path)

def predict_price(model, input_data: dict) -> float:
    features = np.array([list(input_data.values())])
    return model.predict(features)[0]
