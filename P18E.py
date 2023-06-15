import logging

# Configure the logging module
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger(__name__)

# Log some messages
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")