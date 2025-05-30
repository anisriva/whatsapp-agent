from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    status: str
    message: Optional[str] = None
    error: Optional[str] = None
    data: Optional[T] = None