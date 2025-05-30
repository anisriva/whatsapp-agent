from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError, BaseModel
from typing import List

from app.src.utils import loc_to_dot_sep
from app.src.models.api import ApiResponse

class ErrorDetail(BaseModel):
    field: str
    message: str
    
class KafkaException(Exception):
    msg="Something's wrong with the consumer"

async def not_found(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        error_response = ApiResponse[str](
            status="error",
            message="Not Found",
            error="Resource not found"
        )
        return JSONResponse(content=error_response.model_dump(), status_code=404)
    return response

async def error_handler(request: Request, exc: Exception):
    error_response = ApiResponse[str](
        status="error",
        message="Internal Server Error",
        error=str(exc)
    )
    return JSONResponse(content=error_response.model_dump(), status_code=500)

async def validation_error_handler(request: Request, exc: ValidationError):
    error_details = [
        ErrorDetail(field=loc_to_dot_sep(error["loc"]), message=error["msg"])
        for error in exc.errors()
    ]
    error_response = ApiResponse[List[ErrorDetail]](
        status="error",
        message="Validation Error",
        error="Invalid input data",
        data=error_details
    )
    return JSONResponse(content=error_response.model_dump(), status_code=400)