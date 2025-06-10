import uvicorn

from app.src.helpers.log import Logger
from app.src.config.server import get_server_config

logger = Logger()

if __name__ == "__main__":
    serv_config = get_server_config()
    uvicorn.run("app.app:app", **serv_config)
