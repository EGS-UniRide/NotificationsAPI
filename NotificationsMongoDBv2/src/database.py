from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values("/tmp/secrets/.env")

#print(config["DB_USER"])

client = MongoClient(config["DB_URI"], username = config["DB_USER"], password=config["DB_PASS"])
db = client.NotifDB

notif_collection = db["notifications"]