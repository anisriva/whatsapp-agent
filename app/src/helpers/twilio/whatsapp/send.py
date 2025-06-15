import json
from app.src.connectors.twilio import get_twilio_client
from app.src.config.twilio import get_twilio_config


async def send_text(recipient_number: str, message: str):
    client = get_twilio_client()
    bot_number = get_twilio_config()["whatsapp_number"]
    try:
        message = client.messages.create(
            body=message,
            from_=f"whatsapp:{bot_number}",
            to=f"whatsapp:{recipient_number}",
        )
        return message.sid
    except Exception as e:
        print(f"Error sending text: {e}")
        raise e


async def send_healthcheckin(
    recipient_number: str,
):
    client = get_twilio_client()
    config = get_twilio_config()
    bot_number = config["whatsapp_number"]
    try:
        message = client.messages.create(
            from_=f"whatsapp:{bot_number}",
            to=f"whatsapp:{recipient_number}",
            content_sid=config["content_sid"],
            content_variables=json.dumps({
                "1": "Daily health check-ins", 
                "3": "qbdcuh"
            }),
        )
        return message.sid
    except Exception as e:
        print(f"Error sending feedback link: {e}")
        raise e


async def feedback():
    pass
