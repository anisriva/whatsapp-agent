from sqlmodel import SQLModel

class SendTextMessageRequest(SQLModel):
    recipient_number : str
    message : str

class SendPollMessageRequest(SQLModel):
    recipient_number : str
