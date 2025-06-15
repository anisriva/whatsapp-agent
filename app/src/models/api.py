from typing import Generic, TypeVar, Optional
from sqlmodel import SQLModel

T = TypeVar('T')

class ApiResponse(SQLModel, Generic[T]):
    status: str
    message: Optional[str] = None
    error: Optional[str] = None
    data: Optional[T] = None