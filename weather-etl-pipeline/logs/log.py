import logging
import os

def get_logger(name="weather_etl"):
    """
    Creates and configures a reusable logger for the ETL pipeline.
    Logs are written to logs/pipeline.log.
    """

    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is reused
    if not logger.handlers:
        handler = logging.FileHandler("logs/pipeline.log")

        # Log format includes timestamp, level, and message
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger