from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone


class SendTextMessageRequest(SQLModel):
    recipient_number: str
    message: str


class SendPollMessageRequest(SQLModel):
    recipient_number: str


class MessageData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message_sid: str
    account_sid: str
    wa_id: Optional[str] = None
    from_number: str
    to_number: str
    body: str
    profile_name: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
