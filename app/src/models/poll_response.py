# app/src/models/poll_response.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PollResponse(Base):
    __tablename__ = "pollresponse"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, nullable=False)  # "telegram" or "whatsapp"
    user_id = Column(String, nullable=False)
    username = Column(String, nullable=True)
    response = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
