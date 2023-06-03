import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    username: str
    email: EmailStr
    phoneNumber: str
    address: str

class UserUpdate(BaseModel):
    id: str = Field(alias="_id")
    name: Optional[str]
    username: Optional[str]
    email: Optional[EmailStr]
    phoneNumber: Optional[str]
    address: Optional[str]

class UserResponse2(BaseModel):
    name: str
    email: EmailStr
    phoneNumber: str
    address: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr

class Driver(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: EmailStr
    phoneNumber: str
    licence_plate: str
    car_model: str
    coordenates: str
    answer1: str
    answer2: str
    answer3: str

class DriverUpdate(BaseModel):
    id: str = Field(alias="_id")
    name: Optional[str]
    email: Optional[EmailStr]
    phoneNumber: Optional[str]
    licence_plate: Optional[str]
    car_model: Optional[str]
    coordenates: Optional[str]
    answer1: Optional[str]
    answer2: Optional[str]
    answer3: Optional[str]

class DriverResponse(BaseModel):
    id: str
    name: str
    licence_plate: str
    car_model: str
    coordenates: str

class DriverResponse2(BaseModel):
    id: str
    answer1: str
    answer2: str
    answer3: str

class DriverResponse3(BaseModel):
    name: str
    email: str
    phoneNumber: str
        
class Trip(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    begining: str
    destination: str
    date: str
    username: str
    driverId: str

class TripUpdate(BaseModel):
    id: str = Field(alias="_id")
    begining: Optional[str]
    destination: Optional[str]
    date: Optional[str]                         #date is still string
    username: Optional[str]
    driverId: Optional[str]

class Payment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    price: float
    date: str
    travelId: str
    username: str

class PaymentUpdate(BaseModel):
    id: str = Field(alias="_id")
    price: Optional[str]
    destination: Optional[str]
    date: Optional[str]                         #date is still string
    travelId: Optional[str]
    username: Optional[str]

'''
@router.get("/bills", response_description="List all Bills", response_model=list[models.Bill])
async def list_books(request: Request):
    bills = list(request.app.database["bills"].find(limit=100))
    return bills

@router.get("/bills/{userid}", response_description="List all Bills of a given user", response_model=list[models.Bill])
async def list_books(userid: str, request: Request):
    bills = list(request.app.database["bills"].find({"payerid": userid}, limit=100))
    return bills

@router.get("/bill/{billid}", response_description="Get a single bill by id", response_model=models.Bill)
async def get_bill(billid: str, request: Request):
    if (bill := request.app.database["bills"].find_one({"_id": billid})) is not None:
        return bill
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bill with ID {billid} not found")

@router.put("/bill/{billid}", response_description="Update a bill", response_model=models.Bill)
async def put_bill(billid: str, request: Request, bill: models.BillUpdate = Body(...)):
    bill = {k: v for k, v in bill.dict().items() if v is not None}
    if len(bill) >= 1:
        update_result = request.app.database["bills"].update_one(
            {"_id": billid}, {"$set": bill}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bill with ID {billid} not found")

    if (
        existing_bill := request.app.database["bills"].find_one({"_id": billid})
    ) is not None:
        return existing_bill

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bill with ID {billid} not found")

@router.post("/bill")
async def post_bill(request: Request, bill: models.Bill = Body(...)):
    bill = jsonable_encoder(bill)
    new_bill = request.app.database["bills"].insert_one(bill)
    created_bill = request.app.database["bills"].find_one(
        {"_id": new_bill.inserted_id}
    )

    return created_bill

@router.delete("/bill/{billid}", response_description="Delete a bill")
async def delete_book(billid: str, request: Request, response: Response):
    delete_result = request.app.database["bills"].delete_one({"_id": billid})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bill with ID {billid} not found")
'''