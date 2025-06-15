from fastapi import APIRouter
from app.src.controllers.twilio_messages_controller import (
    send_whatsapp_message,
    send_whatsapp_poll,
    receive_whatsapp_message
)

router = APIRouter(prefix="/twilio")

router.post("/send_message", tags=["messages"])(send_whatsapp_message)
router.post("/send_poll", tags=["messages"])(send_whatsapp_poll)
router.post("/receive_message", tags=["messages"])(receive_whatsapp_message)