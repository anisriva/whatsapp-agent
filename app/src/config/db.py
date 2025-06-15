from app.src.config import get_env_vars

def get_db_uri():
    db_type = get_env_vars("DB_TYPE", "sqlite")
    user = get_env_vars("DB_USER", "")
    password = get_env_vars("DB_PASSWORD", "")
    host = get_env_vars("DB_HOST", "")
    port = get_env_vars("DB_PORT", None)
    dbname = get_env_vars("DB_NAME", "")
    user_info = f"{user}:{password}@" if user and password and db_type != "sqlite" else ""
    host_info = f"{host}:{port}" if host and port is not None and db_type != "sqlite" else f"{host}" if host and db_type != "sqlite" else ""
    db_info = f"/{dbname}.db" if dbname and db_type == "sqlite" else f"/{dbname}" if dbname else ""
    return f"{db_type}://{user_info}{host_info}{db_info}"
