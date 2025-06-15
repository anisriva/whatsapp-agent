from typing import Any
from app.src.models.messages import MessageData


def create_message_data(form_data: Any) -> MessageData:
    """
    Creates a MessageData object from form data, sanitizing the input.
    """
    message_data = {
        "message_sid": form_data.get("MessageSid"),
        "account_sid": form_data.get("AccountSid"),
        "from_number": form_data.get("From", "").replace(
            "whatsapp:", ""
        ),  # Format: whatsapp:+1234567890
        "to_number": form_data.get("To", "").replace(
            "whatsapp:", ""
        ),  # Format: whatsapp:+1234567890
        "body": form_data.get("Body", ""),
        "num_media": int(form_data.get("NumMedia", 0)),
        "profile_name": form_data.get("ProfileName"),
        "wa_id": form_data.get("WaId"),
    }
    return MessageData.model_validate(message_data)
