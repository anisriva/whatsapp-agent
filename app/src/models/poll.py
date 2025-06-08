from sqlmodel import SQLModel, Field
from datetime import datetime

class PollResponse(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    answer: int
    timestamp: datetime
