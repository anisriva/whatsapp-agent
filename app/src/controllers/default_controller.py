from fastapi import Request
from app.src.services.health import health_check as health
from app.src.models.api import ApiResponse

"""
$ desc   : Home api
$ route  : GET /api/v1/
$ access : PUBLIC
"""


def home(request: Request):
    return ApiResponse[str](
        data="Welcome! 🙂",
    )


"""
$ desc   : Home api
$ route  : GET /api/v1/health
$ access : PUBLIC
"""


def health_check(request: Request):
    message = "Healthy ❤️" if health() else "Unhealthy 💔"
    return ApiResponse[str](data=message)
