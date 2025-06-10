from fastapi import FastAPI, Depends
from pydantic import ValidationError
from app.src.routes import api_router, view_router
from app.src.middlewares.error_handler import (
    not_found,
    error_handler,
    validation_error_handler,
)

from app.src.config.app import get_app_config
from app.src.connectors.db import get_session

fast_api_config = get_app_config()

app = FastAPI(
    root_path=fast_api_config["root_path"],
    openapi_url=fast_api_config["openapi_url"],
    docs_url=fast_api_config["docs_url"],
    redoc_url=None,
)

# Register routes from router aggregator
app.include_router(api_router, dependencies=[Depends(get_session)])
app.include_router(view_router, dependencies=[Depends(get_session)])

# Middlewares
app.middleware("http")(not_found)

# Exception handling
app.add_exception_handler(ValidationError, validation_error_handler)
app.add_exception_handler(Exception, error_handler)
