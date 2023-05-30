from fastapi import APIRouter
from models.todos import Payment
from config.database import payment_collection
from schema.schemas import list_payments
from bson import ObjectId

paymentRouter = APIRouter(
    prefix="/main/payment",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

@paymentRouter.get("/")
async def get_payments():
    payment = list_payments(payment_collection.find())
    return payment

@paymentRouter.post("/")
async def post_payment(user: Payment):
    payment_collection.insert_one(dict(user))

@paymentRouter.put("/{id}")
async def put_payment(id: str, payment: Payment):
    payment_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(payment)})

@paymentRouter.delete("/{id}")
async def delete_payment(id: str):
    payment_collection.find_one_and_delete({"_id": ObjectId(id)})