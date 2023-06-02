from fastapi import FastAPI
from routes.notif import notifRouter
app = FastAPI()

app.include_router(notifRouter)