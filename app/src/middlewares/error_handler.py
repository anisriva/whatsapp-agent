from typing import List
from fastapi import Request
from pydantic import ValidationError, BaseModel

from app.src.utils import loc_to_dot_sep
from app.src.models.api import ApiResponse, RequestStatus, HTTPStatusCode

class ErrorDetail(BaseModel):
    field: str
    message: str

async def not_found(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == HTTPStatusCode.NOT_FOUND:
        return  ApiResponse[str](
            status=RequestStatus.ERROR,
            message="Not Found",
            error="Resource not found",
            status_code=HTTPStatusCode.NOT_FOUND
        )
    return response

async def error_handler(request: Request, exc: Exception):
    return ApiResponse[str](
        status=RequestStatus.ERROR,
        message="Internal Server Error",
        error=str(exc),
        status_code=HTTPStatusCode.INTERNAL_SERVER_ERROR
    )

async def validation_error_handler(request: Request, exc: ValidationError):
    print(exc.errors())
    error_details = [
        ErrorDetail(field=loc_to_dot_sep(error["loc"]), message=error["msg"])
        for error in exc.errors()
    ]
    return ApiResponse[List[ErrorDetail]](
        status=RequestStatus.ERROR,
        message="Validation Error",
        error="Invalid input data",
        data=error_details,
        status_code=HTTPStatusCode.BAD_REQUEST
    )