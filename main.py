from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="STD24209", description="This is a specification of STD24209")


class Characteristic(BaseModel):
    max_speed: float
    max_fuel_capacity: float

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

class CarUpdate(BaseModel):
    characteristics: Characteristic


cars_db = []


@app.get("/ping")
async def ping():
    return "pong"

@app.post("/cars", status_code=status.HTTP_201_CREATED)
async def create_cars(cars: List[Car]):
    cars_db.extend(cars)
    return {"message": "Cars created successfully", "count": len(cars)}

@app.get("/cars")
async def get_all_cars():
    return cars_db



