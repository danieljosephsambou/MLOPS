from fastapi import FastAPI
from app.model import load_model, predict_price
from app.schemas import HouseData, PredictionResponse
from loguru import logger
import time

app = FastAPI()
model = load_model()

@app.post("/predict", response_model=PredictionResponse)
def predict(data: HouseData):
    start_time = time.time()
    input_data = data.dict()
    prediction = predict_price(model, input_data)
    duration = time.time() - start_time

    logger.info({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "inputs": input_data,
        "prediction": prediction,
        "duration": duration
    })

    return {"prediction": prediction}
