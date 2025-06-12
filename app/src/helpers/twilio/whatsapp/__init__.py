from app.src.connectors.twilio import get_twilio_client
from app.src.config.twilio import get_twilio_config

async def send_whatsapp_message(to_number:str, message_body: str):
    client = get_twilio_client()
    bot_number = get_twilio_config()["whatsapp_number"]
    message = client.messages.create(
        body=message_body,
        from_=f'whatsapp:{bot_number}',
        to=f'whatsapp:{to_number}'
    )
    print(message)
    return message.sid
