from fastapi import APIRouter
from app.src.controllers.twilio_messages_controller import (
    send_whatsapp_message,
    send_whatsapp_poll
)

router = APIRouter(prefix="/twilio")

router.post("/send_message", tags=["message"])(send_whatsapp_message)
router.post("/send_poll", tags=["message"])(send_whatsapp_poll)