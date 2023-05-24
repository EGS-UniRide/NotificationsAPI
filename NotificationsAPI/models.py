from sqlalchemy import Column, Integer, String
from database import Base

class Notifications(Base):
    __tablename__ = "Notifications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, default=None)
    address = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    description = Column(String, nullable=False)