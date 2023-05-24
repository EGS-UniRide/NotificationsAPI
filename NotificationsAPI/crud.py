from sqlalchemy.orm import Session

import models

def get_notif_by_id(db: Session, notif_id: str):
    return db.query(models.Notifications).filter(models.Notifications.id == notif_id).first()

def get_notif_by_address(db: Session, address: str, skip: int = 0, limit: int = 20):
    return db.query(models.Notifications).filter(models.Notifications.address == address).offset(skip).limit(limit).all()

def get_notifications(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Notifications).offset(skip).limit(limit).all()

def delete_notification(db: Session, id: str):
    bill = db.query(models.Notifications).filter(models.Notifications.id == id).delete()
    db.commit()
    return bill