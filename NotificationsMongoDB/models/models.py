from pydantic import BaseModel, EmailStr
from datetime import datetime

class Notification(BaseModel):
    address: EmailStr
    subject: str
    description: str
    