def single_notif(notif) -> dict:
    return{
        "id": str(notif["_id"]),
        "address": notif["address"],
        "subject": notif["subject"],
        "description": notif["description"]
    }

def list_notifs(notifs) -> list:
    return[single_notif(notif) for notif in notifs]