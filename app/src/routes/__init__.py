from fastapi import APIRouter

from app.src.config import get_prefix
from app.src.routes.default_routes import router as default_router

prefix = get_prefix()
if prefix and prefix != "/":
    api_router = APIRouter(prefix=prefix)
else:
    api_router = APIRouter()

api_router.include_router(default_router, prefix="/api/v1")