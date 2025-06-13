from app.src.models.api import ApiResponse
from app.src.models.messages import SendTextMessageRequest, SendPollMessageRequest
from app.src.helpers.twilio.whatsapp.send import send_text, send_healthcheckin

"""
$ desc   : send message api
$ route  : POST /api/v1/send_message
$ access : PRIVATE
"""


async def send_whatsapp_message(message_request: SendTextMessageRequest):
    res = await send_text(message_request.recipient_number, message_request.message)
    return ApiResponse(status="success", data=res)


"""
$ desc   : send message api
$ route  : POST /api/v1/send_poll
$ access : PRIVATE
"""

async def send_whatsapp_poll(message_request: SendPollMessageRequest):
    res = await send_healthcheckin(
        recipient_number=message_request.recipient_number,
    )
    return ApiResponse(status="success", data=res)
