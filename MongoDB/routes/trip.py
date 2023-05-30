from fastapi import APIRouter
from models.todos import Trip
from config.database import trip_collection
from schema.schemas import list_trips
from bson import ObjectId

tripRouter = APIRouter(
    prefix="/main/trip",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

@tripRouter.get("/")
async def get_trips():
    trips = list_trips(trip_collection.find())
    return trips

@tripRouter.post("/")
async def post_trip(user: Trip):
    trip_collection.insert_one(dict(user))

@tripRouter.put("/{id}")
async def put_trip(id: str, trip: Trip):
    trip_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(trip)})

@tripRouter.delete("/{id}")
async def delete_trip(id: str):
    trip_collection.find_one_and_delete({"_id": ObjectId(id)})