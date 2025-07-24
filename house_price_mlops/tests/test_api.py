from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "bedrooms": 3,
        "bathrooms": 2.5,
        "sqft_living": 2000,
        "sqft_lot": 5000,
        "floors": 2,
        "waterfront": 0,
        "view": 0,
        "condition": 3,
        "sqft_above": 1800,
        "sqft_basement": 200,
        "yr_built": 1990,
        "yr_renovated": 0
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
