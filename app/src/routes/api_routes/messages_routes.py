from fastapi import APIRouter
from app.src.controllers.messages_controller import (
    send_message
)

router = APIRouter()

router.post("/send_message", tags=["message"])(send_message)