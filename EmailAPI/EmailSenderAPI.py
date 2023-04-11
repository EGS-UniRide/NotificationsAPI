from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

class EmailSchema(BaseModel):
    address: str
    subject: str
    description: str


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

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"EmailAPI"}

@app.post("/v1/email")
async def simple_send(email: EmailSchema):
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
async def simple_send(email: EmailSchema):

    print(email.address.split())

    print(email.dict().get("email"))

    message = MessageSchema(
        subject=email.subject,
        recipients=email.address.split(),
        body=email.description,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

