from app.src.config import get_env_vars, get_log_config


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