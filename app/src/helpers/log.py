import logging
from app.src.config import get_log_config


class Logger:
    """
    Initializes the logger according to the
    settings.yaml
    """

    def __init__(self):
        self.__configure_logger()

    def __configure_logger(self):
        config = get_log_config()
        logger = logging.getLogger(__name__)
        logging.basicConfig(level=config["level"], format=config["format"], force=True)
        return logger
