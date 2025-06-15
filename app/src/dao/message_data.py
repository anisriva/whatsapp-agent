from app.src.models.messages import MessageData

async def save_message(message_data: MessageData):
    print(f"Got message-> {message_data}")
    pass