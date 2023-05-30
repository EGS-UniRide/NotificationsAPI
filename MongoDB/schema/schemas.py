def individual_serial(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]

def single_driver(driver) -> dict:
    return{
        "id": str(driver["_id"]),
        "name": driver["name"],
        "email": driver["email"],
        "licence_plate": driver["licence_plate"],
        "car_model": driver["car_model"],
        "answer1": driver["answer1"], 
        "answer2": driver["answer2"], 
        "answer3": driver["answer3"]
    }

def list_drivers(drivers) -> list:
    return[single_driver(driver) for driver in drivers]

def single_user(user) -> dict:
    return{
        "id": str(user["_id"]),
        "name": user["name"]
    }

def list_users(users) -> list:
    return[single_user(user) for user in users]

def single_trip(trip) -> dict:
    return{
        "id": str(trip["_id"]),
        "begining": trip["_id"],
        "destination": trip["name"],
        "date": trip["date"],
        "userId": str(trip["userId"]),
        "driverId": str(trip["driverId"]),
    }

def list_trips(trips) -> list:
    return[single_trip(trip) for trip in trips]

def single_payment(payment) -> dict:
    return{
        "id": str(payment["_id"]),
        "userId": str(payment["userId"]),
        "price": payment["price"],
        "date": payment["date"],
        "travelId": str(payment["travelId"])
    }

def list_payments(payments) -> list:
    return[single_payment(payment) for payment in payments]