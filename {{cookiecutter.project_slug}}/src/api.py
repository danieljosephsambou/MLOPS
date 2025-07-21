from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("modele_rf.pkl")  # suppose que tu as sauvegardé ton modèle

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API ML"}

@app.post("/predict")
def make_prediction(data: list[float]):
    prediction = model.predict([data])
    return {"prediction": prediction.tolist()}
