from fastapi import Request
from app.src.services.health import health_check as health
from app.src.models.api import ApiResponse

'''
$ desc   : Home api
$ route  : GET /v1/api/
$ access : PUBLIC
'''
def home(request : Request):
    return ApiResponse[str](
        status="success",
        data="Welcome! What server side query you want to run today 🙂",
    )

'''
$ desc   : Home api
$ route  : GET /v1/api/health
$ access : PUBLIC
'''    
def health_check(request : Request):
    message = "Healthy ❤️" if health() else "Unhealthy 💔"
    return ApiResponse[str](
        status="success",
        data=message
    )