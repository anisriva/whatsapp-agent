from fastapi import Request
from app.src.models.messages import MessageData
from app.src.models.api import ApiResponse, HTTPStatusCode, RequestStatus
from app.src.models.messages import SendTextMessageRequest, SendPollMessageRequest
from app.src.helpers.twilio.whatsapp.send import send_text, send_healthcheckin
from app.src.helpers.twilio.whatsapp.receive import create_message_data
from app.src.dao.message_data import save_message

"""
$ desc   : send message api
$ route  : POST /api/v1/twilio/send_message
$ access : PRIVATE
"""


async def send_whatsapp_message(message_request: SendTextMessageRequest):
    res = await send_text(message_request.recipient_number, message_request.message)
    return ApiResponse(data=res)


"""
$ desc   : send message api
$ route  : POST /api/v1/twilio/send_poll
$ access : PRIVATE
"""


async def send_whatsapp_poll(message_request: SendPollMessageRequest):
    res = await send_healthcheckin(
        recipient_number=message_request.recipient_number,
    )
    return ApiResponse[str](data=res)


"""
$ desc   : recieve messages
$ route  : POST /api/v1/twilio/recieve_message
$ access : PRIVATE
"""


async def receive_whatsapp_message(request: Request):

    # Get form data from Twilio webhook
    form_data = await request.form()

    # Extract message details from Twilio webhook payload
    message_data = create_message_data(form_data)
    
    # Save message to db
    status, error = await save_message(message_data)
    return ApiResponse[MessageData](
        status_code=HTTPStatusCode.INTERNAL_SERVER_ERROR if not status else HTTPStatusCode.CREATED,
        status=RequestStatus.ERROR if not status else RequestStatus.SUCCESS,
        error = error,
        data = message_data
    )