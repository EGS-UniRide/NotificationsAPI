from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

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

@app.get("/")
async def root():
    return {"message":"EmailAPI"}

@app.post("/email")
async def simple_send(email: EmailSchema):

    print(email.address.split())

    print(email.dict().get("email"))

    message = MessageSchema(
        subject=email.subject,
        recipients=email.address.split(), # List of recipients
        body=email.description,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

