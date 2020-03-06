import logging

log = logging.getLogger(__name__)

def run():
    log.info("abc!", extra={"sessionId": 3})
    log.warning("k!", extra={"mbbb": 3})
    log.error("Error")
