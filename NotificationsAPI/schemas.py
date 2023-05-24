from pydantic import BaseModel

class EmailSchema(BaseModel):
    id: int = None
    address: str
    subject: str
    description: str
    
    class Config:
        orm_mode = True