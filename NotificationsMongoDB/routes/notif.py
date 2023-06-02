from fastapi import APIRouter, Body, Request
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from models.models import Notification
from config.database import notif_collection
from schema.schemas import list_notifs
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
#from config.database import db

notifRouter = APIRouter(
    prefix="/notif",
    tags=["main"],
    responses={404: {"description": "Not found"}},
)

conf = ConnectionConfig(
    MAIL_USERNAME = "supp.uniride@gmail.com",
    MAIL_PASSWORD = "drplqaxllmoltzwz",               # password ommited
    MAIL_FROM = "supp.uniride@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="UniRide Support",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = False
)

origins = [
    "http://localhost:8010",
]

@notifRouter.get("/")
async def get_notifs():
    notifs = list_notifs(notif_collection.find())
    return notifs

@notifRouter.put("/{id}")
async def put_notif(id: str, notif: Notification):
    notif_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(notif)})

@notifRouter.delete("/{id}")
async def delete_notif(id: str):
    notif_collection.find_one_and_delete({"_id": ObjectId(id)})

# -------------------------------------------------------------------------------------

@notifRouter.post("/email")
async def simple_send(request: Request, notif: Notification = Body(...)):

    message = MessageSchema(
        subject=notif.subject,
        recipients=notif.address.split(),
        body=notif.description,
        subtype=MessageType.html
        )

    notif = jsonable_encoder(notif)

    notif_collection.insert_one(notif)

    # -----------------------------------------------------

    fm = FastMail(conf)
    await fm.send_message(message)
    return "Success"
