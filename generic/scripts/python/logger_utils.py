import logging
from pathlib import Path


def configure_logger(log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Create and configure a logger that writes to a file."""
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(log_file)
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_message(log_file: str, level: int, message: str) -> None:
    """Log a message to a file at the provided logging level."""
    logger = configure_logger(log_file, level)
    logger.log(level, message)
