import logging
from logging.handlers import RotatingFileHandler
import sys
import os

# Create a custom logger
logger = logging.getLogger("my_app")

# Set the level of this logger.
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
# Use platform-independent path for log file
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'visualizer.log')
file_handler = RotatingFileHandler(log_path, maxBytes=500000, backupCount=10)


# Set the level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Custom exception handler to log unhandled exceptions
def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    logger.error("Unhandled Exception: ", exc_info=(exc_type, exc_value, exc_traceback))


# Set the custom exception handler
sys.excepthook = log_unhandled_exception
