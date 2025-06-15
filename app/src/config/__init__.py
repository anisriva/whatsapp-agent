import os
from dotenv import load_dotenv

load_dotenv(".env", override=True)

def get_env_vars(key, fallback=None):
    return os.getenv(key, fallback)

def get_log_config():
    return {
        "level": "ERROR" if get_env_vars("ENV") == "production" else "DEBUG",
        "format": "{%(asctime)s | %(levelname)s | %(message)s}",
    }

def get_prefix():
    return get_env_vars("PREFIX", None)

def get_root_path():
    return get_env_vars("ROOT_PATH", None)