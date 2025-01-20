
import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "House Price Prediction" in response.text

@pytest.mark.asyncio
async def test_predict_price():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/predict/", json={
            "car_parks": 2,
            "size_num": 1000,
            "location": "suburb",
            "furnishing": "unfurnished"
        })
    assert response.status_code == 200
    assert "predicted_price" in response.json()
