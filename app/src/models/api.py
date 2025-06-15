from enum import Enum
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any
from fastapi import Response, status

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

class ApiResponseModel(BaseModel, Generic[T]):
    """
    Pydantic model for API response structure.
    Handles serialization automatically including enums and complex types.
    """
    status: RequestStatus = RequestStatus.SUCCESS
    message: Optional[str] = None
    error: Optional[str] = None
    data: Optional[T] = None

    class Config:
        # Automatically serialize enums by their value
        use_enum_values = True
        # Allow arbitrary types (useful for complex generics)
        arbitrary_types_allowed = True

class ApiResponse(Response, Generic[T]):
    """
    FastAPI Response wrapper with automatic serialization.
    Uses Pydantic for seamless handling of complex types and enums.
    """
    def __init__(
        self,
        status: RequestStatus = RequestStatus.SUCCESS,
        message: Optional[str] = None,
        error: Optional[str] = None,
        data: Optional[T] = None,
        status_code: HTTPStatusCode = HTTPStatusCode.OK,
        **kwargs: Any
    ):
        # Create the response model
        response_model = ApiResponseModel[T](
            status=status,
            message=message,
            error=error,
            data=data
        )
        # Use Pydantic's built-in serialization
        content = response_model.model_dump_json(exclude_none=False)
        super().__init__(
            content=content,
            status_code=status_code.value,
            media_type="application/json",
            **kwargs
        )