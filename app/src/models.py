from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.src.connectors.db import Base

class PollResponse(Base):
    __tablename__ = 'pollresponse'

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)  # 'telegram' or 'whatsapp'
    user_id = Column(String)
    username = Column(String, nullable=True)
    question = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)