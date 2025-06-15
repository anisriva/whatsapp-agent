import logging
from app.src.models.messages import MessageData
from app.src.connectors.db import get_session
from typing import Tuple, Union


async def save_message(message_data: MessageData) -> Tuple[bool, Union[None, str]]:
    status = False
    error = None
    try:
        session = get_session()
        logging.debug(f"Got message : {message_data}")
        session.add(message_data)
        session.commit()
        status = True
    except Exception as e:
        session.rollback()
        logging.error(e)
        status = False
        error = str(e)
    finally:
        session.close()
        return status, error
