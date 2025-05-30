import os
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

def get_env_vars(key, fallback=None):
    return env_vars.get(key, fallback)

def get_log_config():
    return {
        "level": "ERROR" if get_env_vars("ENV") == "production" else "INFO",
        "format": "{%(asctime)s | %(levelname)s | %(message)s}",
    }

def get_prefix():
    return get_env_vars("PREFIX", None)

def get_root_path():
    return get_env_vars("ROOT_PATH", None)

def get_app_config():
    return {
        "openapi_url": "/v1/api/openapi.json",
        "docs_url": "/v1/api/docs",
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

def get_db_uri():
    db_type = get_env_vars("DB_TYPE", "sqlite")
    user = get_env_vars("DB_USER", "")
    password = get_env_vars("DB_PASSWORD", "")
    host = get_env_vars("DB_HOST", "")
    port = get_env_vars("DB_PORT", "")
    dbname = get_env_vars("DB_NAME", "")
    user_info = f"{user}:{password}@" if user and password else ""
    host_info = f"{host}:{port}" if host and port else ""
    db_info = f"/{dbname}" if dbname else ""

    return f"{db_type}://{user_info}{host_info}{db_info}"
