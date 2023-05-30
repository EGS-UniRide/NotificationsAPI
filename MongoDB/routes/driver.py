from fastapi import APIRouter
from models.todos import Driver
from config.database import driver_collection
from schema.schemas import list_drivers
from bson import ObjectId

driverRouter = APIRouter(
    prefix="/main/driver",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

@driverRouter.get("/")
async def get_drivers():
    drivers = list_drivers(driver_collection.find())
    return drivers

@driverRouter.post("/")
async def post_driver(user: Driver):
    driver_collection.insert_one(dict(user))

@driverRouter.put("/{id}")
async def put_driver(id: str, driver: Driver):
    driver_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(driver)})

@driverRouter.delete("/{id}")
async def delete_driver(id: str):
    driver_collection.find_one_and_delete({"_id": ObjectId(id)})