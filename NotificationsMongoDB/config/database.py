from pymongo import MongoClient

#client = MongoClient("mongodb+srv://UnirideSupport:marcusmiller567@uniridecluster.svdfg3t.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient('mongodb://localhost:27017')
db = client.NotifDB

notif_collection = db["notifications"]