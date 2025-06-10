from fastapi import APIRouter

from app.src.config import get_prefix
from app.src.routes.api_routes.default_routes import router as default_api_router
from app.src.routes.api_routes.messages_routes import router as messages_api_router
from app.src.routes.view_routes.default_routes import router as default_view_router

prefix = get_prefix()
if prefix and prefix != "/":
    api_router = APIRouter(prefix=prefix)
    view_router = APIRouter(prefix=prefix)
else:
    api_router = APIRouter()
    view_router = APIRouter()

api_router.include_router(default_api_router, prefix="/api/v1")
api_router.include_router(messages_api_router, prefix="/api/v1")
view_router.include_router(default_view_router)