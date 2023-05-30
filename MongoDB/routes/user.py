from fastapi import APIRouter
from models.todos import User
from config.database import user_collection
from schema.schemas import list_users
from bson import ObjectId

userRouter = APIRouter(
    prefix="/main/user",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

@userRouter.get("/")
async def get_users():
    users = list_users(user_collection.find())
    return users

@userRouter.post("/")
async def post_user(user: User):
    user_collection.insert_one(dict(user))

@userRouter.put("/{id}")
async def put_user(id: str, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

@userRouter.delete("/{id}")
async def delete_user(id: str):
    user_collection.find_one_and_delete({"_id": ObjectId(id)})
