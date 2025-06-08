from fastapi import FastAPI, Request
from app.src.connectors.db import get_session
from app.src.models import PollResponse
import datetime

app = FastAPI()

@app.post("/webhook/twilio")
async def twilio_webhook(request: Request):
    form = await request.form()
    from_number = form.get("From")
    body = form.get("Body")

    session = get_session()
    session.add(PollResponse(
        platform="whatsapp",
        user_id=from_number,
        question="Did you go to the gym today?",
        response=body,
        timestamp=datetime.datetime.utcnow()
    ))
    session.commit()
    return "OK"

