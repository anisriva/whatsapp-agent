from fastapi.templating import Jinja2Templates
from app.src.config import get_root_path, get_env_vars, get_log_config

def get_app_config():
    return {
        "openapi_url": "/api/openapi.json",
        "docs_url": "/api/docs",
        "root_path": get_root_path(),
    }

def get_server_config():
    return {
        "host": "0.0.0.0",
        "port": int(get_env_vars("PORT", 8000)),
        "workers": int(get_env_vars("WORKERS", 1)),
        "http": "h11",
        "forwarded_allow_ips": "*",
        "reload": False if get_env_vars("ENV") == "production" else True,
        "log_level": get_log_config()["level"].lower(),
    }

def get_templates():
    return Jinja2Templates(directory="app/src/templates")

