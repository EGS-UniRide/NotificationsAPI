from fastapi import FastAPI
from src.notif import notifRouter
app = FastAPI()

app.include_router(notifRouter)