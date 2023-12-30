import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logs.log")

# Create log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Logs to a file
        logging.StreamHandler(sys.stdout)  # Logs to console
    ]
)

# Create a custom logger
logger = logging.getLogger('erslogger')
