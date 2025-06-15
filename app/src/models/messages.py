from sqlmodel import SQLModel, Field
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class SendTextMessageRequest(SQLModel):
    recipient_number: str
    message: str


class SendPollMessageRequest(SQLModel):
    recipient_number: str


class MessageData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message_sid: str = Field(index=True, nullable=False)
    account_sid: str = Field(index=True, nullable=False)
    from_number: str = Field(index=False, nullable=False)
    to_number: str = Field(index=False, nullable=False)
    body: str = Field(index=False, nullable=False)
    num_media: Optional[int] = Field(default=0)
    profile_name: Optional[str] = None
    wa_id: Optional[str] = None
    created_at: datetime = Field(default=datetime.utcnow)
