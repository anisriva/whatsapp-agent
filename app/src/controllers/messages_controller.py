from app.src.models.api import ApiResponse
from app.src.models.messages import MessageSendRequest
from app.src.helpers.twilio.whatsapp import send_whatsapp_message

'''
$ desc   : send message api
$ route  : POST /api/v1/send_message
$ access : PRIVATE
'''
async def send_message(message_request : MessageSendRequest):
    res = await send_whatsapp_message(message_request.to, message_request.content)
    return ApiResponse(status="success", message=res)