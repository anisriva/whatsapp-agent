from fastapi import APIRouter
from app.src.views.default_view import (
    home_view
)

router = APIRouter()

router.get("/", tags=["default"])(home_view)