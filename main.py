import logging
import logging.config
from logging import BASIC_FORMAT


#logging.basicConfig(level=logging.INFO)
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {"format": BASIC_FORMAT},
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(sessionId)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "NOTSET",
            "formatter": "json",
            "stream": "ext://sys.stdout",
        }
    },
    "root": {
        "level": "INFO",
    },
    "loggers": {
        "ml": {"level": "NOTSET", "handlers": ["console"]},
    }
})

# from logging_tree import printout
# printout()

import ml.server

def app(environ, start_response):
    start_response("200 OK", [])
    ml.server.run()
    return [b'hello']
