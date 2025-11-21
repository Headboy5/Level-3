import logging

log = logging.getLogger()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")
log.debug("This is a debug message")
log.critical("This is a critical message")