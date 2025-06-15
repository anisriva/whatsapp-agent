from typing import Generic, TypeVar, Optional, Any
from fastapi import Response, status
from enum import Enum
import json

T = TypeVar("T")

class HTTPStatusCode(Enum):
    OK = status.HTTP_200_OK
    CREATED = status.HTTP_201_CREATED
    ACCEPTED = status.HTTP_202_ACCEPTED
    BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    FORBIDDEN = status.HTTP_403_FORBIDDEN
    NOT_FOUND = status.HTTP_404_NOT_FOUND
    INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR

class RequestStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"

class ApiResponse(Generic[T], Response):  # Removed SQLModel inheritance
    '''
    Wrapper for all responses.
    
        status : "success" | "error" (default = "success")
        status_code : HTTPStatusCode (default = "OK")
    '''
    status: Optional[RequestStatus] = RequestStatus.SUCCESS
    message: Optional[str] = None
    error: Optional[str] = None
    data: Optional[T] = None

    def __init__(
        self,
        status: RequestStatus = RequestStatus.SUCCESS,
        message: Optional[str] = None,
        error: Optional[str] = None,
        data: Optional[T] = None,
        status_code: HTTPStatusCode = HTTPStatusCode.OK,
        **kwargs: Any
    ):
        self.status = status
        self.message = message
        self.error = error
        self.data = data
        content = json.dumps(self.to_dict(), ensure_ascii=False)
        super().__init__(content=content, status_code=status_code.value, **kwargs)

    def to_dict(self) -> dict:
        return {
            "status": self.status.value,
            "message": self.message,
            "error": self.error,
            "data": self.data
        }