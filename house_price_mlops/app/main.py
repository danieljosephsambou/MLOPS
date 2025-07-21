from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import time
import logging
import yaml
from logger.filters import InfoOnlyFilter
import pandas as pd

# Load logging config
with open("logger/logging_config.yaml") as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

logger = logging.getLogger("app_logger")

app = FastAPI()
model = joblib.load("model/model.pkl")

class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    condition: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int

@app.post("/predict/")
async def predict(features: HouseFeatures, request: Request):
    start_time = time.time()

    input_dict = features.dict()
    input_df = pd.DataFrame([input_dict])  # transforme en DataFrame à une ligne
    prediction = model.predict(input_df)[0]

    duration = time.time() - start_time
    logger.info(f"{request.url.path} | INPUT: {input_dict} | PREDICTION: {prediction} | duration: {duration:.4f}s")
    
    return {"prediction": prediction}
