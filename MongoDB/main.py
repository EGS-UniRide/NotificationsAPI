from fastapi import FastAPI
from routes.user import userRouter
from routes.trip import tripRouter
from routes.payment import paymentRouter
from routes.driver import driverRouter
app = FastAPI()

app.include_router(userRouter)
app.include_router(driverRouter)
app.include_router(tripRouter)
app.include_router(paymentRouter)