from logging.config import dictConfig
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.append(HERE)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(module)s:%(lineno)s ~ %(message)s",
            }
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "default",
                "filename": os.path.join(HERE, "logs/registration.log"),
                "maxBytes": 10485760,
                "backupCount": 5,
            },
        },
        "root": {"level": "DEBUG", "handlers": ["file"]},
    }
)


from registry import create_app

application = create_app()
