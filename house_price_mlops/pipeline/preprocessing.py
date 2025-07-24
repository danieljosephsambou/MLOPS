import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    features = [
        'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
        'floors', 'waterfront', 'view', 'condition',
        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated'
    ]
    return df[features]

def build_preprocessing_pipeline():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])
