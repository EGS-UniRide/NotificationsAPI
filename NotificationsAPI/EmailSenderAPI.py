from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import schemas, crud

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


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
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return db.query(models.Notifications).all()

@app.post("/v1/email")
async def simple_send(email: schemas.EmailSchema, db: Session = Depends(get_db)):

    notifModel = models.Notifications()

    notifModel.address = email.address
    notifModel.subject = email.subject
    notifModel.description = email.description

    db.add(notifModel)
    db.commit()

    # -----------------------------------------------------
    html = """<p>You have recieved an Email from the UniRinde EmailAPI</p> """

    print(email)

    print(email.dict().get("email"))

    message = MessageSchema(
        subject="API Email Sending",
        recipients=email.dict().get("email"), # List of recipients
        body=html,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

@app.post("/v2/email")
async def simple_send(email: schemas.EmailSchema , db: Session = Depends(get_db)):

    notifModel = models.Notifications()

    notifModel.address = email.address
    notifModel.subject = email.subject
    notifModel.description = email.description

    db.add(notifModel)
    db.commit()
    db.refresh(notifModel)
    # -----------------------------------------------------

    #print(email.address.split())
    #print(email.dict().get("email"))

    message = MessageSchema(
        subject=email.subject,
        recipients=email.address.split(),
        body=email.description,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@app.get("/v2/emails")
async def get_notifs(address1: str, db: Session = Depends(get_db)):
    db_bill = crud.get_notif_by_address(db=db, address=address1)
    if db_bill != None:
        return db_bill
    else:
        raise HTTPException(status_code=404, detail="Notification not found")
    

@app.delete("/v2/email/{notifId}")
async def delete_notif(notifId: str , db: Session = Depends(get_db)):
    db_notif = crud.get_notif_by_id(db, id=notifId)
    if db_notif != None:
        return crud.delete_notification(db, id=notifId)
    else:
        raise HTTPException(status_code=404, detail="Notification not found")