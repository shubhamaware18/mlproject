# Import necessary modules
import logging  # For logging capabilities
import os  # For file system operations
from datetime import datetime  # For date and time operations


# Define a log file name using the current date and time
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# Define the path where the log file will be stored
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# Ensure the directory structure exists, creating it if necessary
os.makedirs(logs_path, exist_ok=True)

# Define the full path of the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the file where logs will be written
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the log format
    level=logging.INFO,  # Set the logging level to INFO
)