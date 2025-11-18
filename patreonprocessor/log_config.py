# logging_config.py
import logging
import sys

def setup_logging(level=logging.INFO, logfile="patreonParser.log"):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(logfile)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger("patreonparser")
    root_logger.setLevel(level)
    root_logger.handlers = []  # Clear existing handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    return



