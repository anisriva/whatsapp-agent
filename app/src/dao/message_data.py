import logging
from app.src.models.messages import MessageData
from app.src.connectors.db import get_session

async def save_message(message_data: MessageData) -> bool:
    status = False
    message = ""
    try:
        session = get_session()
        logging.debug(f"Got message : {message_data}")
        session.add(message_data)
        session.commit()
        status = True
    except Exception as e:
        session.rollback()
        message = f"Error saving message: {e}"
        logging.error(message)
    finally:
        session.close()
        return (status, message)