from pydantic import BaseModel, Field
from datetime import datetime

class Driver(BaseModel):
    name: str
    email: str
    phone: str
    licence_plate: str
    car_model: str
    answer1: str
    answer2: str
    answer3: str

    #answers: dict = Field(..., example={
    #    "answer1": "yes",
    #    "answer2": "yes",
    #    "answer3": "yes"
    #})


class User(BaseModel):
    name: str

class Trip(BaseModel):
    begining: str
    destination: str
    date: datetime
    userId: str
    driverId: str

class Payment(BaseModel):
    userId: str
    price: float
    date: datetime
    travelId: str