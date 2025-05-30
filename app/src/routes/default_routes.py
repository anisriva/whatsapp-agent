from fastapi import APIRouter
from app.src.controllers.default_controller import (
    home, 
    health_check
)

router = APIRouter()

router.get("/", tags=["default"])(home)
router.get("/health", tags=["default"])(health_check)